# X7E1 SECTION 3.5 CASE C — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7e1-ch3-casec-draft`  
Executor candidate: `7ab6b9ad20f8a91b3d137a1f36b3af8c70a0d66d`

Verdict: **86/100 — REVISE_BLOCKING**

## 1. Overall finding

R1 is technically close and the approved presentation strategy remains valid.

Keep:
- 1 H2 / 2 H3;
- Bảng 3.6;
- Hình 3.9;
- Hình 3.10;
- Hình 3.11;
- no Hình 3.12;
- the rule-label discrepancy disclosure;
- the FILTERED / UNKNOWN / UNPATCHED distinction.

No experiment rerun or structural redesign is required.

R2 is needed because:
1. one NSE04 sentence explicitly reintroduces the prohibited causal explanation;
2. several Windows/local-state sentences overstate continuity or binary-history knowledge;
3. Hình 3.11 does not contain column headers although the locked crop requirement expected them;
4. the first-match paragraph and some cross-layer language are stronger than necessary;
5. Bảng 3.6 and surrounding prose are still too verbose for the final A4 report.

## 2. What passes

### Hình 3.9 — PASS
Crop `x=15,y=190,w=470,h=340` is readable and preserves:
- CASE_C_KALI context;
- rules heading;
- Block row;
- Pass row.

### Hình 3.10 — PASS
Crop `x=195,y=120,w=660,h=505` clearly preserves:
- command;
- host up / arp-response;
- 139 FILTERED/no-response;
- 445 FILTERED/no-response;
- MAC;
- Nmap done.

### Hình 3.11 — PASS for evidence content, REVISE for presentation description
Crop `x=40,y=15355,w=1280,h=220` correctly preserves:
- four Block rows;
- CASE_C_KALI;
- source/destination/ports;
- TCP:S;
- the conflicting Rule label.

It does **not** preserve the column-heading row.

The source header is far away in the long screenshot. Do not create a montage/composite and do not make an unreadably tall crop merely to include it.

R2 should retain this crop and make its interpretation explicit in prose/manifest.

## 3. Blocker A — prohibited NSE04 causal explanation remains

Current draft says:

> `Phép đo từ xa không đưa ra phán quyết lỗ hổng do lưu lượng bị chặn...`

This directly violates the locked boundary.

The evidence establishes:
- TCP 445 FILTERED;
- no usable script verdict;
- pfSense logs corresponding SMB SYN Block events.

It does not establish the internal reason the script produced no result.

Required wording:

`Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.`

Then, separately:
`UNKNOWN != SAFE`.

Delete:
- `do lưu lượng bị chặn`;
- any equivalent script-internal causal explanation.

## 4. Blocker B — Windows/binary continuity is overstated

Examples in R1:

> `cấu hình dịch vụ và mã nhị phân máy chủ không tiếp nhận bất kỳ thay đổi nào`

> `việc lưu lượng bị lọc từ xa thuần túy là kết quả kiểm soát mạng của pfSense`

These are stronger than the evidence.

The supported facts are:
- no Case C SMB-configuration action is recorded;
- no Case C patch-install action is recorded;
- final Case C metadata records SMB1=True, SMB2=True, LanmanServer=Running, local listeners 139/445, UNPATCHED;
- network observations and pfSense logs are cross-layer observations.

Required:
- replace binary-history/absolute wording with recorded-action + point-in-time wording;
- do not say "thuần túy là kết quả" as absolute causality.

Preferred concept:

`Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Metadata cuối lượt Case C ghi nhận SMB1=True, SMB2=True, LanmanServer=Running, listener 139/445 hiện diện và trạng thái bản vá UNPATCHED.`

And:

`Các quan sát từ xa được đối chiếu với các bản ghi Block tương ứng trên pfSense; điều này không làm thay đổi phân loại bản vá cục bộ của máy chủ.`

## 5. Blocker C — Hình 3.11 header requirement is impossible with a single readable crop and must be handled honestly

The derived Hình 3.11 contains the four relevant rows but no column headings.

Do not:
- claim the crop preserves the column headings;
- create a stitched image/montage;
- crop a 15,000-pixel-tall image;
- add artificial labels onto the evidence image.

Keep the current crop.

Before Hình 3.11, add a concise reading guide based on the source UI, e.g.:

`Trong các dòng log được trích, các trường lần lượt cho biết hành động xử lý, thời điểm, giao diện, nhãn quy tắc, địa chỉ nguồn, địa chỉ đích và giao thức.`

Then state the observed values.

Update the crop manifest:
- explicitly say the crop preserves the four relevant rows and Rule field;
- explicitly say the column-heading row is outside this tight crop;
- the interpretation is tied to the original source UI and verified source image;
- no visual content is invented.

This is more academically honest than a montage.

## 6. Blocker D — first-match paragraph over-explains/predicts the result

Current draft says:

> `Do bộ lọc pf áp dụng nguyên tắc so khớp từ trên xuống ... các gói tin ... sẽ khớp ... và bị chặn...`

The Section 3.5 result chapter does not need to predict traffic behavior before showing the measured result.

R2:
- retain the direct observation that the Block row is displayed above the Pass row;
- remove or greatly shorten the predictive first-match sentence;
- use later Nmap/log evidence to establish what was actually observed.

Preferred:

`Hình 3.9 cho thấy quy tắc Block SMB_Ports được đặt phía trên quy tắc Pass baseline. Hình này xác nhận cấu hình và thứ tự hiển thị của ruleset; kết quả xử lý lưu lượng được đối chiếu bằng phép đo Nmap và nhật ký pfSense ở Mục 3.5.2.`

This is enough.

## 7. Blocker E — ARP wording should not make the Nmap line alone prove the entire bridge path

Current:

> `Host is up, received arp-response ... xác nhận kết nối thông suốt qua cầu nối bridge0.`

Use:

`Kết quả Nmap ghi nhận mục tiêu ở trạng thái up với arp-response trong topology Case C.`

The bridge path itself is established by the Case C topology/configuration evidence, not by the ARP line alone.

## 8. Blocker F — internal QA vocabulary is leaking into student-facing prose

Current prose uses:
- `manifest`;
- `báo cáo kiểm toán tiến trình`;
- `point-in-time`.

For internal review these are fine, but the student-facing report should be more natural.

Required:
- rule-label disclosure may refer to `tệp ghi nhận lượt chạy Case C` instead of naked internal term `manifest`;
- local-state provenance may say `metadata/trạng thái ghi nhận cuối lượt Case C`;
- replace English `point-in-time` with a natural Vietnamese phrase such as `trạng thái ghi nhận tại thời điểm kiểm tra`.

Do not hide provenance; make it readable.

## 9. Blocker G — Bảng 3.6 is correct but too dense for A4

The 4-column / 10-row structure is approved and must remain.

However, the current fourth column contains long multi-sentence explanations. In final A4 layout this risks becoming a very tall, dense table.

R2:
- keep all 10 rows;
- shorten each "Diễn giải trực tiếp & Giới hạn kết luận" cell to the minimum useful statement;
- avoid repeating the same boundary in table + prose + conclusion;
- use one concise phrase/sentence per cell where possible.

Examples:
- TCP 139: `FILTERED/no-response từ Kali; không suy ra cổng local đã đóng.`
- TCP 445: `FILTERED/no-response từ Kali; FILTERED != PATCHED.`
- MS17: `Không có phán quyết usable; UNKNOWN != SAFE.`
- local SMB1: `Metadata cuối Case C ghi nhận True; không có thao tác đổi cấu hình SMB.`
- patch: `Vẫn phân loại UNPATCHED; Case C không ghi nhận thao tác cài patch.`

The table should compress the section, not duplicate it.

## 10. Blocker H — whole-section compression

R1 has 1,571 prose words, at the upper edge of the allowed range, plus a large 10-row table.

Target R2:
- approximately **1,300–1,450 prose words**;
- preserve all technical facts;
- remove repeated explanation already carried by Bảng 3.6;
- keep the rule-label discrepancy concise;
- keep one concise section conclusion.

This is important because Sections 3.1–3.4 are already substantial and the final Chapter 3 must not read like an internal audit record.

## 11. Minor wording improvements

Prefer:
- `môi trường thử nghiệm` over `môi trường lab`;
- `trạng thái cục bộ` rather than `trạng thái an ninh của dịch vụ máy chủ` when the evidence is only configuration/service/patch observations;
- `kết quả cho thấy` rather than `khẳng định nguyên lý phương pháp luận`.

Avoid over-grand conclusions.

## 12. R2 scope

Keep unchanged:
- section structure;
- Bảng 3.6 row families;
- Hình 3.9–3.11 numbering;
- Hình 3.9 and 3.10 crops;
- Hình 3.11 current crop bytes unless regeneration is required for byte-identical output;
- source evidence.

Modify only:
- `work/do-an/CH3_35_CASEC_DRAFT_R1.md`
- `work/do-an/CH3_35_CASEC_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_35_CASEC_CROP_MANIFEST_R1.md`

Do not add figures.
Do not write 3.6/3.7.
Do not build Word.

## 13. Final gate

Current verdict:

`X7E1_CASEC_DRAFT_R1_REVISE_BLOCKING`

After R2:
- independently reread the entire Section 3.5;
- recheck Hình 3.11 interpretation;
- recheck raw Nmap/NSE04 and local-state provenance;
- if clean, issue final external PASS and wait for user approval.
