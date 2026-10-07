# CHƯƠNG 3 REDESIGN — EVIDENCE & VISUAL BLUEPRINT (R2)

- **Cổng trạng thái đề xuất:** `R3_0_REVISE_BLOCKING / PENDING_R2_INDEPENDENT_REVIEW` (Chờ thẩm định độc lập R2; chưa chuyển sang R3-1).
- **Phiên bản tài liệu:** `Revision R2` (Hiệu chỉnh toàn diện khắc phục các điểm tồn tại F01–F09 theo Báo cáo thẩm định độc lập R1 tại `work/do-an/R3_0_EVIDENCE_VISUAL_BLUEPRINT_EXTERNAL_REVIEW_R1.md`).
- **Candidate R1 nguồn:** `4f9d3f059f96d8b44ef6c83e0c2b20301245ce3e`.
- **Tài liệu căn cứ lộ trình:** `work/do-an/ROADMAP_CH3_REDESIGN_EVIDENCE_FIRST_2026_10_07.md`.
- **Nhánh làm việc canonical:** `feature/ch3-redesign-evidence-first-r1`.
- **Mục tiêu tài liệu:** Thiết kế chi tiết từng đề mục của Chương 3 theo kiến trúc mới (3.1 đến 3.8), xác định câu hỏi dẫn dắt, thông điệp cốt lõi, bảng biểu, hệ thống 14 hình ảnh đề xuất (Evidence, Comparison, Explanatory), hướng dẫn cắt cúp chuẩn xác theo ảnh thật, ghép panel, ranh giới caption và các tuyên bố bị cấm.
- **Ràng buộc tuyệt đối:** Không tự ý soạn văn xuôi (Zero Prose for Chapter 3 Draft), không sửa `CHAPTER_2.md` hay `CHAPTER_3_DRAFT_R2.md`, không dựng file Word DOCX, không mở Chương 4. Toàn bộ số hiệu bảng/hình mang trạng thái `PROPOSED / WAITING EXTERNAL REVIEW`.

---

## 1. NGUYÊN TẮC THIẾT KẾ THỊ GIÁC VÀ TRUY VẾT BẰNG CHỨNG

1. **Phân loại vai trò hình ảnh (3 loại hình chuẩn mực):**
   - **Evidence Figure (7 hình):** Ảnh chụp màn hình bằng chứng trực tiếp chứng minh một quan sát kỹ thuật cụ thể (terminal output, cấu hình hệ điều hành, nhật ký tường lửa).
   - **Comparison Figure (4 hình):** Ghép hoặc xếp đặt nhiều bằng chứng trực tiếp đã được kiểm chứng (Before vs. After, Local vs. Remote, Sequential Action) để người đọc nhìn thấy trực quan sự thay đổi hoặc sự đối lập giữa hai góc nhìn. Mọi nhãn tổng hợp (như "Remote", "Local") phải được đặt bên ngoài pixel bằng chứng gốc. Tuyệt đối không chỉnh sửa nội dung bên trong từng ảnh thành phần.
   - **Explanatory Figure (3 hình):** Sơ đồ kiến trúc/quy trình do báo cáo dựng từ các sự thật kỹ thuật đã được xác minh (như sơ đồ luồng thực nghiệm hai nhánh, mô hình cầu nối pfSense Transparent Bridge, phân định hai vị trí can thiệp độc lập). Phải ghi rõ là sơ đồ giải thích, không giả dạng làm ảnh chụp màn hình bằng chứng.
2. **Triết lý tận dụng ảnh:** Tận dụng tối đa giá trị giải thích và chứng minh của bộ bằng chứng 34 ảnh canonical. Loại bỏ tư duy máy móc "khống chế tối đa 8 ảnh", nhưng kiên quyết chống "screenshot spam". Mỗi hình đưa vào bản thảo bắt buộc phải có một chức năng lập luận rõ ràng.
3. **Thứ bậc ưu tiên bằng chứng:**
   $$\text{Direct Raw / Local / Visual} > \text{Metadata / Lineage} > \text{Historical / Supporting} > \text{Old Report Prose}$$
4. **Phân định rõ ràng 83 tệp staging:**
   - 78 tệp chứng cứ sơ cấp / trực tiếp (`PRIMARY_RAW`: 39, `PRIMARY_VISUAL`: 33, `PRIMARY_LOCAL_STATE`: 5, `PRIMARY_VISUAL_WITH_BOUNDED_CONFLICT`: 1).
   - 5 tệp chứng cứ thứ cấp (`SECONDARY_META`: 4 run manifests, `SECONDARY_META_CLOSURE`: 1 báo cáo trạng thái Section 21 `RUN4_PAUSE_STATE_REPORT.txt`).
5. **Bảo toàn 5 tiên đề chân lý kỹ thuật:**
   - $\text{TCP 445 OPEN} \neq \text{vulnerable to MS17-010}$
   - $\text{SMBv1 enabled} \neq \text{MS17-010 confirmed}$
   - $\text{UNKNOWN} \neq \text{SAFE}$
   - $\text{FILTERED} \neq \text{PATCHED}$
   - $\text{SMBv1 disabled} \neq \text{PATCHED}$
   - Trạng thái bản vá nội bộ (`UNPATCHED`) hoàn toàn độc lập với phán quyết quét từ xa (`UNKNOWN` / `FILTERED`).

---

## 2. BLUEPRINT CHI TIẾT TỪNG PHẦN (SECTIONS 3.1 ĐẾN 3.8)

---

### MỤC 3.1. MỤC TIÊU VÀ TỔ CHỨC THỰC NGHIỆM

#### 3.1.1. Mục tiêu kiểm chứng
1. **Đề mục:** `3.1.1. Mục tiêu kiểm chứng`
2. **Câu hỏi người đọc:** *Tại sao phải tiến hành thực nghiệm này và tác giả muốn kiểm chứng điều gì cụ thể?*
3. **Thông điệp chính:** Thực nghiệm không nhằm mục đích biểu diễn tấn công khai thác lỗ hổng (exploit/RCE), mà nhằm xác lập một quy trình đo đạc an toàn, có kiểm soát để phân biệt rạch ròi 4 tầng dữ kiện: khả năng tiếp cận mạng (reachability), trạng thái giao thức SMB (protocol state), tín hiệu thăm dò từ xa (remote detection signal), và trạng thái bản vá hệ điều hành (local patch ground truth); đồng thời kiểm chứng thực nghiệm tác động của hai giải pháp phòng thủ giảm thiểu rủi ro độc lập (vô hiệu hóa SMBv1 tại máy chủ và kiểm soát truy cập bằng pfSense trên đường truyền mạng).
4. **Technical facts được phép dùng:**
   - Bám sát Mục tiêu O3, O4 và Câu hỏi nghiên cứu RQ3, RQ4 đã khóa trong `RESEARCH_MAP.md`.
   - 4 biến kỹ thuật cần phân tách: cổng mở, phương ngữ hỗ trợ, kết quả script Nmap, phiên bản tệp driver `srv.sys`.
   - Hai biện pháp can thiệp phòng thủ trong phạm vi: Case B (cấu hình máy chủ Windows) và Case C (tường lửa cầu nối pfSense).
   - Biện pháp cập nhật bản vá hệ điều hành là mốc đối chiếu lý thuyết được thảo luận ở Chương 4, không nằm trong các ca đo đạc can thiệp của Chương 3 (không dùng nhãn "Case A" làm ca thực nghiệm canonical).
5. **Direct evidence tương ứng:** Bám sát thiết kế phương pháp đã khóa tại Chương 2 (Mục 2.1.1, Mục 2.5.1, Bảng 2.4).
6. **Supporting evidence:** `work/do-an/RESEARCH_MAP.md`, `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`.
7. **Bảng cần dùng:** Không dùng bảng riêng (nội dung dẫn nhập định hướng).
8. **Hình cần dùng:** Không dùng hình tại tiểu mục này (hình quy trình nằm ở 3.1.2).
9. **Loại hình:** Không áp dụng.
10. **Hướng dẫn crop:** Không áp dụng.
11. **Ghép panel:** Không áp dụng.
12. **Caption dự kiến:** Không áp dụng.
13. **Ranh giới caption:** Không áp dụng.
14. **Ranh giới kết luận section:** Chỉ nêu mục tiêu và phạm vi đo đạc đã được phê duyệt; không đưa ra kết luận trước về tính hiệu quả hay mức độ an toàn của bất kỳ giải pháp nào.
15. **Overclaim bị cấm:**
   - CẤM tuyên bố thực nghiệm nhằm "chứng minh khả năng khai thác thành công MS17-010".
   - CẤM tuyên bố đo đạc nhằm "đánh giá toàn diện mọi giải pháp bảo mật trong thực tế".
   - CẤM gọi việc cập nhật bản vá là một ca thực nghiệm đã đo (không có Case A experiment).
16. **Nối sang phần kế tiếp:** Nêu rõ để đạt được các mục tiêu kiểm chứng trên, toàn bộ quy trình đo đạc được tổ chức thành một chuỗi luồng thực nghiệm mạch lạc với hai nhánh can thiệp độc lập, được mô tả chi tiết tại Mục 3.1.2.

---

#### 3.1.2. Luồng thực nghiệm
1. **Đề mục:** `3.1.2. Luồng thực nghiệm`
2. **Câu hỏi người đọc:** *Các bước thực nghiệm được tổ chức theo trình tự logic nào và tại sao lại đi theo thứ tự đó?*
3. **Thông điệp chính:** Toàn bộ thực nghiệm được tổ chức theo tiến trình khoa học gồm hai giai đoạn lớn: (1) Xác lập đường cơ sở (Baseline, Kịch bản 1 khảo sát dịch vụ, Kịch bản 2 kiểm tra dấu hiệu MS17-010) $\to$ (2) Hai nhánh can thiệp giảm thiểu độc lập xuất phát từ đường cơ sở: Nhánh 1 can thiệp máy chủ (Case B) và Nhánh 2 can thiệp đường mạng (Case C), kết thúc bằng việc đặt các trạng thái cạnh nhau để đối chiếu đa chiều. Giữa hai nhánh can thiệp, môi trường được hoàn nguyên về mốc xuất phát thông qua snapshot `Before Demo` để bảo đảm tính độc lập của các biến thực nghiệm.
4. **Technical facts được phép dùng:**
   - Chuỗi đo đạc kế thừa từ thiết kế Chương 2 (Mục 2.3, 2.4, 2.5).
   - Hai nhánh can thiệp độc lập: Case B tác động cấu hình máy chủ; Case C tác động đường truyền mạng qua pfSense Transparent Bridge.
   - Case C không kế thừa cấu hình của Case B; máy chủ trong Case C duy trì trạng thái mốc chuẩn (`SMB1=True`, `SMB2=True`, `UNPATCHED`).
   - Mốc phục hồi: Snapshot `Before Demo` chụp trên các máy ảo ở trạng thái tắt máy (ngữ cảnh phục hồi có căn cứ tệp snapshot, không tự đặt mốc thời gian rollback cụ thể).
   - Mỗi giai đoạn can thiệp đều có bước đo đạc lại (retest) từ cùng trạm kiểm thử Kali Linux để bảo đảm tính so sánh đối chứng.
5. **Direct evidence tương ứng:** `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`, `work/do-an/CHAPTER_2.md` (Mục 2.1.2, 2.5.1).
6. **Supporting evidence:** `baseline/Before_Demo_Snapshots.txt`.
7. **Bảng cần dùng:** Không dùng bảng riêng (sơ đồ trực quan đảm nhiệm vai trò này).
8. **Hình cần dùng:** **Hình 3.1** (Sơ đồ tổng thể luồng thực nghiệm hai nhánh độc lập).
9. **Loại hình:** **Explanatory Figure** (Sơ đồ giải thích luồng quy trình thực nghiệm).
10. **Hướng dẫn crop:** Không crop ảnh chụp màn hình; sơ đồ được dựng dạng vector/sơ đồ khối chuẩn khoa học.
11. **Ghép panel:** Dựng sơ đồ khối thể hiện rõ:
    - Khối 1: Xác lập mốc chuẩn xuất phát (Baseline).
    - Khối 2: Khảo sát diện mạo dịch vụ SMB từ xa (Kịch bản 1).
    - Khối 3: Kiểm tra dấu hiệu MS17-010 và đối chiếu chéo Remote/Local (Kịch bản 2).
    - Phân nhánh độc lập:
      * Nhánh A (Can thiệp máy chủ): Case B Vô hiệu hóa SMBv1 $\to$ Kiểm tra cục bộ $\to$ Đo lại từ xa $\to$ Đối chiếu Before/After Case B.
      * Mốc phục hồi: Hoàn nguyên snapshot `Before Demo` về trạng thái xuất phát.
      * Nhánh B (Can thiệp đường mạng): Case C Bố trí pfSense Bridge $\to$ Thiết lập chính sách lọc $\to$ Đo lại từ xa $\to$ Đối chiếu nhật ký tường lửa và trạng thái máy chủ (Windows giữ nguyên baseline).
    - Khối tổng hợp: Đối chiếu đa chiều 3 trạng thái thực nghiệm (Mục 3.7).
12. **Caption dự kiến:** `Hình 3.1. Sơ đồ quy trình thực nghiệm kiểm thử dịch vụ SMB và hai nhánh can thiệp giảm thiểu rủi ro độc lập`
13. **Ranh giới caption:** Caption chỉ nêu chức năng sơ đồ là minh họa quy trình tổ chức thực nghiệm hai nhánh độc lập; không đưa ra kết luận kỹ thuật trong chú thích.
14. **Ranh giới kết luận section:** Khẳng định luồng thực nghiệm cung cấp khung phương pháp nhất quán để tiến hành thu thập dữ liệu khách quan bắt đầu từ việc xác lập trạng thái mốc chuẩn ban đầu.
15. **Overclaim bị cấm:**
    - CẤM mô tả quy trình thực nghiệm như một đường thẳng nối tiếp trong đó Case C kế thừa kết quả của Case B.
    - CẤM tự ý bịa đặt mốc thời gian rollback cụ thể không có trong nhật ký.
    - CẤM gọi pfSense là router hay thiết bị định tuyến trong sơ đồ luồng.
16. **Nối sang phần kế tiếp:** Để có cơ sở đánh giá mọi biến đổi kỹ thuật, bước đầu tiên bắt buộc phải thực hiện là xác lập mốc tham chiếu xuất phát của hệ thống, được trình bày tại Mục 3.2.

---

### MỤC 3.2. XÁC LẬP TRẠNG THÁI BAN ĐẦU CỦA HỆ THỐNG

#### 3.2.1. Trạng thái mạng và dịch vụ SMB
1. **Đề mục:** `3.2.1. Trạng thái mạng và dịch vụ SMB`
2. **Câu hỏi người đọc:** *Trước khi thực hiện bất kỳ lệnh quét nào, hệ thống máy chủ và mạng lab đang ở trạng thái cấu hình như thế nào?*
3. **Thông điệp chính:** Trạng thái xuất phát được kiểm toán nghiêm ngặt: hai máy ảo hoạt động trong phân đoạn mạng Host-Only cô lập (`192.168.56.0/24`), không default route; trên máy chủ Windows Server 2012 R2, dịch vụ chia sẻ tệp `LanmanServer` đang chạy, tính năng `FS-SMB1` đã cài đặt, cả SMBv1 và SMBv2 đều được kích hoạt ở cấu hình cục bộ, hai cờ ký số nội bộ mang giá trị False (độc lập với quan sát từ xa), cổng TCP 139 và 445 đang lắng nghe, và Windows Firewall được bật với quy tắc tùy biến chỉ cho phép duy nhất IP của Kali Linux kết nối vào.
4. **Technical facts được phép dùng:**
   - Kali IP `192.168.56.10/24` (`eth0`), Windows IP `192.168.56.20/24` (`Ethernet`), Host Adapter `192.168.56.1/24`.
   - Cả hai máy ảo không có default route; không card NAT, không Bridged.
   - `LanmanServer` Running, chế độ Automatic.
   - `FS-SMB1` Installed; `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`.
   - Cục bộ: `EnableSecuritySignature : False`, `RequireSecuritySignature : False` (giữ nguyên vẹn, độc lập với kết quả quét mạng từ xa).
   - Socket cục bộ lắng nghe: TCP 445 (`::`), TCP 139 (`192.168.56.20`).
   - Windows Firewall: cả 3 profile Domain, Private, Public đều `Enabled=True`.
   - 16 quy tắc mặc định `File and Printer Sharing` đều `False` (bị tắt).
   - Quy tắc tùy biến `ATTT Lab SMB 139-445` (TCP 139, 445, Inbound, Allow, RemoteAddress duy nhất `192.168.56.10`).
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/baseline/Final_PreDemo_Audit.txt` (PRIMARY_LOCAL_STATE).
   - `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png` (PRIMARY_VISUAL).
6. **Supporting evidence:**
   - `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_02_Firewall.png` (PRIMARY_VISUAL — lưu giữ đối soát quy tắc tường lửa cho Bảng 3.1).
   - `work/do-an/chapter3/evidence/baseline/Windows_FirewallPrep_Final.txt`, `VirtualBox_HostOnly_Config.txt`, `Windows_FirewallPrep_04_Scope.png`.
7. **Bảng cần dùng:** **Bảng 3.1** (Bảng thông số kiểm toán mạng, dịch vụ SMB và Windows Firewall mốc xuất phát).
8. **Hình cần dùng:** **Hình 3.2** (Trạng thái cấu hình mạng, dịch vụ LanmanServer và các cổng lắng nghe trên máy chủ mục tiêu).
9. **Loại hình:** **Evidence Figure** (Ảnh bằng chứng trực tiếp từ PowerShell cục bộ).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/baseline/Windows_PreDemo_01_Network_SMB.png` (đã có bản trình bày chuẩn hóa tại `chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png`).
    - Khu vực giữ: Giao diện PowerShell hiển thị `Get-NetIPAddress` (.56.20/24), `Get-Service LanmanServer` (Running), `Get-WindowsFeature FS-SMB1` (Installed), và `netstat -ano` (cổng 139, 445 Listen).
    - Không được che: Địa chỉ IP 192.168.56.20, trạng thái Running của dịch vụ, cổng lắng nghe 445 và 139.
11. **Ghép panel:** Không ghép; dùng độc lập làm minh chứng cho cấu hình dịch vụ nội bộ. Ảnh `Windows_PreDemo_02_Firewall.png` chuyển thành supporting visual do Bảng 3.1 đã phản ánh đầy đủ thông số tường lửa.
12. **Caption dự kiến:** `Hình 3.2. Trạng thái cấu hình mạng, dịch vụ LanmanServer và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm`
13. **Ranh giới caption:** Caption chỉ mô tả cấu hình mạng, dịch vụ và trạng thái socket đang lắng nghe trên máy chủ; không kết luận về khả năng tiếp cận từ bên ngoài.
14. **Ranh giới kết luận section:** Kết luận rằng dịch vụ SMB đã sẵn sàng trên máy chủ và cổng lắng nghe đã mở cục bộ, được bảo vệ bởi Windows Firewall giới hạn cho trạm kiểm thử. Trạng thái lắng nghe cục bộ không đồng nghĩa với khả năng tiếp cận qua mạng (phải đo từ xa).
15. **Overclaim bị cấm:**
    - CẤM suy diễn cổng lắng nghe cục bộ đồng nghĩa với việc cổng mở hoàn toàn trên mạng.
    - CẤM tuyên bố môi trường cô lập tuyệt đối 100% không thể rò rỉ lưu lượng (chỉ khẳng định cấu hình lab không có default route và dùng Host-Only NIC).
    - CẤM suy diễn thuộc tính ký số nội bộ mang giá trị False đồng nghĩa với việc mạng ngoài cũng thấy signing disabled.
16. **Nối sang phần kế tiếp:** Bên cạnh cấu hình dịch vụ và mạng, yếu tố quyết định đến tính chất an ninh của máy chủ mục tiêu là trạng thái bản vá hệ điều hành, được xác lập tại Mục 3.2.2.

---

#### 3.2.2. Trạng thái bản vá MS17-010
1. **Đề mục:** `3.2.2. Trạng thái bản vá MS17-010`
2. **Câu hỏi người đọc:** *Làm thế nào để biết chính xác máy chủ Windows Server 2012 R2 đã được vá lỗ hổng MS17-010 hay chưa trước khi thử nghiệm?*
3. **Thông điệp chính:** Trạng thái bản vá nội bộ được xác lập độc lập và khách quan dựa trên hai tiêu chí kỹ thuật: (1) Số phiên bản nhị phân của tệp driver nhân `srv.sys` (`6.3.9600.16421`), thấp hơn ngưỡng tối thiểu đã vá theo tài liệu chính thức của Microsoft (`6.3.9600.18604`); và (2) Danh mục hotfix cục bộ (`Get-HotFix`) không chứa các bản cập nhật bảo mật liên quan (KB4012213 hoặc KB4012216). Máy chủ được phân loại chính xác là **UNPATCHED**.
4. **Technical facts được phép dùng:**
   - Đường dẫn driver: `C:\Windows\System32\drivers\srv.sys`.
   - Chuỗi `FileVersion` hiển thị trong console: `6.3.9600.16384 (winblue_rtm.130821-1623)`.
   - Giá trị phiên bản số nhị phân: ghép 4 trường số `FileMajorPart` (6), `FileMinorPart` (3), `FileBuildPart` (9600), `FilePrivatePart` (16421) $\to$ `6.3.9600.16421`.
   - Ngưỡng bản vá Microsoft MS17-010 cho Windows Server 2012 R2: tối thiểu `6.3.9600.18604` (căn cứ tài liệu hỗ trợ chính thức Microsoft Support Article 4023262, mã nguồn `S032` trong `SOURCE_LEDGER.md`, thuộc bản tin bảo mật MS17-010 `S005`, ứng với gói cập nhật KB4012213 Security Only hoặc KB4012216 Monthly Rollup).
   - So sánh số học: $6.3.9600.16421 < 6.3.9600.18604$.
   - Danh mục `Get-HotFix` có 6 bản cập nhật năm 2014 (KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621); hoàn toàn thiếu bản vá MS17-010.
   - Phân loại cục bộ: **UNPATCHED**.
   - Mốc phục hồi: Snapshot `Before Demo` chụp trên cả 2 VM ở trạng thái tắt máy.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png` (PRIMARY_VISUAL — hiển thị cửa sổ PowerShell với chuỗi FileVersion và lệnh ghép 4 trường số nhị phân).
   - `work/do-an/chapter3/evidence/baseline/Windows_MS17010_02_Hotfix.png` (PRIMARY_VISUAL — hiển thị danh mục 6 hotfix từ PowerShell).
6. **Supporting evidence:**
   - `work/do-an/chapter3/evidence/baseline/MS17-010_Official_Mapping.txt` (PRIMARY_LOCAL_STATE — tài liệu điều hướng nội bộ).
   - Nguồn thẩm quyền ngoài chính thức: `S032` (Microsoft Support Article 4023262) và `S005` (Microsoft Security Bulletin MS17-010) trong `SOURCE_LEDGER.md`.
   - `baseline/Before_Demo_Snapshots.txt`, `Windows_Baseline_01_Winver.png`.
7. **Bảng cần dùng:** **Bảng 3.2** (Đối chiếu phiên bản driver `srv.sys`, danh mục hotfix và mốc phục hồi hệ thống).
8. **Hình cần dùng:** **Hình 3.3** (Minh chứng phiên bản tệp `srv.sys` và danh mục hotfix trên máy chủ Windows Server 2012 R2).
9. **Loại hình:** **Comparison Figure** (Ghép 2 panel chứng cứ cục bộ: Panel A hiển thị cửa sổ PowerShell đo tệp driver `srv.sys` + Panel B hiển thị danh mục Hotfix).
10. **Hướng dẫn crop chuẩn xác (F01):**
    - **Panel A:** Tệp nguồn canonical là ảnh cửa sổ console PowerShell `work/do-an/chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png` (tuyệt đối không mô tả là hộp thoại Explorer GUI hay tab Properties/Details). Khu vực crop bắt buộc phải giữ:
      1) Lệnh và kết quả hiển thị chuỗi `FileVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)` và `ProductVersion`;
      2) Lệnh trích xuất 4 trường số (`FileMajorPart`, `FileMinorPart`, `FileBuildPart`, `FilePrivatePart`) và dòng in kết quả phiên bản số nhị phân `6.3.9600.16421`.
    - **Panel B:** Cắt cửa sổ PowerShell hiển thị lệnh `Get-HotFix` (`Windows_MS17010_02_Hotfix.png`), hiển thị danh sách 6 hotfix năm 2014.
    - Không được che: Chuỗi FileVersion hiển thị, kết quả phiên bản số `6.3.9600.16421`, và danh sách mã KB trên Panel B.
    - Phân biệt rõ: ảnh gốc canonical trong `evidence/baseline/`, bản trình bày cũ `presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png`, và panel đề xuất mới của Hình 3.3.
11. **Ghép panel:** Ghép dọc hoặc ngang hai panel tạo thành hình chứng cứ toàn vẹn về trạng thái bản vá nội bộ.
12. **Caption dự kiến:** `Hình 3.3. Phiên bản tệp driver srv.sys hiển thị và số nhị phân cùng danh mục hotfix ghi nhận trên máy chủ mục tiêu`
13. **Ranh giới caption:** Chú thích chỉ mô tả chuỗi phiên bản hiển thị, phiên bản số trích xuất và danh sách hotfix có trên hệ thống; việc kết luận máy chủ UNPATCHED dựa trên phép đối chiếu phiên bản số nhị phân và tài liệu chính thức của Microsoft (S032) được trình bày trong bảng và văn bản phân tích.
14. **Ranh giới kết luận section:** Khẳng định máy chủ mục tiêu ở trạng thái UNPATCHED đối với MS17-010. Đây là sự thật nội bộ (local ground truth) và không tự sinh ra một phán quyết từ xa khi chưa tiến hành đo đạc mạng.
15. **Overclaim bị cấm:**
    - CẤM nhầm lẫn giữa chuỗi hiển thị `6.3.9600.16384` và phiên bản số nhị phân `6.3.9600.16421`.
    - CẤM tuyên bố chỉ riêng chuỗi FileVersion hiển thị là đủ để kết luận UNPATCHED mà phải dựa trên phiên bản số nội bộ + danh mục hotfix + nguồn chính thức Microsoft (S032).
    - CẤM coi file mapping nội bộ `MS17-010_Official_Mapping.txt` là nguồn thẩm quyền ngoài thay thế cho Microsoft Support.
    - CẤM tuyên bố trạng thái UNPATCHED đồng nghĩa với việc đã khai thác thành công.
16. **Nối sang phần kế tiếp:** Sau khi hoàn tất xác lập mốc xuất phát nội bộ, hệ thống bước vào Kịch bản 1 nhằm khảo sát diện mạo dịch vụ SMB nhìn từ góc độ trạm kiểm thử mạng ngoài, được trình bày tại Mục 3.3.

---

### MỤC 3.3. KHẢO SÁT DỊCH VỤ SMB TỪ TRẠM KALI LINUX

#### 3.3.1. Phát hiện máy chủ và khả năng tiếp cận SMB
1. **Đề mục:** `3.3.1. Phát hiện máy chủ và khả năng tiếp cận SMB`
2. **Câu hỏi người đọc:** *Từ trạm kiểm thử Kali Linux, máy chủ mục tiêu có hiện diện trên mạng không và các cổng dịch vụ SMB có tiếp cận được không?*
3. **Thông điệp chính:** Trạm Kali Linux xác nhận sự hiện diện trực tuyến của máy chủ `192.168.56.20` qua giao thức ARP (độ trễ $0.00040\,\text{s}$); quét cổng xác nhận cả hai cổng TCP 139 (`netbios-ssn`) và TCP 445 (`microsoft-ds`) đều ở trạng thái `open`, tiếp nhận kết nối TCP và phản hồi cờ `syn-ack` với giá trị TTL 128.
4. **Technical facts được phép dùng:**
   - Quét khám phá dải mạng B2 (`b2_host_discovery.nmap`): phát hiện 4 IP (.1, .10, .20, .100). Host `.56.100` mang nhãn bắt buộc là `UNKNOWN identity`.
   - Kiểm tra trực tuyến B3 (`b3_target_alive.nmap`): `192.168.56.20` phản hồi trực tuyến (`Host is up`).
   - Quét cổng SMB B4 (`b4_smb_ports.nmap`): cổng 139 và 445 đều `open`, lý do phản hồi `syn-ack ttl 128`.
   - Không sử dụng cờ `-Pn` trong quy trình đo đạc.
   - Tiên đề: `445 OPEN != vulnerable`. Cổng mở chỉ chứng minh khả năng tiếp cận dịch vụ qua mạng.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/scenario1/b2_host_discovery.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario1/b3_target_alive.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario1/b4_smb_ports.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario1/Scenario1_B4_SMB_Ports.png` (PRIMARY_VISUAL).
6. **Supporting evidence:** `scenario1/Scenario1_Run_Manifest.txt` (SECONDARY_META), `Kali_to_Windows_Connectivity.png`.
7. **Bảng cần dùng:** Dữ liệu B2–B4 được tích hợp vào Bảng 3.3 ở Mục 3.3.3.
8. **Hình cần dùng:** **Hình 3.4** (Kết quả quét cổng dịch vụ SMB tại Kịch bản 1).
9. **Loại hình:** **Evidence Figure** (Ảnh bằng chứng quét cổng Nmap).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/scenario1/Scenario1_B4_SMB_Ports.png`.
    - Phân loại trong ledger: Đây là hình thức trình bày bằng chứng có sẵn (Evidence presentation), chưa từng có số hiệu hình riêng trong bản thảo cũ `CHAPTER_3_DRAFT_R2.md`.
    - Khu vực giữ: Cửa sổ dòng lệnh Kali hiển thị lệnh quét `nmap -p 139,445 --reason 192.168.56.20` và bảng kết quả hiển thị `139/tcp open netbios-ssn syn-ack`, `445/tcp open microsoft-ds syn-ack`.
    - Không được che: Trạng thái open, cờ syn-ack và thời gian quét.
11. **Ghép panel:** Không ghép; dùng đơn lẻ làm bằng chứng mở cổng mạng.
12. **Caption dự kiến:** `Hình 3.4. Kết quả quét cổng dịch vụ SMB từ trạm Kali Linux xác nhận cổng 139 và 445 ở trạng thái mở`
13. **Ranh giới caption:** Chú thích chỉ xác nhận hai cổng 139 và 445 đang mở và phản hồi gói tin SYN-ACK từ góc nhìn trạm Kali; không đưa ra kết luận về sự tồn tại của lỗ hổng bảo mật.
14. **Ranh giới kết luận section:** Khẳng định bề mặt tiếp cận mạng của dịch vụ SMB đã được mở ra giữa Kali và Windows; trạm kiểm thử có thể tương tác trực tiếp với dịch vụ SMB qua hai cổng này.
15. **Overclaim bị cấm:**
    - CẤM gán định danh cụ thể cho host `.56.100` (phải giữ nhãn `UNKNOWN identity`).
    - CẤM tuyên bố cổng 445 mở đồng nghĩa với máy chủ dính mã độc hay lỗ hổng MS17-010.
    - CẤM dùng mã quy trình "B2, B3, B4" làm tiêu đề văn bản (chỉ dùng ở tầng truy vết).
16. **Nối sang phần kế tiếp:** Khi hai cổng dịch vụ đã xác nhận mở, bước tiếp theo là nhận diện phiên bản dịch vụ và các đặc tính giao thức chuyên sâu của SMB, được trình bày tại Mục 3.3.2.

---

#### 3.3.2. Nhận diện giao thức và các đặc tính SMB
1. **Đề mục:** `3.3.2. Nhận diện giao thức và các đặc tính SMB`
2. **Câu hỏi người đọc:** *Dịch vụ chạy trên hai cổng mở đó là gì, hỗ trợ những phương ngữ nào và có bắt buộc ký số gói tin hay không?*
3. **Thông điệp chính:** Nmap nhận diện dịch vụ trên cổng 139 là `Windows netbios-ssn` và cổng 445 là `Windows Server 2008 R2 - 2012 microsoft-ds`. Kịch bản `smb-protocols` phát hiện máy chủ hỗ trợ 5 phương ngữ gồm `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, và `3.0.2`. Kịch bản `smb2-capabilities` ghi nhận tính năng DFS trên các phương ngữ `2.0.2` đến `3.0.2`, tính năng Leasing và Multi-credit trên các phương ngữ `2.1` đến `3.0.2`. Kịch bản `smb2-security-mode` xác định chính sách ký số trên SMB 3.0.2 là `Message signing enabled but not required` (ghi nhận độc lập với cờ nội bộ). Kịch bản `smb-os-discovery` không trả về kết quả khả dụng.
4. **Technical facts được phép dùng:**
   - Quét phiên bản B5 (`b5_smb_version.nmap`): dải nhận diện fingerprint là `Windows Server 2008 R2 - 2012`. Đây là dấu vết phiên bản từ xa, không phải định danh tuyệt đối bản 2012 R2.
   - Quét kịch bản B6 (`b6_smb_nse.nmap`): 5 dialect (`NT LM 0.12`, `2.0.2`, `2.1`, `3.0`, `3.0.2`).
   - Chi tiết capabilities (F06): DFS được hỗ trợ trên `2.0.2..3.0.2`; Leasing và Multi-credit operations được hỗ trợ trên `2.1..3.0.2`.
   - Ký số từ xa: `Message signing enabled but not required` trên phương ngữ 3.0.2 (độc lập với cờ ký số nội bộ mang giá trị False).
   - `smb-os-discovery`: không có kết quả khả dụng (`no usable output`).
   - Tiên đề: `SMBv1 enabled != MS17-010 confirmed`. Hỗ trợ SMBv1 chỉ là điều kiện giao thức, không tự chứng minh lỗ hổng.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/scenario1/b5_smb_version.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario1/b6_smb_nse.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario1/Scenario1_B5_SMB_Version.png` (PRIMARY_VISUAL — Hình 3.4 cũ).
   - `work/do-an/chapter3/evidence/scenario1/Scenario1_B6_SMB_NSE_A.png` (PRIMARY_VISUAL — Hình 3.5 cũ).
6. **Supporting evidence:** `Kali_PreDemo_02_NSE_Scripts.png`.
7. **Bảng cần dùng:** Tích hợp đầy đủ vào Bảng 3.3 ở Mục 3.3.3.
8. **Hình cần dùng:** **Hình 3.5** (Kết quả nhận diện phiên bản dịch vụ và phân tích các phương ngữ SMB từ trạm Kali Linux).
9. **Loại hình:** **Comparison Figure** (Ghép 2 panel bằng chứng từ trạm Kali: Panel A nhận diện phiên bản -sV + Panel B phân tích phương ngữ và capabilities NSE).
10. **Hướng dẫn crop:**
    - Panel A (nguồn `Scenario1_B5_SMB_Version.png`, vốn là Hình 3.4 trong bản thảo cũ): Cắt phần output Nmap -sV, hiển thị dải fingerprint `Windows Server 2008 R2 - 2012`.
    - Panel B (nguồn `Scenario1_B6_SMB_NSE_A.png`, vốn là Hình 3.5 trong bản thảo cũ): Cắt phần output `smb-protocols`, `smb2-capabilities` và `smb2-security-mode`, hiển thị danh sách 5 dialect, các capabilities và dòng signing enabled but not required. Nếu layout không đủ chỗ cho toàn bộ capabilities trong panel, phần chi tiết capabilities (DFS/Leasing/Multi-credit) bắt buộc phải được giữ nguyên vẹn trong Bảng 3.3 và văn bản phân tích dựa trên raw `b6_smb_nse.nmap`.
    - Không được che: Dòng chữ NT LM 0.12, SMB 3.0.2 và chính sách signing.
11. **Ghép panel:** Ghép dọc hoặc ghép ngang hai panel để người đọc nhìn thấy toàn diện diện mạo dịch vụ SMB được khám phá từ trạm kiểm thử.
12. **Caption dự kiến:** `Hình 3.5. Kết quả phân tích phiên bản dịch vụ, danh sách phương ngữ và chính sách ký số SMB từ trạm Kali Linux`
13. **Ranh giới caption:** Chú thích mô tả đúng các thông tin nhận diện được: phiên bản dịch vụ tương thích, danh sách 5 phương ngữ hỗ trợ và chính sách ký số không bắt buộc; không kết luận máy chủ có lỗ hổng bảo mật.
14. **Ranh giới kết luận section:** Khẳng định bề mặt tấn công giao thức SMBv1 (`NT LM 0.12`) đang tồn tại trên đường truyền; tuy nhiên việc máy chủ hỗ trợ SMBv1 chưa đủ cơ sở để khẳng định hệ thống bị ảnh hưởng bởi MS17-010.
15. **Overclaim bị cấm:**
    - CẤM tuyên bố hỗ trợ SMBv1 đồng nghĩa với máy chủ đã dính MS17-010.
    - CẤM coi việc ký số `enabled but not required` là một điểm yếu bảo mật hoặc điều kiện tiên quyết cho việc khai thác.
    - CẤM tự ý bịa đặt kết quả hoặc suy diễn nguyên nhân lỗi cho `smb-os-discovery`.
16. **Nối sang phần kế tiếp:** Toàn bộ các kết quả khảo sát mạng và giao thức trong Kịch bản 1 được tổng hợp một cách hệ thống tại Mục 3.3.3.

---

#### 3.3.3. Tổng hợp kết quả khảo sát
1. **Đề mục:** `3.3.3. Tổng hợp kết quả khảo sát`
2. **Câu hỏi người đọc:** *Bức tranh tổng thể về dịch vụ SMB thu được từ Kịch bản 1 có ý nghĩa gì và trả lời được những gì?*
3. **Thông điệp chính:** Hệ thống hóa toàn bộ kết quả đo đạc từ Kịch bản 1 thành một bảng dữ liệu chuẩn; làm rõ rằng trạm kiểm thử đã xác định được sự tồn tại của máy chủ, hai cổng SMB mở tiếp nhận kết nối, và ngăn xếp SMB chấp nhận đàm phán phương ngữ SMBv1 cũ cùng các phương ngữ hiện đại kèm các tính năng DFS, Leasing và Multi-credit.
4. **Technical facts được phép dùng:**
   - Tổng hợp kết quả 5 bước B2 đến B6: cổng, trạng thái, thời gian trễ, tên dịch vụ, danh sách 5 phương ngữ, chi tiết `smb2-capabilities` (DFS trên 2.0.2..3.0.2; Leasing/Multi-credit trên 2.1..3.0.2), chính sách ký số `enabled but not required`, `smb-os-discovery` no usable output.
   - Tái khẳng định nhãn `UNKNOWN identity` cho host `.56.100`.
   - Khẳng định Kịch bản 1 đã hoàn thành trọn vẹn việc khảo sát bề mặt dịch vụ nhưng chưa thực hiện kiểm định chuyên sâu về lỗ hổng MS17-010.
5. **Direct evidence tương ứng:** Toàn bộ dữ liệu thô `work/do-an/chapter3/evidence/scenario1/b{2..6}_*.nmap` (PRIMARY_RAW).
6. **Supporting evidence:** `scenario1/Scenario1_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** **Bảng 3.3** (Bảng kết quả rà quét nhận diện dịch vụ và phương ngữ SMB tại Kịch bản 1).
8. **Hình cần dùng:** Không dùng hình mới tại tiểu mục này (đã có Hình 3.4 và Hình 3.5 minh chứng).
9. **Loại hình:** Không áp dụng.
10. **Hướng dẫn crop:** Không áp dụng.
11. **Ghép panel:** Không áp dụng.
12. **Caption dự kiến:** Không áp dụng.
13. **Ranh giới caption:** Không áp dụng.
14. **Ranh giới kết luận section:** Kết luận Kịch bản 1 đã phác họa đầy đủ diện mạo dịch vụ SMB và đặt ra tiền đề kỹ thuật để chuyển sang Kịch bản 2 nhằm kiểm định trực tiếp dấu hiệu lỗ hổng MS17-010.
15. **Overclaim bị cấm:** CẤM đưa ra bất kỳ kết luận nào về lỗ hổng MS17-010 trong phần tổng kết Kịch bản 1.
16. **Nối sang phần kế tiếp:** Để xác minh liệu việc hỗ trợ phương ngữ SMBv1 có đi kèm với dấu hiệu tồn tại lỗ hổng MS17-010 hay không, Kịch bản 2 được triển khai với tập kịch bản NSE chuyên sâu, trình bày tại Mục 3.4.

---

### MỤC 3.4. KIỂM TRA DẤU HIỆU MS17-010

#### 3.4.1. Kết quả kiểm tra từ xa bằng Nmap/NSE
1. **Đề mục:** `3.4.1. Kết quả kiểm tra từ xa bằng Nmap/NSE`
2. **Câu hỏi người đọc:** *Khi chạy kịch bản quét chuyên dụng kiểm tra MS17-010 từ trạm Kali Linux, công cụ Nmap trả về kết quả gì và kết quả đó có nghĩa là gì?*
3. **Thông điệp chính:** Chuỗi phép đo NSE tái xác nhận cổng 139/445 mở (NSE-SMB-01), 5 phương ngữ (NSE-SMB-02) và chính sách ký số (NSE-SMB-03) đóng vai trò bối cảnh xác nhận. Tại phép đo trọng tâm NSE-SMB-04, kịch bản `smb-vuln-ms17-010` hoàn tất phiên quét trên cổng 445 nhưng không trả về khối kết luận `Host script results:`. Kết quả đo đạc từ xa được phân loại chính xác theo phương pháp luận là **`UNKNOWN / NO USABLE SCRIPT RESULT`**; tuân thủ nghiêm ngặt nguyên tắc `UNKNOWN != SAFE`, không ngộ nhận trạng thái chưa xác định là an toàn. Nguyên nhân của việc thiếu vắng kết luận script chưa được xác lập từ dữ liệu thực nghiệm.
4. **Technical facts được phép dùng (F02):**
   - Đúng ánh xạ quy chuẩn:
     * `NSE-SMB-01`: quét cổng TCP 139/445 (`open`, `syn-ack`).
     * `NSE-SMB-02`: `smb-protocols` (5 phương ngữ).
     * `NSE-SMB-03`: `smb2-security-mode` (signing enabled but not required).
     * `NSE-SMB-04`: `smb-vuln-ms17-010` (cổng 445 open, Nmap hoàn tất, không có khối `Host script results:`).
   - Câu lệnh thực nghiệm:
     * Lệnh thao tác của kiểm thử viên (operator command): `sudo nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`.
     * Tham số ghi nhận trong log Nmap (recorded argv): `nmap -p 445 --script smb-vuln-ms17-010 --privileged 192.168.56.20`.
     * Khi viết dạng rút gọn `nmap -p 445 --script smb-vuln-ms17-010 192.168.56.20`, phải ghi rõ là dạng chuẩn hóa/rút gọn, không gọi là literal command đã ghi nhận trong log.
     * **TUYỆT ĐỐI KHÔNG CÓ THAM SỐ `unsafe=0`** trong câu lệnh thực nghiệm.
   - Phân loại dự án: **`UNKNOWN / NO USABLE SCRIPT RESULT`**.
   - Nguyên nhân của việc thiếu vắng kết luận script **chưa được xác lập** từ bộ dữ liệu thực nghiệm hiện có.
   - Tiên đề: `UNKNOWN != SAFE`. Không tự gán thông báo VULNERABLE, SAFE, hay NOT VULNERABLE.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/scenario2/NSE-SMB-01_ports.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario2/NSE-SMB-02_protocols.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario2/NSE-SMB-03_signing.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario2/NSE-SMB-04_ms17010.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` (PRIMARY_VISUAL — Hình 3.6 cũ).
6. **Supporting evidence:** `scenario2/Scenario2_Run_Manifest.txt` (SECONDARY_META), `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png`.
7. **Bảng cần dùng:** **Bảng 3.4** (Kết quả 4 phép đo NSE khảo sát thuộc tính dịch vụ và dấu hiệu lỗ hổng MS17-010).
8. **Hình cần dùng:** **Hình 3.6** (Kết quả thực thi kịch bản `smb-vuln-ms17-010` từ trạm Kali Linux).
9. **Loại hình:** **Evidence Figure** (Ảnh bằng chứng thực thi script Nmap NSE).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/scenario2/Scenario2_NSE04_MS17010.png` (đã có bản chuẩn hóa `chapter3/presentation/3_3/Hinh_3_6_MS17010_NSE.png`).
    - Khu vực giữ: Cửa sổ terminal Kali hiển thị lệnh quét `smb-vuln-ms17-010` nhắm vào 192.168.56.20 và kết quả: 445/tcp open microsoft-ds, Nmap done, hoàn toàn không có khối Host script results.
    - Không được che: Dòng trạng thái cổng 445 và thông báo hoàn tất quét.
11. **Ghép panel:** Không ghép; dùng đơn lẻ làm minh chứng trung thực cho hiện tượng công cụ không sinh phán quyết.
12. **Caption dự kiến:** `Hình 3.6. Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux ghi nhận cổng 445 mở và không xuất hiện khối kết luận kịch bản`
13. **Ranh giới caption:** Chú thích chỉ mô tả đúng nội dung hiển thị: cổng 445 mở và không có khối kết quả kịch bản; việc phân loại UNKNOWN là quy ước phương pháp luận của đề tài, không phải chuỗi ký tự hiển thị của Nmap.
14. **Ranh giới kết luận section:** Khẳng định kết quả quét từ xa độc lập không cung cấp đủ căn cứ để kết luận máy chủ có lỗ hổng hay an toàn; việc đánh giá an ninh bắt buộc phải đối chiếu chéo với trạng thái nội bộ của máy chủ.
15. **Overclaim bị cấm:**
    - CẤM suy diễn kịch bản quét kết luận máy chủ an toàn hoặc không có lỗ hổng.
    - CẤM tự ý đưa ra nguyên nhân giả định (như lỗi timeout, lỗi đàm phán, thiếu quyền, cơ chế an toàn `unsafe=0`, hay mã lỗi NTSTATUS) khi dữ liệu thô không ghi nhận.
    - CẤM viết "UNKNOWN" như thể đó là một từ khóa do Nmap in ra trên màn hình.
16. **Nối sang phần kế tiếp:** Để hiểu rõ ý nghĩa thực sự của kết quả UNKNOWN từ xa, bước phân tích tiếp theo là đối chiếu kết quả này với trạng thái bản vá thực tế của máy chủ Windows, trình bày tại Mục 3.4.2.

---

#### 3.4.2. Đối chiếu với trạng thái bản vá trên Windows
1. **Đề mục:** `3.4.2. Đối chiếu với trạng thái bản vá trên Windows`
2. **Câu hỏi người đọc:** *Tại sao công cụ quét từ xa trả về UNKNOWN nhưng máy chủ nội bộ lại là UNPATCHED, và điều này có mâu thuẫn không?*
3. **Thông điệp chính:** Hoàn toàn không có mâu thuẫn; đây là minh chứng thực nghiệm then chốt về sự độc lập giữa tín hiệu thăm dò từ xa (remote observation) và trạng thái bản vá nội tại (local ground truth). Máy chủ thực sự chưa được vá lỗi (`srv.sys` cũ, thiếu hotfix), nhưng công cụ quét từ xa không sinh phán quyết khẳng định. Sự đối chiếu này chứng minh ranh giới khoa học: một kết quả quét từ xa không phát hiện lỗ hổng không đồng nghĩa với việc hệ điều hành đã được bảo vệ.
4. **Technical facts được phép dùng (F01, F02, F07):**
   - Trục quan sát từ xa: `UNKNOWN / NO USABLE SCRIPT RESULT` (nguyên nhân chưa xác lập; không gán `unsafe=0`).
   - Trục sự thật nội bộ: `UNPATCHED` (`srv.sys` nhị phân `6.3.9600.16421 < 6.3.9600.18604` theo Microsoft S032, thiếu hotfix KB4012213/KB4012216).
   - Khẳng định tính độc lập giữa hai lớp bằng chứng.
   - Không có hoạt động khai thác xâm nhập (exploit payload, RCE, Meterpreter) trong phạm vi thực nghiệm đã phê duyệt của đồ án.
5. **Direct evidence tương ứng:**
   - Đối chiếu chéo giữa `work/do-an/chapter3/evidence/scenario2/NSE-SMB-04_ms17010.nmap` (PRIMARY_RAW) và `work/do-an/chapter3/evidence/baseline/Windows_MS17010_01_SrvSysVersion.png` (PRIMARY_VISUAL), `Windows_MS17010_02_Hotfix.png` (PRIMARY_VISUAL).
   - Căn cứ thẩm quyền ngoài: Microsoft Support Article 4023262 (`S032`) và Microsoft Security Bulletin MS17-010 (`S005`). File `MS17-010_Official_Mapping.txt` chỉ là tài liệu điều hướng nội bộ.
6. **Supporting evidence:** `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` (ETM-S2-04, ETM-S2-05).
7. **Bảng cần dùng:** Tích hợp trong phân tích đối chiếu tại Bảng 3.4.
8. **Hình cần dùng:** **Hình 3.7** (Sơ đồ đối chiếu chéo giữa phán quyết quét từ xa và trạng thái bản vá nội bộ).
9. **Loại hình:** **Comparison Figure** (Đối chiếu thị giác giữa hai trục dữ kiện: Remote vs. Local).
10. **Hướng dẫn crop và thiết kế (F01):**
    - Khung trái (Remote): Ảnh terminal Nmap NSE04 (`Scenario2_NSE04_MS17010.png`), hiển thị cổng 445 open và không có kết quả script.
    - Khung phải (Local): Trích xuất từ PowerShell `Windows_MS17010_01_SrvSysVersion.png` (hiển thị phiên bản số nhị phân `6.3.9600.16421`) và `Windows_MS17010_02_Hotfix.png` (danh mục 6 hotfix), đối chiếu ngưỡng `6.3.9600.18604` theo Microsoft S032.
    - **Nguyên tắc bắt buộc:** Mọi nhãn tổng hợp (như "Remote: UNKNOWN", "Local: UNPATCHED", "Ngưỡng Microsoft: 6.3.9600.18604") phải được đặt **BÊN NGOÀI pixel ảnh bằng chứng gốc**, không đè chữ vào hình chụp thật.
11. **Ghép panel:** Ghép song song hai khối dữ liệu để người đọc thấy rõ sự độc lập giữa hai góc nhìn.
12. **Caption dự kiến:** `Hình 3.7. Đối chiếu giữa tín hiệu thăm dò từ xa qua Nmap NSE và trạng thái bản vá thực tế trên máy chủ Windows`
13. **Ranh giới caption:** Chú thích mô tả sự đối chiếu độc lập giữa hai nguồn dữ liệu: một bên là kết quả quét mạng không sinh phán quyết, một bên là trạng thái driver chưa vá trên máy chủ.
14. **Ranh giới kết luận section (F07):** Dừng lại ở kết luận khoa học: kết quả quét từ xa và trạng thái bản vá nội bộ là hai lớp dữ kiện độc lập; thiếu vắng cảnh báo từ xa không thay đổi trạng thái chưa vá lỗi của máy chủ. Toàn bộ các phân tích về nguy cơ tiềm ẩn, khuyến nghị phòng thủ theo chiều sâu hay chính sách quản lý lỗ hổng thuộc phạm vi thảo luận của **Chương 4**.
15. **Overclaim bị cấm:**
    - CẤM tuyên bố kết quả UNKNOWN là lỗi của công cụ (tool failure) hoặc do chế độ `unsafe=0`.
    - CẤM suy diễn rằng nếu chạy exploit thật thì chắc chắn sẽ chiếm quyền thành công (việc exploit nằm ngoài phạm vi đã duyệt).
    - CẤM đưa các khuyến nghị an ninh doanh nghiệp hay đánh giá mức độ nghiêm trọng rủi ro vào kết luận mục này (thuộc Chương 4).
16. **Nối sang phần kế tiếp:** Trước thực trạng máy chủ chưa được cập nhật bản vá, giải pháp giảm thiểu đầu tiên được thử nghiệm độc lập là can thiệp cấu hình hệ thống bằng cách vô hiệu hóa giao thức SMBv1, được trình bày tại Mục 3.5.

---

### MỤC 3.5. THỰC NGHIỆM VÔ HIỆU HÓA SMBv1 TRÊN MÁY CHỦ

#### 3.5.1. Trạng thái trước và sau khi vô hiệu hóa SMBv1
1. **Đề mục:** `3.5.1. Trạng thái trước và sau khi vô hiệu hóa SMBv1`
2. **Câu hỏi người đọc:** *Biện pháp vô hiệu hóa SMBv1 được thực hiện như thế nào và cấu hình máy chủ thay đổi ra sao sau câu lệnh?*
3. **Thông điệp chính:** Thao tác quản trị được thực hiện trực tiếp trên máy chủ qua lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`. Cấu hình nội bộ ghi nhận thuộc tính `EnableSMB1Protocol` chuyển từ `True` sang `False`, trong khi `EnableSMB2Protocol` giữ nguyên `True`, thành phần `FS-SMB1` vẫn ở trạng thái `Installed` (không gỡ bỏ tính năng, không khởi động lại máy), và dịch vụ `LanmanServer` được ghi nhận ở trạng thái `Running` tại thời điểm kiểm tra (point-in-time check; không chứng minh tính liên tục tuyệt đối hay khả năng tương thích của mọi ứng dụng).
4. **Technical facts được phép dùng (F03):**
   - Trạng thái trước: `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`, `LanmanServer` Running.
   - Lệnh thực thi: `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`.
   - Trạng thái sau: `EnableSMB1Protocol : False`, `EnableSMB2Protocol : True`, `LanmanServer` Running tại thời điểm kiểm tra.
   - `FS-SMB1` vẫn là `Installed` (đây là can thiệp runtime configuration, không phải gỡ tính năng hệ điều hành).
   - Tệp driver `srv.sys` và trạng thái bản vá vẫn giữ nguyên `UNPATCHED` (`SMBv1 disabled != PATCHED`).
   - Ranh giới quan sát: Hai snapshot point-in-time không chứng minh tính liên tục của dịch vụ trong suốt quá trình thay đổi hay sự tương thích của toàn bộ ứng dụng nghiệp vụ.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_01_Before.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_02_Action.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png` (PRIMARY_VISUAL — Hình 3.7 cũ).
6. **Supporting evidence:** `case_b/SMBv1_Remediation_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** Tích hợp trong Bảng 3.5 ở Mục 3.5.3.
8. **Hình cần dùng:** **Hình 3.8** (Chuỗi thao tác thực thi vô hiệu hóa SMBv1 và trạng thái cấu hình cục bộ trước và sau can thiệp).
9. **Loại hình:** **Comparison Figure** (Ghép 3 panel theo tiến trình thời gian: Trước $\to$ Thao tác $\to$ Sau).
10. **Hướng dẫn crop:**
    - Panel 1 (Trước): Cắt phần hiển thị `EnableSMB1Protocol : True` (`SMBv1_Remediation_01_Before.png`).
    - Panel 2 (Thao tác): Cắt dòng lệnh thực thi `Set-SmbServerConfiguration` (`SMBv1_Remediation_02_Action.png`).
    - Panel 3 (Sau): Cắt kết quả kiểm tra `EnableSMB1Protocol : False`, `FS-SMB1 : Installed`, `LanmanServer : Running` (`SMBv1_Remediation_03_After_Local.png`).
    - Không được che: Tên thuộc tính EnableSMB1Protocol và các giá trị True/False tương ứng.
11. **Ghép panel:** Ghép dọc 3 panel theo thứ tự thời gian (Before $\to$ Action $\to$ After).
12. **Caption dự kiến:** `Hình 3.8. Trình tự thực thi lệnh vô hiệu hóa giao thức SMBv1 và kết quả xác nhận cấu hình cục bộ trên máy chủ Windows`
13. **Ranh giới caption:** Chú thích mô tả việc thực thi lệnh thay đổi cấu hình nội bộ từ True sang False; không tuyên bố máy chủ đã được vá hay dịch vụ chia sẻ tệp an toàn tuyệt đối.
14. **Ranh giới kết luận section (F03):** Khẳng định SMBv1 đã bị tắt thành công ở tầng cấu hình dịch vụ máy chủ nội bộ; dịch vụ LanmanServer được ghi nhận Running tại thời điểm kiểm tra; tuy nhiên trạng thái bản vá driver bên dưới vẫn chưa thay đổi và thao tác này chưa chứng minh tính liên tục hay khả năng tương thích của mọi ứng dụng nghiệp vụ.
15. **Overclaim bị cấm:**
    - CẤM tuyên bố hành động này là "gỡ bỏ hoàn toàn tính năng SMBv1" (tính năng FS-SMB1 vẫn Installed).
    - CẤM tuyên bố việc tắt SMBv1 đồng nghĩa với việc máy chủ đã được vá lỗi MS17-010 (`SMBv1 disabled != PATCHED`).
    - CẤM tuyên bố "không làm gián đoạn dịch vụ" hay "đảm bảo 100% tính liên tục nghiệp vụ" khi chỉ có snapshot point-in-time.
16. **Nối sang phần kế tiếp:** Sau khi cấu hình nội bộ máy chủ đã thay đổi, bước tiếp theo là kiểm tra lại từ xa để xác định sự thay đổi này có phản ánh ra bề mặt mạng hay không, trình bày tại Mục 3.5.2.

---

#### 3.5.2. Kết quả kiểm tra lại từ Kali Linux
1. **Đề mục:** `3.5.2. Kết quả kiểm tra lại từ Kali Linux`
2. **Câu hỏi người đọc:** *Sau khi tắt SMBv1 trên máy chủ, trạm Kali Linux quét lại thấy những gì thay đổi và những gì giữ nguyên?*
3. **Thông điệp chính:** Đo đạc lại từ xa ghi nhận sự thay đổi cụ thể: kịch bản `smb-protocols` xác nhận phương ngữ `NT LM 0.12 (SMBv1)` hoàn toàn vắng mặt khỏi danh sách đàm phán quan sát được; các phương ngữ SMB2/SMB3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`) vẫn quan sát được. Cổng TCP 445 được ghi nhận ở trạng thái `open` trong phép đo lại (lưu ý: cổng 139 không được đo lại trong Case B, và lệnh đo lại cổng 445 không dùng cờ `--reason` nên không có dữ liệu `syn-ack`). Kịch bản `smb-vuln-ms17-010` tiếp tục không có khối kết quả, duy trì phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`.
4. **Technical facts được phép dùng (F03):**
   - Kịch bản `smb-protocols` đo lại (`case_b/NSE-SMB-02_protocols.nmap`): ghi nhận 4 phương ngữ SMB2/3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`); `NT LM 0.12` vắng mặt.
   - Cổng TCP 445 đo lại: `open`.
   - **Ranh giới quan trọng:** Cổng TCP 139 **KHÔNG ĐƯỢC ĐO LẠI** trong Case B (`NOT REMEASURED`).
   - Lệnh đo lại cổng 445 không có cờ `--reason`, do đó không được tự ý gán nhãn `syn-ack`.
   - Việc ghi nhận 4 phương ngữ SMB2/3 chỉ phản ánh mã định danh được công cụ quét ghi nhận từ xa, không chứng minh toàn bộ khối lượng công việc trao đổi tệp của ứng dụng nghiệp vụ đã được kiểm chứng đầy đủ.
   - Kịch bản `smb-vuln-ms17-010` đo lại (`case_b/NSE-SMB-04_ms17010.nmap`): cổng 445 open, không có script verdict $\to$ duy trì `UNKNOWN / NO USABLE SCRIPT RESULT`.
   - Tiên đề: `SMBv1 disabled != PATCHED`.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/case_b/NSE-SMB-02_protocols.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/case_b/NSE-SMB-04_ms17010.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` (PRIMARY_VISUAL — Hình 3.8 cũ).
6. **Supporting evidence:**
   - `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_05_NSE04_MS17010.png` (PRIMARY_VISUAL — lưu giữ đối soát kết quả UNKNOWN đo lại).
   - `case_b/SMBv1_Remediation_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** Tích hợp trong Bảng 3.5 ở Mục 3.5.3.
8. **Hình cần dùng:** **Hình 3.9** (Kết quả đo đạc lại phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1).
9. **Loại hình:** **Evidence Figure** (Ảnh bằng chứng đo đạc lại từ xa).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` (đã có bản chuẩn hóa `chapter3/presentation/3_4/Hinh_3_8_SMB_Protocols_Retest.png`).
    - Khu vực giữ: Cửa sổ terminal Kali hiển thị kết quả script `smb-protocols`, làm nổi bật danh sách dialect chỉ bắt đầu từ `2.0.2` đến `3.0.2`, vắng mặt hoàn toàn dòng `NT LM 0.12`.
    - Không được che: Danh sách các dialect SMB2/3 và thông báo hoàn tất quét.
11. **Ghép panel:** Không ghép; dùng độc lập làm bằng chứng cho sự vắng mặt của phương ngữ SMBv1 trên đường truyền mạng.
12. **Caption dự kiến:** `Hình 3.9. Kết quả đo lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1 xác nhận phương ngữ NT LM 0.12 vắng mặt`
13. **Ranh giới caption:** Chú thích xác nhận phương ngữ NT LM 0.12 không còn xuất hiện trong phản hồi đàm phán; không tuyên bố máy chủ đã hết lỗ hổng hay cổng dịch vụ đã đóng.
14. **Ranh giới kết luận section:** Khẳng định bề mặt tấn công giao thức cũ SMBv1 đã bị loại bỏ khỏi danh sách đàm phán quan sát được từ xa; tuy nhiên cổng 445 vẫn mở và driver `srv.sys` bên dưới vẫn là phiên bản chưa vá lỗi.
15. **Overclaim bị cấm:**
    - CẤM tuyên bố cổng 139 đã đóng hay đã đo lại trong Case B (TCP 139 là NOT REMEASURED).
    - CẤM tự ý gán cờ `syn-ack` cho cổng 445 trong lần đo lại Case B.
    - CẤM tuyên bố việc tắt SMBv1 đã "chặn đứng mọi nguy cơ tấn công" hay "bảo vệ hoàn toàn hệ thống".
    - CẤM suy diễn rằng máy chủ đã từ chối đàm phán vượt quá dữ liệu danh sách phương ngữ quan sát được.
16. **Nối sang phần kế tiếp:** Bức tranh toàn diện về những gì thay đổi và những gì không thay đổi trong Case B được tổng hợp tại Mục 3.5.3.

---

#### 3.5.3. Tổng hợp sự thay đổi quan sát được
1. **Đề mục:** `3.5.3. Tổng hợp sự thay đổi quan sát được`
2. **Câu hỏi người đọc:** *Biện pháp Case B có ưu điểm và giới hạn kỹ thuật cốt lõi nào khi đặt các dữ kiện cạnh nhau?*
3. **Thông điệp chính:** Hệ thống hóa sự so sánh Before vs. After của Case B trên 7 tiêu chí kỹ thuật: cấu hình `EnableSMB1Protocol`, cấu hình `EnableSMB2Protocol`, tính năng `FS-SMB1`, trạng thái dịch vụ `LanmanServer`, cổng TCP 445, phương ngữ SMB từ xa, phán quyết MS17-010, và trạng thái bản vá `srv.sys`. Biện pháp tắt SMBv1 thành công trong việc loại bỏ phương ngữ cũ trên bề mặt mạng mà dịch vụ LanmanServer vẫn duy trì Running tại thời điểm kiểm tra; nhưng giới hạn cốt lõi là không sửa đổi mã nhị phân driver nhân `srv.sys` (kế thừa phân loại `UNPATCHED`), và cổng TCP 445 vẫn tiếp tục mở ra mạng ngoài.
4. **Technical facts được phép dùng (F03, F08):**
   - Bảng đối chiếu Before vs. After gồm 7 hàng dữ liệu kỹ thuật đầy đủ:
     1) Cấu hình SMBv1 (`EnableSMB1Protocol : True` $\to$ `False`).
     2) Cấu hình SMB2/3 (`EnableSMB2Protocol : True` $\to$ `True`).
     3) Tính năng Windows (`FS-SMB1 : Installed` $\to$ `Installed`).
     4) Dịch vụ chia sẻ tệp (`LanmanServer : Running` $\to$ `Running` tại thời điểm kiểm tra; ghi rõ snapshot point-in-time không chứng minh continuity/workload).
     5) Trạng thái cổng từ xa: TCP 445 `OPEN` trước và sau (đo lại không có `--reason`); TCP 139 `NOT REMEASURED` trong Case B.
     6) Phương ngữ từ xa: 5 dialect $\to$ 4 dialect (2.0.2..3.0.2; NT LM 0.12 vắng mặt).
     7) Phán quyết MS17-010: `UNKNOWN` trước và sau.
     8) Trạng thái bản vá: `UNPATCHED` trước và sau (kế thừa mốc baseline và metadata lượt chạy; ảnh After Local không trực tiếp đo driver/hotfix).
   - Nhấn mạnh nguyên tắc: can thiệp cấu hình phần mềm không thay thế được việc cập nhật bản vá lỗ hổng hệ điều hành (`SMBv1 disabled != PATCHED`).
5. **Direct evidence tương ứng:** Toàn bộ bằng chứng cục bộ và từ xa của Case B.
6. **Supporting evidence:** `case_b/SMBv1_Remediation_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** **Bảng 3.5** (Bảng so sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 tại Case B).
8. **Hình cần dùng:** Không dùng hình mới tại tiểu mục này (đã có Hình 3.8 và Hình 3.9 minh chứng).
9. **Loại hình:** Không áp dụng.
10. **Hướng dẫn crop:** Không áp dụng.
11. **Ghép panel:** Không áp dụng.
12. **Caption dự kiến:** Không áp dụng.
13. **Ranh giới caption:** Không áp dụng.
14. **Ranh giới kết luận section:** Đúc kết vai trò và giới hạn của Case B: loại bỏ hiệu quả phương ngữ cũ trên bề mặt mạng nhưng để ngỏ cổng dịch vụ 445 và không vá lỗi nhân; tạo tiền đề cho việc thử nghiệm giải pháp kiểm soát ở tầng mạng.
15. **Overclaim bị cấm:**
    - CẤM kết luận Case B là giải pháp triệt để.
    - CẤM đưa ra các khuyến nghị vận hành doanh nghiệp (dành cho Chương 4).
16. **Nối sang phần kế tiếp:** Do việc tắt SMBv1 vẫn để cổng 445 mở tiếp nhận kết nối, giải pháp giảm thiểu thứ hai được khảo sát độc lập là kiểm soát truy cập ở tầng mạng bằng tường lửa pfSense, trình bày tại Mục 3.6.

---

### MỤC 3.6. THỰC NGHIỆM KIỂM SOÁT TRUY CẬP SMB BẰNG pfSense

#### 3.6.1. Bố trí pfSense và kiểm soát lưu lượng SMB
1. **Đề mục:** `3.6.1. Bố trí pfSense và kiểm soát lưu lượng SMB`
2. **Câu hỏi người đọc:** *Tường lửa pfSense được đặt ở đâu trong mô hình lab, hoạt động theo cơ chế nào và chính sách lọc gói tin được thiết lập ra sao?*
3. **Thông điệp chính:** pfSense được cấu hình hoạt động như một Cầu nối trong suốt Layer 2 (Transparent Bridge `bridge0`) kết nối hai giao diện mạng `CASE_C_KALI` (`em2`) và `CASE_C_WINDOWS` (`em3`), giữ nguyên dải địa chỉ IP `192.168.56.0/24` mà không can thiệp định tuyến Layer 3. Bộ lọc gói tin được kích hoạt trên các giao diện thành viên (`pfil_member=1`, `pfil_bridge=0`). Chính sách tường lửa thiết lập quy tắc chặn (Block) lưu lượng TCP cổng 139 và 445 từ Kali tới Windows có bật ghi nhật ký, được xếp ưu tiên thực thi trước quy tắc cho phép (Pass). Máy chủ Windows phía sau giữ nguyên trạng thái mốc chuẩn baseline.
4. **Technical facts được phép dùng (F05, F07):**
   - Kiến trúc: Transparent Bridge Layer 2 (`bridge0`). Không dùng routing Layer 3 (không gán IP gateway trên bridge).
   - Giao diện: `CASE_C_KALI = em2`, `CASE_C_WINDOWS = em3`. Quản trị qua `em1` (`192.168.57.2/24`).
   - FreeBSD Tunables: `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`. Tham số `pfil_onlyip = 1` chỉ ghi nhận từ metadata, không có trên ảnh trực tiếp.
   - Quy tắc tường lửa trên `CASE_C_KALI`: Action `Block`, Interface `CASE_C_KALI`, TCP, Source `192.168.56.10`, Destination `192.168.56.20`, Port `139, 445`, bật `Log`.
   - Thứ tự thực thi: Hàng quy tắc Block SMB nằm trên hàng quy tắc Baseline Pass.
   - **Tính độc lập của Case C:** Máy chủ Windows phía sau giữ nguyên cấu hình mốc chuẩn baseline: `SMB1=True`, `SMB2=True`, `LanmanServer=Running`, socket lắng nghe mở, `srv.sys` unpatched (không kế thừa cấu hình tắt SMBv1 của Case B).
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/case_c/pfSense_03_Interface_Assignment.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_c/pfSense_04_Bridge.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_c/pfSense_05_Bridge_Filtering.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_c/pfSense_07_Block_Rule_Config.png` (PRIMARY_VISUAL).
   - `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png` (PRIMARY_VISUAL — Hình 3.9 cũ).
6. **Supporting evidence:**
   - `case_c/pfSense_Remediation_Run_Manifest.txt` (SECONDARY_META).
   - `case_c/RUN4_PAUSE_STATE_REPORT.txt` Section 21 (SECONDARY_META_CLOSURE).
7. **Bảng cần dùng:** Tích hợp trong Bảng 3.6 ở Mục 3.6.3.
8. **Hình cần dùng:**
   - **Hình 3.10** (Sơ đồ kiến trúc mạng pfSense Transparent Bridge).
   - **Hình 3.11** (Cấu hình thứ tự quy tắc tường lửa pfSense ưu tiên chặn lưu lượng SMB).
9. **Loại hình:**
   - Hình 3.10: **Explanatory Figure** (Sơ đồ kiến trúc mạng Transparent Bridge Layer 2).
   - Hình 3.11: **Evidence Figure** (Ảnh bằng chứng cấu hình thứ tự rule trên pfSense GUI).
10. **Hướng dẫn crop:**
    - Hình 3.10: Sơ đồ vector thể hiện rõ: Kali (.56.10) $\to$ pfSense Cầu nối Layer 2 (em2/em3, bridge0, điểm lọc 139/445) $\to$ Windows (.56.20).
    - Hình 3.11: Cắt khu vực bảng quy tắc tường lửa trên giao diện `CASE_C_KALI` (`pfSense_08_Rule_Order.png`), hiển thị rõ hàng Block SMB nằm ngay phía trên hàng Baseline Pass.
    - Không được che: Biểu tượng Block đỏ, cổng SMB_Ports (139, 445) và vị trí thứ tự rule.
11. **Ghép panel:** Không ghép ảnh GUI phân mảnh; giữ Hình 3.11 tập trung vào thứ tự quy tắc. Các ảnh interface/bridge/tunables được lưu giữ đối soát qua text và Bảng 3.6.
12. **Caption dự kiến:**
    - Hình 3.10: `Hình 3.10. Sơ đồ kiến trúc mạng pfSense Transparent Bridge kiểm soát lưu lượng SMB giữa trạm Kali Linux và máy chủ mục tiêu`
    - Hình 3.11: `Hình 3.11. Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên giao diện CASE_C_KALI của pfSense`
13. **Ranh giới caption:** Chú thích mô tả đúng kiến trúc cầu nối không đổi IP subnet và cấu hình quy tắc chặn lưu lượng được đặt trước quy tắc cho phép; không suy đoán hiệu lực nếu chưa đo đạc mạng.
14. **Ranh giới kết luận section:** Khẳng định chốt chặn an ninh mạng đã được thiết lập thành công trên đường truyền dữ liệu giữa hai máy ảo mà không làm thay đổi kiến trúc địa chỉ IP của mạng lab.
15. **Overclaim bị cấm:**
    - CẤM dùng từ ngữ "định tuyến qua pfSense" (phải dùng "bố trí đi qua cầu nối pfSense").
    - CẤM tuyên bố bridge0 có địa chỉ IP trong subnet thử nghiệm.
    - CẤM suy đoán chính sách tường lửa cho các cổng khác ngoài 139 và 445.
16. **Nối sang phần kế tiếp:** Sau khi kích hoạt chính sách lọc trên pfSense, bước tiếp theo là thực hiện đo đạc lại từ trạm Kali Linux để kiểm tra phản ứng của đường truyền, trình bày tại Mục 3.6.2.

---

#### 3.6.2. Kết quả kiểm tra lại từ Kali Linux
1. **Đề mục:** `3.6.2. Kết quả kiểm tra lại từ Kali Linux`
2. **Câu hỏi người đọc:** *Khi quét qua đường thử nghiệm có pfSense, trạm Kali Linux quan sát được trạng thái cổng và kịch bản MS17-010 như thế nào?*
3. **Thông điệp chính:** Quét cổng từ trạm Kali Linux ghi nhận cả hai cổng TCP 139 và 445 chuyển từ trạng thái `open` sang trạng thái `filtered` do không nhận được phản hồi mạng (`no-response`). Kịch bản `smb-vuln-ms17-010` không có khối kết quả, tiếp tục duy trì phân loại `UNKNOWN / NO USABLE SCRIPT RESULT` từ góc nhìn trạm quét. Không có phép đo phương ngữ `smb-protocols` nào được thực hiện trong Case C (ghi nhận rõ `NOT MEASURED`).
4. **Technical facts được phép dùng (F04):**
   - Quét cổng đo lại (`case_c/NSE-SMB-01_ports.nmap`): 139/tcp và 445/tcp đều `filtered`, lý do `no-response`.
   - Quét MS17-010 đo lại (`case_c/NSE-SMB-04_ms17010.nmap`): 445/tcp `filtered microsoft-ds`, không xuất hiện khối kết quả kịch bản $\to$ duy trì phân loại chuẩn **`UNKNOWN / NO USABLE SCRIPT RESULT`** (không tạo ra phân loại mới "UNKNOWN/Filtered").
   - Phương ngữ SMB từ xa trong Case C: **`KHÔNG CÓ PHÉP ĐO TƯƠNG ỨNG / NOT MEASURED`**. Tuyệt đối không suy từ kết quả filtered của cổng thành kết quả đo phương ngữ.
   - Bỏ mọi suy diễn về việc "kịch bản không thể gửi gói thăm dò" hay cơ chế xử lý nội bộ của script mà direct evidence không xác lập.
   - Tiên đề: `FILTERED != PATCHED`. Trạng thái filtered chỉ phản ánh việc gói tin không nhận được phản hồi qua đường truyền hiện tại, không đồng nghĩa với máy chủ đã an toàn hay đã vá lỗi.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/case_c/NSE-SMB-01_ports.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/case_c/NSE-SMB-04_ms17010.nmap` (PRIMARY_RAW).
   - `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` (PRIMARY_VISUAL — Hình 3.10 cũ).
6. **Supporting evidence:**
   - `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` (PRIMARY_VISUAL — lưu giữ đối soát cổng filtered cho kịch bản MS17-010).
   - `case_c/pfSense_Remediation_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** Tích hợp trong Bảng 3.6 ở Mục 3.6.3.
8. **Hình cần dùng:** **Hình 3.12** (Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường kiểm thử pfSense).
9. **Loại hình:** **Evidence Figure** (Ảnh bằng chứng quét cổng Nmap ghi nhận trạng thái filtered).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` (đã có bản chuẩn hóa `chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png`).
    - Khu vực giữ: Cửa sổ terminal Nmap hiển thị lệnh `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason 192.168.56.20` và kết quả: `139/tcp filtered netbios-ssn no-response`, `445/tcp filtered microsoft-ds no-response`.
    - Không được che: Trạng thái filtered và lý do no-response trên cả hai cổng.
11. **Ghép panel:** Không ghép; dùng độc lập làm minh chứng cho việc mất khả năng tiếp cận dịch vụ từ trạm Kali.
12. **Caption dự kiến:** `Hình 3.12. Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense ghi nhận trạng thái filtered`
13. **Ranh giới caption:** Chú thích xác nhận cổng 139 và 445 rơi vào trạng thái filtered do không nhận được phản hồi (no-response) từ góc nhìn trạm Kali; ảnh Nmap độc lập không tự chứng minh nguyên nhân nội tại của pfSense.
14. **Ranh giới kết luận section:** Khẳng định bề mặt tiếp cận mạng tới dịch vụ SMB từ trạm Kali Linux đã bị ngăn chặn trên đường truyền thử nghiệm; tuy nhiên kết luận này bắt buộc phải được đối chiếu với nhật ký tường lửa và trạng thái máy chủ.
15. **Overclaim bị cấm:**
    - CẤM tuyên bố trạng thái filtered đồng nghĩa với máy chủ đã an toàn hay đã vá lỗi (`FILTERED != PATCHED`).
    - CẤM suy diễn rằng phương ngữ SMBv1 hay SMB2/3 "không tiếp cận được" như một kết quả đo phương ngữ (phải ghi NOT MEASURED).
    - CẤM tuyên bố bề mặt tấn công SMB bị xóa bỏ vĩnh viễn (kết quả chỉ ghi nhận trên đường truyền qua pfSense).
16. **Nối sang phần kế tiếp:** Để xác nhận việc cổng bị filtered thực sự do pfSense chặn gói tin và kiểm tra xem máy chủ phía sau có bị thay đổi gì không, bước tiếp theo là đối chiếu 3 bên giữa Kali, pfSense và Windows, trình bày tại Mục 3.6.3.

---

#### 3.6.3. Đối chiếu kết quả tại Kali, pfSense và Windows
1. **Đề mục:** `3.6.3. Đối chiếu kết quả tại Kali, pfSense và Windows`
2. **Câu hỏi người đọc:** *Làm sao chứng minh chính pfSense đã chặn các gói tin đó, và tình trạng máy chủ Windows phía sau tường lửa lúc này ra sao?*
3. **Thông điệp chính:** Đối chiếu chéo 3 bên làm sáng tỏ cơ chế phòng thủ: (1) Tại Kali: ghi nhận cổng `filtered (no-response)`; (2) Tại pfSense: nhật ký tường lửa ghi nhận các gói tin TCP SYN từ trạm Kali (`.56.10`) gửi tới cổng 139 và 445 của máy chủ (`.56.20`) bị hành động Block xử lý trong phiên quét canonical; (3) Tại Windows: cấu hình dịch vụ vẫn mở, `SMB1=True`, `SMB2=True`, socket đang lắng nghe và trạng thái bản vá vẫn là `UNPATCHED` (nguồn xác nhận từ Section 21 của `RUN4_PAUSE_STATE_REPORT.txt`).
4. **Technical facts được phép dùng (F05):**
   - Kali: 139/445 filtered do no-response.
   - pfSense Block Log: biểu tượng Block đỏ, Interface `CASE_C_KALI`, Source `192.168.56.10`, Destination `192.168.56.20:139` và `:445`, giao thức TCP, cờ SYN.
   - **Xung đột nhãn quy tắc đã khóa (CF-11):** Ảnh chụp nhật ký hiển thị nhãn `CASE C baseline pass Kali to Windows (100000104)` trong khi manifest/closure ghi `CASE C - Block SMB Kali to Windows (1000000104)`. Được phép kết luận: các gói tin TCP SYN phù hợp đã bị chặn trên đường truyền pfSense trong phiên quét canonical; TUYỆT ĐỐI CẤM quy thuộc đích danh named rule ID hoặc tuyên bố screenshot chứng minh chính xác named rule Block đã khớp. Tuyệt đối không crop ảnh để che conflict này.
   - **Căn cứ nguồn Windows cuối lượt (F05):** Máy chủ Windows phía sau không can thiệp trực tiếp; trạng thái cuối lượt được ghi nhận từ **Section 21 của `case_c/RUN4_PAUSE_STATE_REPORT.txt`** (SECONDARY_META_CLOSURE) và manifest: `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`, `LanmanServer : Running`, listener 139/445 hiện diện, driver `srv.sys` unpatched (`6.3.9600.16421`). Phân định rõ: đây là nguồn thứ cấp, không dùng baseline để giả làm direct screenshot proof.
   - **Giới hạn đối chiếu thời gian (F05):** Đối chiếu giữa Kali Nmap và pfSense log dựa trên run lineage và bộ tuple `(Nguồn: 192.168.56.10, Đích: 192.168.56.20, Cổng: 139/445, Giao thức: TCP, Cờ: SYN)`. Không so sánh xâu thời gian như thể cùng một wall clock và không suy đoán múi giờ đồng bộ chéo hệ thống.
   - Tiên đề: `FILTERED != PATCHED`.
5. **Direct evidence tương ứng:**
   - `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png` (PRIMARY_VISUAL_WITH_BOUNDED_CONFLICT — Hình 3.11 cũ).
   - `work/do-an/chapter3/evidence/case_c/NSE-SMB-01_ports.nmap` (PRIMARY_RAW).
6. **Supporting evidence (F05):**
   - `work/do-an/chapter3/evidence/case_c/RUN4_PAUSE_STATE_REPORT.txt` **Section 21** (SECONDARY_META_CLOSURE — căn cứ nguồn cho trạng thái máy chủ Windows cuối lượt).
   - `case_c/pfSense_Remediation_Run_Manifest.txt` (SECONDARY_META).
7. **Bảng cần dùng:** **Bảng 3.6** (Bảng so sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense tại Case C).
8. **Hình cần dùng:** **Hình 3.13** (Nhật ký tường lửa pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn).
9. **Loại hình:** **Evidence Figure with Bounded Conflict** (Ảnh bằng chứng nhật ký hệ thống kèm ranh giới bảo lưu xung đột nhãn quy tắc).
10. **Hướng dẫn crop:**
    - Tệp nguồn canonical: `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png` (đã có bản trích có sẵn tại `chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png`).
    - Khu vực giữ: Bảng System Logs Firewall hiển thị các dòng log có biểu tượng Block đỏ, giao diện CASE_C_KALI, nguồn 192.168.56.10, đích 192.168.56.20 trên cổng 139 và 445 với cờ SYN.
    - **Bắt buộc:** GIỮ NGUYÊN cột Rule hiển thị `CASE C baseline pass Kali to Windows (100000104)`; TUYỆT ĐỐI KHÔNG CẮT BỎ CỘT RULE ĐỂ CHE GIẤU XUNG ĐỘT NHÃN.
11. **Ghép panel:** Không ghép; dùng độc lập với độ phóng đại sắc nét để người đọc kiểm chứng trực tiếp các trường thông tin trong nhật ký.
12. **Caption dự kiến:** `Hình 3.13. Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm`
13. **Ranh giới caption:** Chú thích xác nhận lưu lượng TCP SYN tới cổng SMB bị chặn trên đường truyền pfSense trong phiên quét canonical; kèm ghi chú bảo lưu về sự không đồng nhất nhãn quy tắc giữa số hiệu 100000104 và vị trí rule trên giao diện, không quy thuộc đích danh rule ID.
14. **Ranh giới kết luận section:** Khẳng định pfSense đã thực thi hành vi chặn gói tin SMB trên đường mạng, giải thích nguyên nhân trạng thái filtered nhìn từ Kali; đồng thời xác thực rằng máy chủ phía sau không hề thay đổi cấu hình hay bản vá (`FILTERED != PATCHED`).
15. **Overclaim bị cấm:**
    - CẤM che giấu hoặc sửa chữa xung đột nhãn quy tắc CF-11.
    - CẤM tuyên bố ảnh nhật ký chứng minh hoàn hảo named rule Block.
    - CẤM tuyên bố tường lửa đã làm cho máy chủ trở nên an toàn tuyệt đối hay đã vá lỗi.
    - CẤM khẳng định hai hệ thống có cùng wall clock time.
16. **Nối sang phần kế tiếp:** Sau khi đã hoàn tất đo đạc cả hai ca can thiệp độc lập (Case B và Case C), bước phân tích tổng hợp là đặt cả ba trạng thái cạnh nhau để đối chiếu toàn diện, trình bày tại Mục 3.7.

---

### MỤC 3.7. ĐỐI CHIẾU KẾT QUẢ CÁC TRẠNG THÁI THỰC NGHIỆM

#### 3.7.1. Đối chiếu trạng thái ban đầu và sau các can thiệp
1. **Đề mục:** `3.7.1. Đối chiếu trạng thái ban đầu và sau các can thiệp`
2. **Câu hỏi người đọc:** *Khi đặt ba trạng thái (Đường cơ sở, Tắt SMBv1, và Tường lửa pfSense) cạnh nhau trên cùng một bảng, sự khác biệt được thể hiện như thế nào?*
3. **Thông điệp chính:** Xây dựng ma trận so sánh đa chiều đối chiếu 3 trạng thái thực nghiệm trên 8 hàng dữ liệu kỹ thuật kế thừa từ bảng đã duyệt của đề tài: Lớp can thiệp, Cổng TCP 139 từ xa, Cổng TCP 445 từ xa, Phương ngữ SMB quan sát từ xa, Cấu hình giao thức SMBv1 cục bộ, Dịch vụ LanmanServer cục bộ, Trạng thái bản vá hệ thống cục bộ, và Phán quyết kiểm tra MS17-010 từ xa. Phản ánh trung thực rằng trong Case C không có phép đo phương ngữ từ xa nào được thực hiện (`NOT MEASURED`).
4. **Technical facts được phép dùng (F04, F08):**
   - Ma trận đối chiếu gồm 8 hàng dữ liệu đầy đủ:
     1) Lớp can thiệp: Baseline (Không can thiệp, Host-Only) vs Case B (Cấu hình máy chủ Windows) vs Case C (Đường thử nghiệm qua pfSense Bridge).
     2) Cổng TCP 139 từ xa: Baseline (`OPEN (syn-ack)`) vs Case B (`Không đo lại trong Case B / NOT REMEASURED`) vs Case C (`FILTERED (no-response)`).
     3) Cổng TCP 445 từ xa: Baseline (`OPEN (syn-ack)`) vs Case B (`OPEN`) vs Case C (`FILTERED (no-response)`).
     4) Phương ngữ SMB quan sát từ xa: Baseline (5 dialect: NT LM 0.12..3.0.2) vs Case B (4 dialect: 2.0.2..3.0.2; NT LM 0.12 vắng mặt) vs Case C (**`Không có phép đo tương ứng trong Case C / NOT MEASURED`** — không điền "Không tiếp cận được").
     5) Cấu hình SMBv1 cục bộ (`EnableSMB1Protocol`): Baseline (`True`) vs Case B (`False`) vs Case C (`True`).
     6) LanmanServer cục bộ: Baseline (`Running`) vs Case B (`Running tại thời điểm kiểm tra`) vs Case C (`Running trạng thái ghi nhận cuối lượt`).
     7) Trạng thái bản vá hệ thống cục bộ (`srv.sys`): Cả 3 trạng thái đều là `UNPATCHED` (Case B và Case C không ghi nhận thao tác cài bản vá).
     8) Phán quyết MS17-010 từ xa: Cả 3 trạng thái đều là `UNKNOWN / NO USABLE SCRIPT RESULT`.
5. **Direct evidence tương ứng:** Tổng hợp đối chiếu chéo từ 78 tệp chứng cứ sơ cấp và 5 tệp chứng cứ thứ cấp đã kiểm toán.
6. **Supporting evidence:** `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md` (Mục 6).
7. **Bảng cần dùng:** **Bảng 3.7** (Bảng ma trận so sánh trạng thái thực nghiệm giữa đường cơ sở, Case B và Case C — 8 hàng dữ liệu chuẩn hóa).
8. **Hình cần dùng:** Không dùng hình tại tiểu mục này (tập trung vào bảng ma trận số liệu).
9. **Loại hình:** Không áp dụng.
10. **Hướng dẫn crop:** Không áp dụng.
11. **Ghép panel:** Không áp dụng.
12. **Caption dự kiến:** Không áp dụng.
13. **Ranh giới caption:** Không áp dụng.
14. **Ranh giới kết luận section:** Khẳng định mỗi biện pháp can thiệp tạo ra một hiệu ứng kỹ thuật hoàn toàn khác biệt trên bề mặt mạng và cấu hình dịch vụ, nhưng điểm chung bất biến là không biện pháp nào thay đổi trạng thái bản vá nội tại của máy chủ.
15. **Overclaim bị cấm:**
    - CẤM xếp hạng biện pháp nào "tốt hơn" hay "hiệu quả hơn" (không effectiveness ranking mang tính chủ quan).
    - CẤM tuyên bố một trong hai biện pháp có thể thay thế hoàn toàn việc cập nhật bản vá.
16. **Nối sang phần kế tiếp:** Từ bảng ma trận so sánh, bước phân tích sâu tiếp theo là phân lập rõ ràng giữa những yếu tố đã thay đổi và những yếu tố bất biến, trình bày tại Mục 3.7.2.

---

#### 3.7.2. Những thay đổi và yếu tố không thay đổi
1. **Đề mục:** `3.7.2. Những thay đổi và yếu tố không thay đổi`
2. **Câu hỏi người đọc:** *Bản chất kỹ thuật của hai vị trí can thiệp (tại máy chủ vs. trên đường mạng) là gì, và tại sao cả hai đều không thay thế được bản vá?*
3. **Thông điệp chính:** Phân định rạch ròi hai vị trí can thiệp an ninh độc lập:
   - *Yếu tố thay đổi:* Case B tác động tại Lớp máy chủ (Host Layer), làm thay đổi danh mục phương ngữ quan sát được từ xa (loại bỏ NT LM 0.12) nhưng để ngỏ cổng 445; Case C tác động tại Lớp đường truyền mạng (Network Path Layer), làm thay đổi trạng thái tiếp cận cổng (chuyển sang filtered) nhưng giữ nguyên dịch vụ máy chủ phía sau.
   - *Yếu tố bất biến:* Trong cả hai trường hợp, mã nhị phân driver nhân `srv.sys` hoàn toàn không thay đổi (`UNPATCHED`). Cả hai giải pháp đều là các biện pháp giảm thiểu bù đắp độc lập, không phải là giải pháp khắc phục tận gốc mã nguồn hệ điều hành.
4. **Technical facts được phép dùng (F07):**
   - Phân định hai vị trí can thiệp: Host Layer (Lớp máy chủ) vs. Network Path Layer (Lớp đường truyền mạng).
   - Tái khẳng định 5 tiên đề chân lý kỹ thuật.
   - Nhấn mạnh tính độc lập giữa quan sát mạng và bản vá nhân hệ điều hành.
   - Hai vị trí can thiệp được đo đạc độc lập trong lab; không suy diễn thành cấu hình kết hợp đã thử nghiệm cùng lúc.
5. **Direct evidence tương ứng:** Dữ liệu so sánh tổng hợp từ Bảng 3.7.
6. **Supporting evidence:** `work/do-an/CHAPTER_2.md` (Mục 2.5.1, 2.6.3).
7. **Bảng cần dùng:** Không dùng bảng mới (dựa trên Bảng 3.7).
8. **Hình cần dùng:** **Hình 3.14** (Sơ đồ phân định hai vị trí can thiệp phòng thủ trong mô hình thực nghiệm).
9. **Loại hình:** **Explanatory Figure** (Sơ đồ giải thích hai tầng can thiệp độc lập: Host Layer vs. Network Path Layer).
10. **Hướng dẫn thiết kế:** Sơ đồ vector thể hiện trực quan máy chủ Windows Server với hai vị trí tác động độc lập: Vị trí 1 (Cấu hình tắt SMBv1 bên trong OS - Case B) và Vị trí 2 (Tường lửa pfSense lọc gói tin trên đường truyền mạng - Case C). Không thể hiện như một kiến trúc gộp đã kích hoạt đồng thời trong cùng một phép đo.
11. **Ghép panel:** Không ghép ảnh; sơ đồ khối kiến trúc chuẩn khoa học.
12. **Caption dự kiến:** `Hình 3.14. Sơ đồ phân định hai vị trí can thiệp giảm thiểu rủi ro độc lập: Lớp cấu hình máy chủ nội bộ và Lớp kiểm soát đường truyền mạng`
13. **Ranh giới caption:** Chú thích chỉ mô tả hai vị trí tác động vật lý/logic của hai giải pháp; không đưa ra kết luận đánh giá mức độ an toàn.
14. **Ranh giới kết luận section (F07):** Dừng lại ở kết luận khoa học cốt lõi: các giải pháp giảm thiểu ở tầng giao thức hay tầng mạng chỉ thay đổi diện mạo quan sát bên ngoài, không giải quyết được lỗ hổng tiềm ẩn bên trong nếu hệ điều hành chưa được cập nhật bản vá. Toàn bộ các phân tích về chiến lược phòng thủ theo chiều sâu (Defense-in-Depth), ma trận đánh giá rủi ro doanh nghiệp, hay khuyến nghị kiến trúc an toàn thông tin thuộc phạm vi thảo luận của **Chương 4**.
15. **Overclaim bị cấm:**
    - CẤM đưa ra các khuyến nghị chiến lược phòng thủ theo chiều sâu (Defense-in-Depth) mang tính quản trị doanh nghiệp (dành cho Chương 4).
    - CẤM đưa ra các công thức tính điểm rủi ro (risk score) hay ma trận mức độ nghiêm trọng.
    - CẤM mô tả hai giải pháp như một hệ thống kết hợp đã được đo đạc cùng lúc trong thực nghiệm.
16. **Nối sang phần kế tiếp:** Toàn bộ các phát hiện thực nghiệm và ranh giới kỹ thuật được tổng kết cô đọng tại Mục 3.8 để khép lại Chương 3 và chuyển giao dữ kiện sạch sang Chương 4.

---

### MỤC 3.8. TỔNG KẾT CHƯƠNG

1. **Đề mục:** `3.8. Tổng kết chương`
2. **Câu hỏi người đọc:** *Chương 3 đã đạt được những kết quả cụ thể nào và chuyển giao dữ kiện gì cho Chương 4 thảo luận?*
3. **Thông điệp chính:** Tóm lược cô đọng toàn bộ các phát hiện thực nghiệm cốt lõi của Chương 3 qua 5 điểm then chốt: (1) Xác lập thành công mốc chuẩn xuất phát với máy chủ UNPATCHED; (2) Nhận diện đầy đủ diện mạo dịch vụ SMB và sự hiện diện của SMBv1 qua Nmap; (3) Xác lập phán quyết UNKNOWN từ xa và chứng minh tính độc lập với trạng thái bản vá nội bộ; (4) Đo đạc đối chứng hiệu quả loại bỏ phương ngữ cũ của Case B; (5) Đo đạc đối chứng hiệu quả lọc gói tin có ghi nhật ký của Case C; qua đó bàn giao toàn bộ cơ sở dữ kiện thực nghiệm khách quan cho Chương 4 tiến hành phân tích rủi ro và thảo luận các giải pháp bảo đảm an toàn thông tin.
4. **Technical facts được phép dùng:**
   - Tóm lược 5 phát hiện chính dựa trên dữ liệu đã được chứng minh tại Mục 3.2 đến 3.7.
   - Tái khẳng định tính toàn vẹn và khả năng truy vết của 83 tệp chứng cứ thực nghiệm (78 primary + 5 secondary).
   - Tuyệt đối không bổ sung dữ liệu mới hay suy diễn mới.
5. **Direct evidence tương ứng:** Toàn bộ kết quả thực nghiệm đã trình bày trong Chương 3.
6. **Supporting evidence:** `work/do-an/RESEARCH_MAP.md` (Mục tiêu O4).
7. **Bảng cần dùng:** Không dùng bảng biểu mới.
8. **Hình cần dùng:** Không dùng hình ảnh mới.
9. **Loại hình:** Không áp dụng.
10. **Hướng dẫn crop:** Không áp dụng.
11. **Ghép panel:** Không áp dụng.
12. **Caption dự kiến:** Không áp dụng.
13. **Ranh giới caption:** Không áp dụng.
14. **Ranh giới kết luận section:** Khép lại toàn bộ nội dung báo cáo kết quả thực nghiệm một cách khiêm tốn, khách quan, chuẩn mực học thuật; tạo cầu nối logic tự nhiên sang Chương 4.
15. **Overclaim bị cấm:**
    - CẤM lấn sân sang nội dung đánh giá rủi ro doanh nghiệp, phân tích nguyên nhân gốc rễ, hay đề xuất chính sách quản lý bản vá (nội dung thuộc Chương 4).
    - CẤM tuyên bố công trình đã giải quyết hoàn toàn bài toán an ninh SMB.
16. **Nối sang phần kế tiếp:** Mở ra không gian cho Chương 4 thảo luận về ý nghĩa của các kết quả thực nghiệm đối với công tác bảo đảm an toàn thông tin trong thực tế hạ tầng công nghệ thông tin.

---

## 3. BẢNG TỔNG HỢP KIỂM TOÁN VÀ ĐÁNH GIÁ BỘ ẢNH BẰNG CHỨNG (34 ẢNH CANONICAL)

Toàn bộ 34 tệp ảnh bằng chứng trực tiếp trong 5 thư mục canonical đã được rà soát chi tiết và phân loại quyết định sử dụng chuẩn xác (F08):

| STT | Tệp ảnh canonical nguồn | Thư mục | Quyết định trong Blueprint | Phân loại hình / Vai trò | Lý do quyết định kỹ thuật |
|---|---|---|---|---|---|
| 1 | `Windows_PreDemo_01_Network_SMB.png` | `baseline/` | **KEEP** | Evidence Figure (Hình 3.2) | Minh chứng trực tiếp IP .56.20, LanmanServer Running, FS-SMB1 Installed, Socket 139/445 Listen. |
| 2 | `Windows_PreDemo_02_Firewall.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Minh chứng cấu hình rule tùy biến; nội dung số liệu đã được tổng hợp trọn vẹn trong Bảng 3.1. |
| 3 | `Windows_Baseline_01_Winver.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Xác nhận Windows Server 2012 R2 Build 9600; Bảng 3.1 đã ghi nhận thông số này. |
| 4 | `Windows_Baseline_04_SMB_Service.png` | `baseline/` | **RETIRE FROM MAIN TEXT** | Historical Context | Đã được bao hàm trọn vẹn và sắc nét hơn trong `Windows_PreDemo_01_Network_SMB.png`. |
| 5 | `Windows_Baseline_05_SMB_Features.png` | `baseline/` | **RETIRE FROM MAIN TEXT** | Historical Context | Đã được bao hàm trọn vẹn trong `Windows_PreDemo_01_Network_SMB.png` (dòng Get-WindowsFeature). |
| 6 | `Windows_Baseline_06_SMB_Config.png` | `baseline/` | **RETIRE FROM MAIN TEXT** | Historical Context | Thông số EnableSMB1/2Protocol đã được Bảng 3.1 tổng hợp và thể hiện ở PreDemo. |
| 7 | `Windows_Baseline_07_Firewall.png` | `baseline/` | **RETIRE FROM MAIN TEXT** | Historical Context | Trạng thái Firewall profile đã được chứng minh trong `Windows_PreDemo_02_Firewall.png`. |
| 8 | `Windows_FirewallPrep_04_Scope.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Minh chứng RemoteAddress Scope 192.168.56.10; lưu trữ đối soát cho Bảng 3.1. |
| 9 | `Windows_MS17010_01_SrvSysVersion.png` | `baseline/` | **MERGE** | Comparison Panel A (Hình 3.3) | Minh chứng cửa sổ PowerShell: FileVersion hiển thị `6.3.9600.16384` và lệnh ghép 4 trường số cho kết quả số `6.3.9600.16421`. |
| 10 | `Windows_MS17010_02_Hotfix.png` | `baseline/` | **MERGE** | Comparison Panel B (Hình 3.3) | Minh chứng cửa sổ PowerShell hiển thị danh mục 6 hotfix năm 2014, thiếu vắng bản vá MS17-010. |
| 11 | `Kali_PreDemo_01_Network_Tools.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Minh chứng IP Kali và phiên bản Nmap 7.99; Bảng 3.1 đã phản ánh đầy đủ. |
| 12 | `Kali_PreDemo_02_NSE_Scripts.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Minh chứng sự sẵn sàng của các tệp script NSE trong Kali; lưu trữ đối soát. |
| 13 | `Kali_to_Windows_Connectivity.png` | `baseline/` | **SUPPORTING** | Supporting Visual | Minh chứng ping hai chiều liên thông; Bảng 3.1 và text đã ghi nhận. |
| 14 | `Scenario1_B4_SMB_Ports.png` | `scenario1/` | **KEEP** | Evidence Figure (Hình 3.4) | Minh chứng cốt lõi: cổng 139 và 445 open kèm cờ `syn-ack ttl 128`. Thêm từ evidence sẵn có vào main text. |
| 15 | `Scenario1_B5_SMB_Version.png` | `scenario1/` | **MERGE** | Comparison Panel A (Hình 3.5) | Minh chứng dải fingerprint dịch vụ `Windows Server 2008 R2 - 2012` (vốn là Hình 3.4 trong bản thảo cũ). |
| 16 | `Scenario1_B6_SMB_NSE_A.png` | `scenario1/` | **MERGE** | Comparison Panel B (Hình 3.5) | Minh chứng 5 phương ngữ SMB, capabilities và signing policy (vốn là Hình 3.5 trong bản thảo cũ). |
| 17 | `Scenario2_NSE01_Ports.png` | `scenario2/` | **SUPPORTING** | Supporting Visual | Tái xác nhận cổng mở; kết quả này đã được chứng minh trực quan bởi Hình 3.4 (Scenario 1). |
| 18 | `Scenario2_NSE02_Protocols.png` | `scenario2/` | **SUPPORTING** | Supporting Visual | Tái xác nhận 5 dialect; kết quả này đã được chứng minh trực quan bởi Hình 3.5 (Scenario 1). |
| 19 | `Scenario2_NSE03_Signing.png` | `scenario2/` | **SUPPORTING** | Supporting Visual | Tái xác nhận thuộc tính signing; kết quả này đã được bao hàm trong Bảng 3.4 và Hình 3.5. |
| 20 | `Scenario2_NSE04_MS17010.png` | `scenario2/` | **KEEP** | Evidence Figure (Hình 3.6 & Hình 3.7) | Bằng chứng trung tâm của Mục 3.4: cổng 445 open, Nmap hoàn tất, không có khối kết quả script (UNKNOWN). |
| 21 | `SMBv1_Remediation_01_Before.png` | `case_b/` | **MERGE** | Action Panel 1 (Hình 3.8) | Panel 1 của chuỗi thao tác Case B: Cấu hình trước can thiệp (EnableSMB1Protocol : True). |
| 22 | `SMBv1_Remediation_02_Action.png` | `case_b/` | **MERGE** | Action Panel 2 (Hình 3.8) | Panel 2 của chuỗi thao tác Case B: Lệnh PowerShell thực thi `Set-SmbServerConfiguration`. |
| 23 | `SMBv1_Remediation_03_After_Local.png` | `case_b/` | **MERGE** | Action Panel 3 (Hình 3.8) | Panel 3 của chuỗi thao tác Case B: Cấu hình sau can thiệp (EnableSMB1Protocol : False, LanmanServer Running point-in-time). |
| 24 | `SMBv1_Remediation_04_NSE02_Protocols.png` | `case_b/` | **KEEP** | Evidence Figure (Hình 3.9) | Bằng chứng đo lại cốt lõi của Case B: phương ngữ NT LM 0.12 biến mất khỏi danh sách đàm phán quan sát được. |
| 25 | `SMBv1_Remediation_05_NSE04_MS17010.png` | `case_b/` | **SUPPORTING** | Supporting Visual | Đo lại MS17-010 tiếp tục UNKNOWN; Bảng 3.5 đã ghi nhận đầy đủ, tránh lặp screenshot. |
| 26 | `pfSense_03_Interface_Assignment.png` | `case_c/` | **SUPPORTING** | Supporting Visual | Minh chứng gán interface em2/em3; Bảng 3.6 và Hình 3.10 đã thể hiện kiến trúc. |
| 27 | `pfSense_04_Bridge.png` | `case_c/` | **SUPPORTING** | Supporting Visual | Minh chứng cấu hình bridge0; Bảng 3.6 và Hình 3.10 đã thể hiện kiến trúc. |
| 28 | `pfSense_05_Bridge_Filtering.png` | `case_c/` | **SUPPORTING** | Supporting Visual | Minh chứng tunables pfil_member=1; Bảng 3.6 đã ghi nhận. |
| 29 | `pfSense_06_Baseline_Pass_Rule.png` | `case_c/` | **RETIRE FROM MAIN TEXT** | Historical Context | Đã được bao hàm trọn vẹn trong `pfSense_08_Rule_Order.png` (hàng Pass bên dưới hàng Block). |
| 30 | `pfSense_07_Block_Rule_Config.png` | `case_c/` | **SUPPORTING** | Supporting Visual | Chi tiết form cấu hình quy tắc Block; lưu trữ đối soát cho Hình 3.11 và Bảng 3.6. |
| 31 | `pfSense_08_Rule_Order.png` | `case_c/` | **KEEP** | Evidence Figure (Hình 3.11) | Minh chứng cốt lõi cấu hình Case C: Hàng Block SMB đặt trên hàng Baseline Pass có bật Log. |
| 32 | `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | `case_c/` | **KEEP** | Evidence Figure (Hình 3.12) | Bằng chứng đo lại cốt lõi của Case C: Cổng 139 và 445 chuyển sang trạng thái `filtered` do `no-response`. |
| 33 | `pfSense_10_Block_Log_CANONICAL.png` | `case_c/` | **KEEP** | Evidence Figure with Bounded Conflict (Hình 3.13) | Bằng chứng nhật ký cốt lõi của Case C: Ghi nhận sự kiện chặn gói TCP SYN tới cổng SMB (bảo lưu CF-11). |
| 34 | `pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | `case_c/` | **SUPPORTING** | Supporting Visual | Đo lại MS17-010 báo filtered; Bảng 3.6 đã ghi nhận đầy đủ, tránh lặp screenshot. |

---

## 4. TỔNG KẾT PHÂN BỔ THỊ GIÁC TOÀN CHƯƠNG (RECONCILED AUDIT)

- **Tổng số ảnh canonical đã kiểm toán:** **34 ảnh** (33 `PRIMARY_VISUAL` + 1 `PRIMARY_VISUAL_WITH_BOUNDED_CONFLICT`).
  - **Số ảnh chọn làm bằng chứng chính độc lập (KEEP):** **7 ảnh** (`Windows_PreDemo_01_Network_SMB.png`, `Scenario1_B4_SMB_Ports.png`, `Scenario2_NSE04_MS17010.png`, `SMBv1_Remediation_04_NSE02_Protocols.png`, `pfSense_08_Rule_Order.png`, `pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`, `pfSense_10_Block_Log_CANONICAL.png`).
  - **Số ảnh tham gia vào các cụm ghép (MERGE vào các Panel/Comparison):** **7 ảnh** (`Windows_MS17010_01_SrvSysVersion.png`, `Windows_MS17010_02_Hotfix.png`, `Scenario1_B5_SMB_Version.png`, `Scenario1_B6_SMB_NSE_A.png`, `SMBv1_Remediation_01_Before.png`, `SMBv1_Remediation_02_Action.png`, `SMBv1_Remediation_03_After_Local.png`).
  - **Số ảnh xếp vào kho bằng chứng bổ trợ (SUPPORTING VISUAL):** **15 ảnh** (Lưu giữ đầy đủ trong repo, phục vụ đối soát và thẩm định độc lập, không đưa trực tiếp vào luồng đọc chính để chống phân mảnh).
  - **Số ảnh loại bỏ khỏi luồng đọc chính do trùng lặp nội dung (RETIRE FROM MAIN TEXT):** **5 ảnh** (`Windows_Baseline_04_SMB_Service.png`, `Windows_Baseline_05_SMB_Features.png`, `Windows_Baseline_06_SMB_Config.png`, `Windows_Baseline_07_Firewall.png`, `pfSense_06_Baseline_Pass_Rule.png` — tất cả đều đã được thay thế bằng các ảnh `PreDemo` và `Rule_Order` bao quát và chuẩn hóa hơn).
  - *Kiểm tra tổng cộng:* $7 + 7 + 15 + 5 = 34$ ảnh.
- **Số hình giải thích mới đề xuất dựng (NEW Explanatory Figures):** **3 hình** (Hình 3.1: Luồng thực nghiệm hai nhánh độc lập; Hình 3.10: Mô hình kiến trúc Transparent Bridge; Hình 3.14: Sơ đồ phân định hai vị trí can thiệp độc lập).
- **Tổng số hình đề xuất trong bản thảo Chương 3 mới:** **14 hình** (7 Evidence figures + 4 Comparison figures + 3 Explanatory figures).
- **Tổng số bảng đề xuất trong bản thảo Chương 3 mới:** **7 bảng** (Bảng 3.1 đến Bảng 3.7; Bảng 3.7 giữ nguyên vẹn 8 hàng dữ liệu chuẩn hóa của đề tài).
- **Phân loại 83 tệp chứng cứ staging:** 78 tệp chứng cứ sơ cấp (primary/direct evidence) + 5 tệp chứng cứ thứ cấp (secondary metadata/closure).
