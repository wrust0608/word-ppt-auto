# BIÊN BẢN BÀN GIAO THỰC THI X7G — RÁP CHƯƠNG 3 ĐƯỢC DUYỆT (X7G_CH3_ASSEMBLY_EXECUTOR_HANDOFF_R1)

- **Trạng thái bàn giao:** `X7G_ASSEMBLY_READY_FOR_INDEPENDENT_REVIEW`
- **Pha thực hiện:** `X7G — Mechanically Assemble Approved Complete Chapter 3`
- **Ngày bàn giao:** 2026-10-07
- **Nhánh làm việc:** `feature/x7g-ch3-assembly-approved-r1`
- **Base Integration HEAD:** `5cedb4d183d9cf58c60fd4553b264768726d0c80`
- **Tập tin kết quả chính:** [CHAPTER_3_DRAFT_R1.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_DRAFT_R1.md)
- **Tập tin tự đánh giá:** [X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7G_CH3_ASSEMBLY_SELF_REVIEW_R1.md)

---

## 1. Mục Đích Biên Bản Bàn Giao
Biên bản này được lập nhằm cung cấp đầy đủ thông tin kỹ thuật và quy trình kiểm chứng độc lập (reproducible audit protocol) cho người đánh giá độc lập (Independent Reviewer), giúp người đánh giá có thể tự chạy kiểm tra cơ học và thẩm định toàn bộ kết quả mà không cần dựa vào bất kỳ tuyên bố tự phong (self-asserted PASS) nào của bên thực thi.

---

## 2. Quy Trình & Lệnh Kiểm Chứng Độc Lập Cho Reviewer

Reviewer độc lập có thể sao chép và thực thi tuần tự các lệnh sau trong môi trường PowerShell tại thư mục gốc repository để kiểm chứng tính xác thực:

### Bước 2.1. Kiểm tra nhánh và phả hệ Git (Lineage Check)
```powershell
git checkout feature/x7g-ch3-assembly-approved-r1
git status --short
git merge-base --is-ancestor 5cedb4d183d9cf58c60fd4553b264768726d0c80 HEAD
```
*Kỳ vọng:* Lệnh `git merge-base` trả về exit code 0 (không in lỗi).

### Bước 2.2. Kiểm tra Git Blob SHA của 6 tập tin nguồn đã duyệt
```powershell
git hash-object `
  work/do-an/CH3_31_BASELINE_DRAFT_R1.md `
  work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md `
  work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md `
  work/do-an/CH3_34_CASEB_DRAFT_R1.md `
  work/do-an/CH3_35_CASEC_DRAFT_R1.md `
  work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md
```
*Kỳ vọng:* Danh sách hash khớp chính xác:
1. `c6ac05184b97f59faa97c3183706149f6641c20b` (3.1 Baseline)
2. `a707d3cfb1bd4ebcfd058c24afacea53a1cf2b6f` (3.2 Scenario 1)
3. `3976e2272241f81cec3d51cb5382fbd6502243f2` (3.3 Scenario 2)
4. `db3777b1e367bcb38b73c8da4ec5fc8f8ad59263` (3.4 Case B)
5. `e28d4940b9067a1c164d511f7fa4fd74f75e2419` (3.5 Case C)
6. `912e788745056be3b3cf2df6a774d8ef35667db0` (3.6–3.7 Synthesis)

### Bước 2.3. Kiểm tra tính toàn vẹn nguyên văn (Exact-Match Audit)
```powershell
uv run python -c "
import sys
sys.stdout.reconfigure(encoding='utf-8')
sources = [
    'work/do-an/CH3_31_BASELINE_DRAFT_R1.md',
    'work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md',
    'work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md',
    'work/do-an/CH3_34_CASEB_DRAFT_R1.md',
    'work/do-an/CH3_35_CASEC_DRAFT_R1.md',
    'work/do-an/CH3_36_37_SYNTHESIS_DRAFT_R1.md'
]
with open('work/do-an/CHAPTER_3_DRAFT_R1.md', 'r', encoding='utf-8') as f:
    assembled = f.read()
for s in sources:
    with open(s, 'r', encoding='utf-8') as f:
        src_text = f.read().strip()
    count = assembled.count(src_text)
    print(f'{s}: {count} match(es)')
    assert count == 1, f'Mismatch in {s}'
print('ALL SOURCES EXACT MATCH 100%')
"
```
*Kỳ vọng:* In ra `ALL SOURCES EXACT MATCH 100%` với đúng 1 match cho từng file.

### Bước 2.4. Kiểm tra chỉ số cấu trúc, đường dẫn ảnh và chống trôi dạt (Structural & Anti-Drift Check)
```powershell
uv run python -c "
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('work/do-an/CHAPTER_3_DRAFT_R1.md', 'r', encoding='utf-8') as f:
    text = f.read()
h1s = re.findall(r'^#\s+(.+)$', text, re.MULTILINE)
h2s = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
h3s = re.findall(r'^###\s+(.+)$', text, re.MULTILINE)
assert len(h1s) == 1 and len(h2s) == 7 and len(h3s) == 10, 'Heading count mismatch'
imgs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
assert len(imgs) == 11, 'Image count mismatch'
for _, p in imgs:
    assert os.path.exists(os.path.join('work/do-an', p)), f'Missing image: {p}'
for bad in ['Bảng 3.8', 'Hình 3.12', 'Meterpreter', 'reverse shell', 'khai thác thành công']:
    assert bad.lower() not in text.lower(), f'Found prohibited term: {bad}'
print('STRUCTURAL & IMAGE INTEGRITY VERIFIED')
"
```
*Kỳ vọng:* In ra `STRUCTURAL & IMAGE INTEGRITY VERIFIED`.

### Bước 2.5. Chạy bộ kiểm thử tự động và linter
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

## 3. Bảng Tổng Hợp Chỉ Số Kiểm Thử Thực Tế

| Tiêu chí | Kỳ vọng thiết kế | Thực tế ghi nhận | Kết quả |
|---|:---:|:---:|:---:|
| **Tiêu đề H1** | 1 (`# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`) | 1 | **ĐẠT** |
| **Tiêu đề H2** | 7 (`3.1` đến `3.7`) | 7 | **ĐẠT** |
| **Tiêu đề H3** | 10 (`3.1.1` đến `3.5.2`) | 10 | **ĐẠT** |
| **Tiêu đề H4** | 0 | 0 | **ĐẠT** |
| **Số bảng (Tables)** | Đúng 7 bảng (`Bảng 3.1` đến `Bảng 3.7`) | 7 | **ĐẠT** |
| **Số hình (Figures)** | Đúng 11 hình (`Hình 3.1` đến `Hình 3.11`) | 11 | **ĐẠT** |
| **Số tệp ảnh Markdown** | Đúng 11 ảnh, đường dẫn tồn tại thật | 11/11 | **ĐẠT** |
| **Số từ văn xuôi (Prose words)** | ~8.500 – 10.000 từ | **9.457 từ** | **ĐẠT** |
| **Tổng số từ (Total words)** | Tính cả bảng, mã lệnh, chú thích | **11.121 từ** | **ĐẠT** |
| **Chỉnh sửa câu chữ** | 0 từ | 0 từ | **ĐẠT** |
| **Ranh giới phương pháp luận** | 5 bất đẳng thức được giữ vững | 100% tuân thủ | **ĐẠT** |

---

## 4. Ranh Giới & Khuyến Nghị Dành Cho Reviewer Độc Lập
1. **Phạm vi kiểm tra:** Thẩm định việc ráp cơ học không làm thay đổi ngữ nghĩa kỹ thuật, không làm mất mát văn bản đã duyệt, và cấu trúc số hiệu bảng/hình được bảo toàn tuyệt đối.
2. **Không chỉnh sửa trong X7G:** X7G là bước ráp cơ học. Công tác đọc toàn chương, phát hiện lặp ý, rút gọn câu từ và tối ưu văn phong học thuật tiếng Việt thuộc trách nhiệm của pha **X7H**.
3. **Không tạo DOCX/PDF:** Chặn hoàn toàn việc dựng Word hoặc PDF cho đến khi X7H hoàn tất và người dùng phê duyệt toàn bộ Chương 3.
4. **Không mở Chương 4:** Giữ nguyên trạng thái đóng đối với Chương 4.
5. **Trạng thái phê duyệt tối đa của bàn giao này:** `X7G_ASSEMBLY_READY_FOR_INDEPENDENT_REVIEW`.
