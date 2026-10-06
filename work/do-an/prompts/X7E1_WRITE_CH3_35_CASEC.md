# X7E1 — WRITE SECTION 3.5 CASE C

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7e1-ch3-casec-draft`  
Approved integration base: `fa7ff8c269d1358c380beabbd2610fda37d3567a`

## 0. Objective

Write the complete student-facing prose for Chapter 3 Section 3.5:

`3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

Use the user-approved X7E0 presentation plan.

This task also creates the three approved presentation crops:
- Hình 3.9
- Hình 3.10
- Hình 3.11

Do not add a fourth standard figure.

Do not write Sections 3.6–3.7.
Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7e1-ch3-casec-draft
git pull --ff-only origin feature/x7e1-ch3-casec-draft
git status --short
git rev-parse HEAD
git merge-base --is-ancestor fa7ff8c269d1358c380beabbd2610fda37d3567a HEAD
```

If lineage fails, STOP.

## 2. Mandatory read order

Read fully:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
6. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
7. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
8. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
9. `work/do-an/CH3_35_CASEC_FIGURE_SELECTION_R1.md`
10. `work/do-an/CH3_35_CASEC_PRESENTATION_PLAN_R1.md`
11. `work/do-an/CH3_35_CASEC_CLAIM_EVIDENCE_MAP_R1.md`
12. `work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R1.md`
13. `work/do-an/X7E0_CASEC_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`
14. `work/do-an/X7E0_CASEC_PLAN_USER_APPROVAL_LOCK.md`
15. approved Sections 3.1–3.4 for continuity:
    - `CH3_31_BASELINE_DRAFT_R1.md`
    - `CH3_32_SCENARIO1_DRAFT_R1.md`
    - `CH3_33_SCENARIO2_DRAFT_R1.md`
    - `CH3_34_CASEB_DRAFT_R1.md`
16. every canonical Case C staged artifact under:
    `work/do-an/chapter3/evidence/case_c/`

Visually inspect all three source images selected for Hình 3.9–3.11 before creating crops.

## 3. Locked section structure

Use exactly:

### `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

#### `3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`

#### `3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`

Do not add another H3.

## 4. Locked presentation

Use exactly:
- **Bảng 3.6**
- **Hình 3.9**
- **Hình 3.10**
- **Hình 3.11**

Do not add:
- bridge screenshot as a separate standard figure;
- NSE04 screenshot as Hình 3.12;
- interface-assignment screenshot;
- sysctl screenshot;
- baseline-pass screenshot;
- full rule-form screenshot;
- montage/composite.

## 5. Create Hình 3.9

Source:

`work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png`

Approved crop direction:
- approximately `x=15, y=190, width=470, height=340`

Before creating the final file:
- visually inspect the source;
- confirm the crop preserves:
  - selected `CASE_C_KALI` context;
  - `Rules (Drag to Change Order)`;
  - complete Block row;
  - complete Pass row;
- remove:
  - insecure-password warning;
  - footer;
  - irrelevant controls.

If exact geometry needs a small adjustment to preserve those elements, adjust minimally and record the final rectangle.

Create:

`work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`

Do not annotate, resize-before-crop, sharpen or alter source evidence.

## 6. Create Hình 3.10

Source:

`work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`

Approved direction:
- around `x=195, y=120, width=660, height=505`

Visually verify the final crop preserves:
- complete Nmap command;
- `Host is up` / `arp-response`;
- `139/tcp filtered netbios-ssn no-response`;
- `445/tcp filtered microsoft-ds no-response`;
- MAC line;
- `Nmap done`.

Create:

`work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`

Do not annotate.

## 7. Create Hình 3.11 — mandatory direct visual verification

Source:

`work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png`

The source is approximately `1359x17637` and the plan's coordinates are PROVISIONAL ONLY.

Starting search region:
- approximately `x=40, width=1280`
- approximately `y=15280..15550`

Do NOT blindly apply that rectangle.

You must:
1. inspect the original image directly;
2. inspect candidate crops around the expected region;
3. choose the tightest readable final rectangle that preserves:
   - required log column headings for interpretation;
   - relevant Block rows for destination 139 and 445;
   - source `192.168.56.10`;
   - destination `192.168.56.20`;
   - TCP SYN / `TCP:S`;
   - interface `CASE_C_KALI`;
   - Rule column / visible conflicting rule label.

Critical:
- do not crop away the Rule column to hide the conflict;
- do not edit the visible rule label;
- do not blur/remove conflicting content.

Create:

`work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`

Record the exact final crop coordinates in the manifest.

## 8. Create crop manifest

Create:

`work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`

For each Hình 3.9–3.11 record:
- source path;
- source SHA-256;
- source dimensions;
- exact final crop rectangle;
- derived path;
- derived dimensions;
- derived SHA-256;
- content preserved;
- content removed;
- interpretation boundary.

For Hình 3.11 explicitly record that:
- visible rule-label conflict is preserved;
- crop does not prove the exact named Block rule matched.

## 9. Reader question

Section 3.5 must answer:

**When the tested Kali → Windows path was placed through pfSense Transparent Bridge with SMB filtering rules, what changed in the remote observations, what did pfSense log, and what remained unchanged on the Windows host?**

The reader should understand this without opening repository metadata.

## 10. Length discipline

Target:
- approximately **1,300–1,600 prose words**, excluding table/captions;
- 2 H3 only;
- 1 table;
- 3 figures.

Case C has more evidence than Case B, but do not turn it into a pfSense configuration tutorial.

Use Bảng 3.6 to compress repeated facts.

Avoid repeating:
- the full baseline story;
- the meaning of MS17-010;
- the full UNKNOWN theory;
- the patch-verification method;
- every pfSense setting already visible in Hình 3.9.

## 11. Section 3.5 opening

Open with a concise paragraph that establishes:
- Case C examines a network-path control layer;
- the tested Kali → Windows path is placed through pfSense Transparent Bridge;
- the comparison focuses on remote port observations, firewall logs, remote MS17 result and Windows-local point-in-time state.

Do not claim effectiveness ranking.
Do not claim the system becomes safe.

## 12. Section 3.5.1 content

Explain only what is needed to understand the test:

### Topology
- Kali `192.168.56.10`
- Windows `192.168.56.20`
- tested path goes through pfSense Transparent Bridge:
  - `CASE_C_KALI / em2`
  - `bridge0`
  - `CASE_C_WINDOWS / em3`
- management path is separate and is not the tested SMB path.

Use bounded wording:
`Trong topology Case C, đường thử nghiệm Kali → Windows được bố trí đi qua bridge0 của pfSense.`

Do not say every possible network path is forced through pfSense.

### Bridge filtering settings
You may state:
- `pfil_member=1`
- `pfil_bridge=0`

Keep this brief. No FreeBSD tutorial.

### Policy
State:
- Block IPv4 TCP;
- source `192.168.56.10`;
- destination `192.168.56.20`;
- destination ports 139/445 via `SMB_Ports`;
- logging enabled;
- Block row appears above Pass row.

Do not explain rule-processing theory beyond what is necessary.

### Hình 3.9

Insert:

`![Hình 3.9](chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png)`

Caption:

`Hình 3.9. Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên giao diện CASE_C_KALI của pfSense`

Before the figure:
- tell the reader to observe the Block row and Pass row.

After the figure:
- state only what the figure directly shows;
- do not say this figure alone proves traffic was actually blocked.

## 13. Bảng 3.6

Use exactly one table with title:

`Bảng 3.6. So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense (Case C)`

Use the approved four-column structure:

`Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case C) | Diễn giải trực tiếp & Giới hạn kết luận`

Keep the approved row families:

1. Vị trí kiểm soát mạng / kiến trúc đường truyền
2. Chính sách lọc pfSense
3. Thứ tự quy tắc
4. TCP 139 remote
5. TCP 445 remote
6. pfSense log
7. MS17-010 remote result
8. SMBv1 local configuration
9. LanmanServer / local listeners
10. local patch state

Important baseline wording:
- do NOT say "no firewall";
- use:
  `Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows`
- Windows Firewall baseline already existed.

For port baseline:
- 139/445 OPEN with syn-ack belongs to earlier Scenario 1 baseline measurements;
- Case C retest:
  - 139 FILTERED / no-response;
  - 445 FILTERED / no-response.

For MS17:
- baseline and Case C remain UNKNOWN;
- no cause assigned.

For Windows-local state:
- use point-in-time metadata wording;
- do not imply continuous uptime.

## 14. Section 3.5.2 — remote port retest

Direct raw Case C result:
- host up, ARP response;
- `139/tcp filtered netbios-ssn no-response`;
- `445/tcp filtered microsoft-ds no-response`.

Allowed:
`Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái FILTERED với lý do no-response trong phép đo Case C.`

Do not say:
- ports are closed;
- local services stopped;
- Windows firewall caused it;
- server was patched;
- pfSense "fixed" the vulnerability.

### Hình 3.10

Insert:

`![Hình 3.10](chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png)`

Caption:

`Hình 3.10. Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense`

Use the figure to show:
- host response;
- both FILTERED rows;
- no-response.

Keep:
`FILTERED != PATCHED`.

## 15. Section 3.5.2 — firewall log comparison

Direct visual evidence supports:
- Action = Block;
- Interface = CASE_C_KALI;
- source = `.56.10`;
- destination = `.56.20:139` / `:445`;
- TCP SYN.

Allowed wording:

`Trong lượt Case C, Nmap ghi nhận TCP 139/445 ở trạng thái FILTERED, đồng thời log pfSense ghi nhận lưu lượng TCP SYN tương ứng từ Kali tới các cổng này bị Block trên đường pfSense.`

Call this:
`đối chiếu liên tầng`

Do not call it:
- causal proof;
- exact same wall-clock event;
- synchronized timestamp proof.

### Hình 3.11

Insert:

`![Hình 3.11](chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png)`

Caption:

`Hình 3.11. Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm`

Before/after figure:
- briefly explain what columns to observe;
- explicitly preserve the rule-label discrepancy.

## 16. Mandatory rule-label conflict wording

Direct screenshot visibly shows a rule label equivalent to:

`CASE C baseline pass Kali to Windows (100000104)`

Manifest/final closure attributes the traffic to:

`CASE C - Block SMB Kali to Windows (1000000104)`

This remains unresolved.

Student-facing prose should not turn into a long forensic discussion.

Use one concise disclosure such as:

`Ảnh nhật ký hiển thị nhãn quy tắc không trùng với tên được ghi trong manifest; vì vậy báo cáo chỉ sử dụng ảnh để xác nhận hành động Block đối với lưu lượng SMB SYN tương ứng, không dùng ảnh này để quy thuộc tuyệt đối cho một tên quy tắc cụ thể.`

Do not hide the conflict.
Do not invent a reconciliation.

## 17. Section 3.5.2 — MS17 retest

Direct raw result:
- host up;
- `445/tcp filtered microsoft-ds`;
- no `Host script results:`;
- no usable vulnerability verdict.

Required classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

Required boundary:

`Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.`

Keep:
`UNKNOWN != SAFE`.

Do not say:
- because port 445 was blocked, the script could not run;
- scanner failed because pfSense;
- Nmap hid the result;
- false negative;
- SAFE;
- NOT VULNERABLE;
- PATCHED.

No Hình 3.12 in the standard layout.

## 18. Section 3.5.2 — Windows-local state

Use correct provenance.

Case C does not include a new Windows screenshot.

Use:
- baseline Section 3.1;
- Case C metadata / `RUN4_PAUSE_STATE_REPORT.txt`.

Point-in-time facts:
- SMB1=True;
- SMB2=True;
- LanmanServer=Running;
- local TCP 139/445 listeners present;
- patch state UNPATCHED;
- numeric `srv.sys` version used for patch comparison = `6.3.9600.16421`.

Do not say:
- "unchanged at every moment";
- zero downtime;
- Windows was never modified historically;
- SMBv1 vulnerable/exploitable is proven;
- local state is proven by pfSense screenshots.

Use:
`Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows; metadata cuối Case C ghi nhận...`

## 19. Timebase boundary

Do not globally align Kali and pfSense timestamps.

Prefer not to mention the displayed times in the student-facing prose.

Do not write:
- 03:20:18 Kali = 14:20:18 pfSense;
- systems are synchronized.

Cross-layer comparison should rely on:
- source/destination IPs;
- destination ports;
- TCP SYN;
- controlled Case C run lineage.

## 20. Section conclusion

End Section 3.5 with a concise empirical conclusion:

Must make clear:
- tested Kali → Windows path went through pfSense;
- remote 139/445 were observed FILTERED;
- matching SMB SYN traffic was logged as Blocked on pfSense;
- remote MS17 result remained UNKNOWN;
- Windows-local SMB1 remained True and patch classification remained UNPATCHED;
- therefore `FILTERED != PATCHED`.

Do not rank Case C against Case B here.

Do not recommend a final security architecture.

A short transition to Section 3.6 may say that the next section compares the observed state changes across baseline, Case B and Case C.

## 21. Academic style

Write as a Vietnamese Information Security graduation/project report.

Prefer:
- `đề tài`;
- `kết quả đo`;
- `ghi nhận`;
- `đường thử nghiệm`;
- `sau can thiệp`;
- `đối chiếu`;
- `trạng thái cục bộ`.

Avoid:
- canonical;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- closure;
- manifest as internal-management jargon unless needed for provenance;
- "100% effective";
- "eliminates exploitability";
- "intrinsically vulnerable";
- marketing/security certainty language.

Do not expose internal claim IDs such as `CC-C01`.

## 22. Required output files

Create:

- `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
- `work/do-an/CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`
- `work/do-an/chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`

Do not modify approved X7E0 plan artifacts.

## 23. Self-review

Create:

`work/do-an/CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`

Report:
- prose word count;
- paragraph count;
- H2/H3 count;
- table count;
- figure count;
- Bảng 3.6 presence;
- Hình 3.9–3.11 presence;
- exact crop coordinates + source/derived SHA;
- no Hình 3.12 standard figure;
- no exact named-rule attribution;
- rule-label conflict preserved;
- no global timestamp synchronization claim;
- no NSE04 cause invention;
- no SAFE/NOT VULNERABLE/PATCHED claim;
- no `FILTERED = PATCHED`;
- no Windows-local state attributed to pfSense images;
- no zero-downtime/continuous-state claim;
- no Case C effectiveness ranking;
- no Chapter 4 recommendation leakage;
- no internal QA/governance vocabulary in student-facing prose.

Do not self-declare external PASS.

Final state:

`X7E1_CASEC_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

## 24. Required searches

Search the draft for problematic wording/concepts:

- `do cổng 445`
- `script không thể`
- `Nmap tự động`
- `false negative`
- `SAFE`
- `NOT VULNERABLE`
- `PATCHED`
- `nhân quả`
- `bắt nguồn từ`
- `hoàn toàn không thay đổi`
- `zero downtime`
- `không gián đoạn`
- `bảo đảm tuyệt đối`
- `eliminated exploitability`
- `intrinsically vulnerable`
- `CC-C`
- Evidence ID / Claim ID / gate / governance.

Manual review is required because forbidden terms may appear inside an explicit inequality/boundary or in a sentence saying they are not concluded.

## 25. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_35_CASEC_DRAFT_R1.md
git diff --check
```

You may run:
`uv run python scripts/validate_project.py`

Do not modify project infrastructure to make QA pass.

Verify source evidence bytes are unchanged.

## 26. Git

Commit:

`draft(ch3): write Case C section 3.5 R1`

Push:

`feature/x7e1-ch3-casec-draft`

Do not merge.

## 27. Handoff

Return:

1. branch;
2. starting SHA;
3. final local/remote SHA;
4. created files;
5. prose word/paragraph counts;
6. heading/table/figure counts;
7. Bảng 3.6 summary;
8. Hình 3.9 crop rectangle + SHA;
9. Hình 3.10 crop rectangle + SHA;
10. Hình 3.11 exact visually verified crop rectangle + SHA;
11. rule-label-conflict handling;
12. Nmap FILTERED audit;
13. NSE04 UNKNOWN audit;
14. Windows-local provenance audit;
15. timebase audit;
16. overclaim search;
17. QA results;
18. clean git status.

Final state:

`X7E1_CASEC_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7F.
Do not write Sections 3.6–3.7.
Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
