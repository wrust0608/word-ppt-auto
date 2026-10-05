# CLAIM MATRIX 2–4 — PROPOSED

Trạng thái: `LOCKED_CANONICAL_FOR_CHAPTERS_2_4`

| Claim ID | Claim | Type | Evidence/Source | Support | Dùng ở | Boundary |
|---|---|---|---|---|---|---|
| X2-C01 | Canonical lab dùng VirtualBox, Kali, Windows Server 2012 R2, Host-Only và snapshot Before Demo | AUTHOR_DATA | ENV-CORE-01/02/05/06/07 | STRONG | Ch2 | Không thay bằng topology lịch sử |
| X2-C02 | Windows target có local patch ground truth UNPATCHED | AUTHOR_DATA + SOURCE_FACT | ENV-CORE-03 + Microsoft MS17-010 | STRONG | Ch2/3/4 | Không chứng minh exploit success |
| X2-C03 | Scenario 1 quan sát TCP 139/445 open từ Kali | AUTHOR_DATA | S1-RAW-03 | STRONG | Ch3 | Open != vulnerable |
| X2-C04 | Scenario 1/2 quan sát SMBv1 NT LM 0.12 cùng SMB2/3 dialects | AUTHOR_DATA | S1-RAW-05, S2-RAW-02 | STRONG | Ch3 | SMBv1 != vulnerable |
| X2-C05 | SMB signing được quan sát enabled but not required ở dialect script trả về | AUTHOR_DATA | S2-RAW-03 | STRONG | Ch3 | Không dùng làm verdict MS17-010 |
| X2-C06 | Baseline smb-vuln-ms17-010 không sinh usable verdict | AUTHOR_DATA | S2-RAW-04 | STRONG | Ch3/4 | Classification = UNKNOWN |
| X2-C07 | Disable SMBv1 làm NT LM 0.12 biến mất trong retest và SMB2/3 còn phản hồi | AUTHOR_DATA | B-LOCAL-01/02, B-RAW-01 | STRONG | Ch3/4 | Không đồng nghĩa patched |
| X2-C08 | Case B remote MS17-010 verdict vẫn UNKNOWN | AUTHOR_DATA | B-RAW-02 | STRONG | Ch3/4 | Không gọi safe |
| X2-C09 | pfSense block rule làm 139/445 filtered từ Kali | AUTHOR_DATA | C-RULE-02, C-RAW-01 | STRONG | Ch3/4 | Chỉ vantage point đã đo |
| X2-C10 | pfSense log quy thuộc blocked SYN cho rule Case C | AUTHOR_DATA | C-LOG-01 | STRONG | Ch3 | Không suy ra host patched |
| X2-C11 | Case C không cho phép remote MS17-010 classification qua filtered path | AUTHOR_DATA | C-RAW-02 | STRONG | Ch3/4 | UNKNOWN/not assessable from that vantage |
| X2-C12 | Patch, disable SMBv1 và network filtering tác động lên các lớp khác nhau | INTERPRETATION | X2-C02/C07/C09 + Microsoft/NIST | STRONG | Ch4 | Không nói mọi lớp tương đương |
| X2-C13 | Case A patch chưa có canonical experiment | AUTHOR_DATA/PROJECT_STATE | Truth Matrix + Evidence Register | STRONG | Ch3/4 | Chỉ recommendation/supplementary |
| X2-C14 | Metasploit thuộc phần nghiên cứu công cụ nhưng không có canonical exploit result | SOURCE_FACT + AUTHOR_DATA | Đề cương + evidence inventory | STRONG | Ch1/limits | Không claim RCE/SYSTEM |
| X2-C15 | UNKNOWN phải được giữ như trạng thái bất định | INTERPRETATION | NEGATIVE_RESULT_POLICY | STRONG | Ch3/4 | Không convert verdict |
