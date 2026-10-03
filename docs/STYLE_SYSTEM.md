# Hệ thống chất lượng văn phong

## Mục tiêu

Lớp này giúp bản thảo bớt chung chung, cân xứng máy móc và tự ca ngợi. Nó không phải công cụ né AI detector. Chất lượng đến từ câu hỏi rõ, bằng chứng thật, quyết định của tác giả và biên tập có lý do.

## Vị trí trong kiến trúc

Lớp phong cách đứng sau governance, evidence và argument:

```text
Institutional rules + locked decisions
                ↓
Evidence → claims → argument → chapter draft
                ↓
Academic register → author voice → Vietnamese lint
                ↓
Whole-document review → DOCX render QA
```

Nếu một cảnh báo phong cách xung đột với quy định trường, nguồn, số liệu hoặc nghĩa của luận điểm, giữ nội dung đúng và ghi `KEEP_WITH_REASON`.

## Ba thành phần

### Ngữ vực theo chức năng

Mỗi loại phần có nhiệm vụ khác nhau. Hệ thống không áp một giọng duy nhất cho mở đầu, phương pháp, kết quả và thảo luận. Câu bị động, ngôi thứ nhất, hedging và signposting được hiệu chỉnh theo chức năng, không bị cấm tuyệt đối.

### Hồ sơ giọng tác giả

`AUTHOR_VOICE.md` chỉ chứa đặc điểm đã rút từ mẫu thật hoặc lựa chọn được tác giả xác nhận. Trước chương đầu tiên, agent tạo đoạn hiệu chỉnh 250–400 từ để tác giả sửa. Không có mẫu thì dùng giọng trung tính và giữ trạng thái `PROVISIONAL`.

### Linter tiếng Việt

`lint_vi_academic.py` phát hiện các mẫu giải thích được: mở bài rộng, phóng đại ý nghĩa, nguồn mơ hồ, chính xác giả, hedge xếp chồng, liên từ quá dày, câu quá dài và nhịp cấu trúc lặp. Công cụ không tự viết lại và không kết luận văn bản do AI hay con người tạo.

## Pipeline review

1. Evidence/citation audit.
2. Argument and limitation audit.
3. Relevance and redundancy edit.
4. Section-register calibration.
5. Author-voice calibration.
6. Deterministic style lint.
7. Whole-chapter reading.
8. Whole-thesis consistency pass.
9. Publication preflight and DOCX render QA.

## Cách thêm rule

Chỉ thêm rule khi có lỗi lặp lại trong nhiều đoạn và có thể mô tả tác hại đối với độ rõ hoặc học thuật. Mỗi rule cần:

- mã ổn định;
- ví dụ kích hoạt và ví dụ sạch;
- thông báo giải thích tác hại;
- gợi ý không làm thay đổi nghĩa;
- test chống false positive hợp lý.

Không thêm danh sách từ cấm dài chỉ vì một từ thường xuất hiện trong văn bản AI. Đánh giá chức năng và mật độ trong ngữ cảnh.

## Nguồn ý tưởng

Kiến trúc và rule tham khảo các repository liệt kê trong `docs/REFERENCES.md`. Hệ thống không sao chép nguyên skill hoặc biến các repo đó thành dependency runtime.
