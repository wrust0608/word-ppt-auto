# Phiếu hiệu chỉnh giọng tác giả

- Trạng thái: `READY_FOR_AUTHOR_REVIEW`
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

## Đoạn thử 300 từ

Trong quy trình đánh giá dịch vụ SMB, trạng thái `open` của cổng TCP 445 chỉ xác nhận rằng máy đích đang chấp nhận kết nối trên cổng thường dùng cho Direct-hosted SMB. Kết quả này chưa cho biết dialect nào được máy chủ hỗ trợ, SMBv1 đã bị vô hiệu hóa hay hệ điều hành đã cài bản vá MS17-010. Việc suy diễn trực tiếp từ cổng mở sang kết luận “có lỗ hổng” vì vậy làm mất ranh giới giữa khả năng tiếp cận dịch vụ và trạng thái an toàn của thành phần xử lý SMB. Nhận định về cổng 445 được đối chiếu với tài liệu Direct host SMB của Microsoft trong S002.

Sau bước quét cổng, phép kiểm tra cần chuyển sang tầng giao thức. Client gửi bản tin thương lượng để xác định dialect mà server chấp nhận; chỉ khi máy chủ đồng ý SMBv1 mới có cơ sở tiếp tục kiểm tra dấu hiệu liên quan đến MS17-010. Kịch bản `smb-vuln-ms17-010.nse` sử dụng một yêu cầu SMB cụ thể và đối chiếu mã trạng thái phản hồi, thay vì coi tên dịch vụ hoặc banner là bằng chứng đủ. Mã nguồn kịch bản trong S018 cho phép truy vết logic kiểm tra, nhưng kết quả `VULNERABLE` của NSE vẫn không thay thế bằng chứng khai thác thành công.

Đề tài vì vậy duy trì bốn mức đánh giá tách biệt: cổng có thể tiếp cận, dialect SMBv1 được chấp nhận, phản hồi phù hợp với hệ thống chưa vá và khả năng thực thi mã trong lab. Cách phân tầng này giúp người đọc nhận ra chính xác bằng chứng nào đã có ở từng bước, đồng thời giới hạn kết luận khi dữ liệu chưa đủ. Hoạt động ở mức khai thác chỉ được thực hiện trong mạng ảo cô lập, có snapshot và điều kiện dừng, phù hợp với nguyên tắc lập kế hoạch kiểm thử của NIST SP 800-115 trong S024. Nếu chưa có log hoặc kết quả chạy thật, báo cáo giữ nhãn `[CẦN DỮ LIỆU]` thay vì mô tả một phiên khai thác giả định như kết quả đã quan sát.

## Nội dung cần tác giả xác nhận

1. Giữ ngôi thứ ba với cách gọi “đề tài” và “nhóm thực hiện”, hay cho phép “chúng tôi” trong phần phương pháp?
2. Mức thuật ngữ tiếng Anh trong đoạn thử có phù hợp không?
3. Tác giả muốn giữ câu ghép tương đối dài hay ưu tiên câu ngắn hơn tại phần phương pháp?
4. Tác giả sửa trực tiếp ít nhất ba vị trí trong đoạn thử; hệ thống sẽ ghi các sửa đổi đó thành quy tắc thay vì chỉ ghi “đã duyệt”.

## Điều kiện khóa

Không chuyển phiếu này sang `LOCKED` cho tới khi có phản hồi thật của tác giả. Trong thời gian chờ, agent được dùng các đặc điểm đã quan sát từ mẫu gốc nhưng không được sáng tác dấu ấn cá nhân mới.
