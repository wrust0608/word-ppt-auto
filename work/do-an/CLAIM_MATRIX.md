# Ma trận luận điểm và bằng chứng

Loại: `SOURCE_FACT`, `AUTHOR_DATA`, `INTERPRETATION`, `PROPOSAL`, `COMMON_KNOWLEDGE`.

Mức hỗ trợ: `STRONG`, `MODERATE`, `WEAK`, `CONTRADICTED`, `MISSING`.

| Claim ID | Luận điểm | Loại | Source/Evidence ID | Vị trí bằng chứng | Mức hỗ trợ | Phản biện/điều kiện | Nơi sử dụng | Trạng thái |
|---|---|---|---|---|---|---|---|---|
| C001 | SMB là giao thức truyền thông mạng chạy ở Kernel-mode (`srv.sys`); SMBv2/v3 khắc phục tính "chatty" và nâng cấp bảo mật so với SMBv1 | SOURCE_FACT | S001, S002, S003, S004, S006, S007, S008 | Tanenbaum [1], Direct host SMB [2], Windows Internals [3], [4], MS Learn [6], [7], [8] | STRONG | Cần phân định rõ các dialect SMB 3.0 và 3.1.1 về thuật toán mã hóa/ký số | Chương 1 (Mục 1.1) | VERIFIED |
| C002 | MS17-010 gồm 6 CVE trong `srv.sys`, trong đó CVE-2017-0144 xuất phát từ lỗi tính toán kích thước FEA gây tràn bộ đệm nhân cho phép RCE với quyền cao | SOURCE_FACT | S003, S005, S010, S011, S012, S013, S014, S015 | MS17-010 [5], MSRC [10], NVD [11], MS Petya [12], Rapid7 [13], CISA [14], MS WannaCrypt [15] | STRONG | NVD [11] chỉ dùng riêng cho CVE-2017-0144; không khái quát toàn bulletin thành một lỗi RCE | Chương 1 (Mục 1.2) | VERIFIED |
| C003 | Khung đánh giá an ninh SMB phân định 4 cấp độ độc lập: Cổng mở, Dịch vụ SMBv1, Dấu hiệu chưa vá (NSE), và Khả năng khai thác thành công | INTERPRETATION | S017, S018, S019 | Nmap Book [17], Mã nguồn NSE [18], Metasploit Guide [19] | STRONG | Dấu hiệu phản hồi 0xC0000205 ở Cấp độ 3 không tương đương với khai thác thành công ở Cấp độ 4 | Chương 1 (Mục 1.3, 1.4) | VERIFIED |
| C004 | Quá trình kiểm thử an ninh SMB phải tuân thủ đạo đức, triển khai trong lab cô lập có snapshot để kiểm soát rủi ro màn hình xanh (BSOD) | PROPOSAL | S013, S016, S019 | Rapid7 [13], Penetration Testing [16], Metasploit Guide [19] | STRONG | Pool grooming không ổn định có thể làm sập hệ điều hành đích | Chương 1 (Mục 1.3.3, 1.4.2) | VERIFIED |
| C005 | Cập nhật bản vá định kỳ và vô hiệu hóa SMBv1 là biện pháp phòng thủ triệt để; kết hợp chặn cổng 445/139 và phân đoạn mạng để chống lây lan ngang | PROPOSAL | S005, S007, S008, S009 | MS17-010 [5], MS Learn [7], [8], McNab [9] | STRONG | Phải duy trì kết nối cổng 445 cho dịch vụ chia sẻ tệp nội bộ đã nâng cấp SMBv2/SMBv3 | Chương 1 (Mục 1.4.3) | VERIFIED |
| C006 | Quá trình phòng thủ SMB phải đi kèm đánh giá tương thích với thiết bị cũ và thực hiện retesting độc lập để xác minh hiệu lực cấu hình | INTERPRETATION | S008, S009, S017 | MS Learn [8], McNab [9], Nmap Book [17] | STRONG | Cần rà soát các máy in/NAS cũ trước khi tắt SMBv1 để tránh gián đoạn dịch vụ | Chương 1 (Mục 1.4.3) | VERIFIED |

## Luận điểm chưa đủ bằng chứng

- Bằng chứng thực nghiệm demo đo lường hiệu năng mạng trước và sau khi kích hoạt SMB Encryption / SMB Signing: Hiện tại giữ nhãn `[CẦN DỮ LIỆU]` theo đúng chỉ thị tránh demo của tác giả.

## Mâu thuẫn cần giải quyết

- Không còn mâu thuẫn nguồn. Toàn bộ 19 tài liệu tham khảo đều là nguồn gốc chính thức (Microsoft Learn, MSRC, CISA, NIST NVD, Rapid7, Nmap Project, sách chuyên khảo học thuật tiêu chuẩn).
