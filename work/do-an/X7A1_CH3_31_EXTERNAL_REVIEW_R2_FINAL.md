# X7A1 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7a1-ch3-baseline-draft`  
Executor R2 candidate: `c2acf1b4bc41c4260f14416fd217b94bf4f829c7`  
Reviewer-final branch head after one bounded wording micro-fix: `2d4690e8c40c870abd19019c0d51b31456a9229c`  
Verdict: `99/100 — PASS / WAITING_FOR_USER_APPROVAL`

## 1. Executive finding

R2 resolves the blocking issues identified in X7A1 R1.

The section is now suitable for user review as a student-facing Chapter 3 result subsection.

No redesign is required.

## 2. Score

| Category | Score |
|---|---:|
| Scope / structure discipline | 15/15 |
| Table/figure presentation | 20/20 |
| Evidence preservation / crop traceability | 15/15 |
| Technical accuracy / bounded interpretation | 20/20 |
| Academic student-facing prose | 14/15 |
| Citation traceability | 10/10 |
| Self-review accuracy | 5/5 |
| **Total** | **99/100** |

Blockers: **0**.

## 3. Scope gate — PASS

Compared with R1 base:
`9c180faab36738626976665059db507e06954725`

Executor R2 modified only:
- `CH3_31_BASELINE_DRAFT_R1.md`
- `CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`

Crop manifest, presentation images, source evidence, X7A0 planning artifacts and Chapter 1/2 were unchanged by R2.

## 4. Structure gate — PASS

Locked structure preserved:
- 1 H2;
- 2 H3;
- 2 tables;
- 3 figures.

No Section 3.2 prose was created.

No Scenario 1/2, Case B/C or Chapter 4 result leakage.

## 5. Technical-boundary gate — PASS

R2 correctly fixes the main R1 overclaims:

- local `EnableSMB1Protocol/EnableSMB2Protocol` flags are reported only as local server configuration;
- remote dialect negotiation is deferred to Scenario 1;
- local signing flags remain separate from remote signing observations;
- local TCP 139/445 Listen state is not called remote OPEN;
- remote accessibility is deferred to later remote measurements;
- Windows Firewall is described as configuration state only;
- no traffic-success or global-block guarantee is inferred from the custom rule;
- no “middle firewall” is introduced in baseline;
- `6.3.9600.18604` is described as the minimum updated version, not a generic safety threshold;
- hotfix wording is bounded to the observed inventory;
- `UNPATCHED` remains a local patch-state classification;
- snapshot is only the defined restore point.

The ICMP/ARP paragraph was correctly removed from student-facing prose.

## 6. Tables — PASS

### Bảng 3.1
Student-facing, compact and readable.

Strong points:
- local configuration and local listener state are clearly separated from remote results;
- no evidence filenames or internal IDs;
- firewall values are reported without unsupported effectiveness claims.

### Bảng 3.2
Correctly separates:
- display FileVersion;
- numeric srv.sys;
- Microsoft minimum updated version;
- KB mapping;
- observed hotfix inventory;
- local UNPATCHED classification;
- restore point.

## 7. Figures — PASS

All three presentation figures remain unchanged from R1 and were independently inspected.

### Hình 3.1
Readable; preserves all relevant network/SMB/local-listener fields.

### Hình 3.2
Readable; preserves custom rule, .56.10 source scope, profile state and default File and Printer Sharing group state.

### Hình 3.3
Readable; preserves display version, numeric version and six hotfix rows while removing irrelevant Action Center UI.

The crop manifest remains traceable to the source evidence hashes.

## 8. Citation strategy — PASS FOR DRAFT STAGE

R1's incorrect visible `[4]`/`[5]` markers are removed.

R2 names the two Microsoft sources naturally and preserves one internal non-rendering anchor:

`<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`

This is correct for the current project phase because:
- S005 = Microsoft Security Bulletin MS17-010;
- S032 = Microsoft Support verification guide;
- final numeric IEEE labels are not yet globally normalized.

No final numeric label is invented.

This must be resolved at the full-report IEEE normalization gate before publication.

## 9. Reviewer micro-fix

One final wording adjustment was made directly after R2:

From:
`Windows ... được gán ... và bảng định tuyến ... không định tuyến kết nối ra bên ngoài mạng phân đoạn.`

To:
`Windows ... được ghi nhận ... và bảng định tuyến cục bộ không ghi nhận tuyến mặc định.`

Reason:
keep the sentence at the level directly supported by the observed routing state and avoid overgeneralizing network reachability.

No claim meaning, table, figure or evidence changed.

## 10. Academic-readability finding

The section now follows a useful student-report flow:

1. baseline network and local SMB state;
2. compact table;
3. direct Windows evidence;
4. firewall configuration;
5. patch-state verification;
6. patch/snapshot table;
7. patch evidence image;
8. neutral transition to Scenario 1.

The section no longer reads like an internal audit memo.

## 11. Final gate

External review: **PASS**.

Current state:
`X7A1_PASS_WAITING_FOR_USER_APPROVAL`.

On user approval:
1. mark Section 3.1 prose USER APPROVED / LOCKED;
2. integrate the completed Section 3.1 artifacts into `feature/ch3-integration`;
3. retain Bảng 3.1–3.2 and Hình 3.1–3.3 numbering;
4. open X7B0 — Scenario 1 evidence/presentation planning only;
5. do not write Scenario 1 prose until X7B0 passes its own review.
