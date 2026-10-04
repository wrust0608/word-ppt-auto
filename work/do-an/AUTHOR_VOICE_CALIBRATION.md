# Phiếu hiệu chỉnh giọng tác giả

- Trạng thái: `APPROVED_CHOICES_RECORDED`
- Ngày lập: 2026-10-04
- Mẫu gốc đã đọc: `inputs/đề mục tham khảo.docx`, 153 đoạn có nội dung; trọng tâm mục 1.1.
- Mục đích: kiểm tra lại hồ sơ giọng trước khi biên tập Chương 1 theo hệ thống mới.

## Đặc điểm quan sát được từ mẫu gốc

- Tác giả đi từ định nghĩa kỹ thuật tới thành phần, luồng xử lý và hệ quả an ninh.
- Câu thường có một quan hệ chính; danh sách được dùng khi phân loại vai trò hoặc các bước giao thức.
- Thuật ngữ tiếng Anh được đặt sau tiếng Việt trong lần xuất hiện đầu tiên, sau đó giữ cách gọi ngắn ổn định.
- Giọng khách quan, ưu tiên chủ thể kỹ thuật cụ thể như client, server, driver, bản tin và công cụ.
- Mẫu gốc có xu hướng khẳng định chắc một số chi tiết mà chưa đặt citation ngay tại câu; hệ thống mới không được bắt chước điểm này.
- Không thấy cơ sở để tự thêm trải nghiệm cá nhân, cảm xúc hoặc quan sát doanh nghiệp ngoài nội dung tác giả đã cung cấp.

## Đoạn thử v2 theo mẫu Tuần 2 (chờ tác giả duyệt)

**Phạm vi đánh giá:** Trạng thái cổng, phiên bản giao thức và dấu hiệu lỗ hổng là ba loại thông tin khác nhau trong quá trình kiểm tra SMB. Cổng TCP 445 là cổng thường dùng cho SMB truyền trực tiếp trên TCP/IP (Direct-hosted SMB), nhưng việc cổng này ở trạng thái `open` chưa cho biết máy chủ hỗ trợ phiên bản SMB nào hoặc đã cài bản vá MS17-010 hay chưa. Nhận định về cổng được đối chiếu với S002; cách phân tầng đánh giá là khung của đề tài trong C003.

**Quy trình kiểm tra:**

1. **Khảo sát khả năng tiếp cận:** Công cụ quét ghi nhận trạng thái cổng TCP 445 của máy đích. Kết quả cổng mở được dùng để xác định bước kiểm tra tiếp theo, chưa dùng để kết luận hệ thống có lỗ hổng.
2. **Thương lượng giao thức (Dialect Negotiation):** Client gửi yêu cầu thương lượng để xác định các phiên bản SMB mà Server chấp nhận. Kết quả này giúp phân biệt khả năng tiếp cận cổng với việc máy chủ hỗ trợ SMBv1; cơ chế giao thức cần đối chiếu S021 và S022.
3. **Kiểm tra dấu hiệu chưa vá:** Kịch bản `smb-vuln-ms17-010.nse` gửi yêu cầu SMB và đối chiếu mã trạng thái phản hồi theo logic trong S018. Kết luận `VULNERABLE` được ghi nhận ở mức dấu hiệu của phép thăm dò, chưa phải bằng chứng khai thác thành công.

**Giới hạn kết luận:** Đề tài phân biệt bốn mức: cổng có thể tiếp cận, SMBv1 được chấp nhận, phản hồi phù hợp với hệ thống chưa vá và khả năng thực thi mã trong lab. Mỗi mức cần bằng chứng tương ứng; kết quả ở mức trước không tự xác nhận mức sau. Quy trình kiểm thử phải xác định phạm vi, được ủy quyền và kiểm soát tác động theo S024. Snapshot và điều kiện dừng là biện pháp của thiết kế lab trong C004. Khi chưa có log hoặc kết quả chạy thật, phần thực nghiệm giữ nhãn `[CẦN DỮ LIỆU]`.

Đoạn này phục vụ hiệu chỉnh giọng, chưa thay thế nội dung Chương 1. Source ID là chú giải làm việc; số IEEE chỉ được gán lại sau khi đối soát nguồn.

### Ba lựa chọn diễn đạt cần tác giả xác nhận

| Vị trí | Phương án A — theo mẫu Tuần 2 | Phương án B |
|---|---|---|
| 1. Cách chia ý | Giữ nhãn “Phạm vi đánh giá”, “Quy trình kiểm tra”, “Giới hạn kết luận” | Viết thành các đoạn liên tục, ít nhãn phụ |
| 2. Thuật ngữ | Giữ “Client”, “Server”; giải thích tiếng Việt kèm thuật ngữ trong ngoặc ở lần đầu | Dùng “máy khách”, “máy chủ” xuyên suốt, chỉ giữ tên bản tin tiếng Anh |
| 3. Nhịp câu | Giữ câu ghép cơ chế → hệ quả khi rõ quan hệ, như đoạn mở | Ưu tiên tách thành câu ngắn hơn, mỗi câu một ý |

Tác giả có thể xác nhận “1A, 2A, 3A” hoặc sửa cụ thể. Mỗi lựa chọn sẽ được ghi thành quy tắc; không tự coi các phương án A là đã được duyệt. Ba lựa chọn này thay cho yêu cầu sửa tay ba chỗ nếu tác giả chọn trực tiếp, phù hợp quy trình “sửa hoặc chọn phương án” của reference academic-register-and-author-voice.md.

## Nội dung cần tác giả xác nhận

1. Giữ ngôi thứ ba với cách gọi “đề tài” và “nhóm thực hiện”, hay cho phép “chúng tôi” trong phần phương pháp?
2. Mức thuật ngữ tiếng Anh trong đoạn thử có phù hợp không?
3. Tác giả muốn giữ câu ghép tương đối dài hay ưu tiên câu ngắn hơn tại phần phương pháp?
4. Tác giả sửa trực tiếp ít nhất ba vị trí trong đoạn thử; hệ thống sẽ ghi các sửa đổi đó thành quy tắc thay vì chỉ ghi “đã duyệt”.

## Điều kiện khóa

Không chuyển phiếu này sang `LOCKED` cho tới khi có phản hồi thật của tác giả. Trong thời gian chờ, agent được dùng các đặc điểm đã quan sát từ mẫu gốc nhưng không được sáng tác dấu ấn cá nhân mới.


## Mẫu bổ sung do tác giả xác nhận ngày 2026-10-04

Tác giả cung cấp `D:/ATTT_DACN_01-BaoCao-Tuan2.docx` và nói: “tôi thường diễn đạt theo cách này”. Đây là xác nhận mẫu đại diện cho cách diễn đạt; không phải xác nhận tính đúng của mọi nội dung kỹ thuật hoặc phê duyệt đoạn thử cũ. Tệp gốc được giữ nguyên, không sao chép vào Git. SHA256: `d38d411924507ea6c2256e3788e79d8f0eb9b8a65bfd98ffc6c3e300daf30899`.

Đã đọc toàn bộ văn bản body, gồm mục 1.1.1–1.1.7 và đề mục 2.1. Các định vị P dưới đây là thứ tự paragraph trong XML, kể cả ô bảng; không phải số trang.

| Đặc điểm | Vị trí trong mẫu | Cách áp dụng |
|---|---|---|
| Nêu khái niệm trực tiếp rồi giải thích chức năng | P4–P6, P92 | Mở bằng chủ thể kỹ thuật và động từ như “là”, “cung cấp”, “vận hành” |
| Chia nội dung bằng nhãn chức năng | P7–P11, P13–P20 | Dùng mục như vai trò, thành phần, quy trình khi nội dung thực sự cần phân loại |
| Mô tả thao tác theo trình tự | P22–P26, P114–P115, P125–P127 | Chủ thể → thao tác → phản hồi; đánh số bước khi trình tự có ý nghĩa |
| Ghép tiếng Việt với thuật ngữ tiếng Anh | P4, P18–P25, P109–P110 | Giải thích tiếng Việt trước, thêm thuật ngữ trong ngoặc; giữ Client/Server khi đã xác định |
| Câu ghép phục vụ cơ chế/hệ quả | P18–P19, P39–P40, P119 | Không ép tất cả về câu ngắn; tách khi một câu chứa nhiều quan hệ độc lập |
| Giọng mô tả khách quan | P14–P16, P100–P101 | Gọi chủ thể cụ thể; mẫu không đủ để suy ra lựa chọn “chúng tôi” trong phần phương pháp |

Các lỗi chính tả như “hhệ”, khẳng định tuyệt đối hoặc chi tiết giao thức chưa có nguồn không được đưa thành quy tắc giọng. Mẫu không tự thay đổi topology, nguồn, số liệu hoặc quyết định LOCKED.

Đây là bằng chứng mới để hiệu chỉnh, chưa ghi nhận tác giả đã sửa ba vị trí hoặc duyệt đoạn thử. Bước 4 giữ READY_FOR_AUTHOR_REVIEW; lượt hiệu chỉnh tiếp theo phải thể hiện ba lựa chọn cụ thể dựa trên mẫu và ghi phản hồi thật của tác giả.


## Phê duyệt ba lựa chọn của tác giả

Ngày 2026-10-04, tác giả chọn rõ: **1B, 2A, 3A**.

1. Viết thành các đoạn liên tục, ít nhãn phụ.
2. Giữ Client/Server; giải thích tiếng Việt kèm thuật ngữ trong ngoặc ở lần đầu.
3. Giữ câu ghép cơ chế → hệ quả khi quan hệ rõ, như đoạn mở.

Ba lựa chọn được ghi thành quy tắc giọng, hoàn tất cổng hiệu chỉnh bước 4. Đây không phải phê duyệt nội dung kỹ thuật, chương hoặc DOCX. Các đoạn “chờ duyệt” phía trên là lịch sử trước phản hồi này.

### Đoạn thử v3 áp dụng các lựa chọn

Trạng thái cổng, phiên bản giao thức và dấu hiệu lỗ hổng là các thông tin khác nhau trong quá trình kiểm tra SMB. Cổng TCP 445 thường dùng cho SMB truyền trực tiếp trên TCP/IP (Direct-hosted SMB), nhưng việc cổng này ở trạng thái `open` chưa cho biết Server hỗ trợ phiên bản SMB nào hoặc đã cài bản vá MS17-010 hay chưa. Kết quả quét cổng vì vậy được dùng để xác định bước kiểm tra tiếp theo, chưa dùng để kết luận hệ thống có lỗ hổng. Cơ sở về cổng được đối chiếu S002; cách phân tầng là khung của đề tài trong C003.

Sau khi xác định khả năng tiếp cận dịch vụ, phép kiểm tra chuyển sang thương lượng giao thức (Dialect Negotiation). Client gửi yêu cầu thương lượng để xác định các phiên bản SMB mà Server chấp nhận; kết quả này giúp phân biệt trạng thái cổng với việc máy chủ hỗ trợ SMBv1. Cơ chế cần đối chiếu S021 và S022. Kịch bản `smb-vuln-ms17-010.nse` tiếp tục gửi yêu cầu SMB và đối chiếu mã trạng thái phản hồi theo logic trong S018. Kết luận `VULNERABLE` được ghi nhận ở mức dấu hiệu của phép thăm dò, chưa phải bằng chứng khai thác thành công.

Đề tài phân biệt bốn mức: cổng có thể tiếp cận, SMBv1 được chấp nhận, phản hồi phù hợp với hệ thống chưa vá và khả năng thực thi mã trong lab. Mỗi mức cần bằng chứng tương ứng; kết quả ở mức trước không tự xác nhận mức sau. Quy trình kiểm thử phải xác định phạm vi, được ủy quyền và kiểm soát tác động theo S024. Snapshot và điều kiện dừng là biện pháp của thiết kế lab trong C004. Khi chưa có log hoặc kết quả chạy thật, phần thực nghiệm giữ nhãn `[CẦN DỮ LIỆU]`.

Source ID là chú giải đối soát, chưa gán lại số IEEE cho chương. V3 là áp dụng lựa chọn diễn đạt đã duyệt, không ghi tác giả đã tự viết hoặc duyệt từng khẳng định trong đoạn này.
