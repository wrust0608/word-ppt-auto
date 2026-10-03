# Cài đặt Antigravity và NotebookLM

## 1. Yêu cầu

- Antigravity IDE hoặc Antigravity CLI.
- Python 3.10 trở lên.
- `uv` có trong `PATH`.
- Tài khoản Google có quyền truy cập notebook cần dùng.
- OfficeCLI nếu cần xuất và kiểm tra DOCX.

NotebookLM MCP trong cấu hình này là phần mềm cộng đồng và có thể bị ảnh hưởng khi NotebookLM thay đổi giao diện hoặc API nội bộ. Không đưa cookie, token hoặc browser profile vào Git.

## 2. Cài NotebookLM MCP

Tại thư mục workspace:

```powershell
uv init --bare
uv add notebooklm-mcp
uv run notebooklm-mcp init "<NOTEBOOK_URL>" -o notebooklm-config.local.json
```

Sau lệnh `init`, đổi tên hoặc lưu cấu hình thành `notebooklm-config.local.json` tại thư mục gốc. File này đã được loại khỏi Git.

Nếu phiên bản CLI tạo tên file khác, cập nhật đối số `-c` trong `.agents/mcp_config.json` thay vì chép cookie vào cấu hình MCP.

## 3. Bật MCP trong Antigravity

Mở `.agents/mcp_config.json` và đổi:

```json
"disabled": true
```

thành:

```json
"disabled": false
```

Sau đó reload MCP trong Antigravity. Cấu hình workspace của Antigravity hỗ trợ server STDIO bằng `command` và `args`; không đổi trường này thành `url`.

## 4. Kiểm tra kết nối

Trong Antigravity, yêu cầu agent:

1. Liệt kê tool của server `notebooklm`.
2. Chạy `healthcheck` nếu tool có mặt.
3. Đọc notebook mặc định.
4. Liệt kê nguồn.
5. Đặt một câu hỏi có đáp án đã biết và trả về tên nguồn hỗ trợ.

Tên tool có thể thay đổi giữa các phiên bản. Agent phải khám phá tool hiện có thay vì giả định cứng tên hàm. Hợp đồng nghiệp vụ tối thiểu cần có: chọn notebook, liệt kê nguồn, thêm nguồn hoặc hướng dẫn người dùng thêm nguồn, và chat dựa trên notebook.

## 5. OfficeCLI

Cài OfficeCLI theo tài liệu của dự án rồi kiểm tra:

```powershell
officecli --help
```

Skill chỉ sử dụng OfficeCLI ở cổng xuất bản. Nếu chưa cài, các cổng nghiên cứu và soạn Markdown vẫn hoạt động bình thường.

## 6. Thay thế NotebookLM MCP

Nếu package hiện tại ngừng hoạt động:

1. Chọn MCP khác có chức năng tương đương.
2. Thay duy nhất mục `notebooklm` trong `.agents/mcp_config.json`.
3. Giữ nguyên `SOURCE_LEDGER.md`, `CLAIM_MATRIX.md` và quy tắc chỉ trích dẫn nguồn gốc.
4. Chạy lại năm bước kiểm tra kết nối trước khi tiếp tục dự án.

Không để chi tiết tên tool của một MCP cụ thể lan vào skill lõi.

