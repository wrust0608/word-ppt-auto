# X7E1 R2 — CORRECT SECTION 3.5 CASE C

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7e1-ch3-casec-draft`  
R1 candidate: `7ab6b9ad20f8a91b3d137a1f36b3af8c70a0d66d`

## 0. Objective

Apply a bounded R2 correction to Section 3.5 based on:

`work/do-an/X7E1_CH3_35_EXTERNAL_REVIEW_R1.md`

Do not redesign Case C.

Keep:
- 1 H2 / 2 H3;
- Bảng 3.6;
- Hình 3.9–3.11;
- current evidence allocation;
- rule-label conflict disclosure.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7e1-ch3-casec-draft
git pull --ff-only origin feature/x7e1-ch3-casec-draft
git status --short
git rev-parse HEAD
```

The branch must contain:
- `X7E1_CH3_35_EXTERNAL_REVIEW_R1.md`;
- this R2 prompt.

Read the review fully.

## 2. Allowed modifications

Modify only:
- `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
- `work/do-an/CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`

Do not modify:
- Hình 3.9;
- Hình 3.10;
- Hình 3.11;
- raw evidence;
- approved X7E0 plan;
- infrastructure;
- Chapter 2;
- other Chapter 3 sections.

## 3. Remove NSE04 causal explanation

Delete any sentence equivalent to:

`không đưa ra phán quyết lỗ hổng do lưu lượng bị chặn`

or:
- because pfSense blocked the traffic;
- because 445 was filtered;
- script could not run/interact.

Use exactly the bounded logic:

`Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.`

Then:
`UNKNOWN != SAFE`.

## 4. Correct Windows/local-state overclaims

Remove wording equivalent to:
- `mã nhị phân máy chủ không tiếp nhận bất kỳ thay đổi nào`;
- `thuần túy là kết quả kiểm soát mạng của pfSense`;
- omniscient/continuous-history statements.

Use:

`Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Trạng thái ghi nhận cuối lượt Case C cho thấy SMB1=True, SMB2=True, LanmanServer=Running, listener cục bộ 139/445 hiện diện và trạng thái bản vá vẫn được phân loại UNPATCHED.`

For cross-layer result:

`Các quan sát FILTERED từ Kali được đối chiếu với các bản ghi Block tương ứng trên pfSense; việc này không làm thay đổi phân loại bản vá cục bộ của máy chủ.`

Do not say pfSense is the exclusive proven cause at every possible network layer/path.

## 5. Keep Hình 3.11 crop but fix how it is described

Keep the current derived image:
`Hinh_3_11_pfSense_Block_Log.png`

Current crop:
`x=40,y=15355,w=1280,h=220`.

Do not create a montage.
Do not alter the image.

The crop contains the four relevant log rows and Rule field but **does not contain the original table-heading row**.

Before the figure or immediately after introducing it, add a concise reading guide:

`Trong các dòng log được trích, các trường lần lượt thể hiện hành động xử lý, thời điểm, giao diện, nhãn quy tắc, địa chỉ nguồn, địa chỉ đích và giao thức.`

Then state the observed values.

Update crop manifest:
- remove any claim that column headings are preserved in the crop;
- explicitly say header row is outside the tight crop;
- state that field interpretation was checked against the full original source screenshot;
- no content/labels were added to the derived image.

## 6. Simplify Hình 3.9 rule-order paragraph

Keep:
- Block row displayed above Pass row.

Remove predictive/tutorial wording such as:

`các gói tin ... sẽ khớp ... và bị chặn trước...`

Preferred:

`Hình 3.9 cho thấy quy tắc Block SMB_Ports được đặt phía trên quy tắc Pass baseline. Hình này xác nhận cấu hình và thứ tự hiển thị của ruleset; kết quả xử lý lưu lượng được đối chiếu bằng phép đo Nmap và nhật ký pfSense ở Mục 3.5.2.`

Do not turn Chapter 3 into a pfSense rule-processing lesson.

## 7. Fix ARP sentence

Replace wording equivalent to:

`arp-response xác nhận kết nối thông suốt qua bridge0`

with:

`Kết quả Nmap ghi nhận mục tiêu ở trạng thái up với arp-response trong topology Case C.`

The path through bridge0 comes from topology/configuration evidence.

## 8. Make student-facing provenance natural

Replace internal wording where possible:

- `manifest` -> `tệp ghi nhận lượt chạy Case C` when discussing the rule-label discrepancy;
- `báo cáo kiểm toán tiến trình` -> `trạng thái/metadata ghi nhận cuối lượt Case C`;
- `point-in-time` -> `trạng thái ghi nhận tại thời điểm kiểm tra`.

Do not hide provenance; just make the report readable to a lecturer.

## 9. Compress Bảng 3.6

Keep:
- 4 columns;
- 10 rows;
- title unchanged.

Shorten the fourth column.

Each cell should normally contain one compact result/boundary.

Suggested style:

- architecture:
  `Đường thử nghiệm Case C được bố trí qua pfSense Transparent Bridge.`
- policy:
  `Ruleset chặn TCP 139/445 từ Kali tới Windows, có ghi log.`
- order:
  `Block được hiển thị trên Pass.`
- TCP139:
  `FILTERED/no-response từ Kali; không suy ra cổng local đã đóng.`
- TCP445:
  `FILTERED/no-response từ Kali; FILTERED != PATCHED.`
- log:
  `Matching SMB SYN traffic được ghi nhận Block; không quy thuộc tuyệt đối theo tên rule.`
- MS17:
  `Không có phán quyết usable; UNKNOWN != SAFE.`
- SMB1:
  `Metadata cuối Case C ghi nhận True; không có thao tác đổi SMB.`
- service/listeners:
  `LanmanServer=Running, listeners 139/445 hiện diện tại thời điểm kiểm tra.`
- patch:
  `Vẫn phân loại UNPATCHED; không ghi nhận thao tác cài patch.`

Do not repeat the same long explanation in table and prose.

## 10. Compress the prose

Target:
- **1,300–1,450 prose words**;
- preserve 15 or fewer natural paragraphs;
- do not delete essential rule-label disclosure;
- do not delete technical boundaries.

Focus prose on:
`setup/control -> observed FILTERED -> pfSense log -> UNKNOWN -> local-state distinction -> conclusion`.

## 11. Make conclusion less grandiose

Avoid:
- `khẳng định nguyên lý phương pháp luận`;
- `trạng thái an ninh của dịch vụ` if the evidence is only configuration/service/patch state.

Prefer:

`Kết quả Case C cho thấy trạng thái quan sát từ xa trên đường mạng và trạng thái bản vá cục bộ là hai lớp thông tin khác nhau: TCP 139/445 được ghi nhận FILTERED từ Kali, trong khi máy chủ vẫn được phân loại UNPATCHED.`

Then transition to 3.6.

## 12. Required searches

Search draft/self-review/manifest for:

- `do lưu lượng bị chặn`
- `do cổng 445`
- `script không thể`
- `thuần túy là kết quả`
- `mã nhị phân máy chủ không tiếp nhận bất kỳ thay đổi`
- `bảo đảm tính trong suốt`
- `xác nhận kết nối thông suốt qua cầu nối`
- `point-in-time`
- `báo cáo kiểm toán tiến trình`
- `khẳng định nguyên lý phương pháp luận`

Problematic uses should be zero.

The word `manifest` may remain only inside internal self-review/manifest artifacts if needed; prefer no naked `manifest` in student-facing prose.

## 13. QA

Run:

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_35_CASEC_DRAFT_R1.md
git diff --check
```

Optionally run project validation.

Do not modify infrastructure.

Verify all three image SHAs remain unchanged.

## 14. Git

Commit:

`fix(ch3): correct Case C section 3.5 R2`

Push:

`feature/x7e1-ch3-casec-draft`

Do not merge.

## 15. Handoff

Return:
1. starting reviewer HEAD;
2. final local/remote SHA;
3. changed files;
4. prose word/paragraph count;
5. NSE04 boundary fix;
6. Windows-state wording fix;
7. Hình 3.11 header/presentation fix;
8. rule-order simplification;
9. ARP wording fix;
10. Bảng 3.6 compression summary;
11. student-facing jargon cleanup;
12. problematic-string audit;
13. unchanged image SHA audit;
14. QA;
15. clean git status.

Final state:

`X7E1_CASEC_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not write 3.6/3.7.
Do not assemble Chapter 3.
Do not build Word.
