# EXTERNAL BENCHMARK REVIEW — Kinh nghiệm tham khảo trước khi chấm

Ngày: 2026-10-05  
Vai trò: tài liệu hiệu chuẩn cho hội đồng phản biện.  
Nguyên tắc: **không thay thế tiêu chuẩn của repo**. Rubric trong `BOARD_REVIEW.md`, quy định HUIT, trạng thái nguồn và các quy tắc học thuật của repo vẫn là chuẩn chấm chính. Tài liệu bên ngoài chỉ dùng để học cách các luận văn/bài nghiên cứu ATTT tổ chức vấn đề, phương pháp, bằng chứng, thực nghiệm và giới hạn.

## 1. Mẫu trong nước đã có

Tiếp tục sử dụng `VIETNAM_BENCHMARK_REVIEW.md` làm lớp tham khảo trong nước. Các bài/luận văn trong đó chỉ cung cấp kinh nghiệm về cấu trúc phương pháp, cách tổ chức kết quả, hồ sơ tái lập và kết luận; không được dùng làm nguồn kỹ thuật SMB nếu không có căn cứ riêng.

## 2. Luận văn / đồ án / capstone quốc tế đã đối chiếu

### B01 — De La Salle University, Master in Information Security, 2022
- Orock EgbeAyuk, *Security assessment via vulnerability assessment: Case of the CCS-TSG of DLSU Manila*.
- Dạng: Master's Thesis / capstone paper, 73 trang.
- Điểm đáng học: xác định rõ đối tượng đánh giá thực tế, mục tiêu vulnerability assessment, dùng công cụ tự động để thu thập phát hiện, tạo báo cáo và tài liệu làm mốc cho các lần đánh giá sau.
- Kinh nghiệm áp dụng: một đồ án ATTT tốt không dừng ở mô tả công cụ; phải làm rõ **đối tượng → phương pháp → kết quả/bằng chứng → tài liệu hóa để tái kiểm tra**.
- Nguồn: https://animorepository.dlsu.edu.ph/etdm_comtech/8/

### B02 — Università Politecnica delle Marche, 2019/2020
- Simone Cappella, *Design and implementation of Penetration Testing techniques to evaluate cybersecurity in real system scenarios*.
- Dạng: luận văn cử nhân kỹ thuật, có PDF toàn văn.
- Điểm đáng học: tiêu đề và phạm vi đặt trọng tâm vào **thiết kế + triển khai kỹ thuật + đánh giá trên kịch bản hệ thống thực**, không biến pentest thành danh sách lệnh.
- Kinh nghiệm áp dụng: phần lý thuyết phải phục vụ trực tiếp thiết kế thực nghiệm; công cụ chỉ có ý nghĩa khi gắn với câu hỏi cần kiểm chứng.
- Nguồn: https://hdl.handle.net/20.500.12075/2682

### B03 — Technical University of Liberec, 2026
- Eliška Minaříková, *Penetration Testing as a Tool of Cybersecurity: Methodologies, Procedures and Practical Applications*.
- Dạng: thesis, 73 trang.
- Điểm đáng học từ abstract: phần lý thuyết bao gồm khung pháp lý/đạo đức và phương pháp pentest; phần thực hành triển khai ba kịch bản Gray Box, trong đó có hạ tầng Linux/Windows Server, Kali Linux và một công cụ Python riêng.
- Kinh nghiệm áp dụng: tách rõ **khung phương pháp** khỏi **các kịch bản thử nghiệm**, và mỗi kịch bản phải có phạm vi, điều kiện, dữ liệu quan sát và kết quả riêng.
- Nguồn: https://dspace.tul.cz/handle/15240/179111

### B04 — Università di Padova, 2022
- Jacopo Momesso, *CyberSecurity and Vulnerability Assessment: notions, approaches, tools and their application in a corporate context*.
- Dạng: luận văn cử nhân.
- Điểm đáng học: sau phần kiến thức và phương pháp là phần áp dụng vulnerability assessment vào bối cảnh doanh nghiệp cụ thể.
- Kinh nghiệm áp dụng: lý thuyết nên kết thúc bằng lý do nó được chọn và cách nó đi vào bài toán thực tế, tránh chương nền tảng đứng độc lập.
- Nguồn: https://hdl.handle.net/20.500.12608/52965

## 3. Bài báo khoa học / tổng quan dùng để hiệu chuẩn tiêu chuẩn học thuật

### B05 — Bertoglio & Zorzo, Journal of the Brazilian Computer Society, 2017
- *Overview and open issues on penetration test*.
- Nghiên cứu systematic mapping từ hơn 1.000 bản ghi và chọn 54 nghiên cứu chính.
- Điểm rất hữu ích cho việc chấm: nghiên cứu này dùng tiêu chí chất lượng gồm:
  1. đóng góp phải được xác định rõ;
  2. phải có đánh giá/case study/thực nghiệm hoặc dạng kiểm chứng kết quả;
  3. công cụ hoặc mô hình phải được mô tả rõ.
- Họ còn loại nghiên cứu phương pháp nếu **không đủ thông tin áp dụng** hoặc **không có đánh giá kết quả**.
- Kinh nghiệm áp dụng: đây là lý do hội đồng sẽ trừ mạnh một chương chỉ mô tả quy trình mà không chỉ ra cách kiểm chứng, dữ liệu và giới hạn.
- DOI: https://doi.org/10.1186/s13173-017-0051-1

### B06 — Shah & Mehtre, Procedia Computer Science, 2015
- *Vulnerability Assessment & Penetration Testing as a Cyber Defence Technology*.
- Điểm đáng học: xem VAPT như một **vòng đời**, không chỉ một thao tác quét hoặc exploit; phát hiện phải dẫn tới xử lý/giảm thiểu và đánh giá lại.
- Kinh nghiệm áp dụng: báo cáo nên nối được chuỗi **phát hiện → xác minh → khắc phục → đối chiếu sau khắc phục**.
- DOI: https://doi.org/10.1016/j.procs.2015.07.458

### B07 — Ghanem et al., 2023
- *Penetration Taxonomy: A Systematic Review on the Penetration Process, Framework, Standards, Tools, and Scoring Methods*.
- Điểm đáng học: phương pháp pentest có nhiều framework/standard/tool/scoring khác nhau; việc chọn chúng phải phụ thuộc nhu cầu và bối cảnh đánh giá.
- Kinh nghiệm áp dụng: không cộng điểm chỉ vì báo cáo nêu nhiều công cụ hoặc tiêu chuẩn; phải giải thích **vì sao chọn** và chúng hỗ trợ câu hỏi nghiên cứu nào.
- DOI: https://doi.org/10.3390/su151310471

### B08 — Heiding, Katsikeas & Lagerström, Computer Science Review, 2023
- *Research communities in cyber security vulnerability assessments: A comprehensive literature review*.
- Điểm đáng học: lĩnh vực vulnerability assessment/ethical hacking bao gồm nhiều loại mô hình và bối cảnh; white/black/gray-box và các lớp công cụ không nên bị dùng lẫn nghĩa.
- Kinh nghiệm áp dụng: báo cáo cần định nghĩa chính xác loại đánh giá đang làm và ranh giới suy luận của từng kỹ thuật.
- DOI: https://doi.org/10.1016/j.cosrev.2023.100551

### B09 — Akhtar & Rawol, bài nghiên cứu peer-reviewed lưu tại University of Cambridge repository
- *Uncovering Cybersecurity Vulnerabilities: A Kali Linux Investigative Exploration Perspective*.
- Methodology nêu bốn giai đoạn: Preparation, Information Gathering, Simulated Attack, Reporting.
- Kinh nghiệm áp dụng: phạm vi/ủy quyền và reporting là một phần của phương pháp, không phải phần phụ sau thao tác kỹ thuật.
- Nguồn: https://www.repository.cam.ac.uk/handle/1810/371529

## 4. Các mẫu chất lượng rút ra để dùng khi phản biện

Các tài liệu ngoài repo cho thấy các công trình ATTT có sức thuyết phục thường có những đặc điểm lặp lại sau:

1. **Câu hỏi/mục tiêu rõ trước công cụ.** Không tổ chức chương theo kiểu “Nmap là gì, Metasploit là gì” nếu không nối chúng vào một câu hỏi cần trả lời.
2. **Phương pháp phải tái lập được.** Phạm vi, hệ thống, phiên bản, topology, điều kiện đầu vào, dữ liệu quan sát, tiêu chí dừng và tiêu chí thành công/thất bại phải đủ rõ để người khác hiểu cách lặp lại.
3. **Tách phát hiện và xác minh.** Scan/indicator không được đồng nhất với vulnerability confirmed hoặc exploit success.
4. **Có bằng chứng đánh giá.** Một quy trình lý thuyết không đủ mạnh nếu không định nghĩa được cách nó sẽ được kiểm chứng bằng case study, experiment, log, packet capture, trạng thái hệ thống hoặc đối chứng phù hợp.
5. **Giải thích lựa chọn phương pháp.** Công cụ/framework được chọn vì phạm vi và đặc tính cần đo, không vì phổ biến.
6. **Báo cáo cả giới hạn và kết quả không xác định.** Timeout, denied, crash, filtered hoặc thiếu phản hồi không được tùy tiện biến thành “an toàn” hay “không có lỗ hổng”.
7. **Chuỗi remediation phải khép kín.** Kết quả trước/sau biện pháp bảo vệ có giá trị hơn một danh sách khuyến nghị chung.
8. **Đóng góp phải được gọi đúng tên.** Kiến thức SMB, MS17-010, Nmap, Metasploit là kiến thức nền; đóng góp của đồ án nằm ở thiết kế mô hình, quy trình kiểm chứng, cách tổ chức bằng chứng, kết quả thực nghiệm và phân tích/khuyến nghị trong phạm vi đã đo.
9. **Threats/limitations phải xuất hiện trong lập luận.** Không đợi tới cuối báo cáo mới nói rằng kết quả chỉ áp dụng cho một Windows build/topology/cấu hình cụ thể.
10. **Reporting là một phần của nghiên cứu.** Bằng chứng phải truy ngược được tới lượt thử, cấu hình và thời điểm; bảng tổng hợp không được tách khỏi dữ liệu gốc.

## 5. Cách dùng khi chấm bài agent

Thứ tự ưu tiên bắt buộc:
1. Tiêu chuẩn của repo và quy định HUIT.
2. Claim/source/data hiện có trong dự án.
3. Nội dung thực tế của bài agent nộp.
4. Benchmark bên ngoài trong file này chỉ dùng để đặt câu hỏi phản biện và hiệu chuẩn mức kỳ vọng.

Không trừ điểm chỉ vì báo cáo khác cấu trúc một luận văn bên ngoài. Không cộng điểm vì bắt chước cấu trúc bên ngoài. Chỉ dùng benchmark để nhận diện các rủi ro như: lý thuyết không gắn phương pháp, thiếu đánh giá, thiếu khả năng tái lập, thiếu giới hạn, hoặc nhầm giữa phát hiện và xác minh.
