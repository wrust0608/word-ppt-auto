# X7D1 SECTION 3.4 CASE B — EXTERNAL REVIEW R2 FINAL

Date: 2026-10-07  
Branch: `feature/x7d1-ch3-caseb-draft`  
Executor R2 candidate: `2e0f74b1c466922d14e0d7c50357338f2ad89878`  
Reviewer-final HEAD: determined by repository after the two bounded wording corrections.

Verdict: **99/100 — PASS**

## 1. Final assessment

Section 3.4 is ready for user approval.

The R2 executor correctly resolved all blocking issues from R1:
- project validator was restored to the original X7D1 starting version;
- TCP 445 wording is observation-only;
- dialect retest wording no longer overstates causality;
- UNPATCHED provenance is correctly bounded;
- Hình 3.7 crop manifest no longer misstates StartType;
- prose was compressed from 1,385 to approximately 1,246 words;
- presentation images and raw evidence hashes remain unchanged.

The reviewer then applied two non-substantive wording tightenings:
1. replaced the phrase implying the service/process state was simply "unchanged" with explicit point-in-time observations;
2. replaced a residual causal phrase "can thiệp cấu hình đã loại bỏ phương ngữ SMBv1..." with a direct measurement statement that NT LM 0.12 does not appear in the retest list.

These edits do not change evidence allocation, technical meaning, figure/table numbering, or the approved X7D0 plan.

## 2. Technical locks — PASS

Verified:
- `SMBv1 disabled != FS-SMB1 uninstalled`;
- `SMBv1 disabled != PATCHED`;
- `445 OPEN != vulnerable`;
- `UNKNOWN != SAFE`;
- Case B after-state does not inherit `syn-ack`;
- no successful-negotiation/handshake claim;
- no zero-downtime claim;
- no workload-continuity claim;
- no feature-uninstall claim;
- no remote SAFE / NOT VULNERABLE claim;
- no false-negative claim;
- no NTSTATUS / IPC$ / SMBv1-probe-cause invention;
- no Case C result leakage;
- no Chapter 4 analysis leakage.

## 3. Presentation — PASS

Locked:
- one table only: Bảng 3.5;
- Hình 3.7: local after-state;
- Hình 3.8: remote dialect retest;
- no Before image;
- no Action image;
- no combined NSE04 image.

The approved crop geometry remains unchanged:
- Hình 3.7: `x=0,y=30,w=872,h=310`;
- Hình 3.8: `x=0,y=24,w=1280,h=400`.

Both images remain readable and focused for later A4 assembly.

## 4. Academic/product quality — PASS

The section now reads as a result narrative rather than an audit log:

`before -> intervention -> local after-state -> remote protocol retest -> remote MS17 retest -> bounded conclusion -> transition to Case C`.

Bảng 3.5 carries most repeated facts, so the prose no longer re-narrates every cell.

The remaining explanation is sufficient for a lecturer to understand:
- what changed;
- what did not change;
- what the remote measurements actually show;
- why disabling SMBv1 must not be confused with patching.

## 5. QA note

The restored historical `validate_project.py` may report a broken-link false positive caused by Markdown example syntax inside the manager prompt. This is not a Chapter 3 content defect and is intentionally not "fixed" inside X7D1.

Other reported checks:
- unit tests PASS;
- Vietnamese academic linter PASS;
- `git diff --check` PASS;
- raw evidence hashes unchanged;
- presentation-image hashes unchanged.

## 6. Final gate

Verdict:

`X7D1_CASEB_DRAFT_R2_FINAL_EXTERNAL_PASS`

Blockers: **0**

Section 3.4 must now wait for explicit user approval.

Do not:
- integrate automatically;
- open X7E / Case C;
- assemble Chapter 3;
- build Word.

After user approval:
1. create a user-approval lock for Section 3.4;
2. integrate only the approved Section 3.4 artifacts/reviews into `feature/ch3-integration`;
3. preserve Bảng 3.5 and Hình 3.7–3.8 numbering;
4. next numbering remains Bảng 3.6 / Hình 3.9;
5. only then open Case C planning.
