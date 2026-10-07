# BÁO CÁO THẨM ĐỊNH TOÀN DIỆN SẢN PHẨM CHƯƠNG 2 + CHƯƠNG 3 (X7J PRODUCT REVIEW R1)

- **Mục tiêu:** Thẩm định độc lập toàn diện chất lượng học thuật và tính nhất quán sản phẩm của tập tài liệu kết hợp Chương 2 và Chương 3 theo góc nhìn của hội đồng chấm đồ án / giảng viên phản biện.
- **Quy chuẩn ủy quyền:** `work/do-an/prompts/X7J_FINAL_CH2_CH3_PRODUCT_REVIEW.md`
- **Tài liệu tham chiếu lộ trình:** `work/do-an/ROADMAP_CURRENT_CH2_CH3_2026_10_07.md` và `work/do-an/PROJECT_STATE.md`
- **Nhánh làm việc chính thức:** `feature/x7j-final-ch2-ch3-review-r1`
- **Base reviewed commit:** `cf41763e340d4449300db16debd21820b5fad0d2`
- **Tệp Word đối tượng thẩm định:** `work/do-an/output/CHAPTER_2_3_REVIEW.docx`
- **Thời gian lập báo cáo:** 2026-10-07T16:00:00+07:00

---

## 1. Xác thực tính toàn vẹn và định danh tệp Word kết hợp (Artifact Identity Verification)

Trước khi tiến hành đánh giá nội dung, đối tượng kiểm tra đã được đối soát kỹ thuật độc lập về kích thước, mã băm và nguồn gốc:

| Tiêu chí kỹ thuật | Giá trị quy chuẩn / Yêu cầu prompt | Giá trị thực tế đo đạc | Kết quả kiểm tra |
|---|---|---|---|
| **Đường dẫn tệp Word** | `work/do-an/output/CHAPTER_2_3_REVIEW.docx` | `work/do-an/output/CHAPTER_2_3_REVIEW.docx` | Khớp đúng đường dẫn |
| **Kích thước tệp (bytes)** | `761.414 bytes` | `761.414 bytes` | **PASS** |
| **Mã băm SHA-256** | `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2` | `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2` | **PASS** |
| **Git blob Chương 2** | `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0` | `55ffb13acb3398c7ab29d6d5abbb369e5d26f3d0` | **PASS (Bảo toàn)** |
| **Git blob Chương 3** | `40d2a895bc970f88d7260b3138b8a701f5eb0a8c` | `40d2a895bc970f88d7260b3138b8a701f5eb0a8c` | **PASS (Bảo toàn)** |
| **Tổng số trang** | 44 trang (12 trang Ch2 + 32 trang Ch3) | 44 trang (A4 portrait) | **PASS** |
| **Báo cáo QA tham chiếu** | [CHAPTER_2_3_REVIEW_DOCX_QA.md](file:///e:/word_ppt-auto/work/do-an/output/CHAPTER_2_3_REVIEW_DOCX_QA.md) | QA R3 đã xác thực chuỗi mã băm bất biến | **PASS** |

*Kết luận định danh:* Tệp Word đang thẩm định hoàn toàn trùng khớp byte-for-byte với tệp đã đóng băng và vượt qua kiểm định trực quan 44/44 trang tại vòng X7I R3. Không có sự trôi lệch hay tái tạo tệp trái phép.

---

## 2. Đánh giá tính nhất quán: Phương pháp Chương 2 ↔ Kết quả Chương 3 (Method ↔ Result Consistency)

Một tiêu chuẩn cốt lõi của đồ án kỹ thuật là mọi kết quả đo đạc trình bày ở chương thực nghiệm phải có cơ sở phương pháp và thiết kế tương ứng ở chương trước, và ngược lại, mọi quy trình được chuẩn hóa ở chương phương pháp đều phải được phản ánh tương ứng trong dữ liệu thực nghiệm.

### Bảng đối chiếu ánh xạ Phương pháp ↔ Kết quả thực nghiệm

| STT | Cụm thực nghiệm / Nhóm đối tượng | Cơ sở phương pháp tại Chương 2 | Kết quả & Phân tích tại Chương 3 | Đánh giá tính nhất quán |
|---|---|---|---|---|
| 1 | **Thiết lập mạng Host-Only & Cách ly lab** | • **Mục 2.1.2 & Hình 2.1:** Topo mạng Host-Only `192.168.56.0/24`, Kali `192.168.56.10`, Windows `192.168.56.20`, không default route, không NAT/Bridged.<br>• **Mục 2.2.1:** Vô hiệu hóa DHCP VirtualBox. | • **Mục 3.1.1 & Bảng 3.1:** Bảng định tuyến hai máy chỉ có subnet cục bộ, không default route, 1 card mạng Host-Only.<br>• **Hình 3.1:** PowerShell hiển thị IP `192.168.56.20/24`. | **Khớp:** Thiết kế cách ly mạng ở Ch2 được xác thực đầy đủ bằng bảng định tuyến và giao diện mạng ở Ch3. |
| 2 | **Cấu hình trạm mục tiêu & Windows Firewall baseline** | • **Mục 2.1.3 & Bảng 2.1:** Thông số VM (2 vCPU, 4GB RAM), Build 9600.<br>• **Mục 2.2.3:** Dịch vụ LanmanServer Running (Automatic), EnableSMB1=True, EnableSMB2=True, FS-SMB1 Installed, Windows Firewall Enabled, quy tắc cho phép TCP 139/445 từ `192.168.56.10`. | • **Mục 3.1.1 & Bảng 3.1:** LanmanServer Running, FS-SMB1 Installed, EnableSMB1=True, EnableSMB2=True, socket 139/445 Listen.<br>• **Hình 3.1:** Trạng thái PowerShell xác thực.<br>• **Hình 3.2:** Quy tắc `ATTT Lab SMB 139-445` (TCP 139/445 Allow Inbound từ RemoteAddress `192.168.56.10`). | **Khớp:** Toàn bộ thông số dịch vụ và chính sách tường lửa nội bộ được chứng minh rõ nét, không thiếu sót. |
| 3 | **Xác định trạng thái bản vá MS17-010 nội bộ** | • **Mục 2.2.4:** Driver `srv.sys` phiên bản chuỗi `6.3.9600.16384`, phiên bản số `6.3.9600.16421` thấp hơn ngưỡng Microsoft `6.3.9600.18604` (KB4012213/KB4012216); `Get-HotFix` không có bản vá MS17-010; phân loại `UNPATCHED`.<br>• **Mục 2.2.5:** Snapshot `Before Demo`. | • **Mục 3.1.2 & Bảng 3.2:** Phân tích chi tiết 4 trường số của `srv.sys` = `6.3.9600.16421 < 6.3.9600.18604`.<br>• **Hình 3.3:** Ảnh chụp PowerShell srv.sys và danh mục 6 hotfix 2014.<br>• Phân loại cục bộ: `UNPATCHED`. Snapshot `Before Demo` ghi nhận. | **Khớp:** Phương pháp trích xuất số phiên bản nhị phân và đối chiếu hotfix được hiện thực hóa trọn vẹn tại Mục 3.1.2. |
| 4 | **Kịch bản 1: Khảo sát dịch vụ SMB (B1 – B6)** | • **Mục 2.3.1 & 2.3.2 (Bảng 2.2):** Quy trình 6 bước tuần tự: B1 (kiểm tra IP/route), B2 (ARP dải mạng), B3 (ARP mục tiêu up), B4 (quét cổng TCP 139/445), B5 (nhận diện phiên bản -sV), B6 (tập kịch bản NSE giao thức SMB). | • **Mục 3.2.1, 3.2.2 & Bảng 3.3:** B2 phát hiện 4 IP (.1, .10, .20, .100); B3 xác nhận target up; B4 cổng 139/445 OPEN (`syn-ack`); B5 dải OS Windows Server 2008 R2–2012 (**Hình 3.4**); B6 5 phương ngữ (NT LM 0.12, 2.0.2..3.0.2), ký số không bắt buộc, `smb-os-discovery` no usable output (**Hình 3.5**). | **Khớp:** Chuỗi 6 bước kỹ thuật ánh xạ trực tiếp sang chuỗi kết quả B2–B6 trong Bảng 3.3 và các hình ảnh minh chứng. |
| 5 | **Kịch bản 2: Kiểm tra dấu hiệu MS17-010 (NSE-SMB-01..04)** | • **Mục 2.4.1 & 2.4.2 (Bảng 2.3):** Chuỗi 4 phép đo NSE: NSE-SMB-01 (cổng 139/445), NSE-SMB-02 (`smb-protocols`), NSE-SMB-03 (`smb2-security-mode`), NSE-SMB-04 (`smb-vuln-ms17-010`).<br>• **Mục 2.4.3:** Nguyên tắc UNKNOWN / NO USABLE SCRIPT RESULT, `UNKNOWN != SAFE`. | • **Mục 3.3.1, 3.3.2 & Bảng 3.4:** Báo cáo tuần tự NSE-SMB-01 (139/445 OPEN), NSE-SMB-02 (5 phương ngữ), NSE-SMB-03 (signing enabled but not required trên 3.0.2), NSE-SMB-04 (cổng 445 open, Nmap done, không có `Host script results:`, **Hình 3.6**).<br>• Phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`, bảo toàn `UNKNOWN != SAFE`. | **Khớp:** 4 phép đo NSE được báo cáo mạch lạc, phân loại an toàn nghiêm ngặt đúng nguyên tắc đã thiết lập ở Ch2. |
| 6 | **Case B: Vô hiệu hóa SMBv1 trên máy chủ Windows** | • **Mục 2.5.1 (Bảng 2.4) & 2.5.2:** Thao tác PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`, kiểm tra cục bộ, đo đạc lại từ xa qua NSE-SMB-02 và NSE-SMB-04.<br>• Ranh giới: không reboot, FS-SMB1 không gỡ, `SMBv1 disabled != PATCHED`. | • **Mục 3.4.1, 3.4.2, Bảng 3.5:** Cục bộ: EnableSMB1=False, EnableSMB2=True, FS-SMB1=Installed, LanmanServer=Running (**Hình 3.7**).<br>• Đo lại từ xa: 4 phương ngữ SMB2/3, NT LM 0.12 biến mất (**Hình 3.8**); NSE-SMB-04 duy trì UNKNOWN.<br>• Phân định 4 tầng độc lập, bảo toàn `SMBv1 disabled != PATCHED`. | **Khớp:** Thao tác can thiệp và các phép đo lại diễn ra chính xác theo kế hoạch; ranh giới kỹ thuật được giữ vững. |
| 7 | **Case C: Kiểm soát SMB bằng pfSense Transparent Bridge** | • **Mục 2.5.1 (Bảng 2.4) & 2.5.3 (Hình 2.2):** Kiến trúc cầu nối L2 `bridge0` (em2 `CASE_C_KALI`, em3 `CASE_C_WINDOWS`), tunables nhân FreeBSD (`pfil_member=1`, `pfil_bridge=0`), luật Block TCP 139/445 có bật log.<br>• Kế hoạch đo lại: quét cổng và script MS17-010 từ Kali.<br>• Ranh giới: `FILTERED != PATCHED`. | • **Mục 3.5.1, 3.5.2, Bảng 3.6:** Cấu hình cầu nối bridge0, rule order Block trên Pass (**Hình 3.9**).<br>• Đo đạc từ xa: cổng 139/445 chuyển sang `FILTERED` (no-response, **Hình 3.10**); log pfSense ghi nhận 4 sự kiện Block TCP SYN (**Hình 3.11**); NSE-SMB-04 báo `filtered`, duy trì UNKNOWN.<br>• Host Windows giữ nguyên cấu hình và trạng thái UNPATCHED; bảo toàn `FILTERED != PATCHED`. | **Khớp:** Mô hình cầu nối L2 và chính sách lọc được thực thi đúng kiến trúc thiết kế; đối chiếu liên tầng giữa Nmap và log tường lửa chuẩn xác. |
| 8 | **Tổng hợp so sánh đa chiều** | • **Mục 2.5.1 & 2.6.3:** Phương pháp so sánh đối chiếu đa kịch bản (Baseline vs B vs C), 5 ranh giới suy luận an toàn, không đồng bộ đồng hồ ảo. | • **Mục 3.6 & Bảng 3.7:** Đối chiếu 7 tiêu chí qua 3 giai đoạn; làm rõ tầng can thiệp (host vs mạng); tái khẳng định 5 ranh giới kỹ thuật; không xếp hạng chủ quan. | **Khớp:** Bảng tổng hợp 3.7 tổng kết trung thực từ các kết quả đo đạc thực tế, không bổ sung suy diễn ngoài phạm vi. |
| 9 | **Kết luận chương** | • **Mục 2.7:** Tóm lược thiết kế và cam kết làm nền tảng cho Chương 3. | • **Mục 3.7:** Đúc kết toàn bộ kết quả đo đạc, khẳng định tính độc lập giữa quan sát từ xa và bản vá nội bộ, khép lại phạm vi thực nghiệm. | **Khớp:** Mạch tổng kết ăn khớp tự nhiên, kết thúc chương trọn vẹn. |

### Đánh giá các nguy cơ lệch pha (Divergence Risks)
- **Có kết quả nào thiếu cơ sở phương pháp không?** **KHÔNG.** Toàn bộ 11 bảng biểu và 13 hình ảnh trong Chương 3 đều có căn cứ từ các bước thiết kế và quy trình đã công bố ở Chương 2.
- **Có phương pháp nào không được phản ánh trong kết quả không?** **KHÔNG.** Toàn bộ các bước B1–B6, 4 phép đo NSE, 2 ca can thiệp Case B, Case C đều được báo cáo kết quả tương ứng đầy đủ.
- **Có sự bất đối xứng phạm vi (Scope Mismatch) giữa hai chương không?** **KHÔNG.** Cả hai chương đều duy trì phạm vi thực nghiệm cô lập, phi xâm nhập, không khai thác sâu, không payload vũ khí hóa.

---

## 3. Kiểm toán tính nhất quán thuật ngữ (Terminology Consistency Audit)

Tài liệu được rà soát kỹ lưỡng đối với các thuật ngữ chuyên môn quan trọng:

1. **Thuật ngữ trạng thái cơ sở (`baseline`):** Được dùng thống nhất xuyên suốt cả hai chương để chỉ trạng thái hệ thống ban đầu chưa qua can thiệp (Mục 2.1.2, 2.2.1, 2.5.1, Bảng 2.4 ↔ Mục 3.1, 3.2, Bảng 3.1, Bảng 3.5, Bảng 3.6, Bảng 3.7). Không bị lẫn lộn sang các từ ngữ tùy tiện.
2. **Định danh kịch bản khảo sát (`Kịch bản 1` / `Kịch bản 2`):** Phân định rõ ràng:
   - `Kịch bản 1`: Khảo sát diện mạo dịch vụ SMB bằng Nmap (Mục 2.3 ↔ Mục 3.2).
   - `Kịch bản 2`: Kiểm tra dấu hiệu MS17-010 bằng NSE (Mục 2.4 ↔ Mục 3.3).
3. **Định danh ca can thiệp phòng thủ (`Case B` / `Case C`):**
   - `Case B`: Can thiệp cấu hình hệ điều hành (vô hiệu hóa SMBv1 trên Windows Server) (Mục 2.5.2 ↔ Mục 3.4).
   - `Case C`: Can thiệp trên đường truyền mạng (tường lửa pfSense Transparent Bridge) (Mục 2.5.3 ↔ Mục 3.5).
   - Biện pháp cài đặt bản vá (Case A) được định vị nhất quán là tham chiếu thảo luận tại Chương 4, không bị gọi nhầm thành một ca đo đạc thực nghiệm.
4. **Hệ thống giao thức (`SMB` / `SMBv1` / `SMB2/3`):** Phân biệt mạch lạc giữa ngăn xếp giao thức SMB nói chung, giao thức cũ kế thừa SMBv1 (ứng với phương ngữ `NT LM 0.12` và tính năng `FS-SMB1`), và các phương ngữ hiện đại SMB2/3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`).
5. **Cổng dịch vụ (`TCP 139` / `TCP 445`):** Luôn đi kèm phân định chức năng: cổng 139 là NetBIOS Session Service (`netbios-ssn`), cổng 445 là Direct-hosted SMB (`microsoft-ds`).
6. **Thuật ngữ trạng thái an ninh & cổng:**
   - `OPEN`: Cổng tiếp nhận kết nối TCP (kèm `syn-ack` hoặc ghi nhận trong phép đo lại).
   - `FILTERED`: Cổng bị lọc bởi thiết bị mạng (kèm lý do `no-response`).
   - `UNKNOWN / NO USABLE SCRIPT RESULT`: Phân loại phương pháp luận khi kịch bản quét không cho ra phán quyết, không viết tắt tùy tiện.
   - `UNPATCHED`: Phân loại trạng thái bản vá cục bộ của hệ điều hành máy chủ, phân biệt rạch ròi với phán quyết quét từ xa.
7. **Kiến trúc pfSense Transparent Bridge:** Sử dụng nhất quán khái niệm "Cầu nối trong suốt Layer 2", "bridge0", "mặt phẳng dữ liệu" và "mặt phẳng quản trị". Không dùng các từ ngữ sai lệch bản chất như "định tuyến qua pfSense" (đã được sửa thành "bố trí đi qua tường lửa pfSense").
8. **Địa chỉ mạng và giao diện:** Nhất quán giữa hai chương: Kali Linux (`192.168.56.10/24`, `eth0`), Windows Server (`192.168.56.20/24`, `Ethernet`), Host Adapter (`192.168.56.1/24`), pfSense Management (`192.168.57.2/24`, `em1`), Host Management (`192.168.57.1/24`).

*Kết luận thuật ngữ:* Các thuật ngữ và định danh kỹ thuật được sử dụng nhất quán, không phát hiện sự mâu thuẫn hay trôi dạt thuật ngữ trong phạm vi đã kiểm.

---

## 4. Kiểm toán các ranh giới kỹ thuật cốt lõi (Technical Truth Locks Audit)

Tất cả các ranh giới chân lý kỹ thuật bắt buộc đã được kiểm toán lập trình và đọc soát thực tế trong văn bản:

| Ranh giới kỹ thuật cốt lõi | Hiện diện trong Chương 2 | Hiện diện trong Chương 3 | Tuân thủ ngữ cảnh | Đánh giá |
|---|---|---|---|---|
| `445 OPEN != vulnerable` | Mục 2.3.3, Mục 2.6.3 | Mục 3.2.1, 3.3.1, 3.4.1, 3.4.2, 3.6 | Khẳng định cổng mở chỉ phản ánh khả năng tiếp cận, không đồng nghĩa với tồn tại lỗ hổng. | **PASS** |
| `SMBv1 enabled != MS17-010 confirmed` | Mục 2.3.3, Mục 2.6.3 | Mục 3.2.2, Mục 3.3.1, Mục 3.6 | Khẳng định hỗ trợ SMBv1 không đủ để kết luận máy dính MS17-010. | **PASS** |
| `SMBv1 disabled != PATCHED` | Mục 2.5.2, Mục 2.6.3 | Mục 3.4.1, Mục 3.4.2, Mục 3.6 | Khẳng định tắt SMBv1 chỉ đổi cờ dịch vụ, không thay thế bản vá mã nhị phân driver nhân. | **PASS** |
| `FILTERED != PATCHED` | Mục 2.5.3, Mục 2.6.3 | Mục 3.5.1, Mục 3.5.2, Mục 3.6 | Khẳng định chặn gói qua tường lửa không biến hệ điều hành thành đã vá lỗi. | **PASS** |
| `UNKNOWN != SAFE` | Mục 2.4.3, Mục 2.6.3 | Mục 3.3.2, Mục 3.4.2, Mục 3.5.2, Mục 3.6 | Khẳng định thiếu cảnh báo từ kịch bản quét từ xa không đồng nghĩa với an toàn. | **PASS** |
| **Tính độc lập hai trục thông tin** | Mục 2.4.3, Mục 2.6.3 | Mục 3.1.2, Mục 3.3.2, Mục 3.6 | Duy trì tách biệt giữa trục bản vá nội bộ (`UNPATCHED`) và trục rà quét từ xa (`UNKNOWN`). | **PASS** |
| **Case B: Cổng 139 không đo lại** | Bảng 2.4 | Bảng 3.5, Bảng 3.7 | Ghi nhận rõ "Không đo lại trong Case B", không tự bịa số liệu. | **PASS** |
| **Case B: Cổng 445 đo lại** | Mục 2.5.2 | Bảng 3.5, Bảng 3.7 | Ghi nhận `OPEN`, không bịa đặt trường `syn-ack` vì lệnh đo lại không có cờ `--reason`. | **PASS** |
| **Case C: Không dùng routing semantics** | Mục 2.1.2, Mục 2.5.3 | Mục 3.5, Mục 3.5.1 | Ghi nhận "bố trí đi qua cầu nối", không dùng "định tuyến qua". | **PASS** |
| **Case C: Bảo tồn ranh giới tên rule pfSense** | Mục 2.5.3 | Mục 3.5.2 (đoạn 276–277) | Phân tích khách quan sự lệch tên giữa ảnh giao diện và file nhật ký lượt chạy. | **PASS** |
| **Không sử dụng vũ khí hóa / exploit** | Toàn bộ Ch2 | Toàn bộ Ch3 | 0 lần xuất hiện: `meterpreter`, `reverse_tcp`, `exploit/windows/smb/ms17_010`. | **PASS** |
| **Không đồng bộ đồng hồ ảo chéo hệ thống** | Mục 2.6.3 | Mục 3.5.2 | Không giả định đồng bộ đồng hồ giữa Kali, pfSense và Windows. | **PASS** |

*Kết luận ranh giới kỹ thuật:* Tuân thủ nghiêm ngặt các ranh giới kỹ thuật đã khóa, không có vi phạm hay nới lỏng ranh giới trong phạm vi đã kiểm.

---

## 5. Đánh giá về sự trùng lặp và cô đọng văn phong (Duplication & Compression Assessment)

Khi đọc Chương 2 và Chương 3 như một tài liệu liền mạch:

- **Phân định rõ vai trò chức năng giữa hai chương:** Chương 2 tập trung trả lời câu hỏi *"Làm như thế nào, bằng công cụ gì, theo quy trình nào và tuân thủ ranh giới nào?"*; Chương 3 tập trung trả lời câu hỏi *"Dữ liệu thực tế thu được là gì, các hiện tượng quan sát được đối chiếu với nhau ra sao và rút ra được điều gì?"*.
- **Tính cô đọng trong tham chiếu:** Khi Chương 3 nhắc lại các thiết lập của Chương 2, văn bản chỉ dẫn chiếu ngắn gọn (ví dụ: *"theo mốc đã xác lập tại Mục 3.1"*, *"theo phương pháp đối chiếu đã trình bày tại Mục 2.5"*), hoàn toàn không chép lại các hướng dẫn cài đặt hay cấu hình môi trường dài dòng.
- **Tính hữu cơ của các mệnh đề ranh giới an toàn:** Các câu ranh giới cốt lõi (như `445 OPEN != vulnerable` hay `UNKNOWN != SAFE`) xuất hiện tại đúng điểm hội tụ phân tích của từng kịch bản cụ thể. Chúng đóng vai trò là "chốt chặn phương pháp luận" ngăn người đọc hiểu sai dữ liệu thực nghiệm, không tạo cảm giác lặp từ sáo rỗng hay văn bản ghi nhớ hành chính (QA memo).
- **Đánh giá trùng lặp:** Không phát hiện tình trạng trùng lặp đoạn văn hoặc sao chép ý thừa thãi. Mức độ cô đọng đạt chuẩn mực của một luận văn tốt nghiệp xuất sắc.

---

## 6. Đánh giá mạch đọc tự nhiên dưới góc nhìn Hội đồng chấm đồ án (Natural Student-Report Flow)

Dưới lăng kính của một giảng viên phản biện hoặc ủy viên hội đồng, tài liệu kết hợp Chương 2 và Chương 3 dẫn dắt câu chuyện nghiên cứu thực nghiệm rất mạch lạc và thuyết phục:

1. **Người đọc hiểu rõ hệ thống được xây dựng thế nào:** Một mô hình thực nghiệm ảo hóa độc lập, giới hạn kết nối trong lab, cấu hình chuẩn hóa, có cơ chế snapshot dự phòng đáng tin cậy (Mục 2.1, 2.2, 3.1).
2. **Người đọc thấy được quy trình đo đạc bài bản:** Bắt đầu từ diện mạo dịch vụ tổng quan (Kịch bản 1), tiến sâu vào thăm dò lỗ hổng chuyên biệt bằng NSE (Kịch bản 2), và ghi nhận khách quan kết quả chưa xác định mà không che giấu hay suy diễn (Mục 3.2, 3.3).
3. **Người đọc thấy rõ tác động của hai biện pháp can thiệp có kiểm soát:**
   - Trong Case B: can thiệp cấu hình máy chủ làm ẩn phương ngữ SMBv1 từ xa, nhưng dịch vụ vẫn mở cổng 445 và mã nguồn driver bên dưới vẫn chưa vá.
   - Trong Case C: can thiệp đường truyền mạng qua cầu nối pfSense làm cổng rơi vào trạng thái FILTERED và ghi nhận nhật ký chặn gói tin, nhưng máy chủ phía sau vẫn giữ nguyên cấu hình và mã lỗi.
4. **Người đọc nhận được kết luận khoa học có giá trị thực tiễn cao:** Bản so sánh tổng hợp tại Mục 3.6 phân định rạch ròi 4 tầng kỹ thuật (cấu hình dịch vụ, tính năng hệ thống, chính sách lọc mạng, bản vá nhân), giúp làm rõ vai trò và giới hạn của từng giải pháp bảo mật trong thực tế doanh nghiệp.

Toàn bộ tài liệu đọc lên như một công trình nghiên cứu nghiêm túc của sinh viên, văn phong học thuật tiếng Việt trong sáng, gãy gọn, giàu tính kỹ thuật và tự nhiên.

---

## 7. Đánh giá năng lực bảo vệ của sinh viên trước Hội đồng (Defense Readiness Assessment)

Bộ tài liệu Chương 2 + Chương 3 cung cấp cơ sở phương pháp và bằng chứng thực nghiệm đo đạc để sinh viên giải thích các câu hỏi liên quan đến phạm vi kỹ thuật của hai chương trước hội đồng:

| Câu hỏi chất vấn dự kiến của Hội đồng | Cơ sở lập luận và minh chứng đã sẵn sàng trong tài liệu | Đánh giá cơ sở trả lời |
|---|---|---|
| *1. Tại sao đề tài lại chọn mô hình Host-Only mà không cho máy ảo ra Internet?* | Mô hình Host-Only (Mục 2.1.2) chỉ sử dụng một card mạng Host-Only, không cấu hình NAT/Bridged và không có default route, qua đó giới hạn đường kết nối của hai máy ảo trong phạm vi mạng lab nội bộ và giảm thiểu các yếu tố ảnh hưởng từ mạng bên ngoài. | **Sẵn sàng trong phạm vi đồ án** |
| *2. Tại sao phải đo cả cổng 139 lẫn 445?* | Cổng TCP 139 là NetBIOS Session Service còn cổng TCP 445 là Direct-hosted SMB. Cả hai cổng đều thuộc diện mạo dịch vụ SMB được xác định trong phạm vi kịch bản của đề tài. Việc khảo sát cả hai cổng cung cấp bức tranh đo đạc dịch vụ từ xa đầy đủ theo đúng phạm vi kịch bản đã định nghĩa. | **Sẵn sàng trong phạm vi đồ án** |
| *3. Kịch bản 1 cho thấy SMBv1 được bật, vậy đã khẳng định được máy chủ dính MS17-010 chưa?* | Chưa. Việc bật SMBv1 chỉ là một quan sát về trạng thái hỗ trợ giao thức mạng (`SMBv1 enabled != MS17-010 confirmed`). Trạng thái hỗ trợ giao thức và trạng thái bản vá lỗ hổng là hai quan sát độc lập; việc phân loại chính xác tình trạng bản vá nội bộ phải được xác lập riêng biệt qua kiểm tra tệp nhị phân và danh mục hotfix. | **Sẵn sàng trong phạm vi đồ án** |
| *4. Tại sao kịch bản Nmap NSE MS17-010 không báo VULNERABLE mà lại trả về không có kết quả (UNKNOWN)?* | Trong Kịch bản 2, công cụ Nmap hoàn tất phiên quét nhưng đầu ra không xuất hiện khối kết luận `Host script results:`. Đề tài phân loại kết quả này là `UNKNOWN / NO USABLE SCRIPT RESULT`. Dữ liệu thực nghiệm không xác lập nguyên nhân của việc thiếu vắng kết luận này; đề tài tuân thủ nguyên tắc `UNKNOWN != SAFE`, không ngộ nhận trạng thái chưa xác định là an toàn. | **Sẵn sàng trong phạm vi đồ án** |
| *5. Vô hiệu hóa SMBv1 ở Case B có giải quyết triệt để MS17-010 không?* | Không triệt để. Dữ liệu thực nghiệm Case B ghi nhận cấu hình máy chủ thay đổi sang `EnableSMB1Protocol=False`, danh mục phương ngữ đo lại từ xa không còn `NT LM 0.12`, nhưng cổng TCP 445 vẫn ở trạng thái OPEN, kết quả quét MS17-010 từ xa duy trì UNKNOWN và trạng thái bản vá nội bộ vẫn là UNPATCHED (`SMBv1 disabled != PATCHED`). Đề tài không suy diễn hành vi đàm phán hay việc chặn đường tấn công ngoài các dữ kiện đã quan sát. | **Sẵn sàng trong phạm vi đồ án** |
| *6. Tường lửa pfSense ở Case C báo FILTERED có đồng nghĩa với máy chủ đã an toàn không?* | Không. Từ trạm Kali Linux, các cổng TCP 139/445 được ghi nhận ở trạng thái FILTERED (no-response) và pfSense ghi nhận nhật ký chặn các gói tin TCP SYN tương ứng. Tuy nhiên, trên máy chủ Windows, cấu hình dịch vụ và trạng thái bản vá nội bộ vẫn giữ nguyên UNPATCHED (`FILTERED != PATCHED`). Do đó trạng thái FILTERED từ xa không đồng nghĩa với việc máy chủ đã được vá hay an toàn. | **Sẵn sàng trong phạm vi đồ án** |
| *7. Tại sao đề tài không chạy mã khai thác thực tế (exploit RCE / Meterpreter)?* | Phạm vi thực nghiệm được phê duyệt của đề tài là đo đạc bề mặt tấn công phi xâm nhập và ghi nhận phản hồi dịch vụ; việc thực thi payload khai thác xâm nhập nằm ngoài phạm vi thực nghiệm đã được phê duyệt của đồ án. | **Sẵn sàng trong phạm vi đồ án** |
| *8. Bảng so sánh 3.7 được tổng hợp dựa trên cơ sở nào?* | Toàn bộ 7 hàng so sánh trong Bảng 3.7 được tổng hợp trực tiếp từ các dữ liệu định lượng và trạng thái đã đo đạc tại Mục 3.1, 3.2, 3.3, 3.4 và 3.5, phản ánh đúng các quan sát thực nghiệm mà không bổ sung nhận định suy diễn ngoài phạm vi. | **Sẵn sàng trong phạm vi đồ án** |

*Kết luận năng lực bảo vệ:* Sản phẩm cung cấp đầy đủ cơ sở phương pháp và minh chứng đo đạc thực nghiệm, giúp sinh viên có cơ sở vững chắc để giải thích rõ các lựa chọn thiết kế, kết quả đo đạc và giới hạn kỹ thuật trong phạm vi Chương 2–3 trước hội đồng.

---

## 8. Kiểm tra cấu trúc hình thức và quy chuẩn trình bày tài liệu (Product Format Checks)

- **Thứ tự chương:** Chương 2 (Trang 1–12) nằm trước Chương 3 (Trang 13–44).
- **Ngắt trang giữa hai chương:** Chương 3 bắt đầu trọn vẹn ở đầu trang mới (Trang 13).
- **Cấu trúc kiểu dáng tiêu đề:** 2 `Heading 1` (outline level 0), 14 `Heading 2` (outline level 1), 30 `Heading 3` (outline level 2) đều là kiểu dáng tiêu đề gốc của Microsoft Word.
- **Hệ thống bảng biểu:** Đúng 11 bảng (Bảng 2.1–2.4, Bảng 3.1–3.7), đều có tên bảng in đậm phía trên, viền thanh thoát, tiêu đề lặp lại sạch sẽ trên các trang tràn (`tblHeader`), dòng không bị xé (`cantSplit`).
- **Hệ thống hình ảnh:** Đúng 13 hình (Hình 2.1–2.2, Hình 3.1–3.11), sắc nét, căn giữa, chú thích in đậm phía dưới hình và cùng trang với hình (`keep_with_next`).
- **Cổng cấm bảng/hình:** Hoàn toàn **không có Bảng 3.8 và Hình 3.12**.
- **Cổng cấm chương ngoài phạm vi:** Hoàn toàn **không có Chương 1, Chương 4, hay lời mở đầu/lời cảm ơn**.
- **Kiểm soát rò rỉ nội bộ:** Hoàn toàn **không có dấu vết quy trình quản trị nội bộ** (như `USER_APPROVED`, `LOCKED`, `DEC`, `BLOCKER`, `X7...`) trong phần văn bản học thuật dành cho người đọc.
- **Thông số lề trang:** Đạt chuẩn HUIT 2024: Trên 3.5 cm, Dưới 3.0 cm, Trái 3.5 cm, Phải 2.0 cm.

---

## 9. Danh mục vấn đề phát hiện và Phán quyết thẩm định cuối cùng (Findings & Verdict)

### Danh mục Blocker (Vấn đề gây tắc nghẽn)
- **Số lượng Blocker phát hiện:** **0 (KHÔNG CÓ)**.
- Không có bất kỳ sai lệch nào về phương pháp, kết quả, thuật ngữ, sự kiện kỹ thuật hay quy chuẩn trình bày Word.

### Phán quyết thẩm định (Final Review Verdict)

Theo thang đánh giá quy định tại prompt X7J:
- [x] **`PASS`**
- [ ] `REVISE_MINOR_BLOCKING`
- [ ] `REVISE_BLOCKING`

### Lý do phán quyết PASS
1. **Tính nhất quán chặt chẽ giữa Phương pháp và Kết quả:** Chương 2 chuẩn bị đầy đủ nền tảng phương pháp cho Chương 3; Chương 3 báo cáo đầy đủ và trung thực các kết quả đo đạc tương ứng với thiết kế.
2. **Kỷ luật kỹ thuật và phân định phương pháp luận:** 5 ranh giới kỹ thuật cốt lõi được bảo toàn, phân định rạch ròi giữa quan sát từ xa và cấu hình nội bộ.
3. **Văn phong học thuật chuẩn mực, mạch lạc:** Không trùng lặp nội dung, cấu trúc khoa học tự nhiên, phù hợp với yêu cầu đồ án tốt nghiệp.
4. **Năng lực bảo vệ được bảo đảm trong phạm vi đồ án:** Cung cấp cơ sở phương pháp và minh chứng giúp sinh viên giải thích rõ các lựa chọn thiết kế, kết quả đo đạc và giới hạn kỹ thuật trong phạm vi Chương 2–3.
5. **Chất lượng tệp Word hoàn thiện:** Đạt quy chuẩn HUIT 2024, bảo toàn nguyên vẹn mã băm `3c9ac6b6bfa1d259f92856a6c6b48ec398178e927f9beb06f5c0c37749dd3db2`.

Bản rà soát R2 sau khi hiệu chỉnh giới hạn lập luận sẵn sàng chuyển sang bước thẩm định độc lập tiếp theo ở trạng thái **`X7J_R2_READY_FOR_INDEPENDENT_REVIEW`**.
