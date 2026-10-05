# X5 DEMO-STYLE — FINAL EXTERNAL REVIEW R4

Ngày: 2026-10-06  
Candidate branch: `feature/x5-chapter-2-demo-style`  
Candidate commit: `38057dc2c9c35fce593d5a784d6df8ad9465282e`  
Kết luận: `PASS / READY_FOR_USER_REVIEW`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 15/15 |
| Academic depth / reasoning | 18/20 |
| Technical accuracy | 19/20 |
| Sources / traceability | 14/15 |
| Structure | 10/10 |
| Academic style / readability | 10/10 |
| QA / artifact consistency | 10/10 |
| **Tổng** | **96/100** |

Blocker: **0**.

## 2. Kết luận hội đồng

R4 đạt đúng định hướng người dùng yêu cầu: đơn giản, dễ hiểu, đúng trọng tâm và đọc như một chương đồ án ATTT có phần demo.

Mạch trình bày:
1. mô hình thực nghiệm;
2. cài đặt/cấu hình môi trường;
3. Demo 1;
4. Demo 2;
5. kiểm thử giảm thiểu;
6. thu thập dữ liệu;
7. tổng kết.

Không còn cảm giác leader/QA/governance report.

## 3. Technical truth

Các điểm kỹ thuật nhạy đã được kiểm:
- Demo 1 giữ đúng B1–B6;
- Demo 2 dùng đúng smb-vuln-ms17-010, không có unsafe=0;
- IPC$ / FID 0 / status-code wording phù hợp nguồn Nmap;
- Windows patch state giữ đúng UNPATCHED;
- UNKNOWN != SAFE;
- FILTERED != PATCHED;
- SMBv1 enabled != MS17-010 confirmed;
- SMBv1 disabled != PATCHED;
- pfSense CE 2.9.0;
- canonical Case C rule source .10 -> destination .20 ports 139/445 + logging;
- pfil_member=1, pfil_bridge=0, pfil_onlyip=1;
- Case A chỉ tham khảo, chưa đo đạc trực tiếp.

External Reviewer cũng xác minh semantics `pfil_onlyip=1` phù hợp FreeBSD bridge documentation: non-IP frames bị kiểm soát theo tùy chọn này, còn IP packets đi qua firewall rules.

## 4. Research grounding

- TL01–TL03 chỉ được dùng ở mức METADATA_ONLY.
- TL03 corrected handle: `HVCNBCVT/3493`.
- TL04–TL07 UNVERIFIED và không tham gia vào presentation conclusions.
- Research artifact không còn mạo nhận đã xem full text khi không truy cập được.

## 5. Presentation quality

Điểm mạnh:
- bảng/lệnh dễ tìm;
- flow demo rõ;
- phần cấu hình đủ để hiểu lab nhưng không biến thành hướng dẫn click-by-click;
- Chương 2 không kể chi tiết result;
- mitigation trình bày theo before/after dễ theo dõi;
- phần 2.6 giữ ngắn, chỉ còn dữ liệu và ranh giới diễn giải cần thiết.

## 6. QA

Executor report:
- 3,655 words;
- 7 H2 / 20 H3;
- validator PASS;
- 7/7 tests PASS;
- academic linter 0 error / 0 warning;
- citation sequence [1]–[11] valid;
- git diff --check PASS;
- clean working tree.

Remote SHA đã được External Reviewer xác minh trực tiếp.

## 7. Non-blocking notes

Không mở lại X5 vì các điểm sau:
- Có thể đổi một số từ tiếng Anh như “baseline”, “before-after test”, “Protocol Hardening” khi publication polish nếu muốn Việt hóa thêm.
- Mermaid sẽ được thay bằng hình/render thật ở giai đoạn Word nếu cần.
- Hình 2.2 hiện là flow định hướng; actual screenshots/result thuộc Chương 3.

## 8. Gate decision

- Score: **96/100**
- Blocker: **0**
- Demo-style structure: **LOCKED**
- Candidate: `38057dc2c9c35fce593d5a784d6df8ad9465282e`
- Status: `CHAPTER_2_DEMO_STYLE_READY_FOR_USER_REVIEW`
- CP5-USER: PENDING
- X6: BLOCKED until explicit user approval.
