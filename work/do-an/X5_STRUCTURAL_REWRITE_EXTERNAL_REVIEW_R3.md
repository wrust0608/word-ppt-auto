# X5 STRUCTURAL REWRITE — EXTERNAL REVIEW ROUND 3

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-structural-revision`  
Candidate commit: `d7fe54d56cc6f7de1ada0817ebd23d254ec22ddc`  
Kết luận: `MINOR_BLOCKING_PATCH_REQUIRED / STRUCTURE_LOCKED`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 15/15 |
| Academic depth / reasoning | 19/20 |
| Technical accuracy | 17/20 |
| Sources / traceability | 14/15 |
| Structure | 10/10 |
| Author Voice / readability | 9/10 |
| QA / artifact consistency | 9/10 |
| **Tổng** | **93/100** |

Blocker: YES — 1 technical mechanism error plus minor precision fixes.

## 2. Điều đã đạt

- Remote commit tồn tại thật.
- Structure giữ đúng 8 H2 / 27 H3.
- Word count nằm trong target.
- Case C tunables đã sửa đúng canonical:
  - pfil_member=1
  - pfil_bridge=0
  - pfil_onlyip=1
- B2/B3 đã tách đúng scope.
- -sV không còn dùng để suy exact OS.
- Result leakage ở 2.4 đã được loại.
- S1-RAW-06 đã bị loại.
- Snapshot restore đã chuyển về wording phương pháp.
- FILTERED đã được trung tính hóa.
- Baseline network overclaims đã giảm.
- S032 đã được integrated.
- Validator/tests/linter/diff-check đều đạt theo handoff.

## 3. BLOCKER — Mô tả cơ chế smb-vuln-ms17-010 sai nguồn chính thức

Mục 2.5.1 hiện viết:

`Kịch bản NSE-SMB-04 kết nối IPC$, gửi SMB_COM_TRANSACTION với hàm PeekNamedPipe (opcode 0x2300) đến đường ống vô hiệu...`

Nmap NSEDoc chính thức mô tả script:
- kết nối cây IPC$;
- thực hiện một transaction trên FID 0;
- kiểm tra lỗi STATUS_INSUFF_SERVER_RESOURCES để nhận diện hệ chưa vá;
- đồng thời kiểm tra các mã lỗi đã biết của hệ patched.

Không nên tự chuyển cơ chế này thành PeekNamedPipe/opcode 0x2300 nếu source S018/Nmap script không trực tiếp mô tả như vậy.

Sửa 2.5.1 thành wording bám sát Nmap official source.

## 4. Case C rule wording

Mục 2.6.3 hiện viết “Luật chặn có log chặn gói TCP SYN...”.

Canonical C-RULE-02 xác nhận policy BLOCK TCP từ 192.168.56.10 tới 192.168.56.20 ports 139/445, logging enabled.

SYN là quan sát trong firewall log, không phải cần thiết là rule condition.

Sửa thành:
“Luật chặn TCP có bật ghi log, áp dụng từ ... tới ... cổng 139/445.”

Actual SYN log thuộc Chương 3.

## 5. Protocol-surface result leakage nhỏ

Mục 2.7.2 ghi:
“SMB 2.0.2 đến 3.0.2”.

Đây trùng exact dialect set quan sát trong run canonical.

Trong Chapter 2 evaluation framework chỉ cần:
“các dialect SMB2/SMB3”.

Exact list để Chương 3.

## 6. Patch baseline precision

Mục 2.2.5 hiện nói không cài KB4012213 hoặc KB4012216.

Canonical truth còn yêu cầu không có superseding rollup tương ứng.

Viết chính xác hơn:
- không ghi nhận hai direct KB hoặc bản cập nhật thay thế tương ứng theo mapping;
- đồng thời srv.sys 6.3.9600.16421 < 6.3.9600.18604 xác nhận UNPATCHED.

Không cần mở rộng danh sách KB.

## 7. Patching wording

Mục 2.6.4 dùng “biện pháp duy nhất tác động trực tiếp...”.

Tránh tuyệt đối hóa. Đổi thành:
“Patching là biện pháp trực tiếp thay đổi trạng thái bản vá của implementation bị ảnh hưởng...”

Không cần “duy nhất”.

## 8. Local patch interpretation wording

Mục 2.5.2:
“Trạng thái unpatched phản ánh khiếm khuyết trong nhân”

Nên chính xác hơn:
“Trạng thái UNPATCHED phản ánh hệ thống chưa đạt mức cập nhật được Microsoft xác minh cho MS17-010; trạng thái này không tự chứng minh khai thác thành công.”

## 9. Evaluation wording

Mục 2.7.4 Case B:
“tính sẵn sàng của SMBv2/v3 vẫn được quan sát”

Đây gần actual result.

Đổi thành criterion:
“đồng thời kiểm tra SMB2/SMB3 còn khả dụng trong phép thương lượng đã thiết kế hay không.”

## 10. Summary wording

2.8:
“Host-Only ... bảo đảm an toàn kiểm thử”

Tránh claim tuyệt đối. Đổi thành:
“Host-Only giới hạn phạm vi kết nối của lab và hỗ trợ kiểm soát rủi ro thử nghiệm.”

“tạo cơ sở chuẩn xác” -> “làm cơ sở”.

## 11. Source / citation consistency

S009/S018 Nmap source phải là nguồn trực tiếp cho cơ chế script. Không thêm nguồn mới nếu sửa theo NSEDoc chính thức.

S032 proposal URL nên đồng nhất với canonical URL đã lưu trong SOURCE_LEDGER nếu có khác biệt do legacy redirect.

## 12. Workflow state

- Structure: LOCKED.
- R3 score: 93/100.
- CP5-TECH: NOT YET.
- X5: OPEN for R4 micro-patch only.
- CP5-USER: PENDING.
- X6: BLOCKED.
