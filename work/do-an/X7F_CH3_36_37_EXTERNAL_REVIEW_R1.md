# X7F SECTIONS 3.6–3.7 — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7f-ch3-synthesis`  
Executor candidate: `ba09295d24f4a76d726d0f980c630d546204cacc`

Verdict: **82/100 — REVISE_BLOCKING**

## 1. Overall finding

The synthesis structure is correct:
- Section 3.6 compares approved results;
- Section 3.7 closes Chapter 3;
- one comparison table only;
- no new figure;
- no new evidence;
- no ranking/recommendation.

However, R1 reintroduces several technical overclaims that were already corrected and locked in Sections 3.4 and 3.5.

The synthesis is not allowed to become stronger than the approved source sections.

No structural rewrite is required, but a bounded R2 is mandatory.

## 2. What passes

Keep:
- headings `3.6. So sánh kết quả thực nghiệm` and `3.7. Tổng kết chương`;
- no H3;
- one Bảng 3.7;
- no Hình 3.12;
- Case B TCP139 explicitly marked `Không đo lại trong Case B`;
- Case C dialect row explicitly marked `Không có phép đo tương ứng trong Case C`;
- no control ranking;
- no recommendation;
- no Chapter 4 content.

## 3. Blocker A — Case B TCP445 incorrectly inherits `syn-ack`

R1 Bảng 3.7 says for Case B:

`OPEN (Phản hồi syn-ack)`

This is wrong.

Approved Section 3.4 explicitly states:
- Case B retest recorded TCP 445 = OPEN;
- Case B retest did not use `--reason`;
- therefore there is no Case B post-intervention `syn-ack` evidence.

R2 must use:

`OPEN`

only.

The self-review must also be corrected; it currently repeats the same wrong `OPEN (syn-ack)` assertion for Case B.

## 4. Blocker B — dialect wording reintroduces negotiation/workload overclaim

R1 uses phrases such as:
- `chấp thuận đàm phán 5 phương ngữ`;
- `các phương ngữ SMB2 và SMB3 tiếp tục được hỗ trợ đầy đủ`;
- `Case B loại bỏ thành công SMBv1 khỏi danh sách đàm phán`;
- `làm thay đổi tập phương ngữ mà dịch vụ chấp thuận`.

These were explicitly narrowed in approved Section 3.4.

Allowed synthesis wording:
- baseline `smb-protocols` **ghi nhận** five dialect values;
- after Case B, `smb-protocols` **ghi nhận** `2.0.2`, `2.1`, `3.0`, `3.0.2`;
- `NT LM 0.12 (SMBv1)` **không xuất hiện trong danh sách phương ngữ của phép đo lại**.

Do not say:
- successful negotiation;
- accepted dialects;
- full SMB2/3 support;
- workload compatibility;
- "successfully removed" as a stronger causal/functional conclusion.

## 5. Blocker C — Case B TCP445 causal wording exceeds evidence

R1 says:
- `Cổng 445 mở trong Case B để phục vụ SMB2/3`;
- `Cổng TCP 445 duy trì trạng thái mở do dịch vụ LanmanServer tiếp tục vận hành...`

The approved Section 3.4 does not establish why TCP 445 was OPEN.

R2 must use observation-only wording:

`Trong phép đo lại Case B, TCP 445 được ghi nhận OPEN.`

Do not attribute the OPEN state to LanmanServer or SMB2/3 service operation.

## 6. Blocker D — Case B local listeners are synthesized beyond the approved Section 3.4 output

Bảng 3.7 currently states that local listeners 139/445 are present in Case B.

The approved Section 3.4/user lock directly carries:
- LanmanServer=Running;
- TCP445 remote OPEN;
- SMB1/SMB2 configuration;
- FS-SMB1;
- dialect retest;
- patch state;
- MS17 UNKNOWN.

It does not lock a Case B local-listener 139/445 comparison row for synthesis.

X7F may use only approved Section 3.1–3.5 outputs.

R2:
- change this comparison criterion to `LanmanServer cục bộ` only; or
- if keeping listener wording, write `Không tổng hợp phép đo listener cục bộ tương ứng trong Mục 3.4` for Case B.

Preferred for a compact table:
use a row named `LanmanServer cục bộ`:
- Baseline: Running;
- Case B: Running at the recorded check;
- Case C: Running at the recorded final state.

Do not invent continuity or local listener measurements for Case B.

## 7. Blocker E — point-in-time states are rewritten as continuous unchanged states

Examples:
- `Dịch vụ máy chủ và các cổng lắng nghe cục bộ tiếp tục duy trì trong mọi kịch bản`;
- `trạng thái nội bộ ... không thay đổi`;
- `giữ nguyên trạng cấu hình và dịch vụ của máy chủ đích`.

These formulations are too absolute.

Use recorded-state language:
- `LanmanServer được ghi nhận Running tại các mốc được kiểm tra`;
- Case C final metadata records SMB1=True, SMB2=True, LanmanServer=Running, local listeners present and UNPATCHED;
- no Case C SMB configuration or patch action is recorded.

Do not imply:
- continuous uptime;
- no transient state change;
- omniscient whole-history continuity.

## 8. Blocker F — patch/binary causality is overstated

R1 says:
- disabling SMBv1 `không can thiệp tệp nhị phân hệ thống; do đó` srv.sys remains UNPATCHED;
- both interventions `không làm thay đổi phân loại bản vá nhị phân`;
- filtering `hoàn toàn không sửa đổi mã nguồn hay vá lỗi`.

Problems:
- the evidence is no recorded patch-install action + approved UNPATCHED classification;
- `mã nguồn` is technically wrong in this context;
- the synthesis should not claim direct binary-causality from the intervention.

Use:
`Trạng thái bản vá vẫn được phân loại UNPATCHED; Case B/Case C không ghi nhận thao tác cài bản vá.`

Keep:
- `SMBv1 disabled != PATCHED`;
- `FILTERED != PATCHED`.

Do not claim exact binary-history change/non-change beyond the approved provenance.

## 9. Blocker G — Case C is written as stronger causal proof than approved Section 3.5

R1 says:
- pfSense intervention makes ports "chuyển" to FILTERED;
- filtering "ngăn chặn sự tiếp cận";
- remote state is "thuần" a result of pfSense in effect.

Approved Section 3.5 uses a bounded cross-layer comparison:
- Kali records 139/445 FILTERED/no-response;
- pfSense logs record matching SMB SYN traffic as Block;
- this is cross-layer comparison;
- exact named-rule attribution remains unresolved.

R2 should preserve that bounded form.

Allowed:
`Trong Case C, từ trạm Kali, TCP 139/445 được ghi nhận FILTERED/no-response; đồng thời pfSense ghi nhận matching SMB SYN traffic bị Block trên đường thử nghiệm.`

Do not make a universal causal claim about every possible path or mechanism.

## 10. Blocker H — UNKNOWN receives a causal explanation again

R1 uses:
- `UNKNOWN do kịch bản kiểm tra không thu được phản hồi khả dụng...`;
- Section 3.7: `UNKNOWN do thiếu dữ kiện phản hồi khả dụng`.

The approved Sections 3.3–3.5 deliberately avoid assigning a cause.

Use:
`Phép đo không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT.`

If needed:
`Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có.`

Do not use `do...` causal wording.

## 11. Blocker I — Section 3.7 overstates Case B and Case C

Current:
- `Case B loại bỏ phương ngữ NT LM 0.12...`;
- `Case C đưa cả hai cổng 139 và 445 về trạng thái FILTERED...`.

Use direct observation wording:

Case B:
`Sau Case B, NT LM 0.12 không xuất hiện trong danh sách phương ngữ của phép đo lại, trong khi TCP 445 vẫn được ghi nhận OPEN.`

Case C:
`Trong Case C, TCP 139 và 445 được ghi nhận FILTERED/no-response từ trạm Kali.`

This closes the chapter without making stronger intervention-causality claims.

## 12. Product-level table issue — Bảng 3.7 should be 4 columns, not 5

The current 5-column table duplicates interpretation already explained in prose and will be unnecessarily dense in A4 portrait layout.

R2 should use a more readable 4-column comparison table:

`Tiêu chí so sánh | Đường cơ sở / Kịch bản 1–2 | Case B — Vô hiệu hóa SMBv1 | Case C — Kiểm soát bằng pfSense`

Remove the fifth `Nhận xét thực nghiệm` column.

Move only essential interpretation to the short prose after the table.

Keep the 8 comparison row families, but make cells concise.

This is an editorial/presentation correction only; it does not change technical meaning or numbering.

## 13. Recommended corrected Bảng 3.7 content

### Lớp can thiệp
Baseline:
`Không có can thiệp Case B/Case C; môi trường Host-Only theo đường cơ sở`

Case B:
`Cấu hình SMBv1 trên Windows Server`

Case C:
`Đường thử nghiệm Kali → Windows qua pfSense Transparent Bridge`

### TCP139 remote
Baseline:
`OPEN (syn-ack)`

Case B:
`Không đo lại trong Case B`

Case C:
`FILTERED (no-response)`

### TCP445 remote
Baseline:
`OPEN (syn-ack)`

Case B:
`OPEN`

Case C:
`FILTERED (no-response)`

### SMB dialects
Baseline:
`NT LM 0.12, 2.0.2, 2.1, 3.0, 3.0.2`

Case B:
`2.0.2, 2.1, 3.0, 3.0.2; NT LM 0.12 không xuất hiện`

Case C:
`Không có phép đo tương ứng trong Case C`

### SMB1 local
Baseline:
`True`

Case B:
`False`

Case C:
`True`

### LanmanServer local
Baseline:
`Running`

Case B:
`Running (tại thời điểm kiểm tra)`

Case C:
`Running (trạng thái ghi nhận cuối lượt)`

### Patch state
Baseline:
`UNPATCHED`

Case B:
`UNPATCHED; không ghi nhận thao tác cài patch`

Case C:
`UNPATCHED; không ghi nhận thao tác cài patch`

### Remote MS17
All three:
`UNKNOWN / NO USABLE SCRIPT RESULT`

Do not add causes.

## 14. Section 3.6 prose target

Keep 3.6 concise:
- approximately **650–800 prose words** after correction;
- table handles the direct state comparison;
- prose explains only:
  1. baseline vs Case B;
  2. baseline vs Case C;
  3. Case B vs Case C;
  4. the key inference boundaries.

Do not repeat every table cell.

## 15. Section 3.7 prose target

Keep:
- approximately **230–330 words**.

Use natural conclusion language.

Avoid:
- `chứng minh được` when `ghi nhận/xác lập trong phạm vi phép đo` is sufficient;
- general claims about limitations of all automated tools;
- active opening of Chapter 4.

Preferred final idea:
the chapter closes the empirical measurement scope; further analysis is outside the current Chapter 3 scope.

## 16. R2 scope

Modify only:
- `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- `work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`

No new file except R2 commit metadata.
No figure.
No evidence.
No Chapter 3 assembly.
No Word.
No Chapter 2/4 edits.

## 17. Final gate

Current verdict:

`X7F_CH3_36_37_R1_REVISE_BLOCKING`

After R2:
- independently compare every Bảng 3.7 cell with the approved Sections 3.1–3.5;
- check for regenerated overclaims;
- if clean, issue final external PASS and wait for explicit user approval before X7G assembly.
