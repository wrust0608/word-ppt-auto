# Thesis Research and Writing System

Hệ thống hỗ trợ Antigravity nghiên cứu và soạn luận văn có kiểm chứng bằng NotebookLM. Hệ thống tách riêng năng lực lõi, quy định của cơ sở đào tạo và hồ sơ từng đề tài để có thể tái sử dụng cho nhiều ngành.

## Bắt đầu nhanh

1. Mở thư mục này bằng Antigravity.
2. Làm theo [hướng dẫn cài đặt](docs/SETUP.md) để kết nối NotebookLM MCP và OfficeCLI.
3. Sao chép các mẫu trong `templates/` vào một thư mục dự án mới dưới `work/<project-slug>/`.
4. Điền `PROJECT_PROFILE.md` và chọn hồ sơ quy định phù hợp. Hồ sơ HUIT tham khảo có tại `profiles/HUIT_2024.md`.
5. Mở [ANTIGRAVITY_MASTER_PROMPT.md](prompts/ANTIGRAVITY_MASTER_PROMPT.md), thay các giá trị trong phần `THÔNG TIN DỰ ÁN`, rồi gửi toàn bộ prompt cho Antigravity.

Antigravity sẽ tự phát hiện skill tại `.agents/skills/thesis-research-and-writing/`. Quy trình bắt buộc dừng tại các cổng duyệt; hệ thống không được tự tạo nguồn, dữ liệu nghiên cứu hay kết quả thực nghiệm.

## Tiếp tục công việc trên thiết bị khác

Đọc [HANDOFF.md](HANDOFF.md), sau đó mở `PROJECT_STATE.md` trong đúng thư mục dưới `work/`. Các tệp trạng thái và artifact dự án được version hóa; thông tin đăng nhập NotebookLM, môi trường ảo, cache và tệp tạm không được đưa vào Git.

## Thành phần chính

- `.agents/skills/thesis-research-and-writing/`: năng lực nghiên cứu, lập luận, viết, kiểm chứng và xuất bản.
- `.agents/mcp_config.json`: cấu hình NotebookLM MCP ở trạng thái tắt an toàn cho tới khi hoàn thành đăng nhập.
- `templates/`: hợp đồng dữ liệu Markdown cho mỗi dự án.
- `profiles/`: quy định theo trường hoặc chương trình đào tạo.
- `prompts/`: prompt hoàn chỉnh để giao việc cho Antigravity.
- `examples/`: ca kiểm thử; không phải quy tắc mặc định của hệ thống.

## Nguyên tắc cốt lõi

- Markdown là nguồn nội dung chuẩn; DOCX là sản phẩm xuất bản.
- NotebookLM hỗ trợ tìm và tổng hợp, nhưng tài liệu gốc mới là nguồn được trích dẫn.
- Mọi luận điểm quan trọng phải truy ngược được tới bằng chứng.
- Mỗi chương phải trả lời một phần câu hỏi nghiên cứu, không trở thành bản tổng hợp kiến thức chung.
- Nếu thiếu nguồn hoặc dữ liệu, dùng nhãn trạng thái thay vì suy đoán.

## Tài liệu

- [Kiến trúc hệ thống](docs/SYSTEM.md)
- [Cài đặt Antigravity và NotebookLM](docs/SETUP.md)
- [Hướng dẫn vận hành](docs/OPERATING_GUIDE.md)
- [Các dự án tham khảo và phạm vi sử dụng](docs/REFERENCES.md)
- [Bộ kiểm thử nghiệm thu](tests/ACCEPTANCE.md)
