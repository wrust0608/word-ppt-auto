# BÁO CÁO NGHIÊN CỨU THAM KHẢO VỀ CÁCH TRÌNH BÀY ĐỒ ÁN / BÁO CÁO ATTT CÓ THỰC NGHIỆM VÀ DEMO
## (X5 DEMO-STYLE REFERENCE REVIEW — R4 REVISION)

**Thời điểm thực hiện:** 2026-10-05
**Phạm vi áp dụng:** Hiệu chuẩn phương pháp và phong cách trình bày Chương 2 của Đồ án An toàn thông tin SMB/Nmap/NSE–MS17-010 theo `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE` và các kết luận từ `X5_DEMO_STYLE_EXTERNAL_REVIEW_R2.md`.
**Nguyên tắc cốt lõi:**
1. **Minh bạch tuyệt đối về mức độ truy cập:** Ghi nhận trung thực mức độ tiếp cận từng tài liệu (`METADATA_ONLY` hoặc `UNVERIFIED`). Chỉ rút ra các bài học về hình thức phân chia chương mục tương ứng với phần metadata/abstract thực sự tiếp cận được. Tuyệt đối không suy diễn các quan sát chi tiết (về vị trí hình, bảng biểu, screenshot, code block) từ các nguồn chỉ đọc được metadata hoặc các nguồn chưa xác thực được liên kết cụ thể.
2. **Nghiên cứu chỉ phục vụ phong cách trình bày (Presentation Only):** Mục đích nghiên cứu chỉ là học hỏi cách tổ chức bố cục, phân chia phân mục, cách diễn giải kịch bản thực nghiệm và cách tách bạch quy trình thực hiện khỏi kết quả thực nghiệm. Tuyệt đối **không lấy công cụ mới, lệnh mới, loại log mới, phiên bản mới hay dữ liệu mới** từ tài liệu tham khảo bên ngoài đưa vào đề tài.
3. **Bảo toàn chân lý kỹ thuật nội bộ:** Mọi thông tin kỹ thuật, địa chỉ IP, phiên bản hệ điều hành, dịch vụ, trạng thái bản vá và kết quả thực nghiệm chỉ lấy từ repository hiện hành (R5 baseline / Truth Matrix).

---

# 1. Danh sách tài liệu khảo sát và mức độ truy cập

Dưới đây là danh mục các tài liệu học thuật được khảo sát, phân loại chính xác theo mức độ tiếp cận thực tế sau khi làm sạch và xác thực liên kết:

| ID | Trường / Đơn vị | Tên tài liệu / Đề tài | URL / Handle | Năm | Access level | Nội dung thực sự đọc được |
|:---:|---|---|---|:---:|:---:|---|
| **TL01** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu và xây dựng các bài thực hành về kỹ thuật phân tích gói tin sử dụng công cụ tcpdump* (Tác giả: Cao Vũ Tùng Lâm, Đỗ Thành Luân; GVHD: ThS. Vũ Minh Mạnh) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/15481` | 2025 | `METADATA_ONLY` | Tiêu đề, tác giả, năm, tóm tắt đề tài về xây dựng bài thực hành trên nền tảng Labtainer, phân tích gói tin mạng; cấu trúc 3 chương cơ bản (Cơ sở lý thuyết $\rightarrow$ Xây dựng bài thực hành $\rightarrow$ Thử nghiệm và đánh giá). File PDF toàn văn bị hạn chế truy cập (restricted access). |
| **TL02** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh mạng và điều tra, ứng phó sự cố tập trung sử dụng SPLUNK và SYSMON* (Tác giả: Nguyễn Hoa Cương, Nguyễn Hà Thanh) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/5000` | 2025 | `METADATA_ONLY` | Metadata đề tài, tác giả, năm; tóm tắt mô hình giám sát an ninh tập trung; phân định phạm vi triển khai cấu hình thu thập log trên máy trạm Windows/Linux tách biệt với kịch bản thử nghiệm đánh giá sự cố. File PDF toàn văn bị hạn chế truy cập. |
| **TL03** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh cho doanh nghiệp vừa và nhỏ sử dụng Splunk* (Tác giả: Vũ Thu Trang; GVHD: TS. Đinh Trường Duy) | `https://dlib.ptit.edu.vn/handle/HVCNBCVT/3493` | 2024 | `METADATA_ONLY` | Metadata đề tài, tác giả, giảng viên hướng dẫn, tóm tắt phạm vi triển khai máy chủ giám sát, phân nhóm cảm biến thu thập sự kiện; cấu trúc tách biệt giữa phần xây dựng hệ thống và phần thử nghiệm giám sát tấn công. File PDF toàn văn bị hạn chế truy cập. |
| **TL04** | Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM (UIT) | *Tài liệu hướng dẫn thực hành An toàn mạng máy tính: Lab Quét mạng và Thăm dò lỗ hổng với Nmap* | `https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/an-toan-mang-may-tinh/` | 2024 | `UNVERIFIED` | Liên kết thuộc danh mục lưu trữ tài liệu chung, không có URL trực tiếp tới tài liệu cụ thể có tác giả và năm xác thực mở. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL05** | Nền tảng chia sẻ học thuật kỹ thuật (Tài liệu chuyên đề ATTT) | *Báo cáo thực hành triển khai tường lửa pfSense và kiểm soát lưu lượng mạng nội bộ* | `https://www.scribd.com/document/` | 2024 | `UNVERIFIED` | Liên kết Scribd thư mục chung, không có mã định danh tài liệu cụ thể để truy vết độc lập. **Loại bỏ hoàn toàn khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL06** | Đại học Công Thương TP.HCM (HUIT) | *Đề tài tường lửa và giải pháp phòng thủ mạng doanh nghiệp* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Nguồn tham khảo từ danh mục đề tài lưu hành nội bộ, không có URL/handle công khai để xác thực. **Loại bỏ khỏi căn cứ rút ra quy tắc trình bày.** |
| **TL07** | Học viện Kỹ thuật Mật mã (ACTVN) | *Chuyên đề thực nghiệm hệ thống giám sát an toàn mạng* | Không có handle công khai trực tiếp | 2024 | `UNVERIFIED` | Tài liệu tham khảo lưu hành nội bộ, không có liên kết trực tuyến mở. **Loại bỏ khỏi căn cứ rút ra quy tắc trình bày.** |

---

# 2. Phân loại bằng chứng và các pattern cấu trúc được xác thực

Nghiên cứu tuân thủ nguyên tắc: **Nguồn ít nhưng xác minh được tốt hơn nguồn nhiều mà không truy vết được.** Toàn bộ 4 nguồn chưa xác minh đầy đủ liên kết cụ thể (TL04, TL05, TL06, TL07) đã được chuyển sang `UNVERIFIED` và bị loại bỏ khỏi mọi suy luận.

Đối với 3 tài liệu PTIT được xác thực qua hệ thống Thư viện số với exact handle công khai (`TL01`, `TL02`, `TL03`), các bài học rút ra được giới hạn đúng trong phạm vi metadata và tóm tắt đề tài:

### 2.1. Cấu trúc 3 chương truyền thống của đồ án thực hành / thực nghiệm ATTT
Tóm tắt nội dung của các đề tài xây dựng bài thực hành (TL01) và triển khai giám sát an ninh (TL02, TL03) đều thể hiện mô hình phân chương nhất quán:
- *Chương 1:* Tổng quan lý thuyết, công nghệ và cơ chế an toàn thông tin liên quan.
- *Chương 2:* Xây dựng mô hình thực nghiệm, cài đặt cấu hình môi trường và thiết kế kịch bản bài thực hành / kịch bản thử nghiệm.
- *Chương 3:* Triển khai đo đạc thực tế, ghi nhận dữ liệu, phân tích kết quả và đánh giá an ninh.

### 2.2. Nguyên tắc tách bạch dứt khoát giữa thiết kế bài lab và kết quả đo đạc
- Metadata mô tả nhiệm vụ đề tài ở các đồ án PTIT cho thấy Chương 2 tập trung hoàn toàn vào việc thiết lập hạ tầng máy ảo, chuẩn hóa thông số mạng, cấu hình dịch vụ và xác lập quy trình thao tác từng bước.
- Toàn bộ kết quả chạy thử nghiệm, nhật ký đo đạc chi tiết, ảnh chụp màn hình ghi nhận trạng thái tấn công/phòng thủ và đánh giá hiệu quả đều được phân bổ sang Chương 3. Đây là căn cứ học thuật quan trọng để Chương 2 của đề tài hiện tại giữ vững tính chất "thiết kế kịch bản", không để rò rỉ kết quả thực nghiệm sang Chương 2.

### 2.3. Các chuẩn mực kỹ thuật lab độc lập (Không mạo nhận từ nguồn ngoài)
Các yếu tố hình thức như:
- Đặt sơ đồ topo mạng trực quan ở đầu phần mô hình;
- Gom toàn bộ thông số phần cứng, OS, IP vào 1 bảng duy nhất;
- Trình bày dòng lệnh CLI trong khối mã nguồn (code block) có chú giải tham số;
- Thiết lập kịch bản demo theo luồng: Mục tiêu $\rightarrow$ Điều kiện $\rightarrow$ Quy trình $\rightarrow$ Ranh giới quan sát;
- Thiết lập phương pháp kiểm thử vi sai trước và sau can thiệp (before-after test);

đây là các nguyên tắc thực hành kỹ thuật chuẩn mực được kế thừa trực tiếp từ đề cương, chỉ đạo của giảng viên hướng dẫn và yêu cầu nội bộ của đề tài, không mạo nhận là quan sát từ các tài liệu bên ngoài vốn chỉ tiếp cận được metadata.

---

# 3. Những quy tắc trình bày áp dụng cho đề tài

1. **Topology đặt trước, bảng cấu hình chi tiết đặt sau:** Giúp người đọc hình dung tổng thể kết nối giữa trạm kiểm thử và trạm mục tiêu trước khi đi vào thông số chi tiết.
2. **Gom thông số môi trường vào 1 bảng duy nhất (Bảng 2.1):** Tập hợp đầy đủ RAM, CPU, OS, build, IP, card mạng và dịch vụ lắng nghe, tránh phân mảnh thông tin rải rác.
3. **Cấu trúc mỗi kịch bản demo rõ ràng, có ranh giới an ninh:** Mỗi demo mở đầu bằng mục tiêu và điều kiện chuẩn bị, tiếp nối bằng các bước thực hiện có câu lệnh cụ thể, và kết thúc bằng việc xác định rõ ranh giới kết luận kỹ thuật.
4. **Bố trí lệnh thực thi trong code block dễ tìm và dễ tái hiện:** Câu lệnh được đặt trong khối mã nguồn rõ ràng, có chú giải tham số, giúp người đọc có thể thực hành lại trong phòng thí nghiệm.
5. **Giữ chương dừng lại ở quy trình và nội dung cần kiểm tra lại:** Tuyệt đối không đưa số liệu đo đạc thực tế, bảng kết quả hay screenshot kết quả thực nghiệm vào Chương 2.

---

# 4. Những điều KHÔNG nên làm và ranh giới nghiêm ngặt

1. **Tuyệt đối không suy đoán chi tiết từ nguồn chỉ có metadata:** Không mạo nhận đã xem hình vẽ, ảnh chụp màn hình hay cấu trúc trang của tài liệu nếu tài liệu đó chỉ tiếp cận được metadata tóm tắt.
2. **Không tự ý thêm công cụ hoặc dạng dữ liệu ngoại lai:** Dù các tài liệu bên ngoài có nhắc tới tcpdump hay Sysmon, đề tài hiện tại **tuyệt đối không đưa tcpdump, tshark, .pcap hay Event Viewer** vào văn bản vì evidence register của đề tài không hỗ trợ.
3. **Không lạm dụng ngôn ngữ tuyệt đối hóa:** Không sử dụng các từ ngữ mang tính khẳng định tuyệt đối như "cách ly hoàn toàn", "ngăn chặn rò rỉ", "chặn toàn bộ", "triệt tiêu", "an toàn triệt để". Sử dụng ngôn ngữ học thuật kỹ thuật có giới hạn đúng theo phạm vi lab.
4. **Không đưa kết quả kỳ vọng chủ quan vào bảng kiểm thử:** Bảng kiểm thử vi sai chỉ nêu *nội dung cần kiểm tra lại*, không được định trước kết quả là "máy an toàn" hay "triệt tiêu lỗ hổng".

---

# 5. Đánh giá và đối chiếu cấu trúc đề xuất (7 H2 / 20 H3)

Căn cứ vào các nguyên tắc đã được làm sạch và xác thực, cấu trúc **7 H2 / 20 H3** được phê duyệt tại `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE` hoàn toàn phù hợp và đáp ứng xuất sắc tính chất của một đồ án an toàn thông tin:

- **2.1. Mô hình thực nghiệm (3 H3):** Mục tiêu mô hình, sơ đồ topo mạng và bảng thông số môi trường tập trung.
- **2.2. Cài đặt và cấu hình môi trường (5 H3):** Cấu hình mạng Host-Only, cấu hình Kali, cấu hình Windows Server, dịch vụ SMB/Firewall và kiểm tra trạng thái bản vá/snapshot.
- **2.3. Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap (3 H3):** Quy trình 6 bước khảo sát bề mặt dịch vụ mạng từ host discovery đến safe NSE.
- **2.4. Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE (3 H3):** Trình bày lệnh `smb-vuln-ms17-010`, cơ chế thăm dò qua pipe IPC$ và nguyên tắc đối chiếu tín hiệu từ xa với trạng thái bản vá nội bộ.
- **2.5. Kiểm thử các biện pháp giảm thiểu (4 H3):** Ma trận kiểm thử vi sai, phân định Case B (vô hiệu hóa SMBv1), Case C (tường lửa pfSense) và Case A (bản vá chính thức đối chứng lý thuyết).
- **2.6. Thu thập dữ liệu phục vụ đánh giá (2 H3):** Chuẩn hóa lưu trữ dữ liệu Nmap thô (`-oA`), bằng chứng ảnh chụp và 5 nguyên tắc suy luận an toàn cốt lõi.
- **2.7. Tổng kết chương:** Tóm tắt ngắn gọn các nội dung đã chuẩn bị làm tiền đề cho Chương 3.

**Khuyến nghị:** `LOCK_STRUCTURE_7H2_20H3`.

---

# 6. "Presentation Rules Learned" (10 quy tắc trình bày cho Chương 2)

1. **Một bảng thông số môi trường thay cho nhiều đoạn kể lể cấu hình:** Mọi chi tiết phần cứng, OS, build, IP, card mạng, dịch vụ được tập trung tại Bảng 2.1.
2. **Topo mạng trực quan đi trước:** Sơ đồ mạng xuất hiện ở đầu phần mô hình để người đọc nắm ngay luồng tương tác giữa các máy.
3. **Mỗi demo mở đầu bằng mục tiêu và điều kiện ban đầu rõ ràng:** Giúp người đọc hiểu ngay mục đích và trạng thái cần có trước khi gõ lệnh.
4. **Lệnh thực thi đặt trong code block có giải thích cờ tham số:** Người đọc dễ tìm, dễ sao chép và hiểu rõ lý do sử dụng từng cờ (`-sS`, `-sV`, `-Pn`, `--reason`, `-oA`).
5. **Không đưa kết quả đo đạc thực tế vào chương thiết kế kịch bản:** Mọi bảng kết quả scan chi tiết, nhận xét sâu và đánh giá hiệu năng thuộc về Chương 3.
6. **Bảng kiểm thử vi sai chỉ ghi nội dung cần kiểm tra lại:** Tuyệt đối không ghi kết quả kỳ vọng mang tính phán quyết chủ quan.
7. **Lược bỏ toàn bộ các bước thao tác đồ họa thông thường:** Không đưa hướng dẫn nhấn nút cài đặt VirtualBox hay Windows; chỉ tập trung vào cấu hình mạng, dịch vụ và câu lệnh kỹ thuật.
8. **Tuân thủ đúng kịch bản đã xây dựng của đề tài:** Không tùy tiện thay đổi các bước trong kịch bản quét hay thêm các công cụ không có trong evidence register.
9. **Sử dụng câu văn ngắn gọn, trực diện, không dùng thuật ngữ quản trị nội bộ:** Dùng văn phong kỹ thuật học thuật của sinh viên, không dùng từ ngữ điều hành dự án hay quản trị nội bộ.
10. **Chỉ giữ các nguyên tắc suy luận an toàn cốt lõi:** Nêu rõ 5 ranh giới suy luận an toàn trực tiếp: `445 open != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`, `UNKNOWN != SAFE`, `FILTERED != PATCHED`, `SMBv1 disabled != PATCHED`.
