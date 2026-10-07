# BIÊN BẢN BÀN GIAO THỰC THI X7H — BIÊN TẬP TOÀN BỘ CHƯƠNG 3 (X7H_CH3_WHOLE_REVIEW_EXECUTOR_HANDOFF_R1)

- **Trạng thái bàn giao:** `X7H_R2_READY_FOR_INDEPENDENT_REVIEW`
- **Pha thực hiện:** `X7H — Whole-Chapter-3 Product Review (Vòng hiệu chỉnh R2)`
- **Ngày bàn giao:** 2026-10-07
- **Nhánh làm việc:** `feature/x7h-ch3-whole-review-approved-r1`
- **Base Reviewed X7G State:** `d348b713802593ff82bbab5b460e5eb7e6973b3d`
- **R1 Candidate Commit:** `01cc66de9845395777ced08801d5816ab1f938fe`
- **Tập tin kết quả chính:** [CHAPTER_3_DRAFT_R2.md](file:///e:/word_ppt-auto/work/do-an/CHAPTER_3_DRAFT_R2.md)
- **Tập tin tự đánh giá:** [X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7H_CH3_WHOLE_REVIEW_SELF_REVIEW_R1.md)
- **Báo cáo thẩm định độc lập R1:** [X7H_CH3_WHOLE_REVIEW_EXTERNAL_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/X7H_CH3_WHOLE_REVIEW_EXTERNAL_REVIEW_R1.md)
- **Chỉ thị hiệu chỉnh R2:** [X7H_R2_CORRECT_WHOLE_CHAPTER_REVIEW.md](file:///e:/word_ppt-auto/work/do-an/prompts/X7H_R2_CORRECT_WHOLE_CHAPTER_REVIEW.md)

---

## 1. Mục Đích Biên Bản Bàn Giao

Biên bản này được lập nhằm cung cấp quy trình kiểm chứng độc lập hoàn chỉnh (reproducible audit protocol) cho người đánh giá độc lập (Independent Reviewer), cho phép thẩm định toàn bộ các cải tiến văn phong, cấu trúc và đặc biệt là 4 điểm hiệu chỉnh ranh giới kỹ thuật theo chỉ thị X7H R2 trên bản thảo `CHAPTER_3_DRAFT_R2.md` mà không cần dựa vào bất kỳ kết luận tự phong nào của bên thực thi.

---

## 2. Giao Thức Kiểm Chứng Độc Lập Cho Reviewer (Independent Audit Protocol)

Reviewer độc lập có thể sao chép và thực thi tuần tự các khối lệnh sau trong PowerShell tại thư mục gốc của repository:

### Bước 2.1. Kiểm tra nhánh và phả hệ Git (Lineage Check)
```powershell
git checkout feature/x7h-ch3-whole-review-approved-r1
git status --short
git merge-base --is-ancestor d348b713802593ff82bbab5b460e5eb7e6973b3d HEAD
```
*Kỳ vọng:* `git merge-base` trả về exit code 0 (không in lỗi), working tree sạch.

### Bước 2.2. Kiểm tra Git Diff giữa Candidate R1 và Candidate R2 (Chỉ đúng 4 đoạn sửa)
```powershell
git diff 01cc66de9845395777ced08801d5816ab1f938fe HEAD -- work/do-an/CHAPTER_3_DRAFT_R2.md
```
*Kỳ vọng:* Diff chỉ gồm đúng 4 đoạn thay thế tương ứng với 4 lỗi kỹ thuật/bằng chứng được reviewer độc lập chỉ ra tại báo cáo R1:
1. Bỏ "định tuyến qua" -> dùng "được bố trí đi qua" pfSense Transparent Bridge (Layer 2).
2. Bỏ claim firewall "bảo đảm chỉ mở cho trạm kiểm thử chỉ định" -> khôi phục mô tả phạm vi cấu hình và đo đạc riêng.
3. Bỏ claim "danh sách cập nhật dừng ở năm 2014" -> dùng wording "sáu mục Get-HotFix quan sát được đều có ngày cài đặt trong năm 2014".
4. Giới hạn Nmap fingerprint vào "trong lần đo này", bỏ nhận định khái quát hóa công cụ.

### Bước 2.3. Kiểm tra tự động các chỉ số cấu trúc, số hiệu và khóa kỹ thuật
```powershell
uv run python -c "
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('work/do-an/CHAPTER_3_DRAFT_R2.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Headings
h1s = re.findall(r'^#\s+(.+)$', text, re.MULTILINE)
h2s = re.findall(r'^##\s+(.+)$', text, re.MULTILINE)
h3s = re.findall(r'^###\s+(.+)$', text, re.MULTILINE)
assert len(h1s) == 1 and h1s[0] == 'CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH'
assert len(h2s) == 7 and len(h3s) == 10, 'Heading count mismatch'

# 2. Tables & Figures
tables = sorted(set(re.findall(r'\bBảng\s+(3\.\d+)', text)))
assert tables == ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7'], f'Table mismatch: {tables}'
imgs = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)
assert len(imgs) == 11, 'Image count mismatch'
for _, p in imgs:
    assert os.path.exists(os.path.join('work/do-an', p)), f'Missing image: {p}'

# 3. Technical Locks & Anti-drift
for lock in ['445 OPEN != vulnerable', 'SMBv1 enabled != MS17-010 confirmed', 'SMBv1 disabled != PATCHED', 'FILTERED != PATCHED', 'UNKNOWN != SAFE']:
    assert lock in text, f'Missing lock: {lock}'
for bad in ['Bảng 3.8', 'Hình 3.12', 'Meterpreter', 'reverse shell', 'khai thác thành công', 'chiếm quyền điều khiển']:
    assert bad.lower() not in text.lower(), f'Found prohibited term: {bad}'
assert '<!--' not in text and 'CITE-ANCHOR' not in text

# 4. R2 Specific Wording Drift Checks
assert 'định tuyến qua tường lửa pfSense' not in text, 'Found routed wording for Transparent Bridge'
assert 'bảo đảm bề mặt dịch vụ tại baseline chỉ mở' not in text, 'Found firewall exclusivity claim'
assert 'dừng ở năm 2014' not in text, 'Found complete-history hotfix claim'
assert 'không thể tự định danh' not in text, 'Found generalized tool capability claim'

# 5. R2 Specific Required Bounded Wording Checks
assert 'được bố trí đi qua tường lửa pfSense' in text, 'Missing bounded L2 bridge wording'
assert 'sáu mục Get-HotFix quan sát được đều có ngày cài đặt trong năm 2014' in text, 'Missing bounded hotfix wording'
assert 'trong lần đo này: Nmap chỉ khu biệt hệ thống trong dải dấu vết phiên bản' in text, 'Missing bounded Nmap measurement wording'
assert 'khả năng tiếp cận dịch vụ từ trạm Kali được kiểm tra riêng bằng các phép đo mạng' in text, 'Missing bounded firewall measurement wording'

print('ALL X7H R2 STRUCTURAL, IMAGE, TECHNICAL LOCK AND BOUNDARY CHECKS PASSED!')
"
```
*Kỳ vọng:* In ra `ALL X7H R2 STRUCTURAL, IMAGE, TECHNICAL LOCK AND BOUNDARY CHECKS PASSED!`.

### Bước 2.4. Chạy bộ linter học thuật và kiểm thử dự án
```powershell
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_3_DRAFT_R2.md
git diff --check
uv run python scripts/validate_project.py
```
*Kỳ vọng:*
- Unittest: 7 tests passed (OK).
- Linter: `Không phát hiện mẫu văn phong cần xem xét.` (error=0, warning=0, info=0).
- Diff check: Sạch (0 lỗi khoảng trắng).
- Validate project: `Project validation passed`.

---

## 3. Bảng Tổng Hợp Chỉ Số Kiểm Thử Sau Hiệu Chỉnh R2

| Tiêu chí | Kỳ vọng thiết kế X7H | Thực tế đạt được R2 | Đánh giá |
|---|:---:|:---:|:---:|
| **Tiêu đề H1** | 1 (`# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH`) | 1 | **ĐẠT** |
| **Tiêu đề H2** | Đúng 7 tiêu đề canonical | Đúng 7 tiêu đề canonical | **ĐẠT** |
| **Tiêu đề H3** | Đúng 10 tiêu đề | Đúng 10 tiêu đề | **ĐẠT** |
| **Số bảng (Tables)** | Đúng 7 bảng (`Bảng 3.1` đến `Bảng 3.7`) | 7 | **ĐẠT** |
| **Số hình (Figures)** | Đúng 11 hình (`Hình 3.1` đến `Hình 3.11`) | 11 | **ĐẠT** |
| **Số tệp ảnh Markdown** | Đúng 11 ảnh, đường dẫn tồn tại thật | 11/11 | **ĐẠT** |
| **Số từ văn xuôi (Prose words)** | ~8.500 – 9.500 từ | **9.268 từ** | **ĐẠT** |
| **Tổng số từ (Total words)** | Tính cả bảng, mã lệnh, chú thích | **10.924 từ** | **ĐẠT** |
| **Cảnh báo Linter học thuật** | 0 lỗi, 0 cảnh báo | **0 lỗi, 0 cảnh báo** | **ĐẠT** |
| **Ranh giới phương pháp luận** | 5 bất đẳng thức được giữ vững | 100% tuân thủ | **ĐẠT** |
| **Hiệu chỉnh 4 lỗi ranh giới R2** | Đã sửa triệt để 4 điểm theo chỉ thị R2 | 4/4 điểm chuẩn xác | **ĐẠT** |

---

## 4. Ranh Giới & Khuyến Nghị Dành Cho Reviewer Độc Lập

1. **Phạm vi thẩm định:** Kiểm tra 4 điểm hiệu chỉnh ranh giới kỹ thuật tại diff của `CHAPTER_3_DRAFT_R2.md`, đánh giá tính mạch lạc của toàn chương và xác nhận toàn bộ các ranh giới thực nghiệm đã đóng khớp.
2. **Không tạo DOCX/PDF:** Không xuất bản DOCX/PDF cho đến khi toàn bộ Chương 3 nhận được sự phê duyệt chính thức từ người dùng.
3. **Không sửa Chapter 2 / Không mở Chapter 4:** Giữ nguyên trạng Chapter 2 đã khóa; không mở nội dung Chapter 4.
4. **Trạng thái bàn giao:** `X7H_R2_READY_FOR_INDEPENDENT_REVIEW`.
