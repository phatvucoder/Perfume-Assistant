from flask import Flask, render_template, request, jsonify, g
import sqlite3
import os
from jinja2 import DictLoader

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "perfumes.db")

# Hàm lấy kết nối CSDL với cấu hình row_factory cho dict
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

# Đóng kết nối CSDL khi kết thúc request
@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Hàm hỗ trợ truy vấn CSDL
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# ------------------- Định nghĩa các template -------------------

base_template = """
<!doctype html>
<html lang="vi">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Quản lý Fragrance & Inventory</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/dataTables.bootstrap5.min.css"/>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- DataTables JS -->
    <script type="text/javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.13.4/js/dataTables.bootstrap5.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <style>
      td[contenteditable="true"] {
        border: 1px dashed #ccc;
      }
    </style>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-3">
      <div class="container-fluid">
        <a class="navbar-brand" href="{{ url_for('home') }}">Perfume Manager</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('fragrances') }}">Fragrance Collection</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('inventory') }}">Inventory</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container">
      {% block content %}{% endblock %}
    </div>
  </body>
</html>
"""

home_template = """
{% extends "base.html" %}
{% block content %}
<div class="jumbotron">
  <h1 class="display-4">Chào mừng đến với Perfume Manager</h1>
  <p class="lead">Chọn mục bên trên để quản lý Fragrance Collection hoặc Inventory.</p>
  <hr class="my-4">
  <p>Sử dụng giao diện bên trên để xem thông tin nước hoa và quản lý tồn kho.</p>
</div>
{% endblock %}
"""

fragrances_template = """
{% extends "base.html" %}
{% block content %}
<h2>Fragrance Collection</h2>
{% if fragrances %}
<table id="fragranceTable" class="table table-bordered table-striped">
  <thead>
    <tr>
      {% for key in fragrances[0].keys() %}
      <th>{{ key }}</th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for f in fragrances %}
    <tr>
      {% for value in f.values() %}
      <td>{{ value }}</td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>
<script>
  $(document).ready(function(){
    $('#fragranceTable').DataTable();
  });
</script>
{% else %}
<p>Chưa có dữ liệu về nước hoa.</p>
{% endif %}
{% endblock %}
"""

# Template Inventory: cho phép inline editing với nút Save và Undo
inventory_template = """
{% extends "base.html" %}
{% block content %}
<h2>Inventory</h2>
<button class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#addInventoryModal">Thêm Sản Phẩm</button>
<table id="inventoryTable" class="table table-bordered table-striped">
  <thead>
    <tr>
      <th>ID</th>
      <th>Brand</th>
      <th>Name</th>
      <th>Quantity</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {% for item in inventory %}
    <tr data-brand="{{ item['Brand'] }}" data-name="{{ item['Name'] }}">
      <td>{{ loop.index }}</td>
      <td contenteditable="true" data-field="Brand">{{ item['Brand'] }}</td>
      <td contenteditable="true" data-field="Name">{{ item['Name'] }}</td>
      <td contenteditable="true" data-field="Quantity">{{ item['Quantity'] }}</td>
      <td>
        <button class="btn btn-sm btn-success save-btn"
                data-brand="{{ item['Brand'] }}"
                data-name="{{ item['Name'] }}">Save</button>
        <button class="btn btn-sm btn-warning undo-btn"
                data-brand="{{ item['Brand'] }}"
                data-name="{{ item['Name'] }}">Undo</button>
        <button class="btn btn-sm btn-danger delete-btn"
                data-brand="{{ item['Brand'] }}"
                data-name="{{ item['Name'] }}">Xoá</button>
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<script>
  $(document).ready(function(){
    console.log("Document ready");
    
    // Initialize DataTable với rowReorder
    var table = $('#inventoryTable').DataTable({
      drawCallback: function() {
        // Cập nhật lại giá trị ban đầu sau khi table được vẽ lại
        $('#inventoryTable tbody tr').each(function(){
          $(this).find('td[contenteditable="true"]').each(function(){
            $(this).attr('data-original', $(this).text().trim());
          });
        });
        
        // Log số lượng buttons sau khi table được vẽ lại
        console.log("After draw - Save buttons:", $('#inventoryTable .save-btn').length);
        console.log("After draw - Delete buttons:", $('#inventoryTable .delete-btn').length);
        console.log("After draw - Undo buttons:", $('#inventoryTable .undo-btn').length);
      }
    });
    
    // Xử lý sự kiện khi nhấn nút Save - sử dụng event delegation
    $('#inventoryTable tbody').on('click', '.save-btn', function(e){
      e.preventDefault();
      console.log("Save button clicked");
      
      var button = $(this);
      var row = button.closest("tr");
      var originalBrand = button.data("brand");
      var originalName = button.data("name");
      
      console.log("Button data:", {
        originalBrand: originalBrand,
        originalName: originalName
      });
      
      if (!originalBrand || !originalName) {
        alert("Lỗi: Không tìm thấy thông tin sản phẩm");
        console.error("Missing original data", button.data());
        return;
      }
      
      var newBrand = row.find('td[data-field="Brand"]').text().trim();
      var newName = row.find('td[data-field="Name"]').text().trim();
      var quantity = row.find('td[data-field="Quantity"]').text().trim();

      console.log("New values:", {
        newBrand: newBrand,
        newName: newName,
        quantity: quantity
      });

      // Kiểm tra các trường bắt buộc
      if (!newBrand || !newName) {
        alert("Lỗi: Brand và Name không được để trống");
        return;
      }

      // Kiểm tra định dạng: Quantity phải là số và không âm
      if(isNaN(quantity) || parseInt(quantity) < 0){
        alert("Lỗi: Quantity phải là số không âm.");
        return;
      }
      
      // Convert quantity to integer
      quantity = parseInt(quantity);
      
      var data = {
        "original": {
          "Brand": originalBrand,
          "Name": originalName
        },
        "updated": {
          "Brand": newBrand,
          "Name": newName,
          "Quantity": quantity
        }
        "Quantity": quantity
      };

      console.log("Sending data:", data);

      // Deep validation of data object
      console.log("Data validation:", {
        id: {
          value: data.id,
          type: typeof data.id,
          isNumber: !isNaN(data.id)
        },
        brand: {
          value: data.Brand,
          type: typeof data.Brand,
          length: data.Brand.length
        },
        name: {
          value: data.Name,
          type: typeof data.Name,
          length: data.Name.length
        },
        quantity: {
          value: data.Quantity,
          type: typeof data.Quantity,
          isNumber: !isNaN(data.Quantity)
        }
      });

      var jsonData = JSON.stringify(data);
      console.log("Stringified data:", jsonData);

      var data = {
        "original": {
          "Brand": originalBrand,
          "Name": originalName
        },
        "updated": {
          "Brand": newBrand,
          "Name": newName,
          "Quantity": parseInt(quantity)
        }
      };
      
      console.log("Sending data to server:", data);
      
      // Disable the button during update
      button.prop('disabled', true);
      
      $.ajax({
        url: "/api/inventory/update",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(response) {
          console.log("Server response:", response);
          // Update the data attributes with new values
          button.data("brand", newBrand);
          button.data("name", newName);
          
          // Update row's data attributes
          row.data("brand", newBrand);
          row.data("name", newName);
          
          // Update the original values for undo
          row.find('td[contenteditable="true"]').each(function(){
            $(this).attr('data-original', $(this).text().trim());
          });
          
          alert("Cập nhật thành công!");
        },
        error: function(xhr, status, error) {
          console.error("Update failed:", {
            status: xhr.status,
            error: error,
            response: xhr.responseText
          });
          
          let errorMessage = "Lỗi khi cập nhật";
          try {
            const response = JSON.parse(xhr.responseText);
            errorMessage = response.message || errorMessage;
          } catch (e) {
            console.error("Error parsing response:", e);
          }
          
          alert(errorMessage);
          
          // Revert the values in case of error
          row.find('td[contenteditable="true"]').each(function(){
            $(this).text($(this).attr('data-original'));
          });
        },
        complete: function() {
          // Re-enable the button
          button.prop('disabled', false);
        }
      });
    });

    // Xử lý sự kiện khi nhấn nút Undo để khôi phục giá trị ban đầu
    $("#inventoryTable").on("click", ".undo-btn", function(){
      var row = $(this).closest("tr");
      row.find('td[contenteditable="true"]').each(function(){
        $(this).text($(this).attr('data-original'));
      });
    });

    // Xoá sản phẩm khỏi Inventory
    $('#inventoryTable tbody').on('click', '.delete-btn', function(e){
      e.preventDefault();
      console.log("Delete button clicked");
      
      var button = $(this);
      var row = button.closest('tr');
      var brand = button.data("brand");
      var name = button.data("name");
      
      console.log("Delete request for:", {brand, name});
      
      if (!brand || !name) {
        console.error("Missing product info:", {brand, name});
        alert("Lỗi: Không tìm thấy thông tin sản phẩm");
        return;
      }
      
      if (!confirm(`Bạn có chắc chắn muốn xoá sản phẩm "${brand} - ${name}"?`)) {
        return;
      }
      
      // Disable button during delete operation
      button.prop('disabled', true);
      
      $.ajax({
        url: "/api/inventory/delete",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
          "Brand": brand,
          "Name": name
        }),
        success: function(response){
          console.log("Delete successful:", response);
          // Remove the row from DataTable
          var table = $('#inventoryTable').DataTable();
          table.row(row).remove().draw();
        },
        error: function(xhr, status, error) {
          console.error("Delete failed:", {
            status: xhr.status,
            error: error,
            response: xhr.responseText
          });
          
          let errorMessage = "Lỗi khi xoá";
          try {
            const response = JSON.parse(xhr.responseText);
            errorMessage = response.message || errorMessage;
          } catch (e) {
            console.error("Error parsing response:", e);
          }
          alert("Lỗi khi xoá: " + errorMessage);
        },
        complete: function() {
          // Re-enable the button
          button.prop('disabled', false);
        }
      });
    });
  });
</script>

<!-- Modal Thêm Inventory -->
<div class="modal fade" id="addInventoryModal" tabindex="-1" aria-labelledby="addInventoryModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <form id="addInventoryForm">
        <div class="modal-header">
          <h5 class="modal-title" id="addInventoryModalLabel">Thêm Sản Phẩm vào Inventory</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Đóng"></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="invFragranceSelect" class="form-label">Chọn nước hoa</label>
            <select class="form-select" id="invFragranceSelect" required>
              <option value="">-- Chọn nước hoa --</option>
              {% for f in fragrances %}
              <option value="{{ f['id'] }}" data-name="{{ f['Name'] }}" data-brand="{{ f['Brand'] }}">
                {{ f['Brand'] }} - {{ f['Name'] }}
              </option>
              {% endfor %}
            </select>
          </div>
          <div class="mb-3">
            <label for="invBrand" class="form-label">Brand</label>
            <input type="text" class="form-control" id="invBrand" name="Brand" readonly>
          </div>
          <div class="mb-3">
            <label for="invName" class="form-label">Name</label>
            <input type="text" class="form-control" id="invName" name="Name" readonly>
          </div>
          <div class="mb-3">
            <label for="invQuantity" class="form-label">Quantity</label>
            <input type="number" class="form-control" id="invQuantity" name="Quantity" value="1" required>
          </div>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary">Thêm</button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Hủy</button>
        </div>
      </form>
    </div>
  </div>
</div>

<script>
  // Khi chọn nước hoa, tự động điền Brand và Name
  $("#invFragranceSelect").on("change", function(){
    var selected = $(this).find("option:selected");
    var name = selected.data("name") || "";
    var brand = selected.data("brand") || "";
    $("#invName").val(name);
    $("#invBrand").val(brand);
  });

  // Gửi form thêm Inventory
  $("#addInventoryForm").on("submit", function(e){
    e.preventDefault();
    var data = {
      "Brand": $("#invBrand").val(),
      "Name": $("#invName").val(),
      "Quantity": $("#invQuantity").val()
    };
    $.ajax({
      url: "/api/inventory/add",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(data),
      success: function(res){
        location.reload();
      },
      error: function(xhr, status, error) {
        alert("Lỗi khi thêm sản phẩm: " + error);
      }
    });
  });
</script>
{% endblock %}
"""


# ------------------- Thiết lập loader cho Jinja2 -------------------
app.jinja_loader = DictLoader({
    "base.html": base_template,
    "home.html": home_template,
    "fragrances.html": fragrances_template,
    "inventory.html": inventory_template
})

# ------------------- Các route -------------------

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/fragrances')
def fragrances():
    db = get_db()
    rows = db.execute("SELECT * FROM fragrance_collection").fetchall()
    fragrances = [dict(row) for row in rows]
    return render_template("fragrances.html", fragrances=fragrances)

@app.route('/inventory')
def inventory():
    db = get_db()
    inv_rows = db.execute("SELECT * FROM inventory").fetchall()
    inventory_data = [dict(row) for row in inv_rows]
    frag_rows = db.execute("SELECT * FROM fragrance_collection").fetchall()
    fragrances = [dict(row) for row in frag_rows]
    return render_template("inventory.html", inventory=inventory_data, fragrances=fragrances)

# --- API cho Fragrance Collection ---
@app.route('/api/fragrance/add', methods=["POST"])
def api_add_fragrance():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    keys = list(data.keys())
    placeholders = ", ".join("?" for _ in keys)
    columns = ", ".join(keys)
    values = tuple(data[k] for k in keys)
    try:
        db = get_db()
        db.execute(f"INSERT INTO fragrance_collection ({columns}) VALUES ({placeholders})", values)
        db.commit()
        return jsonify({"status": "success", "message": "Fragrance added."})
    except Exception as e:
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fragrance/update', methods=["POST"])
def api_update_fragrance():
    data = request.get_json()
    record_id = data.get("id")
    if not record_id:
        return jsonify({"status": "error", "message": "Missing id"}), 400
    fields = [f"{k} = ?" for k in data if k != "id"]
    values = [data[k] for k in data if k != "id"]
    values.append(record_id)
    try:
        db = get_db()
        db.execute(f"UPDATE fragrance_collection SET {', '.join(fields)} WHERE id = ?", values)
        db.commit()
        return jsonify({"status": "success", "message": "Fragrance updated."})
    except Exception as e:
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/fragrance/delete', methods=["POST"])
def api_delete_fragrance():
    data = request.get_json()
    record_id = data.get("id")
    if not record_id:
        return jsonify({"status": "error", "message": "Missing id"}), 400
    try:
        db = get_db()
        db.execute("DELETE FROM fragrance_collection WHERE id = ?", (record_id,))
        db.commit()
        return jsonify({"status": "success", "message": "Fragrance deleted."})
    except Exception as e:
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

# --- API cho Inventory ---
@app.route('/api/inventory/add', methods=["POST"])
def api_add_inventory():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    keys = list(data.keys())
    placeholders = ", ".join("?" for _ in keys)
    columns = ", ".join(keys)
    values = tuple(data[k] for k in keys)
    try:
        db = get_db()
        db.execute(f"INSERT INTO inventory ({columns}) VALUES ({placeholders})", values)
        db.commit()
        return jsonify({"status": "success", "message": "Inventory item added."})
    except Exception as e:
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/inventory/update', methods=["POST"])
def api_update_inventory():
    print("\n=== Inventory Update Request ===")
    print("Request Headers:", dict(request.headers))
    print("Request Data:", request.get_data(as_text=True))
    
    if not request.is_json:
        print("Error: Content-Type is not application/json")
        return jsonify({"status": "error", "message": "Content-Type must be application/json"}), 400
        
    try:
        data = request.get_json()
        print("Parsed JSON data:", data)
    except Exception as e:
        print("Error parsing JSON:", str(e))
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
        
    original = data.get("original")
    updated = data.get("updated")
    
    if not original or not updated:
        print("Error: Missing original or updated data")
        return jsonify({"status": "error", "message": "Missing data structure"}), 400
        
    required_fields = ["Brand", "Name"]
    for field in required_fields:
        if field not in original or field not in updated:
            print(f"Error: Missing required field '{field}'")
            return jsonify({"status": "error", "message": f"Missing {field}"}), 400
            
    try:
        # Validate quantity is a number
        quantity = updated.get("Quantity")
        if quantity is None:
            print("Error: Missing Quantity")
            return jsonify({"status": "error", "message": "Missing Quantity"}), 400
            
        if isinstance(quantity, str):
            quantity = int(quantity.strip())
        else:
            quantity = int(quantity)
            
        if quantity < 0:
            print("Error: Negative quantity")
            return jsonify({"status": "error", "message": "Quantity must be non-negative"}), 400
        
        updated["Quantity"] = quantity
        print("Converted quantity:", quantity)
    except (ValueError, TypeError) as e:
        print("Error converting quantity:", str(e))
        return jsonify({"status": "error", "message": "Quantity must be a valid number"}), 400
    
    try:
        db = get_db()
        # Update using Brand and Name as composite key
        sql = """UPDATE inventory
                SET Brand = ?, Name = ?, Quantity = ?
                WHERE Brand = ? AND Name = ?"""
        values = (updated["Brand"], updated["Name"], updated["Quantity"],
                 original["Brand"], original["Name"])
                 
        print("SQL Query:", sql)
        print("Values:", values)
        
        cursor = db.execute(sql, values)
        if cursor.rowcount == 0:
            db.rollback()
            print("Error: No matching record found")
            return jsonify({"status": "error", "message": "No matching record found"}), 404
            
        db.commit()
        print("Update successful")
        return jsonify({"status": "success", "message": "Inventory item updated."})
    except Exception as e:
        print("Database error:", str(e))
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/inventory/delete', methods=["POST"])
def api_delete_inventory():
    print("\n=== Inventory Delete Request ===")
    print("Request Data:", request.get_data(as_text=True))
    
    if not request.is_json:
        return jsonify({"status": "error", "message": "Content-Type must be application/json"}), 400
        
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"status": "error", "message": "Invalid JSON data"}), 400
    
    brand = data.get("Brand")
    name = data.get("Name")
    
    if not brand or not name:
        return jsonify({"status": "error", "message": "Missing Brand or Name"}), 400
        
    try:
        db = get_db()
        sql = "DELETE FROM inventory WHERE Brand = ? AND Name = ?"
        cursor = db.execute(sql, (brand, name))
        
        if cursor.rowcount == 0:
            db.rollback()
            return jsonify({"status": "error", "message": "No matching record found"}), 404
            
        db.commit()
        return jsonify({"status": "success", "message": "Inventory item deleted."})
    except Exception as e:
        print("Database error:", str(e))
        db.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
