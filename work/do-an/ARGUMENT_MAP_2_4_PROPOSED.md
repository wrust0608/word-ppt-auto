# ARGUMENT MAP 2–4 — PROPOSED

Trạng thái: X2_PROPOSED / NOT_LOCKED

## Kết luận trung tâm

Việc đánh giá MS17-010 trong lab phải tách bốn lớp bằng chứng: **khả năng tiếp cận dịch vụ, trạng thái giao thức SMB, tín hiệu từ công cụ phát hiện và trạng thái bản vá cục bộ**. Các biện pháp giảm thiểu tác động lên các lớp khác nhau; do đó không được đồng nhất OPEN, SMBv1 enabled, UNKNOWN, UNPATCHED, DISABLED hay FILTERED.

## Chuỗi lập luận

| ID | Luận điểm | Loại | Evidence/Source | Giới hạn |
|---|---|---|---|---|
| A21 | Lab VirtualBox Host-Only với snapshot tạo phạm vi cô lập và khả năng phục hồi phù hợp cho kiểm thử có kiểm soát | AUTHOR_DATA + SOURCE_FACT | ENV-CORE-01/02/05 + NIST | Chỉ chứng minh cấu hình canonical đã ghi nhận |
| A22 | Scenario 1 xác định reachability, TCP 139/445, service fingerprint và SMB dialect; không tự xác minh MS17-010 | AUTHOR_DATA + INTERPRETATION | S1-RAW-01..05 + Nmap docs | Không nâng port/protocol observation thành vulnerability verdict |
| A23 | Scenario 2 xác nhận SMBv1 hiện diện nhưng remote NSE-MS17-010 không cho usable verdict | AUTHOR_DATA | S2-RAW-01..04 | Remote classification = UNKNOWN |
| A24 | Local patch baseline cho thấy Windows target UNPATCHED độc lập với remote scanner verdict | AUTHOR_DATA + SOURCE_FACT | ENV-CORE-03 + Microsoft bulletin | UNPATCHED không đồng nghĩa exploit success |
| A25 | Disable SMBv1 làm thay đổi protocol surface: NT LM 0.12 biến mất, nhưng patch state không đổi | AUTHOR_DATA + INTERPRETATION | B-LOCAL/B-RAW + ENV-CORE-03 | Không gọi PATCHED/SAFE |
| A26 | pfSense làm thay đổi reachability từ Kali: 139/445 chuyển FILTERED và log quy thuộc cho rule; host phía sau không được patch bởi thao tác này | AUTHOR_DATA + INTERPRETATION | C-RULE/C-RAW/C-LOG + ENV-CORE-03 | Chỉ trong topology/source đã đo |
| A27 | Patching, protocol hardening và network filtering là ba lớp kiểm soát khác nhau và nên được đánh giá theo defense-in-depth | SOURCE_FACT + INTERPRETATION | Microsoft/NIST + A24–A26 | Case A patch chưa có canonical experiment |
| A28 | UNKNOWN/no-output là kết quả có ý nghĩa về giới hạn đo, không phải bằng chứng an toàn | INTERPRETATION | NEGATIVE_RESULT_POLICY + Nmap/NIST | Không suy đoán nguyên nhân nếu không có evidence |
| A29 | Rủi ro còn lại và tương thích phải được phân tích theo phạm vi thực nghiệm, không khái quát toàn doanh nghiệp | INTERPRETATION + PROPOSAL | source + canonical cases | Lab một target, một source, không exploit |

## Phản biện chính

- “445 open nghĩa là vulnerable” → bác bằng A22/A23/A24.
- “SMBv1 tắt là đã vá” → bác bằng A25.
- “Firewall filtered nghĩa là host an toàn” → bác bằng A26.
- “NSE không báo vulnerable nghĩa là safe” → bác bằng A23/A24/A28.
- “Không exploit thì không đánh giá được gì” → đề tài vẫn đánh giá được detection, patch ground truth và mitigation trong giới hạn evidence.

## Kết luận chương dự kiến

- Ch2: mô hình và phương pháp đủ để tạo phép đo có truy vết/khôi phục.
- Ch3: dữ liệu canonical cho thấy baseline SMBv1 + UNPATCHED nhưng remote verdict UNKNOWN; Case B và C tác động lên hai lớp khác nhau.
- Ch4: kết quả ủng hộ defense-in-depth và yêu cầu phân biệt mitigation với patch state.
