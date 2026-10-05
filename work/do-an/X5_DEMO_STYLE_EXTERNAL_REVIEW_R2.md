# X5 DEMO-STYLE — EXTERNAL REVIEW R2

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-demo-style`  
Candidate commit: `c3f6b4d65caa6ce6056ecc63cb7f6e14a9b4a3f9`  
Kết luận: `REVISE_MINOR_BLOCKING / PRESENTATION_APPROVED`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 14/15 |
| Academic depth / reasoning | 17/20 |
| Technical accuracy | 16/20 |
| Sources / traceability | 9/15 |
| Structure | 10/10 |
| Academic style / readability | 9/10 |
| QA / artifact consistency | 9/10 |
| **Tổng** | **84/100** |

Blocker: YES, nhưng chỉ còn micro-corrections. Không viết lại cấu trúc.

## 2. Điều đã đạt

- Demo-style direction đã đúng: lab -> cấu hình -> Demo 1 -> Demo 2 -> mitigation -> dữ liệu -> tổng kết.
- 7 H2 / 20 H3 hợp lý và nên giữ.
- Demo 1 đã khôi phục đúng B1-B6.
- unsafe=0 đã bị loại.
- Case B action/retest đã quay về evidence hiện hành.
- pfSense CE 2.9.0, source/destination/ports/log và tunables đã đúng canonical.
- Case A đã quay về reference-only.
- tcpdump/tshark/pcap/Event Viewer additions đã bị loại.
- bibliography riêng cuối Chapter 2 đã bị loại.
- Presentation hiện gần đúng kiểu đồ án thực nghiệm sinh viên.

## 3. Blocker A — Windows baseline bị mô tả rộng hơn evidence

Các cụm sau vượt evidence:
- “Build 9600 (RTM nguyên bản)”
- “Tái hiện máy chưa vá”
- “không cài đặt bất kỳ gói rollup nào”

Evidence chỉ khóa:
- Windows Server 2012 R2 Standard Evaluation Build 9600;
- MS17-010 state = UNPATCHED;
- không có KB4012213 / KB4012216 hoặc superseding update tương ứng;
- local system vẫn có các hotfix cũ.

Sửa:
- bỏ “RTM nguyên bản”;
- không nói không có bất kỳ rollup nào;
- chỉ nói không ghi nhận update liên quan MS17-010 theo mapping.

## 4. Blocker B — UNKNOWN vẫn có causal inference

Mục 2.6.2 viết:
“UNKNOWN ... do cơ chế phản hồi hoặc điều kiện mạng”.

Negative Result Policy cấm tự giải thích nguyên nhân khi raw chỉ cho NO USABLE RESULT.

Sửa thành:
“Khi script không cung cấp verdict usable, ghi nhận UNKNOWN / NO USABLE SCRIPT RESULT; không suy diễn thành SAFE.”

Không thêm nguyên nhân.

## 5. Blocker C — FILTERED bị gán nguyên nhân tổng quát

Mục 2.6.2 viết:
“FILTERED ... do tường lửa chặn gói”.

Ở rule tổng quát, chỉ được nói:
- Nmap không đủ phản hồi để phân loại open/closed;
- FILTERED không chứng minh host patched.

Riêng Case C ở Chương 3 mới có thể đối chiếu C-LOG-01 để quy attribution cho pfSense.

## 6. Blocker D — smb-vuln-ms17-010 wording quá quyết định

Mục 2.4.2 viết:
“Nếu máy chủ chưa được cập nhật bản vá, nó phản hồi STATUS_INSUFF_SERVER_RESOURCES...”

Nmap official source mô tả status này là dấu hiệu script dùng để nhận diện vulnerable systems; không được diễn đạt thành mọi unpatched server tất yếu trả status đó.

Sửa thành:
“Script sử dụng STATUS_INSUFF_SERVER_RESOURCES như một dấu hiệu để nhận diện hệ thống có khả năng bị ảnh hưởng.”

Không gắn deterministically với local UNPATCHED state.

## 7. Minor E — governance jargon còn sót

Mục 2.3.2 còn:
“6 bước kỹ thuật canonical”.

Đổi thành:
“6 bước kỹ thuật”.

Mục 2.4.3 còn:
“Local Ground Truth”.

Đổi thành:
“Trạng thái bản vá nội bộ”.

Không cần thuật ngữ nội bộ repo trong prose chính.

## 8. Minor F — Windows Firewall wording

“ngăn chặn truy cập ngoài phạm vi kiểm thử” quá rộng.

Evidence chỉ chứng minh scoped allow cho TCP 139/445 từ Kali và default File and Printer Sharing group OFF.

Sửa thành:
“chỉ cho phép lưu lượng TCP 139/445 từ địa chỉ 192.168.56.10 theo rule phục vụ lab.”

Không suy rộng mọi truy cập khác.

## 9. Minor G — mục tiêu Case B

“nhằm vô hiệu hóa SMBv1 và duy trì chia sẻ tệp qua SMBv2/SMBv3” có thể đọc như đã kiểm chứng workload.

Sửa:
“nhằm vô hiệu hóa SMBv1 và giữ SMB2/SMB3 là các phiên bản giao thức còn được phép thương lượng.”

Không suy ra mọi workload chia sẻ tệp đã được kiểm thử.

## 10. Research artifact vẫn cần làm sạch

Research-first direction được giữ.

Nhưng:
- TL01/PTIT metadata có thể xác minh được và PTIT công khai tóm tắt cấu trúc chương.
- TL02 có handle cụ thể `HVCNBCVT/5000` hoặc `4983`, không để handle trống.
- TL05 “FULL_TEXT” hiện dùng URL Studocu category chung, không phải URL tài liệu cụ thể.
- TL06 “FULL_TEXT” dùng URL Scribd `/document/` chung, không xác minh được tài liệu cụ thể.
- TL07/TL08 đã UNVERIFIED và bị loại, đúng.

R3 phải:
- sửa exact handle cho nguồn xác minh được;
- hạ TL05/TL06 xuống UNVERIFIED nếu không có exact document URL + title/author;
- không dùng TL05/TL06 để biện minh cho pattern cụ thể nếu chưa xác minh được.

Research artifact không cần đủ 6 nguồn nữa nếu nguồn ít hơn nhưng trung thực; chất lượng > số lượng.

## 11. Source-independent presentation insight

Các metadata PTIT đã đủ để ủng hộ hướng lớn:
- nhiều đồ án ATTT tách phần xây dựng/triển khai khỏi thử nghiệm/đánh giá;
- các đề tài Labtainer/bài thực hành tổ chức nội dung theo xây dựng bài thực hành rồi thử nghiệm/đánh giá.

Không cần bịa full-text details để hợp thức hóa cấu trúc 7/20.

## 12. Non-blocking polish

- “ngăn lưu lượng thoát ra mạng bên ngoài” ở 2.1.1 có thể đổi thành “giới hạn đường kết nối của hai VM trong mạng Host-Only quan sát được”.
- “không gây gián đoạn máy mục tiêu” nên là “không thực hiện thao tác có chủ đích gây gián đoạn”.
- “phân loại phiên bản giao thức đang chạy” -> “xác định các dialect SMB được hỗ trợ” sẽ chính xác hơn.
- “Mọi lệnh quét bắt buộc dùng -oA” -> “Các lệnh Nmap trong kịch bản được lưu bằng -oA” để tránh tuyệt đối hóa.

## 13. Gate decision

- Structure 7 H2 / 20 H3: LOCK FOR DEMO STYLE.
- Presentation direction: PASS.
- Technical/source R2: REVISE_MINOR_BLOCKING.
- X5 remains OPEN for R3 micro-patch only.
- CP5-USER remains PENDING.
- X6 remains BLOCKED.
