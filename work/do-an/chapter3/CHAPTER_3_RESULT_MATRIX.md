# MA TRẬN KẾT QUẢ THỰC NGHIỆM CHƯƠNG 3 (CHAPTER 3 RESULT MATRIX)

- **Trạng thái:** `FACTUAL_DATA_LOCKED`
- **Mục đích:** Khóa toàn bộ các quan sát thực nghiệm, nguồn dữ liệu gốc, diễn giải được phép và diễn giải bị cấm theo từng pha đo đạc.
- **Ràng buộc:** Đây là ma trận sự thật kỹ thuật nội bộ, KHÔNG PHẢI VĂN BẢN XUÔI (ZERO PROSE). Toàn bộ nội dung Chương 3 sau này phải bám sát tuyệt đối các hàng trong ma trận này.

---

## 1. Mốc Chuẩn Xuất Phát (Baseline State)

| STT | Tham số / Mục tiêu đo đạc | Quan sát thực nghiệm thực tế | Tệp bằng chứng nguồn | Diễn giải kỹ thuật được phép | Diễn giải bị nghiêm cấm |
|---|---|---|---|---|---|
| B01 | Địa chỉ IP máy kiểm thử Kali | `192.168.56.10/24`, không có default gateway | `Final_PreDemo_Audit.txt` | Trạm kiểm thử nằm trong phân đoạn mạng Host-Only, cô lập với Internet | Không suy diễn Kali có kết nối mạng ra bên ngoài trong suốt quá trình chạy kịch bản |
| B02 | Địa chỉ IP máy chủ mục tiêu | `192.168.56.20/24`, không có default gateway | `Final_PreDemo_Audit.txt` | Máy chủ mục tiêu nằm cùng phân đoạn mạng Host-Only với trạm kiểm thử | Không suy diễn máy chủ có kết nối định tuyến tới các mạng khác |
| B03 | Trạng thái mạng liên thông | Lệnh ping hai chiều thành công, độ trễ $<1\,\text{ms}$, không mất gói | `Final_PreDemo_Audit.txt`, `Kali_to_Windows_Connectivity.png` | Liên kết mạng cơ bản giữa Kali và Windows hoạt động thông suốt | Không suy diễn toàn bộ các cổng TCP/UDP đều mở mặc định |
| B04 | Trạng thái dịch vụ LanmanServer | Dịch vụ `LanmanServer` ở trạng thái `Running`, khởi động `Automatic` | `Final_PreDemo_Audit.txt`, `Windows_Baseline_04_SMB_Service.png` | Dịch vụ chia sẻ tệp Server Message Block đang hoạt động trên hệ điều hành mục tiêu | Không suy diễn dịch vụ đã sẵn sàng cho mọi giao thức nếu chưa kiểm tra registry |
| B05 | Trạng thái lắng nghe cổng cục bộ | Cổng TCP 139 và TCP 445 hiển thị trạng thái `LISTENING` trong `netstat` | `Final_PreDemo_Audit.txt` | Tiến trình hệ thống đang lắng nghe yêu cầu kết nối trên cả hai cổng SMB | **CẤM:** Cổng lắng nghe cục bộ không đồng nghĩa với đã mở qua tường lửa hoặc có lỗ hổng |
| B06 | Kích hoạt giao thức SMBv1 | `Get-SmbServerConfiguration`: `EnableSMB1Protocol : True`, `FS-SMB1` Installed | `Final_PreDemo_Audit.txt`, `Windows_Baseline_05_SMB_Features.png` | Máy chủ cho phép đàm phán phương ngữ SMBv1 | **CẤM:** SMBv1 được bật không đồng nghĩa với đã xác nhận tồn tại lỗ hổng MS17-010 |
| B07 | Kích hoạt giao thức SMBv2/v3 | `Get-SmbServerConfiguration`: `EnableSMB2Protocol : True` | `Final_PreDemo_Audit.txt`, `Windows_Baseline_06_SMB_Config.png` | Cấu hình máy chủ hỗ trợ các phiên bản SMB thế hệ mới | Không suy diễn đã kiểm chứng tải ứng dụng thực tế |
| B08 | Quy tắc tường lửa Windows | Tường lửa bật; Rule tùy biến mở TCP 139/445 với Remote IP: `192.168.56.10` | `Windows_FirewallPrep_Final.txt`, `Windows_FirewallPrep_04_Scope.png` | Cổng SMB được bảo vệ bởi phạm vi IP nguồn; chỉ chấp nhận gói tin từ trạm Kali | Không suy diễn tường lửa máy chủ có khả năng kiểm soát sâu nội dung gói tin |
| B09 | Trạng thái bản vá hệ thống | `srv.sys` FileVersion String `6.3.9600.16384` (phiên bản số `6.3.9600.16421`), thiếu KB4012213 hoặc KB4012216, thấp hơn ngưỡng tối thiểu `6.3.9600.18604` | `MS17-010_Official_Mapping.txt`, `Windows_MS17010_01_SrvSysVersion.png` | Trạng thái bản vá cục bộ của máy chủ mục tiêu là **UNPATCHED** dựa trên phiên bản số nội bộ, danh mục hotfix và bảng ánh xạ chính thức | Không suy diễn riêng ảnh chụp thuộc tính tệp đủ chứng minh UNPATCHED; kết luận phải dựa trên phiên bản số nội bộ + danh mục hotfix + bảng ánh xạ chính thức |
| B10 | Điểm hoàn nguyên hệ thống | Snapshot `Before Demo` đã chụp trên cả hai máy ảo sau khi hoàn tất audit | `Before_Demo_Snapshots.txt` | Thiết lập mốc chuẩn cố định cho toàn bộ chuỗi thực nghiệm | Không coi snapshot là bằng chứng về việc đã rollback trong các lần chạy |

---

## 2. Kịch bản 1 — Khảo sát Dịch vụ SMB (Scenario 1)

| STT | Bước thực thi | Quan sát thực nghiệm thực tế | Tệp bằng chứng nguồn | Diễn giải kỹ thuật được phép | Diễn giải bị nghiêm cấm |
|---|---|---|---|---|---|
| S1-01 | B2 — Khám phá mạng subnet | 4 địa chỉ IP trả lời: `.56.1` (VirtualBox Host-Only host adapter), `.56.10` (Kali), `.56.20` (Windows), `.56.100` (UNKNOWN identity) | `b2_host_discovery.nmap` | Dải mạng lab phản hồi kết nối, máy chủ mục tiêu `.56.20` hiện diện | **NGHIÊM CẤM:** Tuyệt đối không gán bất kỳ định danh cụ thể nào cho host `.56.100`. Host `.56.100` bắt buộc duy trì nhãn UNKNOWN identity |
| S1-02 | B3 — Kiểm tra mục tiêu trực tuyến | `Host is up (0.00040s latency)` | `b3_target_alive.nmap` | Mục tiêu phản hồi tín hiệu thăm dò trước khi tiến hành quét cổng | Không suy diễn trạng thái mở cổng từ phản hồi trực tuyến |
| S1-03 | B4 — Quét cổng dịch vụ SMB | Cổng 139/tcp và 445/tcp mở (`open`), phản hồi SYN-ACK với TTL=128 | `b4_smb_ports.nmap`, `Scenario1_B4_SMB_Ports.png` | Cổng SMB truyền thống và Direct-hosted mở, tiếp nhận kết nối TCP từ trạm Kali | **CẤM:** Cổng 445 mở không đồng nghĩa với hệ thống có lỗ hổng bảo mật (445 open != vulnerable) |
| S1-04 | B5 — Nhận diện phiên bản dịch vụ | 139: `Windows netbios-ssn`; 445: `Windows Server 2008 R2 - 2012 microsoft-ds` | `b5_smb_version.nmap`, `Scenario1_B5_SMB_Version.png` | Nhận diện dịch vụ SMB trên hệ điều hành họ Windows Server | Không suy diễn chính xác phiên bản 2012 R2 chỉ từ fingerprint nếu dải là 2008 R2–2012 |
| S1-05 | B6 — Thăm dò phương ngữ và signing | `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`; signing `enabled but not required` | `b6_smb_nse.nmap`, `Scenario1_B6_SMB_NSE_A.png` | Máy chủ hỗ trợ cả SMBv1 và SMBv2/v3; quan sát từ xa cho thấy chính sách ký số là enabled but not required | **CẤM:** Hỗ trợ SMBv1 không đồng nghĩa với đã xác nhận lỗ hổng MS17-010 (SMBv1 enabled != MS17-010 confirmed) |
| S1-06 | B6 — Script nhận diện hệ điều hành | `smb-os-discovery`: hoàn toàn không xuất hiện trong output | `b6_smb_nse.nmap` | Script không trích xuất được thông tin hệ điều hành từ phản hồi SMB | Không tự suy đoán nguyên nhân không có output nếu thiếu dữ liệu log gói tin thô |

---

## 3. Kịch bản 2 — Kiểm tra Dấu hiệu Lỗ hổng MS17-010 (Scenario 2)

| STT | Bước thực thi | Quan sát thực nghiệm thực tế | Tệp bằng chứng nguồn | Diễn giải kỹ thuật được phép | Diễn giải bị nghiêm cấm |
|---|---|---|---|---|---|
| S2-01 | NSE-SMB-01 — Kiểm tra cổng | Cổng 139/tcp và 445/tcp mở (`open`) | `NSE-SMB-01_ports.nmap`, `Scenario2_NSE01_Ports.png` | Xác nhận tính sẵn sàng của cổng dịch vụ trước khi thực thi chuỗi script NSE | Không suy diễn khả năng khai thác hay mức độ an toàn |
| S2-02 | NSE-SMB-02 — Kiểm tra giao thức | Liệt kê đầy đủ 5 phương ngữ từ `NT LM 0.12` đến `3.0.2` | `NSE-SMB-02_protocols.nmap`, `Scenario2_NSE02_Protocols.png` | Ngăn xếp máy chủ sẵn sàng đàm phán phương ngữ SMBv1 cũ cùng các phương ngữ SMB2/3 | Không kết luận máy chủ dễ bị tấn công hay đã khai thác thành công |
| S2-03 | NSE-SMB-03 — Kiểm tra signing | `Message signing enabled but not required` | `NSE-SMB-03_signing.nmap`, `Scenario2_NSE03_Signing.png` | Ghi nhận quan sát từ xa của Nmap về chính sách ký số SMB | **NGHIÊM CẤM:** Không suy diễn signing là điều kiện tiên quyết cho việc thăm dò/khai thác MS17-010; không tuyên bố nó thỏa mãn điều kiện tiếp nhận payload khai thác |
| S2-04 | NSE-SMB-04 — Script kiểm tra MS17-010 | Cổng 445/tcp `open`; không có mục `Host script results:`; không có phán quyết | `NSE-SMB-04_ms17010.nmap`, `Scenario2_NSE04_MS17010.png` | Phán quyết thăm dò từ xa là **UNKNOWN / NO USABLE SCRIPT RESULT** | **CẤM TUYỆT ĐỐI:** Không được suy diễn UNKNOWN thành SAFE (UNKNOWN != SAFE); không tái sử dụng kết quả lịch sử cũ |
| S2-05 | Đối chiếu chéo từ xa vs. cục bộ | Từ xa: UNKNOWN; Cục bộ: `srv.sys` unpatched, thiếu hotfix KB4012213 hoặc KB4012216 | Đối chiếu chéo `NSE-SMB-04` và `MS17-010_Official_Mapping.txt` | Minh chứng thực nghiệm khẳng định sự độc lập giữa tín hiệu quét từ xa và trạng thái bản vá nội tại | Không quy kết script quét từ xa phản ánh tuyệt đối trạng thái bản vá của hệ thống |

---

## 4. Biện pháp Giảm thiểu Case B — Vô hiệu hóa SMBv1 (Case B)

| STT | Bước thực thi | Quan sát thực nghiệm thực tế | Tệp bằng chứng nguồn | Diễn giải kỹ thuật được phép | Diễn giải bị nghiêm cấm |
|---|---|---|---|---|---|
| CB-01 | Kiểm tra trạng thái trước can thiệp | `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`, `LanmanServer` Running | `SMBv1_Remediation_01_Before.png` | Điểm xuất phát cục bộ của Case B: SMBv1 đang hoạt động | Không suy đoán ngoài thuộc tính registry hiển thị |
| CB-02 | Thực thi vô hiệu hóa | `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` | `SMBv1_Remediation_02_Action.png` | Câu lệnh can thiệp cấu hình đã được thực thi; trạng thái sau can thiệp xác nhận cấu hình mong muốn | Không suy diễn máy chủ đã được vá bản cập nhật hệ điều hành |
| CB-03 | Kiểm tra trạng thái sau can thiệp | `EnableSMB1Protocol : False`, `EnableSMB2Protocol : True`, `LanmanServer` Running | `SMBv1_Remediation_03_After_Local.png` | SMBv1 đã tắt ở mức cấu hình máy chủ; dịch vụ LanmanServer tiếp tục hoạt động | **CẤM:** Tắt SMBv1 không đồng nghĩa với PATCHED (srv.sys vẫn chưa vá); không tuyên bố dịch vụ chia sẻ tệp hiện đại đã được kiểm chứng toàn diện hay chứng minh không có gián đoạn |
| CB-04 | Đo đạc lại phương ngữ từ xa | Phương ngữ `NT LM 0.12` vắng mặt; chỉ còn `2.0.2`, `2.1`, `3.0`, `3.0.2` | `case_b/NSE-SMB-02_protocols.nmap`, `SMBv1_Remediation_04_NSE02_Protocols.png` | Phương ngữ SMBv1 không còn xuất hiện trong phản hồi đàm phán; các phương ngữ SMB2/SMB3 vẫn quan sát được từ trạm quét | Không suy diễn cổng 445 đã đóng; không tuyên bố đã kiểm chứng tải ứng dụng nghiệp vụ |
| CB-05 | Đo đạc lại script MS17-010 | Cổng 445/tcp tiếp tục mở (`open`); không xuất hiện Host script results | `case_b/NSE-SMB-04_ms17010.nmap`, `SMBv1_Remediation_05_NSE04_MS17010.png` | Phán quyết từ xa vẫn là UNKNOWN / NO USABLE SCRIPT RESULT do không có dữ liệu script | Không suy diễn script xác nhận an toàn; trạng thái bản vá nội bộ vẫn là UNPATCHED |
| CB-06 | Đối soát trạng thái bản vá Case B | `srv.sys` vẫn giữ nguyên phiên bản cũ `6.3.9600.16384` | Đối chiếu chéo cục bộ | Trạng thái bản vá của hệ thống vẫn là **UNPATCHED**; việc tắt SMBv1 không thay đổi mã nhị phân driver nhân | Không đánh đồng việc vô hiệu hóa cấu hình với việc cập nhật bản vá hệ điều hành |

---

## 5. Biện pháp Giảm thiểu Case C — Tường lửa Cầu nối pfSense (Case C)

| STT | Bước thực thi | Quan sát thực nghiệm thực tế | Tệp bằng chứng nguồn | Diễn giải kỹ thuật được phép | Diễn giải bị nghiêm cấm |
|---|---|---|---|---|---|
| CC-01 | Gán cổng giao diện mạng | `CASE_C_KALI = em2`, `CASE_C_WINDOWS = em3` | `pfSense_03_Interface_Assignment.png` | Kali và Windows gắn vào hai phân đoạn mạng vật lý ảo độc lập trên pfSense | Không suy diễn định tuyến L3 thông thường |
| CC-02 | Thiết lập Transparent Bridge | Cầu nối `bridge0` chứa cả hai giao diện `em2` và `em3` | `pfSense_04_Bridge.png` | Lưu lượng giữa hai máy đi qua pfSense ở tầng liên kết dữ liệu | Không suy diễn bridge có IP gateway |
| CC-03 | Kích hoạt bộ lọc cầu nối | Tunables: `net.link.bridge.pfil_member = 1`, `pfil_bridge = 0` | `pfSense_05_Bridge_Filtering.png` | Bộ lọc packet filtering được kích hoạt trên từng giao diện thành viên | `pfil_onlyip = 1` ghi nhận từ metadata, không hiển thị trên ảnh trực tiếp |
| CC-04 | Cấu hình quy tắc chặn SMB | Action: `Block`, Interface: `CASE_C_KALI`, Port: `139, 445`, bật `Log` | `pfSense_07_Block_Rule_Config.png` | Định nghĩa quy tắc chặn lưu lượng SMB từ Kali đến Windows có ghi log | Không suy diễn quy tắc đã có hiệu lực nếu chưa xét thứ tự thực thi |
| CC-05 | Thứ tự thực thi quy tắc | Quy tắc Block SMB nằm trên quy tắc Baseline Pass | `pfSense_08_Rule_Order.png` | Quy tắc chặn được xử lý ưu tiên duyệt trước | Không suy đoán hành vi của các giao diện khác |
| CC-06 | Quét lại cổng từ xa | Cổng 139/tcp và 445/tcp ghi nhận trạng thái `filtered` do `no-response` | `case_c/NSE-SMB-01_ports.nmap`, `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | Từ góc nhìn trạm Kali qua đường dẫn Case C, Nmap không nhận đủ phản hồi để phân loại cổng là open hay closed | **NGHIÊM CẤM:** Không tự ý gán nguyên nhân tường lửa trong dòng quan sát quét thô này; FILTERED không đồng nghĩa với PATCHED; chỉ ghi nhận kết quả đo đạc khách quan và trạng thái UNPATCHED từ kiểm toán cục bộ |
| CC-07 | Quét lại script MS17-010 | Cổng 445/tcp tiếp tục `filtered` do `no-response`; script MS17-010 không thể thiết lập kết nối để gửi gói tin thăm dò | `case_c/NSE-SMB-04_ms17010.nmap`, `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | Cổng 445 không thể tiếp cận được từ góc nhìn trạm quét qua đường dẫn Case C; phán quyết từ xa vẫn là UNKNOWN/không tiếp cận được | **NGHIÊM CẤM:** Không tuyên bố bề mặt tấn công bị triệt tiêu vĩnh viễn; không tuyên bố script bị vô hiệu hóa; không kết luận máy chủ an toàn hay đưa ra nhận định vượt quá trạng thái UNPATCHED cục bộ |
| CC-08 | Nhật ký tường lửa chặn gói tin | Ảnh trực tiếp: Biểu tượng Block đỏ, Interface: `CASE_C_KALI`, Source: `.56.10`, Dest: `.56.20:139/445`, TCP SYN | `pfSense_10_Block_Log_CANONICAL.png` | Khẳng định thực nghiệm lưu lượng SMB TCP SYN từ Kali đã bị pfSense chặn trên đường truyền | **XUNG ĐỘT DANH PHÁP ĐÃ KHÓA:** Nhãn hiển thị trên ảnh là `CASE C baseline pass... (100000104)`. Ghi nhận sự kiện lưu lượng bị chặn, CẤM quy thuộc đích danh rule ID |
| CC-09 | Đối soát trạng thái máy chủ Case C | Máy chủ mục tiêu phía sau tường lửa vẫn giữ nguyên `srv.sys` cũ, thiếu bản vá và `SMB1=True` | Đối chiếu chéo mốc chuẩn xuất phát | Giải pháp tường lửa ngăn chặn lưu lượng mạng trên đường truyền; trạng thái bản vá nội bộ của máy chủ vẫn là UNPATCHED | Không tuyên bố giải pháp tường lửa đã thay đổi cấu trúc phần mềm máy chủ; chỉ ghi nhận trạng thái bản vá cục bộ chưa được cập nhật (UNPATCHED) |

---

## 6. Bảng Tổng Hợp So Sánh Đa Chiều Các Trạng Thái

| Tiêu chí kỹ thuật | Mốc chuẩn xuất phát (Baseline) | Kịch bản 1 / 2 (Khảo sát/Kiểm định) | Biện pháp Case B (Tắt SMBv1) | Biện pháp Case C (Tường lửa pfSense) |
|---|---|---|---|---|
| **Trạng thái cổng TCP 139/445** | `LISTENING` (Cục bộ) | `OPEN` (Trạm quét) | `OPEN` (Trạm quét) | `FILTERED` (Trạm quét, no-response) |
| **Phương ngữ SMBv1 (`NT LM 0.12`)** | `Kích hoạt` (Registry) | `Phát hiện` (Đàm phán) | `Vắng mặt` (Không phản hồi đàm phán) | `Không tiếp cận được` (Cổng filtered) |
| **Phương ngữ SMBv2/SMBv3** | `Kích hoạt` (Registry) | `Phát hiện` (Đàm phán) | `Vẫn quan sát được` (Đàm phán thành công) | `Không tiếp cận được` (Cổng filtered) |
| **Phán quyết NSE MS17-010** | Không áp dụng | `UNKNOWN / NO USABLE RESULT` | `UNKNOWN / NO USABLE RESULT` | `UNKNOWN / Không tiếp cận được` |
| **Trạng thái bản vá hệ thống** | `UNPATCHED` (srv.sys cũ) | `UNPATCHED` (srv.sys cũ) | `UNPATCHED` (srv.sys cũ) | `UNPATCHED` (srv.sys cũ) |
| **Khả năng tiếp cận cổng dịch vụ qua mạng** | Mở có kiểm soát (Windows Firewall) | Tiếp cận được từ Kali | Tiếp cận được từ Kali | **Không nhận được phản hồi** (Filtered) |
| **Khả năng đàm phán SMBv1 từ trạm quét** | Sẵn sàng đàm phán | Đàm phán thành công | **Không đàm phán được** | Không tiếp cận được cổng |
| **Rủi ro phụ thuộc bản vá hệ thống** | Phụ thuộc cao (chưa vá) | Phụ thuộc cao (chưa vá) | Phụ thuộc cao (chưa vá) | Phụ thuộc cao (chưa vá) |
