# CHAPTER 3 CURRENT SECTION EVIDENCE MAP

Trạng thái: `LOCKED_CURRENT_2026_10_06`

Mục đích: ánh xạ cấu trúc Chương 3 hiện hành tới các nhóm bằng chứng đã stage sau X6.

File này thay thế phần ánh xạ Chương 3 theo numbering cũ trong `CHAPTERS_2_4_EVIDENCE_MAP.md`.

| Section hiện hành | Nhiệm vụ | Evidence chính | Evidence phụ/nguồn ngoài | Boundary |
|---|---|---|---|---|
| 3.1 Baseline | Xác lập trạng thái trước đo | ENV-CORE-01/02/03/04/05 + staged baseline local/visual | Microsoft S032 cho KB/version threshold | Không đưa Scenario 1/2 result; screenshot srv.sys không tự đủ kết luận UNPATCHED |
| 3.2 Scenario 1 | B2–B6 discovery/service/protocol results | S1-RAW-01..05 + direct Scenario 1 visuals | S1-META-01 chỉ lineage | .56.100 UNKNOWN; OPEN/SMBv1 không đồng nghĩa vulnerable |
| 3.3 Scenario 2 | NSE-SMB-01..04 + remote/local cross-check | S2-RAW-01..04 + direct Scenario 2 visuals + ENV-CORE-03 | Microsoft S032 khi cần nhắc patch mapping | NSE-SMB-04 remote = UNKNOWN; không invent cause/NTSTATUS |
| 3.4 Case B | Before/action/after + two retests | B-LOCAL-01/02, B-ACTION-01, B-RAW-01/02 + direct visuals | B-META-01 chỉ lineage | SMBv1 disabled != patched; không claim workload validation |
| 3.5 Case C | Config/rule/order + Nmap + log + local state | C-IFACE-01, C-BRIDGE-01, C-TUNE-DIRECT-01, C-RULE-01/02/03, C-RAW-01/02, C-LOG-01 + direct visuals | C-META-01/C-CLOSURE-01 chỉ lineage/context | filtered != patched; exact named-rule attribution unresolved |
| 3.6 Comparison | So sánh observations đã approved | Chỉ approved outputs từ 3.1–3.5 | Không mở evidence mới | Không risk score/effectiveness ranking |
| 3.7 Summary | Tóm tắt empirical findings | Chỉ approved conclusions từ 3.1–3.6 | Không evidence mới | Chuyển sang Ch4, không recommendation |

## Isolation by phase

- X7A chỉ baseline evidence.
- X7B chỉ Scenario 1 + approved baseline facts nếu cần.
- X7C chỉ Scenario 2 + approved baseline patch fact cho cross-check.
- X7D chỉ Case B + approved baseline.
- X7E chỉ Case C + approved baseline.
- X7F chỉ approved outputs của X7A–X7E.

## Evidence precedence

`direct raw/local/visual > metadata lineage > historical/supporting > old report prose`.

Known Case C conflict is preserved:
- configured Block rule is directly proven;
- log directly shows matching SMB SYN Block events;
- screenshot rule label conflicts with manifest;
- exact named-rule attribution remains unresolved.
