# BẢNG TỔNG MỤC HÌNH ẢNH VÀ BẢNG BIỂU CHƯƠNG 3 (CH3 REDESIGN TABLE & FIGURE LEDGER R1)

- **Cổng trạng thái đề xuất:** `PROPOSED / WAITING EXTERNAL REVIEW` (Chưa khóa chính thức; tuyệt đối không gắn nhãn `LOCKED`).
- **Tài liệu căn cứ lộ trình:** `work/do-an/ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md`
- **Tài liệu kiến trúc cơ sở:** `work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md`
- **Nhánh làm việc canonical:** `feature/ch3-redesign-evidence-first-r1`
- **Commit khởi tạo:** `170aa24293b2cf8e579abb1ecf60920bca418bd9`
- **Mục tiêu tài liệu:** Thiết lập sổ đăng ký hai chiều (Two-Way Ledger) quản lý hệ thống bảng biểu và hình ảnh đề xuất cho 8 đề mục Chương 3 mới (3.1 đến 3.8); bảo đảm không làm thất thoát bất kỳ bằng chứng cũ nào, phân bổ vai trò rõ ràng, ghi nhận chính xác tệp nguồn canonical, luận điểm chứng minh và ranh giới kỹ thuật.

---

## 1. NGUYÊN TẮC ĐỊNH DANH VÀ KHÓA SỐ HIỆU (NUMBERING RULES)

1. **Trạng thái đề xuất (Proposed State):** Toàn bộ số hiệu bảng (Bảng 3.1 đến Bảng 3.7) và số hiệu hình (Hình 3.1 đến Hình 3.14) trong tài liệu này mang trạng thái `PROPOSED / WAITING EXTERNAL REVIEW`. Chỉ sau khi vượt qua vòng thẩm định độc lập của ChatGPT Reviewer và có phê duyệt rõ ràng từ người dùng, số hiệu mới được chuyển sang trạng thái khóa chính thức (`LOCKED_NUMBERING`).
2. **Quy tắc tiêu thụ bộ đếm:**
   - Bộ đếm bảng biểu đề xuất: 7 bảng (Bảng 3.1 đến Bảng 3.7).
   - Bộ đếm hình ảnh đề xuất: 14 hình (Hình 3.1 đến Hình 3.14).
   - Các hình ảnh thuộc kho bổ trợ (Supporting Visual) hoặc đã loại bỏ khỏi luồng chính (Retire) không tiêu thụ số hiệu hiển thị trong bản thảo văn bản.
3. **Phân loại hành động (Standard Action Tags):**
   - `KEEP`: Giữ nguyên hình ảnh/bảng biểu đơn lẻ từ cấu trúc cũ, chỉ cập nhật đề mục và ngữ cảnh dẫn dắt.
   - `MOVE`: Chuyển vị trí bảng biểu/hình ảnh sang đề mục mới tương ứng trong cấu trúc 8 phần.
   - `MERGE`: Ghép nhiều ảnh bằng chứng thành một hình đa panel (Before/After, Multi-angle, hoặc Sequential Action) để tăng sức thuyết phục và chống phân mảnh thị giác.
   - `RETIRE`: Loại bỏ khỏi luồng đọc chính của bản thảo do nội dung trùng lặp hoặc đã được bao hàm trọn vẹn bởi bằng chứng khác sắc nét hơn (vẫn lưu giữ nguyên vẹn tệp trong repository).
   - `NEW`: Xây dựng sơ đồ giải thích mới (Explanatory Figure) hoặc bảng tổng hợp mới từ dữ kiện đã xác minh.

---

## 2. SỔ ĐĂNG KÝ HỆ THỐNG BẢNG BIỂU ĐỀ XUẤT (PROPOSED TABLE LEDGER)

| Proposed No. | New Section | Type | Role | Source canonical | Old No. | Action | Caption dự kiến | Supported claim (Luận điểm chứng minh) | Boundary (Ranh giới kỹ thuật bắt buộc) |
|---|---|---|---|---|---|---|---|---|---|
| **Bảng 3.1** | 3.2.1 | Data Table | Primary Baseline Spec | `Final_PreDemo_Audit.txt`, `Windows_PreDemo_01_Network_SMB.png`, `Windows_PreDemo_02_Firewall.png`, `Windows_FirewallPrep_Final.txt`, `VirtualBox_HostOnly_Config.txt` | Bảng 3.1 | **MOVE & EXPAND** | Bảng 3.1. Thông số kiểm toán mạng, dịch vụ SMB và Windows Firewall mốc xuất phát | Xác lập mốc tham chiếu xuất phát: IP 192.168.56.20/24 không default route, LanmanServer Running, FS-SMB1 Installed, SMB1=True, SMB2=True, socket 139/445 Listen, Windows Firewall bật kèm quy tắc chỉ cho phép 192.168.56.10 kết nối. | Cấu hình nội bộ cục bộ không đồng nghĩa với việc bên ngoài quét thấy mở; socket lắng nghe cục bộ không chứng minh đường mạng thông suốt. |
| **Bảng 3.2** | 3.2.2 | Data Table | Primary Patch Baseline | `MS17-010_Official_Mapping.txt`, `Windows_MS17010_01_SrvSysVersion.png`, `Windows_MS17010_02_Hotfix.png`, `Before_Demo_Snapshots.txt` | Bảng 3.2 | **MOVE** | Bảng 3.2. Đối chiếu phiên bản driver srv.sys, danh mục hotfix và mốc phục hồi hệ thống | Chứng minh máy chủ ở trạng thái UNPATCHED đối với MS17-010: FileVersion hiển thị `6.3.9600.16384`, phiên bản số nhị phân `6.3.9600.16421` thấp hơn ngưỡng tối thiểu `6.3.9600.18604` theo Microsoft KB4012213/KB4012216, danh mục Get-HotFix thiếu bản vá. | Trạng thái UNPATCHED là sự thật nội bộ (local ground truth), hoàn toàn độc lập với phán quyết quét từ xa; không suy diễn thành khai thác thành công. |
| **Bảng 3.3** | 3.3.3 | Data Table | Scenario 1 Synthesis | `b2_host_discovery.nmap`, `b3_target_alive.nmap`, `b4_smb_ports.nmap`, `b5_smb_version.nmap`, `b6_smb_nse.nmap`, `Scenario1_Run_Manifest.txt` | Bảng 3.3 | **MOVE** | Bảng 3.3. Kết quả rà quét nhận diện dịch vụ và phương ngữ SMB tại Kịch bản 1 | Khảo sát diện mạo dịch vụ SMB: Máy chủ trực tuyến, TCP 139 và 445 OPEN kèm cờ syn-ack TTL 128, fingerprint Windows Server 2008 R2–2012, 5 phương ngữ (NT LM 0.12..3.0.2), signing enabled but not required, smb-os-discovery không đầu ra khả dụng. | 445 OPEN != vulnerable; SMBv1 enabled != MS17-010 confirmed. Trạm .56.100 mang nhãn bắt buộc UNKNOWN identity. Chưa đưa ra kết luận về MS17-010. |
| **Bảng 3.4** | 3.4.1 | Data Table | Scenario 2 NSE Audit | `NSE-SMB-01_ports.nmap`, `NSE-SMB-02_protocols.nmap`, `NSE-SMB-03_signing.nmap`, `NSE-SMB-04_ms17010.nmap`, `Scenario2_Run_Manifest.txt` | Bảng 3.4 | **MOVE** | Bảng 3.4. Kết quả chuỗi kịch bản NSE khảo sát thuộc tính dịch vụ và kiểm tra dấu hiệu MS17-010 | Xác nhận chuỗi 4 phép đo NSE: NSE01 (139/445 open syn-ack), NSE02 (5 dialect), NSE03 (signing enabled but not required), NSE04 (cổng 445 open, Nmap done, không có khối Host script results $\to$ UNKNOWN / NO USABLE SCRIPT RESULT). | UNKNOWN != SAFE. Không tự gán mã lỗi hay nguyên nhân script không ra kết quả. UNKNOWN là phân loại phương pháp luận, không phải chuỗi Nmap in ra. |
| **Bảng 3.5** | 3.5.3 | Data Table | Case B Comparison | `case_b/SMBv1_Remediation_Run_Manifest.txt`, `SMBv1_Remediation_01_Before.png`, `02_Action.png`, `03_After_Local.png`, `NSE-SMB-02_protocols.nmap`, `NSE-SMB-04_ms17010.nmap` | Bảng 3.5 | **MOVE** | Bảng 3.5. So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B) | Đánh giá tác động của việc tắt SMBv1: EnableSMB1Protocol chuyển False, FS-SMB1 vẫn Installed, LanmanServer vẫn Running, đo lại từ xa NT LM 0.12 vắng mặt, dialect 2.0.2..3.0.2 còn nguyên, cổng 445 vẫn OPEN, driver srv.sys vẫn UNPATCHED. | Cổng 139 KHÔNG ĐƯỢC ĐO LẠI trong Case B (NOT REMEASURED). Lệnh đo lại cổng 445 không có cờ --reason (không gán syn-ack). SMBv1 disabled != PATCHED. |
| **Bảng 3.6** | 3.6.3 | Data Table | Case C Comparison | `case_c/pfSense_Remediation_Run_Manifest.txt`, `pfSense_08_Rule_Order.png`, `NSE-SMB-01_ports.nmap`, `NSE-SMB-04_ms17010.nmap`, `pfSense_10_Block_Log_CANONICAL.png`, Windows Baseline Audit | Bảng 3.6 | **MOVE** | Bảng 3.6. So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense (Case C) | Đánh giá tác động của kiểm soát pfSense: Cổng 139/445 chuyển sang FILTERED (no-response), nhật ký pfSense ghi nhận chặn gói TCP SYN, máy chủ Windows giữ nguyên SMB1=True, socket Listen và driver srv.sys UNPATCHED. | FILTERED != PATCHED. Lưu lượng TCP SYN bị chặn trên đường truyền; bảo lưu xung đột nhãn quy tắc CF-11, không quy thuộc đích danh named rule ID. |
| **Bảng 3.7** | 3.7.1 | Synthesis Table | Multi-state Matrix | Tổng hợp đối chiếu chéo 83 tệp bằng chứng thực nghiệm của Mục 3.2 đến 3.6, `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` | Bảng 3.7 | **MOVE** | Bảng 3.7. Ma trận so sánh tổng hợp trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C | Đặt 3 trạng thái cạnh nhau trên 7 tiêu chí đo được: Cổng dịch vụ, Phương ngữ SMBv1, Phương ngữ SMB2/3, Phản hồi mạng, Phán quyết quét từ xa, Trạng thái bản vá nội bộ, và Tầng can thiệp. | Không xếp hạng giải pháp nào tốt hơn (no effectiveness ranking). Không kết luận biện pháp can thiệp thay thế được bản vá hệ điều hành. |

---

## 3. SỔ ĐĂNG KÝ HỆ THỐNG HÌNH ẢNH ĐỀ XUẤT (PROPOSED FIGURE LEDGER)

| Proposed No. | New Section | Type | Role | Source canonical | Old No. | Action | Caption dự kiến | Supported claim (Luận điểm chứng minh) | Boundary (Ranh giới kỹ thuật bắt buộc) |
|---|---|---|---|---|---|---|---|---|---|
| **Hình 3.1** | 3.1.2 | Explanatory Figure | Experiment Workflow Diagram | Dựng sơ đồ vector/khối chuẩn khoa học từ thiết kế Chương 2 và `ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md` | *None* | **NEW** | Hình 3.1. Sơ đồ quy trình thực nghiệm kiểm thử dịch vụ SMB và các biện pháp giảm thiểu | Minh họa tiến trình 6 giai đoạn logic: Baseline $\to$ Kịch bản 1 $\to$ Kịch bản 2 $\to$ Case B $\to$ Case C $\to$ Đối chiếu tổng hợp; làm rõ các điểm hoàn nguyên snapshot. | Sơ đồ quy trình giải thích phương pháp; không giả dạng làm ảnh chụp bằng chứng thực nghiệm. Không mô tả như quy trình kiểm thử xâm nhập. |
| **Hình 3.2** | 3.2.1 | Evidence Figure | Local Service & Socket Proof | `chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png` (chuẩn hóa `chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`) | Hình 3.1 | **KEEP** | Hình 3.2. Trạng thái cấu hình mạng, dịch vụ LanmanServer và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm | Chứng minh trực quan IP 192.168.56.20, LanmanServer Running, FS-SMB1 Installed, và tiến trình hệ thống đang lắng nghe trên cổng TCP 139 và 445. | Cổng lắng nghe cục bộ không chứng minh cổng mở trên mạng ngoài. Chỉ phản ánh cấu hình point-in-time trước khi quét. |
| **Hình 3.3** | 3.2.2 | Comparison Figure | Dual Local Patch Ground Truth Panel | Panel A: `baseline/Windows_MS17010_01_SrvSysVersion.png`<br>Panel B: `baseline/Windows_MS17010_02_Hotfix.png` (chuẩn hóa `chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`) | Hình 3.3 | **MERGE** | Hình 3.3. Thuộc tính phiên bản hiển thị của tệp srv.sys và danh mục hotfix ghi nhận trên máy chủ mục tiêu | Ghép 2 panel chứng minh căn cứ phân loại UNPATCHED: Panel A hiển thị FileVersion `6.3.9600.16384`; Panel B hiển thị danh sách 6 hotfix 2014, thiếu bản vá MS17-010. | Phân biệt rõ chuỗi hiển thị `6.3.9600.16384` và phiên bản số nhị phân `6.3.9600.16421`. Ảnh chỉ thể hiện thuộc tính tệp và hotfix, kết luận UNPATCHED dựa trên đối chiếu tài liệu Microsoft. |
| **Hình 3.4** | 3.3.1 | Evidence Figure | Port Reachability Proof | `chapter3/evidence/scenario1/Scenario1_B4_SMB_Ports.png` | Hình 3.2 cũ / Hình 3.4 trong draft R2 | **KEEP** | Hình 3.4. Kết quả quét cổng dịch vụ SMB từ trạm Kali Linux xác nhận cổng 139 và 445 ở trạng thái mở | Minh chứng trực quan cổng 139 và 445 OPEN kèm cờ `syn-ack ttl 128` từ góc nhìn trạm Kali Linux. | 445 OPEN != vulnerable. Cổng mở chỉ chứng minh khả năng tiếp cận giao vận, không chứng minh lỗ hổng hay phiên SMB thành công. |
| **Hình 3.5** | 3.3.2 | Comparison Figure | Service & Protocol Fingerprint Panel | Panel A: `scenario1/Scenario1_B5_SMB_Version.png`<br>Panel B: `scenario1/Scenario1_B6_SMB_NSE_A.png` (chuẩn hóa `chapter3/presentation/3_2/Hinh_3_5_SMB_NSE.png`) | Hình 3.4 cũ & Hình 3.5 cũ | **MERGE** | Hình 3.5. Kết quả phân tích phiên bản dịch vụ, danh sách phương ngữ và chính sách ký số SMB từ trạm Kali Linux | Ghép 2 panel nhận diện dịch vụ: Panel A hiển thị fingerprint Windows Server 2008 R2–2012; Panel B hiển thị 5 dialect (NT LM 0.12..3.0.2) và signing enabled but not required. | SMBv1 enabled != MS17-010 confirmed. Dải fingerprint không định danh tuyệt đối bản 2012 R2. Signing enabled but not required là quan sát từ xa, không phải lỗ hổng. |
| **Hình 3.6** | 3.4.1 | Evidence Figure | Central MS17-010 Test Proof | `chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` (chuẩn hóa `chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`) | Hình 3.6 | **KEEP** | Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux ghi nhận cổng 445 mở và không xuất hiện khối kết luận kịch bản | Minh chứng trung tâm của phép đo MS17-010: Cổng 445 open, Nmap done hoàn tất, hoàn toàn không có khối `Host script results:`. | UNKNOWN != SAFE. UNKNOWN là phân loại dự án, không phải chuỗi Nmap in ra. Không tự bịa đặt nguyên nhân kỹ thuật khi log không có. |
| **Hình 3.7** | 3.4.2 | Comparison Figure | Cross-Layer Verification Diagram | Ghép đối chiếu thị giác: Khung trái là Nmap NSE04 (Remote UNKNOWN), Khung phải là thông số driver `srv.sys` và Hotfix (Local UNPATCHED) | *None* | **NEW** | Hình 3.7. Đối chiếu giữa tín hiệu thăm dò từ xa qua Nmap NSE và trạng thái bản vá thực tế trên máy chủ Windows | Minh chứng trực quan sự độc lập hoàn toàn giữa tín hiệu đo đạc từ xa (UNKNOWN) và sự thật bản vá nội bộ (UNPATCHED). | Không coi UNKNOWN là tool failure. Không suy diễn rằng nếu exploit thật sẽ thành công (exploit nằm ngoài phạm vi phê duyệt). |
| **Hình 3.8** | 3.5.1 | Comparison Figure | Sequential Remediation Panel | Panel 1: `case_b/SMBv1_Remediation_01_Before.png`<br>Panel 2: `case_b/SMBv1_Remediation_02_Action.png`<br>Panel 3: `case_b/SMBv1_Remediation_03_After_Local.png` (chuẩn hóa `chapter3/presentation/3_4/Hinh_3_7_After_Local.png`) | Hình 3.7 | **MERGE** | Hình 3.8. Trình tự thực thi lệnh vô hiệu hóa giao thức SMBv1 và kết quả xác nhận cấu hình cục bộ trên máy chủ Windows | Ghép 3 panel theo thứ tự thời gian: Before (SMB1=True) $\to$ Action (Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force) $\to$ After (SMB1=False, LanmanServer Running, FS-SMB1 Installed). | SMBv1 disabled != FS-SMB1 uninstalled; SMBv1 disabled != PATCHED. Không chứng minh tính liên tục tuyệt đối của ứng dụng nghiệp vụ. |
| **Hình 3.9** | 3.5.2 | Evidence Figure | Remote Protocol Retest Proof | `chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` (chuẩn hóa `chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`) | Hình 3.8 | **KEEP** | Hình 3.9. Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1 xác nhận phương ngữ NT LM 0.12 vắng mặt | Minh chứng đo lại từ xa: Kịch bản smb-protocols chỉ còn 4 dialect (2.0.2..3.0.2), phương ngữ NT LM 0.12 hoàn toàn vắng mặt. | Cổng 139 không đo lại trong Case B. Lệnh đo lại cổng 445 không có cờ --reason (không gán syn-ack). SMBv1 vắng mặt không đồng nghĩa với máy chủ hết lỗ hổng hay cổng 445 đã đóng. |
| **Hình 3.10** | 3.6.1 | Explanatory Figure | Transparent Bridge Topology Diagram | Dựng sơ đồ kiến trúc Transparent Bridge Layer 2 chuẩn khoa học (Kali .56.10 $\to$ pfSense bridge0 em2/em3 $\to$ Windows .56.20) | *None* | **NEW** | Hình 3.10. Sơ đồ kiến trúc mạng pfSense Transparent Bridge kiểm soát lưu lượng SMB giữa trạm Kali Linux và máy chủ mục tiêu | Giải thích mô hình lab Case C: Cầu nối Layer 2 không thay đổi subnet 192.168.56.0/24, không định tuyến Layer 3, lọc gói tại giao diện CASE_C_KALI qua tunables pfil_member=1. | Sơ đồ kiến trúc mạng giải thích; không giả dạng screenshot. CẤM dùng từ "định tuyến qua pfSense" (phải dùng "đi qua cầu nối pfSense"). |
| **Hình 3.11** | 3.6.1 | Evidence Figure | Firewall Rule Order Proof | `chapter3/evidence/case_c/pfSense_08_Rule_Order.png` (chuẩn hóa `chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png`) | Hình 3.9 | **KEEP** | Hình 3.11. Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên giao diện CASE_C_KALI của pfSense | Minh chứng cấu hình pfSense: Quy tắc Block SMB_Ports (cổng 139, 445) có bật Log được đặt ở vị trí Dòng 1, ngay phía trên quy tắc Pass baseline (Dòng 2). | Xác nhận cấu hình và thứ tự hiển thị của ruleset; hiệu lực chặn thực tế bắt buộc phải chứng minh qua đo đạc Nmap và nhật ký ở phần sau. |
| **Hình 3.12** | 3.6.2 | Evidence Figure | Filtered Ports Measurement Proof | `chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` (chuẩn hóa `chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`) | Hình 3.10 | **KEEP** | Hình 3.12. Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense ghi nhận trạng thái filtered | Minh chứng đo lại từ Kali: Cổng 139/tcp và 445/tcp đều ở trạng thái `filtered` do không nhận phản hồi (`no-response`). | FILTERED != PATCHED. Trạng thái filtered chỉ phản ánh góc nhìn mạng từ trạm Kali, không đồng nghĩa máy chủ đã đóng cổng hay đã vá lỗi. |
| **Hình 3.13** | 3.6.3 | Evidence Figure (Bounded) | Firewall Block Log with Conflict Boundary | `chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png` (chuẩn hóa `chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`) | Hình 3.11 | **KEEP (Bảo lưu CF-11)** | Hình 3.13. Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm | Minh chứng thực nghiệm: Nhật ký pfSense ghi nhận 4 sự kiện chặn gói tin TCP SYN từ 192.168.56.10 tới 192.168.56.20 trên cổng 139 và 445 tương ứng thời điểm quét. | **BẢO LƯU XUNG ĐỘT DANH PHÁP (CF-11):** Ảnh hiển thị nhãn `CASE C baseline pass... (100000104)`. TUYỆT ĐỐI KHÔNG CẮT CỘT RULE ĐỂ CHE GIẤU XUNG ĐỘT. Không quy thuộc tuyệt đối named rule ID. Không suy diễn máy chủ an toàn. |
| **Hình 3.14** | 3.7.2 | Explanatory Figure | Defense Layer Separation Diagram | Dựng sơ đồ phân định hai lớp can thiệp: Lớp cấu hình máy chủ nội bộ (Case B) vs. Lớp kiểm soát đường truyền mạng (Case C) | *None* | **NEW** | Hình 3.14. Sơ đồ phân định hai vị trí can thiệp giảm thiểu rủi ro: Lớp cấu hình máy chủ nội bộ và Lớp kiểm soát đường truyền mạng | Giải thích bản chất kỹ thuật: Case B can thiệp Host Layer (loại bỏ phương ngữ), Case C can thiệp Network Path Layer (chặn truy cập); cả hai đều không thay đổi driver srv.sys. | Sơ đồ giải thích khoa học; không đưa ra khuyến nghị chiến lược Defense-in-Depth doanh nghiệp hay tính điểm rủi ro (dành cho Chương 4). |

---

## 4. BẢNG ĐỐI CHIẾU HAI CHIỀU (TWO-WAY TRACEABILITY MAPPING)

### 4.1. Chiều ánh xạ: Cấu trúc cũ $\to$ Cấu trúc mới đề xuất (Old $\to$ New)

Bảo đảm toàn bộ 7 bảng và 11 hình của bản thảo cũ đều được quản lý minh bạch, không bị thất lạc:

| Đối tượng cũ | Tên gọi / Nội dung cũ | Số hiệu đề xuất mới | Đề mục mới | Quyết định chuyển đổi | Ghi chú lý do chuyển đổi kỹ thuật |
|---|---|---|---|---|---|
| **Bảng 3.1 cũ** | Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc | **Bảng 3.1** | 3.2.1 | **MOVE & EXPAND** | Giữ nguyên vai trò bảng kiểm toán mốc xuất phát, chuyển vào Mục 3.2.1 của cấu trúc mới; tích hợp thêm các dữ kiện từ text để giải phóng ảnh `PreDemo_02_Firewall`. |
| **Bảng 3.2 cũ** | Trạng thái bản vá và mốc phục hồi | **Bảng 3.2** | 3.2.2 | **MOVE** | Giữ nguyên cấu trúc đối chiếu srv.sys, hotfix và snapshot mốc phục hồi; chuyển vào Mục 3.2.2 chuyên sâu về trạng thái bản vá MS17-010. |
| **Bảng 3.3 cũ** | Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux | **Bảng 3.3** | 3.3.3 | **MOVE** | Giữ nguyên kết quả 5 bước B2–B6 (cổng, phiên bản, dialect); chuyển vào Mục 3.3.3 làm bảng tổng hợp diện mạo dịch vụ SMB Kịch bản 1. |
| **Bảng 3.4 cũ** | Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux | **Bảng 3.4** | 3.4.1 | **MOVE** | Giữ nguyên 4 phép đo NSE01–04; chuyển vào Mục 3.4.1 tập trung vào kết quả kiểm tra dấu hiệu MS17-010. |
| **Bảng 3.5 cũ** | So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B) | **Bảng 3.5** | 3.5.3 | **MOVE** | Giữ nguyên bảng so sánh 7 tiêu chí Before vs. After của Case B; chuyển vào Mục 3.5.3 làm bảng tổng hợp phân tích thay đổi quan sát được. |
| **Bảng 3.6 cũ** | So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng pfSense (Case C) | **Bảng 3.6** | 3.6.3 | **MOVE** | Giữ nguyên bảng so sánh các tầng kiểm soát của Case C; chuyển vào Mục 3.6.3 làm bảng đối chiếu 3 bên (Kali, pfSense, Windows). |
| **Bảng 3.7 cũ** | So sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C | **Bảng 3.7** | 3.7.1 | **MOVE** | Giữ nguyên ma trận so sánh đa chiều 3 trạng thái; chuyển vào Mục 3.7.1 làm tâm điểm đối chiếu thực nghiệm toàn chương. |
| **Hình 3.1 cũ** | Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 | **Hình 3.2** | 3.2.1 | **MOVE (Số mới: 3.2)** | Nhường số hiệu 3.1 cho Sơ đồ luồng thực nghiệm mới; giữ nguyên ảnh `Windows_PreDemo_01_Network_SMB.png` chứng minh socket và dịch vụ. |
| **Hình 3.2 cũ** | Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux | *Kho bổ trợ (Supporting)* | 3.2.1 | **SUPPORTING** | Thông số quy tắc tường lửa tùy biến đã được mô tả chi tiết trong Bảng 3.1; chuyển ảnh vào kho bằng chứng bổ trợ để giảm tải trực quan, tránh dàn trải ảnh cấu hình. |
| **Hình 3.3 cũ** | Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2 | **Hình 3.3** | 3.2.2 | **MOVE (Số mới: 3.3)** | Giữ nguyên hình ghép 2 panel (`01_SrvSysVersion` + `02_Hotfix`) chứng minh trạng thái bản vá UNPATCHED tại Mục 3.2.2. |
| **Hình 3.4 cũ** | Kết quả thăm dò phiên bản dịch vụ SMB từ xa bằng công cụ Nmap (-sV) | **Hình 3.5 (Panel A)** | 3.3.2 | **MERGE** | Ghép cùng kết quả kịch bản NSE thành Hình 3.5 (Panel A: Fingerprint dịch vụ; Panel B: Phân tích dialect NSE). |
| **Hình 3.5 cũ** | Kết quả phân tích phương ngữ, tính năng và chính sách ký số SMB bằng Nmap NSE | **Hình 3.5 (Panel B)** | 3.3.2 | **MERGE** | Ghép cùng kết quả -sV thành Hình 3.5 để người đọc thấy trọn vẹn diện mạo dịch vụ SMB trong một cụm thị giác thống nhất. |
| **Hình 3.6 cũ** | Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux | **Hình 3.6 & Hình 3.7** | 3.4.1 & 3.4.2 | **KEEP & EXPAND** | Hình 3.6 giữ nguyên làm bằng chứng trung tâm cho phép đo NSE04 (UNKNOWN); đồng thời làm thành phần đầu vào cho sơ đồ đối chiếu chéo Hình 3.7. |
| **Hình 3.7 cũ** | Trạng thái cấu hình SMB, tính năng FS-SMB1 và dịch vụ LanmanServer sau khi tắt SMBv1 | **Hình 3.8** | 3.5.1 | **MERGE & EXPAND** | Mở rộng thành chuỗi thao tác 3 panel: Panel 1 (Trước) $\to$ Panel 2 (Lệnh thực thi) $\to$ Panel 3 (Sau can thiệp) giúp người đọc theo dõi mạch lạc hành động quản trị. |
| **Hình 3.8 cũ** | Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1 | **Hình 3.9** | 3.5.2 | **MOVE (Số mới: 3.9)** | Giữ nguyên làm bằng chứng đo lại cốt lõi: Phương ngữ NT LM 0.12 vắng mặt khỏi danh sách đàm phán quan sát được từ xa. |
| **Hình 3.9 cũ** | Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên pfSense | **Hình 3.11** | 3.6.1 | **MOVE (Số mới: 3.11)** | Giữ nguyên làm bằng chứng cấu hình Case C: Hàng Block SMB đặt trên hàng Baseline Pass có bật Log trên giao diện CASE_C_KALI. |
| **Hình 3.10 cũ** | Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense | **Hình 3.12** | 3.6.2 | **MOVE (Số mới: 3.12)** | Giữ nguyên làm bằng chứng đo lại cốt lõi của Case C: Cổng 139 và 445 chuyển sang trạng thái filtered (no-response). |
| **Hình 3.11 cũ** | Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm | **Hình 3.13** | 3.6.3 | **MOVE (Số mới: 3.13)** | Giữ nguyên làm bằng chứng nhật ký cốt lõi của Case C; giữ nguyên ranh giới bảo lưu xung đột nhãn quy tắc CF-11. |

---

### 4.2. Chiều ánh xạ: Cấu trúc mới đề xuất $\to$ Nguồn bằng chứng canonical (New $\to$ Evidence Source)

Bảo đảm tính kiểm toán và truy vết 100% của cấu trúc mới:

| Số đề xuất | Đề mục mới | Loại | Nguồn tệp canonical trong repository | Căn cứ phương pháp / Script | Luận điểm kiểm chứng |
|---|---|---|---|---|---|
| **Bảng 3.1** | 3.2.1 | Table | `work/do-an/chapter3/evidence/baseline/Final_PreDemo_Audit.txt` | PowerShell Audit Script | Cấu hình IP, dịch vụ LanmanServer, FS-SMB1, cổng lắng nghe và Windows Firewall tại mốc xuất phát. |
| **Hình 3.1** | 3.1.2 | Figure | Sơ đồ vector do báo cáo dựng dựa trên `work/do-an/CHAPTER_2.md` | Flowchart thiết kế thực nghiệm | Luồng 6 giai đoạn thực nghiệm có kiểm soát và các điểm hoàn nguyên snapshot. |
| **Hình 3.2** | 3.2.1 | Figure | `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png` | `Get-NetIPAddress`, `Get-Service`, `netstat` | Bằng chứng trực tiếp máy chủ đang chạy dịch vụ và mở socket lắng nghe cổng 139, 445. |
| **Bảng 3.2** | 3.2.2 | Table | `work/do-an/chapter3/evidence/baseline/MS17-010_Official_Mapping.txt` | Microsoft Support Bulletin MS17-010 | Đối chiếu phiên bản srv.sys 6.3.9600.16421 < 6.3.9600.18604 và danh mục 6 hotfix năm 2014 $\to$ UNPATCHED. |
| **Hình 3.3** | 3.2.2 | Figure | `baseline/Windows_MS17010_01_SrvSysVersion.png` + `baseline/Windows_MS17010_02_Hotfix.png` | Properties `srv.sys` + `Get-HotFix` | Minh chứng thị giác tệp driver hiển thị `6.3.9600.16384` và danh mục hotfix không có bản vá MS17-010. |
| **Hình 3.4** | 3.3.1 | Figure | `work/do-an/chapter3/evidence/scenario1/Scenario1_B4_SMB_Ports.png` | `nmap -p 139,445 --reason` | Minh chứng trực tiếp cổng 139 và 445 mở, phản hồi syn-ack TTL 128 từ góc nhìn trạm Kali. |
| **Hình 3.5** | 3.3.2 | Figure | `scenario1/Scenario1_B5_SMB_Version.png` + `scenario1/Scenario1_B6_SMB_NSE_A.png` | `nmap -sV` + `nmap --script smb-protocols` | Minh chứng dải fingerprint dịch vụ và 5 dialect SMB quan sát được từ xa. |
| **Bảng 3.3** | 3.3.3 | Table | `work/do-an/chapter3/evidence/scenario1/b{2..6}_*.nmap` | Chuỗi quét Nmap B2–B6 Kịch bản 1 | Bảng dữ liệu chuẩn hóa diện mạo dịch vụ SMB Kịch bản 1. |
| **Bảng 3.4** | 3.4.1 | Table | `work/do-an/chapter3/evidence/scenario2/NSE-SMB-0{1..4}_*.nmap` | Chuỗi 4 kịch bản Nmap NSE Kịch bản 2 | Bảng dữ liệu chuẩn hóa kết quả đo đạc NSE và phán quyết UNKNOWN / NO USABLE SCRIPT RESULT. |
| **Hình 3.6** | 3.4.1 | Figure | `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` | `nmap -p 445 --script smb-vuln-ms17-010` | Bằng chứng thực nghiệm Nmap done không xuất hiện khối Host script results $\to$ UNKNOWN. |
| **Hình 3.7** | 3.4.2 | Figure | Ghép đối chiếu `Scenario2_NSE04_MS17010.png` và `Windows_MS17010_01_SrvSysVersion.png` | Tổng hợp đối chứng đa tầng | Minh họa trực quan sự độc lập giữa tín hiệu thăm dò từ xa (UNKNOWN) và trạng thái bản vá nội bộ (UNPATCHED). |
| **Hình 3.8** | 3.5.1 | Figure | `case_b/SMBv1_Remediation_0{1..3}_*.png` | Chuỗi lệnh PowerShell Case B | Trình tự thực thi lệnh tắt SMBv1 và xác nhận cấu hình nội bộ (Before $\to$ Action $\to$ After). |
| **Hình 3.9** | 3.5.2 | Figure | `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` | `nmap --script smb-protocols` | Bằng chứng đo lại xác nhận phương ngữ NT LM 0.12 vắng mặt khỏi danh sách đàm phán. |
| **Bảng 3.5** | 3.5.3 | Table | `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_Run_Manifest.txt` | Dữ liệu kiểm toán Case B | So sánh Before vs. After trên 7 tiêu chí đo đạc của Case B. |
| **Hình 3.10** | 3.6.1 | Figure | Sơ đồ vector do báo cáo dựng dựa trên cấu hình mạng pfSense | Mô hình Transparent Bridge Layer 2 | Giải thích cấu trúc luồng lưu lượng đi qua cầu nối pfSense không thay đổi IP subnet. |
| **Hình 3.11** | 3.6.1 | Figure | `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png` | Giao diện cấu hình pfSense GUI | Bằng chứng cấu hình quy tắc Block SMB_Ports xếp trên quy tắc Pass baseline có bật Log. |
| **Hình 3.12** | 3.6.2 | Figure | `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | `nmap -p 139,445 --reason` | Bằng chứng đo lại xác nhận cổng 139 và 445 rơi vào trạng thái filtered (no-response). |
| **Hình 3.13** | 3.6.3 | Figure | `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png` | pfSense System Logs Firewall | Bằng chứng nhật ký ghi nhận hành động Block các gói TCP SYN tới cổng 139/445 (bảo lưu CF-11). |
| **Bảng 3.6** | 3.6.3 | Table | `work/do-an/chapter3/evidence/case_c/pfSense_Remediation_Run_Manifest.txt` | Dữ liệu kiểm toán Case C | So sánh Before vs. After trên các tầng kiểm soát của Case C. |
| **Bảng 3.7** | 3.7.1 | Table | Đối chiếu chéo từ 83 tệp bằng chứng thực nghiệm và ETM | Ma trận so sánh đa chiều | Tổng hợp so sánh 3 trạng thái thực nghiệm (Baseline, Case B, Case C) trên 7 tiêu chí đo được. |
| **Hình 3.14** | 3.7.2 | Figure | Sơ đồ vector do báo cáo dựng dựa trên phân tích kỹ thuật | Mô hình phân tầng can thiệp | Phân định rạch ròi hai vị trí can thiệp phòng thủ: Lớp cấu hình máy chủ vs. Lớp kiểm soát đường mạng. |

---

## 5. BẢNG KIỂM TOÁN VÀ ĐỊNH VỊ TOÀN BỘ 34 ẢNH CANONICAL NGUỒN

Bảo đảm mọi tệp ảnh canonical trong 5 thư mục đều có trạng thái định vị cụ thể:

| STT | Tên tệp ảnh canonical nguồn | Thư mục | Quyết định trong Ledger | Xuất hiện tại Proposed Figure | Trạng thái lưu trữ & Vai trò |
|---|---|---|---|---|---|
| 1 | `Windows_PreDemo_01_Network_SMB.png` | `baseline/` | **KEEP** | **Hình 3.2** | Bằng chứng độc lập chính về IP, dịch vụ và socket lắng nghe mốc xuất phát. |
| 2 | `Windows_PreDemo_02_Firewall.png` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ trong kho bằng chứng bổ trợ; số liệu quy tắc đã tích hợp trong Bảng 3.1. |
| 3 | `Windows_Baseline_01_Winver.png` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát thông số Windows Server 2012 R2 Build 9600. |
| 4 | `Windows_Baseline_04_SMB_Service.png` | `baseline/` | **RETIRE** | *Loại bỏ khỏi main text* | Trùng lặp; đã được thay thế bởi `Windows_PreDemo_01_Network_SMB.png` bao quát hơn. |
| 5 | `Windows_Baseline_05_SMB_Features.png` | `baseline/` | **RETIRE** | *Loại bỏ khỏi main text* | Trùng lặp; đã được thay thế bởi `Windows_PreDemo_01_Network_SMB.png` (dòng Get-WindowsFeature). |
| 6 | `Windows_Baseline_06_SMB_Config.png` | `baseline/` | **RETIRE** | *Loại bỏ khỏi main text* | Trùng lặp; số liệu EnableSMB1/2Protocol đã được Bảng 3.1 tổng hợp đầy đủ. |
| 7 | `Windows_Baseline_07_Firewall.png` | `baseline/` | **RETIRE** | *Loại bỏ khỏi main text* | Trùng lặp; trạng thái firewall profiles đã được thể hiện ở PreDemo. |
| 8 | `Windows_FirewallPrep_04_Scope.png` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cấu hình RemoteAddress Scope 192.168.56.10 cho Bảng 3.1. |
| 9 | `Windows_MS17010_01_SrvSysVersion.png` | `baseline/` | **MERGE** | **Hình 3.3 (Panel A)** | Ghép thành Panel A của Hình 3.3 chứng minh FileVersion `6.3.9600.16384` của `srv.sys`. |
| 10 | `Windows_MS17010_02_Hotfix.png` | `baseline/` | **MERGE** | **Hình 3.3 (Panel B)** | Ghép thành Panel B của Hình 3.3 chứng minh danh mục 6 hotfix năm 2014 thiếu bản vá MS17-010. |
| 11 | `Kali_PreDemo_01_Network_Tools.png` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát IP Kali và phiên bản Nmap 7.99 cho Bảng 3.1. |
| 12 | `Kali_PreDemo_02_NSE_Scripts.png` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát tính sẵn sàng của các script NSE trên trạm kiểm thử. |
| 13 | `Kali_to_Windows_Connectivity.png` | `baseline/` | `baseline/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát kiểm tra liên thông mạng hai chiều trước thực nghiệm. |
| 14 | `Scenario1_B4_SMB_Ports.png` | `scenario1/` | **KEEP** | **Hình 3.4** | Bằng chứng độc lập chính về cổng 139 và 445 OPEN kèm cờ syn-ack TTL 128. |
| 15 | `Scenario1_B5_SMB_Version.png` | `scenario1/` | **MERGE** | **Hình 3.5 (Panel A)** | Ghép thành Panel A của Hình 3.5 chứng minh dải fingerprint dịch vụ. |
| 16 | `Scenario1_B6_SMB_NSE_A.png` | `scenario1/` | **MERGE** | **Hình 3.5 (Panel B)** | Ghép thành Panel B của Hình 3.5 chứng minh 5 phương ngữ SMB và signing policy. |
| 17 | `Scenario2_NSE01_Ports.png` | `scenario2/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cho Bảng 3.4; kết quả cổng mở đã được chứng minh trực quan bởi Hình 3.4. |
| 18 | `Scenario2_NSE02_Protocols.png` | `scenario2/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cho Bảng 3.4; kết quả 5 dialect đã được chứng minh trực quan bởi Hình 3.5. |
| 19 | `Scenario2_NSE03_Signing.png` | `scenario2/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cho Bảng 3.4; thuộc tính signing đã được bao hàm trong Bảng 3.4 và Hình 3.5. |
| 20 | `Scenario2_NSE04_MS17010.png` | `scenario2/` | **KEEP** | **Hình 3.6 & Hình 3.7** | Bằng chứng độc lập cốt lõi của phép đo NSE04 (UNKNOWN) và đầu vào cho Hình 3.7. |
| 21 | `SMBv1_Remediation_01_Before.png` | `case_b/` | **MERGE** | **Hình 3.8 (Panel 1)** | Ghép thành Panel 1 (Trước can thiệp: SMB1=True) của Hình 3.8. |
| 22 | `SMBv1_Remediation_02_Action.png` | `case_b/` | **MERGE** | **Hình 3.8 (Panel 2)** | Ghép thành Panel 2 (Lệnh thực thi Set-SmbServerConfiguration) của Hình 3.8. |
| 23 | `SMBv1_Remediation_03_After_Local.png` | `case_b/` | **MERGE** | **Hình 3.8 (Panel 3)** | Ghép thành Panel 3 (Sau can thiệp: SMB1=False, LanmanServer Running) của Hình 3.8. |
| 24 | `SMBv1_Remediation_04_NSE02_Protocols.png` | `case_b/` | **KEEP** | **Hình 3.9** | Bằng chứng độc lập chính về việc phương ngữ NT LM 0.12 vắng mặt khỏi danh sách đàm phán. |
| 25 | `SMBv1_Remediation_05_NSE04_MS17010.png` | `case_b/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cho Bảng 3.5; kết quả UNKNOWN đo lại đã được Bảng 3.5 ghi nhận đầy đủ. |
| 26 | `pfSense_03_Interface_Assignment.png` | `case_c/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát gán card mạng em2/em3 cho Bảng 3.6 và Hình 3.10. |
| 27 | `pfSense_04_Bridge.png` | `case_c/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cấu hình bridge0 cho Bảng 3.6 và Hình 3.10. |
| 28 | `pfSense_05_Bridge_Filtering.png` | `case_c/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát FreeBSD tunables pfil_member=1 cho Bảng 3.6. |
| 29 | `pfSense_06_Baseline_Pass_Rule.png` | `case_c/` | **RETIRE** | *Loại bỏ khỏi main text* | Trùng lặp; đã được bao hàm trọn vẹn trong `pfSense_08_Rule_Order.png` (hàng Pass Dòng 2). |
| 30 | `pfSense_07_Block_Rule_Config.png` | `case_c/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát form cấu hình quy tắc Block cho Hình 3.11 và Bảng 3.6. |
| 31 | `pfSense_08_Rule_Order.png` | `case_c/` | **KEEP** | **Hình 3.11** | Bằng chứng độc lập chính về thứ tự quy tắc: Block SMB xếp trên Pass baseline có bật Log. |
| 32 | `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | `case_c/` | **KEEP** | **Hình 3.12** | Bằng chứng độc lập chính về việc cổng 139 và 445 chuyển sang filtered (no-response). |
| 33 | `pfSense_10_Block_Log_CANONICAL.png` | `case_c/` | **KEEP** | **Hình 3.13** | Bằng chứng độc lập chính về nhật ký chặn gói TCP SYN trên đường truyền (bảo lưu CF-11). |
| 34 | `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | `case_c/` | **SUPPORTING** | *Không đưa vào main text* | Lưu giữ đối soát cho Bảng 3.6; trạng thái filtered đo lại đã được Bảng 3.6 ghi nhận. |

---

## 6. TỔNG KẾT VÀ CHỈ SỐ PHÂN BỔ THỊ GIÁC

- **Tổng số bảng biểu đề xuất:** **7 bảng** (Bảng 3.1 đến Bảng 3.7).
- **Tổng số hình ảnh đề xuất:** **14 hình** (Hình 3.1 đến Hình 3.14).
  - *Hình bằng chứng đơn lẻ (Evidence Figures):* 6 hình (Hình 3.2, 3.4, 3.6, 3.9, 3.11, 3.12, 3.13 — gồm 7 lượt xuất hiện trên 6 tệp canonical).
  - *Hình so sánh / ghép panel (Comparison Figures):* 4 hình (Hình 3.3 ghép 2 panel, Hình 3.5 ghép 2 panel, Hình 3.7 ghép 2 góc nhìn, Hình 3.8 ghép 3 panel).
  - *Hình sơ đồ giải thích (Explanatory Figures):* 3 hình mới (Hình 3.1 sơ đồ luồng, Hình 3.10 sơ đồ cầu nối pfSense, Hình 3.14 sơ đồ phân định hai vị trí can thiệp).
- **Tổng số ảnh canonical đã kiểm toán:** **34 ảnh**.
  - `KEEP`: 6 ảnh.
  - `MERGE`: 7 ảnh.
  - `SUPPORTING`: 16 ảnh.
  - `RETIRE FROM MAIN TEXT`: 5 ảnh.
- **Trạng thái sổ đăng ký:** `PROPOSED / WAITING EXTERNAL REVIEW` (Tuyệt đối không tự ý khóa trước khi có phê duyệt từ reviewer và người dùng).
