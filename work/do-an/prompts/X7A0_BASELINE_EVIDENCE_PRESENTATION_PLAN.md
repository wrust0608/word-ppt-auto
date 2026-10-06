# X7A0 — BASELINE EVIDENCE & PRESENTATION PLAN ONLY

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x7a0-ch3-baseline-plan`

## 0. Objective

Prepare the evidence and presentation plan for Chapter 3 Section 3.1 only.

Do **not** write Section 3.1 report prose yet.

This phase must answer:
- which baseline facts need to appear;
- which table shape explains them best;
- which screenshots are worth keeping;
- which screenshots are redundant;
- whether any wide image needs a derived crop;
- which report claims are supported by which direct evidence.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7a0-ch3-baseline-plan
git pull --ff-only origin feature/x7a0-ch3-baseline-plan
git status --short
git rev-parse HEAD
```

Confirm branch ancestry includes the current integration sync commit:
`7cf63376b40de6758730e10756f403e9a1603ad6`

Expected X7A0 branch synchronization commit at handoff:
`33a490c6573dd7a140545fb5fb29b384e443fe88`

If the branch does not contain `7cf63376b40de6758730e10756f403e9a1603ad6`, STOP.

## 2. Mandatory read order

Read:

1. `origin/main:work/do-an/PROJECT_STATE.md` — current summary only for current state.
2. `origin/main:work/do-an/G0_CH3_GOVERNANCE_RECONCILIATION_FINAL.md`
3. `origin/main:work/do-an/CHAPTER_3_CONTRACT.md`
4. `origin/main:work/do-an/CHAPTER_3_SECTIONED_AUTHORING_PLAN.md`
5. `origin/main:work/do-an/CHAPTER_3_SECTION_EVIDENCE_MAP.md`
6. `origin/main:work/do-an/CHAPTER_3_NUMBERING_LEDGER.md`
7. `origin/main:work/do-an/CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`
8. `work/do-an/chapter3/CHAPTER_3_RESULT_MATRIX.md` — baseline rows only.
9. `work/do-an/chapter3/CHAPTER_3_EVIDENCE_INDEX.md` — baseline section only.
10. `origin/main:work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
11. `origin/main:work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
12. `origin/main:work/do-an/SOURCE_LEDGER.md`
13. `origin/main:work/do-an/AUTHOR_VOICE.md`
14. `origin/main:work/do-an/CHAPTER_2.md` — only baseline/setup portions needed to avoid repetition.

Do not execute or follow:
- old detailed structures in OUTLINE.md;
- old CHAPTERS_2_4_EVIDENCE_MAP numbering;
- monolithic CHAPTER_3_AUTHORING_CONSTRAINTS quotas;
- X7 full-chapter prompt.

## 3. Evidence isolation

Inspect only baseline staged evidence under:

`work/do-an/chapter3/evidence/baseline/`

You may also read the official Microsoft source in SOURCE_LEDGER for patch threshold semantics.

Do not inspect/use:
- scenario1;
- scenario2;
- case_b;
- case_c;
except to confirm they are excluded from this phase.

## 4. Baseline facts that must be considered

Candidate report facts:

Network:
- Kali = `192.168.56.10/24`;
- Windows = `192.168.56.20/24`;
- one Host-Only NIC per VM in final pre-demo state;
- no NAT/Bridged NIC for those VMs;
- no default route in final pre-demo state;
- basic inter-VM reachability.

Windows/SMB:
- LanmanServer Running / Automatic;
- TCP 139/445 listening locally;
- SMB1=True;
- SMB2=True;
- FS-SMB1 installed;
- Windows Firewall enabled;
- custom inbound allow TCP 139/445 only from Kali .56.10;
- default File and Printer Sharing group not broadly enabled.

Patch:
- display FileVersion String = `6.3.9600.16384`;
- numeric srv.sys = `6.3.9600.16421`;
- Microsoft minimum updated = `6.3.9600.18604`;
- observed hotfix inventory does not show KB4012213 / KB4012216 or mapped superseding update;
- local classification = UNPATCHED.

Recovery:
- snapshot `Before Demo` exists after final setup.

## 5. Required output A — Figure selection

Create:

`work/do-an/CH3_31_BASELINE_FIGURE_SELECTION_R1.md`

Inspect **every staged PNG/JPG screenshot in baseline/**.

For every candidate image, record:

| File | Directly shows | Unique information? | Table can replace? | Legibility | Crop needed? | KEEP / OPTIONAL / DROP | Proposed use |
|---|---|---|---|---|---|---|---|

Rules:
- KEEP only if the screenshot proves something useful that prose/table alone would not show as convincingly.
- Do not keep multiple images that prove the same fact unless each adds distinct information.
- For wide screenshots, assess whether a presentation crop would materially improve readability.
- Do not create crops in X7A0; only propose them.
- At least one candidate must support patch-state presentation.
- Target is likely 2–3 final figures, but do not force a number before review.

At the end propose:
- recommended final figure set;
- tentative figure numbering starting from Hình 3.1;
- rejected/redundant images and reason.

## 6. Required output B — Baseline table/presentation plan

Create:

`work/do-an/CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`

Design the presentation of 3.1 without writing report paragraphs.

Include:

### Proposed subsection structure
Recommend H3 structure for 3.1 only.

Default starting proposal:
- 3.1.1 Trạng thái mạng và dịch vụ SMB
- 3.1.2 Trạng thái bản vá và mốc phục hồi

You may propose a change only if baseline evidence clearly justifies it.

### Proposed table(s)
For each table:
- tentative number;
- reader question answered;
- columns;
- rows;
- evidence behind each row;
- whether any row would duplicate an image.

Start from one compact table, but split into two only if readability clearly improves.

### Figure placement
For each recommended KEEP image:
- where it appears;
- what preceding sentence should ask the reader to notice;
- what direct observation may follow;
- what conclusion must NOT be made from the image alone.

### Transition
State only the conceptual transition from 3.1 to 3.2.
Do not write final prose.

## 7. Required output C — claim-evidence map

Create:

`work/do-an/CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`

Use `CHAPTER_3_SECTION_CLAIM_MAP_TEMPLATE.md`.

Every major candidate report claim must map to:
- direct/raw artifact;
- stable Evidence ID;
- external Source ID if needed;
- allowed wording;
- forbidden expansion.

At minimum include claims for:
- IP/network state;
- service/listener state;
- SMB1/SMB2;
- firewall scope;
- numeric srv.sys;
- hotfix inventory wording;
- UNPATCHED classification;
- Before Demo snapshot.

## 8. Patch-state special audit

The plan must preserve all distinctions:

- screenshot FileVersion String != numeric local version;
- numeric local version is the comparison value;
- Microsoft KB/version mapping is external source-backed;
- screenshot alone does not prove UNPATCHED;
- observed hotfix inventory wording is bounded;
- local UNPATCHED is not remote exploitability.

## 9. Image derivation policy

If crop is recommended, specify:
- source path;
- source SHA-256 from staging CSV;
- what rectangle/content should remain;
- what context must not be removed;
- presentation purpose.

Do not create crop files yet.

## 10. Student-reader test

The plan must be understandable to a lecturer who never saw the repository.

For the proposed 3.1, the reviewer must be able to answer:
1. What was the machine/network starting state?
2. What SMB state was verified locally?
3. How was patch state established?
4. What was the recovery point?
5. Which 2–3 visual items, if any, are genuinely worth showing?

## 11. Forbidden

Do not create:
- `CH3_31_BASELINE_DRAFT_R1.md`;
- any prose paragraphs for Section 3.1;
- any Scenario 1/2 content;
- Case B/C content;
- Chapter 4 analysis;
- derived crops;
- final DOCX.

Do not modify evidence bytes.

## 12. Self-review

Create:

`work/do-an/CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md`

Report:
- baseline image files inspected count;
- candidate KEEP/OPTIONAL/DROP counts;
- proposed table count;
- proposed figure count;
- claim-map row count;
- patch-state audit;
- evidence-isolation audit;
- duplication audit;
- unresolved presentation questions.

Do not self-declare PASS.

Final state:
`X7A0_BASELINE_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`

## 13. QA

Run:
```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Verify:
- no report draft file created;
- no evidence byte changed;
- all claim-map evidence paths exist;
- all reviewed baseline image paths exist;
- no Scenario 1/2/Case B/C artifact used.

## 14. Git

Commit:
`plan(ch3): design baseline evidence presentation R1`

Push:
`feature/x7a0-ch3-baseline-plan`

Do not merge.

Stop after handoff.
