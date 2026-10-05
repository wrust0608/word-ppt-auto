# CHAPTERS 2–4 EVIDENCE MAP — PROPOSED

Trạng thái: `LOCKED_CANONICAL / USER_APPROVED_2026_10_05`

| Section | Nhiệm vụ | Evidence/Source chính | Boundary |
|---|---|---|---|
| 2.1 | lý do/an toàn/phạm vi | đề cương + NIST + Truth Matrix | không kể kết quả |
| 2.2 | topology/env | ENV-CORE-01/05/06/07 | canonical lab only |
| 2.3 | baseline prep | ENV-CORE-01/02/03/04 | patch state tách scanner verdict |
| 2.4 | phương pháp bằng chứng | Evidence Register + Negative Result Policy | raw > summary |
| 2.5 | design Scenario 1 | kịch bản 1 + S1 IDs | không đưa observed results trước Ch3 |
| 2.6 | design Scenario 2 | kịch bản 2 + S2 IDs | không hứa VULNERABLE |
| 2.7 | mitigation design | Case B/C evidence structure + source | Case A = recommendation unless audited |
| 2.8 | criteria | Truth Matrix + Claim Matrix | mỗi lớp kết luận riêng |
| 3.1 | pre-test state | ENV-CORE-01/02/03/04 | state tại run canonical |
| 3.2 | Scenario 1 results | S1-RAW-01..05 + S1-META-01 | open/protocol != vulnerable |
| 3.3.1 | ports | S2-RAW-01 | reachability only |
| 3.3.2 | protocols | S2-RAW-02 | protocol only |
| 3.3.3 | signing | S2-RAW-03 | signing only |
| 3.3.4–3.3.5 | MS17-010 remote | S2-RAW-04 | UNKNOWN |
| 3.4 | local patch reconciliation | ENV-CORE-03 + Microsoft | UNPATCHED != exploit success |
| 3.5 | Case B | B-LOCAL-01/02, B-ACTION-01, B-RAW-01/02 | disable != patch |
| 3.6 | Case C | C-IFACE-01, C-BRIDGE-01, C-TUNE-DIRECT-01, C-RULE-01/02/03, C-RAW-01/02, C-LOG-01 | filtered from Kali != patch; C-LOG-01 proves blocked matching traffic but exact named-rule attribution is unresolved |
| 3.7 | result matrix | all AUTHOR_DATA IDs | no new evidence |
| 4.1–4.2 | evaluation framework/baseline | X2-C02..06 + sources | interpret, not re-run |
| 4.3 | Case B analysis | X2-C07/08 + Microsoft | scope of protocol mitigation |
| 4.4 | Case C analysis | X2-C09..11 + NIST/Microsoft | scope of network mitigation |
| 4.5 | patching role | Microsoft + X2-C13 | no claim Case A tested |
| 4.6 | defense layers | X2-C12 + sources | compare different control layers |
| 4.7 | risk/residual risk | source + canonical observations | no pseudo-quantification |
| 4.8 | limitations | experiment design + missing evidence | explicit threats to validity |
| 4.9 | recommendations | Microsoft/NIST + observed limitations | proposal/source-backed |
