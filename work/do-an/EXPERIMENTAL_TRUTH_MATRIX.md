# Ma trận sự thật thực nghiệm (Experimental Truth Matrix)

Trạng thái: `CANONICAL_FOR_CHAPTERS_2_3_4`  
Ngày khóa: 2026-10-05  
Phạm vi: dữ liệu thực nghiệm phục vụ Chương 2, Chương 3 và Chương 4 của đồ án SMB/Nmap/NSE–MS17-010.

## 1. Nguyên tắc sử dụng

Tài liệu này là cổng kiểm soát sự thật thực nghiệm trước khi viết báo cáo chính thức. Báo cáo thực nghiệm cũ chỉ được dùng để tham khảo cách tổ chức lập luận, **không được dùng làm bằng chứng cho một sự kiện thực nghiệm**.

Thứ tự ưu tiên khi có mâu thuẫn:

1. Machine-generated raw output hoặc direct local-state artifact (`.nmap`, `.xml`, `.gnmap`, PowerShell/system audit).
2. Direct screenshot/log của đúng trạng thái hoặc lượt canonical.
3. Final run manifest / bounded final closure nếu không mâu thuẫn direct evidence.
4. Summary/interpretation.
5. Kịch bản gốc và tài liệu kỹ thuật để giải thích ý nghĩa phép đo.
6. Báo cáo thực nghiệm cũ, Word cũ và nội dung agent trước đây chỉ là `HISTORICAL_REFERENCE`.

Nếu direct artifact và manifest mâu thuẫn, giữ cả hai, gắn `CONFLICTING_EVIDENCE`, và hạ claim về mức direct artifact cho phép; không hòa giải bằng suy đoán.

Nếu cấp thấp hơn mâu thuẫn cấp cao hơn, giữ cấp cao hơn và ghi mâu thuẫn. Không chọn kết quả thuận lợi hơn để “hòa giải”.

Nhãn dùng trong ma trận:
- `VERIFIED_FACT`: sự thật có bằng chứng trực tiếp.
- `VERIFIED_OBSERVATION`: quan sát trực tiếp nhưng chưa tự cho phép suy luận trạng thái bên trong.
- `ALLOWED_INTERPRETATION`: suy luận được phép trong phạm vi ghi rõ.
- `CONDITIONAL`: chỉ được viết khi nêu kèm điều kiện/giới hạn.
- `HISTORICAL_ONLY`: có trong lượt/báo cáo cũ nhưng không thuộc evidence canonical hiện hành.
- `FORBIDDEN_CLAIM`: không được viết như kết quả chính thức với evidence hiện có.

## 2. Danh tính lượt thực nghiệm canonical

| Thuộc tính | Giá trị khóa | Bằng chứng chính | Trạng thái |
|---|---|---|---|
| Nền tảng | Oracle VM VirtualBox 7.2.20 | `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| Kali | `192.168.56.10/24` | `Final_PreDemo_Audit.txt`, Scenario 1 B1 | VERIFIED_FACT |
| Windows | Windows Server 2012 R2 Standard Evaluation, Build 9600, `192.168.56.20/24` | `Windows_Baseline.txt`, `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| Mạng baseline | Host-Only, một NIC/VM, không NAT, không Bridged | `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| Default route Internet | Không có ở baseline trước demo | `Final_PreDemo_Audit.txt`, Scenario 1 B1 | VERIFIED_FACT |
| Nmap | 7.99 | `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| Snapshot chuẩn | `Before Demo` trên Kali và Windows | `Before_Demo_Snapshots.txt` | VERIFIED_FACT |
| SMB service | LanmanServer Running/Automatic; TCP 139,445 listen | `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| SMB local baseline | SMB1=True; SMB2=True | `Final_PreDemo_Audit.txt` | VERIFIED_FACT |
| Windows Firewall baseline | Allow TCP 139/445 chỉ từ `192.168.56.10`; group File and Printer Sharing mặc định tắt | `Windows_FirewallPrep_Final.txt` | VERIFIED_FACT |
| Patch MS17-010 | `UNPATCHED`; `srv.sys 6.3.9600.16421 < 6.3.9600.18604`; không có KB4012213/KB4012216 hoặc rollup thay thế | `MS17-010_Official_Mapping.txt` | VERIFIED_FACT; prose phải dẫn nguồn Microsoft tương ứng |

## 3. Kịch bản 1 — Nmap SMB 139/445

| ID | Fact/observation | Evidence | Kết luận tối đa được phép | Không được suy ra |
|---|---|---|---|---|
| ETM-S1-01 | Kali có IP/route nội bộ, không default route | B1 + manifest | baseline scan được cô lập theo cấu hình quan sát | không tuyên bố mọi đường thoát host đều bất khả thi |
| ETM-S1-02 | Target `192.168.56.20` được ARP discovery thấy đang up | B2/B3 raw | target hiện diện trên cùng L2 lúc đo | không suy ra SMB hoạt động |
| ETM-S1-03 | TCP 139/445 `open`, reason `syn-ack ttl 128` | `b4_smb_ports.*` | hai cổng có thể tiếp cận từ Kali | không suy ra SMBv1/MS17-010 |
| ETM-S1-04 | `-sV` nhận diện 139 Windows netbios-ssn; 445 Windows Server 2008 R2–2012 microsoft-ds | `b5_smb_version.*` | fingerprint phù hợp họ Windows Server 2008 R2–2012 | exact OS lấy từ local baseline, không từ fingerprint |
| ETM-S1-05 | `smb-protocols`: NT LM 0.12, 2.0.2, 2.1, 3.0, 3.0.2 | `b6_smb_nse.*` | target chấp nhận SMBv1 và các dialect SMB2/3 trên | SMBv1 != MS17-010 vulnerable |
| ETM-S1-06 | `smb2-security-mode`: 3.0.2, signing enabled but not required | `b6_smb_nse.*` | mô tả đúng signing script quan sát | không khái quát mọi dialect hay coi signing là patch |
| ETM-S1-07 | capability có DFS/Leasing/Multi-credit; `smb-os-discovery` không usable output | `b6_smb_nse.*` | chỉ mô tả output thực có | không bịa OS-discovery |
| ETM-S1-08 | đủ 15 raw file B2–B6 | raw folder | đầy đủ về số lượng artifact | không gọi “integrity 100%” theo nghĩa mật mã nếu không có hash manifest |

**Khóa:** Kịch bản 1 chỉ xác lập bề mặt dịch vụ/cấu hình SMB quan sát được. Không kết luận `VULNERABLE to MS17-010`.

## 4. Kịch bản 2 — NSE SMB / MS17-010

| ID | Fact/observation | Evidence | Kết luận tối đa được phép | Không được suy ra |
|---|---|---|---|---|
| ETM-S2-01 | 139/445 `open`, syn-ack | `NSE-SMB-01_ports.*` | reachability tồn tại | không suy ra lỗ hổng |
| ETM-S2-02 | SMBv1 NT LM 0.12 + SMB2/3 dialects | `NSE-SMB-02_protocols.*` | SMBv1 được chấp nhận từ Kali | không suy ra exploitability |
| ETM-S2-03 | signing 3.0.2 enabled but not required | `NSE-SMB-03_signing.*` | trạng thái signing quan sát được | không dùng làm verdict MS17-010 |
| ETM-S2-04 | `smb-vuln-ms17-010` chạy xong nhưng không sinh Host script results/verdict | `NSE-SMB-04_ms17010.*` | **Remote verdict = UNKNOWN / NO USABLE SCRIPT RESULT** | FORBIDDEN: VULNERABLE, SAFE, NOT VULNERABLE, hoặc gán NTSTATUS không có trong raw |
| ETM-S2-05 | local patch baseline = `UNPATCHED` | `MS17-010_Official_Mapping.txt` | hệ điều hành chưa cài bản vá MS17-010 theo ground truth local | UNPATCHED không chứng minh exploit thành công |
| ETM-S2-06 | không có exploitation/Metasploit trong canonical run | manifest/summary | đây là detection/safe assessment | không tạo RCE/SYSTEM/BSOD/callback giả |

**Khóa:** tách hai trục độc lập: `remote scanner verdict = UNKNOWN` và `local patch ground truth = UNPATCHED`.

## 5. Case B — Disable SMBv1

| ID | Fact/observation | Evidence | Kết luận tối đa được phép | Không được suy ra |
|---|---|---|---|---|
| ETM-B-01 | Before: SMB1=True, SMB2=True, FS-SMB1 Installed, patch=UNPATCHED | Case B manifest | baseline trước can thiệp | — |
| ETM-B-02 | Action: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` | screenshot + manifest | runtime SMB1 True→False | không gọi uninstall feature |
| ETM-B-03 | After local: SMB1=False; SMB2=True; FS-SMB1 Installed; service/listeners giữ; patch vẫn UNPATCHED | manifest/summary | thay protocol config, không patch driver | không gọi PATCHED |
| ETM-B-04 | Retest protocols: NT LM 0.12 biến mất; 2.0.2/2.1/3.0/3.0.2 còn | Case B `NSE-SMB-02_protocols.*` | SMBv1 không còn xuất hiện trong phép thương lượng đã đo; SMB2/3 vẫn đáp ứng | không suy ra mọi workload nghiệp vụ SMB2/3 đều đã kiểm thử |
| ETM-B-05 | Retest MS17-010: không script verdict | Case B `NSE-SMB-04_ms17010.*` | verdict = UNKNOWN | FORBIDDEN: “Couldn't negotiate SMBv1”, SAFE, NOT VULNERABLE nếu raw không có |
| ETM-B-06 | `srv.sys` giữ 6.3.9600.16421 | manifest/summary | disable SMBv1 là mitigation/hardening, không phải patch | không nói driver đã được sửa |

**Khóa:** được kết luận bề mặt SMBv1 quan sát từ xa bị loại khỏi phép thương lượng đã đo; không kết luận host đã vá.

## 6. Case C — pfSense Transparent Bridge

| ID | Fact/observation | Evidence | Kết luận tối đa được phép | Không được suy ra |
|---|---|---|---|---|
| ETM-C-01 | Case C canonical = pfSense Transparent Bridge | pfSense bridge/tunable + manifest | pfSense L2 firewall là biến can thiệp | FORBIDDEN: Case C canonical = Windows Firewall |
| ETM-C-02 | Kali/Windows IP không đổi; Windows SMB1=True, SMB2=True, LanmanServer Running, patch=UNPATCHED | pfSense summary | biến thay đổi chính là policy pfSense | không nói host được patch/harden nội tại |
| ETM-C-03 | BLOCK TCP `192.168.56.10 -> 192.168.56.20:139,445`, log enabled, đặt trên pass rule | rule config/order | policy đúng source/dest/ports | không suy ra mọi nguồn/đường đều bị chặn |
| ETM-C-04 | Retest ports: 139/445 từ `open/syn-ack` -> `filtered/no-response` | Case C `NSE-SMB-01_ports.*` | từ Kali, đường TCP 139/445 bị lọc trong topology thử nghiệm | không suy ra service local đã tắt |
| ETM-C-05 | pfSense log tại thời điểm canonical scan ghi blocked TCP SYN từ `.56.10` tới `.56.20:139/445` trên CASE_C_KALI; visible Rule label trong screenshot mâu thuẫn manifest về tên/ID rule | `pfSense_10_Block_Log_CANONICAL.png` + Case C manifest/closure | được kết luận matching SMB SYN traffic bị chặn trong pfSense path; exact named-rule attribution = `CONFLICTING_EVIDENCE / UNRESOLVED` | không được nói log screenshot đã chứng minh chính xác named rule `CASE C - Block SMB Kali to Windows` cho tới khi conflict được resolve |
| ETM-C-06 | Retest MS17-010: 445 `filtered`, không có script verdict | Case C `NSE-SMB-04_ms17010.*` | remote classification = UNKNOWN từ vantage point này; raw chỉ chứng minh 445 filtered và không có verdict | không gọi SAFE/PATCHED/NOT VULNERABLE; không thêm causal explanation ngoài raw |
| ETM-C-07 | host phía sau vẫn UNPATCHED và local SMB1=True | pfSense summary | network filtering giảm exposure từ nguồn/đường thử nhưng không đổi patch/protocol state host | không nói bypass firewall => chắc chắn exploit thành công |

**Khóa:** TCP 139/445 từ Kali bị lọc trong topology Case C và pfSense log ghi matching SMB SYN traffic bị block trên CASE_C_KALI. Exact named-rule attribution của log đang có conflict giữa screenshot và manifest, nên không được viết mạnh hơn. `FILTERED != PATCHED`.

## 7. Ma trận tổng hợp dùng cho Chương 4

| Trạng thái | Reachability từ Kali | SMBv1 từ phép thương lượng | Patch ground truth | NSE MS17-010 | Diễn giải đúng |
|---|---|---|---|---|---|
| Baseline | 139/445 OPEN | Có NT LM 0.12 | UNPATCHED | UNKNOWN | bề mặt SMBv1 tồn tại; host chưa vá; scanner không cho verdict |
| Case B | 445 vẫn khả dụng/listen | Không còn NT LM 0.12; SMB2/3 còn | UNPATCHED | UNKNOWN | protocol mitigation, không patch driver |
| Case C | 139/445 FILTERED từ Kali | không đo qua đường bị chặn; local SMB1 vẫn True | UNPATCHED | UNKNOWN | network mitigation, không đổi host patch state |
| Case A — Patch | **không có canonical evidence trong bộ hiện hành** | **không khóa** | **không khóa** | **không khóa** | chỉ viết như khuyến nghị/lý thuyết tới khi evidence được audit |

## 8. Claim cũ bị cấm tái sử dụng như fact

1. Baseline NSE-SMB-04 = `VULNERABLE` hoặc có `STATUS_INSUFF_SERVER_RESOURCES` trong canonical run.
2. Case A đã cài KB4012213, srv.sys=6.3.9600.18604, hoặc NSE trả STATUS_INVALID_HANDLE nếu chưa có canonical evidence Case A.
3. Case C canonical dùng Windows Firewall.
4. Snapshot `BASELINE_PRE_TEST`/`DETECTION_READY_PRE_MITIGATION` là snapshot canonical hiện hành; snapshot hiện khóa là `Before Demo` trừ khi có lineage riêng.
5. Kali canonical có NAT NIC; pre-demo audit ghi chỉ Host-Only NIC.
6. “NSE chứng minh vulnerable/safe” khi raw không có verdict.
7. “Disable SMBv1 làm script trả lỗi thương lượng cụ thể” nếu raw chỉ không có output.
8. `Filtered = patched/safe/not vulnerable`.
9. `Disable SMBv1 = patched`.
10. `SMBv1 enabled = vulnerable` hoặc `445 open = vulnerable`.
11. RCE/SYSTEM/exploit success/BSOD/callback/Meterpreter trong canonical run.
12. “Không memory leak”, “CPU ổn định”, “Event Viewer không lỗi”, “không BSOD” như kết quả định lượng nếu thiếu artifact tương ứng.
13. “Integrity 100%” theo nghĩa mật mã nếu chưa có hash manifest.
14. “Spoof IP là đủ bypass firewall” hoặc “bypass pfSense thì chắc chắn khai thác thành công”.
15. Các từ tuyệt đối hóa: “hoàn hảo”, “triệt để”, “100% an toàn”, “không thể chối cãi”, “bền vững vĩnh viễn” khi không có tiêu chí định lượng.

## 9. Quy tắc viết Chương 2–3–4

### Chương 2
- Dùng `00_Environment` và kịch bản gốc để mô tả môi trường thật.
- Phân biệt baseline ban đầu với final pre-demo state; Kali ban đầu chưa có Nmap nhưng pre-demo có Nmap 7.99.
- Không đưa kết quả Scenario 1/2 vào phần thiết kế ngoài tiêu chí dự kiến.
- pfSense là biến can thiệp Case C, không được hồi tố thành topology baseline của hai kịch bản chính.

### Chương 3
Mỗi kết quả phải theo chuỗi:

`phép đo -> raw evidence -> quan sát -> phân loại -> giới hạn suy luận`.

Raw output có quyền cao hơn Summary.

### Chương 4
Trục phân tích:
1. OPEN khác SMBv1 ENABLED.
2. SMBv1 ENABLED khác remote MS17-010 verdict.
3. UNKNOWN khác PATCHED/SAFE.
4. UNPATCHED là patch ground truth, không phải bằng chứng RCE.
5. Disable SMBv1 tác động protocol attack surface nhưng không patch driver.
6. pfSense filtering tác động reachability từ nguồn thử nhưng không patch/disable SMBv1 trên host.
7. Phải phân biệt patching, protocol hardening và network access control.

## 10. Evidence map tối thiểu

| Nội dung | Evidence bắt buộc |
|---|---|
| Environment/OS/IP/NIC | `Final_PreDemo_Audit.txt` + baseline |
| Snapshot | `Before_Demo_Snapshots.txt` |
| Patch state | `MS17-010_Official_Mapping.txt` + nguồn Microsoft trong ledger |
| Scenario 1 ports | `b4_smb_ports.nmap/xml` + B4 |
| Scenario 1 version | `b5_smb_version.nmap/xml` + B5 |
| Scenario 1 SMB config | `b6_smb_nse.nmap/xml` + B6 |
| Scenario 2 ports | `NSE-SMB-01_ports.nmap/xml` + NSE01 |
| Scenario 2 protocols | `NSE-SMB-02_protocols.nmap/xml` + NSE02 |
| Scenario 2 signing | `NSE-SMB-03_signing.nmap/xml` + NSE03 |
| Scenario 2 MS17-010 | `NSE-SMB-04_ms17010.nmap/xml` + NSE04; verdict UNKNOWN |
| Case B before/action/after | 3 ảnh local + manifest/summary |
| Case B protocols | Case B `NSE-SMB-02_protocols.*` + screenshot 04 |
| Case B MS17-010 | Case B `NSE-SMB-04_ms17010.*` + screenshot 05; UNKNOWN |
| Case C topology/rules | pfSense 04–08 + manifest/summary |
| Case C port result | canonical screenshot 09 + raw NSE-SMB-01 |
| Case C causal attribution | `pfSense_10_Block_Log_CANONICAL.png` |
| Case C MS17-010 | canonical screenshot 11 + raw NSE-SMB-04; UNKNOWN |

## 11. Cổng duyệt trước prose

Agent không được viết toàn văn Chương 2–3–4 cho tới khi:
1. đọc ma trận này;
2. lập outline mới bám evidence/kịch bản thật;
3. lập evidence map từng mục;
4. báo claim cũ bị loại/chưa có evidence;
5. không dùng Case A như kết quả thực nghiệm nếu chưa audit evidence;
6. được người dùng/reviewer duyệt outline + evidence map.

Sau khi duyệt: **Chương 2 -> review -> Chương 3 -> review -> Chương 4 -> review -> DOCX**.

## 12. Kết luận quản trị

Bộ evidence 2026-10-04 đủ để xây báo cáo thực nghiệm có giá trị mà không cần ép NSE-SMB-04 phải trả `VULNERABLE`. Trục nghiên cứu cần giữ là sự phân biệt giữa **quan sát từ xa**, **trạng thái giao thức**, **ground truth bản vá**, và **tác động của từng lớp mitigation**. Mọi kết luận vượt các ranh giới trên phải mang nhãn thiếu bằng chứng hoặc bị loại khỏi bản chính thức.



## 13. ALL(1).zip audit R2 lock — 2026-10-06

Authoritative internal evidence layer:
- `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R2_ALL_2026_10_06.md`
- `work/do-an/evidence/ALL_2026_10_06/FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`
- `work/do-an/evidence/ALL_2026_10_06/CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
- `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md`
- `work/do-an/evidence/ALL_2026_10_06/CANONICAL_NMAP_TEXT_OUTPUTS.md`
- `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_USE_POLICY_ALL_ZIP.md`

Archive SHA-256:
`dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`.

### 13.1 Command provenance lock
Do not merge operator command and Nmap-recorded argv:
- operator command comes from manifest/screenshot and may contain `sudo`;
- Nmap raw argv comes from `.nmap/.xml/.gnmap` and may contain normalized `--privileged`.

All 13 raw triplets agree internally on Nmap argv: **13/13 PASS**.

### 13.2 Baseline chronology lock
- `Kali_Baseline.txt` is early pre-Nmap history; final pre-demo state has Nmap 7.99.
- pre-demo audit precedes creation of `Before Demo`; later snapshot audit establishes final snapshot state.
- Case C topology is separate from baseline and must not be projected backward.

### 13.3 Case C evidence-grade lock
Direct evidence proves:
- CASE_C_KALI=em2; CASE_C_WINDOWS=em3;
- bridge0 membership;
- `pfil_member=1`, `pfil_bridge=0`;
- configured BLOCK rule source `.56.10` -> destination `.56.20`, SMB_Ports, logging enabled;
- block row above pass row;
- 139/445 filtered/no-response in canonical retest;
- 445 filtered/no MS17-010 verdict.

Final metadata supports, but direct screenshot does not independently prove:
- `pfil_onlyip=1`;
- Internal Network names and management-plane addresses;
- pfSense CE 2.9.0-RELEASE and snapshot metadata.

### 13.4 Case C log conflict lock
`pfSense_10_Block_Log_CANONICAL.png` visibly shows blocked SMB SYN traffic at canonical scan time, but its Rule label reads:
`CASE C baseline pass Kali to Windows (100000104)`.

Manifest/closure claims:
`CASE C - Block SMB Kali to Windows (1000000104)`.

Therefore:
- allowed: matching SMB SYN traffic was blocked in the pfSense path;
- forbidden: exact named-rule attribution is proven by the log screenshot.

Configured Block rule existence/order remain separately proven by direct screenshots.

### 13.5 Report-writing consequence
- Chapter 2 may use verified setup/method facts, with exact commands taken through the command-lineage matrix.
- Chapter 3 must bind each result to raw/direct evidence; do not use summary prose as ground truth.
- Chapter 4 may compare Baseline, Case B and Case C within these bounds.
- Case A remains theory/recommendation only.
