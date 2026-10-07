# BIÊN BẢN BÀN GIAO THỰC THI X7G R2 — CHUẨN HÓA RÁP CHƯƠNG 3 (X7G_CH3_ASSEMBLY_EXECUTOR_HANDOFF_R1)

- **Trạng thái bàn giao:** `X7G_R2_READY_FOR_INDEPENDENT_REVIEW`
- **Pha thực hiện:** `X7G R2 — Bounded Correction of Complete Chapter 3 Assembly`
- **Ngày bàn giao:** 2026-10-07
- **Nhánh làm việc:** `feature/x7g-ch3-assembly-approved-r1`
- **Base Integration HEAD:** `5cedb4d183d9cf58c60fd4553b264768726d0c80`
- **Tập tin kết quả chính:** [CHAPTER_3_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_DRAFT_R1.md)
- **Tập tin tự đánh giá:** [X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md)
- **Báo cáo đánh giá độc lập R1:** [X7G_CH3_ASSEMBLY_EXTERNAL_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7G_CH3_ASSEMBLY_EXTERNAL_REVIEW_R1.md)

---

## 1. Tóm Tắt Các Điểm Hiệu Chỉnh R2

Bản giao nộp R2 này thực hiện xử lý triệt để 2 vấn đề minor blocking được xác định bởi External Review R1:
1. **Chuẩn hóa H2 Mục 3.3 và 3.4:** Đưa 2 tiêu đề H2 về đúng chuẩn của [CHAPTER_3_CONTRACT.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_CONTRACT.md):
   - `## 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010`
   - `## 3.4. Kết quả Case B — Vô hiệu hóa SMBv1`
2. **Loại bỏ thẻ chú thích HTML nội bộ:** Xóa bỏ comment `<!-- CITE-ANCHOR: S005, S032; final IEEE numbering deferred to global normalization gate -->` khỏi `CHAPTER_3_DRAFT_R1.md`, đảm bảo văn bản bản thảo sạch hoàn toàn không chứa mã quản trị quy trình.

---

## 2. Giao Thức Kiểm Chứng Độc Lập Cho Reviewer (Independent Audit Protocol)

Reviewer độc lập có thể sao chép và thực thi tuần tự các lệnh sau trong môi trường PowerShell tại thư mục gốc repository:

### Bước 2.1. Kiểm tra Git Diff trên bản thảo `CHAPTER_3_DRAFT_R1.md`
```powershell
git diff HEAD~1 work/do-an/CHAPTER_3_DRAFT_R1.md
```
*Kỳ vọng:* Diff chỉ hiển thị đúng 3 thay đổi:
- Xóa dòng `<!-- CITE-ANCHOR: ... -->`
- Chuẩn hóa H2 Mục 3.3 (bỏ đuôi `bằng NSE`)
- Chuẩn hóa H2 Mục 3.4 (bỏ đuôi `và đo lại từ xa`)

### Bước 2.2. Kiểm tra Git Blob SHA của 6 tập tin nguồn đã duyệt (Bảo toàn 100%)
```powershell
git hash-object `
  work/do-an/CH3_31_BASELINE_DRAFT_R1.md `
  work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md `
  work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md `
  work/do-an/CH3_34_CASEB_DRAFT_R1.md `
  work/do-an/CH3_35_CASEC_DRAFT_R1.md `
  work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md
```
*Kỳ vọng:* Danh sách hash giữ nguyên vẹn:
1. `c6ac05184b97f59faa97c3183706149f6641c20b` (3.1 Baseline)
2. `a707d3cfb1bd4ebcfd058c24afacea53a1cf2b6f` (3.2 Scenario 1)
3. `3976e2272241f81cec3d51cb5382fbd6502243f2` (3.3 Scenario 2)
4. `db3777b1e367bcb38b73c8da4ec5fc8f8ad59263` (3.4 Case B)
5. `e28d4940b9067a1c164d511f7fa4fd74f75e2419` (3.5 Case C)
6. `912e788745056be3b3cf2df6a774d8ef35667db0` (3.6–3.7 Synthesis)

### Bước 2.3. Kiểm tra tự động các tiêu đề, HTML comment, và chỉ số toàn chương
```powershell
uv run python -c "
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('work/do-an/CHAPTER_3_DRAFT_R1.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Headings check
h1s = re.findall(r'^#\s+(.+)$', text, re.MULTILINE)
h2s = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
h3s = re.findall(r'^###\s+(.+)$', text, re.MULTILINE)

expected_h2s = [
    '3.1. Trạng thái baseline trước đo đạc',
    '3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB',
    '3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010',
    '3.4. Kết quả Case B — Vô hiệu hóa SMBv1',
    '3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense',
    '3.6. So sánh kết quả thực nghiệm',
    '3.7. Tổng kết chương'
]
assert len(h1s) == 1 and h1s[0] == 'CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH'
assert h2s == expected_h2s, f'H2 mismatch: {h2s}'
assert len(h3s) == 10

# 2. HTML comments & CITE-ANCHOR
html_comments = re.findall(r'<!--.*?-->', text, re.DOTALL)
assert len(html_comments) == 0, f'Found HTML comments: {html_comments}'
assert 'CITE-ANCHOR' not in text

# 3. Images & Tables
imgs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
assert len(imgs) == 11
for _, p in imgs:
    assert os.path.exists(os.path.join('work/do-an', p)), f'Missing image: {p}'

print('ALL R2 CHECKS PASSED: CANONICAL HEADINGS + CLEAN NO-HTML DRAFT')
"
```
*Kỳ vọng:* In ra `ALL R2 CHECKS PASSED: CANONICAL HEADINGS + CLEAN NO-HTML DRAFT`.

### Bước 2.4. Chạy bộ kiểm thử tự động và linter
```powershell
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_DRAFT_R1.md
git diff --check
```
*Kỳ vọng:*
- Unittest: 7 tests passed (OK).
- Linter: error=0, warning=1 (`VI012` ghi nhận `KEEP_WITH_REASON` phục vụ X7H).
- Diff check: Sạch (không có lỗi khoảng trắng).

---

## 3. Bảng Tổng Hợp Chỉ Số Kiểm Thử Sau R2

| Tiêu chí | Kỳ vọng thiết kế R2 | Thực tế ghi nhận | Kết quả |
|---|:---:|:---:|:---:|
| **Tiêu đề H1** | 1 (`# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`) | 1 | **ĐẠT** |
| **Tiêu đề H2** | 7 tiêu đề chuẩn hóa theo `CHAPTER_3_CONTRACT.md` | Đúng 7 tiêu đề canonical | **ĐẠT** |
| **Tiêu đề H3** | 10 (`3.1.1` đến `3.5.2`) | 10 | **ĐẠT** |
| **Số bảng (Tables)** | Đúng 7 bảng (`Bảng 3.1` đến `Bảng 3.7`) | 7 | **ĐẠT** |
| **Số hình (Figures)** | Đúng 11 hình (`Hình 3.1` đến `Hình 3.11`) | 11 | **ĐẠT** |
| **Số tệp ảnh Markdown** | Đúng 11 ảnh, đường dẫn tồn tại thật | 11/11 | **ĐẠT** |
| **Thẻ HTML comment** | 0 thẻ | **0 thẻ** | **ĐẠT** |
| **Mã neo CITE-ANCHOR** | 0 lần | **0 lần** | **ĐẠT** |
| **Số từ văn xuôi (Prose words)** | ~8.500 – 10.000 từ | **9.444 từ** | **ĐẠT** |
| **Tổng số từ (Total words)** | Tính cả bảng, mã lệnh, chú thích | **11.101 từ** | **ĐẠT** |
| **Ranh giới phương pháp luận** | 5 bất đẳng thức được giữ vững | 100% tuân thủ | **ĐẠT** |

---

## 4. Trạng Thái Hoàn Thành
`X7G_R2_READY_FOR_INDEPENDENT_REVIEW`
