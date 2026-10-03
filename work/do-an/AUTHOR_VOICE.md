# Hồ sơ giọng tác giả

Hồ sơ này được lập dựa trên mẫu văn bản thực tế do tác giả cung cấp trong `work/do-an/inputs/đề mục tham khảo.docx` (phần 1.1) và các quy định đào tạo ngành An toàn thông tin tại HUIT.

## Nguồn nhận diện giọng

- Mẫu văn bản do tác giả viết: `work/do-an/inputs/đề mục tham khảo.docx`
- Phần/trang đã phân tích: Mục 1.1 (1.1.1 đến 1.1.7, gồm 128 dòng văn bản kỹ thuật về SMB)
- Nội dung của mẫu không nên bắt chước: Các lỗi chính tả nhỏ (nếu có), các câu lặp từ hoặc câu bị khuyết dấu câu.
- Ngày tác giả xác nhận hồ sơ: 2026-09-12 (Dự thảo chờ xác nhận)

## Quy ước diễn đạt

- Đại từ/cách xưng hô: Sử dụng ngôi thứ ba khách quan, trung tính; khi cần đề cập đến chủ thể hành động thì dùng "đề tài" hoặc "nhóm thực hiện" (tránh lạm dụng "chúng tôi" hoặc "tôi" trong các phân tích kỹ thuật).
- Mức độ trang trọng: Trang trọng, học thuật kỹ thuật cao, cô đọng, đi thẳng vào bản chất công nghệ.
- Độ dài câu điển hình: Câu ghép từ 20 - 35 từ, có cấu trúc logic rõ ràng (chủ ngữ - vị ngữ - thành phần bổ nghĩa chỉ quan hệ nhân quả, điều kiện tiên quyết).
- Cách chuyển ý thường dùng: Chuyển ý qua quan hệ chức năng và phân tầng kỹ thuật (Từ kiến trúc tổng thể → Thành phần cấp nhân → Luồng bản tin → Tham số an ninh); không dùng các câu mào đầu vô nghĩa.
- Mật độ thuật ngữ phù hợp: Mật độ cao; giữ nguyên các thuật ngữ tiếng Anh chuẩn của giao thức mạng và hệ điều hành: `Named Pipes`, `Session Setup`, `Tree Connect`, `Dialect`, `Negotiate Protocol`, `Direct-hosted SMB`, `Kernel-mode driver`, `srv.sys`, `srv2.sys`.
- Cách giải thích khái niệm: Định nghĩa khái niệm bằng tầng mạng, vai trò, thành phần chịu trách nhiệm và cổng kết nối; sau đó liệt kê các trường hợp/chức năng cụ thể bằng gạch đầu dòng ngắn gọn.
- Thuật ngữ tác giả ưu tiên: Giao thức SMB, thương lượng dialect, thiết lập phiên làm việc, kết nối tài nguyên, driver cấp nhân, lùi cổng (fallback).
- Cụm từ tác giả không muốn dùng: Tránh tuyệt đối các sáo ngữ: "trong bối cảnh hiện nay", "thời đại công nghệ 4.0", "vô cùng quan trọng", "không chỉ... mà còn...", "có thể thấy rằng", "một cách toàn diện và tối ưu".

## Dấu ấn riêng của công trình

- Động cơ chọn đề tài đã xác nhận: Giải quyết nguy cơ mất an toàn hệ thống từ giao thức SMBv1 còn sót lại trong mạng doanh nghiệp; làm rõ cơ chế lỗ hổng mức nhân MS17-010 và xây dựng quy trình kiểm thử có kiểm soát rủi ro.
- Những lựa chọn do tác giả trực tiếp đưa ra:
  1. Phân định rạch ròi 4 cấp độ: Phát hiện cổng 445 mở → Nhận diện phiên bản SMBv1 → Dấu hiệu nghi ngờ qua NSE → Xác minh lỗ hổng bằng phản hồi gói tin chuẩn.
  2. Bắt buộc kiểm thử trong mô hình mạng ảo cô lập (Host-only) và có cơ chế snapshot phục hồi.
  3. Đề xuất giải pháp phòng thủ đa tầng kết hợp: Cập nhật bản vá, vô hiệu hóa hoàn toàn SMBv1, kiểm soát tường lửa cổng 445 và phân đoạn mạng.
- Lý do thật cho từng lựa chọn: Tránh dương tính giả; ngăn chặn nguy cơ crash hệ thống (BSOD) do corrupt kernel pool khi chạy module khai thác; và đảm bảo không phá vỡ tính tương thích của hệ thống mạng.
- Quan sát hoặc khó khăn tác giả thực sự gặp: Khó khăn trong việc cân bằng giữa yêu cầu bảo mật (tắt SMBv1) và tính tương thích với các thiết bị ngoại vi đời cũ (máy in, máy scan, NAS cũ) trong mạng nội bộ.
- Điều tác giả đồng ý nhận định: Đóng cổng TCP 445 tại tường lửa biên chỉ là giải pháp tối thiểu, không thể thay thế việc hardening nội bộ vì nguy cơ lây lan ngang (lateral movement).
- Điều tác giả chưa xác nhận: Số liệu đo lường định lượng cụ thể về độ trễ truyền dữ liệu khi bật SMB Encryption / Signing (hiện tại giữ nhãn `[CẦN DỮ LIỆU]`).

## Ranh giới

- Ngôi viết được trường cho phép: Ngôi thứ ba khách quan ("đề tài", "nhóm thực hiện").
- Mức độ thể hiện quan điểm cá nhân: Chỉ thể hiện qua phân tích kỹ thuật, đối chiếu tiêu chí và khuyến nghị có căn cứ; không biểu lộ cảm xúc cá nhân.
- Thông tin cá nhân không được đưa vào: Không đưa số điện thoại cá nhân hay thông tin riêng tư vào phần nội dung học thuật chính.
- Nội dung phải gắn [CẦN TÁC GIẢ XÁC NHẬN]: Bất kỳ nhận định nào về hiện trạng hạ tầng cụ thể tại một cơ quan/doanh nghiệp ngoài phạm vi lab.

## Mẫu hiệu chỉnh (Calibration Sample - 310 từ)

> **Đoạn thử nghiệm hiệu chỉnh văn phong kỹ thuật (về cơ chế lựa chọn cổng dịch vụ SMB):**
>
> "Để thiết lập kênh truyền thông giữa Client và Server, dịch vụ Server Message Block (SMB) trên hệ điều hành Windows sử dụng hai cổng mạng tiêu chuẩn: TCP 139 và TCP 445. Cổng TCP 139 vận hành trên nền tảng NetBIOS over TCP/IP (NBT), đóng vai trò lớp bao bọc trung gian đòi hỏi hai máy trạm phải hoàn tất phiên NetBIOS Session Service và phân giải tên máy tính qua giao thức NetBIOS trước khi truyền tải các bản tin SMB. Ngược lại, cổng TCP 445 được tích hợp từ phiên bản Windows 2000 cho phép triển khai cơ chế Direct-hosted SMB, truyền trực tiếp các gói tin SMB trên nền TCP/IP mà không phụ thuộc vào tiêu đề NetBIOS, qua đó giảm độ trễ đóng gói dữ liệu và hỗ trợ phân giải địa chỉ thông qua hệ thống phân giải tên miền (DNS).
>
> Trong quá trình khởi tạo kết nối chia sẻ tài nguyên, ngăn xếp mạng của Windows áp dụng cơ chế bắt tay đồng thời: hệ điều hành gửi song song hai gói tin TCP SYN đến cả cổng 445 và cổng 139 của máy đích. Nếu cổng 445 phản hồi gói tin SYN-ACK trước, kết nối Direct-hosted SMB sẽ được thiết lập ngay lập tức, đồng thời gói tin gửi tới cổng 139 bị hủy bỏ (TCP RST). Trong trường hợp cổng 445 bị chặn bởi tường lửa hoặc hệ thống máy chủ chỉ hỗ trợ các chuẩn Windows cũ, quá trình kết nối sẽ tự động lùi bước (fallback) về cổng TCP 139 thông qua NetBIOS. Cơ chế này đảm bảo tính tương thích ngược, nhưng đồng thời mở rộng bề mặt tấn công mạng nội bộ nếu quản trị viên không thực hiện kiểm soát lưu lượng trên cả hai cổng."

| Đoạn thử | Điểm khớp giọng | Điểm còn máy móc/khuôn mẫu | Điều chỉnh đã duyệt |
|---|---|---|---|
| Đoạn mẫu trên | Đúng cấu trúc logic, từ ngữ kỹ thuật chính xác, không dùng câu mào đầu sáo rỗng, giải thích rõ nguyên nhân - kết quả và cơ chế mạng | Không có sáo ngữ AI; nhịp câu tự nhiên, chặt chẽ | Chờ tác giả xác nhận / góp ý hiệu chỉnh |
