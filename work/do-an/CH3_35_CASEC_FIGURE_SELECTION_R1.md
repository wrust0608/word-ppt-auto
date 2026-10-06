# BÁO CÁO LỰA CHỌN VÀ ĐÁNH GIÁ HÌNH ẢNH MỤC 3.5 CASE C R2 (CH3_35_CASEC_FIGURE_SELECTION_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E0 R2 — Correct Case C Evidence/Presentation Plan`
- **Mục tiêu:** Thẩm tra toàn diện bằng chứng thị giác Kịch bản kiểm soát mạng Case C (Tường lửa pfSense Transparent Bridge), phân loại giá trị gia tăng từng ảnh, ngăn chặn triệt để tình trạng "album ảnh chụp màn hình", và đề xuất khung cắt cúp dự kiến có thể tái lập phục vụ trang in A4.
- **Phạm vi thẩm tra thực tế:** Toàn bộ 17 tệp bằng chứng Case C canonical đã stage tại `work/do-an/chapter3/evidence/case_c/`:
  - 9 tệp ảnh chụp màn hình trực tiếp:
    1. `pfSense_03_Interface_Assignment.png` (485×944 px)
    2. `pfSense_04_Bridge.png` (485×654 px)
    3. `pfSense_05_Bridge_Filtering.png` (720×400 px)
    4. `pfSense_06_Baseline_Pass_Rule.png` (485×678 px)
    5. `pfSense_07_Block_Rule_Config.png` (485×2246 px)
    6. `pfSense_08_Rule_Order.png` (485×731 px)
    7. `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` (1280×800 px)
    8. `pfSense_10_Block_Log_CANONICAL.png` (1359×17637 px)
    9. `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` (1280×800 px)
  - 2 bộ ba tệp thô máy đọc Nmap (6 tệp):
    * `NSE-SMB-01_ports.gnmap`, `NSE-SMB-01_ports.nmap`, `NSE-SMB-01_ports.xml`
    * `NSE-SMB-04_ms17010.gnmap`, `NSE-SMB-04_ms17010.nmap`, `NSE-SMB-04_ms17010.xml`
  - 2 tệp siêu dữ liệu và báo cáo tiến trình thực thi:
    * `RUN4_PAUSE_STATE_REPORT.txt` (báo cáo trạng thái tạm dừng và kết luận Mục 21 Final Bounded Completion Closure)
    * `pfSense_Remediation_Run_Manifest.txt` (manifest điều hành tiến trình)

---

## 1. Kiểm Toán Kho Bằng Chứng Và Xác Lập Mâu Thuẫn Thực Tế

Trong quá trình đối soát giữa 17 tệp bằng chứng thực tế tại `work/do-an/chapter3/evidence/case_c/`, kế hoạch ghi nhận hai hiện tượng kỹ thuật bắt buộc phải khóa ranh giới phương pháp luận:

### 1.1. Mâu thuẫn thực tế giữa nhãn quy tắc trong ảnh chụp nhật ký và bản ghi manifest (Rule-Label Discrepancy)
- **Nội dung hiển thị trên ảnh trực tiếp `pfSense_10_Block_Log_CANONICAL.png`:**
  Tại các dòng nhật ký chặn cổng SMB lúc 14:20:18–14:20:19, biểu tượng chi tiết quy tắc hiển thị chuỗi nhãn văn bản:
  `CASE C baseline pass Kali to Windows (100000104)`
- **Nội dung ghi chép trong tệp manifest và báo cáo điều hành:**
  Tệp `pfSense_Remediation_Run_Manifest.txt` (dòng 79) và `RUN4_PAUSE_STATE_REPORT.txt` (Mục 21) gán lưu lượng bị chặn cho quy tắc:
  `CASE C - Block SMB Kali to Windows (1000000104)`
- **Quy tắc xử lý bắt buộc trong kế hoạch:**
  - Đây là một **mâu thuẫn thực tế nội tại chưa hòa giải (unresolved conflict)** trong bộ dữ liệu thực nghiệm. Báo cáo không che giấu, không tự ý sửa đổi và không hợp thức hóa mâu thuẫn này.
  - **TUYỆT ĐỐI KHÔNG VIẾT:** *"Ảnh chụp nhật ký chứng minh chính xác quy tắc 'CASE C - Block SMB Kali to Windows' đã khớp."*
  - **CHỈ ĐƯỢC PHÉP KẾT LUẬN:** *"Lưu lượng TCP SYN tương ứng gửi tới các cổng SMB (139/445) từ trạm Kali tới máy chủ Windows được ghi nhận bị chặn (Block) trên đường truyền đi qua pfSense."*
  - Sự tồn tại của quy tắc chặn (Block rule) và thứ tự ưu tiên (Block nằm trên Pass) được chứng minh độc lập bởi các ảnh chụp cấu hình và danh sách quy tắc (`pfSense_07`, `pfSense_08`), nhưng ảnh nhật ký `pfSense_10` chỉ chứng minh hành vi chặn lưu lượng mạng thực tế.

### 1.2. Sự vắng mặt của ảnh chụp màn hình máy chủ Windows cục bộ trong Case C
- **Hiện trạng:** Bộ 9 ảnh chụp màn hình của Case C thuần túy ghi nhận giao diện pfSense (WebGUI, console FreeBSD) và trạm kiểm thử Kali Linux. Không có ảnh chụp màn hình bảng điều khiển Windows Server 2012 R2 cục bộ nào được tạo mới trong Case C (khác với Case B có ảnh `03_After_Local`).
- **Quy tắc xử lý bắt buộc:**
  - Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Metadata cuối Case C ghi nhận `SMB1=True`, `SMB2=True`, `LanmanServer=Running`, các listener cục bộ 139/445 hiện diện và trạng thái bản vá hệ thống cục bộ duy trì `UNPATCHED` (`srv.sys` numeric canonical version = `6.3.9600.16421`).
  - **TUYỆT ĐỐI KHÔNG gán ghép hoặc suy diễn trạng thái Windows cục bộ xuất phát từ bất kỳ ảnh chụp màn hình nào của pfSense.**
  - Trạng thái máy chủ cục bộ sẽ được trình bày rõ ràng thông qua Bảng 3.6 và phân tích ranh giới trong văn xuôi với nguồn gốc xuất xứ (provenance) minh bạch từ mốc baseline Mục 3.1 và báo cáo kiểm toán hệ thống `RUN4_PAUSE_STATE_REPORT.txt`.

---

## 2. Bảng Đánh Giá Chi Tiết Toàn Bộ 9 Ảnh Chụp Màn Hình Case C

| STT | Tệp ảnh gốc (File) | Kích thước gốc | Giai đoạn Case C | Nội dung hiển thị trực tiếp (Directly shows) | Tính độc bản so với Mục 3.1–3.4 | Bảng/văn bản thay thế được? | Giá trị thị giác (Visual value) | Cần cắt cúp? (Crop needed?) | Phân loại (KEEP / OPTIONAL / DROP) | Lý do & Đề xuất sử dụng (Reason & Proposed use) |
|:---:|---|:---:|---|---|---|---|---|:---:|:---:|---|
| 1 | `pfSense_03_Interface_Assignment.png` | 485×944 px | Thiết lập giao diện mạng | Giao diện WebGUI Interfaces > Assignments: gán `em0` làm WAN, `em1` làm LAN, `em2` làm `CASE_C_KALI`, `em3` làm `CASE_C_WINDOWS`, cổng khả dụng `BRIDGE0`. | Thấp. Việc đặt tên giao diện là bước cấu hình định danh nội bộ pfSense. | **Có hoàn toàn**. Thông tin ánh xạ card mạng và IP được trình bày cô đọng trong Bảng 3.6 và sơ đồ mô hình thực nghiệm. | Trung bình (giao diện cấu hình hẹp, dài, nhiều khoảng trống). | Có (bỏ cảnh báo mật khẩu, chân trang). | **DROP** | **Loại bỏ**. Tránh biến báo cáo thành hướng dẫn cài đặt từng bước (step-by-step tutorial). Việc ánh xạ giao diện là tiền đề kỹ thuật, không phải kết quả kiểm soát an ninh. |
| 2 | `pfSense_04_Bridge.png` | 485×654 px | Cấu hình cầu nối | Giao diện WebGUI Interfaces > Bridges: hiển thị giao diện `BRIDGE0` với các thành viên `CASE_C_KALI, CASE_C_WINDOWS`, mô tả `CASE_C_BRIDGE`. | Trung bình. Minh chứng thị giác trực tiếp về việc pfSense ghép nối hai cổng mạng thành một cầu nối Transparent Bridge Layer 2. | Có thể mô tả qua văn xuôi và Bảng 3.6. | Khá tốt, bảng cấu hình cầu nối rõ ràng. | Có (cắt bỏ phần cảnh báo mật khẩu bên trên và chân trang). | **OPTIONAL / DROP** | **Dự phòng / Ưu tiên loại bỏ**. Nhằm giữ số lượng hình ảnh tối giản, cấu hình cầu nối Layer 2 được mô tả chuẩn xác trong văn bản và Bảng 3.6. Chỉ giữ lại ảnh này nếu hội đồng yêu cầu minh chứng thị giác giao diện tạo bridge; Chapter 2 đã có sơ đồ Transparent Bridge (Hình 2.2). |
| 3 | `pfSense_05_Bridge_Filtering.png` | 720×400 px | Tham số nhân FreeBSD | Màn hình console dòng lệnh FreeBSD: thực thi lệnh `sysctl net.link.bridge.pfil_member net.link.bridge.pfil_bridge` hiển thị `pfil_member: 1`, `pfil_bridge: 0`. | Thấp. Đây là tham số tunable tầng kernel của FreeBSD để chuyển hướng lọc gói tin sang các card mạng thành viên. | **Có hoàn toàn**. Hai cặp giá trị sysctl được ghi nhận chuẩn xác trong Bảng 3.6 và văn xuôi kỹ thuật. | Rất thấp (chỉ là 2 dòng văn bản console đen trắng). | Không đáng kể. | **DROP** | **Loại bỏ**. Một màn hình console chỉ để hiển thị 2 dòng giá trị sysctl không đem lại giá trị học thuật thị giác trên trang in A4. Tránh lãng phí diện tích báo cáo. |
| 4 | `pfSense_06_Baseline_Pass_Rule.png` | 485×678 px | Trạng thái quy tắc ban đầu | Giao diện WebGUI Firewall > Rules > CASE_C_KALI: chỉ có duy nhất 1 quy tắc Pass (dấu kiểm xanh) cho phép mọi lưu lượng IPv4 từ `192.168.56.10` tới `192.168.56.20`. | Không độc bản. Đây là trạng thái trung gian trước khi tạo quy tắc Block. Ảnh `pfSense_08` bao quát trọn vẹn cả quy tắc Block lẫn quy tắc Pass. | **Có hoàn toàn**. Bảng 3.6 và ảnh `pfSense_08` đã thể hiện đầy đủ quy tắc này. | Thấp (chỉ có một dòng quy tắc đơn lẻ). | Có. | **DROP** | **Loại bỏ**. Ảnh thể hiện trạng thái chưa hoàn thiện của chính sách kiểm soát. Bị thay thế hoàn toàn bởi ảnh `pfSense_08_Rule_Order.png`. |
| 5 | `pfSense_07_Block_Rule_Config.png` | 485×2246 px | Chi tiết cấu hình quy tắc chặn | Form WebGUI Edit Firewall Rule: Action=Block, Protocol=TCP, Source=`192.168.56.10`, Destination=`192.168.56.20`, Port=`SMB_Ports` (139, 445), Log=Enabled, Description=`CASE C - Block SMB Kali to Windows`. | Có giá trị chi tiết, nhưng chiều dọc quá lớn (2246 px), chứa nhiều trường nhập liệu mặc định không mang thông tin mới. | **Có**. Các tham số cốt lõi (Block, TCP, IP nguồn/đích, cổng, cờ ghi log) đều được thể hiện cô đọng tại ảnh `pfSense_08` và Bảng 3.6. | Thấp trên A4 (ảnh quá dài, nếu co lại sẽ làm chữ bé không đọc được). | Bắt buộc phải crop rất phức tạp hoặc chia cột. | **OPTIONAL / DROP** | **Dự phòng / Ưu tiên loại bỏ**. Chiều cao bất thường gây vỡ bố cục trang in A4. Ảnh `pfSense_08_Rule_Order.png` thể hiện trọn vẹn chính sách và thứ tự ưu tiên của quy tắc một cách trực quan, khoa học hơn nhiều. |
| 6 | `pfSense_08_Rule_Order.png` | 485×731 px | Danh sách & thứ tự quy tắc tường lửa | Bảng danh sách Firewall Rules trên giao diện `CASE_C_KALI`: Dòng 1: Biểu tượng X đỏ (Block), biểu tượng ghi log, IPv4 TCP, Source `192.168.56.10`, Destination `192.168.56.20`, Port `SMB_Ports`. Dòng 2: Dấu kiểm xanh (Pass), IPv4 *, Source `192.168.56.10`, Destination `192.168.56.20`. | **Rất cao (Độc bản & Cốt lõi)**. Minh chứng trực tiếp hai sự thật kỹ thuật: (1) Quy tắc Block SMB có bật ghi log thực sự tồn tại; (2) Quy tắc Block nằm TRÊN quy tắc Pass baseline trong cấu hình pfSense. | Bảng 3.6 ghi nhận thông tin, nhưng ảnh là bằng chứng thị giác xác thực không thể thiếu cho chính sách an ninh. | **Rất cao**. Bố cục bảng ngang gọn gàng, thể hiện trọn vẹn thứ tự luật lọc. | Có (cắt bỏ phần cảnh báo mật khẩu phía trên, chân trang Netgate và các nút thao tác thừa bên dưới; giữ ngữ cảnh `CASE_C_KALI`). | **KEEP (Ưu tiên 1)** | **Hình 3.9 (Đề xuất chính thức)**. Bằng chứng thị giác trung tâm cho việc cấu hình chính sách kiểm soát lưu lượng SMB và thứ tự ưu tiên quy tắc trên tường lửa pfSense. |
| 7 | `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | 1280×800 px | Đo đạc lại cổng dịch vụ từ xa (NSE-01) | Cửa sổ terminal Kali Linux: thực thi lệnh `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`. Kết quả: `139/tcp filtered netbios-ssn no-response`, `445/tcp filtered microsoft-ds no-response`. | **Rất cao (Độc bản & Trọng yếu)**. Khác biệt căn bản so với baseline và Case B (vốn ghi nhận OPEN): cổng 139 và 445 chuyển sang trạng thái `filtered` do không nhận được phản hồi (`no-response`). | Bảng 3.6 ghi nhận kết quả, nhưng ảnh cung cấp bằng chứng thị giác trực tiếp từ góc nhìn trạm kiểm thử. | **Rất cao**. Terminal sắc nét, thể hiện đầy đủ cú pháp lệnh, cờ chẩn đoán nguyên nhân và kết quả quét cổng. | Có (cắt bỏ hình nền desktop Kali, thanh tác vụ trên cùng và khoảng trống console phía dưới; giữ đầy đủ lệnh, arp-response, cổng, MAC, Nmap done). | **KEEP (Ưu tiên 2)** | **Hình 3.10 (Đề xuất chính thức)**. Bằng chứng thực nghiệm trung tâm từ góc nhìn trạm kiểm thử Kali Linux, xác nhận sự thay đổi trạng thái cổng dịch vụ SMB từ OPEN sang FILTERED. |
| 8 | `pfSense_10_Block_Log_CANONICAL.png` | 1359×17637 px | Nhật ký chặn tường lửa đối chiếu liên tầng | Trang WebGUI System Logs > Firewall: chứa các dòng nhật ký ghi nhận hành động Block (X đỏ) trên giao diện `CASE_C_KALI` đối với các gói tin TCP SYN từ `192.168.56.10` tới `192.168.56.20:139` và `:445` tại mốc thời gian 14:20:18–14:20:19. | **Rất cao (Độc bản & Cốt lõi)**. Cung cấp bằng chứng đối chiếu liên tầng: ghi nhận lưu lượng TCP SYN tương ứng gửi tới các cổng SMB từ trạm Kali đã bị pfSense chặn lại trên đường truyền trong lượt Case C. | Bảng 3.6 tóm lược dữ liệu, nhưng nhật ký là minh chứng khách quan cho sự can thiệp tích cực của tường lửa. | **Rất cao khi cắt cúp**. Nguyên bản quá dài (17637 px), vùng nhật ký liên quan đến đợt quét cần được trích xuất cô đọng. | Bắt buộc cắt cúp chính xác vùng chứa tiêu đề bảng nhật ký và các dòng log 14:20:18–14:20:19; crop mang tính PROVISIONAL. | **KEEP (Ưu tiên 3)** | **Hình 3.11 (Đề xuất chính thức)**. Minh chứng đối chiếu liên tầng xác nhận lưu lượng TCP SYN tới cổng SMB từ trạm Kali đã bị pfSense chặn lại. Đi kèm lưu ý xử lý mâu thuẫn nhãn luật. |
| 9 | `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | 1280×800 px | Kiểm tra dấu hiệu MS17-010 từ xa (NSE-04) | Cửa sổ terminal Kali Linux: thực thi lệnh `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`. Kết quả: `445/tcp filtered microsoft-ds`, phiên quét hoàn tất trong 0.51 giây và không có khối `Host script results:`. | Phép đo ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có. | Bảng 3.6 và văn xuôi phân tích ranh giới UNKNOWN thể hiện trọn vẹn và cô đọng kết quả này. | Khá tốt, hiển thị trực quan phiên quét MS17-010 hoàn tất không có phán quyết. | Có (cắt bỏ phần terminal phía trên của lệnh NSE-01, hình nền desktop và khoảng trống thừa). | **OPTIONAL / DROP** | **Dự phòng (Phương án mở rộng)**. Trong phương án tối ưu khuyến nghị (3 hình), ảnh này được xếp loại OPTIONAL/DROP và nhường chỗ cho phân tích Bảng 3.6. Nếu hội đồng yêu cầu minh chứng đầy đủ cả hai lệnh đo đạc, ảnh sẽ được dùng làm Hình 3.12. |

---

## 3. Phân Tích Chuyên Sâu Về Chiến Lược Tối Giản Hình Ảnh

### 3.1. Nguyên tắc chống biến báo cáo thành "album ảnh chụp màn hình"
- Trong nghiên cứu kỹ thuật an toàn thông tin, mỗi hình ảnh đưa vào báo cáo phải trả lời được một câu hỏi khoa học cụ thể và mang giá trị thông tin không thể thay thế bằng văn bản hay bảng biểu.
- Case C có tới 9 ảnh chụp màn hình ứng viên. Nếu đưa toàn bộ hoặc phần lớn vào Mục 3.5, người chấm luận văn sẽ thấy một tài liệu chứa đầy các bước thiết lập cấu hình giao diện mạng, làm loãng trọng tâm khoa học của đề tài là **đo đạc, đối chiếu và đánh giá an ninh thực nghiệm**.
- Do đó, việc mạnh dạn loại bỏ (DROP) 4 ảnh (`03_Interface_Assignment`, `05_Bridge_Filtering`, `06_Baseline_Pass_Rule`, `07_Block_Rule_Config`) là quyết định đúng đắn, chuyển tải toàn bộ các thông số kỹ thuật này vào Bảng 3.6 và văn xuôi mô tả có cấu trúc.

### 3.2. Cặp bài trùng chính sách an ninh: Vì sao chọn `pfSense_08` thay vì `pfSense_07`?
- Ảnh `pfSense_07_Block_Rule_Config.png` chụp lại form chỉnh sửa một quy tắc duy nhất. Ảnh có tỷ lệ khung hình bất thường ($485 \times 2246\,\text{px}$), chiều cao gấp gần 5 lần chiều rộng. Nếu chèn nguyên bản vào trang in A4 portrait, ảnh sẽ chiếm 2–3 trang hoặc buộc phải co nhỏ tới mức không thể đọc được chữ.
- Ngược lại, ảnh `pfSense_08_Rule_Order.png` ($485 \times 731\,\text{px}$) có tỷ lệ khung hình cân đối, hiển thị dạng bảng danh sách quy tắc chuẩn mực của pfSense:
  * Thể hiện rõ hành động Block (X đỏ) và Pass (dấu kiểm xanh).
  * Thể hiện biểu tượng ghi log (quy tắc Block được cấu hình ghi log).
  * Thể hiện địa chỉ nguồn, đích và cổng dịch vụ (`SMB_Ports`).
  * Thể hiện trực tiếp sự tồn tại của quy tắc Block và thứ tự hiển thị: quy tắc Block nằm ở Dòng 1, phía trên quy tắc Pass ở Dòng 2.
- Báo cáo kết quả Chương 3 chỉ cần ghi nhận thứ tự sắp xếp quy tắc thực tế trong cấu hình; không cần phân tích lý thuyết rườm rà hay khẳng định tuyệt đối về cơ chế nội bộ của bộ lọc gói tin. Do đó, `pfSense_08` mang giá trị chứng minh thực nghiệm vượt trội so với `pfSense_07`.

### 3.3. So sánh lựa chọn giữa Phương án 3 Hình (Khuyến nghị) và Phương án 4 Hình (Mở rộng)
- **Phương án A — Khuyến nghị chính thức (3 Hình: 3.9, 3.10, 3.11):**
  * `Hình 3.9`: Cấu hình và thứ tự quy tắc tường lửa trên pfSense (`pfSense_08_Rule_Order.png`).
  * `Hình 3.10`: Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux (`pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`).
  * `Hình 3.11`: Nhật ký pfSense ghi nhận chặn lưu lượng TCP SYN tới cổng SMB (`pfSense_10_Block_Log_CANONICAL.png`).
  * *Ưu điểm:* Cấu trúc cân đối hoàn hảo (1 hình chính sách tường lửa + 1 hình đo đạc mạng từ xa + 1 hình nhật ký đối chiếu liên tầng). Tiết kiệm diện tích trang in, tập trung cao độ vào bản chất thực nghiệm. Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng (phân loại UNKNOWN / NO USABLE SCRIPT RESULT; nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có); kết quả này được Bảng 3.6 và văn xuôi đối chiếu mạch lạc, tương tự như tiền lệ Case B đã được người dùng và hội đồng phê chuẩn.
- **Phương án B — Phương án mở rộng (4 Hình: bổ sung Hình 3.12):**
  * Bổ sung `Hình 3.12` từ ảnh `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` để minh chứng trực quan màn hình terminal chạy lệnh `smb-vuln-ms17-010`.
  * *Đặc điểm:* Ảnh hiển thị cổng 445 `filtered` và không có khối kết quả script. Phương án này được lưu giữ sẵn trong kế hoạch như một giải pháp dự phòng nếu người đánh giá ngoài hoặc giảng viên yêu cầu phải thấy ảnh terminal của lệnh NSE-04.

---

## 4. Đề Xuất Khung Cắt Cúp Dự Kiến Có Thể Tái Lập (Provisional Reproducible Crop Proposals)

> **LƯU Ý:** Bước này **TUYỆT ĐỐI KHÔNG TẠO TỆP CẮT CÚP THẬT TRÊN ĐĨA**. Các thông số tọa độ dưới đây chỉ là đề xuất kỹ thuật dự kiến phục vụ Pass 1 (X7E1).

### 4.1. Hình 3.9 — Danh sách và thứ tự quy tắc tường lửa pfSense trên giao diện kiểm thử
- **Tệp gốc:** `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png`
- **Kích thước gốc:** $485 \times 731\,\text{px}$.
- **Vị trí đề xuất:** Tiểu mục `3.5.1`.
- **Chú thích đề xuất:** *Hình 3.9. Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự ưu tiên trên giao diện CASE_C_KALI của tường lửa pfSense*
- **Khung cắt cúp dự kiến (Hiệu chỉnh R2):**
  * Khung tọa độ đề xuất: `x ≈ 15, y ≈ 190, width ≈ 470, height ≈ 340` (vùng `[left=15, top=190, right=485, bottom=530]`).
- **Vùng bắt buộc giữ lại (Must keep):**
  * Thẻ ngữ cảnh giao diện mạng đang chọn: `CASE_C_KALI` (và thanh tab giao diện).
  * Tiêu đề bảng quy tắc: `Rules (Drag to Change Order)` cùng các cột States, Protocol, Source, Port, Destination, Port.
  * Toàn bộ Dòng 1: Hộp kiểm, biểu tượng X đỏ, biểu tượng ghi log, `IPv4 TCP`, `192.168.56.10 *`, `192.168.56.20 SMB_Ports`.
  * Toàn bộ Dòng 2: Hộp kiểm, dấu kiểm xanh, `IPv4 *`, `192.168.56.10 *`, `192.168.56.20 *`.
- **Vùng loại bỏ (Must drop):**
  * Phần cảnh báo mật khẩu mặc định và logo pfSense phía trên ($y < 190$).
  * Các nút chức năng (Add, Delete, Toggle, Copy, Save, Separator) và chân trang bản quyền Netgate phía dưới ($y > 530$).
- **Mục đích:** Loại bỏ cảnh báo mật khẩu thừa, giữ trọn vẹn ngữ cảnh giao diện `CASE_C_KALI`, tiêu đề bảng và cả hai dòng quy tắc Block và Pass.

### 4.2. Hình 3.10 — Kết quả quét cổng dịch vụ SMB từ trạm kiểm thử Kali Linux
- **Tệp gốc:** `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`
- **Kích thước gốc:** $1280 \times 800\,\text{px}$.
- **Vị trí đề xuất:** Tiểu mục `3.5.2`.
- **Chú thích đề xuất:** *Hình 3.10. Kết quả đo đạc trạng thái cổng dịch vụ SMB từ trạm Kali Linux qua đường truyền tường lửa pfSense*
- **Khung cắt cúp dự kiến:**
  * Khung tọa độ: `x = 195, y = 120, width = 660, height = 505` (vùng `[left=195, top=120, right=855, bottom=625]`).
- **Vùng bắt buộc giữ lại (Must keep):**
  * Toàn bộ dòng lệnh thực thi: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`.
  * Dòng thông báo phiên bản và thời gian bắt đầu quét Nmap.
  * Dòng báo cáo máy chủ hoạt động: `Host is up, received arp-response (0.00054s latency)`.
  * Bảng kết quả cả hai cổng dịch vụ:
    - `139/tcp filtered netbios-ssn no-response`
    - `445/tcp filtered microsoft-ds no-response`
  * Dòng địa chỉ MAC card mạng ảo: `MAC Address: 08:00:27:55:71:CE (Oracle VirtualBox virtual NIC)`.
  * Dòng thông báo hoàn tất: `Nmap done: 1 IP address (1 host up) scanned in 1.33 seconds` và dấu nhắc lệnh kết thúc.
- **Vùng loại bỏ (Must drop):**
  * Thanh tác vụ trên cùng của desktop Kali ($y < 30$), hình nền đồ họa desktop và các biểu tượng Home, File System, Trash bên trái ($x < 195, x > 855$).
- **Mục đích:** Giữ trọn vẹn các thành phần cốt lõi của phiên quét cổng trong một khung hình sắc nét, cân đối trên trang in A4.

### 4.3. Hình 3.11 — Nhật ký chặn gói tin SMB SYN trên tường lửa pfSense (Provisional Only)
- **Tệp gốc:** `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png`
- **Kích thước gốc:** $1359 \times 17637\,\text{px}$.
- **Vị trí đề xuất:** Tiểu mục `3.5.2`.
- **Chú thích đề xuất:** *Hình 3.11. Nhật ký tường lửa pfSense ghi nhận hành vi chặn các gói tin TCP SYN hướng tới cổng dịch vụ SMB*
- **Tình trạng khung cắt cúp:** **ĐỀ XUẤT TẠM THỜI (PROVISIONAL ONLY)**.
  * *Lưu ý kỹ thuật bắt buộc:* Do tệp ảnh gốc có chiều cao rất lớn ($17637\,\text{px}$), tọa độ dưới đây chỉ mang tính định hướng ban đầu. Khi bước vào pha X7E1 và tạo tệp ảnh cắt cúp thật, người thực hiện **bắt buộc phải trực tiếp kiểm tra lại vùng hiển thị trên ảnh gốc** trước khi chốt tọa độ cắt cúp cuối cùng.
- **Khung tọa độ dự kiến ban đầu:**
  * Khung ngang: `x = 40, width = 1280` (vùng `[left=40, right=1320]`).
  * Khung dọc dự kiến: Khoảng $y \approx 15280$ đến $y \approx 15550$ (chiều cao khoảng 270 px), bao quát các dòng log tại thời điểm 14:20:18 và 14:20:19.
- **Vùng bắt buộc giữ lại (Must keep):**
  * Tiêu đề các cột dữ liệu cần thiết: `Action`, `Time`, `Interface`, `Rule`, `Source`, `Destination`, `Protocol`.
  * Các dòng nhật ký khớp với đợt quét của trạm Kali:
    - Dòng 1: `Action: Block (X đỏ)`, `Time: Oct 4 14:20:18`, `Interface: CASE_C_KALI`, `Source: 192.168.56.10:39801`, `Destination: 192.168.56.20:139`, `Protocol: TCP:S`.
    - Dòng 2: `Action: Block (X đỏ)`, `Time: Oct 4 14:20:19`, `Interface: CASE_C_KALI`, `Source: 192.168.56.10:39803`, `Destination: 192.168.56.20:139`, `Protocol: TCP:S`.
    - Dòng 3: `Action: Block (X đỏ)`, `Time: Oct 4 14:20:19`, `Interface: CASE_C_KALI`, `Source: 192.168.56.10:39804`, `Destination: 192.168.56.20:445`, `Protocol: TCP:S`.
  * Cột `Rule` hiển thị nhãn quy tắc mâu thuẫn (nếu cột này được đưa vào khung hình).
- **Ranh giới xử lý mâu thuẫn:** **TUYỆT ĐỐI KHÔNG cắt bỏ cột Rule nhằm né tránh mâu thuẫn nhãn quy tắc.** Mâu thuẫn này phải được bảo tồn và giải thích minh bạch trong báo cáo.
- **Vùng loại bỏ (Must drop):**
  * Các dòng nhật ký từ chối mặc định không liên quan đến đợt quét SMB của Kali ($y < 15280$ và $y > 15550$).

### 4.4. Hình 3.12 (Tùy chọn dự phòng) — Kết quả kiểm tra lỗ hổng MS17-010 từ trạm Kali Linux
- **Tệp gốc:** `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png`
- **Kích thước gốc:** $1280 \times 800\,\text{px}$.
- **Vị trí đề xuất:** Tiểu mục `3.5.2` (chỉ dùng khi chọn Phương án B).
- **Chú thích đề xuất:** *Hình 3.12. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux khi cổng 445 ở trạng thái filtered*
- **Khung cắt cúp dự kiến:**
  * Khung tọa độ: `x = 195, y = 300, width = 660, height = 325` (vùng `[left=195, top=300, right=855, bottom=625]`).
- **Vùng bắt buộc giữ lại (Must keep):**
  * Dòng lệnh: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`.
  * Dòng trạng thái: `445/tcp filtered microsoft-ds`.
  * Dòng hoàn tất: `Nmap done: 1 IP address (1 host up) scanned in 0.51 seconds`.
- **Vùng loại bỏ (Must drop):**
  * Phần terminal phía trên thuộc về lệnh NSE-01 ($y < 300$), desktop và thanh tác vụ ngoài cửa sổ console.

---

## 5. Kết Luận Phân Bổ Hình Ảnh Cho Mục 3.5

- **Tổng số ảnh gốc thẩm tra:** 9 ảnh.
- **Số ảnh KEEP (chọn đưa vào báo cáo chính thức):** 3 ảnh (`pfSense_08_Rule_Order.png`, `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`, `pfSense_10_Block_Log_CANONICAL.png`).
- **Số ảnh OPTIONAL / DROP (dự phòng có kiểm soát):** 2 ảnh (`pfSense_04_Bridge.png`, `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png`).
- **Số ảnh DROP (loại bỏ hoàn toàn):** 4 ảnh (`pfSense_03_Interface_Assignment.png`, `pfSense_05_Bridge_Filtering.png`, `pfSense_06_Baseline_Pass_Rule.png`, `pfSense_07_Block_Rule_Config.png`).
- **Số lượng ảnh mới được tạo ra trên đĩa:** 0 (tuân thủ nghiêm ngặt quy định Pass 0 — Không tạo phái sinh trước khi được duyệt).
