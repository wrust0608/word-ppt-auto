# X7A1 — DRAFT CHAPTER 3 SECTION 3.1 BASELINE

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7a1-ch3-baseline-draft`

## 0. Objective

Write the first review draft of Chapter 3 Section 3.1 only, using the user-approved X7A0 presentation plan.

This phase must produce a student-facing results section with:
- 2 locked H3 subsections;
- 2 locked tables;
- 3 locked evidence figures;
- bounded technical interpretation;
- no Scenario 1/2 result leakage;
- no Chapter 4 discussion.

Do not create a final DOCX.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7a1-ch3-baseline-draft
git pull --ff-only origin feature/x7a1-ch3-baseline-draft
git status --short
git rev-parse HEAD
```

Record the branch HEAD before editing.

The branch must descend from the current `feature/ch3-integration` state that contains the user-approved X7A0 plan.

If the approved artifacts or numbering lock are missing, STOP.

## 2. Mandatory read order

Read:

1. `work/do-an/PROJECT_STATE.md`
2. `work/do-an/CHAPTER_3_CONTRACT.md`
3. `work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
4. `work/do-an/X7A0_BASELINE_PLAN_USER_APPROVAL_LOCK.md`
5. `work/do-an/X7A0_BASELINE_PLAN_EXTERNAL_REVIEW_R2_FINAL.md`
6. `work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`
8. `work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md`
9. `work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`
10. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — baseline only
11. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — baseline only
12. `work/do-an/EVIDENCE_REGISTER.md`
13. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
14. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
15. `work/do-an/AUTHOR_VOICE.md`
16. approved `work/do-an/CHAPTER_2.md` — baseline/setup portions only.

Do not follow superseded monolithic X7 constraints/prompt.

## 3. Files allowed to create

Create:

- `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- `work/do-an/CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_31_BASELINE_CROP_MANIFEST_R1.md`

Derived presentation images may be created only under:

`work/do-an/chapter3/presentation/3_1/`

Use these filenames:

- `Hinh_3_1_Network_SMB.png`
- `Hinh_3_2_Firewall.png`
- `Hinh_3_3_SrvSys_Hotfix.png`

Do not modify source evidence under:
`work/do-an/chapter3/evidence/**`

Do not modify the approved X7A0 planning artifacts.

## 4. Locked structure

The draft fragment must contain exactly:

```text
## 3.1. Trạng thái baseline trước đo đạc

### 3.1.1. Trạng thái mạng và dịch vụ SMB

### 3.1.2. Trạng thái bản vá và mốc phục hồi
```

No additional numbered H3.

Use one short opening paragraph immediately under 3.1.

## 5. Writing objective

The section should answer, in student-report language:

1. What was the actual network/SMB state before scanning?
2. What Windows Firewall state was verified?
3. What local patch state was established?
4. What restore point existed before measurements?

The reader should not need to understand repository QA terminology.

## 6. Locked Table 3.1

Title:

**Bảng 3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc**

Columns:

`Hạng mục | Giá trị ghi nhận | Ghi chú`

Use the approved X7A0 rows and boundaries.

Required content includes:
- Kali `192.168.56.10/24`;
- Windows `192.168.56.20/24`;
- local route state / no default route;
- one Host-Only NIC per VM;
- no NAT/Bridged NIC in final baseline;
- LanmanServer = Running / Automatic;
- FS-SMB1 = Installed;
- EnableSMB1Protocol=True;
- EnableSMB2Protocol=True;
- local signing flags False/False;
- TCP 139/445 listening locally;
- three Windows Firewall profiles enabled;
- default File and Printer Sharing group disabled;
- custom inbound TCP 139/445 allow rule scoped to source .56.10.

Do not include:
- filenames;
- Evidence IDs;
- Claim IDs;
- ICMP result;
- risk/effectiveness judgment.

Do not call local listeners remote OPEN.

## 7. Locked Figure 3.1

Source:
`work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png`

Presentation path:
`work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`

Caption:

**Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm**

Before the figure:
- tell the reader that the image shows the consolidated local Windows baseline.

After the figure:
- note only visible/local facts;
- keep local listener state distinct from remote port reachability.

Do not use the word `kiểm toán` in student-facing prose.

## 8. Locked Figure 3.2

Source:
`work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`

Presentation path:
`work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png`

Caption:

**Hình 3.2. Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux**

Allowed direct observations:
- custom rule enabled;
- inbound;
- allow;
- TCP;
- local ports 139/445;
- RemoteAddress .56.10;
- Domain/Private/Public profiles enabled;
- default File and Printer Sharing group observed disabled.

Do not claim:
- all other IPs are definitely blocked by every possible rule;
- this configuration makes the machine safe.

## 9. Locked Table 3.2

Title:

**Bảng 3.2. Trạng thái bản vá và mốc phục hồi**

Columns:

`Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn`

Required:
- display FileVersion String `6.3.9600.16384`;
- numeric srv.sys `6.3.9600.16421`;
- Microsoft minimum updated `6.3.9600.18604`;
- KB4012213 / KB4012216;
- observed six-hotfix inventory;
- bounded wording that the observed inventory does not show the relevant direct/mapped update;
- local classification `UNPATCHED`;
- `Before Demo` snapshot for both VMs.

Use the same approved citation numbering already used for these Microsoft claims in Chapter 2.
Do not invent new numeric references.

## 10. Locked Figure 3.3

Source:
`work/do-an/chapter3/evidence/baseline/Windows_MS17010_02_Hotfix.png`

Presentation path:
`work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`

Caption:

**Hình 3.3. Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2**

After the figure, explicitly distinguish:
- display version;
- numeric version;
- observed hotfix inventory;
- external Microsoft threshold.

`UNPATCHED` is a combined local classification.

Do not say:
- the screenshot alone proves UNPATCHED;
- local UNPATCHED proves remote exploitability;
- NSE remotely confirmed the vulnerability.

## 11. Derived presentation image rules

For each of the three locked figures:

1. determine source dimensions programmatically;
2. inspect the source image;
3. create a derived crop only if it materially improves print readability;
4. otherwise create a byte-identical or visually identical presentation copy;
5. never alter source evidence.

Create:
`CH3_31_BASELINE_CROP_MANIFEST_R1.md`

For each image record:
- source path;
- source SHA-256;
- source dimensions;
- derived path;
- derived SHA-256;
- mode = CROP or COPY;
- exact crop rectangle if CROP;
- visual content preserved;
- UI removed;
- reason;
- reviewer boundary retained.

Visually inspect all three derived images after creation.

If a crop hides any value needed for the caption or paragraph, redo it.

Do not annotate, recolor, sharpen, regenerate or add graphical marks.

## 12. Prose style

Use academic Vietnamese appropriate for an undergraduate Information Security report.

Use:
- direct, compact paragraphs;
- neutral third-person voice;
- observed values;
- simple transitions.

Avoid:
- audit/governance vocabulary;
- evidence IDs;
- canonical / gate / truth matrix;
- internal filenames;
- self-praise;
- “Single Source of Truth”;
- repetitive “có thể thấy rằng”, “qua đó”, “như vậy” patterns.

At first meaningful use, write:
`trạng thái ban đầu (baseline)`.

Target length for Section 3.1:
approximately **1,000–1,500 words**, including table commentary but excluding table cell text/captions if the counting script can distinguish them.

Do not pad to hit a quota.

## 13. Results boundary

Allowed:
- verified baseline state;
- local patch classification;
- short explanation of why the baseline matters for later measurements.

Not allowed:
- Scenario 1 measured results;
- Scenario 2 measured results;
- Case B;
- Case C;
- risk rating;
- CIA analysis;
- recommendation;
- “best solution”;
- broader mitigation evaluation.

End 3.1 with one short transition only:
the next section presents the remote SMB survey results from Kali Linux.

Do not include Scenario 1 commands or results in the transition.

## 14. Technical wording locks

Preserve:

- one Host-Only NIC per VM;
- no NAT/Bridged NIC in final baseline;
- no default route;
- do not call the lab completely isolated;
- Windows IP is observed as `192.168.56.20/24`; do not invent “static” unless directly evidenced;
- LanmanServer = Running / Automatic; do not say “working normally”;
- local SMB enable flags do not establish remote dialect negotiation;
- local signing flags do not establish remote signing result;
- TCP 139/445 listening locally != remote OPEN;
- custom firewall rule scope != proof that every other source is blocked;
- observed hotfix inventory wording must remain bounded;
- snapshot = defined restore point, not perfect reproducibility.

## 15. Claim-map discipline

The approved internal claim map remains:
`BASE-C01 ... BASE-C16`.

Do not expose those IDs in the draft.

In the self-review create a paragraph/table-to-claim audit:
- draft location;
- claims used;
- whether wording stays within approved Allowed wording;
- whether any new factual claim was introduced.

Any new factual claim not in BASE-C01..C16 is a blocker unless it is purely transitional/non-technical.

## 16. Citation discipline

Experimental observations do not need external citations.

Microsoft threshold/KB semantics must reuse the exact citation markers already used for those same claims in approved Chapter 2.

Do not create a new reference list.

Do not renumber citations in this phase.

## 17. Self-review

Create:
`work/do-an/CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`

Include:
1. word count;
2. heading audit;
3. table count = 2;
4. figure count = 3;
5. image path existence;
6. crop-manifest audit;
7. paragraph-to-claim map;
8. patch-state boundary audit;
9. local-vs-remote boundary audit;
10. Chapter 3/4 boundary audit;
11. citation audit;
12. author-voice audit;
13. forbidden-term search;
14. unresolved concerns.

Do not self-declare PASS.

Final self-review state:
`X7A1_CH3_31_BASELINE_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

## 18. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_31_BASELINE_DRAFT_R1.md
uv run python scripts/audit_ieee_citations.py work/do-an/CH3_31_BASELINE_DRAFT_R1.md
git diff --check
```

Verify:
- exactly 1 H2 + 2 H3 in the section fragment;
- exactly 2 report tables;
- exactly 3 image embeds;
- all 3 presentation images exist;
- all 3 source evidence files unchanged;
- no internal Evidence/Claim IDs in draft;
- no `canonical`, `truth matrix`, `gate`, `Single Source of Truth`;
- no absolute isolation wording;
- no ICMP-firewall causality;
- no remote OPEN claim;
- no Scenario 1/2 result leakage;
- no Chapter 4 recommendation/risk discussion.

## 19. Git

Commit:

`draft(ch3): write baseline section 3.1 R1`

Push:

`feature/x7a1-ch3-baseline-draft`

Do not merge.

## 20. Handoff

Return:
1. branch;
2. starting SHA;
3. local SHA;
4. remote SHA;
5. modified/created file list;
6. word count;
7. H2/H3 count;
8. table count;
9. figure count;
10. crop-manifest summary;
11. paragraph-to-claim audit summary;
12. patch-state boundary audit;
13. local/remote boundary audit;
14. citation audit;
15. QA results;
16. clean git status.

Final state:
`X7A1_CH3_31_BASELINE_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`

Stop.

Do not open X7B.
Do not write Section 3.2.
Do not create final DOCX.
