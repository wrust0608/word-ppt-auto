# X7D1 — WRITE SECTION 3.4 CASE B

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7d1-ch3-caseb-draft`  
Approved integration base: `6c3e8c326321fd372dc6d047077bdc7256af0d09`

## 0. Objective

Write the complete student-facing prose for Chapter 3 Section 3.4:

`3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`

Use the user-approved X7D0 presentation plan.

This task must produce a concise, thesis-quality result section that reads naturally after Sections 3.1–3.3.

Do not write like an evidence audit or command diary.

Do not rewrite Chapter 2.
Do not rewrite Sections 3.1–3.3.
Do not open Case C.
Do not build DOCX.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7d1-ch3-caseb-draft
git pull --ff-only origin feature/x7d1-ch3-caseb-draft
git status --short
git rev-parse HEAD
git merge-base --is-ancestor 6c3e8c326321fd372dc6d047077bdc7256af0d09 HEAD
```

If lineage is wrong, STOP.

## 2. Mandatory read order

Read fully:

1. `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md`
2. `work/do-an/PROJECT_STATE.md`
3. `work/do-an/CHAPTER_3_CONTRACT.md`
4. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
6. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
7. `work/do-an/CH3_34_CASEB_PRESENTATION_PLAN_R1.md`
8. `work/do-an/CH3_34_CASEB_FIGURE_SELECTION_R1.md`
9. `work/do-an/CH3_34_CASEB_CLAIM_EVIDENCE_MAP_R1.md`
10. `work/do-an/X7D0_CASEB_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`
11. `work/do-an/X7D0_CASEB_PLAN_USER_APPROVAL_LOCK.md`
12. approved `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
13. approved `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
14. approved `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
15. all canonical Case B staged evidence under:
    `work/do-an/chapter3/evidence/case_b/`

Visually inspect the two source screenshots selected for Hình 3.7 and Hình 3.8 before cropping.

## 3. Locked structure

Use exactly:

### `3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`

#### `3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ`

#### `3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng`

Do not add another H3.

## 4. Locked presentation

Use exactly:

- **Bảng 3.5** — one before/after comparison table;
- **Hình 3.7** — local state after intervention;
- **Hình 3.8** — remote SMB dialect retest.

Do not add:
- Before screenshot;
- Action screenshot;
- combined NSE04 screenshot;
- extra table;
- extra figure.

## 5. Create approved presentation crops

Create:

`work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`

from:

`work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png`

using approved crop:

`x=0, y=30, width=872, height=310`

Source SHA-256:
`2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad`

Create:

`work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`

from:

`work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png`

using approved crop:

`x=0, y=24, width=1280, height=400`

Source SHA-256:
`21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a`

Do not:
- annotate;
- sharpen;
- resize source before crop;
- modify original evidence;
- create montage/composite.

Visually inspect both derived crops.

## 6. Create crop manifest

Create:

`work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`

For each derived image record:

- source path;
- source SHA-256;
- source dimensions;
- exact crop rectangle;
- derived path;
- derived dimensions;
- derived SHA-256;
- content preserved;
- content removed;
- interpretation boundary.

## 7. Writing goal

Section 3.4 must answer one simple reader question:

**When SMBv1 server configuration was disabled, what changed locally and remotely, and what did not change?**

The section should be understandable without opening the repository.

Narrative flow:

`before -> action -> local after-state -> remote protocol retest -> remote MS17 retest -> bounded conclusion -> transition to Case C`

## 8. Length discipline

Do not maximize completeness at the expense of readability.

Target:
- approximately **1,100–1,400 prose words**, excluding table/captions;
- about 10–14 prose paragraphs;
- 2 H3 only;
- 1 table;
- 2 figures.

Sections 3.1–3.3 are already substantial.

Do not re-explain:
- what TCP 445 is;
- what SMBv1 is;
- what MS17-010 is;
- all five baseline dialects in long prose;
- the full patch-verification method;
- the full UNKNOWN theory.

Refer back briefly to earlier sections instead.

## 9. Section 3.4 opening

Open with a short result-oriented paragraph.

It should establish:
- this is the first controlled intervention;
- the changed variable is SMBv1 server configuration;
- the section compares local state and selected remote retests against the approved baseline.

Do not:
- call the mitigation effective/safe;
- give Chapter 4 risk conclusions;
- repeat the entire baseline.

## 10. Section 3.4.1 content

Must cover concisely:

### Before
From approved baseline / Case B before state:
- `EnableSMB1Protocol=True`
- `EnableSMB2Protocol=True`
- `FS-SMB1=Installed`
- `LanmanServer=Running`

Do not turn these four values into a long repeated baseline narrative.

### Action
State the intervention:

`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Interpret only as:
- changing SMB server configuration.

Do not call it:
- patch installation;
- feature uninstall;
- OS update;
- driver update.

### After local
Direct after-state:
- `EnableSMB1Protocol=False`
- `EnableSMB2Protocol=True`
- `FS-SMB1=Installed`
- `LanmanServer=Running`

Key interpretation:
- SMB1 server configuration changed;
- SMB2 property remained True;
- Windows SMB1 feature remained installed;
- LanmanServer was observed Running after the intervention.

Do not say:
- zero downtime;
- no interruption;
- all workloads remained healthy;
- feature removed;
- patched.

### Hình 3.7

Insert:

`![Hình 3.7](chapter3/presentation/3_4/Hinh_3_7_After_Local.png)`

Caption:

`Hình 3.7. Trạng thái cấu hình SMB, tính năng FS-SMB1 và dịch vụ LanmanServer sau khi vô hiệu hóa SMBv1`

Before the figure:
- tell the reader what to look for.

After the figure:
- state the direct result in one concise paragraph;
- state the key boundary:
  `SMBv1 disabled != FS-SMB1 uninstalled`
  and
  `SMBv1 disabled != PATCHED`.

Do not repeat every table cell in prose.

## 11. Bảng 3.5

Use the user-approved table design from:

`CH3_34_CASEB_PRESENTATION_PLAN_R1.md`

Title exactly:

`Bảng 3.5. So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B)`

Keep the eight comparison rows:
1. EnableSMB1Protocol
2. EnableSMB2Protocol
3. FS-SMB1
4. LanmanServer
5. TCP 445
6. SMB dialects
7. MS17-010 remote result
8. local patch state

Preserve all corrected R2 boundaries.

Do not:
- add raw command strings;
- add internal IDs;
- add repository paths;
- add post-Case-B `syn-ack`;
- call OPEN a vulnerability finding;
- say SMB2 workloads were validated.

The table is the main compression device.

Because the table already contains many repeated facts, prose around it must synthesize rather than restate all eight rows.

## 12. Section 3.4.2 — protocol retest

Direct raw Case B result:

- target host up;
- `445/tcp open microsoft-ds`;
- `smb-protocols` records:
  - `2.0.2`
  - `2.1`
  - `3.0`
  - `3.0.2`
- `NT LM 0.12 (SMBv1)` does not appear.

Allowed wording:

`Kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ của phép đo lại.`

Do not say:
- successful negotiation;
- successful handshake;
- fully supported;
- full workload compatibility;
- SMBv1 uninstalled.

### Hình 3.8

Insert:

`![Hình 3.8](chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png)`

Caption:

`Hình 3.8. Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1`

Before figure:
- tell the reader the measured difference being checked.

After figure:
- state that SMBv1 no longer appears in the measured dialect list;
- the four SMB2/3 dialect values remain recorded;
- this does not prove full application/workload continuity.

## 13. Section 3.4.2 — MS17-010 retest

Direct raw result:

- target up;
- TCP 445 OPEN;
- scan reaches `Nmap done`;
- no `Host script results:` block;
- no usable vulnerability verdict;
- no displayed error establishing a cause.

Required classification:

`UNKNOWN / NO USABLE SCRIPT RESULT`

Required interpretation:

`Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có.`

Keep:

`UNKNOWN != SAFE`

Do not say:
- false negative;
- scanner limitation caused it;
- SMBv1 probe was silenced;
- couldn't negotiate SMBv1;
- NTSTATUS;
- IPC$ cause;
- script failed;
- safe;
- not vulnerable;
- patched.

Do not add the optional combined NSE04 screenshot.

One concise paragraph is enough.

## 14. Local patch state

Keep:

`UNPATCHED`

but state provenance correctly.

Preferred wording concept:

`Trạng thái bản vá cục bộ vẫn được giữ ở phân loại UNPATCHED theo mốc đã xác lập tại Mục 3.1; Case B không ghi nhận thao tác cài bản vá.`

Do not imply Hình 3.7 re-measured:
- srv.sys;
- hotfix inventory.

Do not repeat the exact srv.sys version unless needed in the table/brief cross-reference.

## 15. Four-layer distinction

The underlying technical distinction must remain correct:

1. SMB server configuration;
2. Windows feature installation state;
3. local patch state;
4. remote NSE verdict.

But do not reproduce the large four-layer ASCII diagram from the internal plan.

Student-facing prose should explain the distinction naturally in 1–2 paragraphs.

No internal governance language.

## 16. Section conclusion

End Section 3.4 with a concise empirical conclusion:

It should make clear:
- the intervention changed the SMB1 server configuration;
- the SMB1 dialect disappeared from the selected remote protocol retest;
- TCP 445 remained OPEN;
- the local patch classification remained UNPATCHED;
- the remote MS17-010 result remained UNKNOWN.

Do not rank effectiveness.

Do not say the host is safer/safe.

Then use a brief transition equivalent to:

`Case B thay đổi cấu hình giao thức ở máy chủ; Case C tiếp tục khảo sát một lớp kiểm soát khác trên đường truyền mạng bằng pfSense Transparent Bridge.`

Do not reveal Case C results.

## 17. Academic style

Write as a Vietnamese Information Security graduation/project report.

Prefer:
- `đề tài`;
- `kết quả đo`;
- `ghi nhận`;
- `trước can thiệp`;
- `sau can thiệp`;
- `phép đo lại`;
- `không xuất hiện trong danh sách phương ngữ`.

Avoid:
- canonical;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- ground truth;
- QA jargon;
- “mitigation effective”;
- marketing-like security claims.

Use paragraphs with natural variation.

Do not write every paragraph in the same formula.

## 18. Required output files

Create:

- `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- `work/do-an/CH3_34_CASEB_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`
- `work/do-an/chapter3/presentation/3_4/Hinh_3_7_After_Local.png`
- `work/do-an/chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`

Do not modify the approved X7D0 plan artifacts.

## 19. Self-review

Create:

`work/do-an/CH3_34_CASEB_DRAFT_SELF_REVIEW_R1.md`

Report:
- prose word count;
- paragraph count;
- H2/H3 count;
- table count;
- figure count;
- Bảng 3.5 presence;
- Hình 3.7/Hình 3.8 presence;
- crop SHA/dimensions;
- no-before/no-action/no-combined-NSE04 figure audit;
- no post-Case-B syn-ack;
- no successful-negotiation language;
- no zero-downtime/workload claim;
- no feature-uninstall claim;
- no patched/safe/not-vulnerable claim;
- correct UNPATCHED provenance;
- correct UNKNOWN boundary;
- no Case C result leakage;
- no Chapter 4 analysis leakage;
- no internal QA/governance vocabulary in report prose.

Do not self-declare external PASS.

Final state:
`X7D1_CASEB_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

## 20. Required searches

Search the draft for problematic strings/concepts:

- `syn-ack` in Case B after/retest context;
- `đàm phán thành công`;
- `bắt tay thành công`;
- `zero downtime`;
- `không gián đoạn`;
- `hoạt động bình thường`;
- `fully compatible`;
- `feature uninstalled`;
- `patched`;
- `safe`;
- `not vulnerable`;
- `false negative`;
- `Couldn't negotiate SMBv1`;
- `STATUS_`;
- `IPC$`;
- `SMBv1 probe silenced`;
- Evidence IDs;
- Claim IDs;
- gate/governance language.

Where a forbidden English term appears only inside an explicit inequality such as `SMBv1 disabled != PATCHED`, review manually rather than relying only on raw count.

## 21. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Verify source evidence bytes are unchanged.

## 22. Git

Commit:

`draft(ch3): write Case B section 3.4 R1`

Push:

`feature/x7d1-ch3-caseb-draft`

Do not merge.

## 23. Handoff

Return:

1. branch;
2. starting SHA;
3. local/remote SHA;
4. created file list;
5. prose word count/paragraph count;
6. heading/table/figure counts;
7. Bảng 3.5 summary;
8. Hình 3.7/Hình 3.8 crop summary + SHA;
9. before/action/after narrative audit;
10. protocol-retest audit;
11. MS17 UNKNOWN audit;
12. UNPATCHED provenance audit;
13. overclaim-search results;
14. project QA;
15. clean git status.

Final state:

`X7D1_CASEB_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7E.
Do not write Case C.
Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
