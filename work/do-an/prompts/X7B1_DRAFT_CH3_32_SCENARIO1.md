# X7B1 — DRAFT CHAPTER 3 SECTION 3.2 SCENARIO 1

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7b1-ch3-scenario1-draft`  
Approved integration base: `e56458a21f8caffe777113d1e073e083810d4af7`

## 0. Objective

Write the first review draft of Chapter 3 Section 3.2 only:

`3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`

Use the user-approved X7B0 Scenario 1 Evidence & Presentation Plan.

This phase must produce a student-facing experimental-results section with:

- exactly 2 locked H3 subsections;
- exactly 1 locked results table: Bảng 3.3;
- exactly 2 locked evidence figures: Hình 3.4 and Hình 3.5;
- approved B5/B6 derived presentation crops with full SHA/crop traceability;
- bounded interpretation of B2–B6;
- no Scenario 2 result leakage;
- no Case B/Case C leakage;
- no Chapter 4 risk/recommendation discussion.

Do not create a final DOCX.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/x7b1-ch3-scenario1-draft
git pull --ff-only origin feature/x7b1-ch3-scenario1-draft
git status --short
git rev-parse HEAD
git merge-base --is-ancestor e56458a21f8caffe777113d1e073e083810d4af7 HEAD
```

The last command must succeed.

Record the starting HEAD before editing.

If the branch does not descend from the approved integration commit or the approved X7B0 artifacts/numbering lock are missing, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/X7B0_SCENARIO1_PLAN_USER_APPROVAL_LOCK.md`
5. `work/do-an/X7B0_SCENARIO1_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`
8. `work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`
9. `work/do-an/CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
10. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` — Scenario 1 rows only
11. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — Scenario 1 only
12. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — Scenario 1 only
13. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
14. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
15. `work/do-an/AUTHOR_VOICE.md`
16. approved `work/do-an/CHAPTER_2.md` — Scenario 1 method only
17. approved `work/do-an/CH3_31_BASELINE_DRAFT_R1.md` — continuity only
18. all Scenario 1 raw evidence under:
    `work/do-an/chapter3/evidence/scenario1/`

Do not follow:
- superseded monolithic X7 instructions;
- historical Chapter 3 numbering;
- old report prose as experimental truth;
- Scenario 1 manifest overclaims when they conflict with direct raw evidence or final review locks.

Evidence precedence:
`direct raw/local/visual > metadata/manifest > historical/support > old report prose`.

## 3. Files allowed to create

Create:

- `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
- `work/do-an/CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_32_SCENARIO1_CROP_MANIFEST_R1.md`

Create derived presentation images only under:

`work/do-an/chapter3/presentation/3_2/`

Use exactly:

- `Hinh_3_4_SMB_Version.png`
- `Hinh_3_5_SMB_NSE.png`

Do not modify source evidence under:
`work/do-an/chapter3/evidence/**`

Do not modify approved X7B0 planning artifacts.

Do not modify Section 3.1.

## 4. Locked section structure

The draft fragment must contain exactly:

```text
## 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB

### 3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB

### 3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB
```

No additional numbered H3/H4.

Use one short opening paragraph under 3.2 that explains the result sequence, not the method in command-by-command detail.

The narrative should read as:

`host discovery -> target confirmation -> remote port state -> service/version fingerprint -> SMB protocol profile`

not as a shell-command transcript.

## 5. Core writing objective

A lecturer reading only Section 3.2 should be able to answer:

1. Which hosts were observed on the lab segment?
2. Which system was then examined as the target?
3. What was the remote state of TCP 139/445 from Kali?
4. How precise was the Nmap service/version fingerprint?
5. Which SMB dialects, capabilities and signing state were observed?
6. What did `smb-os-discovery` fail to provide?
7. Why does Scenario 1 still not establish an MS17-010 verdict?

The prose must make the demo visible without requiring repository terminology.

## 6. Locked Bảng 3.3

Title:

**Bảng 3.3. Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux**

Columns:

`Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`

Use the approved plan as the source.

Required rows:

### B2 — Phát hiện trạm mạng

Phép đo:
- ARP host discovery over `192.168.56.0/24`.

Observed:
- `192.168.56.1`
- `192.168.56.10`
- `192.168.56.20`
- `192.168.56.100`
all observed up.

Boundary:
- `.56.100 = UNKNOWN identity`.
- do not identify .56.100 from MAC, metadata, historical text or later topology.

### B3 — Kiểm tra mục tiêu trực tuyến

Observed:
- `192.168.56.20` = `up`.

Allowed interpretation:
- confirms the target was online before subsequent port scans.

Do not state:
- “sẵn sàng tiếp nhận kết nối”;
- service availability;
- open port state;
- workload health.

Do not include the exact `0.00034 s` latency in the public table.

### B4 — Khảo sát cổng dịch vụ SMB

Observed from Kali:
- `139/tcp OPEN`
- `445/tcp OPEN`
- response reason `syn-ack`, TTL 128.

Allowed interpretation:
- from the Kali vantage point, TCP 139/445 were reachable/open and returned SYN-ACK.

Do not state:
- Windows Firewall “proved” the traffic path;
- SMB vulnerability;
- authenticated file-sharing capability;
- `445 OPEN = vulnerable`.

### B5 — Nhận diện dịch vụ/phiên bản

Observed:
- TCP 139: `Microsoft Windows netbios-ssn`
- TCP 445: `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`
- Service Info includes Windows/CPE.

Locked interpretation:
- remote fingerprint range only:
  `Microsoft Windows Server 2008 R2–2012`.

Never state that B5 remotely proves exact Windows Server 2012 R2.

If exact Windows Server 2012 R2 is mentioned for lab continuity, explicitly attribute it to the controlled baseline/local lab context, not B5.

### B6 — SMB NSE profile

Observed dialects:
- `NT LM 0.12 (SMBv1)`
- `2.0.2`
- `2.1`
- `3.0`
- `3.0.2`

Observed signing:
- `Message signing enabled but not required`.

Observed capabilities:
- 2.0.2: Distributed File System
- 2.1: Distributed File System, Leasing, Multi-credit operations
- 3.0: Distributed File System, Leasing, Multi-credit operations
- 3.0.2: Distributed File System, Leasing, Multi-credit operations

Observed `smb-os-discovery`:
- **no usable output**.

Boundary:
- do not invent a cause for no usable output;
- do not call absence of output safe/failed/unsupported unless direct evidence says so;
- do not convert SMBv1 presence into MS17-010 confirmation.

## 7. Locked figure decision

Use exactly two report figures.

### Hình 3.4

Source:
`work/do-an/chapter3/evidence/scenario1/Scenario1_B5_SMB_Version.png`

Derived path:
`work/do-an/chapter3/presentation/3_2/Hinh_3_4_SMB_Version.png`

Caption:

**Hình 3.4. Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap**

Approved provisional crop:
- source dimensions: 1280 × 800
- rectangle:
  `x=0, y=24, width=1280, height=310`

Must preserve:
- relevant Nmap command line;
- PORT/STATE/SERVICE/VERSION block;
- B5 fingerprint range;
- Service Info;
- enough terminal context to remain recognizable as direct Nmap output.

Do not claim the figure proves exact Windows Server 2012 R2.

### Hình 3.5

Source:
`work/do-an/chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png`

Derived path:
`work/do-an/chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png`

Caption:

**Hình 3.5. Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng tập kịch bản Nmap NSE**

Approved provisional crop:
- source dimensions: 1280 × 800
- rectangle:
  `x=0, y=24, width=1280, height=710`

Must preserve:
- full relevant command line;
- `smb-protocols`;
- `smb2-capabilities`;
- `smb2-security-mode`;
- normal end-of-scan context.

Important:
The absence of an `smb-os-discovery` result block is interpreted only together with the fact that the command line visibly includes `smb-os-discovery`.

Do not add annotations, arrows, highlights, recoloring, sharpening or generated text.

## 8. Crop implementation and manifest

Create the two derived crops using the approved rectangles.

Before cropping:
1. calculate source SHA-256;
2. verify source dimensions are exactly 1280 × 800;
3. if dimensions differ, STOP.

After cropping:
1. calculate derived SHA-256;
2. verify derived dimensions;
3. visually inspect both images;
4. confirm all required evidence is readable;
5. confirm no meaningful line is cut off.

Create:

`work/do-an/CH3_32_SCENARIO1_CROP_MANIFEST_R1.md`

For each figure record:
- source path;
- source SHA-256;
- source dimensions;
- derived path;
- derived SHA-256;
- mode = CROP;
- exact rectangle;
- derived dimensions;
- content preserved;
- UI removed;
- reason;
- interpretation boundary preserved.

If an approved rectangle unexpectedly cuts required text, do not silently change it. Record the issue and STOP for reviewer decision.

## 9. Figure placement in prose

### Before Hình 3.4

Lead the reader to observe:
- the service/version result;
- especially the fact that Nmap returns a range rather than an exact OS release.

### After Hình 3.4

State:
- what B5 actually recorded;
- the precision limit of the fingerprint.

Do not repeat the entire table row.

### Before Hình 3.5

Lead the reader to observe:
- dialect list;
- capabilities;
- signing state.

### After Hình 3.5

State:
- the directly observed SMB profile;
- `smb-os-discovery` returned no usable output;
- this does not establish MS17-010.

Do not turn the paragraph into a bullet-by-bullet restatement of the screenshot.

## 10. B2/B3 narrative discipline

B2 and B3 belong in 3.2.1.

B3 is a short continuity-confirmation step.

Do not:
- give B3 its own paragraph of disproportionate length;
- create a separate B3 figure;
- use latency as an analytical result;
- claim B3 proves SMB is available.

A natural flow is:

B2 identifies the observed hosts -> target .56.20 is selected based on controlled lab context -> B3 confirms it remains up -> B4 measures TCP 139/445.

Do not assign an identity to .56.100.

## 11. B5 narrative discipline

Use language such as:

- “Kết quả nhận diện dịch vụ/phiên bản của Nmap ghi nhận...”
- “Chuỗi nhận diện trên cổng 445 nằm trong khoảng...”

Avoid:
- “Nmap xác định chính xác...”
- “Nmap chứng minh hệ điều hành là Windows Server 2012 R2”
- unnecessary `probe/banner` mechanism language.

Do not use B5 as vulnerability evidence.

## 12. B6 narrative discipline

Use direct language:

- “Kịch bản `smb-protocols` ghi nhận...”
- “`smb2-security-mode` trả về...”
- “`smb2-capabilities` ghi nhận...”
- “`smb-os-discovery` không trả về khối dữ liệu khả dụng trong lần đo này.”

Do not:
- infer why `smb-os-discovery` has no result;
- call SMBv1 “vulnerable” merely because Nmap displays `[dangerous, but default]`;
- convert signing configuration into a complete security assessment;
- discuss mitigation/recommendation.

## 13. Section ending / transition to 3.3

End Section 3.2 with one short transition.

Required meaning:

- Scenario 1 establishes the remotely observed SMB exposure/profile;
- those observations do not themselves provide an MS17-010 verdict;
- Section 3.3 presents the dedicated NSE measurements related to that question.

Do not reveal Scenario 2 outcomes in the transition.

## 14. Student-facing prose style

Use academic Vietnamese appropriate for an undergraduate Information Security project.

Use:
- neutral third-person voice;
- direct observations;
- natural paragraph lengths;
- compact interpretation;
- terminology consistent with Chapters 2 and 3.1.

Prefer:
- “kết quả đo”;
- “ghi nhận”;
- “quan sát được”;
- “từ trạm Kali”;
- “trong lần đo này”.

Do not use in report prose:
- canonical;
- ground truth;
- truth matrix;
- gate;
- governance;
- Evidence ID;
- Claim ID;
- evidence layer;
- Single Source of Truth;
- internal file paths;
- audit-report terminology.

Do not mechanically repeat the same paragraph formula.

Target prose length:
approximately **1,000–1,500 words** for Section 3.2, excluding table cell text and captions where practical.

Do not pad to meet the target.

## 15. Chapter 3 / Chapter 4 boundary

Allowed:
- measured results;
- direct evidence;
- bounded interpretation;
- comparison between consecutive B2–B6 observations where useful.

Forbidden:
- risk rating;
- CIA discussion;
- exploitability judgment;
- “mức độ nguy hiểm” analysis;
- recommendation;
- residual risk;
- patch strategy;
- solution ranking;
- enterprise guidance.

Those belong to Chapter 4.

## 16. Global technical locks

Preserve exactly:

- `.56.100 = UNKNOWN identity`
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- local baseline state is independent from remote scan result
- B5 range != exact Windows Server 2012 R2 remote identification
- `smb-os-discovery = no usable output`
- Scenario 1 does not conclude MS17-010

No exploitation.
No RCE.
No reverse shell.
No Meterpreter.

## 17. Timebase discipline

Do not construct a cross-system chronology from displayed wall-clock timestamps.

Scenario 1 B2–B6 may be described in procedural step order because they are the defined experiment sequence, but do not use displayed timestamp comparisons to prove cross-layer timing relationships.

Do not introduce timestamp analysis unless directly necessary.

## 18. Claim-map discipline

Use the approved internal claim map:

`S1-C01 ... S1-C13`.

Do not expose those IDs in student prose.

In self-review, map each substantive paragraph/table/figure to the approved claims.

Any new factual result claim outside the approved map is a blocker unless it is purely transitional or editorial.

## 19. Citation discipline

Scenario 1 measured observations normally do not need external citations.

Do not create a new bibliography.

Do not invent IEEE numbering.

If an external technical definition is absolutely needed, first verify it exists in the current Source Ledger and reuse its stable source anchor; otherwise omit the unnecessary explanatory claim.

This section should primarily stand on direct experimental evidence.

## 20. Self-review

Create:

`work/do-an/CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1.md`

Include:

1. word count;
2. heading audit;
3. table count = 1;
4. figure count = 2;
5. presentation image existence;
6. crop-manifest audit;
7. paragraph/table/figure-to-claim audit;
8. B2/B3 redundancy audit;
9. .56.100 identity audit;
10. B4 remote-port wording audit;
11. B5 fingerprint-boundary audit;
12. B6 dialect/capability/signing audit;
13. `smb-os-discovery` no-output audit;
14. MS17-010 overclaim audit;
15. Chapter 3/4 boundary audit;
16. citation audit;
17. author-voice audit;
18. forbidden-term search;
19. later-section leakage audit;
20. unresolved concerns.

Do not self-declare external PASS.

Final state:

`X7B1_CH3_32_SCENARIO1_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

## 21. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md
git diff --check
```

If `scripts/audit_ieee_citations.py` accepts this standalone fragment without requiring a complete bibliography context, run it as well. If it is inapplicable to a citation-free fragment, record that explicitly rather than inventing citations.

Verify:

- exactly 1 H2 + 2 H3;
- exactly 1 report table;
- exactly 2 report image embeds;
- Bảng 3.3 only;
- Hình 3.4 and Hình 3.5 only;
- both presentation images exist;
- source evidence bytes unchanged;
- crop rectangles match approved plan;
- no `-Pn` invented;
- no wrong B4 MAC;
- no B3 latency in public result table;
- no .56.100 identity assignment;
- no exact OS inference from B5;
- no MS17-010 verdict;
- no Scenario 2 outcome;
- no Case B/C content;
- no Chapter 4 analysis;
- no internal Evidence/Claim IDs in student prose.

## 22. Git

Commit:

`draft(ch3): write scenario1 section 3.2 R1`

Push:

`feature/x7b1-ch3-scenario1-draft`

Do not merge.

## 23. Handoff

Return:

1. branch;
2. starting SHA;
3. local commit SHA;
4. remote commit SHA;
5. created/modified file list;
6. prose word count;
7. H2/H3 count;
8. table count;
9. figure count;
10. crop-manifest summary with source/derived SHA and rectangles;
11. paragraph-to-claim audit summary;
12. .56.100 audit;
13. B4 port wording audit;
14. B5 fingerprint audit;
15. B6 protocol/signing/capability audit;
16. `smb-os-discovery` audit;
17. MS17-010 boundary audit;
18. citation audit;
19. QA results;
20. clean git status.

Final state:

`X7B1_CH3_32_SCENARIO1_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not open X7C.
Do not write Section 3.3.
Do not write Chapter 4.
Do not create final DOCX.
