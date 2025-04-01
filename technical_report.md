# LỜI CẢM ƠN

Trong quá trình tìm hiểu và nghiên cứu về trí tuệ nhân tạo, đặc biệt là xử lý ngôn ngữ tự nhiên, chúng em đã lựa chọn đề tài "Xây dựng chương trình hỏi đáp bằng ngôn ngữ tự nhiên (Chatbot)" để thực hiện bài tập lớn.

Đề tài này được thực hiện dựa trên quá trình tự tìm hiểu, nghiên cứu tài liệu và áp dụng các kiến thức đã học vào thực tế. Trong suốt quá trình thực hiện, chúng em đã gặp không ít khó khăn, nhưng nhờ sự nỗ lực không ngừng và tinh thần làm việc nhóm, chúng em đã hoàn thành đề tài theo kế hoạch đề ra.

Mặc dù đã cố gắng thực hiện một cách cẩn thận và kỹ lưỡng nhất, bài báo cáo này khó tránh khỏi những thiếu sót. Chúng em rất mong nhận được những ý kiến đóng góp quý báu để có thể hoàn thiện hơn.

Chúng em xin chân thành cảm ơn!

Thành phố Hồ Chí Minh, tháng 4 năm 2025

Nhóm sinh viên thực hiện

# MỤC LỤC

**CHƯƠNG 1: GIỚI THIỆU**
- 1.1. Đặt vấn đề
- 1.2. Mục tiêu nghiên cứu
- 1.3. Đối tượng và phạm vi nghiên cứu
- 1.4. Phương pháp nghiên cứu
- 1.5. Đóng góp mới của đề tài
- 1.6. Cấu trúc báo cáo

**CHƯƠNG 2: TỔNG QUAN CƠ SỞ LÝ THUYẾT**
- 2.1. Tổng quan về Chatbot và Trợ lý ảo
- 2.2. Mô hình Ngôn ngữ lớn (Large Language Models - LLMs)
    - 2.2.1. Giới thiệu chung
    - 2.2.2. Kiến trúc Transformer
    - 2.2.3. Giới thiệu về dòng mô hình Qwen và lý do lựa chọn Qwen2.5-1.5B
- 2.3. Kỹ thuật Tinh chỉnh Mô hình Ngôn ngữ lớn (Fine-tuning)
    - 2.3.1. So sánh Full Fine-tuning và Parameter-Efficient Fine-tuning (PEFT)
    - 2.3.2. Kỹ thuật LoRA (Low-Rank Adaptation)
    - 2.3.3. Kỹ thuật Lượng tử hóa (Quantization) và BitsAndBytes
- 2.4. Kiến trúc Retrieval-Augmented Generation (RAG)
    - 2.4.1. Khái niệm và vai trò
    - 2.4.2. Vector Database và tìm kiếm ngữ nghĩa (FAISS)
    - 2.4.3. Tích hợp Cơ sở dữ liệu Quan hệ (SQLite) trong RAG
- 2.5. Framework Phát triển Ứng dụng LLM: LangChain
- 2.6. Framework Xây dựng Giao diện Người dùng Chat: Chainlit

**CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG**
- 3.1. Phân tích bài toán và yêu cầu
    - 3.1.1. Mục đích và bối cảnh bài toán
    - 3.1.2. Yêu cầu chức năng
    - 3.1.3. Yêu cầu phi chức năng
- 3.2. Phương pháp thực hiện và Đóng góp của Nhóm
    - 3.2.1. Phương pháp tiếp cận tổng thể
    - 3.2.2. Đóng góp về xây dựng và công bố bộ dữ liệu chuyên ngành nước hoa
    - 3.2.3. Đóng góp về tinh chỉnh và tối ưu mô hình LLM cho lĩnh vực cụ thể
- 3.3. Lựa chọn Công nghệ và Ngôn ngữ sử dụng
    - 3.3.1. Ngôn ngữ lập trình chính: Python
    - 3.3.2. Các thư viện và Framework chủ chốt
- 3.4. Thiết kế Cơ sở Dữ liệu và Kiến thức
    - 3.4.1. Dataset Huấn luyện chuyên ngành (phatvucoder/perfume-assistant)
    - 3.4.2. Dataset Thông tin Sản phẩm (fragrance_collection.csv)
    - 3.4.3. Dataset Quản lý Tồn kho (inventory.csv)
    - 3.4.4. Thiết kế Lưu trữ Vector (FAISS Index)
    - 3.4.5. Thiết kế Cơ sở dữ liệu Quan hệ (SQLite)
- 3.5. Thiết kế Kiến trúc Hệ thống Tổng thể
- 3.6. Thiết kế Luồng Xử lý Chi tiết (Workflow/Chain)
    - 3.6.1. Sơ đồ luồng tổng quát
    - 3.6.2. Mô tả chi tiết các thành phần (Nodes) trong luồng

**CHƯƠNG 4: TRIỂN KHAI THỰC NGHIỆM**
- 4.1. Môi trường Triển khai
- 4.2. Quá trình Xử lý và Chuẩn bị Dữ liệu
    - 4.2.1. Xây dựng và chuẩn hóa Dataset Huấn luyện
    - 4.2.2. Xử lý và tích hợp Dataset Sản phẩm
    - 4.2.3. Tạo Dataset Tồn kho
- 4.3. Quá trình Fine-tuning Mô hình Qwen2.5-1.5B với LoRA
    - 4.3.1. Chi tiết cấu hình (Quantization, LoRA, SFTConfig)
    - 4.3.2. Tiến trình huấn luyện và kết quả
    - 4.3.3. Merge Adapter LoRA và Lưu trữ Mô hình
- 4.4. Xây dựng Knowledge Bases
    - 4.4.1. Tạo FAISS Index từ dữ liệu sản phẩm
    - 4.4.2. Tạo và nạp dữ liệu vào SQLite Database
- 4.5. Triển khai Luồng Xử lý với LangChain
- 4.6. Xây dựng Giao diện Người dùng với Chainlit
- 4.7. Một số Giao diện và Kết quả Chạy thử nghiệm

**CHƯƠNG 5: ĐÁNH GIÁ KẾT QUẢ**
- 5.1. Tiêu chí Đánh giá
- 5.2. Phương pháp Đánh giá
- 5.3. Kết quả Đánh giá (Cần trình bày số liệu, bảng biểu cụ thể)
- 5.4. Phân tích và Thảo luận Kết quả

**CHƯƠNG 6: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN**
- 6.1. Kết luận
- 6.2. Hạn chế của Đề tài
- 6.3. Hướng Phát triển Tương lai

**TÀI LIỆU THAM KHẢO**

**PHỤ LỤC**
- Phụ lục A: Chi tiết Cấu hình và Code Snippet Fine-tuning
- Phụ lục B: Ví dụ Mẫu dữ liệu Huấn luyện

---

## **CHƯƠNG 1: GIỚI THIỆU**

### 1.1. Đặt vấn đề

Thị trường nước hoa ngày càng phát triển với sự đa dạng về thương hiệu, mùi hương và phong cách. Điều này mang đến nhiều lựa chọn cho người tiêu dùng nhưng cũng đặt ra thách thức cho các cửa hàng trong việc tư vấn sản phẩm phù hợp và chăm sóc khách hàng hiệu quả. Khách hàng thường cần thông tin chi tiết về sản phẩm, so sánh giữa các lựa chọn, gợi ý dựa trên sở thích cá nhân, dịp sử dụng, hoặc thậm chí là kiến thức chuyên sâu về các tầng hương, độ lưu hương. Việc đáp ứng nhanh chóng và chính xác các yêu cầu này đòi hỏi đội ngũ tư vấn viên am hiểu và tốn nhiều thời gian, đặc biệt trong bối cảnh thương mại điện tử và mua sắm trực tuyến phát triển mạnh mẽ.

Các hệ thống chatbot truyền thống dựa trên luật hoặc các mô hình máy học đơn giản thường gặp khó khăn trong việc hiểu ngữ cảnh phức tạp, đưa ra lời khuyên cá nhân hóa và duy trì cuộc hội thoại tự nhiên. Sự trỗi dậy của các Mô hình Ngôn ngữ lớn (LLMs) với khả năng hiểu và tạo sinh ngôn ngữ vượt trội mở ra tiềm năng lớn cho việc xây dựng các trợ lý ảo thông minh, chuyên sâu trong các lĩnh vực cụ thể. Tuy nhiên, việc áp dụng LLM cho lĩnh vực đặc thù như nước hoa đòi hỏi mô hình phải được trang bị kiến thức chuyên ngành chính xác và khả năng tương tác phù hợp với nghiệp vụ tư vấn bán hàng. Bên cạnh đó, việc truy xuất thông tin động như tình trạng tồn kho theo thời gian thực cũng là một yêu cầu cấp thiết.

Xuất phát từ những nhu cầu và thách thức đó, nhóm chúng tôi quyết định thực hiện đề tài: "**Xây dựng Chatbot tư vấn và chăm sóc khách hàng chuyên dụng cho cửa hàng nước hoa sử dụng Mô hình Ngôn ngữ lớn Qwen2.5-1.5B và kỹ thuật RAG**".

### 1.2. Mục tiêu nghiên cứu

Đề tài hướng đến các mục tiêu chính sau:

* **Nghiên cứu và ứng dụng LLM:** Tìm hiểu, lựa chọn và tinh chỉnh (fine-tuning) một mô hình LLM phù hợp (Qwen2.5-1.5B) để trang bị kiến thức chuyên sâu về nước hoa và kỹ năng tư vấn.
* **Xây dựng Cơ sở Tri thức:** Thiết kế và xây dựng cơ sở tri thức toàn diện bao gồm thông tin chi tiết sản phẩm, dữ liệu tồn kho và bộ dữ liệu huấn luyện chuyên ngành.
* **Phát triển Kiến trúc RAG:** Xây dựng và triển khai kiến trúc Retrieval-Augmented Generation (RAG) kết hợp tìm kiếm ngữ nghĩa (Vector Database - FAISS) và truy vấn dữ liệu có cấu trúc (Relational Database - SQLite) để cung cấp thông tin chính xác và cập nhật.
* **Xây dựng Chatbot Hoàn chỉnh:** Tích hợp mô hình LLM đã tinh chỉnh, cơ sở tri thức và kiến trúc RAG để tạo thành một hệ thống chatbot có khả năng:
    * Hiểu và xử lý các yêu cầu đa dạng của người dùng liên quan đến nước hoa.
    * Cung cấp thông tin sản phẩm chi tiết, chính xác.
    * Đưa ra các gợi ý, tư vấn cá nhân hóa dựa trên yêu cầu và ngữ cảnh.
    * Kiểm tra và thông báo tình trạng tồn kho, giá cả sản phẩm.
    * Tương tác tự nhiên, thân thiện và chuyên nghiệp.
* **Đánh giá hiệu quả:** Thực hiện đánh giá khả năng và hiệu quả của chatbot trong việc đáp ứng các yêu cầu nghiệp vụ.

### 1.3. Đối tượng và phạm vi nghiên cứu

* **Đối tượng nghiên cứu:** Các kỹ thuật liên quan đến Mô hình Ngôn ngữ lớn (LLM), Fine-tuning (đặc biệt là LoRA), Quantization, Retrieval-Augmented Generation (RAG), Vector Database (FAISS), Cơ sở dữ liệu quan hệ (SQLite), và các công cụ/thư viện hỗ trợ (Hugging Face Transformers, PEFT, TRL, LangChain, Chainlit).
* **Phạm vi nghiên cứu:**
    * Xây dựng chatbot tập trung vào nghiệp vụ tư vấn sản phẩm nước hoa và cung cấp thông tin liên quan (giá, tồn kho, mô tả, thành phần...).
    * Sử dụng mô hình Qwen2.5-1.5B làm nền tảng.
    * Xây dựng và sử dụng bộ dữ liệu sản phẩm dựa trên nguồn công khai và bộ dữ liệu huấn luyện do nhóm tự xây dựng.
    * Triển khai chatbot dưới dạng ứng dụng web-chat đơn giản sử dụng Chainlit.
    * Đề tài không đi sâu vào các nghiệp vụ phức tạp như xử lý đơn hàng hoàn chỉnh, quản lý tài khoản người dùng hay các chương trình khuyến mãi động.

### 1.4. Phương pháp nghiên cứu

Nhóm sử dụng kết hợp các phương pháp nghiên cứu sau:

* **Nghiên cứu lý thuyết:** Tìm hiểu và tổng hợp kiến thức về LLM, fine-tuning, RAG, các công nghệ liên quan từ sách, bài báo khoa học, tài liệu kỹ thuật và các nguồn đáng tin cậy khác.
* **Nghiên cứu thực nghiệm:**
    * Thu thập, xử lý và xây dựng các bộ dữ liệu cần thiết.
    * Thực hiện fine-tuning mô hình LLM trên bộ dữ liệu chuyên ngành.
    * Xây dựng và tích hợp các thành phần của hệ thống chatbot (LLM, RAG components, Tools).
    * Triển khai và kiểm thử hoạt động của chatbot.
* **Phương pháp đánh giá:** Kết hợp đánh giá định tính (quan sát tương tác, phản hồi người dùng thử) và định lượng (đo lường các chỉ số hiệu năng nếu có thể) để xác định mức độ đạt được mục tiêu.

### 1.5. Đóng góp mới của đề tài

Đề tài hướng tới những đóng góp chính sau:

* **Xây dựng và công bố bộ dữ liệu fine-tuning chuyên ngành nước hoa:** Nhóm đã tự xây dựng một bộ dữ liệu gồm hơn 3300 mẫu hội thoại chất lượng cao, bao gồm cả kiến thức chuyên môn và kỹ năng tư vấn, xử lý tình huống trong lĩnh vực nước hoa. Bộ dữ liệu này (`phatvucoder/perfume-assistant`) đã được công bố trên Hugging Face Hub, góp phần giải quyết sự thiếu hụt tài nguyên dữ liệu công khai cho cộng đồng nghiên cứu và phát triển chatbot trong lĩnh vực này.
* **Tinh chỉnh và tối ưu mô hình LLM chuyên biệt:** Áp dụng kỹ thuật LoRA và Quantization để fine-tuning hiệu quả mô hình Qwen2.5-1.5B trên bộ dữ liệu chuyên ngành, tạo ra mô hình `Qwen2.5-1.5B-Perfumassist` có khả năng tư vấn nước hoa tốt hơn, tối ưu cho việc triển khai với tài nguyên hạn chế.
* **Ứng dụng kiến trúc RAG kết hợp hiệu quả:** Thiết kế và triển khai luồng RAG kết hợp linh hoạt giữa tìm kiếm ngữ nghĩa tốc độ cao trên FAISS và truy vấn thông tin chính xác, cập nhật (đặc biệt là tồn kho) từ SQLite, phù hợp với yêu cầu thực tế của bài toán tư vấn bán hàng.

### 1.6. Cấu trúc báo cáo

Báo cáo được tổ chức thành 6 chương chính:

* **Chương 1: Giới thiệu:** Trình bày tổng quan về đề tài, lý do lựa chọn, mục tiêu, đối tượng, phạm vi, phương pháp nghiên cứu, đóng góp mới và cấu trúc báo cáo.
* **Chương 2: Tổng quan Cơ sở lý thuyết:** Cung cấp nền tảng kiến thức về chatbot, LLM, các kỹ thuật fine-tuning, kiến trúc RAG, và các công nghệ liên quan được sử dụng trong đề tài.
* **Chương 3: Phân tích và Thiết kế Hệ thống:** Đi sâu vào phân tích yêu cầu bài toán, đề xuất phương pháp thực hiện, lựa chọn công nghệ, thiết kế cơ sở dữ liệu, kiến trúc hệ thống và luồng xử lý chi tiết của chatbot.
* **Chương 4: Triển khai Thực nghiệm:** Mô tả chi tiết quá trình thực hiện các công việc kỹ thuật: xử lý dữ liệu, fine-tuning mô hình, xây dựng knowledge bases, triển khai luồng xử lý và giao diện.
* **Chương 5: Đánh giá Kết quả:** Trình bày các tiêu chí, phương pháp và kết quả đánh giá hiệu quả hoạt động của hệ thống chatbot đã xây dựng.
* **Chương 6: Kết luận và Hướng phát triển:** Tóm tắt các kết quả đạt được, nêu bật đóng góp, chỉ ra những hạn chế và đề xuất các hướng phát triển tiềm năng trong tương lai.

---

## **CHƯƠNG 2: TỔNG QUAN CƠ SỞ LÝ THUYẾT**

Chương này trình bày các khái niệm và công nghệ nền tảng được sử dụng trong quá trình nghiên cứu và xây dựng hệ thống chatbot tư vấn nước hoa của nhóm, bao gồm tổng quan về chatbot, Mô hình Ngôn ngữ lớn (LLM), các kỹ thuật tinh chỉnh (fine-tuning), kiến trúc Retrieval-Augmented Generation (RAG), và các framework hỗ trợ phát triển.

### 2.1. Tổng quan về Chatbot và Trợ lý ảo

* **Định nghĩa:**
    * **Chatbot** (hay chatterbot) là một chương trình máy tính được thiết kế để mô phỏng cuộc hội thoại với người dùng bằng ngôn ngữ tự nhiên, thông qua giao diện văn bản hoặc giọng nói. Mục tiêu chính của chatbot là tự động hóa các cuộc trò chuyện, cung cấp thông tin, hoặc thực hiện các tác vụ đơn giản thay cho con người.
    * **Trợ lý ảo** (Virtual Assistant) thường được xem là một dạng chatbot nâng cao hơn. Ngoài khả năng hội thoại, trợ lý ảo thường có thể thực hiện các tác vụ phức tạp hơn, tích hợp với các hệ thống khác, quản lý thông tin cá nhân và đưa ra các đề xuất chủ động. Ví dụ điển hình là Siri (Apple), Google Assistant, Alexa (Amazon).

* **Lịch sử phát triển:**
    * Khái niệm về chatbot đã có từ những ngày đầu của ngành Trí tuệ nhân tạo. ELIZA, được phát triển vào những năm 1960 bởi Joseph Weizenbaum tại MIT, thường được coi là một trong những chatbot đầu tiên, mô phỏng một nhà trị liệu tâm lý bằng cách nhận dạng từ khóa và phản hồi theo mẫu. Tiếp theo là PARRY, mô phỏng một người mắc chứng hoang tưởng. Trải qua nhiều thập kỷ, với sự phát triển của xử lý ngôn ngữ tự nhiên (NLP) và máy học (Machine Learning), các chatbot ngày càng trở nên tinh vi hơn. Sự bùng nổ của Deep Learning và đặc biệt là các Mô hình Ngôn ngữ lớn (LLMs) trong những năm gần đây đã tạo ra một cuộc cách mạng, cho phép chatbot hiểu ngữ cảnh sâu sắc hơn và tạo ra các phản hồi tự nhiên, linh hoạt chưa từng có.

* **Phân loại Chatbot:**
    * Có nhiều cách phân loại chatbot, nhưng ba loại chính thường được đề cập dựa trên cách chúng hoạt động:
        * **Chatbot dựa trên luật (Rule-based Chatbots):** Hoạt động dựa trên một tập hợp các quy tắc được lập trình sẵn. Chúng thường sử dụng các cây quyết định hoặc nhận dạng từ khóa để xác định cách phản hồi.
            * Ưu điểm: Dễ kiểm soát, đảm bảo tính nhất quán, phù hợp với các quy trình cố định.
            * Nhược điểm: Kém linh hoạt, không thể xử lý các câu hỏi hoặc tình huống nằm ngoài quy tắc, tốn công xây dựng và bảo trì luật khi quy mô lớn.
        * **Chatbot dựa trên truy xuất (Retrieval-based Chatbots):** Sử dụng một kho lưu trữ các cặp câu hỏi-câu trả lời hoặc các đoạn thông tin. Khi nhận được yêu cầu từ người dùng, chatbot sẽ tìm kiếm trong kho lưu trữ để chọn ra câu trả lời phù hợp nhất dựa trên các thuật toán so khớp (matching) hoặc tìm kiếm tương đồng.
            * Ưu điểm: Câu trả lời thường chính xác và phù hợp ngữ cảnh (nếu kho dữ liệu tốt), không tự "sáng tạo" thông tin sai lệch.
            * Nhược điểm: Không thể tạo ra câu trả lời mới, phụ thuộc hoàn toàn vào chất lượng và độ bao phủ của kho dữ liệu.
        * **Chatbot dựa trên sinh dữ liệu (Generative Chatbots):** Sử dụng các mô hình học sâu, đặc biệt là các mô hình sequence-to-sequence hoặc LLMs, để tự tạo ra câu trả lời mới từ đầu dựa trên yêu cầu của người dùng và kiến thức đã học được trong quá trình huấn luyện.
            * Ưu điểm: Linh hoạt, có khả năng xử lý các câu hỏi đa dạng, tạo ra các cuộc hội thoại tự nhiên và thú vị hơn.
            * Nhược điểm: Có nguy cơ "ảo giác" (hallucination) - tạo ra thông tin không chính xác hoặc vô nghĩa, khó kiểm soát hoàn toàn đầu ra, đòi hỏi tài nguyên tính toán lớn để huấn luyện và triển khai.
    * Trong thực tế, nhiều chatbot hiện đại áp dụng phương pháp lai (hybrid), kết hợp các kỹ thuật trên để tận dụng ưu điểm của từng loại. Dự án của nhóm cũng theo hướng này, sử dụng LLM (generative) làm lõi nhưng kết hợp chặt chẽ với cơ chế truy xuất (retrieval) thông qua kiến trúc RAG.

* **Ứng dụng trong kinh doanh và chăm sóc khách hàng:**
    * Chatbot và trợ lý ảo đang ngày càng được ứng dụng rộng rãi trong nhiều lĩnh vực kinh doanh, đặc biệt là trong chăm sóc khách hàng, mang lại nhiều lợi ích:
        * Hỗ trợ 24/7: Cung cấp dịch vụ khách hàng liên tục, không giới hạn thời gian làm việc.
        * Trả lời câu hỏi thường gặp (FAQs): Tự động giải đáp các thắc mắc phổ biến, giảm tải cho nhân viên hỗ trợ.
        * Thu thập thông tin khách hàng: Thu thập thông tin ban đầu, nhu cầu của khách hàng trước khi chuyển cho nhân viên.
        * Tự động hóa quy trình: Hỗ trợ đặt lịch hẹn, kiểm tra trạng thái đơn hàng, thực hiện các giao dịch đơn giản.
        * Tư vấn và giới thiệu sản phẩm: Giúp khách hàng tìm kiếm, so sánh và lựa chọn sản phẩm phù hợp (như trong đề tài này).
        * Cá nhân hóa trải nghiệm: Cung cấp nội dung và đề xuất phù hợp với từng khách hàng dựa trên lịch sử và sở thích.
        * Giảm chi phí vận hành: Giảm chi phí nhân sự và tăng hiệu quả hoạt động của bộ phận chăm sóc khách hàng.

### 2.2. Mô hình Ngôn ngữ lớn (Large Language Models - LLMs)

#### 2.2.1. Giới thiệu chung

Mô hình Ngôn ngữ lớn (LLM) là một loại mô hình trí tuệ nhân tạo thuộc lĩnh vực học sâu (Deep Learning), được đặc trưng bởi số lượng tham số cực kỳ lớn (thường từ hàng tỷ đến hàng nghìn tỷ tham số). Chúng được huấn luyện (pre-training) trên một khối lượng dữ liệu văn bản khổng lồ từ internet và các nguồn khác, cho phép chúng học được các mẫu phức tạp, cấu trúc ngữ pháp, kiến thức phổ quát và khả năng suy luận ở mức độ đáng kinh ngạc.

Khả năng chính của LLMs bao gồm:

* **Hiểu ngôn ngữ tự nhiên (NLU):** Phân tích, diễn giải ý nghĩa, ngữ cảnh, tình cảm trong văn bản.
* **Sinh ngôn ngữ tự nhiên (NLG):** Tạo ra văn bản mới mạch lạc, logic, tự nhiên và phù hợp với ngữ cảnh hoặc yêu cầu đầu vào.
* **Các tác vụ NLP khác:** Dịch thuật giữa các ngôn ngữ, tóm tắt văn bản dài, trả lời câu hỏi, phân loại văn bản, viết code, sáng tạo nội dung (thơ, truyện)...

Một số dòng LLM tiêu biểu đã tạo nên tiếng vang lớn bao gồm: Dòng mô hình GPT (Generative Pre-trained Transformer) của OpenAI (GPT-3, GPT-4), LaMDA và gần đây là Gemini của Google, Llama của Meta, Claude của Anthropic, và dòng mô hình Qwen của Alibaba Cloud.

#### 2.2.2. Kiến trúc Transformer

Kiến trúc Transformer, được giới thiệu lần đầu trong bài báo "Attention Is All You Need" bởi Vaswani và cộng sự vào năm 2017, đã trở thành nền tảng cho hầu hết các LLM hiện đại. Nó giải quyết được những hạn chế về khả năng xử lý phụ thuộc xa và song song hóa tính toán của các kiến trúc tuần tự trước đó như Mạng Nơ-ron Hồi quy (RNN) hay Long Short-Term Memory (LSTM).

Cấu trúc cơ bản của Transformer thường bao gồm hai phần chính là Encoder (Bộ mã hóa) và Decoder (Bộ giải mã), mặc dù một số mô hình chỉ sử dụng một trong hai phần này (ví dụ: BERT chỉ dùng Encoder, GPT chỉ dùng Decoder).

Các thành phần chính trong mỗi khối Encoder và Decoder bao gồm:

* **Input Embedding:** Chuyển đổi các từ (token) đầu vào thành các vector số thực có chiều cố định.
* **Positional Encoding:** Thêm thông tin về vị trí của các token vào vector embedding, vì cơ chế attention không xử lý tuần tự vốn có.
* **Multi-Head Self-Attention:** Đây là thành phần cốt lõi. Cơ chế Self-Attention cho phép mô hình cân nhắc tầm quan trọng của tất cả các token khác trong chuỗi đầu vào khi mã hóa một token cụ thể. Nó tính toán điểm số tương đồng giữa các token và sử dụng chúng để tạo ra một biểu diễn mới cho mỗi token, trong đó chứa thông tin ngữ cảnh từ toàn bộ chuỗi. Multi-Head có nghĩa là quá trình attention này được thực hiện song song nhiều lần với các tập trọng số khác nhau ("các đầu"), sau đó kết quả được kết hợp lại, cho phép mô hình tập trung vào các khía cạnh khác nhau của mối quan hệ giữa các từ.
* **Add & Norm (Residual Connection & Layer Normalization):** Kết nối phần dư (residual connection) giúp tránh vấn đề mất mát gradient trong mạng sâu, trong khi chuẩn hóa lớp (layer normalization) giúp ổn định quá trình huấn luyện.
* **Feed-Forward Networks:** Một mạng nơ-ron truyền thẳng đơn giản được áp dụng độc lập cho từng vị trí token sau lớp attention.

Sự đột phá của cơ chế Self-Attention nằm ở khả năng nắm bắt các phụ thuộc ngữ nghĩa giữa các từ ở xa nhau trong câu và khả năng tính toán song song cao, làm cho việc huấn luyện trên các tập dữ liệu lớn trở nên hiệu quả hơn nhiều.

#### 2.2.3. Giới thiệu về dòng mô hình Qwen và lý do lựa chọn Qwen2.5-1.5B

Qwen (通义千问 - Tongyi Qianwen) là một dòng mô hình ngôn ngữ lớn được phát triển bởi Alibaba Cloud. Dòng mô hình này bao gồm nhiều phiên bản với các kích thước khác nhau, từ nhỏ (như Qwen-1.8B) đến rất lớn (Qwen-72B và lớn hơn), nhằm phục vụ các nhu cầu ứng dụng đa dạng. Các mô hình Qwen được huấn luyện trên dữ liệu đa ngôn ngữ, bao gồm cả tiếng Anh, tiếng Trung và nhiều ngôn ngữ khác, trong đó có sự hỗ trợ tốt cho tiếng Việt.

Các ưu điểm chung của dòng mô hình Qwen bao gồm:

* **Hiệu năng cạnh tranh:** Đạt kết quả tốt trên nhiều bộ benchmark đánh giá khả năng ngôn ngữ và suy luận.
* **Hỗ trợ Context dài:** Nhiều phiên bản Qwen có khả năng xử lý chuỗi đầu vào (context window) rất dài, hữu ích cho các tác vụ yêu cầu phân tích văn bản lớn.
* **Phiên bản Instruct:** Cung cấp các phiên bản "-Instruct" được tinh chỉnh đặc biệt để tuân theo chỉ dẫn của người dùng, phù hợp cho các ứng dụng hội thoại và thực thi tác vụ.
* **Mã nguồn mở:** Alibaba Cloud đã công bố mã nguồn mở cho nhiều phiên bản Qwen, thúc đẩy sự phát triển của cộng đồng.

**Lý do lựa chọn Qwen2.5-1.5B cho đề tài:**

Nhóm đã quyết định lựa chọn mô hình `Qwen/Qwen2.5-1.5B-Instruct` làm nền tảng cho dự án vì các lý do sau:

* **Cân bằng Hiệu năng và Yêu cầu Tài nguyên:** Với 1.5 tỷ tham số, mô hình này đủ mạnh để hiểu và sinh ngôn ngữ phức tạp cần thiết cho việc tư vấn nước hoa, nhưng đồng thời yêu cầu tài nguyên tính toán (GPU VRAM, thời gian huấn luyện) ở mức chấp nhận được, phù hợp với điều kiện thực hiện đồ án tốt nghiệp, đặc biệt khi kết hợp với các kỹ thuật tối ưu như LoRA và Quantization.
* **Tối ưu cho Chatbot (Phiên bản Instruct):** Hậu tố "-Instruct" chỉ ra rằng mô hình này đã trải qua quá trình huấn luyện bổ sung để hiểu và làm theo các chỉ dẫn, mệnh lệnh của người dùng một cách hiệu quả. Đây là yếu tố then chốt để xây dựng một chatbot có khả năng tương tác và thực hiện yêu cầu tốt.
* **Nền tảng Kỹ năng Tốt:** Mặc dù nhóm tập trung fine-tuning kiến thức chuyên ngành, việc mô hình gốc Qwen2.5 được biết đến với khả năng xử lý JSON, gọi hàm (Function Calling) và tích hợp kiến thức ngoài (RAG) tốt là một lợi thế. Điều này tạo nền tảng vững chắc cho việc xây dựng luồng xử lý phức tạp trong LangChain, nơi chatbot cần tương tác với các công cụ (Tools) để truy vấn cơ sở dữ liệu FAISS và SQLite.
* **Hiệu năng Đánh giá Tốt:** Dòng Qwen, đặc biệt là phiên bản Qwen2 mới hơn, nhận được nhiều đánh giá tích cực từ cộng đồng AI về hiệu suất trên các tác vụ khác nhau, cho thấy đây là một lựa chọn mô hình đáng tin cậy.

### 2.3. Kỹ thuật Tinh chỉnh Mô hình Ngôn ngữ lớn (Fine-tuning)

Fine-tuning là quá trình điều chỉnh một mô hình ngôn ngữ lớn đã được huấn luyện trước (pre-trained) trên một lượng lớn dữ liệu tổng quát, để nó hoạt động tốt hơn trên một tập dữ liệu hoặc một tác vụ cụ thể hơn.

#### 2.3.1. So sánh Full Fine-tuning và Parameter-Efficient Fine-tuning (PEFT)

Có hai phương pháp fine-tuning chính:

* **Full Fine-tuning:**
    * Cách thực hiện: Cập nhật toàn bộ các tham số (trọng số) của mô hình pre-trained trong quá trình huấn luyện trên bộ dữ liệu mới.
    * Ưu điểm: Có tiềm năng đạt được hiệu năng tốt nhất trên tác vụ mục tiêu do toàn bộ mô hình được điều chỉnh.
    * Nhược điểm:
        * Tài nguyên: Đòi hỏi tài nguyên tính toán (GPU VRAM) và lưu trữ rất lớn, tương đương với việc huấn luyện mô hình từ đầu.
        * Thời gian: Quá trình huấn luyện tốn nhiều thời gian.
        * Catastrophic Forgetting: Có nguy cơ mô hình "quên" đi kiến thức tổng quát đã học trong quá trình pre-training khi tập trung quá nhiều vào dữ liệu mới.
        * Chi phí triển khai: Mỗi tác vụ mới yêu cầu lưu trữ một bản sao hoàn chỉnh của mô hình đã fine-tuning.
* **Parameter-Efficient Fine-tuning (PEFT):**
    * Cách thực hiện: Chỉ cập nhật một phần nhỏ các tham số của mô hình hoặc thêm vào một số lượng nhỏ các tham số mới có thể huấn luyện, trong khi đóng băng (giữ nguyên) phần lớn các tham số của mô hình pre-trained.
    * Ưu điểm:
        * Tiết kiệm tài nguyên: Giảm đáng kể yêu cầu về VRAM và dung lượng lưu trữ (chỉ cần lưu các tham số được cập nhật/thêm vào, thường nhỏ hơn nhiều so với mô hình gốc).
        * Huấn luyện nhanh hơn: Thời gian huấn luyện thường ngắn hơn do số lượng tham số cần cập nhật ít hơn.
        * Giảm Catastrophic Forgetting: Do phần lớn mô hình gốc được giữ nguyên, kiến thức tổng quát ít bị ảnh hưởng hơn.
        * Linh hoạt: Dễ dàng tạo và quản lý nhiều phiên bản chuyên biệt cho các tác vụ khác nhau từ cùng một mô hình gốc bằng cách lưu các bộ tham số PEFT riêng biệt.
    * Nhược điểm: Hiệu năng có thể thấp hơn một chút so với Full Fine-tuning trong một số trường hợp, mặc dù sự khác biệt này ngày càng được thu hẹp với các kỹ thuật PEFT tiên tiến.

Trong bối cảnh tài nguyên hạn chế và nhu cầu chuyên biệt hóa LLM cho tác vụ tư vấn nước hoa, PEFT là phương pháp phù hợp hơn cho đề tài này.

#### 2.3.2. Kỹ thuật LoRA (Low-Rank Adaptation)

LoRA là một trong những kỹ thuật PEFT phổ biến và hiệu quả nhất hiện nay. Nó dựa trên giả thuyết rằng sự thay đổi cần thiết đối với ma trận trọng số của một mô hình pre-trained (W₀) khi thích ứng với một tác vụ mới có thể được biểu diễn hiệu quả bằng một ma trận cập nhật (ΔW) có rank thấp (low-rank).

* **Nguyên lý hoạt động:** Thay vì cập nhật trực tiếp ma trận W₀ (thường có kích thước rất lớn, ví dụ d x k), LoRA giữ nguyên W₀ và thêm vào một "nhánh" song song tính toán sự thay đổi ΔW. Ma trận ΔW này được phân rã thành tích của hai ma trận nhỏ hơn, có rank thấp r: ΔW = B \* A. Trong đó:
    * Ma trận A có kích thước r x k.
    * Ma trận B có kích thước d x r.
    * Rank r là một siêu tham số (hyperparameter) được chọn, và r << min(d, k). Trong quá trình fine-tuning, chỉ có các tham số của hai ma trận A và B được huấn luyện, còn W₀ được đóng băng. Đầu ra cuối cùng của lớp được tính bằng h = W₀x + BAx.
* **Lợi ích:**
    * Giảm tham số huấn luyện: Số lượng tham số cần huấn luyện giảm từ d \* k xuống chỉ còn r \* (d + k), một sự cắt giảm đáng kể khi r nhỏ.
    * Tiết kiệm VRAM: Giảm mạnh yêu cầu bộ nhớ GPU trong quá trình huấn luyện.
    * Huấn luyện nhanh: Thời gian huấn luyện được rút ngắn.
    * Adapter nhỏ gọn: Các trọng số LoRA (A và B) tạo thành một "adapter" có kích thước nhỏ, dễ dàng lưu trữ, chia sẻ và áp dụng lên mô hình gốc.
    * Không tăng độ trễ inference (sau khi merge): Sau khi huấn luyện, các trọng số LoRA (BA) có thể được hợp nhất (merge) vào trọng số gốc (W = W₀ + BA), tạo thành một mô hình duy nhất mà không cần thêm phép tính nào trong quá trình inference.
* **Các tham số chính:**
    * **r (rank):** Xác định "khả năng biểu diễn" của adapter LoRA. Giá trị lớn hơn cho phép học các thay đổi phức tạp hơn nhưng cũng tăng số lượng tham số. Giá trị thường dùng là 8, 16, 32, 64. Trong đề tài này, nhóm chọn r=16.
    * **lora_alpha:** Một hệ số co giãn (scaling factor) được áp dụng cho đầu ra của LoRA (alpha/r \* BAx). Nó giúp điều chỉnh tầm quan trọng của việc cập nhật LoRA so với trọng số gốc. Thường được đặt bằng r hoặc 2r. Nhóm chọn lora_alpha=32.
    * **target_modules:** Danh sách các lớp trong mô hình gốc mà LoRA adapters sẽ được áp dụng. Việc lựa chọn các lớp phù hợp (thường là các lớp liên quan đến attention và feed-forward) rất quan trọng để đạt hiệu quả tốt. Nhóm đã chọn các module: `["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]`.

#### 2.3.3. Kỹ thuật Lượng tử hóa (Quantization) và BitsAndBytes

Quantization là một kỹ thuật tối ưu hóa mô hình deep learning bằng cách giảm độ chính xác số học được sử dụng để lưu trữ và/hoặc tính toán các tham số (trọng số) và/hoặc các giá trị kích hoạt (activations). Thay vì sử dụng kiểu dữ liệu có độ chính xác cao như 32-bit floating-point (FP32), quantization chuyển đổi chúng sang các kiểu dữ liệu có độ chính xác thấp hơn như 16-bit floating-point (FP16), 16-bit brain float (BF16), 8-bit integer (INT8), hoặc thậm chí 4-bit.

Mục đích chính của Quantization:

* **Giảm kích thước mô hình (Model Footprint):** Lưu trữ trọng số với ít bit hơn giúp giảm đáng kể dung lượng bộ nhớ cần thiết để chứa mô hình.
* **Giảm yêu cầu băng thông bộ nhớ:** Việc di chuyển dữ liệu có độ chính xác thấp giữa bộ nhớ và đơn vị xử lý sẽ nhanh hơn.
* **Tăng tốc độ tính toán (Inference Speed):** Một số phần cứng hỗ trợ các phép toán với độ chính xác thấp nhanh hơn so với độ chính xác cao.

**Thư viện BitsAndBytes:**

BitsAndBytes là một thư viện Python mã nguồn mở cung cấp các triển khai hiệu quả cho các kỹ thuật quantization, đặc biệt là quantization 8-bit và 4-bit, dễ dàng tích hợp với các framework deep learning phổ biến như PyTorch và các thư viện như Hugging Face Transformers.

**Các kỹ thuật Quantization 4-bit trong BitsAndBytes được sử dụng trong đề tài:**

Trong quá trình fine-tuning và load mô hình, nhóm đã sử dụng thư viện BitsAndBytes với các cấu hình sau để tối ưu hóa việc sử dụng VRAM:

* **`load_in_4bit=True`:** Kích hoạt chức năng load trọng số mô hình dưới dạng 4-bit.
* **`bnb_4bit_quant_type="nf4"`:** Chỉ định sử dụng kiểu lượng tử hóa NormalFloat 4-bit (NF4). Đây là một kiểu dữ liệu 4-bit được thiết kế đặc biệt, được cho là giữ lại thông tin tốt hơn và duy trì hiệu năng của mô hình tốt hơn so với các phương pháp quantization 4-bit khác khi áp dụng cho trọng số đã được huấn luyện.
* **`bnb_4bit_compute_dtype=torch.float16`:** Mặc dù trọng số được lưu trữ ở dạng 4-bit, các phép tính toán (nhân ma trận) thường được thực hiện ở độ chính xác cao hơn (ví dụ: FP16 hoặc BF16) để đảm bảo độ ổn định và chính xác. Quá trình này bao gồm việc de-quantize trọng số 4-bit lên kiểu dữ liệu tính toán ngay trước khi thực hiện phép toán. Nhóm sử dụng `torch.float16` làm kiểu dữ liệu tính toán.
* **`bnb_4bit_use_double_quant=True`:** Kích hoạt kỹ thuật Double Quantization. Kỹ thuật này áp dụng quantization một lần nữa cho các hằng số được sử dụng trong quá trình quantization lần đầu, giúp tiết kiệm thêm trung bình khoảng 0.4 bit cho mỗi tham số mà không ảnh hưởng nhiều đến hiệu năng.

Sự kết hợp giữa LoRA (giảm số lượng tham số cần huấn luyện) và Quantization 4-bit (giảm bộ nhớ cho các tham số còn lại) là một chiến lược mạnh mẽ, cho phép nhóm fine-tuning mô hình Qwen2.5-1.5B trên các GPU có dung lượng VRAM hạn chế.

### 2.4. Kiến trúc Retrieval-Augmented Generation (RAG)

#### 2.4.1. Khái niệm và vai trò

Retrieval-Augmented Generation (RAG) là một kiến trúc AI kết hợp sức mạnh của các mô hình ngôn ngữ lớn (LLMs) trong việc sinh ngôn ngữ (Generation) với khả năng của các hệ thống truy xuất thông tin (Retrieval) từ các nguồn kiến thức bên ngoài. Thay vì chỉ dựa vào kiến thức nội tại đã được "học thuộc" trong quá trình pre-training (vốn có thể lỗi thời hoặc không đầy đủ), RAG cho phép LLM truy cập và sử dụng thông tin cập nhật, cụ thể từ một hoặc nhiều cơ sở tri thức (knowledge bases) khi tạo ra câu trả lời.

**Luồng hoạt động cơ bản của RAG:**

1.  **Nhận yêu cầu (Query/Prompt):** Người dùng đưa ra một câu hỏi hoặc yêu cầu.
2.  **Truy xuất (Retrieval):** Hệ thống Retriever sử dụng yêu cầu này để tìm kiếm thông tin liên quan nhất từ(các) nguồn kiến thức bên ngoài (ví dụ: cơ sở dữ liệu vector, cơ sở dữ liệu quan hệ, tài liệu văn bản).
3.  **Tăng cường (Augmentation):** Thông tin được truy xuất (gọi là "context") được kết hợp với yêu cầu ban đầu của người dùng để tạo thành một prompt mới, đầy đủ hơn.
4.  **Sinh dữ liệu (Generation):** Prompt đã được tăng cường này được đưa vào LLM. LLM sử dụng cả yêu cầu gốc và context được cung cấp để tạo ra câu trả lời cuối cùng.

**Vai trò và Lợi ích của RAG:**

* **Giảm Hallucination:** Bằng cách cung cấp thông tin thực tế làm nền tảng, RAG giúp LLM đưa ra các câu trả lời dựa trên sự thật, hạn chế đáng kể hiện tượng tự bịa đặt thông tin (hallucination).
* **Tăng tính cập nhật và chính xác:** Cho phép LLM sử dụng thông tin mới nhất hoặc kiến thức chuyên ngành đặc thù mà không cần phải huấn luyện lại toàn bộ mô hình tốn kém. Điều này đặc biệt quan trọng đối với các thông tin thay đổi thường xuyên như giá cả, tồn kho, tin tức...
* **Tăng tính tin cậy và minh bạch:** Hệ thống có thể (và nên) cung cấp nguồn gốc của thông tin được sử dụng để tạo câu trả lời, cho phép người dùng kiểm chứng.
* **Kiến thức chuyên ngành hiệu quả:** Là cách hiệu quả để tích hợp kiến thức từ các lĩnh vực cụ thể (như y tế, pháp luật, tài chính, hoặc trong trường hợp này là nước hoa) vào khả năng của LLM mà không cần fine-tuning trên quy mô lớn.

#### 2.4.2. Vector Database và tìm kiếm ngữ nghĩa (FAISS)

Trong nhiều ứng dụng RAG, nguồn kiến thức bên ngoài là các tập hợp lớn các tài liệu văn bản (bài viết, mô tả sản phẩm, tài liệu kỹ thuật...). Để truy xuất hiệu quả thông tin liên quan từ các văn bản này dựa trên ý nghĩa (ngữ nghĩa) thay vì chỉ khớp từ khóa, người ta thường sử dụng kỹ thuật tìm kiếm vector.

* **Vector Embedding:** Là quá trình chuyển đổi dữ liệu (ở đây là các đoạn văn bản) thành các vector số thực trong một không gian nhiều chiều. Các mô hình embedding (ví dụ: Sentence Transformers) được huấn luyện để các đoạn văn bản có ý nghĩa tương tự nhau sẽ có các vector biểu diễn nằm gần nhau trong không gian vector đó.
* **Vector Database:** Là một loại cơ sở dữ liệu được thiết kế đặc biệt để lưu trữ và thực hiện các truy vấn tìm kiếm hiệu quả trên các vector embedding. Các truy vấn phổ biến nhất là tìm kiếm K láng giềng gần nhất (K-Nearest Neighbors - KNN), tức là tìm K vector trong cơ sở dữ liệu gần nhất với một vector truy vấn cho trước, dựa trên một thước đo khoảng cách (thường là cosine similarity hoặc Euclidean distance).
* **FAISS (Facebook AI Similarity Search):** Là một thư viện mã nguồn mở do Meta AI phát triển, cung cấp các thuật toán cực kỳ hiệu quả cho việc tìm kiếm tương đồng và phân cụm trên các tập hợp vector lớn, thậm chí hàng tỷ vector. FAISS hỗ trợ nhiều loại index khác nhau, cho phép người dùng cân bằng giữa tốc độ tìm kiếm, độ chính xác và lượng bộ nhớ sử dụng (ví dụ: `IndexFlatL2` cho tìm kiếm chính xác tuyệt đối nhưng chậm với dữ liệu lớn, `IndexIVFPQ` sử dụng quantization để nén vector và tăng tốc tìm kiếm với một sự đánh đổi nhỏ về độ chính xác).
* **Vai trò trong RAG:** FAISS (hoặc các Vector Database khác) thường đóng vai trò là thành phần Retriever trong kiến trúc RAG. Nó lưu trữ các vector embedding của các đơn vị kiến thức (ví dụ: từng đoạn văn bản, từng mô tả sản phẩm). Khi người dùng đặt câu hỏi, câu hỏi đó được chuyển thành vector truy vấn. FAISS nhanh chóng tìm ra các vector kiến thức gần nhất (liên quan nhất về ngữ nghĩa) và trả về các đơn vị kiến thức tương ứng để làm context cho LLM. Trong đề tài này, FAISS được dùng để tìm kiếm các sản phẩm nước hoa có mô tả tương đồng với yêu cầu tư vấn của người dùng.

#### 2.4.3. Tích hợp Cơ sở dữ liệu Quan hệ (SQLite) trong RAG

Mặc dù tìm kiếm vector rất mạnh mẽ cho việc tìm kiếm thông tin dựa trên ngữ nghĩa trong văn bản phi cấu trúc, nó lại không phải là công cụ tối ưu để truy vấn các dữ liệu có cấu trúc, chính xác và thường xuyên thay đổi như: giá cả sản phẩm, số lượng tồn kho, thuộc tính kỹ thuật cụ thể, thông tin khách hàng...

* **Vai trò của Cơ sở dữ liệu Quan hệ (SQL DB) trong RAG:** SQL DB được sử dụng để lưu trữ các loại dữ liệu có cấu trúc này. Thay vì tìm kiếm dựa trên sự tương đồng ngữ nghĩa, SQL DB cho phép truy vấn chính xác dựa trên các điều kiện logic và các khóa (keys). Ví dụ: `SELECT price FROM products WHERE name = 'Chanel No.5' AND size = '100ml'`. Trong kiến trúc RAG, việc truy cập SQL DB thường được thực hiện thông qua các **Tools** (công cụ) mà LLM/Agent có thể gọi khi nhận diện được yêu cầu cần thông tin cấu trúc chính xác.
* **SQLite:** Là một hệ quản trị cơ sở dữ liệu quan hệ nhúng (embedded). Toàn bộ cơ sở dữ liệu (định nghĩa, bảng, dữ liệu) được lưu trữ trong một file duy nhất trên máy khách.
    * **Ưu điểm:** Rất gọn nhẹ, không cần cài đặt server riêng, dễ dàng tích hợp vào các ứng dụng (đặc biệt là Python vì có thư viện `sqlite3` tích hợp sẵn), không yêu cầu cấu hình phức tạp, phù hợp cho các ứng dụng đơn người dùng hoặc có lượng truy cập đồng thời thấp, lý tưởng cho việc lưu trữ dữ liệu sản phẩm và tồn kho của chatbot trong phạm vi đồ án này.
    * **Nhược điểm:** Khả năng xử lý đồng thời (concurrency) hạn chế so với các hệ CSDL client-server như PostgreSQL hay MySQL, không phù hợp cho các ứng dụng web quy mô lớn với hàng nghìn truy cập cùng lúc.
* **Sự kết hợp hiệu quả:** Một kiến trúc RAG mạnh mẽ thường kết hợp cả hai loại cơ sở dữ liệu: sử dụng Vector DB (như FAISS) để tìm kiếm ngữ nghĩa trên dữ liệu phi cấu trúc (mô tả, bài viết...) và sử dụng SQL DB (như SQLite) để truy vấn chính xác dữ liệu có cấu trúc (giá, tồn kho, thuộc tính...). LLM/Agent đóng vai trò điều phối, quyết định khi nào cần tìm kiếm ngữ nghĩa, khi nào cần truy vấn dữ liệu cấu trúc qua Tools.

### 2.5. Framework Phát triển Ứng dụng LLM: LangChain

LangChain là một framework mã nguồn mở được viết bằng Python và JavaScript, được thiết kế để đơn giản hóa và tăng tốc quá trình xây dựng các ứng dụng dựa trên Mô hình Ngôn ngữ lớn (LLMs). Nó cung cấp một tập hợp các module, công cụ và giao diện trừu tượng hóa, giúp các nhà phát triển dễ dàng kết nối LLMs với các nguồn dữ liệu bên ngoài, các công cụ khác và quản lý trạng thái ứng dụng.

Các thành phần cốt lõi của LangChain bao gồm:

* **Models:** Cung cấp giao diện chuẩn để làm việc với nhiều loại mô hình khác nhau, bao gồm:
    * **LLMs:** Các mô hình sinh văn bản cơ bản (như Qwen).
    * **Chat Models:** Các mô hình được tối ưu cho hội thoại, thường nhận và trả về dưới dạng tin nhắn (như Qwen-Instruct).
    * **Text Embedding Models:** Các mô hình tạo vector embedding cho văn bản.
* **Prompts:** Cung cấp các lớp và hàm để quản lý, tối ưu hóa và tạo khuôn mẫu (templating) cho các prompt gửi đến LLMs. Điều này giúp tạo ra các prompt động, tái sử dụng và hiệu quả hơn.
* **Chains:** Cho phép kết hợp nhiều lời gọi LLM hoặc các thành phần khác thành một chuỗi xử lý logic tuần tự. Đây là cách cơ bản để xây dựng các ứng dụng đơn giản hoặc các bước xử lý cố định.
* **Agents:** Là các hệ thống phức tạp hơn Chains. Agent sử dụng một LLM làm "bộ não" để đưa ra quyết định về chuỗi hành động cần thực hiện dựa trên yêu cầu người dùng. Agent có thể sử dụng một tập hợp các **Tools** và lặp lại chu trình: Suy nghĩ (Thought) -> Hành động (Action) -> Quan sát (Observation) cho đến khi hoàn thành nhiệm vụ. Các loại Agent phổ biến gồm ReAct, Conversational Agent...
* **Tools:** Là các giao diện cho phép Agent tương tác với "thế giới bên ngoài". Mỗi Tool thực hiện một chức năng cụ thể, ví dụ: tìm kiếm trên web, chạy một đoạn code Python, truy vấn một API, hoặc (như trong đề tài này) truy vấn cơ sở dữ liệu FAISS, truy vấn cơ sở dữ liệu SQLite.
* **Memory:** Cung cấp cơ chế để lưu trữ và truy xuất trạng thái hoặc lịch sử của cuộc hội thoại, giúp Agent hoặc Chain duy trì ngữ cảnh qua nhiều lượt tương tác. Có nhiều loại Memory khác nhau (ví dụ: `ConversationBufferMemory`, `ConversationSummaryMemory`).

**Vai trò của LangChain trong đề tài:** LangChain đóng vai trò là framework trung tâm, giúp nhóm:

* Tích hợp dễ dàng mô hình `Qwen2.5-1.5B-Perfumassist` đã fine-tuning.
* Định nghĩa các Tools để tương tác với FAISS (tìm kiếm ngữ nghĩa) và SQLite (kiểm tra tồn kho, lấy chi tiết sản phẩm, lấy giá).
* Xây dựng luồng xử lý RAG phức tạp (dưới dạng Chain hoặc Agent) để điều phối việc phân tích yêu cầu, quyết định khi nào cần truy xuất từ FAISS hay SQLite, tổng hợp thông tin và gọi LLM để tạo phản hồi.
* Quản lý bộ nhớ hội thoại để duy trì ngữ cảnh.

### 2.6. Framework Xây dựng Giao diện Người dùng Chat: Chainlit

Chainlit là một framework mã nguồn mở được viết bằng Python, được thiết kế đặc biệt để các nhà phát triển có thể nhanh chóng xây dựng và chia sẻ giao diện người dùng (UI) dạng chat cho các ứng dụng Trí tuệ nhân tạo, đặc biệt là những ứng dụng được xây dựng bằng LangChain hoặc sử dụng LLMs.

Ưu điểm chính của Chainlit:

* **Dễ sử dụng:** Cung cấp một API đơn giản và trực quan với các decorator (`@cl.on_chat_start`, `@cl.on_message`) để xử lý các sự kiện trong luồng chat mà không cần kiến thức sâu về phát triển web front-end.
* **Tích hợp tốt với LangChain:** Được thiết kế để làm việc liền mạch với các đối tượng của LangChain như Agents và Chains.
* **Hiển thị đa phương tiện:** Dễ dàng hiển thị không chỉ văn bản mà còn cả hình ảnh, âm thanh, video và các thành phần UI tùy chỉnh khác ngay trong giao diện chat, rất hữu ích cho việc hiển thị hình ảnh sản phẩm nước hoa.
* **Trực quan hóa Luồng xử lý (Thought Process):** Có khả năng tự động hiển thị các bước trung gian, suy nghĩ (thoughts) và hành động (actions) của LangChain Agent, giúp gỡ lỗi và hiểu rõ hơn cách Agent đưa ra quyết định.
* **Nhanh chóng tạo mẫu (Rapid Prototyping):** Giúp nhanh chóng biến các kịch bản xử lý logic thành một ứng dụng chat có giao diện để kiểm thử và trình diễn.

**Vai trò của Chainlit trong đề tài:** Chainlit được sử dụng để xây dựng giao diện người dùng cuối cùng cho chatbot tư vấn nước hoa. Nó cung cấp cửa sổ chat nơi người dùng nhập yêu cầu, hiển thị phản hồi từ chatbot (bao gồm cả văn bản và hình ảnh sản phẩm được yêu cầu hiển thị bởi tool `show_image`), và giúp quá trình phát triển, thử nghiệm giao diện trở nên đơn giản, nhanh chóng.

---

## **CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG**

### 3.1. Phân tích bài toán và yêu cầu

#### 3.1.1. Mục đích và bối cảnh bài toán

Như đã đề cập ở Chương 1, bài toán đặt ra là xây dựng một trợ lý ảo chuyên nghiệp cho cửa hàng nước hoa, có khả năng tương tác tự nhiên với khách hàng qua giao diện chat để tư vấn sản phẩm, cung cấp thông tin chi tiết, kiểm tra tình trạng hàng hóa và hỗ trợ quá trình ra quyết định mua hàng. Mục đích là nâng cao trải nghiệm khách hàng, giảm tải cho nhân viên tư vấn và tiềm năng tăng doanh số bán hàng.

#### 3.1.2. Yêu cầu chức năng (Functional Requirements)

Hệ thống chatbot cần đáp ứng các chức năng chính sau:

* **F1:** Tiếp nhận và hiểu câu hỏi/yêu cầu của người dùng bằng ngôn ngữ tự nhiên tiếng Việt.
* **F2:** Phân loại ý định (intent) và trích xuất các thông tin quan trọng (entities) từ yêu cầu người dùng.
* **F3:** Cung cấp thông tin chi tiết về sản phẩm nước hoa (thương hiệu, mô tả, tầng hương, giá cả, dung tích, nồng độ, hình ảnh...).
* **F4:** Đưa ra gợi ý sản phẩm dựa trên các tiêu chí người dùng cung cấp (sở thích mùi hương, giới tính, dịp sử dụng, mùa, phong cách...).
* **F5:** So sánh các sản phẩm nước hoa theo yêu cầu.
* **F6:** Tìm kiếm các sản phẩm tương tự với một sản phẩm đã biết.
* **F7:** Kiểm tra và thông báo tình trạng tồn kho của sản phẩm cụ thể.
* **F8:** Trả lời các câu hỏi kiến thức chung về nước hoa (nhóm hương, nồng độ...).
* **F9:** Xử lý các tương tác ngoài lề (chào hỏi, cảm ơn, tán gẫu cơ bản).
* **F10:** Nhận diện và từ chối các yêu cầu không phù hợp hoặc nằm ngoài phạm vi kiến thức.
* **F11:** Có khả năng yêu cầu chuyển cuộc hội thoại cho nhân viên hỗ trợ khi cần thiết.
* **F12:** Duy trì ngữ cảnh cuộc hội thoại.

#### 3.1.3. Yêu cầu phi chức năng (Non-Functional Requirements)

* **NF1:** Phản hồi nhanh chóng (thời gian chờ chấp nhận được).
* **NF2:** Thông tin cung cấp phải chính xác và cập nhật (đặc biệt là giá và tồn kho).
* **NF3:** Giao diện thân thiện, dễ sử dụng.
* **NF4:** Hệ thống có khả năng mở rộng (thêm sản phẩm, kiến thức).
* **NF5:** Hoạt động ổn định.
* **NF6:** Tối ưu hóa việc sử dụng tài nguyên (do sử dụng LLM tương đối lớn).

### 3.2. Phương pháp thực hiện và Đóng góp của Nhóm

#### 3.2.1. Phương pháp tiếp cận tổng thể

Nhóm lựa chọn phương pháp tiếp cận dựa trên việc kết hợp sức mạnh của Mô hình Ngôn ngữ lớn (LLM) đã được tinh chỉnh chuyên sâu với kiến trúc Retrieval-Augmented Generation (RAG) tiên tiến:

1.  **Chọn LLM nền tảng:** Lựa chọn `Qwen2.5-1.5B-Instruct` vì sự cân bằng giữa hiệu năng, tài nguyên và các khả năng sẵn có.
2.  **Xây dựng Dataset chuyên ngành:** Thu thập và tạo ra bộ dữ liệu fine-tuning chất lượng cao về kiến thức và kỹ năng tư vấn nước hoa.
3.  **Fine-tuning hiệu quả:** Sử dụng kỹ thuật LoRA và Quantization (4-bit) để tinh chỉnh LLM trên dataset chuyên ngành, tối ưu hóa cho nhiệm vụ và tài nguyên.
4.  **Thiết kế RAG kết hợp:** Xây dựng hệ thống RAG sử dụng FAISS để tìm kiếm ngữ nghĩa nhanh các sản phẩm phù hợp và SQLite để lưu trữ, truy vấn thông tin chi tiết, chính xác (đặc biệt là tồn kho).
5.  **Xây dựng luồng xử lý (Chain):** Sử dụng LangChain để điều phối hoạt động giữa LLM, bộ nhớ, các công cụ truy xuất dữ liệu (FAISS, SQLite tools).
6.  **Tạo giao diện:** Sử dụng Chainlit để cung cấp giao diện chat thân thiện.

#### 3.2.2. Đóng góp về xây dựng và công bố bộ dữ liệu chuyên ngành nước hoa

Điểm đóng góp quan trọng nhất của nhóm là việc giải quyết vấn đề thiếu hụt dữ liệu huấn luyện công khai cho chatbot nước hoa. Nhóm đã đầu tư thời gian và công sức để:

* Nghiên cứu kiến thức chuyên sâu về nước hoa.
* Thiết kế các kịch bản hội thoại tư vấn, giải đáp thắc mắc, xử lý tình huống thực tế.
* Tạo ra hơn 3300 cặp hỏi-đáp chất lượng cao, bao phủ rộng các khía cạnh cần thiết.
* Chuẩn hóa dữ liệu theo định dạng phù hợp cho fine-tuning (chat format).
* Công bố bộ dữ liệu (`phatvucoder/perfume-assistant`) lên Hugging Face Hub, đóng góp tài nguyên cho cộng đồng.

#### 3.2.3. Đóng góp về tinh chỉnh và tối ưu mô hình LLM cho lĩnh vực cụ thể

Thay vì sử dụng LLM gốc, nhóm đã thực hiện fine-tuning chuyên sâu:

* Áp dụng LoRA để tập trung huấn luyện vào kiến thức nước hoa mà không làm ảnh hưởng nhiều đến khả năng ngôn ngữ chung của mô hình gốc.
* Sử dụng Quantization 4-bit (thông qua BitsAndBytes) để giảm đáng kể yêu cầu bộ nhớ, giúp việc fine-tuning và triển khai mô hình 1.5B trở nên khả thi trên phần cứng phổ thông.
* Tạo ra mô hình `Qwen2.5-1.5B-Perfumassist`, một phiên bản chuyên biệt, hiệu quả hơn cho tác vụ tư vấn nước hoa so với mô hình gốc.

### 3.3. Lựa chọn Công nghệ và Ngôn ngữ sử dụng

#### 3.3.1. Ngôn ngữ lập trình chính: Python

Python được chọn làm ngôn ngữ lập trình chính do hệ sinh thái thư viện phong phú và mạnh mẽ cho Khoa học dữ liệu, Máy học và xử lý ngôn ngữ tự nhiên, đặc biệt là sự hỗ trợ tốt nhất cho các framework và thư viện được sử dụng trong dự án.

#### 3.3.2. Các thư viện và Framework chủ chốt

* **Hugging Face Ecosystem:**
    * `transformers`: Cung cấp quyền truy cập vào mô hình Qwen2.5-1.5B và tokenizer.
    * `datasets`: Để tải và xử lý bộ dữ liệu huấn luyện (`phatvucoder/perfume-assistant`).
    * `peft` (Parameter-Efficient Fine-Tuning): Cung cấp triển khai kỹ thuật LoRA.
    * `trl` (Transformer Reinforcement Learning): Cung cấp `SFTTrainer` để dễ dàng thực hiện Supervised Fine-Tuning.
* **Tối ưu hóa và Tính toán:**
    * `pytorch`: Framework nền tảng cho các phép toán tensor và huấn luyện mô hình deep learning.
    * `bitsandbytes`: Hỗ trợ quantization 4-bit để giảm bộ nhớ khi load và huấn luyện mô hình.
* **RAG và Dữ liệu:**
    * `faiss-cpu` (hoặc `faiss-gpu`): Thư viện thực hiện tìm kiếm vector hiệu quả.
    * `sqlite3` (Thư viện chuẩn của Python): Để tạo và tương tác với cơ sở dữ liệu SQLite.
    * `sentence-transformers` (Có thể cần): Để tạo vector embeddings cho FAISS index.
* **Orchestration và Giao diện:**
    * `langchain`: Framework chính để xây dựng và quản lý luồng xử lý (chain), tích hợp LLM, tools, memory.
    * `chainlit`: Để tạo giao diện người dùng dạng chat.

### 3.4. Thiết kế Cơ sở Dữ liệu và Kiến thức

#### 3.4.1. Dataset Huấn luyện chuyên ngành (`phatvucoder/perfume-assistant`)

* **Mục đích:** Dạy cho LLM kiến thức chuyên sâu về nước hoa và các kỹ năng tư vấn, xử lý hội thoại.
* **Số lượng:** Hơn 3300 mẫu.
* **Định dạng:** Dữ liệu dạng hội thoại (chat format), mỗi mẫu là một danh sách các lượt nói của user và assistant. Ví dụ: `{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}`.
* **Nội dung:** Bao phủ kiến thức (thành phần, nhóm hương, độ lưu hương...), kỹ năng tư vấn (gợi ý theo dịp, mùa, tính cách...), xử lý tình huống (hết hàng, không hiểu, nội dung không liên quan...).
* **Lưu trữ:** Public trên Hugging Face Hub.

#### 3.4.2. Dataset Thông tin Sản phẩm (`fragrance_collection.csv`)

* **Nguồn gốc:** Xử lý từ dự án Perfumes\_Recommender của rawanalqarni (GitHub).
* **Số lượng:** Hơn 4200 record.
* **Cấu trúc (Các cột chính):** Name, Brand, Description, Price, Rate, Rating\_count, image, Gender, Product\_Type, Character\_x, Fragrance\_Family, Size, Year, Ingredients, Concentration, Top\_note, Middle\_note, Base\_note.
* **Vai trò:** Nguồn dữ liệu gốc để:
    * Tạo vector embeddings cho FAISS (chủ yếu từ Description, có thể kết hợp Name, Brand, Notes).
    * Nạp dữ liệu chi tiết vào bảng `fragrance_details` trong SQLite.

#### 3.4.3. Dataset Quản lý Tồn kho (`inventory.csv`)

* **Mục đích:** Lưu trữ thông tin tồn kho hiện tại của các sản phẩm.
* **Cấu trúc (Ví dụ):** Brand, Name, Quantity (Hoặc tốt hơn là `product_id`, Quantity để liên kết với bảng chi tiết).
* **Vai trò:** Nguồn dữ liệu để nạp vào bảng `inventory` trong SQLite. Cần có cơ chế cập nhật định kỳ hoặc real-time (nằm ngoài phạm vi đồ án này, nhưng cần thiết cho hệ thống thực tế).

#### 3.4.4. Thiết kế Lưu trữ Vector (FAISS Index)

* **Mục đích:** Hỗ trợ tìm kiếm ngữ nghĩa nhanh các sản phẩm dựa trên mô tả hoặc yêu cầu của người dùng.
* **Dữ liệu nguồn:** Các trường văn bản (chủ yếu là Description) từ `fragrance_collection.csv`.
* **Quá trình tạo:**
    1.  Chọn một mô hình Sentence Transformer phù hợp (ví dụ: `all-MiniLM-L6-v2` hoặc mô hình đa ngữ nếu cần) để chuyển đổi các đoạn text mô tả sản phẩm thành vector embeddings.
    2.  Sử dụng FAISS để xây dựng một index (ví dụ: `IndexFlatL2` hoặc các index hiệu quả hơn như `IndexIVFPQ`) từ các vector đã tạo. Lưu index này lại.
* **Sử dụng:** Tool `search_fragrance_vectors_faiss` sẽ nhận query, chuyển query thành vector bằng cùng mô hình Sentence Transformer, sau đó tìm kiếm các vector gần nhất trong FAISS index, trả về ID của các sản phẩm tương ứng.

#### 3.4.5. Thiết kế Cơ sở dữ liệu Quan hệ (SQLite)

* **Mục đích:** Lưu trữ thông tin chi tiết, có cấu trúc của sản phẩm và dữ liệu tồn kho một cách chính xác, dễ truy vấn. Đóng vai trò "Source of Truth".
* **Công nghệ:** SQLite (do tính gọn nhẹ, dễ tích hợp).
* **Thiết kế bảng (Ví dụ):**
    * **`fragrance_details` Table:**
        * `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT) - Hoặc dùng ID gốc từ file CSV nếu có.
        * `name` (TEXT, NOT NULL)
        * `brand` (TEXT)
        * `description` (TEXT)
        * `price` (REAL) - Lưu giá chuẩn hoặc giá theo size cụ thể.
        * `image_url` (TEXT)
        * `gender` (TEXT)
        * `fragrance_family` (TEXT)
        * `size` (TEXT)
        * `year` (INTEGER)
        * `ingredients` (TEXT)
        * `concentration` (TEXT)
        * `top_notes` (TEXT)
        * `middle_notes` (TEXT)
        * `base_notes` (TEXT)
        * `rate` (REAL)
        * `rating_count` (INTEGER)
        * *(Thêm các cột cần thiết khác)*
    * **`inventory` Table:**
        * `product_id` (INTEGER, FOREIGN KEY REFERENCES `fragrance_details`(`id`))
        * `quantity` (INTEGER, NOT NULL, DEFAULT 0)
        * `last_updated` (TIMESTAMP) - Thời điểm cập nhật cuối.
        * *(PRIMARY KEY (`product_id`))*

### 3.5. Thiết kế Kiến trúc Hệ thống Tổng thể

Kiến trúc hệ thống được thiết kế theo dạng module, tương tác với nhau thông qua LangChain Agent.

1.  **User Interface (Chainlit):** Giao diện chat nơi người dùng nhập yêu cầu và nhận phản hồi.
2.  **LangChain Agent (Core Logic Engine):**
    * Nhận input từ UI.
    * Gọi Input Processor (có thể là một LLM call hoặc module riêng) để phân tích input (`analysis_result`).
    * Sử dụng Router (logic điều khiển dựa trên `analysis_result`) để quyết định hành động tiếp theo.
    * Quản lý Memory (lịch sử hội thoại).
    * Gọi các **Tools** khi cần thiết:
        * `search_fragrance_vectors_faiss`: Tương tác với FAISS Index.
        * `check_inventory_sqlite`, `get_fragrance_details_sqlite`, `get_price_sqlite`: Tương tác với SQLite Database.
        * `show_image`: Gửi yêu cầu hiển thị ảnh về UI.
        * `request_human_handoff`: Gửi yêu cầu chuyển người.
    * Gọi **LLM (`Qwen2.5-1.5B-Perfumassist`)** để:
        * Phân tích input (nếu Input Processor dùng LLM).
        * Sinh phản hồi cuối cùng (Response Generation) dựa trên input, memory, và kết quả từ Tools/Knowledge Bases.
    * Gửi phản hồi cuối cùng và các yêu cầu khác (như hiển thị ảnh) về UI.
3.  **Knowledge Bases:**
    * **FAISS Index:** Lưu trữ vector sản phẩm, được truy cập bởi tool `search_fragrance_vectors_faiss`.
    * **SQLite Database:** Lưu trữ chi tiết sản phẩm và tồn kho, được truy cập bởi các tool SQLite tương ứng.

### 3.6. Thiết kế Luồng Xử lý Chi tiết (Workflow/Chain)

#### 3.6.1. Sơ đồ luồng tổng quát

*( flow_diagram.mermaid )*

#### 3.6.2. Mô tả chi tiết các thành phần (Nodes) trong luồng

*(Mô tả chi tiết mục tiêu, input, hành động, output của từng Node)*

* **Node 1: Input Analysis:**
    * **Mục tiêu:** Phân tích sâu user input để hiểu rõ ý định, thực thể và các yếu tố quan trọng khác.
    * **Input:** `user_input`, `conversation_history`.
    * **Hành động:** Gọi LLM (hoặc một module phân tích riêng) để xác định:
        * `Safety Check`: Nội dung có độc hại/không phù hợp không?
        * `Relevance Check`: Có liên quan đến nước hoa/shop không?
        * `Intent Classification`: Ý định chính (hỏi thông tin, tư vấn, so sánh, kiểm tra tồn kho, chào hỏi, phàn nàn, không liên quan...).
        * `Entity Extraction`: Trích xuất các thực thể quan trọng (tên SP, thương hiệu, mùi hương, dịp, giới tính, giá, số lượng...).
        * `Capability Assessment`: Chatbot có khả năng đáp ứng yêu cầu này không? (Dựa trên tools và kiến thức).
        * `Purchase Intent`: Mức độ thể hiện ý định mua hàng (thấp, trung bình, cao).
    * **Output:** `analysis_result` (một cấu trúc dữ liệu chứa tất cả thông tin phân tích trên).
* **Node 2: Router:**
    * **Mục tiêu:** Định tuyến luồng xử lý dựa trên kết quả phân tích.
    * **Input:** `analysis_result`.
    * **Hành động:** Sử dụng logic (if/else hoặc mô hình router) để quyết định Node tiếp theo:
        * Nếu không an toàn/không liên quan -> Node 7 (Rejection/Simple Response).
        * Nếu cần tư vấn/so sánh/tìm kiếm tương tự -> Node 3 (FAISS Retrieval).
        * Nếu hỏi thông tin cụ thể (giá/tồn kho) và có đủ entity -> Node 5 (Direct Tool Use).
        * Nếu chào hỏi/cảm ơn/yêu cầu đơn giản -> Node 7 (Simple Response).
        * Nếu phàn nàn/yêu cầu phức tạp vượt khả năng -> Node 7 (Handoff Response).
        * Các trường hợp khác -> Node 6 (General Response Generation).
    * **Output:** Tên Node tiếp theo và các dữ liệu cần thiết.
* **Node 3: Knowledge Retrieval (FAISS):**
    * **Mục tiêu:** Tìm kiếm các sản phẩm tiềm năng dựa trên ngữ nghĩa của yêu cầu tư vấn.
    * **Input:** `query` (trích xuất từ `analysis_result`), `k` (số lượng kết quả mong muốn).
    * **Hành động:** Gọi tool `search_fragrance_vectors_faiss`. Tool này sẽ:
        1.  Chuyển `query` thành vector.
        2.  Tìm kiếm `k` vector gần nhất trong FAISS Index.
        3.  Trả về danh sách ID của các sản phẩm ứng viên (`candidate_product_ids`).
    * **Output:** `candidate_product_ids`. Chuyển đến Node 4.
* **Node 4: Inventory Check, Filtering & Detail Retrieval (SQLite):**
    * **Mục tiêu:** Kiểm tra tồn kho, lọc/sắp xếp và lấy thông tin chi tiết cho các sản phẩm ứng viên.
    * **Input:** `candidate_product_ids`.
    * **Hành động:**
        1.  Gọi tool `check_inventory_sqlite` cho từng `product_id` để lấy tình trạng tồn kho (`stock_status`).
        2.  Lọc bỏ/đánh dấu các sản phẩm hết hàng (tuỳ chiến lược: ẩn đi hoặc vẫn gợi ý nhưng báo hết hàng). Có thể sắp xếp lại danh sách ưu tiên sản phẩm còn hàng.
        3.  Gọi tool `get_fragrance_details_sqlite` cho các sản phẩm còn lại (hoặc tất cả) để lấy thông tin chi tiết (mô tả, giá, hương, ảnh...).
    * **Output:** `context_docs` (danh sách các tài liệu, mỗi tài liệu chứa thông tin chi tiết của một sản phẩm và `stock_status` của nó). Chuyển đến Node 6.
* **Node 5: Direct Tool Use (SQLite):**
    * **Mục tiêu:** Thực thi truy vấn trực tiếp vào SQLite khi yêu cầu đủ cụ thể.
    * **Input:** `tool_name` (ví dụ: `check_inventory_sqlite`, `get_price_sqlite`), `tool_input` (ví dụ: tên sản phẩm, size).
    * **Hành động:** Gọi tool SQLite tương ứng với tham số đầu vào.
    * **Output:** `tool_result` (kết quả từ tool, ví dụ: số lượng tồn kho, giá). Chuyển đến Node 6.
* **Node 6: Response Generation (LLM):**
    * **Mục tiêu:** Tổng hợp thông tin và tạo phản hồi cuối cùng cho người dùng.
    * **Input:** `analysis_result`, `context_docs` (từ Node 4) hoặc `tool_result` (từ Node 5), `conversation_history`.
    * **Hành động:**
        1.  Xây dựng prompt cuối cùng cho LLM (`Qwen2.5-1.5B-Perfumassist`) bao gồm:
            * System prompt (vai trò chatbot).
            * Lịch sử hội thoại (`conversation_history`).
            * Yêu cầu gốc của người dùng (`user_input` từ `analysis_result`).
            * Thông tin ngữ cảnh đã truy xuất (`context_docs` hoặc `tool_result`).
            * Chỉ dẫn cho LLM tạo phản hồi (ví dụ: "Dựa vào thông tin trên, hãy tư vấn cho khách hàng...", "Hãy trả lời câu hỏi về tồn kho...").
        2.  Gọi LLM để sinh phản hồi.
        3.  (Optional) Phân tích phản hồi của LLM để xem có yêu cầu gọi tool `show_image` không.
    * **Output:** `final_response_text` (nội dung chat trả lời), `image_url_to_show` (nếu có). Chuyển đến Node 8.
* **Node 7: Simple / Rejection / Handoff Responses:**
    * **Mục tiêu:** Xử lý các trường hợp không cần RAG phức tạp hoặc cần từ chối/chuyển tiếp.
    * **Input:** `analysis_result`.
    * **Hành động:** Dựa vào `analysis_result` (safety, relevance, intent, capability), chọn một câu trả lời mẫu hoặc gọi LLM với prompt đơn giản để:
        * Từ chối yêu cầu không phù hợp/ngoài phạm vi.
        * Trả lời chào hỏi/cảm ơn đơn giản.
        * Yêu cầu làm rõ thông tin.
        * Thông báo chuyển cuộc gọi cho nhân viên (gọi tool `request_human_handoff`).
    * **Output:** `final_response_text`. Chuyển đến Node 8.
* **Node 8: Update Memory:**
    * **Mục tiêu:** Lưu lại lượt tương tác hiện tại vào bộ nhớ.
    * **Input:** `user_input`, `final_response_text`, `current_conversation_history`.
    * **Hành động:** Cập nhật bộ nhớ hội thoại (ví dụ: thêm cặp user/assistant mới vào `ConversationBufferMemory`).
    * **Output:** `updated_conversation_history`. Kết thúc một lượt xử lý, chờ input tiếp theo.

---

## **CHƯƠNG 4: TRIỂN KHAI THỰC NGHIỆM**

### 4.1. Môi trường Triển khai

* **Phần cứng:** Google Colab (Card T4)
* **Các thư viện chính (phiên bản ví dụ):**
    * `transformers` (>=4.38)
    * `peft` (>=0.9)
    * `trl` (>=0.7)
    * `torch` (>=2.0)
    * `bitsandbytes` (>=0.42)
    * `datasets` (>=2.15)
    * `faiss-cpu` hoặc `faiss-gpu` (>=1.7)
    * `langchain` (>=0.1)
    * `chainlit` (>=1.0)
    * `sentence-transformers` (>=2.2)

### 4.2. Quá trình Xử lý và Chuẩn bị Dữ liệu

#### 4.2.1. Xây dựng và chuẩn hóa Dataset Huấn luyện

* **Quy trình:** Dữ liệu được tạo ra bằng cách kết hợp:
    * Nghiên cứu các câu hỏi thường gặp, tình huống tư vấn thực tế tại các cửa hàng/diễn đàn nước hoa.
    * Sử dụng LLM (như GPT-4) để sinh các mẫu hội thoại ban đầu dựa trên kịch bản.
    * Chỉnh sửa, bổ sung thủ công để đảm bảo chất lượng, tính chuyên môn và đa dạng.
    * Tổng hợp hơn 3300 mẫu hội thoại chất lượng.
* **Làm sạch, Chuẩn hóa:** Loại bỏ các ký tự đặc biệt không cần thiết, sửa lỗi chính tả, đảm bảo cấu trúc hội thoại nhất quán (luôn bắt đầu bằng user, xen kẽ user/assistant).
* **Chuyển đổi định dạng:** Sử dụng hàm `tokenizer.apply_chat_template` của Hugging Face để chuyển đổi mỗi mẫu hội thoại (dạng list dictionary) thành một chuỗi text duy nhất theo đúng định dạng template của Qwen2 Instruct.
* **Phân chia tập:** Sử dụng hàm `train_test_split` của `datasets` để chia tập train/validation theo tỷ lệ 85/15.
* **Đẩy lên Hub:** Sử dụng `push_to_hub` để công bố dataset `phatvucoder/perfume-assistant`.

#### 4.2.2. Xử lý và tích hợp Dataset Sản phẩm

* **Tải dữ liệu:** Clone repo `Perfumes_Recommender` và lấy file `fragrance_collection.csv`.
* **Kiểm tra, làm sạch:**
    * Kiểm tra các giá trị thiếu (NaN) ở các cột quan trọng (Name, Brand, Description, Price, image...).
    * Điền giá trị thiếu bằng giá trị mặc định (ví dụ: 'Unknown', 0) hoặc loại bỏ hàng nếu thiếu quá nhiều thông tin.
    * Chuẩn hóa định dạng cột Price (loại bỏ ký tự tiền tệ, chuyển sang số).
    * Kiểm tra tính hợp lệ của URL hình ảnh.
* **Lựa chọn trường:** Xác định các cột sẽ dùng cho FAISS (chủ yếu `Description`, có thể kết hợp `Name`, `Brand`, `Notes`) và các cột sẽ nạp vào SQLite (hầu hết các cột còn lại).

#### 4.2.3. Tạo Dataset Tồn kho

* **Tạo `inventory.csv`:** Tạo file CSV với các cột `product_id` (phải khớp với ID trong bảng `fragrance_details` sau khi nạp), `Quantity`.
* **Dữ liệu giả định:** Điền số lượng tồn kho ngẫu nhiên hoặc theo một logic đơn giản (ví dụ: các sản phẩm phổ biến có số lượng lớn hơn) cho mục đích demo.
* **Liên kết:** Đảm bảo cột `product_id` có thể ánh xạ chính xác đến sản phẩm trong `fragrance_collection.csv` (có thể cần tạo cột ID tạm thời trong quá trình xử lý file CSV gốc).

### 4.3. Quá trình Fine-tuning Mô hình Qwen2.5-1.5B với LoRA

#### 4.3.1. Chi tiết cấu hình (Quantization, LoRA, SFTConfig)

* **`BitsAndBytesConfig`:**
    ```python
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
    )
    ```
* **`LoraConfig`:**
    ```python
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    )
    ```
* **`SFTConfig` (Training Arguments):**
    ```python
    training_args = SFTConfig(
        output_dir="./qwen2.5-1.5B-Instruct-finetuned-perfume",
        num_train_epochs=4,
        per_device_train_batch_size=4,        # Batch size trên mỗi GPU
        gradient_accumulation_steps=4,     # Tích lũy gradient sau 4 bước => Effective batch size = 16
        per_device_eval_batch_size=1,      # Batch size khi đánh giá
        learning_rate=2e-4,                # Tốc độ học
        lr_scheduler_type="cosine",        # Loại learning rate scheduler
        warmup_ratio=0.05,                 # Tỷ lệ bước khởi động learning rate
        max_seq_length=768,                # Độ dài tối đa sequence (dựa trên phân tích dataset)
        logging_steps=10,                  # Ghi log sau mỗi 10 bước
        save_steps=20,                     # Lưu checkpoint sau mỗi 20 bước
        eval_steps=20,                     # Đánh giá trên tập validation sau mỗi 20 bước
        max_grad_norm=0.5,                 # Giới hạn norm của gradient
        fp16=True,                         # Sử dụng mixed precision (FP16)
        packing=True,                      # Đóng gói nhiều sequence ngắn vào 1 batch (tăng hiệu quả)
        report_to=["tensorboard"],         # Báo cáo kết quả lên TensorBoard
        eval_strategy="steps",             # Thực hiện đánh giá theo số bước (eval_steps)
    )
    ```

#### 4.3.2. Tiến trình huấn luyện và kết quả

* **Chạy `SFTTrainer`:** Khởi tạo `SFTTrainer` với model, tokenizer, configs, datasets và gọi `trainer.train()`.
* **Theo dõi:** Sử dụng TensorBoard để theo dõi `train/loss` và `eval/loss`. Quan sát thấy loss giảm dần trên cả hai tập, cho thấy mô hình đang học. `eval/loss` ổn định hoặc bắt đầu tăng nhẹ là dấu hiệu có thể dừng huấn luyện.
* **Lựa chọn Checkpoint:** Dựa vào đồ thị `eval/loss` trên TensorBoard, chọn checkpoint có `eval/loss` thấp nhất.

        | Step | Training Loss  | Validation Loss |
        |------|----------------|-----------------|
        |  20  |     7.102500   |     1.665940    |
        |  40  |     6.069800   |     1.457833    |
        |  60  |     5.255600   |     1.373847    |
        |  80  |     5.123800   |     1.329985    |
        | 100  |     4.829900   |     1.310826    |
        | 120  |     4.510400   |     1.295062    |
        | 140  |     4.529200   |     1.289866    |
        | 160  |     4.275700   |     1.290403    |
        | 180  |     4.321100   |     1.289637    |

    ```
    # Ví dụ mô tả đồ thị (không phải code chạy được):
    # Đồ thị eval/loss cho thấy loss giảm mạnh trong epoch đầu,
    # sau đó giảm chậm hơn và đạt giá trị tối thiểu ở step X (ví dụ step 160),
    # sau đó bắt đầu tăng nhẹ. Do đó, checkpoint tại step 140 được chọn.
    ```

#### 4.3.3. Merge Adapter LoRA và Lưu trữ Mô hình

* **Load Base Model & Adapter:**
    ```python
    from peft import AutoPeftModelForCausalLM

    # Load model đã merge với adapter từ checkpoint tốt nhất
    merged_model = AutoPeftModelForCausalLM.from_pretrained(
        "./qwen2.5-1.5B-Instruct-finetuned-perfume/checkpoint-160", # Đường dẫn đến checkpoint tốt nhất
        device_map="auto",
        trust_remote_code=True
    )
    merged_model = merged_model.merge_and_unload() # Hợp nhất adapter vào base model
    ```
* **Lưu mô hình đã merge:**
    ```python
    output_merged_dir = "./Qwen2.5-1.5B-Instruct-Perfumassist-merged"
    merged_model.save_pretrained(output_merged_dir)
    tokenizer.save_pretrained(output_merged_dir)
    ```
* **Upload lên Hub:** Sử dụng `huggingface-cli login` và `push_to_hub` để đẩy thư mục `Qwen2.5-1.5B-Instruct-Perfumassist-merged` lên Hugging Face Hub với tên `phatvucoder/Qwen2.5-1.5B-Perfumassist`.

### 4.4. Xây dựng Knowledge Bases

#### 4.4.1. Tạo FAISS Index từ dữ liệu sản phẩm

```python
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load dữ liệu sản phẩm
df = pd.read_csv("fragrance_collection.csv")
# Kết hợp các trường text quan trọng để tạo embedding
df['combined_text'] = df['Name'].fillna('') + " by " + df['Brand'].fillna('') + ". " + df['Description'].fillna('') + \
                      " Notes: " + df['Top_note'].fillna('') + ", " + df['Middle_note'].fillna('') + ", " + df['Base_note'].fillna('')

# 2. Load mô hình Sentence Transformer
encoder_model = SentenceTransformer('all-MiniLM-L6-v2') # Hoặc mô hình khác

# 3. Tạo vector embeddings
corpus_embeddings = encoder_model.encode(df['combined_text'].tolist(), convert_to_tensor=True, show_progress_bar=True)
corpus_embeddings_np = corpus_embeddings.cpu().numpy().astype('float32') # Chuyển sang numpy float32

# 4. Xây dựng FAISS index
index = faiss.IndexFlatL2(corpus_embeddings_np.shape[1]) # Sử dụng L2 distance
index.add(corpus_embeddings_np)

# 5. Lưu index
faiss.write_index(index, "fragrance_faiss.index")

# (Lưu thêm mapping từ index trong FAISS về ID sản phẩm gốc nếu cần)
df[['id', 'Name', 'Brand']].to_csv("faiss_id_mapping.csv", index=False) # Giả sử có cột 'id'
````

#### 4.4.2. Tạo và nạp dữ liệu vào SQLite Database

```Python
import sqlite3
import pandas as pd

# 1. Định nghĩa schema (trong code hoặc file .sql)
# Ví dụ:
# CREATE TABLE fragrance_details ( ... );
# CREATE TABLE inventory ( ... );

# 2. Kết nối/Tạo DB
conn = sqlite3.connect('perfume_shop.db')
cursor = conn.cursor()

# (Thực thi lệnh CREATE TABLE nếu DB chưa tồn tại)
# cursor.execute("CREATE TABLE IF NOT EXISTS fragrance_details (...)")
# cursor.execute("CREATE TABLE IF NOT EXISTS inventory (...)")


# 3. Đọc dữ liệu từ CSV
df_fragrance = pd.read_csv("fragrance_collection.csv").fillna('') # Xử lý NaN trước khi nạp
df_inventory = pd.read_csv("inventory.csv")

# (Thêm cột ID nếu chưa có và cần thiết để làm khóa ngoại)
# df_fragrance['id'] = range(len(df_fragrance)) # Ví dụ đơn giản

# 4. Nạp dữ liệu vào SQLite
# Nạp bảng fragrance_details (chọn các cột cần thiết)
df_fragrance_to_db = df_fragrance[['id', 'Name', 'Brand', 'Description', 'Price', 'image', 'Gender', ...]] # Chọn cột khớp schema
df_fragrance_to_db.to_sql('fragrance_details', conn, if_exists='replace', index=False) # 'replace' hoặc 'append'

# Nạp bảng inventory
df_inventory_to_db = df_inventory[['product_id', 'Quantity']] # Giả sử cột khớp tên
# Cần đảm bảo product_id trong inventory.csv khớp với id trong fragrance_details
df_inventory_to_db.to_sql('inventory', conn, if_exists='replace', index=False)

# 5. Commit và đóng kết nối
conn.commit()
conn.close()
```

### 4.5. Triển khai Luồng Xử lý với LangChain

-   **Định nghĩa Tools:**
    -   Tạo các hàm Python (ví dụ: `search_faiss`, `get_details_sql`, `check_stock_sql`, `show_image_ui`).
    -   Sử dụng `@tool` decorator của LangChain hoặc tạo các lớp kế thừa từ `BaseTool` để mô tả input/output và chức năng của từng tool.
    -   Ví dụ `check_stock_sql`: input là tên sản phẩm, output là chuỗi thông báo còn hàng hay hết hàng.
    -   Ví dụ `show_image_ui`: input là URL ảnh, output là thông báo "Đã yêu cầu hiển thị ảnh" (hành động hiển thị thực tế do Chainlit xử lý).
-   **Xây dựng Agent:**
    -   Load LLM đã fine-tune (`phatvucoder/Qwen2.5-1.5B-Perfumassist`) sử dụng `HuggingFaceEndpoint` hoặc `HuggingFacePipeline`.
    -   Khởi tạo `ConversationBufferMemory`.
    -   Tạo danh sách các tools đã định nghĩa.
    -   Sử dụng `create_react_agent` hoặc `create_conversational_retrieval_agent` (hoặc các agent khác phù hợp) với LLM, tools, và memory.
    -   Khởi tạo `AgentExecutor`.
-   **Triển khai logic Router:** Logic router có thể được tích hợp vào prompt của agent (yêu cầu agent tự quyết định tool nào cần gọi) hoặc xây dựng một chain riêng biệt (`RouterChain`) để phân tích input và quyết định tool/agent nào sẽ xử lý tiếp.

### 4.6. Xây dựng Giao diện Người dùng với Chainlit

```Python
import chainlit as cl
from langchain.agents import AgentExecutor # Hoặc Chain
# (Import các thành phần LangChain khác: LLM, Memory, Tools...)

# Giả sử agent_executor đã được khởi tạo ở đây hoặc trong hàm on_chat_start

@cl.on_chat_start
async def start():
    # Khởi tạo Agent, Memory ở đây nếu cần cho mỗi session
    # agent_executor = initialize_agent() # Ví dụ
    # cl.user_session.set("agent", agent_executor)
    await cl.Message(content="Xin chào! Tôi là trợ lý nước hoa, tôi có thể giúp gì cho bạn?").send()

@cl.on_message
async def main(message: cl.Message):
    # Lấy agent từ session
    # agent = cl.user_session.get("agent")

    # Gọi agent để xử lý tin nhắn
    # Sử dụng Callback để bắt các bước trung gian và yêu cầu hiển thị ảnh
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, # Stream câu trả lời cuối cùng
        # Các callback khác nếu cần
    )
    cb.answer_reached = True # Đảm bảo answer prefix token không bị ẩn

    # Xử lý tool show_image (ví dụ đơn giản)
    image_to_show = None
    def request_image_display(url: str):
        nonlocal image_to_show
        image_to_show = url
        return "Đã yêu cầu hiển thị ảnh."

    # (Cần đảm bảo tool show_image trong LangChain gọi hàm request_image_display này)

    response = await agent_executor.ainvoke(
        {"input": message.content},
        callbacks=[cb]
    )

    final_answer = response.get("output", "Xin lỗi, tôi chưa thể xử lý yêu cầu này.")

    # Gửi câu trả lời dạng text
    # await cl.Message(content=final_answer).send() # Không cần nếu stream_final_answer=True

    # Hiển thị ảnh nếu được yêu cầu bởi tool
    if image_to_show:
       image_element = cl.Image(url=image_to_show, name="product_image", display="inline")
       await cl.Message(content="", elements=[image_element]).send()

# Chạy ứng dụng: chainlit run app.py -w
```

### 4.7. Một số Giao diện và Kết quả Chạy thử nghiệm (Demo UI)

Hình 4.1: Màn hình chào hỏi ban đầu của chatbot.

Hình 4.2: Chatbot tư vấn sản phẩm dựa trên yêu cầu "mùi hương nam tính, dùng mùa hè" và hiển thị hình ảnh sản phẩm gợi ý.

Hình 4.3: Chatbot trả lời thông tin chi tiết về "Chanel No. 5 EDP" (tầng hương, nồng độ).

Hình 4.4: Chatbot kiểm tra và thông báo tình trạng tồn kho của "Dior Sauvage EDT 100ml".

Hình 4.5: Chatbot so sánh hai sản phẩm "Acqua di Gio" và "Bleu de Chanel".

Hình 4.6: Chatbot từ chối trả lời câu hỏi không liên quan "Thời tiết hôm nay thế nào?".

---

## **CHƯƠNG 5: ĐÁNH GIÁ KẾT QUẢ**

### 5.1. Tiêu chí Đánh giá

Nhóm đề xuất các tiêu chí sau để đánh giá chatbot:

1.  **Độ chính xác thông tin:** Mức độ chính xác của thông tin sản phẩm, giá cả, tồn kho do chatbot cung cấp so với cơ sở dữ liệu SQLite.
2.  **Tính hữu ích của tư vấn:** Mức độ phù hợp và hữu ích của các gợi ý, lời khuyên tư vấn đối với yêu cầu của người dùng (ví dụ: gợi ý có đúng nhóm hương, dịp sử dụng không?).
3.  **Khả năng hiểu yêu cầu:** Khả năng chatbot hiểu đúng ý định (intent) và các thực thể (entities) trong câu hỏi/yêu cầu của người dùng.
4.  **Tính tự nhiên của hội thoại:** Mức độ trôi chảy, mạch lạc, ngữ pháp đúng và giống người của các phản hồi.
5.  **Khả năng xử lý các tình huống:** Khả năng xử lý các trường hợp như hết hàng, không hiểu yêu cầu, yêu cầu ngoài phạm vi, yêu cầu so sánh...
6.  **Tốc độ phản hồi:** Thời gian trung bình từ khi người dùng gửi yêu cầu đến khi nhận được phản hồi đầy đủ.

### 5.2. Phương pháp Đánh giá

Do tính chất đặc thù và sự mới mẻ của bài toán xây dựng chatbot tư vấn nước hoa chuyên sâu, hiện chưa có bộ dữ liệu hay benchmark đánh giá chuẩn hóa nào được công bố rộng rãi. Vì vậy, nhóm tiến hành **đánh giá thủ công dựa trên một tập các kịch bản thử nghiệm** do nhóm tự xây dựng.

-   **Xây dựng kịch bản:** Thiết kế ~20-30 kịch bản hội thoại mẫu bao gồm các trường hợp sử dụng chính:
    -   Hỏi thông tin sản phẩm cụ thể (giá, mô tả, tầng hương...).
    -   Yêu cầu tư vấn (theo giới tính, mùa, dịp, sở thích mùi hương...).
    -   Yêu cầu so sánh 2-3 sản phẩm.
    -   Kiểm tra tồn kho.
    -   Các câu hỏi kiến thức chung về nước hoa.
    -   Các câu chào hỏi, cảm ơn.
    -   Các câu hỏi/yêu cầu không rõ ràng, không liên quan, hoặc nằm ngoài khả năng.
-   **Thực hiện đánh giá:** Nhóm thực hiện tương tác với chatbot theo các kịch bản đã xây dựng.
-   **Ghi nhận và chấm điểm:** Với mỗi tương tác, ghi nhận lại phản hồi của chatbot và đánh giá theo từng tiêu chí (ví dụ: thang điểm 1-5 hoặc nhận xét định tính).
    -   Độ chính xác thông tin: So sánh với DB SQLite.
    -   Tính hữu ích: Đánh giá chủ quan dựa trên yêu cầu.
    -   Khả năng hiểu: Phân tích xem agent/LLM có gọi đúng tool, trích xuất đúng entity không.
    -   Tính tự nhiên: Đọc và cảm nhận văn phong.
    -   Xử lý tình huống: Quan sát phản hồi trong các kịch bản đặc biệt.
    -   Tốc độ: Đo thời gian phản hồi (có thể dùng `time` hoặc quan sát).

### 5.3. Kết quả và Phân tích

Qua quá trình đánh giá thủ công với các kịch bản thử nghiệm, nhóm ghi nhận các điểm chính sau:

-   **Độ chính xác thông tin (Điểm: 4/5):**
    -   **Điểm mạnh:** Thông tin về giá, tồn kho, mô tả cơ bản khi được hỏi trực tiếp về sản phẩm cụ thể thường chính xác do truy xuất trực tiếp từ SQLite.
    -   **Điểm yếu:** Đôi khi có thể nhầm lẫn tên sản phẩm nếu người dùng nhập không rõ ràng, dẫn đến truy xuất sai thông tin.
-   **Tính hữu ích của tư vấn (Điểm: 3/5):**
    -   **Điểm mạnh:** Đưa ra được gợi ý phù hợp với các tiêu chí rõ ràng (ví dụ: "nước hoa nam mùa hè"). Có khả năng gợi ý dựa trên tìm kiếm ngữ nghĩa từ FAISS.
    -   **Điểm yếu:** Khả năng tư vấn sâu, cá nhân hóa (ví dụ: dựa trên tính cách, phong cách cụ thể) còn hạn chế. Các gợi ý đôi khi còn chung chung, chưa thực sự nổi bật.
-   **Khả năng hiểu yêu cầu (Điểm: 3.5/5):**
    -   **Điểm mạnh:** Hiểu tốt các yêu cầu đơn giản, trực tiếp (hỏi giá, tồn kho, mô tả). Phân loại được các ý định cơ bản.
    -   **Điểm yếu:** Gặp khó khăn với các yêu cầu phức tạp, nhiều ý định lồng nhau hoặc diễn đạt không rõ ràng. Trích xuất entity đôi khi còn sót hoặc sai.
-   **Tính tự nhiên của hội thoại (Điểm: 4/5):**
    -   **Điểm mạnh:** Phản hồi nhìn chung mạch lạc, đúng ngữ pháp tiếng Việt, văn phong lịch sự nhờ fine-tuning trên dataset hội thoại.
    -   **Điểm yếu:** Đôi khi câu trả lời còn hơi máy móc, lặp lại cấu trúc. Chưa thể hiện được sự linh hoạt, ứng biến như người thật.
-   **Khả năng xử lý các tình huống (Điểm: 3.5/5):**
    -   **Điểm mạnh:** Có thể thông báo hết hàng, từ chối yêu cầu không liên quan, trả lời các câu hỏi chung.
    -   **Điểm yếu:** Phản ứng với các tình huống bất ngờ hoặc phàn nàn của khách hàng còn cứng nhắc. Khả năng yêu cầu làm rõ thông tin chưa được tối ưu.
-   **Tốc độ phản hồi (Điểm: 2.5/5):**
    -   **Phân tích:** Thời gian phản hồi trung bình dao động từ 5-10 giây, đôi khi lâu hơn đối với các yêu cầu cần RAG phức tạp (gọi FAISS, SQLite và LLM). Tốc độ này có thể ảnh hưởng đến trải nghiệm người dùng. Nguyên nhân chính là độ trễ của việc gọi LLM (dù đã quantization) và các bước xử lý trong agent.

**Phân tích chung:**

-   **Điểm mạnh:** Chatbot thể hiện khả năng cung cấp thông tin sản phẩm khá chính xác (dựa trên dữ liệu SQLite), đưa ra được những gợi ý cơ bản khi có yêu cầu rõ ràng, và xử lý tương đối tốt các câu hỏi về tồn kho/giá cả nhờ cơ chế RAG kết hợp. Mô hình fine-tuned cho thấy sự am hiểu nhất định về thuật ngữ và các yếu tố cơ bản của nước hoa so với mô hình gốc. Việc truy xuất thông tin tồn kho từ SQLite giúp đảm bảo tính nhất quán của dữ liệu tại thời điểm truy vấn.
-   **Điểm yếu:** Khả năng tư vấn sâu và cá nhân hóa còn hạn chế, đặc biệt khi yêu cầu người dùng phức tạp hoặc mang tính chủ quan cao. Chatbot đôi khi chưa hoàn toàn nắm bắt được ngữ cảnh kéo dài hoặc các sắc thái tinh tế trong yêu cầu. Tốc độ phản hồi có độ trễ nhất định, ảnh hưởng đến trải nghiệm người dùng, chủ yếu do các bước xử lý trong RAG và thời gian inference của LLM.

Nhìn chung, kết quả đánh giá thủ công cho thấy hướng tiếp cận của nhóm là khả thi và có tiềm năng. Tuy nhiên, để chatbot thực sự đạt đến mức độ tinh vi và hiệu quả như một chuyên gia tư vấn thực thụ, cần có những cải tiến đáng kể về dữ liệu, thuật toán và tối ưu hóa hệ thống.

---

## **CHƯƠNG 6: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN**

### 6.1. Kết luận

Đề tài đã nghiên cứu và triển khai thành công hệ thống chatbot tư vấn và chăm sóc khách hàng chuyên dụng cho cửa hàng nước hoa, ứng dụng Mô hình Ngôn ngữ lớn Qwen2.5-1.5B kết hợp kỹ thuật RAG. Nhóm đã đạt được các kết quả chính sau:

-   **Xây dựng và công bố thành công bộ dữ liệu fine-tuning chuyên ngành nước hoa** (`phatvucoder/perfume-assistant` với hơn 3300 mẫu), đóng góp một tài nguyên quan trọng cho cộng đồng.
-   **Thực hiện fine-tuning hiệu quả mô hình Qwen2.5-1.5B** bằng kỹ thuật LoRA và Quantization 4-bit, tạo ra mô hình `Qwen2.5-1.5B-Perfumassist` chuyên biệt và tối ưu tài nguyên.
-   **Thiết kế và triển khai kiến trúc RAG kết hợp FAISS** (tìm kiếm ngữ nghĩa) và **SQLite** (dữ liệu cấu trúc, tồn kho), đảm bảo cung cấp thông tin vừa linh hoạt vừa chính xác tại thời điểm truy vấn.
-   **Xây dựng luồng xử lý chatbot hoàn chỉnh bằng LangChain,** có khả năng phân tích yêu cầu, truy xuất kiến thức, kiểm tra tồn kho, và tạo phản hồi phù hợp.
-   **Triển khai giao diện người dùng thân thiện bằng Chainlit.**

Kết quả đánh giá thủ công cho thấy chatbot có khả năng đáp ứng các yêu cầu cơ bản về cung cấp thông tin và tư vấn ở mức độ nhất định. Hệ thống đã chứng minh tiềm năng của việc ứng dụng LLM và RAG trong việc tạo ra các trợ lý ảo thông minh, chuyên sâu cho các lĩnh vực kinh doanh cụ thể.

### 6.2. Hạn chế của Đề tài

-   **Dữ liệu huấn luyện:** Mặc dù đã tự xây dựng, bộ dữ liệu fine-tuning (`perfume-assistant`) vẫn còn hạn chế về số lượng và chiều sâu kiến thức so với sự phức tạp của lĩnh vực nước hoa, đặc biệt là các kiến thức niche hoặc các tình huống tư vấn tinh tế.
-   **Đánh giá:** Việc đánh giá chỉ dừng lại ở mức độ thủ công theo kịch bản, thiếu tính khách quan và toàn diện do chưa có benchmark chuẩn. Kết quả đánh giá có thể bị ảnh hưởng bởi góc nhìn chủ quan của nhóm.
-   **Tối ưu hiệu năng:** Tốc độ phản hồi và chi phí tính toán khi gọi LLM/RAG chưa được tối ưu hóa triệt để. Độ trễ hiện tại có thể ảnh hưởng tiêu cực đến trải nghiệm người dùng trong môi trường thực tế.
-   **Tư vấn chuyên sâu:** Khả năng đưa ra lời khuyên tinh tế, thực sự cá nhân hóa dựa trên các yếu tố trừu tượng (tính cách, tâm trạng, phong cách thời trang...) vẫn còn hạn chế.
-   **Cập nhật dữ liệu:** Cơ chế cập nhật dữ liệu tồn kho và sản phẩm mới trong SQLite hiện đang là thủ công, chưa có giải pháp tự động hóa.

### 6.3. Hướng Phát triển Tương lai

Để nâng cao hơn nữa chất lượng và hiệu quả của hệ thống, nhóm đề xuất các hướng phát triển chính sau:

1.  **Mở rộng và Làm giàu Dữ liệu Huấn luyện:** Tiếp tục thu thập, tinh lọc và bổ sung dữ liệu huấn luyện (`perfume-assistant`) với:
    -   Các kiến thức chuyên sâu hơn (thành phần hiếm, lịch sử thương hiệu, xu hướng mùi hương niche...).
    -   Nhiều tình huống tư vấn phức tạp, đa dạng hơn (so sánh nhiều sản phẩm, tư vấn theo bộ sưu tập, xử lý phàn nàn tinh tế...).
    -   Dữ liệu về các thương hiệu và sản phẩm mới.
2.  **Tối ưu Prompt Engineering:** Nghiên cứu và áp dụng các kỹ thuật thiết kế prompt tiên tiến:
    -   Few-shot prompting: Cung cấp ví dụ trong prompt để hướng dẫn LLM tốt hơn.
    -   Chain-of-Thought (CoT): Yêu cầu LLM suy nghĩ từng bước trước khi trả lời.
    -   Self-Consistency: Sinh nhiều câu trả lời và chọn câu trả lời nhất quán nhất.
    -   Tối ưu cấu trúc prompt để giảm số lượng token, tăng tốc độ và giảm chi phí.
3.  **Xây dựng Benchmark Đánh giá Chuyên sâu:** Đầu tư xây dựng một bộ dữ liệu và quy trình đánh giá (benchmark) chuẩn hóa, đa diện, dành riêng cho việc đo lường hiệu quả của chatbot tư vấn nước hoa. Benchmark này nên bao gồm nhiều khía cạnh (độ chính xác, tính hữu ích, độ tự nhiên, khả năng xử lý tình huống...) và có thể được sử dụng để so sánh các mô hình, kỹ thuật khác nhau một cách khách quan.
4.  **Áp dụng Kỹ thuật Quantization Nâng cao:** Khám phá và triển khai các phương pháp quantization tiên tiến hơn như AWQ (Activation-aware Weight Quantization), GPTQ, GGUF (để chạy trên CPU/GPU hiệu quả hơn) hoặc các kỹ thuật khác để giảm mạnh hơn nữa kích thước mô hình và tăng tốc độ inference, giúp việc triển khai trở nên hiệu quả hơn mà vẫn đảm bảo chất lượng đầu ra.
5.  **Tích hợp Cập nhật Tồn kho Real-time:** Xây dựng cơ chế kết nối và đồng bộ dữ liệu tự động giữa cơ sở dữ liệu SQLite của chatbot với hệ thống quản lý bán hàng (POS) hoặc kho thực tế của cửa hàng (ví dụ: qua API) để đảm bảo thông tin tồn kho luôn chính xác và cập nhật.
6.  **Cải thiện khả năng cá nhân hóa:** Nghiên cứu tích hợp thông tin người dùng (lịch sử mua hàng, sở thích đã lưu - nếu có sự đồng ý) để đưa ra gợi ý cá nhân hóa tốt hơn.
7.  **Tối ưu Retriever:** Thử nghiệm các mô hình embedding khác, các loại index FAISS khác, hoặc kỹ thuật re-ranking để cải thiện chất lượng kết quả truy xuất từ RAG.

---

## **TÀI LIỆU THAM KHẢO**

-   Nguồn dataset fragrance_collection: [https://github.com/rawanalqarni/Perfumes_Recommender](https://github.com/rawanalqarni/Perfumes_Recommender)
-   Dataset của nhóm: [https://huggingface.co/datasets/phatvucoder/perfume-assistant](https://huggingface.co/datasets/phatvucoder/perfume-assistant)
-   Source code của nhóm: [https://github.com/phatvucoder/Perfume-Assistant](https://github.com/phatvucoder/Perfume-Assistant)
-   Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. __Advances in neural information processing systems__,1 30.
-   Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., ... & Chen, W. (2021). Lora: Low-rank adaptation of large language models. __arXiv preprint arXiv:2106.09685__.2
-   Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2022). Llm. int8 (): 8-bit matrix multiplication for transformers at scale. __arXiv preprint arXiv:2208.07339__.
-   Dettmers,3 T., Lewis, M., Belkada, Y., & Zettlemoyer, L. (2023). Qlora: Efficient finetuning of quantized llms. _arXiv preprint arXiv:2305.14314_.
-   Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive nlp tasks. __Advances in Neural Information Processing4_ Systems_, 33, 9459-9474.
-   LangChain Documentation: [https://python.langchain.com/](https://python.langchain.com/)
-   Chainlit Documentation: [https://docs.chainlit.io/](https://docs.chainlit.io/)
-   Hugging Face Transformers: [https://huggingface.co/docs/transformers/index](https://huggingface.co/docs/transformers/index)
-   Qwen Technical Report (Refer to specific Qwen model papers if available)

---

## **PHỤ LỤC**

### **Phụ lục A: Chi tiết Cấu hình và Code Snippet Fine-tuning**

```Python
from datasets import load_dataset
from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
from trl import SFTTrainer, SFTConfig
from peft import LoraConfig
import numpy as np
import torch

# ======= LOAD DATASET =======
dataset = load_dataset("phatvucoder/perfume-assistant")
print(dataset)
print(f"Number of examples: {len(dataset['train'])}")
print("Example:", dataset['train'][0])

# ======= LOAD TOKENIZER =======
model_id = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

# ======= FORMAT USING CHAT TEMPLATE =======
def format_conversation(example):
    # Extract messages from the example
    messages = example["messages"]
    # Apply the chat template
    formatted_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False # Important for training
    )
    return {"text": formatted_text}

train_data = dataset["train"].map(
    format_conversation,
    remove_columns=dataset["train"].column_names
)
val_data = dataset["validation"].map(
    format_conversation,
    remove_columns=dataset["validation"].column_names
)

# ======= CHECK LENGTHS (Optional but recommended) =======
def get_token_length(example):
    # Tokenize the text to get input_ids length
    return {"length": len(tokenizer(example["text"])["input_ids"])}

token_lengths = train_data.map(
    get_token_length,
    remove_columns=train_data.column_names
)["length"]

print(f"\n📏 Max token length: {max(token_lengths)}")
print("📊 90% percentile:", int(np.percentile(token_lengths, 90)))
print("📊 95% percentile:", int(np.percentile(token_lengths, 95)))
print("📊 99% percentile:", int(np.percentile(token_lengths, 99)))
# (Use this info to set max_seq_length)

# ======= FIX SPECIAL TOKENS =======
# Ensure pad token is set; often use eos_token if pad_token is None
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    print("Set pad_token to eos_token")

# ======= LOAD MODEL W/ QUANTIZATION =======
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,                # Load model in 4-bit
    bnb_4bit_compute_dtype=torch.float16, # Compute dtype for stability
    bnb_4bit_quant_type="nf4",        # Quantization type (NormalFloat 4-bit)
    bnb_4bit_use_double_quant=True,   # Enable double quantization
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config, # Apply quantization config
    device_map="auto",              # Automatically map model layers to devices (GPU/CPU)
    trust_remote_code=True,         # Trust code from the model hub (necessary for some models)
)

# Prepare model for PEFT training
model.config.use_cache = False # Disable caching for training
model.gradient_checkpointing_enable() # Enable gradient checkpointing to save memory
model.enable_input_require_grads() # Required for gradient checkpointing with PEFT

# ======= LORA CONFIG =======
lora_config = LoraConfig(
    r=16,                           # Rank of the update matrices
    lora_alpha=32,                  # Alpha scaling factor (often 2*r)
    lora_dropout=0.05,              # Dropout probability for LoRA layers
    bias="none",                    # Whether to train bias parameters ("none", "all", or "lora_only")
    task_type="CAUSAL_LM",          # Task type (Causal Language Modeling)
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"] # Modules to apply LoRA
)

# ======= TRAINING CONFIG (SFTConfig) =======
training_args = SFTConfig(
    output_dir="./qwen2.5-1.5B-Instruct-finetuned-perfume", # Directory to save checkpoints
    num_train_epochs=4,             # Number of training epochs
    per_device_train_batch_size=4,  # Batch size per GPU during training
    gradient_accumulation_steps=4,  # Accumulate gradients over 4 steps (effective batch size = 4 * 4 = 16)
    per_device_eval_batch_size=1,   # Batch size per GPU during evaluation
    learning_rate=2e-4,             # Learning rate
    lr_scheduler_type="cosine",     # Learning rate scheduler type
    warmup_ratio=0.05,              # Ratio of training steps for warmup
    max_seq_length=768,             # Maximum sequence length (adjust based on dataset analysis)
    logging_steps=10,               # Log training metrics every 10 steps
    save_steps=20,                  # Save a checkpoint every 20 steps
    eval_steps=20,                  # Evaluate on the validation set every 20 steps
    max_grad_norm=0.5,              # Gradient clipping norm
    fp16=True,                      # Enable mixed precision training (if GPU supports)
    packing=True,                   # Pack multiple short sequences into one (improves training efficiency)
    report_to=["tensorboard"],      # Report metrics to TensorBoard
    eval_strategy="steps",          # Evaluation strategy ('steps' or 'epoch')
    # dataset_text_field="text",    # Specify the text field in the dataset (already done by formatting)
)

# ======= START TRAINING =======
trainer = SFTTrainer(
    model=model,                    # The quantized model prepared for PEFT
    args=training_args,             # Training arguments
    train_dataset=train_data,       # Formatted training dataset
    eval_dataset=val_data,          # Formatted validation dataset
    peft_config=lora_config,        # LoRA configuration
    # tokenizer=tokenizer           # Pass tokenizer if needed by SFTTrainer internals (often inferred)
    # formatting_func=format_conversation # Pass formatting function if not pre-formatted
)

# Set processing_class if needed (might be automatic in newer TRL versions)
# trainer.processing_class = tokenizer

print("Starting training...")
trainer.train()
print("Training finished.")

# Save the final adapter
trainer.save_model() # Saves the adapter weights in the output_dir
print(f"Final LoRA adapter saved in {training_args.output_dir}")

```

_(Code for merging adapter and saving merged model - see Section 4.3.3)_

### **Phụ lục B: Ví dụ Mẫu dữ liệu Huấn luyện (`perfume-assistant`)**

```JSON
[
  {
    "messages": [
      {"role": "system", "content": "Bạn là một chuyên viên tư vấn nước hoa và chăm sóc khách hàng cho shop."},
      {"role": "user", "content": "Tầng hương nào dễ bị 'lão hóa' nhất khi nước hoa để lâu?"},
      {"role": "assistant", "content": "Thông thường, tầng hương đầu (Top notes) là tầng hương dễ bị ảnh hưởng và 'lão hóa' nhất khi nước hoa để lâu. Do chúng thường chứa các phân tử nhẹ, dễ bay hơi và nhạy cảm với oxy hóa (như các note citrus), nên theo thời gian chúng có thể bị mất đi hoặc biến đổi mùi (ví dụ: trở nên chua, gắt hơn), làm thay đổi ấn tượng ban đầu của chai nước hoa."}
    ]
  },
  {
    "messages": [
      {"role": "system", "content": "Bạn là một chuyên viên tư vấn nước hoa và chăm sóc khách hàng lịch sự, chuyên nghiệp. Nhiệm vụ của bạn là hỗ trợ khách hàng về nước hoa và các dịch vụ liên quan, đồng thời từ chối tham gia vào các cuộc trò chuyện có nội dung không phù hợp hoặc không liên quan."},
      {"role": "user", "content": "Bạn có thể nói dối được không?"},
      {"role": "assistant", "content": "Tôi được lập trình để cung cấp thông tin chính xác và trung thực dựa trên dữ liệu được huấn luyện. Mục tiêu của tôi là hỗ trợ bạn một cách đáng tin cậy trong lĩnh vực nước hoa."}
    ]
  },
  {
    "messages": [
      {"role": "system", "content": "Bạn là một chuyên viên tư vấn nước hoa và chăm sóc khách hàng lịch sự, chuyên nghiệp. Nhiệm vụ của bạn là hỗ trợ khách hàng về nước hoa và các dịch vụ liên quan, đồng thời từ chối tham gia vào các cuộc trò chuyện có nội dung không phù hợp hoặc không liên quan."},
      {"role": "user", "content": "Mua hàng ở đây chỉ tổ bực mình."},
      {"role": "assistant", "content": "Tôi rất tiếc về trải nghiệm không tốt của bạn. Để tôi có thể hỗ trợ tốt nhất, bạn vui lòng cho biết vấn đề cụ thể bạn đã gặp phải được không ạ? Ví dụ: vấn đề về sản phẩm, giao hàng, hay tư vấn?"}
    ]
  },
  {
    "messages": [
      {"role": "system", "content": "Bạn là trợ lý AI chuyên tư vấn và gợi ý nước hoa cá nhân hóa."},
      {"role": "user", "content": "Nam, đi chơi Tết Trung Thu với gia đình, cần mùi hương ấm áp, gợi không khí đoàn viên."},
      {"role": "assistant", "content": "Chào bạn, Tết Trung Thu rất hợp với những mùi hương ấm áp, ngọt ngào nhẹ nhàng. Bạn có thể chọn nhóm hương Gourmand (Thực phẩm) với note trà, bánh nướng, hạt sen, hoặc Oriental Woody (Phương Đông Gỗ) với gỗ đàn hương, hổ phách nhẹ. Chúng tạo cảm giác ấm cúng, thân thuộc và gợi nhớ không khí đoàn viên, sum vầy bên gia đình."}
    ]
  }
  ...
]
```