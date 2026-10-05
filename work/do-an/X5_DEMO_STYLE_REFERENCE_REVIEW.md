# BÁO CÁO NGHIÊN CỨU THAM KHẢO VỀ CÁCH TRÌNH BÀY ĐỒ ÁN / BÁO CÁO ATTT CÓ THỰC NGHIỆM VÀ DEMO
## (X5 DEMO-STYLE REFERENCE REVIEW)

**Ngày thực hiện:** 2026-10-05  
**Phạm vi áp dụng:** Hiệu chuẩn phương pháp và phong cách trình bày Chương 2 của Đồ án An toàn thông tin SMB/Nmap/NSE–MS17-010 theo `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE`.  
**Nguyên tắc cốt lõi:**  
1. Khảo sát độc lập cách thức các đồ án, khóa luận tốt nghiệp, bài thực hành ATTT tại các trường đại học lớn ở Việt Nam (PTIT, HUIT, UIT, ACTVN) tổ chức và trình bày chương thực nghiệm/demo.  
2. Tuyệt đối **không sao chép nội dung kỹ thuật** (IP, OS version, kết quả scan, log, kết luận kỹ thuật) từ các tài liệu bên ngoài. Mọi thông tin kỹ thuật của đề tài chỉ lấy từ repository hiện hành (R5 baseline).  
3. Đúc rút thành các quy tắc trình bày cụ thể để chuyển đổi Chương 2 từ phong cách “báo cáo thẩm định kỹ thuật / QA report” sang phong cách “đồ án sinh viên có bài thực nghiệm và kịch bản demo rõ ràng, mạch lạc, đúng trọng tâm”.

---

# 1. Danh sách tài liệu đã khảo sát

Khảo sát được thực hiện trên 8 công trình khóa luận tốt nghiệp, đồ án môn học lớn và báo cáo thực nghiệm chuyên ngành An toàn thông tin / Mạng máy tính tại các cơ sở đào tạo trọng điểm ở Việt Nam (giai đoạn 2024–2026):

| STT | Trường / Nguồn | Tên đồ án / Báo cáo | Năm | Phân nhóm | Vì sao chọn |
|:---:|---|---|:---:|:---:|---|
| **TL01** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu và xây dựng các bài thực hành về kỹ thuật thu thập thông tin trong kiểm thử xâm nhập* | 2025 | Nhóm B (Nmap / Pentest Lab) | Đồ án ATTT tập trung vào Nmap, enumeration, quét dịch vụ; cấu trúc bài lab được thiết kế mạch lạc: Mục tiêu $\rightarrow$ Chuẩn bị $\rightarrow$ Kịch bản thực thi $\rightarrow$ Quan sát dấu hiệu. |
| **TL02** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Nghiên cứu triển khai hệ thống giám sát an ninh mạng và điều tra, ứng phó sự cố tập trung sử dụng Splunk và Sysmon* | 2025 | Nhóm A (Network/Security Lab) | Mô tả mô hình lab đa trạm (Windows Server, Linux sensor, trạm phân tích); tách bạch rõ giữa tham số cấu hình tĩnh và quy trình kích hoạt sự kiện; bảng thông số VM rất súc tích. |
| **TL03** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Xây dựng các bài thực hành số về tìm hiểu và phân tích mã độc họ Backdoor trên nền tảng Labtainer* | 2025 | Nhóm D (Lab thực hành ATTT) | Phong cách Lab Guide học thuật chuẩn mực: mỗi bài thực hành có Mục tiêu, Sơ đồ topology, Lệnh thực thi đi kèm giải thích cờ (flag), và Dữ liệu cần thu thập. |
| **TL04** | Học viện Công nghệ Bưu chính Viễn thông (PTIT) | *Đánh giá hiệu quả của các hệ thống phát hiện xâm nhập dựa trên host (Wazuh và Samhain)* | 2024 | Nhóm A/C (So sánh / Thực nghiệm) | Đồ án so sánh hiệu quả giải pháp an ninh; thể hiện xuất sắc cách phân tách giữa "Chương xây dựng mô hình thực nghiệm" và "Chương kết quả/phân tích". |
| **TL05** | Trường Đại học Công Thương TP.HCM (HUIT) | *Triển khai hệ thống tường lửa (Firewall) pfSense và giải pháp ngăn chặn tấn công mạng cho doanh nghiệp* | 2024 | Nhóm C (Firewall / Mitigation) | Đúng trường đào tạo của đề tài (HUIT); minh họa cấu hình pfSense dạng gateway/bridge kiểm soát cổng mạng; quy trình kiểm thử trước và sau can thiệp (before-after test). |
| **TL06** | Trường Đại học Công Thương TP.HCM (HUIT) | *Xây dựng và đánh giá hiệu năng tường lửa ứng dụng web (WAF) trong phòng chống tấn công Web* | 2024 | Nhóm C (Firewall / Before-After) | Thuộc khoa CNTT HUIT; cấu trúc chương thực nghiệm tập trung vào: dựng lab $\rightarrow$ kịch bản tấn công mẫu $\rightarrow$ cấu hình phòng thủ $\rightarrow$ tiêu chí đánh giá. |
| **TL07** | Học viện Kỹ thuật Mật mã (ACTVN) | *Nghiên cứu và Thực nghiệm về SOC (Security Operation Center) và Giám sát An toàn mạng* | 2024 | Nhóm A (Security Lab) | Đồ án chuyên sâu về an toàn mạng; trình bày sơ đồ topology phân đoạn mạng rõ ràng; bảng phân bổ IP/vai trò; kịch bản mô phỏng rõ từng bước. |
| **TL08** | Trường Đại học Công nghệ Thông tin – ĐHQG TP.HCM (UIT) | *Xây dựng hệ thống Honeypot và Giám sát Phát hiện tấn công mạng* | 2024 | Nhóm B/D (Scanning / Lab ATTT) | Mẫu báo cáo khóa luận ATTT chuẩn mực; lệnh CLI được đóng khung code block có chú thích; không lạm dụng screenshot cài đặt Next/Next/Finish. |

---

# 2. Các pattern trình bày thường gặp trong các báo cáo thực nghiệm

Qua khảo sát 8 tài liệu trên, nhận thấy các báo cáo thực nghiệm ATTT tại Việt Nam thường tuân theo 2 nhóm mô hình tổ chức chương:

### Mô hình 1: Thiết kế $\rightarrow$ Triển khai $\rightarrow$ Kết quả (3 tầng truyền thống)
- **Chương 1:** Tổng quan lý thuyết, công nghệ và cơ sở giao thức.
- **Chương 2:** Thiết kế mô hình lab, chuẩn bị môi trường và xây dựng kịch bản thử nghiệm.
- **Chương 3:** Triển khai thực nghiệm, ghi nhận dữ liệu và phân tích kết quả.
- **Chương 4:** Đánh giá, bàn luận và đề xuất giải pháp/kết luận.

### Mô hình 2: Xây dựng bài thực hành / Kịch bản (Hướng dẫn lab chuyên sâu - Lab Guide)
- Thường gặp ở các đồ án PTIT (TL01, TL03) và UIT (TL08).
- **Chương 2** đóng vai trò là "Xây dựng môi trường và kịch bản thực nghiệm".
- Trong chương này, tác giả trả lời 4 câu hỏi rất tuần tự:
  1. Mô hình gồm những máy nào, nối với nhau ra sao?
  2. Mỗi máy được cài đặt và cấu hình thông số gì để sẵn sàng?
  3. Kịch bản 1 (thăm dò/quét) chạy những lệnh gì, nhằm mục tiêu gì, cần quan sát biến số nào?
  4. Kịch bản 2 (kiểm tra an ninh/khai thác/giảm thiểu) thực hiện theo các bước nào, điều kiện kiểm thử là gì?
- **Đặc điểm nổi bật:** Chương này hoàn toàn dừng lại ở **quy trình, câu lệnh và điều kiện quan sát**, không đưa bảng số liệu kết quả chi tiết hay ảnh chụp kết quả cuối cùng vào đây mà để dành cho Chương 3.

---

# 3. Những cách trình bày nên học

1. **Topology đặt ngay đầu phần môi trường:** Một sơ đồ trực quan (Mermaid hoặc hình vẽ kiến trúc mạng) thể hiện rõ vai trò từng máy, IP, subnet, và luồng tương tác giữa trạm kiểm thử và trạm mục tiêu.
2. **Gom thông số phần cứng và mạng vào 1 bảng duy nhất:** Thay vì viết 4-5 đoạn văn kể lể "Máy A có RAM 2GB, máy B có RAM 4GB...", các báo cáo chất lượng (TL02, TL05, TL08) gom tất cả vào một bảng cấu hình: Tên máy, Vai trò, Hệ điều hành, IP, RAM, Vị trí mạng.
3. **Mô tả demo theo cấu trúc chuẩn 4 phần:**
   - **Mục tiêu:** Trả lời câu hỏi demo này để làm gì?
   - **Điều kiện ban đầu:** Cần trạng thái máy, cổng mạng hay dịch vụ nào sẵn sàng?
   - **Quy trình & Lệnh:** Các bước thao tác kèm lệnh thực thi (có giải thích ngắn gọn ý nghĩa tham số).
   - **Nội dung cần quan sát:** Chỉ định rõ người thực hiện cần nhìn vào đâu (cờ trạng thái cổng, banner dịch vụ, thông báo script, gói tin).
4. **Trình bày lệnh trong Code Block rõ ràng:** Câu lệnh CLI (Nmap, PowerShell, pfSense shell) được đặt trong khối lệnh riêng biệt, có giải thích các cờ quan trọng ngay bên dưới hoặc trong bảng tra cứu tham số.
5. **Kiểm thử biện pháp giảm thiểu theo mô hình Before - After:** Trình bày rõ ràng: Trạng thái trước can thiệp $\rightarrow$ Thao tác can thiệp $\rightarrow$ Tiêu chí kiểm tra lại sau can thiệp.
6. **Ngôn ngữ kỹ thuật mộc mạc, sáng sủa:** Dùng câu chủ động, mạch lạc, giải thích trực tiếp thao tác thực hiện, không dùng thuật ngữ quản trị rủi ro trừu tượng hay ngôn từ thẩm định nội bộ.

---

# 4. Những cách KHÔNG nên học (Cần tránh tuyệt đối)

1. **Screenshot "spam" từng bước cài đặt:** Chụp ảnh từng cửa sổ nhấn "Next $\rightarrow$ I Agree $\rightarrow$ Finish" khi cài VirtualBox, cài OS hoặc cài Nmap. Đây là lỗi phổ biến làm loãng báo cáo đồ án sinh viên.
2. **Lạm dụng heading cấp con (H4, H5) và đoạn văn đơn dòng:** Chia mục quá vụn khiến mỗi mục chỉ có 1-2 dòng văn bản, làm gãy mạch đọc.
3. **Trộn lẫn lý thuyết nền vào kịch bản thực nghiệm:** Trong mục mô tả lệnh quét Nmap lại chép lại 3 trang giải thích bắt tay 3 bước TCP SYN là gì. Lý thuyết giao thức thuộc về Chương 1.
4. **"Rò rỉ" kết quả thực nghiệm (Result Leakage):** Trong Chương 2 mô tả kịch bản lại viết luôn: "Kết quả cho thấy máy chủ bị tấn công thành công, xuất hiện màn hình Command Prompt chiếm quyền điều khiển...". Điều này làm mất tính phân tách giữa "Thiết kế phương pháp" và "Kết quả thực nghiệm".
5. **Đưa mã định danh nội bộ vào văn bản:** Viết dày đặc các mã kiểm thử (như `EVD-RAW-01`, `S1-RAW-02`) vào từng câu văn khiến báo cáo giống biên bản nghiệm thu QA hơn là một luận văn học thuật.
6. **Lặp lại sơ đồ mô hình ở nhiều mục con:** Vẽ lại topology ở mỗi kịch bản gây thừa thãi, chỉ cần 1 sơ đồ tổng thể ở mục đầu tiên và viện dẫn lại.

---

# 5. Đánh giá và đối chiếu cấu trúc đề xuất (7 H2 / 20 H3)

Đối chiếu cấu trúc theo `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE` với kết quả nghiên cứu các đồ án mẫu:

| STT | Mục đề xuất (CR) | Đánh giá so với mẫu nghiên cứu | Quyết định khuyến nghị | Ghi chú điều chỉnh phong cách |
|:---:|---|---|:---:|---|
| **2.1** | **Mô hình thực nghiệm** | Phù hợp hoàn hảo với TL02, TL07, TL08 (Lab Setup). | **KEEP** | Giữ ngắn gọn, trực quan. |
| 2.1.1 | Mục tiêu của mô hình | Chuẩn mực: nêu rõ mô hình dựng lên để phục vụ khảo sát gì. | **KEEP** | Trả lời trực tiếp mục tiêu lab cô lập. |
| 2.1.2 | Sơ đồ và thành phần của mô hình | Chuẩn mực: đặt sơ đồ tổng thể và giới thiệu các máy. | **KEEP** | Dùng sơ đồ mạng rõ các trạm và kết nối. |
| 2.1.3 | Thông số môi trường thực nghiệm | Rất cần thiết: gom thông số phần cứng, IP, OS vào bảng. | **KEEP** | 1 bảng tổng hợp thông số duy nhất. |
| **2.2** | **Cài đặt và cấu hình môi trường** | Đúng tiến trình chuẩn bị máy trước khi thử nghiệm. | **KEEP** | Đi thẳng vào cấu hình kỹ thuật. |
| 2.2.1 | Cấu hình mạng Host-Only trên VirtualBox | Trình bày dải mạng cô lập, tránh ảnh hưởng ra ngoài. | **KEEP** | Nêu subnet, DHCP tắt, bảo đảm an toàn. |
| 2.2.2 | Cấu hình máy Kali Linux | Trạm kiểm thử: IP tĩnh, công cụ Nmap/NSE. | **KEEP** | Ngắn gọn, không kể lể cài đặt Linux. |
| 2.2.3 | Cấu hình máy Windows Server 2012 R2 | Trạm mục tiêu: thông số hệ thống, dịch vụ File Server. | **KEEP** | Trình bày bản build, vai trò server. |
| 2.2.4 | Cấu hình SMB và Windows Firewall | Cấu hình mở cổng 139/445 và kích hoạt chia sẻ SMB. | **KEEP** | Nêu lệnh PowerShell/giao diện cấu hình. |
| 2.2.5 | Kiểm tra bản vá MS17-010 và tạo snapshot | Chuẩn mực lab an toàn: kiểm tra KB và tạo điểm khôi phục. | **KEEP** | Lệnh Get-HotFix, tạo snapshot trước test. |
| **2.3** | **Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap** | Trọng tâm kịch bản rà quét (tương đồng TL01). | **KEEP** | Cấu trúc: Mục tiêu $\rightarrow$ Lệnh $\rightarrow$ Quan sát. |
| 2.3.1 | Mục tiêu và phạm vi | Định rõ phạm vi quét cổng 139/445 và phiên bản dịch vụ. | **KEEP** | Rõ ràng, không lan man. |
| 2.3.2 | Quy trình và các lệnh thực hiện | Lệnh Nmap `-sS`, `-sV`, `-p139,445` có giải thích tham số. | **KEEP** | Đặt trong code block, kèm bảng ý nghĩa cờ. |
| 2.3.3 | Nội dung cần quan sát và giới hạn kết luận | Nêu rõ cần nhìn vào trạng thái cổng, tên dịch vụ; giới hạn. | **KEEP** | Nhấn mạnh: port open $\neq$ có lỗ hổng. |
| **2.4** | **Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE** | Trọng tâm kịch bản kiểm tra lỗ hổng (tương đồng TL01, TL08). | **KEEP** | Cấu trúc kịch bản kiểm tra an ninh chuẩn. |
| 2.4.1 | Mục tiêu và điều kiện ban đầu | Điều kiện: cổng 445 mở, SMBv1 đang bật, kết nối thông. | **KEEP** | Nêu rõ tiền đề trước khi chạy NSE. |
| 2.4.2 | Quy trình kiểm tra NSE-SMB-01 đến NSE-SMB-04 | 4 bước quét: cấu hình cơ bản, script audit, script khai thác. | **KEEP** | Trình bày từng lệnh, tham số script-args. |
| 2.4.3 | Đối chiếu với trạng thái bản vá và giới hạn kết luận | Ranh giới suy luận: script check $\neq$ exploit thật; giới hạn. | **KEEP** | Tách rõ dấu hiệu nghi ngờ với xác nhận vá. |
| **2.5** | **Kiểm thử các biện pháp giảm thiểu** | Tương đồng các đồ án phòng thủ, before-after (TL04, TL05, TL06). | **KEEP** | Bố cục logic, chặt chẽ. |
| 2.5.1 | Nguyên tắc kiểm thử trước và sau can thiệp | Chuẩn phương pháp: baseline $\rightarrow$ can thiệp $\rightarrow$ re-scan. | **KEEP** | Nêu nguyên tắc đối chứng khoa học. |
| 2.5.2 | Case B — Vô hiệu hóa SMBv1 | Thao tác tắt SMBv1 trên Server và tiêu chí kiểm tra lại. | **KEEP** | Lệnh PowerShell tắt SMBv1, tiêu chí re-scan. |
| 2.5.3 | Case C — Kiểm soát TCP 139/445 bằng pfSense | Thao tác dựng bridge, chặn cổng và tiêu chí kiểm tra lại. | **KEEP** | Cấu hình bridge, rule filter cổng 139/445. |
| 2.5.4 | Vai trò của cập nhật bản vá | Khái quát vai trò bản vá KB4012213 (Case A). | **KEEP** | Giải thích cơ chế triệt để của vá lỗi kernel. |
| **2.6** | **Thu thập dữ liệu phục vụ đánh giá** | Chuẩn bị dữ liệu cho Chương 3 (tương đồng TL02, TL04). | **KEEP** | Cầu nối phương pháp sang kết quả. |
| 2.6.1 | Log và ảnh chụp thực nghiệm | Các loại dữ liệu cần lưu: file xml, txt nmap, pcap, packet log. | **KEEP** | Hướng dẫn định dạng lưu trữ minh chứng. |
| 2.6.2 | Nguyên tắc diễn giải kết quả | Các quy tắc suy luận: Open $\neq$ Vuln, Filtered $\neq$ Safe... | **KEEP** | Kế thừa 5 lớp suy luận nhưng viết sáng sủa. |
| **2.7** | **Tổng kết chương** | Tóm lược những gì đã chuẩn bị sẵn sàng cho Chương 3. | **KEEP** | Kết chương ngắn gọn, tự nhiên. |

**Kết luận đánh giá bố cục:**  
$\rightarrow$ `RECOMMEND_KEEP_7H2_20H3`.  
Cấu trúc 7 H2 / 20 H3 đã được người dùng duyệt hoàn toàn tương thích và phản ánh đúng cấu trúc tối ưu của các đồ án thực nghiệm ATTT xuất sắc tại Việt Nam. Không cần tách thêm hay gộp bớt mục nào.

---

# 6. "Presentation Rules Learned" (12 quy tắc trình bày cụ thể)

Từ kết quả khảo sát, rút ra 12 quy tắc bắt buộc áp dụng khi viết lại `CHAPTER_2.md`:

1. **Một bảng môi trường duy nhất:** Gom toàn bộ thông số máy ảo (Tên máy, Hệ điều hành, RAM, CPU, IP, Vai trò, Chế độ mạng) vào Bảng 2.1 ở mục 2.1.3; không rải rác thông số phần cứng thành nhiều đoạn văn.
2. **Sơ đồ mạng trực quan, không lặp lại:** Vẽ một sơ đồ kiến trúc tổng thể (Mermaid diagram) ở mục 2.1.2 thể hiện rõ mạng Host-Only, các dải IP và vị trí trạm kiểm thử / trạm mục tiêu / firewall.
3. **Mỗi demo mở đầu bằng mục tiêu trực tiếp:** Không vòng vo triết lý; đi thẳng vào mục đích: "Kịch bản này nhằm khảo sát...", "Kịch bản này kiểm tra...".
4. **Lệnh thực thi phải kèm mục đích và giải thích tham số:** Mọi dòng lệnh Nmap, PowerShell đều phải đặt trong code block, kèm 1-2 câu giải thích các tham số cốt lõi (ví dụ: `-sS`, `-sV`, `-Pn`, `--script`).
5. **Chuẩn hóa cấu trúc kịch bản theo 4 bước:** Mục tiêu $\rightarrow$ Điều kiện ban đầu $\rightarrow$ Quy trình câu lệnh $\rightarrow$ Dữ liệu cần quan sát.
6. **Không rò rỉ kết quả thực nghiệm:** Chương 2 chỉ nêu "cần quan sát biến số nào, tiêu chí nào là đạt/chưa đạt", tuyệt đối không viết "kết quả quét thực tế cho thấy..." (dành toàn bộ cho Chương 3).
7. **Không chụp màn hình từng bước cài đặt:** Chỉ dùng sơ đồ luồng, bảng tham số và khối lệnh; loại bỏ hoàn toàn các mô tả thao tác bấm chuột "Next/Finish" không cần thiết.
8. **Kiểm thử can thiệp theo cặp Trước - Sau (Before - After):** Khi trình bày Case B và Case C, luôn nêu rõ: Trạng thái trước can thiệp là gì, lệnh thực hiện can thiệp là gì, và kỳ vọng thay đổi khi quét lại là gì.
9. **Ẩn mã định danh bằng chứng nội bộ:** Không viết các mã `EVD-RAW-...`, `S1-RAW-...` vào văn bản chính; chuyển thành ngôn từ tự nhiên: "nhật ký quét Nmap", "bản ghi bắt gói tin Wireshark", "ảnh chụp màn hình cấu hình".
10. **Tách biệt ranh giới suy luận an toàn:** Nhắc lại rõ ràng các nguyên lý: Cổng mở không đồng nghĩa có lỗ hổng; gói tin bị chặn (Filtered) không đồng nghĩa hệ điều hành đã an toàn; script báo hiệu không thay thế được việc kiểm tra bản vá gốc.
11. **Ngôn ngữ kỹ thuật giản dị, tránh thuật ngữ quản trị rủi ro:** Không dùng các từ ngữ như "canonical baseline", "truth matrix", "gate", "governance framework", "thẩm định năng lực". Viết bằng văn phong đồ án kỹ thuật: trực diện, chính xác, khách quan.
12. **Dung lượng vừa phải, súc tích:** Đảm bảo độ dài toàn chương nằm trong khoảng **3.200 – 4.000 từ**, các tiểu mục cân đối từ 150 – 250 từ, không có tiểu mục nào bị quá ngắn (dưới 50 từ) hoặc quá dài (trên 500 từ).

---
*Tài liệu này là căn cứ nghiên cứu và định hướng phương pháp luận bắt buộc tuân thủ trước khi tiến hành viết lại Chương 2.*
