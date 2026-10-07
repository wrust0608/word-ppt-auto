# X7H WHOLE-CHAPTER-3 PRODUCT REVIEW — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7h-ch3-whole-review-approved-r1`  
Executor candidate: `01cc66de9845395777ced08801d5816ab1f938fe`

Verdict: **REVISE_BLOCKING**  
Score: **92/100**

## 1. Independent verification

The reviewer independently verified that:
- branch HEAD exactly matches `01cc66de9845395777ced08801d5816ab1f938fe`;
- X7H adds only the authorized prompt plus:
  - `CHAPTER_3_DRAFT_R2.md`;
  - `X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1.md`;
  - `X7H_CH3_WHOLE_REVIEW_EXECUTOR_HANDOFF_R1.md`;
- Chapter structure remains 1 H1, 7 canonical H2, 10 H3;
- Bảng 3.1–3.7 and Hình 3.1–3.11 remain unchanged in numbering/allocation;
- no Bảng 3.8 or Hình 3.12 was added;
- the R1→R2 chapter difference consists of exactly 11 replaced prose blocks.

The editorial direction is generally good:
- repetitive openings were reduced;
- several long sentences were shortened;
- transitions are more natural;
- total prose was reduced without major structural compression;
- no Chapter 4 recommendation/risk-ranking section was added.

However, four R2 wording changes cross the X7H boundary by strengthening or changing technical/evidence meaning.

## 2. Blocking issue 1 — Case C topology changed from transparent bridging to routing

R2 currently states:

`đường thử nghiệm giữa trạm Kali và máy chủ Windows được định tuyến qua tường lửa pfSense hoạt động ở chế độ Transparent Bridge (Layer 2)`

This is technically inconsistent.

The approved Case C source states that the test path is **bố trí đi qua** pfSense operating as a **Transparent Bridge Layer 2**. A transparent Layer-2 bridge is not described here as a routed path.

Required correction:
- replace `được định tuyến qua` with bounded wording such as `được bố trí đi qua`;
- preserve `Transparent Bridge (Layer 2)`;
- do not introduce router/L3 semantics.

This is a factual topology drift introduced by X7H.

## 3. Blocking issue 2 — firewall wording overclaims exclusivity

R2 states:

`Thiết lập này bảo đảm bề mặt dịch vụ tại baseline chỉ mở cho trạm kiểm thử chỉ định`

The locked evidence supports:
- a custom inbound allow rule for TCP 139/445 scoped to source `192.168.56.10`;
- default File and Printer Sharing rules observed disabled;
- actual remote reachability is measured separately from Kali.

It does not authorize a global claim that the service exposure is guaranteed to be open **only** to that station.

Required correction:
- return to configuration-bounded language;
- describe the rule scope and disabled default rules;
- keep actual reachability as a separate measurement.

## 4. Blocking issue 3 — local hotfix inventory wording became historical/omniscient

R2 states:

`danh sách cập nhật dừng ở năm 2014`

This is stronger than the approved evidence.

The locked evidence is a local `Get-HotFix` inventory in which six observed items have 2014 installation dates, with the relevant mapped MS17-010 updates not observed in that inventory. It is not a complete omniscient update-history claim.

Required correction:
- use bounded wording such as:
  `sáu mục Get-HotFix quan sát được đều có ngày cài đặt trong năm 2014`;
- keep UNPATCHED classification tied to the numeric `srv.sys` comparison plus the observed inventory;
- avoid `dừng ở`, `chỉ cập nhật đến`, or equivalent complete-history wording.

## 5. Blocking issue 4 — Nmap fingerprint wording became an absolute capability claim

R2 states:

`Nmap chỉ khu biệt hệ thống trong một dải phiên bản ... chứ không thể tự định danh chính xác phiên bản Windows Server 2012 R2 nếu thiếu dữ liệu xác thực cục bộ`

The approved result is narrower:
- **in this measurement**, Nmap returned a Windows Server 2008 R2–2012 fingerprint range;
- those responses were not sufficient to uniquely identify Windows Server 2012 R2.

The R2 wording generalizes into what Nmap can or cannot do in principle.

Required correction:
- bind the sentence to `trong lần đo này`;
- state that the observed remote responses were insufficient for exact unique identification;
- do not generalize tool capability beyond the recorded measurement.

## 6. Product-level assessment

The chapter is close to whole-chapter approval quality.

PASS aspects:
- progression baseline → Scenario 1 → Scenario 2 → Case B → Case C → comparison → conclusion is clear;
- section lengths are reasonably balanced;
- Bảng 3.7 provides useful synthesis without adding a new figure;
- figure/table sequence remains coherent;
- prose is less repetitive and less QA-like than R1;
- no major over-compression occurred;
- no new Chapter 4 recommendation/risk-ranking section appears.

The remaining blockers are not stylistic preferences. They are evidence/topology precision issues introduced during editorial rewriting.

## 7. Reopen decision

No approved source section needs to be reopened.

The source sections remain authoritative and unchanged. These defects were introduced only in `CHAPTER_3_DRAFT_R2.md` by X7H editorial wording. R2 correction must restore the approved technical meaning without modifying any source-section file.

## 8. Gate

Current verdict:

`X7H_R1_REVISE_BLOCKING`

X7I remains BLOCKED.

Run one bounded X7H R2 correction:
1. correct the four wording drifts above;
2. change nothing else unless required by those exact corrections;
3. rerun structural, technical-lock, linter, tests, diff-check and project validation;
4. provide an exact R1-candidate → R2-candidate diff;
5. return for independent whole-chapter review.

Do not create DOCX/PDF.  
Do not edit Chapter 2.  
Do not open Chapter 4.  
Do not declare Chapter 3 user-approved.
