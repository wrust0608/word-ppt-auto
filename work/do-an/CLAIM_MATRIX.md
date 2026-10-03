# Ma trận luận điểm và bằng chứng

Loại: `SOURCE_FACT`, `AUTHOR_DATA`, `INTERPRETATION`, `PROPOSAL`, `COMMON_KNOWLEDGE`.

Mức hỗ trợ: `STRONG`, `MODERATE`, `WEAK`, `CONTRADICTED`, `MISSING`.

| Claim ID | Luận điểm | Loại | Source/Evidence ID | Vị trí bằng chứng | Mức hỗ trợ | Phản biện/điều kiện | Nơi sử dụng | Trạng thái |
|---|---|---|---|---|---|---|---|---|
| C001 | SMB là giao thức chia sẻ tài nguyên mạng; các vai trò client/server, dialect SMBv1–v3 và cơ chế bảo mật phải được phân định theo đặc tả tương ứng | SOURCE_FACT | S002, S006, S007, S008, S020, S021, S022, S023 | Direct-host SMB; SMB overview; SMB security; [MS-SMB]; [MS-SMB2]; SMB signing | STRONG | Không khái quát mọi xử lý SMB đều nằm trong cùng một driver hoặc cùng chế độ thực thi; đối chiếu theo phiên bản Windows và dialect | Chương 1 (Mục 1.1) | VERIFIED |
| C002 | MS17-010 là bulletin chứa nhiều CVE; CVE-2017-0144 liên quan xử lý gói SMBv1 và có thể dẫn tới thực thi mã từ xa | SOURCE_FACT | S005, S010, S011, S012, S013, S015 | MS17-010; MSRC; NVD; Rapid7; Microsoft Threat Intelligence | STRONG | Không đồng nhất toàn bộ bulletin với một root cause; S014 đang `RECHECK` và không được dùng tới khi khôi phục nguồn | Chương 1 (Mục 1.2) | VERIFIED |
| C003 | Khung đánh giá an ninh SMB phân định 4 cấp độ độc lập: cổng mở, dialect/dịch vụ, dấu hiệu chưa vá qua NSE và khả năng khai thác | INTERPRETATION | S013, S017, S018, S021, S022 | Rapid7 module; Nmap Guide; mã nguồn NSE; đặc tả MS-SMB/MS-SMB2 | STRONG | Phản hồi NSE ở Cấp độ 3 không tương đương với khai thác thành công ở Cấp độ 4 | Chương 1 (Mục 1.3, 1.4) | VERIFIED |
| C004 | Kiểm thử SMB phải có ủy quyền, phạm vi cô lập, snapshot/khôi phục và giới hạn số lần thử để kiểm soát tác động | PROPOSAL | S013, S024 | Rapid7 module; NIST SP 800-115 | STRONG | Pool grooming có thể làm sập hệ điều hành; không thực hiện ngoài lab được cấp phép | Chương 1 (Mục 1.3.3, 1.4.2), Chương 2 | VERIFIED |
| C005 | Vá hệ thống và vô hiệu hóa SMBv1 là kiểm soát chính; chính sách tường lửa và phân đoạn giảm khả năng tiếp cận dịch vụ nhưng không thay thế hardening máy chủ | PROPOSAL | S005, S007, S008, S023, S025 | MS17-010; Microsoft Learn; SMB signing; NIST SP 800-41 Rev.1 | STRONG | Cổng 445 vẫn cần cho SMBv2/v3 hợp lệ; luật tường lửa phải bám nhu cầu nghiệp vụ và được kiểm thử | Chương 1 (Mục 1.4.3), Chương 2 | VERIFIED |
| C006 | Phòng thủ SMB phải đánh giá tương thích thiết bị cũ và retest độc lập để xác minh hiệu lực cấu hình | INTERPRETATION | S008, S017, S023, S024, S025 | Microsoft Learn; Nmap Guide; NIST SP 800-115; NIST SP 800-41 Rev.1 | STRONG | Gỡ SMBv1 hoặc siết signing có thể ảnh hưởng thiết bị cũ; mọi ngoại lệ phải được ghi và giới hạn | Chương 1 (Mục 1.4.3), Chương 2 | VERIFIED |

## Luận điểm chưa đủ bằng chứng

- Bằng chứng thực nghiệm demo đo lường hiệu năng mạng trước và sau khi kích hoạt SMB Encryption / SMB Signing: Hiện tại giữ nhãn `[CẦN DỮ LIỆU]` theo đúng chỉ thị tránh demo của tác giả.

## Mâu thuẫn cần giải quyết

- Bibliography cũ chưa đồng bộ ledger: 7 nguồn còn RECHECK, dù sáu luận điểm trung tâm đã có tuyến nguồn khả dụng. Không coi đủ 19 nguồn đã xác minh. Xem SOURCE_RECONCILIATION_PLAN.md; mỗi phát biểu phải kiểm tra đoạn gốc trước thay citation.
