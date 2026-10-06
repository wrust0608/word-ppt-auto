# X7A0 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Executor R2 candidate: `33a694b94a6f32773c7c91591d2d127649183f3c`  
Reviewer-final branch head after micro-fixes: `e6996af7ca53a273a93a1850e58c938bf40fad46`  
Branch: `feature/x7a0-ch3-baseline-plan`  
Verdict: `98/100 — PASS / WAITING_FOR_USER_APPROVAL`

## 1. Score

| Category | Score |
|---|---:|
| Scope discipline | 15/15 |
| Evidence inventory / image review | 20/20 |
| Student-facing presentation design | 19/20 |
| Technical claim accuracy | 19/20 |
| Claim/evidence traceability | 15/15 |
| Governance / numbering discipline | 10/10 |
| QA / handoff accuracy | 10/10 |
| **Total** | **98/100** |

Blockers: **0**.

## 2. Scope gate — PASS

Remote candidate HEAD matches executor handoff:
`33a694b94a6f32773c7c91591d2d127649183f3c`.

Compared with reviewer-cleaned R2 base:
`668cc5d697b98cdccd26707289bef4944f9ec320`

R2 modifies only the four authorized baseline planning artifacts:
- `CH3_31_BASELINE_FIGURE_SELECTION_R1.md`
- `CH3_31_BASELINE_PRESENTATION_PLAN_R1.md`
- `CH3_31_BASELINE_CLAIM_EVIDENCE_MAP_R1.md`
- `CH3_31_BASELINE_PLAN_SELF_REVIEW_R1.md`

No `CH3_31_BASELINE_DRAFT_R1.md` exists.
No Chapter 3 prose has been authored.

## 3. H3 structure — PASS

Approved for Section 3.1:

### 3.1.1. Trạng thái mạng và dịch vụ SMB
### 3.1.2. Trạng thái bản vá và mốc phục hồi

These titles are concise, student-facing and map cleanly to the evidence.

## 4. Table plan — PASS

### Bảng 3.1 — Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc

Columns:
- Hạng mục
- Giá trị ghi nhận
- Ghi chú

### Bảng 3.2 — Trạng thái bản vá và mốc phục hồi

Columns:
- Hạng mục
- Giá trị ghi nhận
- Ghi chú / căn cứ đối chiếu ngắn

PASS:
- no evidence filenames in student-facing tables;
- no Evidence IDs / Claim IDs;
- no risk/effectiveness column;
- ICMP row removed from main table;
- local listener state remains distinct from remote OPEN.

## 5. Figure set — PASS

Recommended tentative set:

### Hình 3.1
`Windows_PreDemo_01_Network_SMB.png`

Purpose:
- Windows IP/route;
- LanmanServer;
- FS-SMB1;
- local SMB flags;
- local TCP 139/445 listeners;
- numeric srv.sys.

### Hình 3.2
`Windows_PreDemo_02_Firewall.png`

Purpose:
- custom allow rule;
- TCP 139/445;
- source scope .56.10;
- firewall profiles;
- default File and Printer Sharing group state.

### Hình 3.3
`Windows_MS17010_02_Hotfix.png`

Purpose:
- displayed FileVersion;
- numeric srv.sys;
- observed hotfix inventory.

Classification:
- KEEP = 3
- OPTIONAL = 3
- DROP = 7

Crop policy is correctly non-rigid at planning stage.

## 6. Claim traceability — PASS

Claim IDs remain section-local:
`BASE-C01 ... BASE-C16`.

Stable Evidence IDs are now limited to the registered set:
- ENV-CORE-01
- ENV-CORE-02
- ENV-CORE-03
- ENV-CORE-04
- ENV-CORE-05

No invented `BL-*` IDs remain.

## 7. Technical-boundary gates — PASS

Corrected:
- no absolute network-isolation conclusion in allowed report wording;
- ICMP non-response has no invented firewall cause;
- LanmanServer is reported as Running/Automatic, not “healthy/normal workload”;
- local SMB flags are not converted into remote dialect results;
- local signing flags are kept separate from remote signing;
- local 139/445 listeners are not called remote OPEN;
- firewall custom rule is not expanded into a claim that every other source is blocked;
- hotfix inventory wording is bounded to observed inventory;
- snapshot is a defined restore point, not proof of perfect reproducibility.

## 8. Patch-state gate — PASS

Preserved:
- display FileVersion String = `6.3.9600.16384`;
- numeric srv.sys = `6.3.9600.16421`;
- Microsoft minimum updated = `6.3.9600.18604`;
- KB4012213 / KB4012216;
- observed inventory does not show the relevant direct/mapped update;
- local classification = `UNPATCHED`.

The screenshot itself does not independently prove UNPATCHED.
The classification uses numeric version + observed hotfix inventory + Microsoft mapping.

## 9. Reviewer micro-fixes

After executor R2, reviewer made three narrow wording corrections only:
1. removed unsupported word “static” from the Windows IP claim;
2. removed internal phrase “bảo đảm an toàn cho lab” from firewall figure-selection rationale;
3. changed a screenshot-description phrase from “hoàn toàn không xuất hiện” to bounded “không ghi nhận”.

No evidence bytes, table structure, figure set or claim meaning changed.

## 10. Final planning gate

X7A0 external review: **PASS**.

Not yet locked into integration because the workflow requires explicit user approval.

On user approval:
1. lock Bảng 3.1–3.2 in `CHAPTER_3_NUMBERING_LEDGER.md`;
2. lock Hình 3.1–3.3;
3. integrate the approved X7A0 artifacts into `feature/ch3-integration`;
4. create X7A1 from the new integration HEAD;
5. authorize Section 3.1 prose only.

X7B remains blocked until Section 3.1 itself passes external review + user approval.
