# Chuẩn làm việc của leader và phản biện học thuật

Authority: yêu cầu trực tiếp của người dùng ngày 2026-10-08. Mục tiêu là lãnh đạo agent viết báo cáo có logic, lập luận, chiều sâu và một giọng tác giả nhất quán. Đây là chuẩn review bổ sung; không thay quy định HUIT, technical truth locks hay gate hiện hành. Không mở R3-1 hoặc Chương 4.

## 1. Cơ sở tham khảo và giới hạn tiếp cận

Nguồn dưới đây phục vụ phương pháp viết/review, không tự động trở thành tài liệu tham khảo kỹ thuật của luận văn. Ngày truy cập: 2026-10-08. Chỉ nêu phần thực sự đã đọc; không xem trường danh tiếng hay việc lưu trong repository là chứng nhận mọi kết luận của mẫu đều đúng.

| ID | Nguồn gốc | Phần đã đọc và điều có thể tham khảo |
|---|---|---|
| AR01 | [CMU — Final report guidelines](https://www.cs.cmu.edu/~prs/cap/Final.html) | Toàn trang hướng dẫn ngắn. Báo cáo nối mục tiêu, kiến trúc, lựa chọn triển khai và đánh giá; cần giải thích tiêu chí cùng thiết lập thực nghiệm. |
| AR02 | [CMU — Logic and Computation Senior Thesis](https://www.cmu.edu/dietrich/philosophy/undergraduate/logic-and-computation/thesis-writing.html) | Expectations, Learning Outcomes, Requirements. Vấn đề phải có phạm vi quản lý được; xác định đóng góp và ý nghĩa, phân biệt với tri thức có sẵn. Chuyên ngành khác ATTT nên chỉ tham khảo nguyên tắc lập luận. |
| AR03 | [Kieron Turk, A Web Application Vulnerability Scanner, Cambridge, Part II project, 2020](https://www.cl.cam.ac.uk/~kst36/documents/ba-dissertation.pdf) | Toàn văn truy cập được; đọc mục lục, đoạn lựa chọn thư viện, Chapter 4 Evaluation, đặc biệt 4.1–4.4, trang in 25–33. So sánh trên các test đã xác định, phân biệt false positive/negative và phân tích hạn chế crawler. Không áp các chỉ số của mẫu vào đồ án SMB khi chưa có dữ liệu tương ứng. |
| AR04 | [Nicolai Hellesnes, Ethical Hacking of an IoT camera, KTH, 2021](https://www.diva-portal.org/smash/get/diva2%3A1632105/FULLTEXT01.pdf) | Toàn văn truy cập được; đọc câu hỏi/phương pháp/phạm vi, cấu trúc từng phép thử, Chapter 6 và 7, trang in 54–58. Có phản tỉnh về phương pháp quá rộng làm giảm thời gian kiểm thử, kết luận giới hạn vào web application và firmware đã thử. Bậc second cycle; không áp mức yêu cầu học vị này nguyên xi lên đồ án HUIT. |
| AR05 | [Melanie L. Abbas, Network Security: An Evaluation of Security Policies and Firewall Implementations, UNI, 1998](https://scholarworks.uni.edu/etd/1592/) | Chỉ đọc metadata và abstract; toàn văn chưa lấy được. Tóm tắt nêu các tiêu chí so sánh công cụ và quan hệ với nhu cầu tổ chức. Không nhận xét văn phong/chất lượng từng chương; không dùng công nghệ năm 1998 làm chuẩn hiện hành. |
| AR06 | [CMU — Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html) | Hướng dẫn về tiêu chí, mức chất lượng và mô tả mức đạt. Dùng để làm nhận xét minh bạch; không coi bộ tiêu chí tự xây là thang điểm chính thức HUIT. |

Đã tìm thêm mẫu Linnaeus/Halmstad/Linköping nhưng truy cập toàn văn thất bại trong lượt này; không tính chúng là mẫu đã review. Quy định HUIT lấy từ INSTITUTION_PROFILE.md và tài liệu chính thức dự án đã khóa; không lấy rubric ngành khác trên web thay cho ATTT HUIT.

## 2. Nhận định sau đối chiếu

Đây là tổng hợp của reviewer, không phải quy định nguyên văn của các trường. Giá trị báo cáo nằm ở khả năng trả lời một vấn đề bằng lựa chọn có lý do và bằng chứng phù hợp. Truy vết là điều kiện để tin kết quả; chiều sâu còn cần giải thích kết quả hỗ trợ điều gì, phản bác điều gì và có hiệu lực đến đâu.

Review trước của leader tập trung nhiều vào integrity và locator. Những lỗi gán sai nguồn/lệnh vẫn phải sửa vì ảnh hưởng độ tin cậy. Tuy nhiên, từ các lượt sau, leader phải đánh giá cả mạch lập luận và sự chọn lọc dữ kiện; không lấy số claim, số ảnh hay tests PASS làm đại diện cho chất lượng học thuật.

Hai mẫu toàn văn cũng cần được đọc phản biện: so sánh công cụ chỉ công bằng khi scope/test/điều kiện tương thích; tự nhận phương pháp “thorough” không tự chứng minh tính đầy đủ. Kết quả tốt trong tập thử không đảm bảo mọi môi trường. Những bài học này là đánh giá của reviewer, không phải kết luận thực nghiệm mới về SMB.

## 3. Các câu hỏi bắt buộc khi leader duyệt

| Tiêu chí | Câu hỏi phản biện | Dấu hiệu cần sửa |
|---|---|---|
| Vấn đề và đóng góp | Mục này giải quyết câu hỏi nào? Người đọc hiểu thêm điều gì nhờ dữ liệu của tác giả? | Mô tả công cụ hoặc khái niệm nhưng không dùng trong lập luận. |
| Lựa chọn phương pháp | Vì sao chọn phép đo và thiết lập này? Nó quan sát được điều gì? | Chép thao tác mà không giải thích chức năng/điều kiện. |
| Cầu nối lập luận | Từ dữ kiện nào suy ra kết luận, qua bước giải thích nào? | Đặt ảnh/log rồi kết luận ngay; liên từ thay cho giải thích. |
| Đối chứng | Các nhánh có xuất phát phù hợp? Điều gì đổi, điều gì được kiểm hoặc chỉ kế thừa? | So sánh các quan sát khác phạm vi như cùng một phép đo. |
| Phản biện và bất định | Cách giải thích cạnh tranh nào còn khả dĩ? Dữ kiện thiếu làm giới hạn kết luận ra sao? | Chọn nguyên nhân chưa đo hoặc chỉ thêm câu “còn hạn chế” chung chung. |
| Kết luận | Mục đã trả lời phần nào của câu hỏi? Điều gì chưa kết luận được? | Kết đoạn “tạo nền tảng”, “rất quan trọng” không có phát hiện cụ thể. |
| Trình bày và giọng | Văn bản có chủ thể, quyết định và thuật ngữ nhất quán? Hình/bảng giúp hiểu gì? | Lặp caption bằng prose, nhiều nhãn máy móc, giọng đổi giữa các mục. |

Không ép mọi đoạn theo cùng một công thức. Một đoạn mô tả phép đo có thể ngắn; đoạn phân tích kết quả phải có quan hệ giải thích đủ rõ. Không kéo dài báo cáo bằng số trang, thêm lý thuyết không dùng hoặc lặp mọi screenshot.

## 4. Áp dụng cho Chương 3 hiện hành

- 3.1–3.2: người đọc hiểu điều kiện xuất phát và vì sao các nhánh có thể đối chiếu. Không kể lại toàn bộ thao tác thiết lập Chương 2.
- 3.3: phân tầng quan sát mạng, nhận diện dịch vụ, phương ngữ/capabilities và signing. Mỗi tầng trả lời câu hỏi riêng; không gộp thành bằng chứng xác nhận MS17-010.
- 3.4: giá trị là đối chiếu góc nhìn remote UNKNOWN với local UNPATCHED. Giải thích khác biệt về đối tượng quan sát và giới hạn của phép đo; nguyên nhân nội bộ của script vẫn chưa xác lập.
- 3.5–3.6: trình bày điều kiện, can thiệp và kết quả từng nhánh độc lập; làm rõ cấu hình, phương ngữ quan sát và trạng thái tiếp cận mạng là các loại dữ kiện khác nhau. Không suy ra tính sẵn sàng workload từ service Running.
- 3.7: so sánh theo các tiêu chí có chứng cứ; ô NOT MEASURED là giới hạn thật. Không xếp hạng chung nếu chưa có tiêu chí và phép đo phù hợp.
- 3.8: chốt các câu trả lời đã chứng minh và dữ kiện bàn giao. Khuyến nghị doanh nghiệp/đánh giá rủi ro tổng quát dành cho Chương 4 khi được mở.

Đây là chỉ dẫn nhiệm vụ lập luận, chưa phải prose mới hoặc phê duyệt blueprint. Không đổi kiến trúc 3.1–3.8 đã khóa.

## 5. Cách leader giao việc cho Antigravity

Mỗi prompt cần nêu câu hỏi người đọc, kết luận dự kiến có điều kiện, dữ kiện được dùng, lý do thứ tự trình bày và các nhận xét cần executor tự kiểm. Giữ ma trận truy vết trong tài liệu nội bộ; nội dung báo cáo cuối tập trung vào những dữ kiện cần cho câu trả lời. Coverage migration phải kiểm được và có quyết định retire; không đồng nghĩa giữ mọi dữ kiện cũ trong main text.

Leader đọc bản văn liên tục như người phản biện: có hiểu vấn đề và tin kết luận mà không mở ma trận không? Sau đó kiểm nguồn của các kết luận quan trọng và chọn hình/bảng theo chức năng. Review phải tách lỗi làm sai/mất căn cứ kết luận, lỗi cấu trúc làm người đọc không hiểu, và đề xuất biên tập nhỏ. Không chặn toàn bộ gate chỉ vì sở thích câu chữ hay cảnh báo linter; lỗi nguồn thật không được hạ thành lỗi phong cách.

“Như một cá nhân” nghĩa là một người chịu trách nhiệm về lựa chọn, lập trường có căn cứ và giọng xuyên suốt. Tuân theo AUTHOR_VOICE.md đã khóa; không tự thêm trải nghiệm/cảm xúc/ngôi thứ nhất hoặc giả làm giảng viên có chức danh thật. Vai trò giảng viên phản biện ở đây là cách đánh giá, không phải tư cách hội đồng chính thức.

## 6. Trạng thái và kiểm tra

Chuẩn bổ sung áp dụng cho các prompt/review tiếp theo. R3-0 vẫn WAITING_EXECUTOR_R3; báo cáo review R2 và prompt sửa R3 giữ nguyên. Không viết chương, không sửa khóa, không gửi message cho executor trong lượt này.

Lint chạy sau review nội dung; findings phải có disposition. Validator và unit tests chỉ kiểm sức khỏe dự án; không xác nhận chất lượng học thuật.
