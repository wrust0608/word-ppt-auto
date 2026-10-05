# X5 PRODUCT-ALIGNED R2 — MICRO PATCH ONLY

Status: `READY_FOR_EXECUTOR`
Branch: `feature/x5-chapter-2-product-aligned`

## 1. Goal

Apply only the corrections from:
`origin/main:work/do-an/X5_PRODUCT_ALIGNED_EXTERNAL_REVIEW_R1.md`

Do NOT restructure Chapter 2.
Do NOT add new research.
Do NOT open Chapter 3.
Do NOT change the locked 7 H2 / 20 H3 structure.

Candidate R1:
`1e1cc9edc191efb2a03e6b20807fa82d32841448`

## 2. Mandatory setup

```bash
git fetch origin
git checkout feature/x5-chapter-2-product-aligned
git pull --ff-only origin feature/x5-chapter-2-product-aligned
git status --short
git rev-parse HEAD
```

Read:
1. `origin/main:work/do-an/X5_PRODUCT_ALIGNED_EXTERNAL_REVIEW_R1.md`
2. `origin/main:work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
3. `origin/main:work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
4. `origin/main:work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`

## 3. Patch result leakage in method tables

Chapter 2 method tables must specify what to observe, not the final measured values.

### Scenario 1 table

Replace outcome-specific phrases:

B4:
- avoid `syn-ack` as the expected result;
- use: `Trạng thái cổng và trường REASON do Nmap trả về`.

B5:
- use: `Chuỗi service/version fingerprint do Nmap trả về`.

B6:
- do not write `NT LM 0.12`, concrete SMB2/3 dialect values, or actual signing state;
- use: `Danh sách dialect SMB, chính sách ký số và các capability do script trả về`.

### Scenario 2 table

NSE-SMB-01:
- `Trạng thái TCP 139/445 và trường REASON`.

NSE-SMB-02:
- `Danh sách dialect SMB do script trả về`.

NSE-SMB-03:
- `Chính sách ký số SMB do script trả về`.

NSE-SMB-04:
- `Script output / verdict nếu có`.

Do not place actual measured outcome values in Chapter 2.

## 4. Fix generic FILTERED semantics

In 2.6.3 replace causal wording.

Required meaning:

`FILTERED cho biết Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed; trạng thái này không chứng minh máy chủ đã được vá.`

Do not write generic:
`FILTERED = firewall blocked the packet`.

Case C causal correlation belongs to Chapter 3 where Nmap result can be compared with pfSense direct log evidence.

## 5. Tighten SMBv1 inference

In both 2.3.3 and 2.6.3, use this meaning:

`SMBv1 được bật chỉ cho thấy giao thức liên quan còn được hỗ trợ; trạng thái này không đủ để xác nhận MS17-010. Việc đánh giá cần đối chiếu thêm trạng thái bản vá nội bộ và kết quả kiểm tra từ xa.`

Do not write:
- SMBv1 is a “necessary condition” for vulnerability;
- exploitability depends only on patch state;
- SMBv1 + UNPATCHED implies MS17-010 confirmed.

## 6. Tighten Case B wording

Replace:
`nhằm loại bỏ hoàn toàn việc hỗ trợ giao thức kế thừa SMBv1`

with:
`nhằm vô hiệu hóa SMBv1 trong cấu hình SMB Server`.

Replace:
`Thao tác can thiệp không yêu cầu khởi động lại máy`

with:
`Trong kịch bản không thực hiện bước khởi động lại máy.`

Keep:
- `FS-SMB1` remains installed;
- no patch claim;
- actual two retests only.

## 7. Patch-state wording

Replace heading/phrase:
`Đối chiếu ngưỡng an toàn`

with:
`Đối chiếu ngưỡng phiên bản đã cập nhật`.

Keep local wording bounded to observed hotfix inventory / project mapping.

Do not imply complete historical knowledge of every update ever installed.

## 8. Bound isolation wording

Avoid:
- `loại trừ kết nối mạng ngoài`
- `bảo đảm tính khép kín`
- `bảo đảm lưu lượng chỉ lưu chuyển cục bộ`

Use factual wording:

`Ở trạng thái baseline, hai máy ảo chỉ sử dụng Host-Only NIC, không cấu hình NAT/Bridged và không có default route, qua đó giới hạn đường kết nối của chúng trong mạng lab.`

Do not infer host-level forwarding state beyond evidence.

## 9. Clarify evidence selection in 2.6.2

Troubleshooting/pre-repair/aborted data must not sound deleted or hidden.

Required meaning:
- they remain preserved for traceability;
- they are not used as the main result set because they are not the final completed run;
- Chapter 3 result claims use the final completed/canonical run.

Use normal academic Vietnamese; do not expose internal governance jargon.

## 10. Case C tunables

Keep:
- `pfil_member=1`
- `pfil_bridge=0`
- `pfil_onlyip=1`

Do not change their semantics.

Do not claim one screenshot directly proves all three values.

No exact named-rule attribution from the conflicting firewall log.

## 11. Style cleanup

In 2.7 replace self-evaluative wording such as:

`tạo lập nền tảng khoa học vững chắc`

with:

`Các tệp kết quả và nguyên tắc diễn giải trên được dùng làm cơ sở phân tích tại Chương 3.`

## 12. Do not change already-correct content

Do not alter:
- 7 H2 / 20 H3;
- exact Scenario 1 commands;
- exact Scenario 2 operator commands;
- Case B action/retest commands;
- Case C topology;
- Case C rule design;
- Case A removal;
- timebase lock;
- .56.100 unidentified state.

## 13. Search gate

Before commit verify:
- actual `NT LM 0.12` result not present in method-table observation columns;
- actual `syn-ack` result not present in method-table observation columns;
- generic `FILTERED` cause does not say firewall/blocked packet;
- `điều kiện giao thức cần` -> 0;
- `loại bỏ hoàn toàn việc hỗ trợ giao thức` -> 0;
- `ngưỡng an toàn` -> 0;
- `loại trừ kết nối mạng ngoài` -> 0;
- `nền tảng khoa học vững chắc` -> 0.

## 14. QA

Run:
```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md
uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md
git diff --check
```

## 15. Files allowed

Only:
- `work/do-an/CHAPTER_2.md`
- `work/do-an/CHAPTER_2_X5_SELF_REVIEW.md`

## 16. Git

Commit:
`fix(ch2): close product-aligned R1 review findings`

Push:
`feature/x5-chapter-2-product-aligned`

Verify local SHA = remote SHA.

## 17. Handoff

Return:
1. local SHA;
2. remote SHA;
3. word count;
4. 7 H2 / 20 H3;
5. R1 issue-closure matrix;
6. result-leakage table audit;
7. FILTERED wording check;
8. SMBv1 boundary check;
9. QA;
10. clean status.

Final status:
`X5_PRODUCT_ALIGNED_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Stop.

Do not self-declare PASS.
Do not open Chapter 3.
