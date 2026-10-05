# Đề cương lập luận

Trạng thái: `LOCKED_CANONICAL_2026_10_05`

## Ngân sách toàn văn

- Mở đầu: 1.200–1.500 từ.
- Chương 1: khoảng 7.000–8.500 từ; ưu tiên tái sử dụng bản đã có sau X4 review.
- Chương 2: 3.500–4.500 từ.
- Chương 3: 4.500–6.000 từ.
- Chương 4: 3.500–4.500 từ.
- Kết luận/kiến nghị: 800–1.200 từ.
- Tổng dự kiến: khoảng 20.500–26.200 từ trước lượt anti-rambling.

## Vai trò từng phần

| Phần | Câu hỏi chính | Kết luận cần đạt | Ràng buộc |
|---|---|---|---|
| Mở đầu | Vì sao nghiên cứu, mục tiêu/phạm vi/phương pháp là gì? | Đặt đúng vấn đề và giới hạn | Không đưa kết quả chi tiết |
| Chương 1 | SMB/MS17-010/công cụ hoạt động ra sao? | Nền lý thuyết đủ cho experiment | Không lặp Ch2–4 |
| Chương 2 | Lab/phương pháp được thiết kế thế nào? | Mô hình canonical an toàn, tái lập, truy vết | Không kể chi tiết kết quả |
| Chương 3 | Thực nghiệm cho thấy gì? | AUTHOR_DATA canonical, 100% trace | Không suy diễn vượt evidence |
| Chương 4 | Kết quả có ý nghĩa gì? | So sánh mitigation, risk, limitations, recommendation | Không đưa evidence mới |
| Kết luận | Đã trả lời RQ/O đến đâu? | Tổng hợp đúng mức | Không tạo claim mới |

## Mạch chuyển chương

1. Chương 1 cung cấp thuật ngữ và cơ chế cần thiết để hiểu phương pháp đo.
2. Chương 2 chuyển nền lý thuyết thành lab, kịch bản, tiêu chí và evidence model.
3. Chương 3 trình bày dữ liệu canonical theo Scenario 1/2 và Case B/C.
4. Chương 4 diễn giải sự khác biệt giữa reachability, protocol surface, remote signal, patch state và mitigation layers.
5. Kết luận đóng RQ/O và công khai giới hạn.

---

Trạng thái: `LOCKED_CANONICAL / USER_APPROVED_2026_10_05`

# CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM

## 2.1. Yêu cầu và nguyên tắc thiết kế
### 2.1.1. Mục tiêu của môi trường thực nghiệm
### 2.1.2. Phạm vi, nguyên tắc an toàn và giới hạn đạo đức
### 2.1.3. Nguyên tắc cô lập mạng và khả năng khôi phục
### 2.1.4. Nguyên tắc thu thập, truy vết và bảo toàn bằng chứng

## 2.2. Kiến trúc môi trường thực nghiệm
### 2.2.1. Nền tảng Oracle VirtualBox
### 2.2.2. Máy kiểm thử Kali Linux
### 2.2.3. Máy mục tiêu Windows Server 2012 R2
### 2.2.4. Mạng Host-Only và bảng địa chỉ IP
### 2.2.5. Kiểm tra kết nối trong phạm vi lab

## 2.3. Chuẩn bị trạng thái baseline
### 2.3.1. Trạng thái hệ điều hành và dịch vụ SMB
### 2.3.2. Trạng thái SMBv1/SMB2 và TCP 139/445
### 2.3.3. Cấu hình Windows Firewall phục vụ phép đo
### 2.3.4. Xác định trạng thái bản vá MS17-010 và srv.sys
### 2.3.5. Kiểm tra Nmap và NSE script trên Kali
### 2.3.6. Snapshot Before Demo và phương án phục hồi

## 2.4. Phương pháp kiểm thử và mô hình bằng chứng
### 2.4.1. Các lớp quan sát: reachability, service, protocol, remote signal, local ground truth
### 2.4.2. Quy tắc phân biệt dữ kiện, diễn giải và kết luận
### 2.4.3. Định dạng raw output và Evidence ID
### 2.4.4. Quy tắc xử lý UNKNOWN, NO OUTPUT và FILTERED

## 2.5. Thiết kế Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap
### 2.5.1. Mục tiêu và điều kiện bắt đầu
### 2.5.2. Phát hiện máy trong mạng lab
### 2.5.3. Xác nhận máy mục tiêu
### 2.5.4. Kiểm tra TCP 139/445
### 2.5.5. Nhận diện dịch vụ và phiên bản
### 2.5.6. Khảo sát SMB bằng NSE
### 2.5.7. Tiêu chí dừng và bằng chứng cần thu

## 2.6. Thiết kế Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010 bằng NSE
### 2.6.1. NSE-SMB-01 — trạng thái cổng
### 2.6.2. NSE-SMB-02 — SMB dialects
### 2.6.3. NSE-SMB-03 — SMB signing
### 2.6.4. NSE-SMB-04 — dấu hiệu MS17-010
### 2.6.5. Đối chiếu remote observation với local patch ground truth
### 2.6.6. Tiêu chí kết luận và giới hạn suy diễn

## 2.7. Thiết kế kiểm thử biện pháp giảm thiểu
### 2.7.1. Nguyên tắc differential testing và phục hồi baseline
### 2.7.2. Case B — Vô hiệu hóa SMBv1
### 2.7.3. Case C — Giới hạn TCP 139/445 bằng pfSense Transparent Bridge
### 2.7.4. Vai trò của cập nhật bản vá trong mô hình phòng thủ
### 2.7.5. Ma trận biến can thiệp và phép đo lại

## 2.8. Tiêu chí đánh giá kết quả
### 2.8.1. Tiêu chí reachability
### 2.8.2. Tiêu chí protocol surface
### 2.8.3. Tiêu chí remote vulnerability signal
### 2.8.4. Tiêu chí patch ground truth
### 2.8.5. Tiêu chí hiệu quả và giới hạn của mitigation

## 2.9. Tổng kết Chương 2

# CHƯƠNG 3. THỰC NGHIỆM KIỂM THỬ DỊCH VỤ SMB VÀ MS17-010

## 3.1. Xác nhận trạng thái trước thực nghiệm
### 3.1.1. Trạng thái Kali Linux và công cụ
### 3.1.2. Trạng thái Windows Server 2012 R2
### 3.1.3. Trạng thái mạng, SMB và firewall
### 3.1.4. Snapshot và patch baseline

## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
### 3.2.1. Phát hiện máy trong mạng lab
### 3.2.2. Xác nhận máy mục tiêu
### 3.2.3. Trạng thái TCP 139/445
### 3.2.4. Nhận diện dịch vụ SMB
### 3.2.5. SMB dialects và các thông tin NSE quan sát được
### 3.2.6. Tổng hợp Kịch bản 1 và ranh giới kết luận

## 3.3. Kết quả Kịch bản 2 — Đánh giá cấu hình SMB và MS17-010
### 3.3.1. NSE-SMB-01 — TCP 139/445
### 3.3.2. NSE-SMB-02 — SMB dialects
### 3.3.3. NSE-SMB-03 — SMB signing
### 3.3.4. NSE-SMB-04 — kết quả kiểm tra MS17-010
### 3.3.5. Phân loại remote verdict UNKNOWN

## 3.4. Đối chiếu với trạng thái bản vá cục bộ
### 3.4.1. Phiên bản srv.sys và hotfix baseline
### 3.4.2. Xác định trạng thái UNPATCHED
### 3.4.3. Quan hệ giữa remote verdict và local ground truth

## 3.5. Case B — Thực nghiệm vô hiệu hóa SMBv1
### 3.5.1. Trạng thái trước can thiệp
### 3.5.2. Thao tác vô hiệu hóa SMBv1
### 3.5.3. Trạng thái cục bộ sau can thiệp
### 3.5.4. Retest SMB dialects
### 3.5.5. Retest MS17-010
### 3.5.6. Kết quả differential test

## 3.6. Case C — Thực nghiệm giới hạn SMB bằng pfSense
### 3.6.1. Mô hình pfSense Transparent Bridge
### 3.6.2. Baseline pass rule
### 3.6.3. Thiết lập block TCP 139/445
### 3.6.4. Retest trạng thái cổng từ Kali
### 3.6.5. Đối chiếu firewall log
### 3.6.6. Retest MS17-010 qua đường bị lọc
### 3.6.7. Xác nhận trạng thái Windows phía sau không đổi

## 3.7. Tổng hợp kết quả thực nghiệm
### 3.7.1. Ma trận Baseline — Case B — Case C
### 3.7.2. Các kết luận được phép rút ra
### 3.7.3. Các kết luận không được phép suy diễn
### 3.7.4. Các dữ liệu chưa có hoặc không thuộc canonical run

## 3.8. Tổng kết Chương 3

# CHƯƠNG 4. ĐÁNH GIÁ KẾT QUẢ, RỦI RO VÀ KHUYẾN NGHỊ

## 4.1. Khung đánh giá kết quả
### 4.1.1. Reachability
### 4.1.2. Protocol surface
### 4.1.3. Remote vulnerability signal
### 4.1.4. Local patch ground truth
### 4.1.5. Mitigation layer

## 4.2. Đánh giá trạng thái baseline
### 4.2.1. Ý nghĩa của TCP 139/445 open
### 4.2.2. Ý nghĩa của SMBv1 được chấp nhận
### 4.2.3. Ý nghĩa của remote verdict UNKNOWN
### 4.2.4. Ý nghĩa của local state UNPATCHED

## 4.3. Đánh giá Case B — Vô hiệu hóa SMBv1
### 4.3.1. Thay đổi trên bề mặt giao thức
### 4.3.2. Những gì không thay đổi trên host
### 4.3.3. Hiệu quả và giới hạn của biện pháp
### 4.3.4. Ảnh hưởng tương thích cần xem xét

## 4.4. Đánh giá Case C — Kiểm soát truy cập bằng pfSense
### 4.4.1. Thay đổi về khả năng tiếp cận từ Kali
### 4.4.2. Quy thuộc kết quả cho firewall rule
### 4.4.3. Những gì không thay đổi trên Windows target
### 4.4.4. Hiệu quả và giới hạn của biện pháp

## 4.5. Vai trò của cập nhật bản vá
### 4.5.1. Patching khác với disable SMBv1 và network filtering
### 4.5.2. Vị trí của patching trong defense-in-depth
### 4.5.3. Giới hạn thực nghiệm: chưa có Case A canonical

## 4.6. So sánh các lớp phòng thủ
### 4.6.1. Patching
### 4.6.2. Protocol hardening
### 4.6.3. Network access control
### 4.6.4. Ma trận defense-in-depth

## 4.7. Đánh giá rủi ro và rủi ro còn lại
### 4.7.1. Tác động tới tính bí mật
### 4.7.2. Tác động tới tính toàn vẹn
### 4.7.3. Tác động tới tính sẵn sàng
### 4.7.4. Residual risk sau từng lớp kiểm soát

## 4.8. Giới hạn và threats to validity
### 4.8.1. Một Windows target và một nguồn kiểm thử
### 4.8.2. Môi trường ảo hóa
### 4.8.3. Không thực hiện khai thác RCE canonical
### 4.8.4. Remote NSE verdict UNKNOWN
### 4.8.5. Không có Case A patch canonical
### 4.8.6. Không có benchmark hiệu năng

## 4.9. Khuyến nghị triển khai
### 4.9.1. Cập nhật bản vá bảo mật
### 4.9.2. Loại bỏ hoặc vô hiệu hóa SMBv1 khi không cần thiết
### 4.9.3. Giới hạn TCP 139/445 theo nhu cầu nghiệp vụ
### 4.9.4. Phân đoạn mạng và kiểm soát truy cập
### 4.9.5. Giám sát và kiểm tra định kỳ
### 4.9.6. Kiểm thử lại sau thay đổi

## 4.10. Hướng phát triển
## 4.11. Tổng kết Chương 4

