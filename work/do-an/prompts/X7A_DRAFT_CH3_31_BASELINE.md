# X7A — DRAFT CHAPTER 3 SECTION 3.1 BASELINE ONLY

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x7a-ch3-baseline`

## 0. Objective

Draft only Section 3.1 of Chapter 3:

`3.1. Trạng thái baseline trước đo đạc`

This phase exists to establish the experimental starting state clearly before any scan result is presented.

Do not draft any later Chapter 3 section.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7a-ch3-baseline
git pull --ff-only origin feature/x7a-ch3-baseline
git status --short
git rev-parse HEAD
```

## 2. Read order

Read:

1. `origin/main:work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
2. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — baseline rows only
3. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — baseline section only
4. `origin/main:work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
5. `origin/main:work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
6. `origin/main:work/do-an/SOURCE_LEDGER.md`
7. `origin/main:work/do-an/AUTHOR_VOICE.md`
8. `origin/main:work/do-an/CHAPTER_2.md` — only 2.1 and 2.2.

Do not inspect Scenario 1/2 or Case B/C evidence unless needed to verify that it is not being used.

## 3. Allowed evidence family

Use only baseline/pre-demo evidence, especially:

- `chapter3/evidence/baseline/Final_PreDemo_Audit.txt`
- `chapter3/evidence/baseline/Before_Demo_Snapshots.txt`
- `chapter3/evidence/baseline/MS17-010_Official_Mapping.txt`
- `chapter3/evidence/baseline/Windows_FirewallPrep_Final.txt`
- `chapter3/evidence/baseline/VirtualBox_HostOnly_Config.txt`
- baseline Windows screenshots staged in `chapter3/evidence/baseline/`

No Scenario 1/2 raw files.
No Case B/C evidence.

## 4. Draft structure

Create:

# 3.1. Trạng thái baseline trước đo đạc

## 3.1.1. Trạng thái mạng và dịch vụ SMB

## 3.1.2. Trạng thái bản vá và mốc phục hồi

Do not add another H3 in X7A.

## 5. Content requirements — 3.1.1

Explain the measured starting state concisely:

- Kali `192.168.56.10/24`;
- Windows `192.168.56.20/24`;
- baseline Host-Only;
- no NAT/Bridged NIC for the two VMs in final pre-demo state;
- no default route;
- basic reachability;
- LanmanServer Running / Automatic;
- local TCP 139/445 listening;
- SMB1=True;
- SMB2=True;
- Windows Firewall enabled;
- scoped custom rule for 139/445 from .56.10;
- default File and Printer Sharing group not broadly enabled.

Do not call the environment “cô lập hoàn toàn”.

Create one table:

**Bảng 3.1. Trạng thái baseline của môi trường trước đo đạc**

Recommended columns:
- Thành phần / tham số
- Giá trị ghi nhận
- Ý nghĩa đối với phép đo

Keep it compact.

## 6. Content requirements — 3.1.2

Explain patch state as a **local baseline fact**:

- FileVersion String `6.3.9600.16384`;
- numeric `srv.sys 6.3.9600.16421`;
- Microsoft minimum updated `6.3.9600.18604`;
- observed hotfix inventory does not show KB4012213 / KB4012216 or a mapped superseding update;
- local classification = UNPATCHED;
- snapshot `Before Demo` exists after final setup.

Must explicitly distinguish:
- screenshot display version;
- numeric local version used for comparison;
- official Microsoft mapping.

Do not claim complete historical knowledge of all updates ever installed.

## 7. Figure-selection task

This phase is deliberately evidence-rich.

Create:

`work/do-an/CH3_31_BASELINE_FIGURE_SELECTION.md`

Inspect all baseline screenshots available in the staged baseline directory.

For each candidate screenshot, record:
- filename;
- what it directly shows;
- whether it adds unique information;
- whether a table already communicates the same fact;
- KEEP / OPTIONAL / DROP;
- proposed caption if KEEP;
- whether cropping would improve legibility.

Do not modify source images.

For the draft itself, select **2 or 3 images maximum**.

At least one selected image must support patch-state evidence.

Strong candidates include:
- `Windows_MS17010_01_SrvSysVersion.png`
- `Windows_FirewallPrep_04_Scope.png`
- one SMB/service/config screenshot if it adds information not already clear in Bảng 3.1.

Do not force all three if two are enough.

## 8. Figure placement

Every selected figure must:
- be introduced in the preceding paragraph;
- use a relative Markdown path;
- have a caption that states only what is visibly shown;
- be followed by a short interpretation paragraph.

Do not put “UNPATCHED” directly in the srv.sys screenshot caption unless the figure itself shows the complete basis for that classification.

## 9. Writing style

This should read like a student results section, not an audit report.

Avoid:
- canonical;
- evidence layer;
- gate;
- truth matrix;
- source-of-truth;
- ENV-* IDs;
- PRIMARY_* labels;
- governance language.

Use direct academic Vietnamese.

Do not repeat Chapter 2 setup instructions.
Report the **verified starting state**, not installation steps.

## 10. Citations

Experimental observations themselves are project data.

Use an external citation only for:
- Microsoft KB mapping;
- minimum updated srv.sys version.

Use only verified Microsoft source already recorded in SOURCE_LEDGER.

Do not invent bibliography numbering.

## 11. Forbidden drift

Do not include:
- Scenario 1 results;
- Scenario 2 results;
- Case B;
- Case C;
- Chapter 4 risk/recommendation;
- claims about exploitability.

Do not identify .56.100; it is not relevant to baseline section anyway.

## 12. Output files

Create only:

- `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- `work/do-an/CH3_31_BASELINE_FIGURE_SELECTION.md`
- `work/do-an/CH3_31_BASELINE_SELF_REVIEW.md`

## 13. Self-review

Self-review must report:

- H2/H3 count;
- word count;
- table count;
- selected figure count;
- list of all baseline screenshot candidates reviewed;
- selected figures and rationale;
- patch-state wording audit;
- Chapter 2 repetition audit;
- Chapter 4 leakage audit;
- author-voice audit;
- unresolved concerns.

Do not self-declare PASS.

Final state:
`X7A_CH3_31_BASELINE_R1_READY_FOR_EXTERNAL_REVIEW`

## 14. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_31_BASELINE_DRAFT_R1.md
uv run python scripts/audit_ieee_citations.py work/do-an/CH3_31_BASELINE_DRAFT_R1.md
git diff --check
```

Verify every embedded image path exists.

## 15. Git

Commit:

`draft(ch3): write baseline results section R1`

Push:

`feature/x7a-ch3-baseline`

Do not merge.

Stop after handoff.
Do not start X7B.
