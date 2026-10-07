# X7F R2 — CORRECT SECTIONS 3.6 AND 3.7

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7f-ch3-synthesis`  
R1 candidate: `ba09295d24f4a76d726d0f980c630d546204cacc`

## 0. Objective

Apply a bounded R2 correction to Sections 3.6 and 3.7 based on:

`work/do-an/X7F_CH3_36_37_EXTERNAL_REVIEW_R1.md`

Do not redesign Chapter 3.

Keep:
- Section 3.6;
- Section 3.7;
- Bảng 3.7;
- no H3;
- no new figure;
- no new evidence.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7f-ch3-synthesis
git pull --ff-only origin feature/x7f-ch3-synthesis
git status --short
git rev-parse HEAD
```

The branch must contain:
- `X7F_CH3_36_37_EXTERNAL_REVIEW_R1.md`;
- this R2 prompt.

Read the external review fully.

Then reread the approved:
- `CH3_31_BASELINE_DRAFT_R1.md`
- `CH3_32_SCENARIO1_DRAFT_R1.md`
- `CH3_33_SCENARIO2_DRAFT_R1.md`
- `CH3_34_CASEB_DRAFT_R1.md`
- `CH3_35_CASEC_DRAFT_R1.md`

The synthesis must never be stronger than these approved source sections.

## 2. Allowed modifications

Modify only:
- `work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md`
- `work/do-an/CH3_36_37_SYNTHESIS_SELF_REVIEW_R1.md`

No other file may change.

## 3. Fix Case B TCP445

In Bảng 3.7 and self-review:

Case B TCP445 must be:

`OPEN`

NOT:

`OPEN (syn-ack)`

Reason:
Case B retest did not use `--reason`.

Search and ensure no Case B post-intervention `syn-ack` remains anywhere.

Baseline may retain:
`OPEN (syn-ack)`.

Case C may retain:
`FILTERED (no-response)`.

## 4. Remove negotiation/support overclaims

Remove wording such as:
- `chấp thuận đàm phán 5 phương ngữ`;
- `được hỗ trợ đầy đủ`;
- `loại bỏ thành công SMBv1`;
- `dịch vụ chấp thuận`.

Use:
- `smb-protocols ghi nhận...`;
- `NT LM 0.12 không xuất hiện trong danh sách phương ngữ của phép đo lại`.

Do not claim:
- handshake success;
- successful negotiation;
- complete workload support;
- protocol removal beyond the observed list.

## 5. Remove Case B TCP445 cause

Delete:
- `Cổng 445 mở ... để phục vụ SMB2/3`;
- `Cổng 445 ... do LanmanServer...`;
- equivalent causal wording.

Use:
`Trong phép đo lại Case B, TCP 445 được ghi nhận OPEN.`

Nothing more is required.

## 6. Fix local-service/listener comparison

Do not state Case B local listeners 139/445 as if Section 3.4 locked that comparison.

Preferred Bảng 3.7 row:

`LanmanServer cục bộ`

- Baseline: `Running`
- Case B: `Running (tại thời điểm kiểm tra)`
- Case C: `Running (trạng thái ghi nhận cuối lượt)`

If you keep a listener row, Case B must say:
`Không có phép đo listener cục bộ tương ứng được tổng hợp trong Mục 3.4`.

Preferred: remove listener from this row and compare LanmanServer only.

## 7. Fix point-in-time / continuity language

Remove:
- `duy trì trong mọi kịch bản`;
- `trạng thái nội bộ không thay đổi`;
- `giữ nguyên trạng cấu hình và dịch vụ`;
- equivalent continuous-history claims.

Use:
- `được ghi nhận ... tại thời điểm kiểm tra`;
- `trạng thái ghi nhận cuối lượt Case C...`;
- `Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài patch`.

## 8. Fix patch/binary wording

Remove:
- `không can thiệp tệp nhị phân; do đó...`;
- `không làm thay đổi phân loại bản vá nhị phân`;
- `không sửa đổi mã nguồn`;
- any binary-history causal claim.

Use:

`Trạng thái bản vá vẫn được phân loại UNPATCHED; Case B/Case C không ghi nhận thao tác cài bản vá.`

Keep:
- `SMBv1 disabled != PATCHED`
- `FILTERED != PATCHED`

## 9. Bound Case C comparison

Use:

`Trong Case C, từ trạm Kali, TCP 139/445 được ghi nhận FILTERED/no-response; đồng thời pfSense ghi nhận lưu lượng SMB SYN tương ứng bị Block trên đường thử nghiệm.`

Do not say:
- pfSense universally caused all remote states;
- the intervention proves an exclusive cause;
- every possible path is blocked.

Do not reopen the rule-label conflict in detail.

If mentioning the log:
`matching SMB SYN traffic was recorded as Block`.

Do not name the exact matched rule.

## 10. Remove causal explanation from UNKNOWN

Replace all forms such as:
- `UNKNOWN do...`;
- `do thiếu dữ kiện phản hồi...`;
- `do kịch bản không thu được...`.

Use:

`Phép đo không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT.`

If needed:

`Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có.`

Keep:
`UNKNOWN != SAFE`.

## 11. Correct Section 3.7 intervention wording

Case B:
use:
`Sau Case B, NT LM 0.12 không xuất hiện trong danh sách phương ngữ của phép đo lại, trong khi TCP 445 vẫn được ghi nhận OPEN.`

Case C:
use:
`Trong Case C, TCP 139 và 445 được ghi nhận FILTERED/no-response từ trạm Kali.`

Do not write:
- `Case B loại bỏ...`;
- `Case C đưa ... về FILTERED`.

## 12. Redesign Bảng 3.7 for A4 readability

Keep:
- title unchanged;
- 8 row families.

Change from 5 columns to 4 columns:

`Tiêu chí so sánh | Đường cơ sở / Kịch bản 1–2 | Case B — Vô hiệu hóa SMBv1 | Case C — Kiểm soát bằng pfSense`

Remove:
`Nhận xét thực nghiệm`.

Interpretation belongs in the prose after the table.

Use concise cells.

Recommended content:

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
Baseline:
`UNKNOWN / NO USABLE SCRIPT RESULT`

Case B:
`UNKNOWN / NO USABLE SCRIPT RESULT`

Case C:
`UNKNOWN / NO USABLE SCRIPT RESULT`

No causes.

## 13. Section 3.6 prose

Target:
- approximately **650–800 prose words**.

Flow:
1. short synthesis opening;
2. Bảng 3.7;
3. baseline vs Case B;
4. baseline vs Case C;
5. Case B vs Case C;
6. concise inference boundaries.

Do not narrate the table row-by-row.

## 14. Section 3.7 prose

Target:
- approximately **230–330 words**.

Keep it a chapter conclusion.

Use:
- `ghi nhận`;
- `trong phạm vi phép đo`;
- `không cung cấp phán quyết khả dụng`.

Avoid:
- `chứng minh tuyệt đối`;
- general claims about all automated scanning tools;
- recommendations;
- active Chapter 4 opening.

## 15. Required searches

Search draft + self-review for:

- `Case B.*syn-ack`
- `chấp thuận đàm phán`
- `hỗ trợ đầy đủ`
- `loại bỏ thành công`
- `để phục vụ SMB2/3`
- `do dịch vụ LanmanServer`
- `duy trì trong mọi kịch bản`
- `trạng thái nội bộ.*không thay đổi`
- `giữ nguyên trạng`
- `không can thiệp tệp nhị phân`
- `mã nguồn`
- `UNKNOWN do`
- `do thiếu dữ kiện`
- `do kịch bản kiểm tra`
- `Case B loại bỏ`
- `Case C đưa`

Problematic uses must be zero.

## 16. Self-review

Update self-review to explicitly audit:
- Case B TCP445 = OPEN only;
- Case B TCP139 = not remeasured;
- Case C dialects = no corresponding measurement;
- Case B local listener state not invented;
- no negotiation/workload overclaim;
- no UNKNOWN cause;
- no point-in-time -> continuous-state overclaim;
- no binary-history inference;
- Bảng 3.7 now 4 columns × 8 row families;
- no ranking/recommendation;
- no new evidence;
- no Chapter 4 leakage.

Do not self-declare external PASS.

## 17. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md
git diff --check
```

Do not modify infrastructure.

## 18. Git

Commit:

`fix(ch3): correct sections 3.6 and 3.7 R2`

Push:

`feature/x7f-ch3-synthesis`

Do not merge.

## 19. Handoff

Return:
1. starting reviewer HEAD;
2. final local/remote SHA;
3. changed files;
4. 3.6 word count;
5. 3.7 word count;
6. corrected Bảng 3.7 shape/rows;
7. Case B TCP445/syn-ack audit;
8. Case B unmeasured-data audit;
9. dialect wording audit;
10. UNKNOWN cause audit;
11. point-in-time/local-state audit;
12. patch/binary wording audit;
13. no-ranking/no-recommendation audit;
14. QA;
15. clean git status.

Final state:

`X7F_CH3_36_37_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not assemble Chapter 3.
Do not build Word.
Do not modify Chapter 2.
Do not open Chapter 4.
