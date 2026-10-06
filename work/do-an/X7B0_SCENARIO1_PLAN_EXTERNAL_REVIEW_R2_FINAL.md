# X7B0 EXTERNAL REVIEW R2 — FINAL

Date: 2026-10-06  
Branch: `feature/x7b0-ch3-scenario1-plan`  
Executor R2 candidate: `952fbd6637c5161e9681f050024deb9e3809b53c`  
Verdict after reviewer bounded wording micro-fix: **98/100 — PASS / WAITING_FOR_USER_APPROVAL**

## 1. Executive finding

R2 resolves the blocking factual-transcription issues from R1.

The Scenario 1 presentation plan is now suitable for user review as the approved design basis for Section 3.2.

No redesign is required.

## 2. Score

| Category | Score |
|---|---:|
| Evidence coverage / isolation | 20/20 |
| Academic structure / reader flow | 20/20 |
| Figure/table selection | 20/20 |
| Technical interpretation boundaries | 20/20 |
| Evidence transcription / lineage fidelity | 18/20 |
| **Total** | **98/100** |

Blockers: **0**.

## 3. Evidence fidelity — PASS

Independent comparison against B2–B6 raw Nmap outputs, Scenario 1 manifest, and direct screenshots confirms:

- no operational `-Pn` remains in the plan;
- B4 MAC is correctly bounded to direct evidence and omitted from the public table;
- B3 public result is reduced to target `up`, without unnecessary latency;
- B5 preserves the Nmap fingerprint range `Microsoft Windows Server 2008 R2–2012`;
- B6 preserves the five observed dialects, recorded capabilities, and `Message signing enabled but not required`;
- `smb-os-discovery` remains `no usable output` with no invented cause.

## 4. Academic structure — PASS

Locked recommendation for user review:

- **3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB**
  - B2–B4;
  - B2/B3 remain visible but not over-expanded;
  - no dedicated B2/B3/B4 figure.

- **3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB**
  - B5–B6;
  - B5 and B6 direct evidence figures retained.

This structure makes the experiment readable as a discovery sequence rather than a command log.

## 5. Table design — PASS

Recommended public table:

**Bảng 3.3 — Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux**

Columns:

`Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`

The table is now result-oriented and no longer duplicates Chapter 2 command syntax.

Reviewer made two bounded wording micro-fixes after R2:

1. B3 interpretation was narrowed from "sẵn sàng tiếp nhận kết nối" to "mục tiêu đang trực tuyến".
2. B4 interpretation was narrowed from service-level acceptance to the directly observed fact that TCP 139/445 were reachable/open and returned SYN-ACK from the Kali vantage point.

These changes do not alter the experiment or presentation geometry.

## 6. Figure selection — PASS

Final recommended set for user approval:

- B4 screenshot: **DROP**
- B5 screenshot: **KEEP — tentative Hình 3.4**
- B6 screenshot: **KEEP — tentative Hình 3.5**

Rationale:

- B4 contains only short port-state data that Bảng 3.3 communicates more efficiently.
- B5 visually demonstrates the limitation of the Nmap fingerprint range.
- B6 is the highest-value direct evidence image because it shows dialects, capabilities and signing in one result block.

No additional screenshot is needed.

## 7. Crop planning — PASS

Provisional reproducible rectangles are acceptable:

- B5 source 1280×800:
  `x=0, y=24, width=1280, height=310`
- B6 source 1280×800:
  `x=0, y=24, width=1280, height=710`

No derived crop has yet been created, which is correct for X7B0.

Actual crop files and crop manifest must be created during X7B1 only after user approval of this plan.

## 8. Technical-boundary gate — PASS

The plan preserves:

- `.56.100 = UNKNOWN identity`;
- `445 OPEN != vulnerable`;
- B5 fingerprint range != exact Windows Server 2012 R2 identification;
- SMBv1 observation != MS17-010 confirmation;
- local baseline facts remain separate from remote measurement;
- `smb-os-discovery = no usable output`;
- Scenario 1 does not produce an MS17-010 verdict.

## 9. Lecturer / defense-readiness assessment

From the perspective of an Information Security thesis examiner, the proposed Section 3.2 geometry is strong:

- the reader can see the measurement progression immediately;
- B2/B3 are documented without wasting visual space;
- B4 is summarized efficiently;
- B5 demonstrates the precision limit of remote fingerprinting;
- B6 provides the strongest protocol-level evidence;
- the section naturally motivates Scenario 2 without pre-empting its vulnerability-oriented measurements.

The plan is sufficiently clear and defensible for a student project report.

## 10. Final gate

External review: **PASS**.

Current state:

`X7B0_PASS_WAITING_FOR_USER_APPROVAL`

Do not open X7B1 yet.

On explicit user approval:
1. lock the 2-H3 Scenario 1 structure;
2. lock Bảng 3.3;
3. lock Hình 3.4–3.5;
4. explicitly integrate approved X7B0 planning artifacts into `feature/ch3-integration`;
5. update `CHAPTER_3_NUMBERING_LEDGER.md` so the next available numbers become Bảng 3.4 and Hình 3.6;
6. create X7B1 from the new integration HEAD;
7. X7B1 may create the approved B5/B6 presentation crops + crop manifest and write Section 3.2 prose only;
8. Scenario 2 remains blocked until Section 3.2 prose passes external review + user approval.
