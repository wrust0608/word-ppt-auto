# X7E1 SECTION 3.5 CASE C — EXTERNAL REVIEW R2 FINAL

Date: 2026-10-07  
Branch: `feature/x7e1-ch3-casec-draft`  
Executor R2 candidate: `00c6936eabd096af11c71db91f78a97f19a348b8`

Verdict: **99/100 — PASS**

## 1. Final assessment

Section 3.5 is ready for explicit user approval.

R2 resolves all blocking issues from the R1 review without changing the user-approved Case C structure or evidence allocation.

Final product shape:
- 1 H2;
- 2 H3;
- Bảng 3.6;
- Hình 3.9;
- Hình 3.10;
- Hình 3.11;
- no Hình 3.12 in the standard layout.

Prose is now approximately 1,442 words, which is appropriate for the wider evidence set in Case C while remaining controlled enough for the final Chapter 3 coherence review.

## 2. NSE-SMB-04 boundary — PASS

Verified:
- TCP 445 = FILTERED;
- no usable vulnerability verdict;
- classification remains `UNKNOWN / NO USABLE SCRIPT RESULT`;
- no internal script-failure cause is asserted;
- `UNKNOWN != SAFE`.

The prohibited R1 sentence assigning the missing verdict to blocked traffic has been removed.

## 3. Windows-local state — PASS

The final draft now uses recorded-action and point-in-time language:
- Case C does not record an SMB configuration change on Windows;
- Case C does not record a patch-install action;
- final recorded state:
  - SMB1=True;
  - SMB2=True;
  - LanmanServer=Running;
  - local listeners 139/445 present;
  - patch classification UNPATCHED;
  - numeric srv.sys version used for patch classification = 6.3.9600.16421.

No continuous-uptime, lifetime-binary-history or "pfSense changed the host" inference remains.

## 4. Hình 3.11 presentation honesty — PASS

The approved crop remains:
`x=40,y=15355,w=1280,h=220`.

It preserves:
- four Block rows;
- CASE_C_KALI;
- source/destination addresses and ports;
- TCP:S;
- the conflicting Rule label.

The crop does not contain the original table-heading row.

The R2 draft now explicitly gives the reader a short field-order guide, and the crop manifest states:
- the heading row is outside the tight crop;
- field interpretation was checked against the full source screenshot;
- no labels or artificial annotations were added;
- no montage was created.

This is an acceptable and transparent presentation choice for the final A4 report.

## 5. Rule-label conflict — PASS

The visible screenshot label remains:

`CASE C baseline pass Kali to Windows (100000104)`

while the run record names:

`CASE C - Block SMB Kali to Windows (1000000104)`.

The final text:
- discloses the mismatch;
- does not invent a reconciliation;
- uses Hình 3.11 only to support the observed Block action on matching SMB SYN traffic;
- does not claim the screenshot proves the exact named Block rule matched.

## 6. Network-result wording — PASS

Verified:
- 139/tcp FILTERED / no-response;
- 445/tcp FILTERED / no-response;
- baseline OPEN/syn-ack comparison remains bounded to earlier measurements;
- `FILTERED != PATCHED`;
- no CLOSED claim;
- no local-service-stopped claim;
- ARP wording is now limited to the target being up with arp-response in the Case C topology.

Nmap and pfSense records are described as a cross-layer comparison, not as globally synchronized causal proof.

## 7. Bảng 3.6 — PASS

The approved 4-column / 10-row table remains intact but is now materially more readable.

The fourth column has been compressed to concise result/boundary statements rather than repeating full prose.

Important distinctions remain visible:
- baseline had no pfSense on the tested path, not "no firewall";
- 139/445 OPEN -> FILTERED from the Kali vantage point;
- remote MS17 result remains UNKNOWN;
- local SMB1 remains True;
- local service/listener state remains present at the recorded point;
- local patch classification remains UNPATCHED.

## 8. Academic/product quality — PASS

R2 now reads more like a Vietnamese Information Security project report and less like an internal evidence audit.

The reader flow is clear:

`Case C control setup -> Bảng 3.6 overview -> Nmap FILTERED result -> pfSense Block-log comparison -> rule-label disclosure -> MS17 UNKNOWN -> local Windows state -> bounded conclusion`.

The conclusion is appropriately empirical and prepares Section 3.6 without ranking Case B vs Case C prematurely.

## 9. Artifact integrity — PASS

Compared with reviewer base `7611bbb1628fe68594ec516c9a91f444e720c32f`, R2 changes only:
- `CH3_35_CASEC_DRAFT_R1.md`;
- `CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`;
- `CH3_35_CASEC_CROP_MANIFEST_R1.md`.

The three presentation images are byte-identical to R1:
- Hình 3.9 SHA-256 `5b8a4a3b26c6aca6b667e5a4ee256c48dcdd555324e2f7ed0755ae80eba06285`;
- Hình 3.10 SHA-256 `da342f6fb9909da67fd38caedf73e2f848ac3c65306ec5993f864f9260418942`;
- Hình 3.11 SHA-256 `8333c06da3e35553481d00a7f84c4d65b64dde5a4f7aadc77567d52d113c919b`.

## 10. QA

Executor reported:
- unit tests PASS;
- Vietnamese academic linter PASS;
- `git diff --check` PASS;
- clean working tree.

Independent repository comparison confirms the R2 commit is one commit ahead of the reviewer base and modifies only the three authorized text artifacts.

## 11. Final gate

Verdict:

`X7E1_CASEC_DRAFT_R2_FINAL_EXTERNAL_PASS`

Score: **99/100**

Blockers: **0**

Section 3.5 must now wait for explicit user approval.

Do not:
- integrate automatically;
- open Section 3.6/3.7;
- assemble Chapter 3;
- build Word.

After explicit user approval:
1. create Section 3.5 user-approval lock;
2. integrate the approved Section 3.5 draft/crop artifacts/reviews into `feature/ch3-integration`;
3. preserve Bảng 3.6 and Hình 3.9–3.11;
4. next numbering remains Bảng 3.7 / Hình 3.12;
5. then open Section 3.6–3.7 synthesis workflow.
