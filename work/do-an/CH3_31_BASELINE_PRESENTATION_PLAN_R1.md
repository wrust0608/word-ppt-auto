# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.1 BASELINE (CH3_31_BASELINE_PRESENTATION_PLAN_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 R2 — Correct Baseline Evidence & Presentation Plan`
- **Ràng buộc tuyệt đối:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI (ZERO PROSE)**. Tài liệu này chỉ thiết kế cấu trúc đề mục H3, cấu trúc 2 bảng biểu sinh viên ngắn gọn, vị trí bố trí 3 hình ảnh, câu dẫn và kết luận kỹ thuật có điều kiện, chính sách cắt cúp không khóa tọa độ cứng và đoạn chuyển tiếp ý niệm cho Mục 3.1.

---

## 1. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

Mục 3.1 sử dụng cấu trúc 2 tiểu mục H3 ngắn gọn, chuẩn mực học thuật, không dùng thuật ngữ kiểm toán nội bộ hay danh pháp tiếng Anh:

### `3.1. Trạng thái baseline trước đo đạc`
- **`3.1.1. Trạng thái mạng và dịch vụ SMB`**
  * *Nhiệm vụ trọng tâm:* Trình bày thông số định danh mạng (IP, Subnet, Route, Adapter, phạm vi kết nối), trạng thái dịch vụ chia sẻ tệp (LanmanServer, FS-SMB1, các cờ kích hoạt phương ngữ nội bộ, thiết lập ký số) và chính sách tường lửa Windows (các profile được bật, vô hiệu hóa 16 quy tắc chia sẻ tệp mặc định, quy tắc tùy biến giới hạn địa chỉ nguồn từ trạm Kali).
  * *Hình thức trình bày:* Bảng 3.1 (Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc); Hình 3.1 (Tổng hợp cấu hình mạng và dịch vụ); Hình 3.2 (Cấu hình quy tắc tường lửa tùy biến).
- **`3.1.2. Trạng thái bản vá và mốc phục hồi`**
  * *Nhiệm vụ trọng tâm:* Trình bày phương pháp xác minh kép đối với driver nhân `srv.sys` (chuỗi hiển thị `6.3.9600.16384` so với phiên bản số nhị phân `6.3.9600.16421`), đối chiếu với ngưỡng cập nhật tối thiểu `6.3.9600.18604` theo tài liệu chính thức của Microsoft (Article 4023262) ứng với gói KB4012213 / KB4012216, kiểm kê danh mục 6 bản vá hệ thống ghi nhận được, xác lập phân loại trạng thái bản vá cục bộ là `UNPATCHED`, và công bố điểm phục hồi `Before Demo` trên máy ảo.
  * *Hình thức trình bày:* Bảng 3.2 (Trạng thái bản vá và mốc phục hồi); Hình 3.3 (Thuộc tính phiên bản driver srv.sys và danh mục bản vá ghi nhận).

---

## 2. Thiết Kế Bảng Biểu Trình Bày Học Thuật (Student-Facing Tables)

Thay thế bảng kiểm toán nội bộ 16 hàng 5 cột cồng kềnh trước đây bằng 2 bảng báo cáo sinh viên độc lập, mạch lạc, dễ đọc trên khổ giấy in A4 tiêu chuẩn HUIT. Các bảng tuyệt đối không chứa tên tệp bằng chứng, mã Evidence ID/Claim ID, hay cột phán xét rủi ro/hiệu quả.

### 2.1. Bảng 3.1 — Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc
- **Số hiệu dự kiến:** `Bảng 3.1` (Số tạm theo `CHAPTER_3_NUMBERING_LEDGER.md`, sẽ khóa chính thức sau khi người dùng phê duyệt section).
- **Câu hỏi của người đọc được trả lời:** *Môi trường thử nghiệm có những thông số mạng, dịch vụ chia sẻ tệp và thiết lập tường lửa nào được xác lập trên máy chủ trước khi tiến hành các lượt quét thăm dò?*
- **Cấu trúc cột:** `Hạng mục | Giá trị ghi nhận | Ghi chú`

| Hạng mục | Giá trị ghi nhận | Ghi chú |
|---|---|---|
| Địa chỉ IP và mạng con Kali Linux | `192.168.56.10/24` (giao diện `eth0`) | Tuyến mạng cục bộ `192.168.56.0/24`, không cấu hình default route |
| Địa chỉ IP và mạng con Windows Server | `192.168.56.20/24` (giao diện `Ethernet`) | Bảng định tuyến cục bộ, không cấu hình default route |
| Cấu hình card mạng VirtualBox | 1 card Host-Only Adapter trên mỗi máy ảo | Cấu hình giới hạn đường truyền trong phân đoạn lab, không cấu hình card NAT hay Bridged |
| Dịch vụ chia sẻ tệp (LanmanServer) | `Running` (chế độ khởi động `Automatic`) | Dịch vụ SMB đang chạy cục bộ trên máy chủ mục tiêu |
| Tính năng Windows FS-SMB1 | `Installed` | Thành phần SMBv1 được cài đặt sẵn trên hệ điều hành |
| Cấu hình phương ngữ SMB cục bộ | `EnableSMB1Protocol : True`<br>`EnableSMB2Protocol : True` | Máy chủ kích hoạt hỗ trợ SMBv1 và SMB2/SMB3 ở mức cấu hình nội bộ |
| Chính sách ký số gói tin SMB nội bộ | `EnableSecuritySignature : False`<br>`RequireSecuritySignature : False` | Thiết lập ký số cục bộ không bắt buộc |
| Trạng thái lắng nghe cổng cục bộ | TCP 445 (`::`)<br>TCP 139 (`192.168.56.20`) | Tiến trình hệ thống đang lắng nghe cục bộ trên cổng 139 và 445 |
| Trạng thái hồ sơ Windows Firewall | Domain: `True`, Private: `True`, Public: `True` | Toàn bộ 3 hồ sơ tường lửa Windows đều được kích hoạt bảo vệ |
| Nhóm quy tắc chia sẻ tệp mặc định | 16 quy tắc `File and Printer Sharing` đều `False` | Các quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa |
| Quy tắc tường lửa tùy biến | Tên: `ATTT Lab SMB 139-445`<br>Action: `Allow`, Direction: `Inbound`<br>Protocol: `TCP`, LocalPort: `{139, 445}` | Quy tắc cho phép có phạm vi RemoteAddress giới hạn duy nhất tại `192.168.56.10` |

*Ghi chú ranh giới:* Bảng 3.1 tập trung vào các thông số mạng và dịch vụ có thể xác minh được. Lượt thử nghiệm ICMP Echo (ping) nhận 0 phản hồi được lược bỏ khỏi bảng báo cáo chính nhằm tránh đưa thông tin nhiễu và tránh quy kết nguyên nhân chủ quan do tường lửa.

---

### 2.2. Bảng 3.2 — Trạng thái bản vá và mốc phục hồi
- **Số hiệu dự kiến:** `Bảng 3.2` (Số tạm theo `CHAPTER_3_NUMBERING_LEDGER.md`, sẽ khóa chính thức sau khi người dùng phê duyệt section).
- **Câu hỏi của người đọc được trả lời:** *Trạng thái bản vá đối với lỗ hổng MS17-010 trên máy chủ mục tiêu được xác định như thế nào và mốc phục hồi môi trường được thiết lập ra sao?*
- **Cấu trúc cột:** `Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn`

| Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn |
|---|---|---|
| Chuỗi phiên bản hiển thị tệp `srv.sys` | `FileVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)` | Chuỗi ký tự thuộc tính hiển thị của tệp driver |
| Phiên bản số nhị phân tệp `srv.sys` | `6.3.9600.16421` | Trích xuất từ 4 trường số FileMajor, FileMinor, FileBuild, FilePrivate |
| Ngưỡng phiên bản cập nhật tối thiểu | `6.3.9600.18604` | Căn cứ tài liệu Microsoft Support (Article 4023262) cho Windows Server 2012 R2 |
| Mã bản vá liên quan khắc phục MS17-010 | `KB4012213` (Security Only) hoặc `KB4012216` (Monthly Rollup) | Các gói cập nhật chính thức áp dụng cho Windows Server 2012 R2 |
| Danh mục bản vá hệ thống ghi nhận | 6 bản vá (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621 cài ngày 21/03/2014) | Danh mục ghi nhận không chứa KB4012213, KB4012216 hoặc bản vá thay thế chứa bản sửa lỗi MS17-010 |
| Phân loại trạng thái bản vá cục bộ | **`UNPATCHED`** | Kết luận đối chiếu: phiên bản số nhị phân thấp hơn ngưỡng tối thiểu ($6.3.9600.16421 < 6.3.9600.18604$) và thiếu bản vá tương ứng |
| Mốc khôi phục môi trường (Snapshot) | `Before Demo` | Điểm phục hồi được ghi nhận cho cả hai máy ảo ở trạng thái tắt máy sạch |

---

## 3. Kế Hoạch Bố Trí Hình Ảnh R2 (Figure Placement & Visual Directives)

### 3.1. Hình 3.1 (Tạm thời) — Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.1.1`, ngay sau Bảng 3.1.
- **Câu văn dẫn nhập (Preceding Directive Sentence):**
  *"Hình 3.1 trình bày kết quả kiểm tra tổng hợp cấu hình mạng, trạng thái dịch vụ chia sẻ tệp và các cổng lắng nghe trên máy chủ Windows Server 2012 R2 thông qua giao diện Windows PowerShell trước thực nghiệm."*
- **Quan sát trực tiếp được phép diễn giải (Direct Observations Allowed):**
  1. Giao diện PowerShell ghi nhận địa chỉ IP của giao diện Ethernet là `192.168.56.20/24`.
  2. Dịch vụ `LanmanServer` ở trạng thái `Running` với `StartType` là `Automatic`.
  3. Tính năng `FS-SMB1` hiển thị trạng thái `Installed`.
  4. Cấu hình dịch vụ SMB ghi nhận `EnableSMB1Protocol : True` và `EnableSMB2Protocol : True`.
  5. Kiểm tra kết nối mạng cục bộ ghi nhận cổng TCP 445 (`::`) và cổng TCP 139 (`192.168.56.20`) đang ở trạng thái `Listen` bởi tiến trình System (PID 4).
  6. Lệnh trích xuất thuộc tính driver `srv.sys` ghi nhận giá trị phiên bản số nhị phân cấu thành là `6.3.9600.16421`.
- **Ranh giới nghiêm ngặt — Điều TUYỆT ĐỐI KHÔNG ĐƯỢC suy diễn:**
  * **CẤM:** Không đồng nhất việc cổng 139/445 đang lắng nghe cục bộ trên máy chủ với việc cổng đó ở trạng thái `OPEN` nhìn từ xa qua mạng. Khả năng tiếp cận từ xa phụ thuộc vào chính sách tường lửa và đường truyền mạng, sẽ được kiểm chứng độc lập ở Kịch bản 1.
  * **CẤM:** Không tuyên bố bức ảnh chứng minh mọi giá trị tham số trong Bảng 3.1 nếu phần ảnh hiển thị không bao hàm thông tin đó.

---

### 3.2. Hình 3.2 (Tạm thời) — Cấu hình quy tắc tường lửa tùy biến
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.1.1`, đi kèm phần phân tích chính sách kiểm soát phạm vi kết nối.
- **Câu văn dẫn nhập (Preceding Directive Sentence):**
  *"Hình 3.2 minh chứng các thuộc tính cấu hình của quy tắc tường lửa tùy biến ATTT Lab SMB 139-445 cùng trạng thái các hồ sơ tường lửa trên máy chủ mục tiêu."*
- **Quan sát trực tiếp được phép diễn giải (Direct Observations Allowed):**
  1. Quy tắc `ATTT Lab SMB 139-445` được kích hoạt (`Enabled: True`), chiều lưu lượng đi vào (`Direction: Inbound`), hành động cho phép (`Action: Allow`).
  2. Giao thức áp dụng là `TCP`, cổng dịch vụ đích cục bộ là `{139, 445}`.
  3. Phạm vi địa chỉ nguồn từ xa (`RemoteAddress`) được chỉ định duy nhất là `192.168.56.10` (trạm Kali Linux).
  4. Cả 3 hồ sơ tường lửa (`Domain`, `Private`, `Public`) đều đang bật (`Enabled: True`) và toàn bộ 16 quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa (`Count: 16, False`).
- **Ranh giới nghiêm ngặt — Điều TUYỆT ĐỐI KHÔNG ĐƯỢC suy diễn:**
  * **CẤM:** Không suy diễn từ sự tồn tại của quy tắc tùy biến này rằng "mọi địa chỉ IP khác chắc chắn bị chặn trên mọi phương diện". Bằng chứng chỉ xác nhận quy tắc cho phép cụ thể này áp dụng cho nguồn .56.10 và các luật mặc định bị tắt.
  * **CẤM:** Không kết luận máy chủ tồn tại lỗ hổng an ninh chỉ từ việc có quy tắc tường lửa cho phép kết nối cổng SMB.

---

### 3.3. Hình 3.3 (Tạm thời) — Thuộc tính phiên bản tệp driver `srv.sys` và danh mục bản vá
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.1.2`, ngay sau Bảng 3.2.
- **Câu văn dẫn nhập (Preceding Directive Sentence):**
  *"Hình 3.3 thể hiện kết quả kiểm tra thuộc tính phiên bản của driver nhân srv.sys kết hợp danh mục các bản vá hệ thống được ghi nhận trên máy chủ Windows Server 2012 R2."*
- **Quan sát trực tiếp được phép diễn giải (Direct Observations Allowed):**
  1. Câu lệnh trích xuất thuộc tính `FileVersion` cho chuỗi hiển thị `6.3.9600.16384 (winblue_rtm.130821-1623)`.
  2. Câu lệnh ghép nối 4 trường nhị phân (`FileMajorPart`, `FileMinorPart`, `FileBuildPart`, `FilePrivatePart`) xác nhận giá trị phiên bản số thực tế là `6.3.9600.16421`.
  3. Lệnh `Get-HotFix` ghi nhận danh sách 6 bản vá hệ thống có ngày cài đặt 21/03/2014; trong danh mục hiển thị không ghi nhận KB4012213 hoặc KB4012216.
- **Ranh giới nghiêm ngặt — Điều TUYỆT ĐỐI KHÔNG ĐƯỢC suy diễn:**
  * **CẤM:** Tuyệt đối không đưa chữ "UNPATCHED" trực tiếp vào tiêu đề hình ảnh. Phán quyết `UNPATCHED` là kết luận tổng hợp khi đối chiếu phiên bản số nhị phân `6.3.9600.16421` thấp hơn ngưỡng tối thiểu `6.3.9600.18604` kết hợp danh mục hotfix vắng mặt bản cập nhật tương ứng theo tài liệu Microsoft Support (Article 4023262).
  * **CẤM:** Trạng thái chưa vá cục bộ của hệ điều hành độc lập với tín hiệu quét từ xa qua mạng và không đồng nghĩa với việc lỗ hổng chắc chắn bị khai thác thành công qua mạng.

---

## 4. Chính Sách Cắt Cúp Hình Ảnh R2 (Non-Rigid Crop Policy)

Trong pha kế hoạch R2, tuyệt đối không khóa cứng tọa độ pixel. Quy trình tạo ảnh phái sinh chỉ thực hiện khi biên tập báo cáo thực tế và đáp ứng các tiêu chí định tính sau:

### 4.1. Đề xuất cắt cúp đối với `Windows_PreDemo_01_Network_SMB.png` (Hình 3.1)
- **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png`
- **SHA-256 nguồn:** `e3744451374e9544f29dda79b06bd1e8df122119ef046b20dfb9f396d65a0b34`
- **Vùng thông tin phải giữ:** Toàn bộ cửa sổ PowerShell hiển thị các lệnh kiểm toán mạng, dịch vụ LanmanServer, cấu hình SMB server, cổng lắng nghe và phiên bản srv.sys.
- **Giao diện thừa có thể loại bỏ:** Vùng nền desktop Server Manager trống bên phải và thanh taskbar bên dưới.
- **Ngữ cảnh bắt buộc bảo tồn:** Tiêu đề cửa sổ PowerShell, các câu lệnh đã chạy và các khối kết quả đầu ra.
- **Mục đích trình bày:** Tối ưu hóa kích thước chữ khi chèn vào trang văn bản A4, giúp người đọc dễ dàng theo dõi chi tiết cấu hình dịch vụ.

### 4.2. Đề xuất cắt cúp đối với `Windows_PreDemo_02_Firewall.png` (Hình 3.2)
- **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`
- **SHA-256 nguồn:** `c685573c3c1d00460d49d8718cc02a48ef8bceda26ce5cac1ab913e1db0d7077`
- **Vùng thông tin phải giữ:** Cửa sổ PowerShell hiển thị 5 khối lệnh kiểm toán tường lửa (thuộc tính quy tắc tùy biến, hồ sơ tường lửa, danh sách luật mặc định).
- **Giao diện thừa có thể loại bỏ:** Thanh taskbar và phần nền Server Manager mờ phía sau.
- **Ngữ cảnh bắt buộc bảo tồn:** Tên quy tắc `ATTT Lab SMB 139-445`, cổng `{139, 445}`, địa chỉ nguồn `192.168.56.10`, trạng thái 3 profile `True` và số lượng 16 luật mặc định `False`.
- **Mục đích trình bày:** Loại bỏ chi tiết giao diện không mang thông tin, tập trung trực quan vào chính sách an ninh mạng.

### 4.3. Đề xuất cắt cúp đối với `Windows_MS17010_02_Hotfix.png` (Hình 3.3)
- **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_MS17010_02_Hotfix.png`
- **SHA-256 nguồn:** `c2130e7256c08f592f9f884ec979e505c775cdfb74bc149dfa63fef5335e658f`
- **Vùng thông tin phải giữ:** Cửa sổ PowerShell chứa toàn bộ các lệnh lấy thuộc tính tệp `srv.sys` và bảng kết quả `Get-HotFix`.
- **Giao diện thừa có thể loại bỏ:** Thanh taskbar và bong bóng thông báo "View messages in Action Center" ở khay hệ thống, phần nền desktop trống.
- **Ngữ cảnh bắt buộc bảo tồn:** Toàn bộ nội dung lệnh kiểm tra `srv.sys`, các dòng chuỗi/số phiên bản và bảng danh mục 6 hotfix.
- **Mục đích trình bày:** Loại bỏ popup thông báo không liên quan ở khay hệ thống, bảo đảm tính trang nghiêm khoa học và độ rõ nét của bằng chứng bản vá.

---

## 5. Đoạn Chuyển Tiếp Ý Niệm Sang Mục 3.2 (Conceptual Transition to Section 3.2)

- **Bản chất logic chuyển tiếp:**
  Sau khi toàn bộ tham số môi trường mạng, dịch vụ SMB, chính sách tường lửa kiểm soát phạm vi nguồn và trạng thái bản vá cục bộ của máy chủ (`UNPATCHED` đối với MS17-010) đã được ghi nhận độc lập tại mốc chuẩn xuất phát, hệ thống máy ảo được xác lập tại điểm phục hồi `Before Demo`.
  Tiếp theo, trạm kiểm thử Kali Linux bắt đầu tiến trình thực nghiệm Kịch bản 1 nhằm rà quét, phát hiện mục tiêu và định danh dịch vụ SMB từ góc nhìn mạng bên ngoài mà không cần bỏ qua kiểm tra trực tuyến (`không dùng cờ -Pn`), qua đó thiết lập bức tranh thực tế về khả năng tiếp cận dịch vụ trước khi tiến hành kiểm định dấu hiệu lỗ hổng an ninh chuyên sâu.
