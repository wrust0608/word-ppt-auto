# X7A1 R2 — CORRECT SECTION 3.1 BASELINE DRAFT

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x7a1-ch3-baseline-draft`

## 0. Objective

Perform a focused prose correction of Section 3.1.

Do not redesign the approved tables/figures.
Do not reopen X7A0.
Do not open X7B.

Read first:
`origin/main:work/do-an/X7A1_CH3_31_EXTERNAL_REVIEW_R1.md`

## 1. Start

```bash
git fetch origin
git checkout feature/x7a1-ch3-baseline-draft
git pull --ff-only origin feature/x7a1-ch3-baseline-draft
git status --short
git rev-parse HEAD
```

Expected R1 HEAD:
`9c180faab36738626976665059db507e06954725`

Record it as the R2 base.

## 2. Files allowed to modify

Modify only:
- `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- `work/do-an/CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1.md`

Do not modify:
- crop manifest;
- three presentation images;
- source evidence;
- approved X7A0 planning files;
- Chapter 1;
- Chapter 2;
- Chapter 3 governance files.

## 3. Preserve locked structure

Keep exactly:
- 1 H2;
- 2 H3;
- Bảng 3.1;
- Bảng 3.2;
- Hình 3.1;
- Hình 3.2;
- Hình 3.3.

Do not renumber.

## 4. Opening paragraph

Replace language that claims baseline guarantees objectivity/reproducibility.

Use the idea:
`baseline provides a consistent reference point for comparison with subsequent measurements`.

Do not say:
- bảo đảm tính khách quan;
- bảo đảm tính lặp lại;
- perfect reproducibility.

## 5. Section 3.1.1 corrections

### Remove ICMP/ARP paragraph from student-facing prose

Delete the full paragraph about:
- ARP REACHABLE;
- 100% ICMP loss.

Do not replace it with another connectivity paragraph.

### Local SMB flags

Replace any wording that turns:
- `EnableSMB1Protocol=True`;
- `EnableSMB2Protocol=True`

into successful/ready remote negotiation.

Allowed:
`Hai thuộc tính cấu hình SMB Server đều có giá trị True. Đây là trạng thái cấu hình cục bộ; các dialect thực sự quan sát được từ xa được trình bày ở Kịch bản 1.`

In Bảng 3.1 rename:
`Cấu hình phương ngữ SMB cục bộ`
to:
`Cấu hình giao thức SMB Server`.

The note should only say the two local flags are True.

### Signing

Keep:
- EnableSecuritySignature=False;
- RequireSecuritySignature=False.

Phrase:
`Hai thuộc tính ký số cục bộ được ghi nhận False; kết quả signing quan sát từ xa được trình bày riêng ở Kịch bản 1/2.`

Do not turn local flags into a remote result.

### Local listeners

State only:
- TCP 445 on `::`;
- TCP 139 on `.56.20`;
- state = Listen.

Do not interpret `::` as proven IPv4+IPv6 functional service.

### Post-Hình 3.1

Use:
`Trạng thái lắng nghe cục bộ không tự xác định trạng thái cổng nhìn từ trạm Kali; khả năng tiếp cận từ xa phải được đo riêng qua đường mạng và chính sách lọc hiện hành.`

Remove:
- “depends directly on middle firewall”.

### Firewall paragraph

Report only configuration facts.

Do not claim:
- disabled default group blocks the entire range;
- custom rule proves traffic passes;
- the rule guarantees interaction;
- other devices cannot interfere.

Post-Hình 3.2 use this bounded idea:

`Hình 3.2 xác nhận quy tắc tùy biến được cấu hình cho TCP 139/445 với phạm vi địa chỉ nguồn 192.168.56.10, đồng thời nhóm File and Printer Sharing mặc định được ghi nhận ở trạng thái tắt. Đây là trạng thái cấu hình tại baseline; khả năng tiếp cận dịch vụ từ Kali được kiểm tra bằng các phép đo từ xa ở phần tiếp theo.`

### Table 3.1 wording

Replace:
`Toàn bộ 3 hồ sơ ... được kích hoạt bảo vệ`
with:
`Cả ba hồ sơ Windows Firewall có Enabled=True`.

Do not expose internal IDs.

## 6. Section 3.1.2 corrections

### First paragraph

Remove generalized claims that FileVersion is normally a static RTM compile string or does not reflect servicing changes.

Do not call MS17-010 one singular “buffer overflow vulnerability”.

Use:
`Để xác định trạng thái cập nhật liên quan MS17-010, đề tài đối chiếu thông tin phiên bản srv.sys và danh mục hotfix cục bộ với tài liệu Microsoft.`

Then state observed display/numeric versions.

### Microsoft threshold

Use:
`ngưỡng phiên bản đã cập nhật tối thiểu`

not:
`ngưỡng an toàn tối thiểu`.

### Hotfix paragraph

Use bounded wording:

`Danh mục Get-HotFix quan sát được gồm sáu mục ...; trong danh mục này không ghi nhận KB4012213, KB4012216 hoặc bản cập nhật thay thế đã được ánh xạ là chứa bản sửa lỗi MS17-010.`

Do not use:
- hoàn toàn không xuất hiện;
- all post-2017 rollups absent;
- exhaustive update history.

### UNPATCHED paragraph

Keep local classification.

Simplify the boundary to:

`UNPATCHED là phân loại trạng thái bản vá cục bộ và không tự tạo ra một phán quyết lỗ hổng từ phép đo từ xa.`

Do not discuss exploit packet structure or broader exploitation conditions here.

### Snapshot paragraph

Use:
`Snapshot Before Demo được ghi nhận cho cả hai máy ảo ở trạng thái poweroff và được chọn làm mốc phục hồi của thực nghiệm.`

Remove:
- bảo đảm tính toàn vẹn;
- bảo đảm khả năng tái lập;
- trạng thái đồng nhất.

### Table 3.2

Keep the values.

Replace any “safe threshold” wording.

For hotfix row use bounded observed-inventory wording.

For snapshot row:
`Recorded for both VMs; final state poweroff at verification`.

Do not say `clean shutdown` unless directly supported by the Before Demo snapshot record.

### Post-Hình 3.3

Replace self-evaluative wording with:

`Hai nhóm dữ liệu phiên bản và hotfix được dùng cùng với ngưỡng Microsoft để phân loại trạng thái bản vá cục bộ.`

## 7. Citation correction — mandatory

Do not use numeric `[4]` or `[5]` for the patch paragraph.

Current global Chapter 1 bibliography makes:
- [4] = SMB security enhancements;
- [5] = SMB signing;
- [7] = MS17-010 bulletin.

S032 Microsoft Support has no locked global number yet.

Because full-report IEEE normalization is deferred, R2 must not invent a final number.

Write the source-dependent sentence naturally, e.g.:

`Theo Microsoft Security Bulletin MS17-010 và tài liệu hỗ trợ “How to verify that MS17-010 is installed”, ...`

Immediately after the paragraph add:

`<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->`

This comment is internal and non-rendering.

Do not expose `S005`/`S032` in rendered prose/table/caption.

Update self-review:
- S005 supports MS17-010 bulletin/KB mapping;
- S032 supports Windows Server 2012 R2 verification and minimum srv.sys version;
- final numeric IEEE labels remain pending X11/global normalization.

Do not edit Chapter 1/2 references in X7A1 R2.

## 8. Final transition

Use one short neutral transition.

Example idea:
`Trên cơ sở trạng thái baseline này, Mục 3.2 trình bày các kết quả khảo sát SMB từ trạm Kali Linux.`

No Scenario 1 result leakage.

## 9. Self-review

Rewrite the self-review where necessary.

It must not claim:
- 100% technical perfection;
- no unresolved issue unless actually verified;
- [4]/[5] citation mapping is correct.

Add search/audit rows for:
- `SMB2/SMB3` inference from local flag = 0;
- `tường lửa trung gian` = 0;
- traffic guarantee/exclusion claim = 0;
- `ngưỡng an toàn` = 0;
- `hoàn toàn không xuất hiện` = 0;
- perfect reproducibility wording = 0;
- visible `[4]`/`[5]` patch citation = 0;
- exactly one non-rendering CITE-ANCHOR with S005/S032.

## 10. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_31_BASELINE_DRAFT_R1.md
git diff --check
```

Do **not** treat the old numeric citation audit as PASS if it only checks syntax.
Record the deliberate citation-anchor deferral in self-review.

Verify:
- 1 H2 / 2 H3;
- 2 tables;
- 3 images;
- image paths unchanged;
- crop manifest unchanged;
- only draft + self-review modified relative to R1;
- no wrong [4]/[5] markers;
- no new evidence/result claim.

## 11. Git

Commit:
`fix(ch3): correct baseline section 3.1 R2`

Push:
`feature/x7a1-ch3-baseline-draft`

Do not merge.

## 12. Handoff

Return:
1. branch;
2. R1 base SHA;
3. local SHA;
4. remote SHA;
5. modified files;
6. word count;
7. H2/H3 count;
8. table/figure count;
9. technical-boundary search results;
10. citation-anchor audit;
11. crop/image unchanged audit;
12. QA results;
13. clean status.

Final state:
`X7A1_CH3_31_BASELINE_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Stop.
Do not open X7B.
