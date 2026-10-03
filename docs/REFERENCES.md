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

### Writing Skills

Nguồn: https://github.com/msimchowitz/writing-skills

Áp dụng cách tách lượt viết, academic voice, cadence, paper writing và whole-document pass. Hệ thống hiện tại vẫn dùng một skill lõi với progressive disclosure, không cài runtime của repo này.

### Academic Writing Skill

Nguồn: https://github.com/felixschrimpff/academic-writing-skill

Áp dụng nguyên tắc hiệu chỉnh theo ngành/loại phần và dùng khoảng phù hợp thay cho lệnh cấm tuyệt đối. Các con số/corpus của repo không được sao chép thành chuẩn cho luận văn tiếng Việt khi chưa có kiểm chứng riêng.

### Humanize rule catalogs

Nguồn: https://github.com/kimhons/humanize và https://github.com/keez97/humanizer

Áp dụng ý tưởng phát hiện citation laundering, phóng đại ý nghĩa, pseudo-precision, cấu trúc ba vế và nhịp văn bản đều. Không dùng điểm “human”, không tối ưu AI detector và không chèn lỗi có chủ ý.

### Vale

Nguồn: https://github.com/vale-cli/vale và https://github.com/vale-cli/agent-tools

Áp dụng mô hình prose lint có rule giải thích được, vị trí dòng, test fixture và tích hợp CI. Phiên bản hiện tại dùng linter Python tiếng Việt tự chứa; Vale không phải dependency bắt buộc.

### STORM và PaperQA

Nguồn: https://github.com/stanford-oval/storm và https://github.com/Future-House/paper-qa

STORM chỉ gợi ý cách đặt câu hỏi đa góc nhìn trước khi lập đề cương. PaperQA gợi ý cách truy vết claim–evidence. NotebookLM và source ledger vẫn là hợp đồng bằng chứng chính thức của hệ thống.

## Nguyên tắc thay thế

Một tích hợp có thể được thay khi vẫn bảo toàn hợp đồng của hệ thống:

- nguồn học thuật phải có danh tính và vị trí truy vết;
- claim matrix không phụ thuộc nhà cung cấp;
- Markdown vẫn là nguồn chuẩn;
- cổng duyệt không thay đổi;
- khi công cụ bằng chứng lỗi, viết có căn cứ phải dừng;
- không để khóa, cookie hoặc hồ sơ đăng nhập trong workspace.

