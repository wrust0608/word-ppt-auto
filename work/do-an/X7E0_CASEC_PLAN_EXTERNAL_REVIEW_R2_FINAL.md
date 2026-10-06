# X7E0 CASE C EVIDENCE & PRESENTATION PLAN — EXTERNAL REVIEW R2 FINAL

Date: 2026-10-07  
Branch: `feature/x7e0-ch3-casec-plan`  
Executor R2 candidate: `51ecfcb8c89bc51a768d889705819d1ead7ae5e0`

Verdict: **99/100 — PASS**

## 1. Final assessment

The R2 plan is ready for user approval.

All blocking issues from R1 were corrected without changing the accepted product structure.

Locked product shape:
- 2 H3;
- 1 Bảng 3.6;
- 3 main figures:
  - Hình 3.9 — pfSense rule order/configuration;
  - Hình 3.10 — Nmap 139/445 FILTERED result;
  - Hình 3.11 — pfSense Block log;
- bridge screenshot and NSE04 screenshot remain OPTIONAL/DROP for the standard layout.

This is an appropriate balance between technical proof and page economy.

## 2. Evidence-boundary review — PASS

Verified:
- NSE04 no longer receives an invented internal failure cause;
- Case C result remains `UNKNOWN / NO USABLE SCRIPT RESULT`;
- `UNKNOWN != SAFE`;
- `FILTERED != PATCHED`;
- local SMB1=True / SMB2=True / LanmanServer=Running / listeners / UNPATCHED are kept as point-in-time metadata facts;
- no claim that SMBv1 is remotely exploitable;
- no claim that the server is safe/patched/not vulnerable;
- no bypass -> exploit-success inference;
- no global synchronized timeline across Kali/pfSense.

## 3. Baseline wording — PASS

Bảng 3.6 no longer says the baseline had "no firewall".

Corrected distinction:
- baseline: no pfSense on the Kali -> Windows tested path;
- Case C: tested path is placed through pfSense Transparent Bridge with the Case C ruleset.

This preserves the already locked Windows Firewall baseline.

## 4. Cross-layer wording — PASS

The R2 plan replaces strong causal claims with bounded comparison:

- Nmap records 139/445 FILTERED;
- pfSense logs record corresponding TCP SYN traffic being Blocked;
- the report may describe this as cross-layer comparison;
- it does not claim absolute causal proof from synchronized clocks.

The rule-label discrepancy remains explicit and unresolved.

Allowed report conclusion:
`matching SMB SYN traffic was blocked in the pfSense path`.

Forbidden:
the log screenshot proves the exact named Block rule matched.

## 5. Figure plan — PASS

### Hình 3.9
The revised provisional crop around:
`x≈15, y≈190, w≈470, h≈340`
is consistent with the visual source and preserves:
- CASE_C_KALI context;
- Rules heading;
- full Block row;
- full Pass row.

### Hình 3.10
The proposed crop retains:
- Nmap command;
- host/ARP response;
- both FILTERED rows;
- MAC;
- Nmap done.

### Hình 3.11
The crop is correctly marked PROVISIONAL ONLY.

X7E1 must visually verify the actual log region before creating the derived crop.

The final crop must preserve:
- relevant log headings;
- 139/445 Block rows;
- Rule column / visible rule-label conflict when used.

No crop may hide the discrepancy.

## 6. Evidence-map integrity — PASS

The nonexistent `CHAPTER_3_EVIDENCE_INDEX.md` reference was removed.

The claim map now relies on:
- actual evidence files;
- evidence type:
  - Direct raw;
  - Direct visual;
  - Metadata/lineage;
- allowed wording;
- forbidden inference.

No new evidence registry was invented.

## 7. Product-quality review — PASS

The plan now supports a thesis result section rather than a pfSense installation tutorial.

The intended reader flow is clear:

`control-path / rules -> observed FILTERED result -> firewall log comparison -> MS17 UNKNOWN -> unchanged local Windows state`

The three-figure strategy is sufficient for a lecturer to see:
1. what network control was configured;
2. what Kali observed;
3. what pfSense recorded.

The remaining setup screenshots would add little value to the final page flow and correctly remain excluded from the standard layout.

## 8. QA

Executor reported:
- unit tests PASS;
- `git diff --check` PASS;
- project validation PASS;
- clean working tree.

Branch diff from the reviewer base changes only the four authorized X7E0 plan files.

## 9. Final gate

Verdict:

`X7E0_CASEC_PLAN_R2_FINAL_EXTERNAL_PASS`

Blockers: **0**

The Case C plan now waits for explicit user approval.

Do not:
- write Section 3.5 prose;
- create derived crops;
- open X7F;
- assemble Chapter 3;
- build Word.

After explicit user approval:
1. create the Case C plan user-approval lock;
2. integrate only approved X7E0 plan/review artifacts into `feature/ch3-integration`;
3. lock Bảng 3.6 and Hình 3.9–3.11 allocation;
4. next numbering becomes Bảng 3.7 / Hình 3.12 unless the OPTIONAL NSE04 figure is intentionally activated;
5. open X7E1 to create the final crops and write Section 3.5 prose.
