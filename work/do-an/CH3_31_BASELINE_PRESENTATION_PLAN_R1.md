# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.1 BASELINE (CH3_31_BASELINE_PRESENTATION_PLAN_R1)

- **Trạng thái:** `PLAN_LOCKED_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A0 — Baseline Evidence & Presentation Plan`
- **Ràng buộc:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI (ZERO PROSE)**. Tài liệu này chỉ thiết kế cấu trúc đề mục H3, cấu trúc bảng biểu, vị trí bố trí hình ảnh, các câu dẫn/kết luận kỹ thuật có điều kiện và đoạn chuyển tiếp ý niệm cho Mục 3.1.

---

## 1. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

Mục 3.1 giữ nguyên cấu trúc 2 tiểu mục H3 logic và mạch lạc theo đúng định hướng phương pháp tại Chương 2:

### `3.1. Trạng thái baseline trước đo đạc`
- **`3.1.1. Cấu hình hạ tầng mạng, dịch vụ và chính sách tường lửa kiểm soát`**
  * *Nhiệm vụ trọng tâm:* Công bố toàn bộ thông số định danh mạng (IP, Subnet, Route, Adapter, tính cô lập Internet), trạng thái dịch vụ chia sẻ tệp (LanmanServer, FS-SMB1, các dialect được kích hoạt, chính sách ký gói tin) và chính sách tường lửa máy chủ (bật toàn bộ profile, tắt 16 luật chia sẻ tệp mặc định, thiết lập quy tắc tùy biến giới hạn địa chỉ nguồn duy nhất cho trạm Kali).
  * *Hình thức trình bày:* 1 Bảng tổng hợp các thông số mạng/dịch vụ/tường lửa; 1 Hình minh chứng quy tắc tường lửa tùy biến (Hình 3.2 tạm thời).
- **`3.1.2. Trạng thái bản vá hệ thống và mốc khôi phục môi trường`**
  * *Nhiệm vụ trọng tâm:* Trình bày phương pháp thẩm tra kép đối với driver nhân `srv.sys` (chuỗi hiển thị `6.3.9600.16384` so với phiên bản số cấu thành `6.3.9600.16421`), đối chiếu với ngưỡng cập nhật tối thiểu `6.3.9600.18604` theo tài liệu chính thức của Microsoft (KB4012213 / KB4012216), kiểm kê danh mục 6 bản vá hệ thống đã cài đặt, xác lập phán quyết trạng thái bản vá cục bộ là `UNPATCHED`, và công bố điểm khôi phục `Before Demo` trên hypervisor.
  * *Hình thức trình bày:* 1 Bảng tổng hợp đối chiếu trạng thái bản vá và snapshot; 1 Hình minh chứng trích xuất thuộc tính phiên bản tệp `srv.sys` (Hình 3.1 tạm thời).

---

## 2. Thiết Kế Bảng Biểu Tổng Hợp Mốc Xuất Phát (Proposed Tables)

Nhằm tối ưu hóa trải nghiệm của người đọc học thuật và tránh chia cắt dữ liệu vụn vặt, toàn bộ mốc chuẩn xuất phát được cấu trúc thành **Bảng 3.1 (Tạm thời)** toàn diện, có phân chia thành 4 nhóm khối tham số mạch lạc.

### Bảng 3.1 (Tạm thời): Bảng tổng hợp thông số kiểm toán mốc chuẩn xuất phát trước thực nghiệm
- **Số hiệu dự kiến:** `Bảng 3.1` (Số tạm theo `CHAPTER_3_NUMBERING_LEDGER.md`, sẽ khóa chính thức sau khi người dùng phê duyệt section).
- **Câu hỏi của người đọc được trả lời:** *Môi trường thử nghiệm có những tham số mạng, dịch vụ, tường lửa và trạng thái bản vá nào được xác lập trước khi tiến hành các lượt quét thăm dò?*
- **Các cột (Columns):**
  1. `Khối tham số` (Parameter Category)
  2. `Thuộc tính kiểm toán` (Audit Attribute)
  3. `Giá trị xác lập thực tế` (Observed Value)
  4. `Tệp bằng chứng đối soát` (Evidence Source)
  5. `Ý nghĩa an ninh / Ranh giới kỹ thuật` (Security Significance / Boundary)
- **Các hàng dữ liệu chi tiết (Detailed Rows):**

| Khối tham số | Thuộc tính kiểm toán | Giá trị xác lập thực tế | Tệp bằng chứng đối soát | Ý nghĩa an ninh / Ranh giới kỹ thuật |
|---|---|---|---|---|
| **I. Hạ tầng mạng** | Địa chỉ IP & Subnet Kali Linux | `192.168.56.10/24` (eth0) | `Final_PreDemo_Audit.txt`, `VirtualBox_HostOnly_Config.txt` | Trạm kiểm thử đóng vai trò nguồn phát lưu lượng quét an ninh |
| | Địa chỉ IP & Subnet Windows Server | `192.168.56.20/24` (Ethernet) | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Máy chủ mục tiêu tiếp nhận kiểm thử trong mạng cô lập |
| | Cấu hình VirtualBox NIC | 1 card mạng Host-Only Adapter duy nhất trên mỗi VM | `VirtualBox_HostOnly_Config.txt`, `Before_Demo_Snapshots.txt` | Không dùng NAT/Bridged; ngăn chặn hoàn toàn kết nối ra ngoài Internet |
| | Bảng định tuyến (Routing Table) | Chỉ có tuyến cục bộ `192.168.56.0/24`, không có Default Route | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Môi trường lab hoàn toàn cô lập về mặt định tuyến IP |
| | Kết nối liên máy ảo (Reachability) | ARP L2: `08:00:27:55:71:ce REACHABLE`; ICMP L3: 100% loss | `Kali_to_Windows_Connectivity.png`, `Final_PreDemo_Audit.txt` | Hai máy ảo thông mạng ở tầng L2; ICMP bị tường lửa Windows chặn |
| **II. Dịch vụ SMB** | Dịch vụ chia sẻ tệp (LanmanServer) | Trạng thái `Running`, Khởi động `Automatic` | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Dịch vụ chia sẻ tệp của Windows đang hoạt động bình thường |
| | Tính năng Windows (FS-SMB1) | Trạng thái `Installed` | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Thành phần tính năng SMBv1 đã được cài đặt sẵn trên máy chủ |
| | Cấu hình phương ngữ cục bộ | `EnableSMB1Protocol : True`<br>`EnableSMB2Protocol : True` | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Máy chủ sẵn sàng đàm phán cả SMBv1 và các dialect SMB2/SMB3 |
| | Chính sách ký số gói tin SMB | `EnableSecuritySignature : False`<br>`RequireSecuritySignature : False` | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png` | Cấu hình ký số nội bộ không bắt buộc (chính sách mặc định hệ thống) |
| | Trạng thái lắng nghe cổng cục bộ | `:: : 445` (Listen, Process 4)<br>`192.168.56.20 : 139` (Listen, Process 4) | `Final_PreDemo_Audit.txt`, `Windows_FirewallPrep_Final.txt` | Cổng NetBIOS-SSN (139) và Direct-hosted (445) đang mở cục bộ |
| **III. Tường lửa** | Trạng thái hồ sơ tường lửa | Domain: `True`, Private: `True`, Public: `True` | `Windows_FirewallPrep_Final.txt`, `Windows_PreDemo_02_Firewall.png` | Tường lửa Windows bật bảo vệ trên toàn bộ các hồ sơ mạng |
| | Nhóm luật chia sẻ tệp mặc định | 16 luật `File and Printer Sharing` đều `False` (Disabled) | `Windows_FirewallPrep_Final.txt`, `Windows_PreDemo_02_Firewall.png` | Không cho phép lưu lượng SMB quảng bá hay truy cập đại trà |
| | Quy tắc kiểm soát tùy biến | Tên: `ATTT Lab SMB 139-445`<br>Action: `Allow`, Direction: `Inbound`<br>Protocol: `TCP`, LocalPort: `{139, 445}`<br>RemoteAddress: `192.168.56.10` | `Windows_FirewallPrep_Final.txt`, `Windows_PreDemo_02_Firewall.png` | **Giới hạn phạm vi chặt chẽ:** Chỉ duy nhất trạm Kali được phép kết nối tới cổng 139 và 445; các nguồn IP khác bị chặn |
| **IV. Bản vá & Mốc phục hồi** | Chuỗi phiên bản hiển thị tệp `srv.sys` | `FileVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)` | `Windows_MS17010_01_SrvSysVersion.png`, `MS17-010_Official_Mapping.txt` | Chuỗi ký tự hiển thị thuộc tính tệp (chưa phản ánh phiên bản số nhị phân) |
| | Phiên bản số nhị phân tệp `srv.sys` | `6.3.9600.16421` (Major:6, Minor:3, Build:9600, Private:16421) | `Windows_MS17010_01_SrvSysVersion.png`, `MS17-010_Official_Mapping.txt` | Giá trị số thực tế cấu thành từ 4 trường nhị phân dùng để đối soát |
| | Ngưỡng cập nhật tối thiểu của MS | `6.3.9600.18604` (Tài liệu MS Support 4023262) | `MS17-010_Official_Mapping.txt`, `SOURCE_LEDGER.md` (S032) | Ngưỡng phiên bản driver srv.sys đã vá MS17-010 cho Windows Server 2012 R2 |
| | Danh mục bản vá đã cài đặt | 6 bản vá (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621 - đều cài ngày 21/03/2014) | `MS17-010_Official_Mapping.txt`, `Windows_MS17010_02_Hotfix.png` | Hệ thống thiếu hoàn toàn bản vá KB4012213, KB4012216 hoặc rollup thay thế |
| | Phán quyết trạng thái bản vá | **`UNPATCHED`** | Đối soát chéo: Phiên bản số $6.3.9600.16421 < 6.3.9600.18604$ + Thiếu KB | Khẳng định thực tế khách quan rằng máy chủ chưa vá MS17-010 |
| | Điểm khôi phục (Snapshot) | Tên: `Before Demo` (Trạng thái tắt máy sạch) | `Before_Demo_Snapshots.txt` | Mốc khôi phục chuẩn xác phục vụ cô lập và lặp lại thực nghiệm |

- **Đánh giá về tính trùng lặp:** Bảng 3.1 đóng vai trò là "Bảng sự thật duy nhất" (Single Source of Truth) định hình toàn bộ nền tảng dữ liệu cho Chương 3. Các hình ảnh chỉ minh chứng thị giác cho các điểm mấu chốt (thuộc tính driver và quy tắc tường lửa), hoàn toàn không gây lặp thừa thông tin.

---

## 3. Kế Hoạch Bố Trí Hình Ảnh (Figure Placement & Visual Directives)

### 3.1. Hình 3.1 (Tạm thời) — Thuộc tính phiên bản driver `srv.sys`
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.1.2`, ngay sau đoạn văn phân tích phương pháp xác minh kép thuộc tính tệp driver nhân.
- **Câu văn dẫn nhập (Preceding Directive Sentence):**  
  *"Hình 3.1 trình bày kết quả trích xuất thuộc tính phiên bản của tệp driver srv.sys từ giao diện điều khiển Windows PowerShell trên máy chủ mục tiêu trước khi tiến hành thực nghiệm."*
- **Quan sát trực tiếp được phép diễn giải (Direct Observations Allowed):**
  1. Câu lệnh trích xuất thuộc tính `FileVersion` cho chuỗi giá trị hiển thị là `6.3.9600.16384 (winblue_rtm.130821-1623)`.
  2. Câu lệnh ghép nối 4 trường phiên bản số nhị phân (`FileMajorPart`, `FileMinorPart`, `FileBuildPart`, `FilePrivatePart`) xác nhận giá trị phiên bản số thực tế là `6.3.9600.16421`.
- **Ranh giới nghiêm ngặt — Điều TUYỆT ĐỐI KHÔNG ĐƯỢC suy diễn từ hình ảnh này:**
  * **CẤM:** Ảnh chụp màn hình một mình KHÔNG đủ để tuyên bố máy chủ ở trạng thái UNPATCHED. Phán quyết UNPATCHED chỉ được xác lập khi đối chiếu giá trị số `6.3.9600.16421` thấp hơn ngưỡng chuẩn `6.3.9600.18604` kết hợp kiểm kê bản vá thiếu hụt KB4012213 / KB4012216 theo tài liệu hướng dẫn chính thức của Microsoft (Article 4023262).
  * **CẤM:** Trạng thái chưa vá cục bộ của hệ điều hành không đồng nghĩa với việc lỗ hổng có thể khai thác thành công từ xa qua mạng.

---

### 3.2. Hình 3.2 (Tạm thời) — Cấu hình quy tắc tường lửa tùy biến
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.1.1`, ngay sau đoạn văn giải thích thiết kế kiểm soát phạm vi quét an ninh.
- **Câu văn dẫn nhập (Preceding Directive Sentence):**  
  *"Hình 3.2 minh chứng các thuộc tính cấu hình của quy tắc tường lửa tùy biến ATTT Lab SMB 139-445 được thiết lập trên máy chủ Windows Server 2012 R2."*
- **Quan sát trực tiếp được phép diễn giải (Direct Observations Allowed):**
  1. Quy tắc `ATTT Lab SMB 139-445` được kích hoạt (`Enabled: True`), chiều lưu lượng đi vào (`Direction: Inbound`), hành động cho phép (`Action: Allow`).
  2. Giao thức áp dụng là `TCP`, cổng dịch vụ đích cục bộ là `{139, 445}`.
  3. Phạm vi địa chỉ nguồn từ xa (`RemoteAddress`) được chỉ định nghiêm ngặt là `192.168.56.10` (trạm Kali Linux).
  4. Cả 3 hồ sơ tường lửa (`Domain`, `Private`, `Public`) đều đang bật (`Enabled: True`) và toàn bộ 16 quy tắc chia sẻ tệp mặc định đều bị vô hiệu hóa (`Count: 16, False`).
- **Ranh giới nghiêm ngặt — Điều TUYỆT ĐỐI KHÔNG ĐƯỢC suy diễn từ hình ảnh này:**
  * **CẤM:** Không suy diễn rằng việc mở cổng 139/445 cho trạm Kali đồng nghĩa với việc máy chủ mở dịch vụ không kiểm soát ra toàn bộ mạng.
  * **CẤM:** Không kết luận máy chủ tồn tại lỗ hổng bảo mật chỉ từ việc có quy tắc cho phép kết nối cổng SMB.

---

## 4. Chính Sách Cắt Cúp Hình Ảnh Trình Bày (Image Derivation & Crop Policy)

Không chỉnh sửa byte của các tệp ảnh nguồn. Đối với bản in và báo cáo DOCX sau này, đề xuất các khung cắt cúp (Crop Rectangles) để loại bỏ không gian chết và tối ưu hóa độ phân giải:

### Đề xuất Cắt Cúp 1: Đối với `Windows_MS17010_01_SrvSysVersion.png` (Hình 3.1)
- **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png`
- **SHA-256 nguồn:** `2f8c1b7ce276919c72bb40a75fbeacdef81f2fa98695758df27f8772bdc149c8`
- **Kích thước gốc:** $1440 \times 900\,\text{px}$.
- **Vùng cắt đề xuất (Crop Box):**
  * Tọa độ: $X_1 = 0\,\text{px}, Y_1 = 0\,\text{px}, X_2 = 880\,\text{px}, Y_2 = 900\,\text{px}$ (Giữ trọn vẹn toàn bộ cửa sổ PowerShell từ thanh tiêu đề đến con trỏ lệnh cuối cùng).
  * Nội dung loại bỏ: Vùng màn hình desktop Server Manager trống bên phải (chiếm 40% diện tích không mang thông tin).
  * Ngữ cảnh bắt buộc bảo tồn: Tiêu đề cửa sổ PowerShell, toàn bộ dòng lệnh gọi `$env:SystemRoot...`, 2 dòng kết quả `FileVersion` / `ProductVersion`, dòng lệnh trích xuất 4 trường `$vi...`, kết quả số `6.3.9600.16421`.
- **Mục đích:** Tối đa hóa cỡ chữ khi chèn vào khổ giấy A4, giúp người chấm bài đọc rõ từng ký tự phiên bản mà không cần zoom.

### Đề xuất Cắt Cúp 2: Đối với `Windows_PreDemo_02_Firewall.png` (Hình 3.2)
- **Tệp nguồn:** `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png`
- **SHA-256 nguồn:** `c685573c3c1d00460d49d8718cc02a48ef8bceda26ce5cac1ab913e1db0d7077`
- **Kích thước gốc:** $1440 \times 900\,\text{px}$.
- **Vùng cắt đề xuất (Crop Box):**
  * Tọa độ: $X_1 = 40\,\text{px}, Y_1 = 60\,\text{px}, X_2 = 980\,\text{px}, Y_2 = 860\,\text{px}$ (Bao bọc trọn vẹn cửa sổ PowerShell hiển thị 5 khối lệnh kiểm toán tường lửa).
  * Nội dung loại bỏ: Thanh taskbar Windows Server và phần nền Server Manager mờ phía sau.
  * Ngữ cảnh bắt buộc bảo tồn: Tên quy tắc `ATTT Lab SMB 139-445`, cổng `{139, 445}`, địa chỉ nguồn `192.168.56.10`, trạng thái 3 profile `True`, số lượng luật chia sẻ tệp mặc định `False: 16`.
- **Mục đích:** Trình bày tập trung vào dữ liệu an ninh mạng, loại bỏ chi tiết giao diện thừa.

---

## 5. Đoạn Chuyển Tiếp Ý Niệm Sang Mục 3.2 (Conceptual Transition to Section 3.2)

- **Bản chất chuyển tiếp:**  
  Sau khi toàn bộ tham số môi trường mạng, dịch vụ SMB, chính sách tường lửa kiểm soát phạm vi và trạng thái bản vá cục bộ của máy chủ (`UNPATCHED` đối với MS17-010) đã được kiểm toán và ghi nhận độc lập tại mốc chuẩn xuất phát, hệ thống lab được bảo tồn tại điểm phục hồi `Before Demo`.  
  Tiếp theo, trạm kiểm thử Kali Linux bắt đầu tiến trình thực nghiệm Kịch bản 1 nhằm rà quét, phát hiện và định danh dịch vụ SMB từ góc nhìn mạng bên ngoài mà không cần bỏ qua kiểm tra trực tuyến (`không dùng cờ -Pn`), qua đó thiết lập bức tranh thực tế về khả năng tiếp cận dịch vụ trước khi kiểm định dấu hiệu lỗ hổng an ninh chuyên sâu.
