# X5 STRUCTURAL REWRITE — EXTERNAL REVIEW ROUND 4 (PANEL-STYLE REVIEW)

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-structural-revision`  
Candidate commit: `6ec02ffcacd02c66e14858cad89e2c719fdccfc4`  
Kết luận: `PASS_WITH_MINOR_REVISIONS / NO BLOCKER`

## 1. Điểm hội đồng

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 15/15 |
| Academic depth / reasoning | 19/20 |
| Technical accuracy | 18/20 |
| Sources / traceability | 15/15 |
| Structure | 10/10 |
| Academic style / author voice | 8/10 |
| QA / artifact consistency | 9/10 |
| **Tổng** | **94/100** |

Không còn blocker.

Theo ngưỡng dự án, 90–94 = đạt nhưng cần minor revision trước khi khóa kỹ thuật.

## 2. Nhận xét kiểu hội đồng phản biện

### 2.1. Cấu trúc
Cấu trúc 8 H2 / 27 H3 được đánh giá rất tốt. Mạch:
design -> lab/baseline -> evidence method -> Scenario 1 -> Scenario 2 -> mitigation -> evaluation framework -> summary
rõ chức năng, ít trùng lặp và đúng vai trò Chương 2.

Không yêu cầu đổi outline.

### 2.2. Logic nghiên cứu
Điểm mạnh nhất là mô hình 5 lớp:
Reachability -> Port & Service -> Protocol -> Remote Vulnerability Signal -> Local Patch State.

Mô hình này bảo vệ các ranh giới:
- 445 open != SMBv1;
- SMBv1 != MS17-010;
- UNKNOWN != SAFE;
- filtered != patched;
- disable SMBv1 != patched.

Logic đủ mạnh để bảo vệ trước câu hỏi phản biện “Nmap không báo vulnerable thì vì sao vẫn nói máy chưa vá?”.

### 2.3. Evidence / source
R4 đã đóng các lỗi R1–R3:
- Nmap MS17-010 mechanism bám official NSEDoc;
- S032 Microsoft patch verification đã verified;
- pfSense tunables đúng canonical;
- invalid Evidence ID đã loại;
- Case A không còn bị trình bày như completed experiment.

Nguồn hiện đủ cho Chương 2.

## 3. Minor revisions bắt buộc trước CP5-TECH lock

### MR-01 — NO USABLE RESULT vẫn có causal wording
Mục 2.5.2 viết:
“nếu kịch bản NSE không nhận đủ phản hồi để phân loại...”

Negative Result Policy cấm tự gán nguyên nhân cho NO OUTPUT nếu evidence không chứng minh.

Đổi thành:
“nếu script không cung cấp verdict usable, kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT.”

### MR-02 — Set-SmbServerConfiguration wording
Mục 2.6.2 viết:
“Thao tác chỉ điều chỉnh dịch vụ LanmanServer...”

Lệnh này điều chỉnh cấu hình SMB Server, không nên mô tả là điều chỉnh bản thân service.

Đổi thành:
“Thao tác chỉ thay đổi cấu hình SMB Server, không gỡ FS-SMB1 và không thay đổi driver srv.sys.”

### MR-03 — Bảng 2.1: ‘Tách biệt L3’ sai logic
Kali và Windows cùng subnet 192.168.56.0/24, nên cột Ý nghĩa thiết kế của dòng IP không được ghi “Tách biệt L3”.

Đổi thành:
“Địa chỉ tĩnh trong cùng mạng lab” hoặc “Định danh tĩnh trong cùng subnet thực nghiệm”.

### MR-04 — Reachability terminology
Bảng 2.2 gọi Reachability là “Khả năng định tuyến L3” trong khi phương pháp còn dùng ARP probe.

Đổi thành:
“Khả năng hiện diện/tiếp cận trong mạng lab”.

Ở 2.7.1, tránh xem không phản hồi ICMP/ARP như bằng chứng tuyệt đối “Unreachable”; dùng “có phản hồi / không ghi nhận phản hồi ở phép tiền kiểm” nếu cần.

### MR-05 — TCP closed response
2.7.1 ghi closed = “RST-ACK”.

Nmap documentation dùng RST là dấu hiệu chính cho closed trong SYN scan.

Đổi thành “nhận phản hồi RST”.

### MR-06 — Signing framework
2.7.2 nói phân loại signing để “đánh giá khả năng chống tấn công chuyển tiếp”.

Ở Chương 2 nên thu hẹp mục tiêu:
“đánh giá chính sách ký số và mức độ bắt buộc ký”.

Phân tích relay/MITM để Chương 1/4 nếu cần.

### MR-07 — Case B còn một câu gần result leakage
2.7.4:
“cổng TCP 445 vẫn mở”

Trong framework nên viết theo quan hệ kỹ thuật, không như observed result:
“việc tắt SMBv1 không đồng nghĩa đóng TCP 445; phép retest phải kiểm tra SMB2/SMB3 còn khả dụng hay không.”

### MR-08 — Internal repository jargon
Giảm các từ không tự nhiên trong báo cáo:
- “canonical” -> “lượt đo chính thức” / “bộ dữ liệu thực nghiệm hiện hành”;
- “implementation” -> “thành phần SMB bị ảnh hưởng”;
- “reason” -> “lý do phân loại”;
- ưu tiên “bề mặt dịch vụ/bề mặt tấn công” ổn định hơn “bề mặt tiếp xúc” nếu không có lý do đổi thuật ngữ.

Không cần truy quét thay toàn bộ, chỉ sửa các vị trí nổi bật.

### MR-09 — Mục tiêu câu đầu
2.1.1 “đánh giá nhận diện MS17-010 từ xa” hơi cứng.

Khuyến nghị:
“đánh giá khả năng nhận diện dấu hiệu MS17-010 từ xa”.

### MR-10 — Safety wording
2.1.2 “không gây sập hệ thống” có sắc thái claim kết quả.

Đổi thành:
“không thực hiện thao tác có chủ đích gây sập hoặc gián đoạn hệ thống.”

## 4. Các điểm KHÔNG cần sửa

- Không đổi 8 H2 / 27 H3.
- Không thêm figure/table mới.
- Không mở lại Case A evidence.
- Không thêm exploitation.
- Không đổi 5-layer model.
- Không chuyển UNKNOWN thành SAFE/VULNERABLE.
- Không thêm bibliography riêng cuối Chương 2.

## 5. Kết luận hội đồng

R4 đã đạt chất lượng đồ án tốt và không còn blocker kỹ thuật.
Điểm hiện tại: **94/100 — PASS WITH MINOR REVISIONS**.

Sau khi đóng MR-01 -> MR-10 bằng một micro-edit, candidate đủ điều kiện chấm lại CP5-TECH; không cần thêm vòng structural rewrite.
