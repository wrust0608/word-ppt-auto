# Các dự án tham khảo và phạm vi sử dụng

Hệ thống chỉ tiếp thu mô hình thiết kế và giao diện phù hợp; không sao chép mã từ các dự án dưới đây.

## Thành phần chạy trực tiếp

### NotebookLM MCP

Nguồn: https://github.com/khengyun/notebooklm-mcp

Vai trò: kết nối Antigravity với notebook, nguồn và phiên hỏi đáp qua STDIO. Đây là tích hợp cộng đồng dựa trên NotebookLM; phiên đăng nhập hoặc giao diện nội bộ có thể thay đổi. Vì vậy skill dùng hợp đồng nghiệp vụ trung lập thay vì khóa cứng tên tool.

### OfficeCLI

Nguồn: https://github.com/iOfficeAI/OfficeCLI

Vai trò: tạo, đọc, sửa, kiểm tra và render DOCX trong vòng lặp xuất → xem → sửa. Chỉ gọi tại G6 sau khi Markdown đã duyệt.

## Thành phần tùy chọn

### AnySearch Skill

Nguồn: https://github.com/anysearch-ai/anysearch-skill

Vai trò: mở rộng tìm kiếm nhiều nguồn và truy xuất toàn văn. Kết quả chỉ là ứng viên cho tới khi được nhập và xác minh trong NotebookLM.

### RetainPDF

Nguồn: https://github.com/wxyhgk/retain-pdf

Vai trò: xử lý tài liệu scan, OCR, công thức hoặc nội dung cần giữ bố cục. Kết quả OCR phải được đối chiếu trực quan trước khi trở thành bằng chứng.

## Tham chiếu thiết kế, không phải dependency

### TencentDB Agent Memory

Nguồn: https://github.com/TencentCloud/TencentDB-Agent-Memory

Áp dụng ý tưởng bộ nhớ phân lớp vào PROJECT_STATE.md: quyết định bền vững, trạng thái tác vụ, khoảng trống bằng chứng và gói bàn giao. Phiên bản này không triển khai dịch vụ bộ nhớ riêng.

### Prime Agent

Nguồn: https://github.com/PrimeIntellect-ai/prime-agent

Áp dụng mẫu bàn giao ngữ cảnh và khôi phục tiến độ từ artifact đã lưu; không dùng Prime Agent làm runtime.

### Parlant

Nguồn: https://github.com/emcie-co/parlant

Áp dụng guideline có điều kiện, cổng quyết định, ranh giới gọi công cụ và truy vết quyết định; không dùng Parlant làm dependency.

## Nguyên tắc thay thế

Một tích hợp có thể được thay khi vẫn bảo toàn hợp đồng của hệ thống:

- nguồn học thuật phải có danh tính và vị trí truy vết;
- claim matrix không phụ thuộc nhà cung cấp;
- Markdown vẫn là nguồn chuẩn;
- cổng duyệt không thay đổi;
- khi công cụ bằng chứng lỗi, viết có căn cứ phải dừng;
- không để khóa, cookie hoặc hồ sơ đăng nhập trong workspace.

