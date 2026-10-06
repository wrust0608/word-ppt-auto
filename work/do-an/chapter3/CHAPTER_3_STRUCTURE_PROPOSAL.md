# ĐỀ XUẤT CẤU TRÚC CHƯƠNG 3 (CHAPTER 3 STRUCTURE PROPOSAL)

- **Trạng thái:** `PROPOSAL_LOCKED_FOR_EXTERNAL_REVIEW`
- **Ràng buộc:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI (ZERO PROSE)**. Tài liệu này chỉ đề xuất khung cấu trúc, ánh xạ 1:1 với phương pháp đã thiết kế tại Chương 2, xác định bộ bằng chứng và phân định ranh giới chặt chẽ với Chương 4.

---

## 1. Khung Tiêu Đề Đề Xuất (7 Mục H2)

# CHƯƠNG 3. KẾT QUẢ THỰC NGHIỆM VÀ PHÂN TÍCH

- **3.1. Trạng thái baseline trước đo đạc**
- **3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB**
- **3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010**
- **3.4. Kết quả Case B — Vô hiệu hóa SMBv1**
- **3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense**
- **3.6. So sánh kết quả thực nghiệm**
- **3.7. Tổng kết chương**

---

## 2. Chi Tiết Từng Đề Mục H2

### Mục 3.1. Trạng thái baseline trước đo đạc
- **Mục đích:** Công bố số liệu kiểm toán hiện trạng của môi trường lab tại thời điểm xuất phát; xác lập mốc chuẩn khách quan về cấu hình mạng, dịch vụ chia sẻ tệp, chính sách tường lửa máy chủ và trạng thái bản vá hệ thống trước khi tiến hành các lượt quét thăm dò.
- **Bộ bằng chứng (Evidence Set):**
  - Tệp kiểm toán văn bản: `Final_PreDemo_Audit.txt`, `MS17-010_Official_Mapping.txt`, `Windows_FirewallPrep_Final.txt`, `VirtualBox_HostOnly_Config.txt`, `Before_Demo_Snapshots.txt`.
  - Ảnh kiểm chứng thị giác: `Windows_MS17010_01_SrvSysVersion.png`, `Windows_FirewallPrep_04_Scope.png`, `Windows_Baseline_01_Winver.png`.
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.1:** Bảng tổng hợp thông số kiểm toán mốc chuẩn xuất phát trước thực nghiệm (đầy đủ các trường: IP, Routing, Service, Registry, Firewall Scope, Driver File Version).
  - **Hình 3.1:** Phiên bản hiển thị của tệp srv.sys trên máy Windows Server 2012 R2 trước thực nghiệm.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Số liệu đo đạc cấu hình thực tế, trạng thái bản vá cục bộ (UNPATCHED đối với MS17-010 dựa trên phiên bản số `6.3.9600.16421` thấp hơn ngưỡng tối thiểu `6.3.9600.18604` theo tài liệu KB4012213 / KB4012216 của Microsoft).
  - *Thuộc Chương 4:* Đánh giá rủi ro hệ thống từ việc tồn tại các máy chủ chưa cập nhật bản vá trong hạ tầng doanh nghiệp; chính sách quản lý bản vá (Patch Management Lifecycle).

---

### Mục 3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB
- **Mục đích:** Báo cáo chi tiết kết quả thực nghiệm quy trình rà quét (từ phát hiện mạng, kiểm tra trực tuyến, quét cổng đến nhận diện dịch vụ và phương ngữ SMB) bằng công cụ Nmap trên trạm kiểm thử Kali Linux.
- **Bộ bằng chứng (Evidence Set):**
  - Dữ liệu thô Nmap (Raw Triplets): `b2_host_discovery.{nmap,xml,gnmap}`, `b3_target_alive.{nmap,xml,gnmap}`, `b4_smb_ports.{nmap,xml,gnmap}`, `b5_smb_version.{nmap,xml,gnmap}`, `b6_smb_nse.{nmap,xml,gnmap}`.
  - Ảnh chụp màn hình: `Scenario1_B4_SMB_Ports.png`, `Scenario1_B5_SMB_Version.png`, `Scenario1_B6_SMB_NSE_A.png`.
  - Dòng lệnh thao tác: `Scenario1_Run_Manifest.txt` (khẳng định không dùng cờ `-Pn`).
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.2:** Bảng kết quả rà quét nhận diện dịch vụ và phương ngữ SMB tại Kịch bản 1 (tổng hợp 5 bước B2 đến B6: cổng, trạng thái, thời gian trễ, tên dịch vụ, danh sách dialect, signing; ghi nhận `.56.100` mang nhãn UNKNOWN identity).
  - **Hình 3.2:** Kết quả quét cổng dịch vụ SMB tại Kịch bản 1 xác nhận cổng 139 và 445 ở trạng thái mở.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Dữ liệu thô về trạng thái cổng mở (139/tcp, 445/tcp), các phương ngữ SMB được hệ thống trả về, việc script OS discovery không sinh output.
  - *Thuộc Chương 4:* Phân tích nguy cơ rò rỉ thông tin hạ tầng mạng (Information Disclosure) từ kết quả quét phiên bản và phương ngữ SMB; khuyến nghị cấu hình ẩn thông tin dịch vụ.

---

### Mục 3.3. Kết quả Kịch bản 2 — Kiểm tra dấu hiệu MS17-010
- **Mục đích:** Công bố kết quả đo đạc từ chuỗi 4 kịch bản NSE chuyên sâu; phân tích bản chất phán quyết UNKNOWN từ xa và đối chiếu chéo với trạng thái UNPATCHED cục bộ của máy chủ.
- **Bộ bằng chứng (Evidence Set):**
  - Dữ liệu thô Nmap (Raw Triplets): `NSE-SMB-01_ports.{nmap,xml,gnmap}`, `NSE-SMB-02_protocols.{nmap,xml,gnmap}`, `NSE-SMB-03_signing.{nmap,xml,gnmap}`, `NSE-SMB-04_ms17010.{nmap,xml,gnmap}`.
  - Ảnh chụp màn hình: `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png`, `Scenario2_NSE04_MS17010.png`.
  - Metadata: `Scenario2_Run_Manifest.txt`.
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.3:** Bảng kết quả chuỗi kịch bản kiểm định lỗ hổng an ninh MS17-010 tại Kịch bản 2 (chi tiết từng script: trạng thái cổng, phương ngữ đàm phán, thuộc tính SMB signing quan sát từ xa `Message signing enabled but not required` không quy kết thành điều kiện tiên quyết khai thác, phán quyết script MS17-010 UNKNOWN / NO USABLE SCRIPT RESULT).
  - **Hình 3.3:** Kết quả script smb-protocols trong Kịch bản 2 xác nhận máy chủ hỗ trợ phương ngữ SMBv1.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Dữ liệu đo đạc thực tế rằng script MS17-010 không sinh phán quyết (UNKNOWN / No usable output); sự độc lập giữa tín hiệu thăm dò từ xa và trạng thái bản vá máy chủ.
  - *Thuộc Chương 4:* Phân tích giới hạn của kỹ thuật quét black-box không xâm nhập; nguy cơ diễn giải sai một kết quả `UNKNOWN`; cơ chế khai thác bộ nhớ nhân hệ điều hành của EternalBlue chỉ ở mức lý thuyết/học thuật.

---

### Mục 3.4. Kết quả Case B — Vô hiệu hóa SMBv1
- **Mục đích:** Trình bày kết quả thực nghiệm can thiệp cấu hình hệ thống bằng cách tắt giao thức SMBv1; cung cấp số liệu đo đạc đối chứng trước và sau can thiệp ở cả góc nhìn máy chủ cục bộ và góc nhìn mạng từ xa.
- **Bộ bằng chứng (Evidence Set):**
  - Dữ liệu cục bộ: `SMBv1_Remediation_01_Before.png`, `SMBv1_Remediation_02_Action.png`, `SMBv1_Remediation_03_After_Local.png`.
  - Dữ liệu thô đo đạc lại (Retest Raw Triplets): `case_b/NSE-SMB-02_protocols.{nmap,xml,gnmap}`, `case_b/NSE-SMB-04_ms17010.{nmap,xml,gnmap}`.
  - Ảnh chụp kết quả quét lại: `SMBv1_Remediation_04_NSE02_Protocols.png`, `SMBv1_Remediation_05_NSE04_MS17010.png`.
  - Metadata: `SMBv1_Remediation_Run_Manifest.txt`.
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.4:** Bảng đo đạc đối chứng kết quả trước và sau khi vô hiệu hóa SMBv1 (Case B: phương ngữ SMBv1 vắng mặt, các dialect SMB2/SMB3 vẫn quan sát được, cổng 445 vẫn mở, trạng thái bản vá cục bộ giữ nguyên UNPATCHED).
  - **Hình 3.4:** Thao tác thực thi lệnh vô hiệu hóa giao thức SMBv1 và kết quả xác nhận cấu hình cục bộ tại Case B.
  - **Hình 3.5:** Kết quả quét lại từ xa xác nhận phương ngữ SMBv1 không còn xuất hiện trong danh sách đàm phán sau can thiệp Case B.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Xác nhận thực nghiệm phương ngữ SMBv1 vắng mặt khỏi danh sách đàm phán từ xa, các phương ngữ SMB2/SMB3 vẫn quan sát được, cổng 445 vẫn mở, trạng thái driver `srv.sys` cục bộ chưa cập nhật bản vá (UNPATCHED).
  - *Thuộc Chương 4:* Đánh giá khả năng tương thích của các ứng dụng kế thừa (Legacy Compatibility); rủi ro tồn lưu khi quản trị viên kích hoạt lại SMBv1; chiến lược dừng sử dụng SMBv1 trong hạ tầng doanh nghiệp.

---

### Mục 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense
- **Mục đích:** Báo cáo kết quả thực nghiệm triển khai tường lửa cầu nối pfSense; chứng minh sự thay đổi trạng thái cổng mạng từ OPEN sang FILTERED (no-response) và hành vi chặn gói tin TCP SYN thăm dò trên nhật ký tường lửa.
- **Bộ bằng chứng (Evidence Set):**
  - Cấu hình tường lửa: `pfSense_03_Interface_Assignment.png`, `pfSense_04_Bridge.png`, `pfSense_05_Bridge_Filtering.png`, `pfSense_07_Block_Rule_Config.png`, `pfSense_08_Rule_Order.png`.
  - Dữ liệu thô đo đạc lại: `case_c/NSE-SMB-01_ports.{nmap,xml,gnmap}`, `case_c/NSE-SMB-04_ms17010.{nmap,xml,gnmap}`.
  - Ảnh chụp cổng và nhật ký: `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`, `pfSense_10_Block_Log_CANONICAL.png`, `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png`.
  - Metadata: `pfSense_Remediation_Run_Manifest.txt`, `RUN4_PAUSE_STATE_REPORT.txt`.
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.5:** Bảng đo đạc đối chứng kết quả kiểm soát lưu lượng qua tường lửa pfSense (Case C: cổng 139 và 445 chuyển sang filtered do no-response, nhật ký ghi nhận các gói TCP SYN bị Block, trạng thái bản vá cục bộ của máy chủ giữ nguyên UNPATCHED).
  - **Hình 3.6:** Thứ tự thực thi quy tắc tường lửa pfSense ưu tiên chặn lưu lượng SMB trước quy tắc cho phép.
  - **Hình 3.7:** Kết quả quét cổng SMB ghi nhận trạng thái filtered sau khi triển khai pfSense.
  - **Hình 3.8:** Nhật ký tường lửa pfSense ghi nhận việc chặn các gói tin TCP SYN thăm dò cổng dịch vụ SMB *(Kèm lưu ý bảo lưu: tồn tại sự không đồng nhất về nhãn quy tắc giữa số hiệu 100000104 và vị trí rule 2 trên giao diện, không tự quy thuộc nhãn rule)*.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Báo cáo kết quả đo đạc Nmap ghi nhận cổng 139/445 ở trạng thái filtered (no-response), nhật ký pfSense ghi nhận lưu lượng SYN tương ứng bị chặn, trạng thái máy chủ phía sau giữ nguyên cấu hình SMB và trạng thái bản vá UNPATCHED.
  - *Thuộc Chương 4:* Đánh giá tính khả thi và chi phí vận hành giải pháp Transparent Bridge trong môi trường mạng nội bộ; nguy cơ đứt gãy dịch vụ chia sẻ tệp; giải pháp phòng thủ theo chiều sâu (Defense-in-Depth).

---

### Mục 3.6. So sánh kết quả thực nghiệm
- **Mục đích:** Xây dựng ma trận so sánh tổng hợp giữa trạng thái mốc chuẩn ban đầu và hai biện pháp Case B, Case C; làm rõ các thay đổi quan sát được dựa trên dữ liệu đã đo.
- **Bộ bằng chứng (Evidence Set):**
  - Tổng hợp dữ liệu đối chiếu chéo từ 83 tệp bằng chứng thực nghiệm của các mục 3.1 đến 3.5.
- **Kế hoạch Bảng/Hình:**
  - **Bảng 3.6:** Bảng ma trận so sánh tổng hợp hiệu quả của các biện pháp phòng thủ (so sánh Baseline, Case B, Case C trên các tiêu chí kỹ thuật: Trạng thái cổng dịch vụ 139 và 445, Khả năng đàm phán phương ngữ SMBv1, Khả năng đàm phán phương ngữ SMB2/SMB3, Trạng thái phản hồi gói tin mạng, và Trạng thái bản vá cục bộ).
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Bảng so sánh khách quan dựa trên sự thật thực nghiệm đo được (cổng, phương ngữ, phản hồi mạng, trạng thái bản vá).
  - *Thuộc Chương 4:* Khuyến nghị mô hình kiến trúc an ninh phù hợp; phân tích chi phí - hiệu quả giữa cập nhật bản vá, cấu hình dịch vụ máy chủ và kiểm soát lưu lượng mạng.

---

### Mục 3.7. Tổng kết chương
- **Mục đích:** Tóm lược các kết quả thực nghiệm cốt lõi đã trình bày và chuyển sang phần đánh giá, rủi ro và khuyến nghị tại Chương 4.
- **Bộ bằng chứng (Evidence Set):**
  - Không bổ sung dữ liệu mới; tổng kết trên cơ sở các phát hiện chính đã được chứng minh tại các mục 3.1 đến 3.6.
- **Kế hoạch Bảng/Hình:**
  - Không sử dụng bảng biểu hay hình ảnh mới; tóm lược bằng các tiêu điểm kết quả ngắn gọn.
- **Ranh giới với Chương 4 (Boundary with Ch4):**
  - *Thuộc Chương 3:* Khép lại phần báo cáo kết quả đo đạc thực nghiệm.
  - *Thuộc Chương 4:* Mở ra không gian thảo luận về quản trị an toàn thông tin, phân tích nguyên nhân gốc rễ và đề xuất giải pháp tổng thể cho hệ thống công nghệ thông tin.
