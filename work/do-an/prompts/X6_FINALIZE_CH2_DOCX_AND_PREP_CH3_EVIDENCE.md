# X6 PREP — FINALIZE CHAPTER 2 DOCX AND STAGE CHAPTER 3 EVIDENCE

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x6-ch3-evidence-prep`

## 0. Goal

This task has two deliverables only:

1. Create the final Word report for the approved Chapter 2.
2. Prepare the canonical evidence/data package required for Chapter 3.

Do **not** draft Chapter 3 prose yet.

Chapter 2 content is already user-approved and locked.

## 1. Repository and source of truth

Repository:
`wrust0608/word-ppt-auto`

Start from:

```bash
git fetch origin
git checkout feature/x6-ch3-evidence-prep
git pull --ff-only origin feature/x6-ch3-evidence-prep
git status --short
git rev-parse HEAD
```

Mandatory source files on `origin/main`:

1. `work/do-an/CHAPTER_2.md`
2. `work/do-an/X5_PRODUCT_ALIGNED_EXTERNAL_REVIEW_R2_FINAL.md`
3. `work/do-an/PROJECT_STATE.md`
4. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
5. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
6. `work/do-an/evidence/ALL_2026_10_06/CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
7. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md`
8. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_USE_POLICY_ALL_ZIP.md`
9. `work/do-an/evidence/ALL_2026_10_06/CANONICAL_NMAP_TEXT_OUTPUTS.md`
10. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`

Locked approved Chapter 2 source:
`work/do-an/CHAPTER_2.md` on `origin/main`.

Do not rewrite its technical content.

## 2. Deliverable A — final Chapter 2 DOCX

Create:

`work/do-an/output/CHAPTER_2_FINAL.docx`

This must be a real final-use Word file, not a rough export.

### 2.1 Page setup

Use:
- paper: A4;
- orientation: portrait;
- one-sided layout;
- top margin: 3.5 cm;
- bottom margin: 3.0 cm;
- left margin: 3.5 cm;
- right margin: 2.0 cm;
- body font: Times New Roman 13 pt;
- line spacing: 1.5;
- body alignment: justified;
- first-line paragraph indent: approximately 1.0–1.27 cm where appropriate;
- no artificial blank paragraphs to force layout.

Use proper Word styles:
- Heading 1 for chapter title;
- Heading 2 for 2.1–2.7;
- Heading 3 for 2.x.x;
- Normal for body;
- dedicated code style for commands;
- dedicated caption styles for figures and tables.

Do not flatten headings into plain bold text.

### 2.2 Heading presentation

Chapter title:
`CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM`

Keep the approved 7 H2 / 20 H3 exactly.

Do not add new numbered sections.

### 2.3 Tables

Preserve the four Chapter 2 tables:
- Bảng 2.1
- Bảng 2.2
- Bảng 2.3
- Bảng 2.4

Rules:
- table title above table;
- keep numbering exactly by chapter;
- header row bold;
- repeat header row on multipage tables;
- no clipped command strings;
- do not shrink the entire document font to make wide tables fit;
- commands may use a smaller monospace font only inside command cells;
- allow manual line wrapping inside command cells if needed without changing command meaning.

### 2.4 Figures

The Markdown contains two Mermaid diagrams.

In the DOCX, do not leave raw Mermaid code.

Create clean rendered figures for:
- Hình 2.1 — baseline topology;
- Hình 2.2 — pfSense Transparent Bridge topology.

Requirements:
- high-resolution or vector-quality;
- Vietnamese labels;
- readable at normal page zoom;
- no decorative styling;
- no invented components;
- exact IP/interface/topology facts from approved Chapter 2;
- figure caption below figure;
- center figure and caption consistently.

Do not use ZIP folder structure as visual architecture.

### 2.5 Commands/code

Use a monospace font such as Consolas/Courier New for command blocks.

Keep exact commands from the approved Chapter 2.

Do not:
- add `-Pn`;
- add operator `--privileged`;
- alter output filenames;
- rewrite Case B/Case C commands.

### 2.6 Citations

Preserve IEEE citation markers `[1]...[11]` exactly as present.

Do not invent bibliography entries.

This file is the Chapter 2 module of a larger report; do not append a new standalone bibliography unless the project source explicitly requires it.

### 2.7 DOCX QA — mandatory

Before committing the DOCX:

1. render the DOCX to page images;
2. inspect **every page** at normal/100% zoom;
3. correct any:
   - clipped text;
   - table overflow;
   - broken code wrapping;
   - orphaned headings;
   - figure caption separation;
   - missing glyphs;
   - inconsistent margins;
   - broken page breaks;
   - accidental blank pages;
4. render again after every layout-sensitive correction.

Create a short QA record:

`work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`

It must record:
- final page count;
- render method;
- every page visually checked = yes/no;
- table overflow = pass/fail;
- figure readability = pass/fail;
- heading count = 7 H2 / 20 H3;
- content source hash/commit;
- final DOCX SHA-256.

Do not commit rendered PNGs/PDF unless explicitly needed for debugging. Remove temporary render artifacts before final commit.

## 3. Deliverable B — stage Chapter 3 evidence

The user has approved moving beyond Chapter 2. Now stage the actual evidence needed for Chapter 3 from the original `ALL(1).zip`.

### 3.1 Source package verification

Before extracting/copying any artifact:

- locate the original `ALL(1).zip` available in the project/workspace;
- compute SHA-256;
- it must equal:

`dc63f3ba5ed514f0c6b5e947474baca712c15a4c08c42b2228e421512cb04ff3`

If the archive cannot be found or the hash differs:
- do not substitute another archive;
- stop evidence-copy work;
- still complete the Chapter 2 DOCX;
- report the exact problem.

### 3.2 Evidence staging structure

Create a new neutral staging tree:

```text
work/do-an/chapter3/
  evidence/
    baseline/
    scenario1/
    scenario2/
    case_b/
    case_c/
  CHAPTER_3_EVIDENCE_INDEX.md
  CHAPTER_3_RESULT_MATRIX.md
  CHAPTER_3_FIGURE_PLAN.md
  CHAPTER_3_STRUCTURE_PROPOSAL.md
```

This staging tree is **not** the Chapter 3 heading structure.

Do not mirror the original ZIP directory tree.

Do not move or alter source artifacts; copy them byte-for-byte.

### 3.3 Evidence selection rules

Use the final R3 evidence locks and the canonical map.

Primary evidence to stage must cover:

#### Baseline
- final pre-demo audit;
- final snapshot verification;
- Windows local SMB/service state;
- Windows Firewall final scoped rule state;
- local MS17-010 patch baseline/mapping state;
- host-only network configuration;
- only the screenshots directly needed to show baseline facts in Chapter 3.

#### Scenario 1
Stage the final canonical B2–B6 raw Nmap triplets:
- `.nmap`
- `.xml`
- `.gnmap`

Also stage only screenshots that correspond to the final completed run and materially improve report readability.

#### Scenario 2
Stage final canonical NSE-SMB-01 through NSE-SMB-04 raw triplets.

Also stage final completed-run screenshots, if present and directly traceable.

#### Case B
Stage:
- local before screenshot/state;
- action screenshot/state;
- local after screenshot/state;
- final `smb-protocols` retest raw triplet;
- final `smb-vuln-ms17-010` retest raw triplet;
- any directly corresponding final screenshots.

#### Case C
Stage:
- bridge/interface configuration visuals;
- bridge filtering/tunable visual(s);
- configured block rule visual;
- rule-order visual;
- canonical port-scan raw triplet;
- canonical MS17-010 raw triplet;
- canonical Nmap port screenshot;
- canonical firewall-log screenshot;
- canonical MS17-010 screenshot;
- metadata needed to establish management/data-plane topology.

### 3.4 Excluded from main Chapter 3 result set

Do not place these into the main result folders:
- HostRepair;
- pre-repair Case C attempts;
- aborted/debug runs;
- MSI repair/install troubleshooting;
- old report DOCX files;
- summary prose that adds claims beyond raw/direct evidence.

If useful for audit history, list them in the evidence index as:
`PRESERVED / NOT USED AS MAIN RESULT`

Do not delete them from the original package.

### 3.5 Hash preservation

For every staged artifact:
- compute SHA-256;
- compare against the source-package manifest/canonical evidence map where available;
- byte identity must be preserved.

Create:
`work/do-an/chapter3/CHAPTER_3_EVIDENCE_SHA256.csv`

Columns:
- staged_path
- source_archive_path
- source_sha256
- staged_sha256
- match
- evidence_role

All primary artifacts must have `match=TRUE`.

## 4. Chapter 3 evidence index

Create:
`work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md`

For each result unit include:

- result unit ID;
- experiment phase;
- staged artifact(s);
- source artifact path;
- SHA-256;
- direct observation available;
- allowed conclusion;
- forbidden inference;
- suggested figure/table use;
- evidence strength: direct raw / direct screenshot / local state / metadata-supported.

Keep internal evidence IDs in this file; do not expose them as report prose.

## 5. Chapter 3 result matrix

Create:
`work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md`

This is an internal factual matrix, not narrative prose.

Rows must include at minimum:

### Baseline
- Kali/Windows addresses;
- baseline network state;
- LanmanServer;
- local 139/445 listening;
- SMB1/SMB2;
- Windows Firewall scoped rule;
- local patch state;
- snapshot.

### Scenario 1
- B2 host discovery;
- B3 target alive;
- B4 ports;
- B5 service/version;
- B6 dialect/signing/capabilities;
- `smb-os-discovery` no usable output.

### Scenario 2
- NSE-SMB-01;
- NSE-SMB-02;
- NSE-SMB-03;
- NSE-SMB-04 = UNKNOWN / NO USABLE SCRIPT RESULT.

### Case B
- before state;
- action;
- after local state;
- protocol retest;
- MS17-010 retest;
- patch remains UNPATCHED.

### Case C
- topology/configuration;
- configured rule;
- port retest;
- pfSense blocked matching SMB SYN observation;
- MS17-010 retest;
- local Windows patch state remains UNPATCHED.

Each row must include:
- factual observation;
- source artifact;
- allowed interpretation;
- prohibited interpretation.

Do not resolve the known Case C exact rule-label conflict.

## 6. Chapter 3 figure plan

Create:
`work/do-an/chapter3/CHAPTER_3_FIGURE_PLAN.md`

Plan only the strongest figures.

Avoid screenshot spam.

For each proposed figure specify:
- proposed figure number;
- purpose;
- source artifact;
- crop recommendation if needed;
- what the caption should say;
- what conclusion the figure supports;
- whether a raw table is better than a screenshot.

Prefer:
- raw result summarized in tables;
- screenshots only when they add visible proof that text/raw output cannot communicate as clearly.

## 7. Chapter 3 structure proposal

Create:
`work/do-an/chapter3/CHAPTER_3_STRUCTURE_PROPOSAL.md`

Do not write prose.

Propose a simple results-oriented structure that maps 1:1 to Chapter 2 methods.

Default target:

```text
CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

3.1. Trạng thái baseline trước đo đạc
3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
3.4. Kết quả Case B — Vô hiệu hóa SMBv1
3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
3.6. So sánh kết quả thực nghiệm
3.7. Tổng kết chương
```

For each H2, provide only:
- purpose;
- evidence set;
- planned tables/figures;
- boundary with Chapter 4.

Do not draft paragraphs.

### Chapter 3 / Chapter 4 boundary

Chapter 3:
- measured result;
- direct interpretation;
- factual before/after comparison.

Chapter 4:
- security impact;
- CIA/risk;
- broader evaluation;
- recommendations;
- residual risk;
- patching strategy.

Do not move Chapter 4 discussion into Chapter 3.

## 8. Critical truth locks

Preserve all of these:

- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- `FILTERED != PATCHED`
- `SMBv1 disabled != PATCHED`
- local patch state and remote NSE signal are independent;
- `.56.100` remains unidentified;
- cross-system clocks are not a unified wall clock;
- Case C firewall log does not independently prove exact named-rule attribution;
- no canonical exploitation/RCE/Meterpreter/reverse shell occurred;
- Case A patching is not a completed experiment.

## 9. Files allowed to modify/create

Allowed:
- `work/do-an/output/CHAPTER_2_FINAL.docx`
- `work/do-an/output/CHAPTER_2_FINAL_DOCX_QA.md`
- `work/do-an/chapter3/**`

Do not modify:
- `work/do-an/CHAPTER_2.md`
- evidence lock files;
- Truth Matrix;
- Source Ledger;
- Chapter 4;
- any source ZIP content.

Do not create `CHAPTER_3.md` yet.

## 10. QA

Before commit:

### Chapter 2 DOCX
- verify DOCX opens;
- render every page;
- visually inspect every page;
- verify figures/tables/captions;
- verify no raw Mermaid remains;
- verify no content drift from locked `CHAPTER_2.md`.

### Chapter 3 staging
- verify source ZIP SHA-256;
- verify all staged primary artifacts byte-match source SHA-256;
- verify no troubleshooting file is mislabeled primary;
- verify Case C conflict remains documented;
- verify no Chapter 3 prose was written.

Run project QA:
```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

## 11. Git

Commit on:
`feature/x6-ch3-evidence-prep`

Suggested commit:
`prep(ch3): finalize chapter 2 docx and stage canonical evidence`

Push remote.

Do not merge main.

## 12. Handoff

Return exactly:

1. branch;
2. local SHA;
3. remote SHA;
4. `CHAPTER_2_FINAL.docx` path;
5. DOCX SHA-256;
6. DOCX page count;
7. visual QA result;
8. source ZIP SHA-256;
9. number of staged primary evidence files;
10. number of preserved-but-not-main-result artifacts referenced;
11. evidence SHA mismatch count;
12. list of Chapter 3 staging files created;
13. proposed Chapter 3 H2 structure;
14. QA results;
15. clean git status.

Final state:
`X6_EVIDENCE_PREP_READY_FOR_EXTERNAL_REVIEW`

Stop.

Do not self-declare Chapter 3 PASS.
Do not draft Chapter 3 prose.
