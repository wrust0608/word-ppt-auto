# X7A1 EXTERNAL REVIEW R1 — SECTION 3.1 BASELINE DRAFT

Date: 2026-10-06  
Branch: `feature/x7a1-ch3-baseline-draft`  
Remote candidate HEAD: `9c180faab36738626976665059db507e06954725`  
Verdict: `82/100 — REVISE_BLOCKING`

## 1. Executive verdict

The R1 section is structurally strong and visually much better than the earlier monolithic approach.

PASS:
- scope is clean;
- 1 H2 / 2 H3;
- 2 locked tables;
- 3 locked figures;
- crop manifest is traceable;
- source evidence hashes match the staged SHA ledger;
- no Scenario 1/2, Case B/C or Chapter 4 prose was added.

However, the prose is not ready for user approval because several sentences exceed the evidence boundaries already locked in X7A0 and the citation markers are not valid in the global report context.

The correct action is a focused prose R2, not a redesign.

## 2. Score

| Category | Score |
|---|---:|
| Scope / structure discipline | 15/15 |
| Table/figure presentation | 19/20 |
| Evidence preservation / crop traceability | 15/15 |
| Technical accuracy / bounded interpretation | 14/20 |
| Academic student-facing prose | 14/15 |
| Citation integrity | 7/10 |
| Self-review accuracy | 8/10 |
| **Total** | **82/100** |

Blockers: **technical-boundary wording + citation integrity**.

## 3. PASS — branch and artifact scope

Remote HEAD:
`9c180faab36738626976665059db507e06954725`

Compared with starting HEAD:
`59bb8c3b10c5b671f4d1f96624172846e8535038`

Only the six authorized X7A1 outputs were added:
- `CH3_31_BASELINE_DRAFT_R1.md`
- `CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`
- `CH3_31_BASELINE_CROP_MANIFEST_R1.md`
- three presentation images under `chapter3/presentation/3_1/`.

No source evidence file was modified.

## 4. PASS — derived images

Reviewer independently inspected all three presentation images.

### Hình 3.1
Readable and appropriately cropped.
Preserves:
- Windows IP/route;
- LanmanServer;
- FS-SMB1;
- SMB server flags;
- local 139/445 listeners;
- numeric srv.sys.

### Hình 3.2
Readable and appropriately cropped.
Preserves:
- custom rule;
- TCP 139/445;
- RemoteAddress .56.10;
- profile state;
- default File and Printer Sharing group state.

### Hình 3.3
Readable and appropriately cropped.
Preserves:
- display FileVersion;
- numeric srv.sys;
- six observed hotfix rows.

The Action Center popup is successfully removed.

Source hashes in the crop manifest match `CHAPTER_3_EVIDENCE_SHA256.csv`.

Keep all three derived images unchanged in R2 unless a new visual defect is discovered.

## 5. BLOCKER A — local SMB flags are still converted into negotiation capability

Current prose says, in substance:

`EnableSMB1Protocol=True` and `EnableSMB2Protocol=True` prove the server is ready to negotiate SMBv1 and SMB2/SMB3.

This exceeds the X7A0 lock.

Allowed:
- the two local server-configuration flags are True;
- these are local configuration values.

Do not convert them into:
- successful remote negotiation;
- a remote dialect list;
- proof that SMB3 was negotiated or available in the measured connection.

Recommended wording:
`Hai thuộc tính EnableSMB1Protocol và EnableSMB2Protocol đều có giá trị True, cho biết hai nhóm giao thức tương ứng đang được bật ở mức cấu hình SMB Server. Danh sách dialect thực sự được chấp nhận từ xa được trình bày riêng ở Kịch bản 1.`

In Bảng 3.1, rename:
`Cấu hình phương ngữ SMB cục bộ`
to:
`Cấu hình giao thức SMB Server`.

Do not write `SMB2/SMB3` in the explanatory cell.

## 6. BLOCKER B — remote port state is incorrectly made dependent on a “middle firewall”

Current post-Hình 3.1 paragraph says remote OPEN depends directly on packet-control policy of a “tường lửa trung gian”.

Problems:
- baseline uses Windows Firewall on the target; it is not the Case C transparent middle firewall;
- remote Nmap state depends on the tested path and response behavior, not solely/directly on one firewall statement.

Replace with a bounded sentence:

`Trạng thái lắng nghe cục bộ không tự xác định trạng thái cổng nhìn từ trạm Kali; khả năng tiếp cận từ xa phải được đo riêng qua đường mạng và chính sách lọc hiện hành.`

Do not use `tường lửa trung gian` in baseline.

## 7. BLOCKER C — firewall configuration is repeatedly converted into proven traffic behavior

Current prose contains claims equivalent to:
- disabled default rules prevent automatic opening for the whole network range;
- the custom rule proves SMB traffic from Kali is accepted through the firewall;
- the configuration ensures Kali can interact with SMB;
- the configuration excludes the risk of other devices interfering.

These claims go beyond the configuration screenshot.

Allowed:
- all three profiles are Enabled;
- the 16 displayed File and Printer Sharing rules are disabled;
- the custom rule is Enabled / Inbound / Allow / TCP / LocalPort 139,445 / RemoteAddress .56.10.

Do not claim actual traffic passage until remote measurements are presented.

Required replacement after Hình 3.2:
`Hình 3.2 xác nhận quy tắc tùy biến được cấu hình cho TCP 139/445 với phạm vi địa chỉ nguồn 192.168.56.10, đồng thời nhóm File and Printer Sharing mặc định được ghi nhận ở trạng thái tắt. Đây là trạng thái cấu hình tại baseline; khả năng tiếp cận dịch vụ từ Kali được kiểm tra bằng các phép đo từ xa ở phần tiếp theo.`

## 8. BLOCKER D — patch verification explanation adds unsupported/generalized claims

Current prose says FileVersion is generally a static string from RTM and does not accurately reflect binary changes after small servicing updates.

This is not part of the approved BASE-C11 wording and is an unnecessary generalized Windows claim.

Remove that explanation.

Use only the observed distinction:
- display FileVersion = `6.3.9600.16384`;
- numeric version = `6.3.9600.16421`;
- Microsoft verification threshold = `6.3.9600.18604`.

Also avoid describing MS17-010 as one singular “buffer overflow vulnerability” in this baseline subsection.
Use:
`trạng thái cập nhật liên quan MS17-010`
or
`bản cập nhật khắc phục MS17-010`.

## 9. BLOCKER E — “safe threshold” wording

Current prose calls `6.3.9600.18604`:
`ngưỡng phiên bản an toàn tối thiểu`.

The official support guidance establishes a minimum updated/patched file version, not a general “safe” threshold.

Use:
`ngưỡng phiên bản đã cập nhật tối thiểu`
or
`phiên bản srv.sys tối thiểu đã chứa bản cập nhật tương ứng`.

Do not use `an toàn` for this threshold.

## 10. BLOCKER F — hotfix inventory wording regressed to an absolute claim

Current prose:
`hoàn toàn không xuất hiện KB4012213, KB4012216 hoặc bất kỳ gói cập nhật thay thế nào...`

This violates the bounded wording approved in X7A0.

Use:
`Trong danh mục hotfix quan sát được không ghi nhận KB4012213, KB4012216 hoặc bản cập nhật thay thế đã được ánh xạ là chứa bản sửa lỗi MS17-010.`

Do not claim exhaustive lifetime update history.

## 11. BLOCKER G — snapshot/reproducibility is overclaimed

Current prose contains:
- `bảo đảm tính toàn vẹn và khả năng tái lập`;
- `hoàn nguyên môi trường về trạng thái đồng nhất`.

A snapshot is the defined restore point, but does not by itself prove perfect reproducibility/integrity.

Use:
`Snapshot Before Demo được ghi nhận cho cả hai máy ảo ở trạng thái poweroff và được chọn làm mốc phục hồi của thực nghiệm.`

Do not claim perfect/identical reproduction.

The opening paragraph should also avoid:
`bảo đảm tính lặp lại và tính khách quan cho toàn bộ quá trình đo đạc`.

Prefer:
`tạo mốc tham chiếu nhất quán để đối chiếu các phép đo tiếp theo`.

## 12. Recommended deletion — ICMP paragraph

The ICMP/ARP paragraph is technically bounded, but it does not improve the baseline story enough to justify its space.

Reasons:
- it is absent from Bảng 3.1 by design;
- it distracts from the clearer local-state narrative;
- target availability will be measured cleanly in Scenario 1.

Recommendation:
remove the full ICMP/ARP paragraph from student-facing 3.1.

The internal claim `BASE-C04` remains preserved in the claim map; it simply does not need to appear in prose.

## 13. Citation blocker — [4]/[5] are wrong in the global report context

The R1 self-review says:
- [4] = Microsoft Bulletin MS17-010;
- [5] = Microsoft Support Article 4023262.

This is false in the current global Chapter 1 bibliography.

Current Chapter 1 references are:
- [4] = Microsoft, `SMB security enhancements`;
- [5] = Microsoft, `What is Server Message Block signing?`;
- [7] = Microsoft Security Bulletin MS17-010.

The Microsoft Support source `How to verify that MS17-010 is installed` is registered as `S032` but does not yet have a locked global IEEE number.

Therefore the visible citations `[4]` and `[5]` in Section 3.1 must not survive R2.

### R2 citation strategy

Because the project already has a planned global IEEE normalization gate, do not invent a new final numeric label in X7A1.

In student-facing R2 prose:
- name the Microsoft sources naturally where needed;
- do not place the wrong [4]/[5] markers.

Immediately after the source-dependent sentence, add a non-rendering Markdown comment:

`<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`

This preserves traceability without exposing internal Source IDs in rendered student prose.

Self-review must explicitly state:
- S005 = MS17-010 bulletin;
- S032 = Microsoft support verification guide;
- final numeric IEEE labels are pending global normalization;
- current global [4]/[5] are not used for these claims.

Do not modify Chapter 1 or Chapter 2 citation numbering in X7A1 R2.

## 14. Additional prose refinements

### Table 3.1
Replace:
`Toàn bộ 3 hồ sơ tường lửa Windows đều được kích hoạt bảo vệ`

with:
`Cả ba hồ sơ Windows Firewall đều có Enabled=True`.

### Hình 3.1 commentary
Avoid:
`khả năng sẵn sàng xử lý yêu cầu kết nối nội bộ`
if this is used to imply functional service success.

Prefer:
`các socket 139/445 đang ở trạng thái Listen trên máy chủ`.

### Hình 3.3 commentary
Replace self-evaluative:
`củng cố tính chuẩn xác của phương pháp xác minh kép`

with:
`Hai nhóm dữ liệu này được dùng cùng với ngưỡng Microsoft để phân loại trạng thái bản vá cục bộ.`

### Final transition
Keep one neutral sentence only.
Do not state the system is “ready” as a technical result.

## 15. Self-review defect

The self-review claims:
- no new factual claim beyond BASE-C01..C16;
- 100% wording follows approved boundaries;
- citation [4]/[5] is correct;
- no unresolved technical concern.

Those statements are not accurate.

R2 self-review must acknowledge and verify the actual corrected boundaries rather than self-declare 100% technical perfection.

## 16. R2 acceptance criteria

R2 must preserve:
- exactly 1 H2 / 2 H3;
- exactly 2 tables;
- exactly 3 figures;
- same three presentation images and crop manifest unless a visual defect is found.

R2 must correct:
- local flags -> no remote negotiation inference;
- no “middle firewall” dependency;
- no firewall behavior guarantee;
- no generalized FileVersion/RTM claim;
- no “safe threshold” wording;
- bounded hotfix inventory;
- bounded snapshot wording;
- remove ICMP paragraph;
- no wrong numeric [4]/[5] citations;
- CITE-ANCHOR uses S005/S032 only in non-rendering comment;
- no Chapter 4 leakage.

Desired status:
`X7A1_CH3_31_BASELINE_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`.

X7B remains blocked.
