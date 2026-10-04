# RUBRIC TRACEABILITY MATRIX — X0

Trạng thái: `DRAFT_FOR_REVIEW`  
Nguồn: bảng Thang điểm trong đề cương chi tiết đã duyệt.

| ID | CLO / Tiêu chí | Điểm | Deliverable/section chịu trách nhiệm | Evidence/QA chính | Gate |
|---|---|---:|---|---|---|
| R01 | CLO1.1 — Xác định mục tiêu, phạm vi, đạo đức | 0.25 | Mở đầu + Project/Research profile | Requirement reconciliation | X0/X2 |
| R02 | CLO1.1 — Khảo sát hiện trạng SMB | 0.25 | Ch1 + Ch2 baseline | Source + baseline evidence | X4/X5 |
| R03 | CLO1.1 — Đề xuất mô hình kiểm thử/phòng thủ | 0.25 | Ch2 + Ch4 | lab design + mitigation analysis | X5/X7 |
| R04 | CLO6 — Kế hoạch/phân công | 0.25 | Roadmap + responsibility matrix | Execution plan | X0 |
| R05 | CLO1.2 — SMB/MS17-010/nguy cơ | 0.50 | Ch1 | Source ledger/claim matrix | X4 |
| R06 | CLO1.2 — Nmap/NSE/Metasploit | 0.25 | Ch1 | official docs; no fake exploit | X4 |
| R07 | CLO2.1 — Công nghệ/công cụ/mô hình | 0.25 | Ch2 | environment evidence | X5 |
| R08 | CLO2.1 — Sơ đồ lab/luồng kiểm thử | 0.50 | Ch2 | topology + flow figure | X3/X5 |
| R09 | CLO2.2 — Vai trò/quan hệ thành phần | 0.50 | Ch2 | chapter contract + topology explanation | X5 |
| R10 | CLO3 — Kịch bản/tiêu chí kiểm thử | 0.50 | Ch2 | scenario contracts | X3/X5 |
| R11 | CLO3 — Chọn công cụ/môi trường | 0.50 | Ch2 | VirtualBox/Kali/Windows/Nmap evidence | X5 |
| R12 | CLO3 — Cấu hình Kali/Windows/mạng | 0.50 | Ch2 | baseline/pre-demo evidence | X5 |
| R13 | CLO3 — Hạ tầng ảo/cô lập | 0.50 | Ch2 | Host-Only + snapshot | X5 |
| R14 | CLO3 — Khảo sát SMB bằng Nmap | 0.50 | Ch3 Scenario 1 | raw B2–B6 | X6 |
| R15 | CLO3 — Xác minh trạng thái MS17-010 | 0.50 | Ch3 Scenario 2 + local baseline | NSE + patch ground truth | X6 |
| R16 | CLO3 — Kiểm thử có kiểm soát | 0.50 | Ch3 | safe detection/differential testing | X6 |
| R17 | CLO3 — Áp dụng biện pháp phòng thủ | 0.50 | Ch3 Case B/C; patch recommendation if no Case A | canonical mitigation evidence | X6/X7 |
| R18 | CLO3 — Retest + minh chứng | 0.50 | Ch3 + appendix | raw retest + log + screenshot | X6 |
| R19 | CLO4 — Before/after, risk, residual risk | 0.50 | Ch4 | comparison matrix + limitations | X7 |
| R20 | CLO5.1 — Nội dung báo cáo | 0.50 | toàn văn | G5 synthesis review | X9 |
| R21 | CLO5.1 — Hình thức/định dạng | 0.50 | DOCX | publication QA | X10 |
| R22 | CLO6 — Thái độ/tác phong | 0.50 | ngoài nội dung kỹ thuật; theo GVHD/nhóm | meeting/progress records nếu cần | governance |
| R23 | CLO5.2 — Báo cáo/slide | 0.50 | defense package | slide/Q&A/rehearsal | X11 |

## Nhận định rubric

- CLO3 = **4.5/10**, là workstream lớn nhất.
- CLO3 + CLO4 = **5.0/10** nên Ch2–4/evidence phải nhận phần lớn effort QA.
- Patch là một mitigation được đề cương nêu. Nếu không có canonical Case A, cần minh bạch khoảng trống thay vì bịa đủ rubric.
- Metasploit được yêu cầu về mặt nghiên cứu công cụ; không bắt buộc phải tuyên bố exploit thành công khi canonical run không có.
