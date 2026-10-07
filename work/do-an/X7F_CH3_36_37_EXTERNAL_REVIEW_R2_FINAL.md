# X7F SECTIONS 3.6–3.7 — EXTERNAL REVIEW R2 FINAL

Date: 2026-10-07  
Branch: `feature/x7f-ch3-synthesis`  
Executor R2 candidate: `0567e1128110f691b905f9c2aa6c7cae60f490f8`

Verdict: **99/100 — PASS**

## 1. Final assessment

Sections 3.6 and 3.7 are ready for explicit user approval.

The R2 executor corrected the technical overclaims from R1 while preserving the intended synthesis structure:
- Section 3.6 compares approved results rather than retelling all prior sections;
- Section 3.7 closes Chapter 3 without opening Chapter 4;
- Bảng 3.7 is the sole synthesis table;
- no new figure or evidence was introduced.

The reviewer then applied a few bounded wording tightenings:
- patch classification is stated as an approved state plus absence of a recorded patch-install action, not as a causal consequence;
- FILTERED wording is kept observational rather than framed as proof of a mechanism;
- the Chapter 3 conclusion limits claims about automated testing to the tools used in this project.

These edits do not change technical meaning or table structure.

## 2. Bảng 3.7 — PASS

Final structure:
- 4 columns;
- 8 comparison rows;
- compact enough for later A4 layout.

Critical cells are now correct:

### TCP 139
- Baseline: `OPEN (syn-ack)`
- Case B: `Không đo lại trong Case B`
- Case C: `FILTERED (no-response)`

### TCP 445
- Baseline: `OPEN (syn-ack)`
- Case B: `OPEN`
- Case C: `FILTERED (no-response)`

The Case B post-intervention `syn-ack` overclaim is fully removed.

### SMB dialects
- Baseline: five recorded dialect values;
- Case B: four recorded values; `NT LM 0.12` does not appear;
- Case C: no corresponding dialect measurement.

No negotiation/workload-success claim remains.

### Local service
The comparison uses `LanmanServer` only:
- Baseline: Running;
- Case B: Running at the recorded check;
- Case C: Running at the recorded final state.

No Case B local-listener measurement is invented.

### Patch state
All three states remain bounded to the approved local classification:
- baseline UNPATCHED;
- Case B UNPATCHED; no recorded patch-install action;
- Case C UNPATCHED; no recorded patch-install action.

### Remote MS17
All three:
`UNKNOWN / NO USABLE SCRIPT RESULT`.

No internal cause is assigned.

## 3. Section 3.6 — PASS

The final comparison correctly distinguishes:
- host-side protocol configuration change in Case B;
- tested-path network filtering observations in Case C;
- independent local patch classification;
- independent remote MS17 verdict.

Verified boundaries:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`
- `UNKNOWN != SAFE`

The prose does not rank Case B against Case C and does not recommend a control.

## 4. Section 3.7 — PASS

The chapter conclusion now uses direct observation language:
- after Case B, `NT LM 0.12` does not appear in the retest dialect list and TCP 445 is recorded OPEN;
- in Case C, TCP 139/445 are recorded FILTERED/no-response from Kali;
- remote MS17 results remain UNKNOWN;
- local patch classification remains UNPATCHED.

The conclusion closes the empirical scope without opening Chapter 4 or adding recommendations.

## 5. Product quality — PASS

The final X7F output works as a thesis synthesis rather than an internal audit summary.

The reader can understand, in one table and a short synthesis:
1. what was measured at baseline;
2. what changed in Case B;
3. what changed in Case C;
4. what was not remeasured;
5. which conclusions remain outside the evidence.

No new Hình 3.12 is required.

## 6. Artifact integrity — PASS

Compared with the reviewer base, R2 modifies only:
- `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- `work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`

No evidence, image, infrastructure or other chapter file was changed.

## 7. QA

Executor reported:
- Section 3.6 prose: approximately 745 words;
- Section 3.7 prose: approximately 316 words;
- total prose: approximately 1,061 words;
- unit tests PASS;
- Vietnamese academic linter PASS;
- `git diff --check` PASS;
- clean working tree before reviewer edits.

## 8. Final gate

Verdict:

`X7F_CH3_36_37_R2_FINAL_EXTERNAL_PASS`

Score: **99/100**

Blockers: **0**

Sections 3.6–3.7 now wait for explicit user approval.

Do not:
- integrate automatically;
- assemble Chapter 3;
- build Word;
- modify Chapter 2;
- open Chapter 4.

After explicit user approval:
1. create X7F user-approval lock;
2. integrate approved X7F artifacts/reviews into `feature/ch3-integration`;
3. lock Bảng 3.7;
4. no Hình 3.12 is allocated by X7F;
5. open X7G mechanical assembly of complete Chapter 3;
6. after X7G, perform X7H whole-Chapter-3 review before any Chapter 2+3 DOCX work.
