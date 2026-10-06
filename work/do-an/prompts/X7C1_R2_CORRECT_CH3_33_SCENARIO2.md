# X7C1 R2 — CORRECT SECTION 3.3 SCENARIO 2 DRAFT

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7c1-ch3-scenario2-draft`  
R1 candidate: `f9c3d13d3036113a21dcb5221598426a6da3f7da`

## 0. Objective

Correct only the bounded issues identified in:

`work/do-an/X7C1_CH3_33_EXTERNAL_REVIEW_R1.md`

Do not redesign Section 3.3.

Preserve:

- exactly 1 H2 + 2 H3;
- Bảng 3.4 only;
- Hình 3.6 only;
- the existing derived Hình 3.6 image;
- the existing crop rectangle;
- all approved X7C0 numbering;
- the core remote UNKNOWN / local UNPATCHED independence.

Do not write Section 3.4.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7c1-ch3-scenario2-draft
git pull --ff-only origin feature/x7c1-ch3-scenario2-draft
git status --short
git rev-parse HEAD
```

Read first:

1. `work/do-an/X7C1_CH3_33_EXTERNAL_REVIEW_R1.md`
2. `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
3. `work/do-an/CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1.md`
4. `work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md`
5. reviewer-final `work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md`
6. `work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md`
7. Scenario 2 raw NSE01–04 outputs
8. approved Section 3.1 draft for the exact UNPATCHED cross-reference.

## 2. Allowed files to modify

Modify only:

- `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`
- `work/do-an/CH3_33_SCENARIO2_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_33_SCENARIO2_CROP_MANIFEST_R1.md`

Do not modify:

- Hình 3.6 derived image;
- source evidence;
- approved X7C0 planning artifacts;
- claim map;
- numbering ledger;
- Sections 3.1/3.2;
- Chapter 2;
- truth matrix;
- R3 locks.

## 3. Keep structure and presentation unchanged

Keep exactly:

- 1 H2;
- 2 H3;
- Bảng 3.4;
- Hình 3.6;
- no NSE01/02/03 screenshots.

Do not regenerate Hình 3.6.

Expected derived SHA-256 remains:

`8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`

Expected crop remains:

`x=0, y=24, width=1280, height=330`.

## 4. Correct NSE-SMB-02 dialect wording

Remove or rewrite student-facing phrases such as:

- `đàm phán và lập danh mục ... chấp thuận`;
- `máy chủ hỗ trợ 5 phương ngữ`;
- `hỗ trợ đàm phán`;
- `Hỗ trợ đa phương ngữ`;
- `tính tương thích ngược`.

Use the direct form:

`Kịch bản smb-protocols ghi nhận 5 phương ngữ: NT LM 0.12 (SMBv1), 2.0.2, 2.1, 3.0 và 3.0.2.`

In Bảng 3.4 use the approved wording:

- objective: `Khảo sát các phương ngữ SMB được ghi nhận từ xa`;
- classification heading: `Các phương ngữ SMB được ghi nhận`.

For `[dangerous, but default]`:

- report it only as a literal Nmap annotation;
- do not expand it into a generalized risk statement such as “tính chất mất an toàn của SMB thế hệ đầu tiên”.

Keep:

`SMBv1 enabled != MS17-010 confirmed`.

## 5. Narrow NSE-SMB-03 signing prose

Keep direct evidence:

- `smb2-security-mode`;
- dialect 3.0.2;
- `Message signing enabled but not required`;
- remote observation independent from local flags.

Remove unnecessary theory such as:

- explaining the general integrity-security purpose of signing;
- explaining what every client must or does not have to do beyond the literal result.

Use a compact result-oriented paragraph.

## 6. Correct NSE-SMB-04 observation/classification wording

### 6.1 Bảng 3.4

Replace:

`Kết quả này phản ánh giới hạn của phép đo từ xa...`

with wording equivalent to:

`Kết quả này chỉ cho phép phân loại là chưa xác định trong phạm vi phép đo; nguyên nhân của việc không có đầu ra script khả dụng không được xác lập. UNKNOWN != SAFE.`

### 6.2 Execution wording

Do not write:

- `NSE-SMB-04 được kích hoạt`;
- `gọi kịch bản chuyên biệt`.

Use:

`Phép đo NSE-SMB-04 được thực hiện bằng lệnh Nmap có tùy chọn --script smb-vuln-ms17-010 nhắm vào TCP 445 của 192.168.56.20.`

### 6.3 Visible completion facts

Do not write:

- `phiên quét kết thúc bình thường`;
- `shell trả về bình thường`.

Use only direct facts:

- output reaches `Nmap done`;
- shell prompt appears afterward;
- no corresponding error message is displayed in the recorded output.

### 6.4 Missing-output cause

Prefer:

`Nguyên nhân của việc không có đầu ra script khả dụng không được xác lập từ bộ bằng chứng hiện có.`

Do not write:

`không thể xác định`

as a universal claim.

Do not say the missing verdict itself proves a limitation/cause of Nmap.

### 6.5 Crop manifest

Update only the interpretation wording in the manifest.

Replace `phiên quét kết thúc bình thường` with the direct visible fact:

`đầu ra đạt đến dòng Nmap done`.

Do not change any path, SHA, dimensions or crop rectangle.

## 7. Simplify the local UNPATCHED cross-reference

Preferred public prose:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

Do not re-derive the patch classification unless necessary.

Preferred R2 action:
- remove the long detailed `srv.sys` / KB repetition from Section 3.3;
- rely on the Section 3.1 cross-reference.

If any detail is retained, use only the exact locked wording:

- numeric `srv.sys = 6.3.9600.16421`;
- Microsoft minimum updated version threshold = `6.3.9600.18604`;
- **observed local hotfix inventory** does not record KB4012213, KB4012216, or a **mapped superseding update containing the MS17-010 fix**.

Forbidden:

- `ngưỡng cập nhật an toàn tối thiểu`;
- broad `các bản cập nhật thay thế tương ứng`.

## 8. Simplify the exploitation boundary in student prose

Replace the long tooling list with a compact student-facing boundary.

Recommended:

`Kịch bản 2 dừng ở phạm vi rà quét NSE; không có bước khai thác hoặc kết quả thực thi mã từ xa được ghi nhận trong kịch bản này.`

Do not list in student prose:

- Meterpreter;
- reverse shell;
- exploit-session tooling.

The internal self-review may retain detailed scope checks.

## 9. Light academic tightening

R1 prose count is approximately **1,719 words**, which is above the requested ~1,100–1,600 range.

Do a light tightening pass.

Target approximately:

**1,300–1,550 prose words**

Do not:
- remove substantive evidence;
- remove the UNKNOWN/UNPATCHED explanation;
- compress the section into terse QA prose.

Trim mainly:
- repeated restatements of the same uncertainty boundary;
- broad security theory;
- repeated patch details already established in 3.1;
- verbose scope disclaimers.

## 10. Self-review must describe the final file truthfully

Rebuild the self-review after the final R2 edit.

Required corrections:

1. Do not say 1,719 words is within a 1,100–1,600 range.
2. Recompute final word count.
3. Run forbidden-term searches only after the final prose has been saved.
4. Report actual counts.
5. Do not claim `Meterpreter / reverse shell = 0` if those strings exist.
6. Update all wording that still says:
   - dialects were “negotiated successfully”;
   - scan completed “normally”;
   - shell returned “normally”.
7. Keep paragraph/table/figure-to-claim mapping aligned with S2-C01..S2-C15.
8. Do not self-declare external PASS.

Final executor state:

`X7C1_CH3_33_SCENARIO2_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

## 11. Required searches

After final editing, search the **student prose** for:

- `hỗ trợ 5 phương ngữ`
- `hỗ trợ đàm phán`
- `Hỗ trợ đa phương ngữ`
- `tính chất mất an toàn`
- `phản ánh giới hạn của phép đo từ xa`
- `được kích hoạt`
- `gọi kịch bản chuyên biệt`
- `trả về bình thường`
- `kết thúc bình thường`
- `ngưỡng cập nhật an toàn tối thiểu`
- `các bản cập nhật thay thế tương ứng`
- `Meterpreter`
- `reverse shell`

All should be **0** in student prose.

Also verify:
- `Baseline Case A` = 0;
- `false negative` / `âm tính giả` = 0;
- no internal S2 IDs;
- no invented NTSTATUS/IPC$ cause;
- no `-Pn`;
- no local/remote signing reconciliation;
- no Case B result;
- no Case C;
- no Chapter 4 recommendation/risk content.

## 12. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md
git diff --check
```

Verify hashes again:

Source Hình 3.6:
`c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`

Derived Hình 3.6:
`8f7a343fe9ab100a187a5ab4fe85cac320e9350cf5d59df0c4d78e385a137bdc`

The image must not be modified in R2.

## 13. Git

Commit:

`fix(ch3): correct scenario2 section 3.3 R2`

Push:

`feature/x7c1-ch3-scenario2-draft`

Do not merge.

## 14. Handoff

Return:

1. starting SHA;
2. local/remote R2 SHA;
3. modified file list;
4. before/after summary for each reviewer correction group;
5. final prose word count;
6. H2/H3/table/figure count;
7. Hình 3.6 source/derived hash verification;
8. dialect wording audit;
9. signing wording audit;
10. NSE04 direct-observation vs classification audit;
11. crop-manifest wording audit;
12. UNPATCHED cross-reference audit;
13. exploitation-scope wording audit;
14. forbidden-search results;
15. self-review truthfulness audit;
16. QA results;
17. clean git status.

Final state:

`X7C1_CH3_33_SCENARIO2_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open X7D.
Do not write Section 3.4.
Do not write Chapter 4.
Do not create final DOCX.
