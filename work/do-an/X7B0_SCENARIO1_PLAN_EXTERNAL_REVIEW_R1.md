# X7B0 EXTERNAL REVIEW R1 — SCENARIO 1 PLAN

Date: 2026-10-06  
Branch: `feature/x7b0-ch3-scenario1-plan`  
Candidate: `4a9e40626a14b0ff60d9820df59037e0d5e237e7`  
Verdict: **91/100 — REVISE_MINOR_BLOCKING**

## 1. Executive finding

The overall academic presentation direction is strong and should be preserved.

The proposed 2-H3 structure, one compact result table, B4 screenshot DROP, and B5/B6 screenshot KEEP strategy are suitable for a student-facing Information Security thesis section. The plan correctly avoids turning Scenario 1 into a screenshot album and preserves the main technical interpretation boundaries.

However, the plan is not ready for user approval because several factual transcription errors were introduced into the planning artifacts. These are narrow and correctable without redesign.

## 2. Score

| Category | Score |
|---|---:|
| Evidence coverage / isolation | 19/20 |
| Academic structure / reader flow | 19/20 |
| Figure/table selection | 19/20 |
| Technical interpretation boundaries | 19/20 |
| Evidence transcription / lineage fidelity | 15/20 |
| **Total** | **91/100** |

Blocking corrections: **3 narrow issues**.

## 3. What passes

### 3.1 Structure — PASS

Recommended structure is appropriate:

- 3.2.1 groups B2–B4 as discovery/port results;
- 3.2.2 groups B5–B6 as service/protocol characterization.

This is preferable to creating one H3 per Nmap step.

### 3.2 Table strategy — PASS

One compact Bảng 3.3 for B2–B6 is appropriate.

B2 and B3 do not need dedicated screenshots. B3 should remain a short continuity/target-confirmation step rather than receiving disproportionate narrative space.

### 3.3 Figure strategy — PASS

Independent visual inspection confirms:

- `Scenario1_B4_SMB_Ports.png`: readable but information-light and redundant with Bảng 3.3 → DROP is appropriate.
- `Scenario1_B5_SMB_Version.png`: useful direct evidence for the limited `Microsoft Windows Server 2008 R2 - 2012` fingerprint range → KEEP.
- `Scenario1_B6_SMB_NSE_A.png`: highest information value; directly shows dialects, SMB2 capabilities, signing result, and the command includes `smb-os-discovery` while no usable result block is printed → KEEP.

The standard 2-figure plan is acceptable and does not constitute screenshot overload.

### 3.4 Interpretation boundaries — PASS

The plan correctly preserves:

- `.56.100 = UNKNOWN identity`;
- `445 OPEN != vulnerable`;
- B5 fingerprint is a range, not exact Windows Server 2012 R2 identification;
- SMBv1 observation does not confirm MS17-010;
- remote signing is `enabled but not required`;
- `smb-os-discovery` has no usable output without assigning a cause;
- Scenario 1 does not make an MS17-010 verdict.

## 4. Blocking correction A — invented `-Pn` parameter

Direct raw evidence, screenshots, Scenario 1 manifest, and approved Chapter 2 operator lineage all agree that B4, B5 and B6 **do not use `-Pn`**.

Authoritative command lineage:

- B4: `sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports`
- B5: `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`
- B6: `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse`

R1 incorrectly inserts `-Pn` in:
- three rows of `CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`;
- the B4 row of `CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`.

This is blocking because it changes the performed method and would conflict with Chapter 2 and direct evidence if propagated into prose.

Required correction:
- remove every invented `-Pn`;
- do not invent or normalize command options;
- where exact commands are unnecessary in the student-facing table, prefer short method labels instead of duplicating Chapter 2 command syntax.

## 5. Blocking correction B — incorrect B4 MAC address

R1 states B4 MAC:

`08:00:27:1B:32:04`

Direct B4 raw output and screenshot both show:

`08:00:27:55:71:CE`

The incorrect MAC must be removed or corrected.

Reviewer preference:
- remove MAC from the public-facing presentation design because it adds no value to the reader question of Section 3.2;
- if retained in an internal evidence note, use the direct observed value only.

## 6. Blocking correction C — table should be more result-oriented than method-oriented

Chapter 3 is a results chapter. Chapter 2 already records exact commands.

The current Bảng 3.3 concept is sound, but the `Kỹ thuật / Công cụ` column should not become a second command ledger.

R2 should use concise method labels, for example:
- ARP host discovery;
- single-target ARP confirmation;
- TCP SYN scan of 139/445;
- Nmap service/version detection;
- Nmap NSE SMB profiling.

This also eliminates the risk of future command-line drift.

For B3, omit the exact `0.00034 s` latency from the proposed public table unless a clear analytical purpose is identified. The meaningful result is simply that `192.168.56.20` was observed up before deeper scanning.

## 7. Minor academic refinements

These are not redesign requests:

1. Replace mechanistic wording such as `probe/banner` with the more defensible `kết quả nhận diện dịch vụ/phiên bản của Nmap` unless the mechanism itself is being analyzed.
2. For B6, prefer direct wording:
   `Nmap smb-protocols ghi nhận các dialect ...`
   rather than stronger wording such as `xác nhận ngăn xếp sẵn sàng đàm phán` where the direct output wording is sufficient.
3. If crops remain recommended, record a provisional reproducible crop rectangle for B5 and B6 in R2. Final crop manifest and derived SHA remain deferred until crops are actually created.

## 8. Lecturer / thesis-defense assessment

From a thesis-reader perspective, the proposed section geometry is strong:

- B2/B3 are visible without wasting figures;
- B4 is summarized efficiently;
- B5 visually demonstrates the fingerprint limitation;
- B6 provides the strongest protocol-level evidence;
- the transition to Scenario 2 has a clear intellectual purpose.

No additional screenshot is needed.

The weakness is not the presentation design; it is evidence transcription fidelity. This must be corrected before user approval because a defense panel can immediately challenge a command shown in the report that does not match the recorded experiment.

## 9. Final gate

Verdict: **REVISE_MINOR_BLOCKING**.

Do not open X7B1 prose.

R2 must be a bounded correction of the four X7B0 planning artifacts only.

After R2, perform a final external review again before asking the user to approve X7B0.
