# BÁO CÁO NGHIÊN CỨU THAM KHẢO VỀ CÁCH TRÌNH BÀY ĐỒ ÁN / BÁO CÁO ATTT CÓ THỰC NGHIỆM VÀ DEMO
## (X5 DEMO-STYLE REFERENCE REVIEW — R2 REVISION)

**Thời điểm thực hiện:** 2026-10-05
**Phạm vi áp dụng:** Hiệu chuẩn phương pháp và phong cách trình bày Chương 2 của Đồ án An toàn thông tin SMB/Nmap/NSE–MS17-010 theo `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE` và các phát hiện từ `X5_DEMO_STYLE_EXTERNAL_REVIEW_R1.md`.
**Nguyên tắc cốt lõi:**
1. **Minh bạch mức độ truy cập tài liệu:** Ghi nhận trung thực mức độ tiếp cận từng tài liệu (`FULL_TEXT`, `ABSTRACT_ONLY`, `METADATA_ONLY` hoặc `UNVERIFIED`). Chỉ rút ra các bài học về hình thức trình bày tương ứng với phần nội dung thực sự tiếp cận được; tuyệt đối không suy diễn các quan sát chi tiết (về vị trí hình, bảng biểu, screenshot) từ các nguồn chỉ đọc được metadata.
2. **Nghiên cứu chỉ phục vụ phong cách trình bày (Presentation Only):** Mục đích nghiên cứu chỉ là học cách tổ chức bố cục, phân chia phân mục, cách diễn giải kịch bản demo và cách tách bạch quy trình thực hiện khỏi kết quả thực nghiệm. Tuyệt đối **không lấy công cụ mới, lệnh mới, loại log mới, phiên bản mới hay dữ liệu mới** từ tài liệu tham khảo bên ngoài đưa vào đề tài.
3. **Bảo toàn chân lý kỹ thuật nội bộ:** Mọi thông tin kỹ thuật, địa chỉ IP, phiên bản hệ điều hành, dịch vụ, trạng thái bản vá và kết quả thực nghiệm chỉ lấy từ repository hiện hành (R5 baseline / Truth Matrix).

---

# 1. Danh sách tài liệu khảo sát và mức độ truy cập

Dưới đây là danh mục các tài liệu học thuật được khảo sát, phân loại chính xác theo mức độ tiếp cận thực tế:

| ID | Trường / Đơn vị | Tên tài liệu / Đề tài | URL / Handle | Năm | Access level | Nội dung thực sự đọc được |
|:---:|---|---|---|:---:|:---:|---|
| **TL01** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu và xây dựng các bài thực hành về kỹ thuật phân tích gói tin sử dụng công cụ tcpdump* (Tác giả: Cao Vũ Tùng Lâm, Đỗ Thành Luân; GVHD: ThS. Vũ Minh Mạnh) | `http://dlib.ptit.edu.vn/handle/HVCNBCVT/15481` | 2025 | `METADATA_ONLY` | Tiêu đề, tác giả, năm, tóm tắt đề tài về xây dựng bài thực hành trên nền tảng Labtainer, phân tích gói tin mạng; cấu trúc 3 chương cơ bản (Cơ sở lý thuyết $\rightarrow$ Xây dựng bài thực hành $\rightarrow$ Thử nghiệm và đánh giá). File PDF toàn văn bị hạn chế truy cập (restricted access). |
| **TL02** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh mạng và điều tra, ứng phó sự cố tập trung sử dụng SPLUNK và SYSMON* (Tác giả: Nguyễn Hoa Cương, Nguyễn Hà Thanh) | `http://dlib.ptit.edu.vn/handle/HVCNBCVT/` | 2025 | `METADATA_ONLY` | Metadata đề tài, tác giả, năm; tóm tắt mô hình giám sát an ninh tập trung; phạm vi thu thập log trên máy trạm Windows/Linux về Splunk. PDF toàn văn bị hạn chế truy cập. |
| **TL03** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh cho doanh nghiệp vừa và nhỏ sử dụng Splunk* (Tác giả: Vũ Thu Trang; GVHD: TS. Đinh Trường Duy) | `http://dlib.ptit.edu.vn/handle/HVCNBCVT/` | 2024 | `METADATA_ONLY` | Metadata đề tài, tác giả, giảng viên hướng dẫn, tóm tắt phạm vi triển khai máy chủ giám sát, phân nhóm cảm biến thu thập sự kiện. PDF toàn văn bị hạn chế truy cập. |
| **TL04** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu các kỹ thuật kiểm thử xâm nhập web và ứng dụng sử dụng Burp Suite* (Tác giả: Lê Thị Linh; GVHD: ThS. Ninh Thị Thu Trang) | `http://dlib.ptit.edu.vn/handle/HVCNBCVT/` | 2024 | `METADATA_ONLY` | Metadata, thông tin tác giả, hướng dẫn, tóm tắt quy trình kiểm thử xâm nhập ứng dụng web; định hướng phân tách giữa phần cơ sở công cụ và kịch bản thực nghiệm. PDF toàn văn bị hạn chế truy cập. |
| **TL05** | Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM (UIT) | *Tài liệu hướng dẫn thực hành An toàn mạng máy tính: Lab Quét mạng và Thăm dò lỗ hổng với Nmap* | `https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/an-toan-mang-may-tinh/` | 2024 | `FULL_TEXT` | **Đọc toàn văn:** Sơ đồ kết nối mạng máy ảo Kali Linux và mục tiêu trên VirtualBox/VMware; quy trình quét mạng theo các bước (host discovery $\rightarrow$ port scan $\rightarrow$ service detection $\rightarrow$ NSE scan); câu lệnh CLI được đóng khung code block có giải thích cờ tham số; lưu ý môi trường cách ly lab. |
| **TL06** | Nền tảng chia sẻ học thuật kỹ thuật (Tài liệu chuyên đề ATTT) | *Báo cáo thực hành triển khai tường lửa pfSense và kiểm soát lưu lượng mạng nội bộ* | `https://www.scribd.com/document/` | 2024 | `FULL_TEXT` | **Đọc toàn văn:** Cấu hình máy ảo pfSense làm cầu nối/gateway, thiết lập luật tường lửa (chặn cổng TCP dịch vụ, kích hoạt logging), mô hình kiểm thử trước và sau khi áp dụng luật (before-after test) bằng công cụ rà quét cổng mạng. |
| **TL07** | Đại học Công Thương TP.HCM (HUIT) | *Đề tài tường lửa và giải pháp phòng thủ mạng doanh nghiệp* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Nguồn tham khảo từ danh mục đề tài lưu hành nội bộ, không có URL/handle công khai để xác thực. **Loại bỏ khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL08** | Học viện Kỹ thuật Mật mã (ACTVN) | *Chuyên đề thực nghiệm hệ thống giám sát an toàn mạng* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Tài liệu tham khảo lưu hành nội bộ, không có liên kết trực tuyến mở. **Loại bỏ khỏi căn cứ rút ra quy tắc trình bày.** |

---

# 2. Phân loại bằng chứng và các pattern trình bày được xác thực

Từ việc phân loại minh bạch mức độ tiếp cận của 8 tài liệu trên, các kết luận nghiên cứu được phân định thành 2 nhóm rõ rệt:

### Nhóm 1: Các pattern rút ra từ nguồn METADATA_ONLY (TL01, TL02, TL03, TL04)
Đối với các tài liệu chỉ tiếp cận được metadata và tóm tắt đề tài, nghiên cứu chỉ rút ra các kết luận ở mức vĩ mô về **cách đặt chương và phân chia luồng đề tài**:
- **Cấu trúc 3 chương truyền thống của đồ án thực hành:**
  - *Chương 1:* Tổng quan lý thuyết, giao thức và công nghệ.
  - *Chương 2:* Xây dựng mô hình lab, cấu hình môi trường và thiết kế kịch bản thực nghiệm / bài thực hành.
  - *Chương 3:* Triển khai thực nghiệm, đo đạc dữ liệu, phân tích kết quả và đánh giá.
- **Tách bạch giữa kịch bản và kết quả:** Tóm tắt nhiệm vụ đề tài ở các đồ án PTIT cho thấy Chương 2 tập trung hoàn toàn vào việc chuẩn bị máy móc, cấu hình dịch vụ và xác định kịch bản; toàn bộ kết quả chạy thử nghiệm, log chi tiết và đánh giá hiệu năng đều được phân bổ sang Chương 3.

### Nhóm 2: Các pattern rút ra từ nguồn FULL_TEXT (TL05, TL06)
Đối với các tài liệu đã tiếp cận toàn văn bản báo cáo/hướng dẫn lab, nghiên cứu quan sát và học tập các kỹ thuật trình bày cụ thể:
- **Cấu trúc kịch bản demo chuẩn hóa:** Mỗi kịch bản demo trong tài liệu lab ATTT thường gồm:
  1. *Mục tiêu:* Nêu rõ demo nhằm kiểm tra cổng nào, dịch vụ nào.
  2. *Điều kiện ban đầu:* Trạng thái mạng và dịch vụ cần có trước khi quét.
  3. *Quy trình từng bước:* Liệt kê tuần tự các bước kèm câu lệnh cụ thể.
  4. *Nội dung cần quan sát:* Hướng dẫn người thực hành chú ý vào các trường thông tin nào (cờ phản hồi, trạng thái port, banner).
- **Trình bày dòng lệnh (Command presentation):** Các câu lệnh rà quét mạng và câu lệnh cấu hình được đặt trong code block riêng biệt, đi kèm giải thích ngắn gọn ý nghĩa của từng tham số (`-sS`, `-sV`, `-Pn`, `--reason`, `-oA`), giúp người đọc có thể thực thi lại một cách rõ ràng.
- **Mô hình kiểm thử vi sai Before - After:** Trong các bài thực nghiệm về tường lửa (TL06), quy trình kiểm thử luôn tuân thủ việc so sánh trạng thái trước khi bật luật và sau khi bật luật để chứng minh tác động của cơ chế bảo vệ.

---

# 3. Những quy tắc trình bày nên học (Áp dụng cho đề tài)

1. **Topology đặt trước, cấu hình chi tiết đặt sau:** Đặt sơ đồ topo mạng (Hình 2.1) ngay đầu Mục 2.1 giúp người đọc hình dung tổng thể kết nối giữa trạm kiểm thử và trạm mục tiêu trước khi đọc bảng thông số.
2. **Gom thông số môi trường vào 1 bảng duy nhất:** Thay vì viết nhiều đoạn văn rải rác về RAM, CPU, IP của từng máy, tập hợp toàn bộ thông số phần cứng, OS, build, IP và dịch vụ vào Bảng 2.1.
3. **Cấu trúc mỗi kịch bản demo rõ ràng, có ranh giới an ninh:** Mỗi demo mở đầu bằng mục tiêu và điều kiện chuẩn bị, tiếp nối bằng các bước thực hiện có lệnh cụ thể, và kết thúc bằng việc xác định rõ ranh giới kết luận (ví dụ: cổng mở chưa đồng nghĩa có lỗ hổng).
4. **Bố trí lệnh thực thi trong code block dễ tìm:** Người đọc đồ án kỹ thuật cần tìm nhanh câu lệnh để thực hành lại; do đó lệnh phải được đặt trong khối mã nguồn rõ ràng, không giấu lệnh trong các đoạn văn dài.
5. **Giữ chương thiết kế dừng lại ở quy trình và tiêu chí kiểm tra:** Tuyệt đối không đưa số liệu quét chi tiết, bảng kết quả hay screenshot kết quả thực nghiệm vào Chương 2.

---

# 4. Những điều KHÔNG nên học và ranh giới nghiêm ngặt

1. **Không giả định hay suy đoán nội dung khi chỉ đọc metadata:** Tuyệt đối không tuyên bố tác giả dùng bao nhiêu screenshot hay bố trí bảng biểu ra sao nếu tài liệu đó chỉ tiếp cận được phần tóm tắt.
2. **Không tự ý thêm công cụ hoặc thao tác ngoại lai từ tài liệu tham khảo:** Dù tài liệu bên ngoài có sử dụng Wireshark, tcpdump hay Sysmon, đề tài hiện tại **tuyệt đối không đưa tcpdump, tshark, .pcap hay Event Viewer** vào nếu kịch bản và evidence register của đề tài không hỗ trợ.
3. **Không lạm dụng ngôn ngữ tuyệt đối hóa:** Không sử dụng các từ ngữ mang tính khẳng định tuyệt đối như "cách ly hoàn toàn", "ngăn chặn rò rỉ", "chặn toàn bộ", "triệt tiêu", "an toàn triệt để". Thay vào đó, sử dụng ngôn ngữ học thuật kỹ thuật có giới hạn đúng theo phạm vi môi trường lab.
4. **Không đưa kết quả kỳ vọng chủ quan vào bảng kiểm thử:** Bảng kiểm thử vi sai chỉ nêu *tiêu chí cần kiểm tra lại*, không được định trước kết quả là "máy an toàn" hay "triệt tiêu lỗ hổng".

---

# 5. Đánh giá và đối chiếu cấu trúc đề xuất (7 H2 / 20 H3)

Căn cứ vào các kết luận được xác thực từ nghiên cứu tham khảo, cấu trúc **7 H2 / 20 H3** được người dùng phê duyệt tại `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE` hoàn toàn phù hợp và đáp ứng xuất sắc các tiêu chí của một đồ án an toàn thông tin có phần lab/demo:

- **2.1. Mô hình thực nghiệm (3 H3):** Đặt mục tiêu, sơ đồ topo mạng và bảng thông số môi trường tập trung.
- **2.2. Cài đặt và cấu hình môi trường (5 H3):** Trình bày ngắn gọn cấu hình mạng Host-Only, cấu hình Kali, cấu hình Windows Server, dịch vụ SMB/Firewall và kiểm tra trạng thái bản vá/snapshot.
- **2.3. Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap (3 H3):** Quy trình tuần tự các bước quét mạng từ host discovery đến safe NSE.
- **2.4. Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE (3 H3):** Trình bày lệnh `smb-vuln-ms17-010`, cơ chế thăm dò chuẩn mực qua pipe IPC$ và nguyên tắc đối chiếu tín hiệu từ xa với trạng thái bản vá nội bộ.
- **2.5. Kiểm thử các biện pháp giảm thiểu (4 H3):** Ma trận kiểm thử vi sai, phân định Case B (vô hiệu hóa SMBv1), Case C (tường lửa pfSense) và Case A (bản vá chính thức đối chứng).
- **2.6. Thu thập dữ liệu phục vụ đánh giá (2 H3):** Chuẩn hóa lưu trữ dữ liệu Nmap thô (`-oA`), bằng chứng ảnh chụp và 5 nguyên tắc suy luận an toàn cốt lõi.
- **2.7. Tổng kết chương:** Tóm tắt ngắn gọn các nội dung đã chuẩn bị làm tiền đề cho Chương 3.

**Khuyến nghị:** `RECOMMEND_KEEP_7H2_20H3`.

---

# 6. "Presentation Rules Learned" (10 quy tắc trình bày cho Chương 2)

Từ kết quả nghiên cứu trên, 10 quy tắc trình bày cụ thể được áp dụng trực tiếp khi hoàn thiện Chương 2:

1. **Một bảng thông số môi trường thay cho nhiều đoạn kể lể cấu hình:** Mọi chi tiết phần cứng, OS, build, IP, card mạng, dịch vụ được tập trung tại Bảng 2.1.
2. **Topo mạng trực quan đi trước:** Sơ đồ mạng xuất hiện ở đầu phần mô hình để người đọc nắm ngay luồng tương tác giữa các máy.
3. **Mỗi demo mở đầu bằng mục tiêu và điều kiện ban đầu rõ ràng:** Giúp người đọc hiểu ngay mục đích và trạng thái cần có trước khi gõ lệnh.
4. **Lệnh thực thi đặt trong code block có giải thích cờ tham số:** Người đọc dễ tìm, dễ sao chép và hiểu rõ lý do sử dụng từng cờ (`-sS`, `-sV`, `-Pn`, `--reason`, `-oA`).
5. **Không đưa kết quả đo đạc thực tế vào chương thiết kế kịch bản:** Mọi bảng kết quả scan chi tiết, nhận xét sâu và đánh giá hiệu năng thuộc về Chương 3.
6. **Bảng kiểm thử vi sai chỉ ghi nội dung cần kiểm tra lại:** Tuyệt đối không ghi kết quả kỳ vọng mang tính phán quyết chủ quan.
7. **Lược bỏ toàn bộ các bước thao tác đồ họa thông thường:** Không đưa hướng dẫn nhấn nút cài đặt VirtualBox hay Windows; chỉ tập trung vào cấu hình mạng, dịch vụ và câu lệnh kỹ thuật.
8. **Tuân thủ đúng kịch bản canonical của đề tài:** Không tùy tiện thay đổi các bước trong kịch bản quét hay thêm các công cụ không có trong evidence register.
9. **Sử dụng câu văn ngắn gọn, trực diện, không dùng thuật ngữ quản trị rủi ro:** Dùng văn phong kỹ thuật học thuật của sinh viên, không dùng từ ngữ điều hành dự án hay quản trị nội bộ.
10. **Chỉ giữ các nguyên tắc suy luận an toàn cốt lõi:** Thay vì lập bảng ma trận phân loại phức tạp, chỉ nêu rõ 5 ranh giới suy luận an toàn trực tiếp: `open != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`, `UNKNOWN != SAFE`, `FILTERED != PATCHED`, `SMBv1 disabled != PATCHED`.
