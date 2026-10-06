# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.4 CASE B (CH3_34_CASEB_PRESENTATION_PLAN_R1)

- **Trạng thái:** `R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7D0 R1 — Case B Evidence & Presentation Plan`
- **Ràng buộc cốt lõi:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI BÁO CÁO (ZERO REPORT PROSE)**. Tài liệu này chỉ thiết kế câu hỏi người đọc, cấu trúc tiểu mục H3, thiết kế bảng biểu so sánh trước/sau theo định hướng kết quả (result-oriented), kế hoạch bố trí hình ảnh kèm ranh giới diễn giải và khung cắt cúp dự kiến có thể tái lập, phân định rạch ròi 4 tầng an ninh độc lập, và xác lập chuyển tiếp ý niệm sang Kịch bản tiếp theo (Case C).

---

## 1. Câu Hỏi Trọng Tâm Dành Cho Người Đọc Luận Văn (Reader Question)

> *Khi biện pháp vô hiệu hóa giao thức SMBv1 được áp dụng trên máy chủ Windows Server 2012 R2 thông qua thay đổi cấu hình dịch vụ, những thuộc tính cấu hình và trạng thái nào của hệ thống thay đổi, những thành phần nào duy trì nguyên vẹn ở mức cục bộ, danh sách phương ngữ đàm phán ghi nhận từ xa qua mạng phản ánh sự biến đổi ra sao, và kết quả đo đạc lại bằng kịch bản kiểm tra MS17-010 xác lập được những giới hạn kỹ thuật gì mà không được đánh đồng với việc hệ thống đã được cập nhật bản vá hay trở nên an toàn?*

Câu hỏi này định hình Mục 3.4 thành một **nghiên cứu thực nghiệm so sánh đối chứng có kiểm soát chặt chẽ (controlled comparative experiment)**:
1. Làm rõ thao tác can thiệp: chỉ là thay đổi cấu hình máy chủ (`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`), không phải cập nhật bản vá (`patch`), không phải gỡ bỏ tính năng (`feature uninstall`), không phải nâng cấp driver hay hệ điều hành.
2. Xác lập tính toàn vẹn của hiện trạng cục bộ sau can thiệp: `EnableSMB1Protocol` chuyển thành `False`, nhưng `EnableSMB2Protocol` giữ `True`, `FS-SMB1` vẫn `Installed`, `LanmanServer` tiếp tục `Running`, và tệp driver nhân `srv.sys` vẫn chưa vá (`UNPATCHED`).
3. Khảo sát hiệu ứng mạng quan sát được từ xa: cổng 445 vẫn mở, phương ngữ cũ `NT LM 0.12 (SMBv1)` biến mất khỏi danh sách đàm phán, trong khi các phương ngữ SMB2/3 (`2.0.2`, `2.1`, `3.0`, `3.0.2`) vẫn tiếp tục được ghi nhận.
4. Trình bày trung thực kết quả đo lại kịch bản `smb-vuln-ms17-010`: tiếp tục hoàn tất mà không có phán quyết kịch bản khả dụng (`UNKNOWN / NO USABLE SCRIPT RESULT`), duy trì nguyên tắc bất định `UNKNOWN != SAFE`, và giữ vững ranh giới độc lập giữa 4 tầng kỹ thuật.

---

## 2. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

### 2.1. Đánh giá các phương án phân chia tiểu mục
- **Phương án 4 tiểu mục (1 H3 cho mỗi tệp/lệnh):** Chia cắt quá vụn vặt văn bản, biến báo cáo thành nhật ký thao tác dòng lệnh (command log), làm mờ nhạt tính hệ thống của quy trình can thiệp và đo đạc lại.
- **Phương án 3 tiểu mục (Trước can thiệp, Thao tác & Kiểm tra cục bộ, Đo đạc lại từ xa):** Tiểu mục "Trước can thiệp" sẽ bị trùng lặp lớn với dữ liệu baseline đã trình bày ở Mục 3.1 và Mục 3.2, gây lãng phí dung lượng.
- **Phương án 2 tiểu mục (Khuyến nghị chính thức):** Nhóm theo hai cụm tư duy kỹ thuật mạch lạc và đối xứng: (1) Thao tác can thiệp và kiểm chứng trạng thái máy chủ cục bộ; (2) Đo đạc lại từ xa qua mạng và đối chiếu đa tầng. Bố cục này đồng bộ hoàn hảo với quy mô 2 H3 đã được phê chuẩn tại Mục 3.1, Mục 3.2 và Mục 3.3.

### 2.2. Bố cục đề xuất chính thức

### `3.4. Kết quả Case B — Vô hiệu hóa SMBv1 và đo lại từ xa`

- **`3.4.1. Thao tác vô hiệu hóa SMBv1 và kiểm tra trạng thái máy chủ cục bộ`**
  * *Nội dung kỹ thuật:*
    - Trình bày ngắn gọn mốc xuất phát cục bộ trước can thiệp: dịch vụ `LanmanServer` đang chạy, tính năng `FS-SMB1` đã cài đặt, cả hai cờ `EnableSMB1Protocol` và `EnableSMB2Protocol` đều ở trạng thái `True`.
    - Trình bày thao tác can thiệp: thực thi lệnh PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` nhằm vô hiệu hóa giao thức SMBv1 ở mức cấu hình máy chủ chia sẻ tệp.
    - Trình bày kết quả kiểm tra cục bộ ngay sau can thiệp: `EnableSMB1Protocol` chuyển thành `False`; `EnableSMB2Protocol` duy trì `True`; tính năng `FS-SMB1` vẫn ở trạng thái `Installed`; dịch vụ `LanmanServer` tiếp tục `Running`.
    - Phân tích ranh giới kỹ thuật cục bộ:
      * Khẳng định việc tắt cấu hình SMBv1 hoàn toàn **không đồng nghĩa** với việc gỡ bỏ gói tính năng `FS-SMB1` khỏi Windows Server (`SMBv1 disabled != FS-SMB1 uninstalled`).
      * Khẳng định việc thay đổi cấu hình máy chủ **không làm thay đổi tệp driver `srv.sys`**; trạng thái bản vá hệ thống cục bộ vẫn là **`UNPATCHED`** (`SMBv1 disabled != PATCHED`).
      * Làm rõ rằng sự tiếp tục hoạt động của dịch vụ `LanmanServer` không tự nó chứng minh toàn bộ các ứng dụng nghiệp vụ hay tải chia sẻ tệp hiện đại đều tương thích hoàn hảo và không gián đoạn.
  * *Phương thức thể hiện:* Sử dụng Hình 3.7 (minh chứng trực quan console PowerShell sau can thiệp) và nửa phần trên của Bảng 3.5; kết hợp văn xuôi chặt chẽ (bounded prose).

- **`3.4.2. Kết quả đo đạc lại từ xa và đối chiếu đa tầng`**
  * *Nội dung kỹ thuật:*
    - Trình bày kết quả đo đạc lại phương ngữ từ xa (NSE-SMB-02 retest): trạm Kali Linux thực thi lệnh Nmap với kịch bản `smb-protocols` nhắm vào cổng 445 của máy chủ mục tiêu; ghi nhận cổng `445/tcp` tiếp tục ở trạng thái `open`; danh sách phương ngữ đàm phán thành công gồm `2.0.2`, `2.1`, `3.0`, `3.0.2`; phương ngữ cũ `NT LM 0.12 (SMBv1)` hoàn toàn không còn xuất hiện.
    - Trình bày kết quả đo đạc lại kịch bản MS17-010 từ xa (NSE-SMB-04 retest): trạm Kali Linux thực thi lệnh Nmap với kịch bản `smb-vuln-ms17-010` nhắm vào cổng 445; phiên quét hoàn tất đạt đến dòng `Nmap done`, không xuất hiện khối kết quả `Host script results:`, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận.
    - Xác lập phân loại kỹ thuật từ xa: phán quyết đo đạc từ xa của kịch bản MS17-010 duy trì phân loại **`UNKNOWN / NO USABLE SCRIPT RESULT`**.
    - Phân tích ranh giới phương pháp luận và đối chiếu 4 tầng:
      * Khẳng định nguyên tắc bất định `UNKNOWN != SAFE`: việc kịch bản quét không in ra phán quyết lỗ hổng từ xa không đồng nghĩa với việc hệ thống mục tiêu đã an toàn hay đã miễn nhiễm.
      * Bác bỏ cụm từ suy diễn nguyên nhân trong manifest ("SMBv1 probe silenced"): không sử dụng cụm từ này làm sự thật khoa học hay lời giải thích nhân quả.
      * Phân định rạch ròi 4 tầng an ninh độc lập: (1) Cấu hình dịch vụ máy chủ; (2) Trạng thái cài đặt tính năng hệ thống; (3) Trạng thái bản vá mã nhị phân cục bộ; (4) Phán quyết kịch bản rà quét từ xa. Tuyệt đối không gộp 4 tầng này thành một "trạng thái an ninh" chung.
  * *Phương thức thể hiện:* Sử dụng Bảng 3.5 (bảng so sánh tổng hợp Trước/Sau); Hình 3.8 (minh chứng trực quan danh sách phương ngữ đo lại); phần lập luận ranh giới bằng văn xuôi nghiêm ngặt.

---

## 3. Thiết Kế Bảng Biểu Báo Cáo Sinh Viên (Student-Facing Tables)

Thiết kế **1 bảng tổng hợp duy nhất (Bảng 3.5)** theo định hướng kết quả (result-oriented), cô đọng toàn bộ tiến trình so sánh đối chứng của Case B.

### Bảng 3.5 — So sánh cấu hình và kết quả đo đạc trước và sau khi vô hiệu hóa SMBv1 (Case B)

- **Số hiệu dự kiến:** `Bảng 3.5` (Tiếp nối Bảng 3.1, 3.2 của Mục 3.1, Bảng 3.3 của Mục 3.2, và Bảng 3.4 của Mục 3.3).
- **Câu hỏi của người đọc được trả lời:** *Khi thực hiện vô hiệu hóa SMBv1 trên máy chủ mục tiêu, các thông số cấu hình cục bộ, trạng thái tính năng, dịch vụ chia sẻ tệp, khả năng phản hồi mạng và phán quyết rà quét từ xa biến đổi như thế nào so với mốc xuất phát ban đầu?*
- **Cấu trúc cột chuẩn hóa:** `Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case B) | Diễn giải trực tiếp & Giới hạn kết luận`

| Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case B) | Diễn giải trực tiếp & Giới hạn kết luận |
|---|---|---|---|
| **Cấu hình máy chủ SMBv1**<br>(`EnableSMB1Protocol`) | `True`<br>(Đang kích hoạt) | `False`<br>(Đã vô hiệu hóa) | **Cấu hình máy chủ đã thay đổi**<br>Giao thức SMBv1 đã chuyển từ trạng thái kích hoạt sang vô hiệu hóa ở mức cấu hình dịch vụ máy chủ thông qua lệnh can thiệp PowerShell. |
| **Cấu hình máy chủ SMB2/3**<br>(`EnableSMB2Protocol`) | `True`<br>(Đang kích hoạt) | `True`<br>(Duy trì kích hoạt) | **Cấu hình SMB thế hệ mới giữ nguyên**<br>Cấu hình máy chủ tiếp tục cho phép đàm phán các phương ngữ SMB2 và SMB3 hiện đại; không bị tác động bởi lệnh tắt SMBv1. |
| **Tính năng hệ điều hành**<br>(`FS-SMB1`) | `Installed`<br>(Đã cài đặt) | `Installed`<br>(Vẫn duy trì cài đặt) | **Tính năng Windows không bị gỡ bỏ**<br>Gói tính năng `FS-SMB1` vẫn hiện diện trên hệ điều hành. Can thiệp cấu hình máy chủ không đồng nghĩa với việc gỡ bỏ tính năng (`SMBv1 disabled != FS-SMB1 uninstalled`). |
| **Dịch vụ chia sẻ tệp**<br>(`LanmanServer`) | `Running`<br>(Đang hoạt động) | `Running`<br>(Tiếp tục hoạt động) | **Dịch vụ máy chủ không bị gián đoạn tiến trình**<br>Tiến trình dịch vụ `LanmanServer` tiếp tục duy trì trạng thái hoạt động. Dữ kiện này không chứng minh toàn bộ các ứng dụng nghiệp vụ hiện đại đều tương thích hoàn hảo. |
| **Trạng thái cổng dịch vụ từ xa**<br>(Cổng TCP 445 từ Kali) | `OPEN`<br>(Phản hồi `syn-ack`) | `OPEN`<br>(Phản hồi `syn-ack`) | **Cổng dịch vụ tiếp tục tiếp cận được**<br>Cổng 445/tcp tiếp tục mở và tiếp nhận kết nối qua mạng từ trạm Kali. Trạng thái cổng mở không đồng nghĩa với tồn tại lỗ hổng (`445 OPEN != vulnerable`). |
| **Phương ngữ SMB ghi nhận từ xa**<br>(Kịch bản `smb-protocols`) | 5 phương ngữ:<br>• `NT LM 0.12 (SMBv1)`<br>• `2.0.2`, `2.1`<br>• `3.0`, `3.0.2` | 4 phương ngữ:<br>• `2.0.2`, `2.1`<br>• `3.0`, `3.0.2`<br>(`NT LM 0.12` vắng mặt) | **SMBv1 không còn xuất hiện trong đàm phán**<br>Phương ngữ SMBv1 cũ không còn xuất hiện trong danh sách phương ngữ đàm phán được đo lại; các phương ngữ SMB2/3 vẫn được ghi nhận. Không suy diễn toàn bộ workload thực tế đã được kiểm chứng. |
| **Phán quyết kiểm tra MS17-010**<br>(Kịch bản `smb-vuln-ms17-010`) | `UNKNOWN`<br>(Không có kết quả script) | `UNKNOWN`<br>(Không có kết quả script) | **Phán quyết từ xa duy trì không xác định**<br>Phiên quét hoàn tất đạt `Nmap done`, cổng 445 mở, không xuất hiện khối `Host script results:`. Phân loại từ xa là `UNKNOWN / NO USABLE SCRIPT RESULT`. `UNKNOWN != SAFE`. |
| **Trạng thái bản vá hệ thống**<br>(Mã nhị phân driver `srv.sys`) | `UNPATCHED`<br>(Phiên bản `6.3.9600.16421`) | `UNPATCHED`<br>(Phiên bản `6.3.9600.16421`) | **Trạng thái bản vá không thay đổi**<br>Tệp driver nhân `srv.sys` giữ nguyên phiên bản chưa vá, danh mục hotfix không thay đổi. Vô hiệu hóa SMBv1 không đồng nghĩa với cập nhật bản vá (`SMBv1 disabled != PATCHED`). |

### Quy tắc nghiêm ngặt đối với Bảng 3.5:
- **ĐƯỢC PHÉP:** Sử dụng các nhãn tham số chuẩn hóa (`EnableSMB1Protocol`, `EnableSMB2Protocol`, `FS-SMB1`, `LanmanServer`, `smb-protocols`, `smb-vuln-ms17-010`, `srv.sys`).
- **CẤM:** Không đưa cú pháp dòng lệnh thô hoặc chuỗi đối số argv của Nmap (`--privileged`, `-T3`, `--max-retries 2`, `-oA ...`).
- **CẤM:** Không đưa mã định danh quản trị nội bộ như Stable Evidence ID (`B-LOCAL-*`, `B-RAW-*`, `CB-*`), Claim ID (`CB-C*`), hay đường dẫn tệp trong kho lưu trữ (`case_b/NSE-SMB-02_protocols.nmap`).
- **CẤM:** Không gán nhãn "unchanged" (không thay đổi) cho các tham số không có bằng chứng trực tiếp hỗ trợ trong lần đo Case B.
- **CẤM:** Không đưa các phán quyết ngoài phạm vi bằng chứng như `PATCHED`, `SAFE`, `NOT VULNERABLE`, `VULNERABILITY FIXED`, `RISK ELIMINATED`.

---

## 4. Kế Hoạch Bố Trí Hình Ảnh (Figure Placement Directives)

Theo kết quả thẩm tra tại `CH3_34_CASEB_FIGURE_SELECTION_R1.md`, bố trí **2 hình ảnh (Hình 3.7 và Hình 3.8)**:

### 4.1. Hình 3.7 (Tạm thời) — Trạng thái cấu hình máy chủ, tính năng hệ thống và dịch vụ LanmanServer cục bộ sau khi vô hiệu hóa SMBv1
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.4.1`, ngay sau đoạn phân tích kết quả thay đổi cấu hình máy chủ cục bộ.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.7 thể hiện giao diện bảng điều khiển PowerShell trên máy chủ Windows Server 2012 R2 ghi nhận trạng thái cấu hình giao thức SMB, tính năng hệ thống và dịch vụ chia sẻ tệp ngay sau khi thực thi lệnh vô hiệu hóa SMBv1."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Lệnh `Get-SmbServerConfiguration` ghi nhận thuộc tính `EnableSMB1Protocol` hiển thị giá trị `False`, trong khi `EnableSMB2Protocol` hiển thị giá trị `True`.
  2. Lệnh `Get-WindowsFeature FS-SMB1` ghi nhận tính năng hỗ trợ chia sẻ tệp SMB 1.x (`SMB 1.x/CIFS File Sharing Support`) vẫn ở trạng thái cài đặt (`Installed`).
  3. Lệnh `Get-Service LanmanServer` ghi nhận dịch vụ `Server` (`LanmanServer`) tiếp tục ở trạng thái đang hoạt động (`Status: Running`).
  4. Dấu nhắc lệnh trở lại bình thường và không xuất hiện thông báo lỗi.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh tính năng SMBv1 đã bị gỡ bỏ khỏi hệ điều hành Windows (`SMBv1 disabled != FS-SMB1 uninstalled`).
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh hệ điều hành đã được cài đặt bản vá bảo mật MS17-010 (`SMBv1 disabled != PATCHED`).
  * **CẤM:** Không được tuyên bố hình ảnh chứng minh dịch vụ chia sẻ tệp hoạt động bình thường cho mọi ứng dụng nghiệp vụ hay bảo đảm không có gián đoạn dịch vụ đối với người dùng cuối.
- **Khung cắt cúp đề xuất có thể tái lập:**
  * *Tệp nguồn:* `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_03_After_Local.png` ($1280 \times 800\,\text{px}$, SHA-256: `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad`).
  * *Tọa độ đề xuất:* `x = 0, y = 30, width = 1280, height = 730` (vùng `[left=0, top=30, right=1280, bottom=760]`).
  * *Vùng bảo toàn:* Toàn bộ các dòng lệnh và bảng dữ liệu trả về của 3 lệnh kiểm tra PowerShell.
  * *Giao diện loại bỏ:* Thanh tiêu đề cửa sổ console ($y < 30$) và thanh tác vụ Windows Server ở đáy màn hình ($y > 760$).

### 4.2. Hình 3.8 (Tạm thời) — Kết quả đo đạc lại các phương ngữ SMB từ trạm Kali Linux sau khi vô hiệu hóa SMBv1
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.4.2`, ngay sau đoạn mô tả phép đo đạc lại phương ngữ từ xa bằng kịch bản `smb-protocols`.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.8 thể hiện giao diện dòng lệnh và kết quả thực thi kịch bản smb-protocols nhắm vào cổng 445 của máy chủ mục tiêu từ trạm kiểm thử Kali Linux sau khi áp dụng biện pháp can thiệp Case B."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Lệnh Nmap được thực thi với tùy chọn `--script smb-protocols` nhắm vào cổng 445 tới IP mục tiêu `192.168.56.20`.
  2. Máy chủ mục tiêu trực tuyến (`Host is up`), cổng `445/tcp` tiếp tục ở trạng thái mở (`open microsoft-ds`).
  3. Khối kết quả `Host script results:` dưới kịch bản `smb-protocols` liệt kê đúng 4 phương ngữ: `2.0.2`, `2.1`, `3.0`, và `3.0.2`.
  4. Phương ngữ cũ `NT LM 0.12 (SMBv1)` hoàn toàn không còn xuất hiện trong danh sách phương ngữ ghi nhận được.
  5. Tiến trình quét hoàn tất với thông báo `Nmap done: 1 IP address (1 host up) scanned`.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh cổng 445 đã bị đóng hoặc dịch vụ SMB đã ngừng hoạt động qua mạng.
  * **CẤM:** Không được tuyên bố hình ảnh chứng minh giao thức SMBv1 đã bị "xóa bỏ hoàn toàn khỏi hệ điều hành".
  * **CẤM:** Không được tuyên bố toàn bộ các ứng dụng nghiệp vụ hiện đại sử dụng SMB2/3 đã được kiểm chứng hoạt động ổn định hay không xảy ra lỗi kết nối thực tế.
  * **CẤM:** Không đưa ra phán quyết về lỗ hổng MS17-010 từ hình ảnh kiểm tra phương ngữ này.
- **Khung cắt cúp đề xuất có thể tái lập:**
  * *Tệp nguồn:* `work/do-an/chapter3/evidence/case_b/SMBv1_Remediation_04_NSE02_Protocols.png` ($1280 \times 800\,\text{px}$, SHA-256: `21ed6473f4e7010841e9730620b159c272238cf7335eb80fcfaf4ad61f7a7b5a`).
  * *Tọa độ đề xuất:* `x = 0, y = 24, width = 1280, height = 360` (vùng `[left=0, top=24, right=1280, bottom=384]`).
  * *Vùng bảo toàn:* Dòng lệnh Nmap, trạng thái host/cổng, khối kết quả 4 phương ngữ SMB2/3, thông báo hoàn tất phiên quét `Nmap done`, và dấu nhắc lệnh tiếp theo.
  * *Giao diện loại bỏ:* Thanh panel trên cùng của desktop Kali XFCE ($y < 24$) và vùng không gian terminal đen trống phía dưới ($y > 384$).

---

## 5. Ranh Giới Ngôn Từ So Sánh Trước / Sau (Before/After Wording Boundaries)

Mục 3.4 là phần trình bày **kết quả thực nghiệm đối chứng**, không phải bản đánh giá hiệu quả an ninh tổng thể (dành cho Chương 4). Việc sử dụng từ ngữ phải tuân thủ nghiêm ngặt các ranh giới sau:

### 5.1. Khái niệm và cụm từ ĐƯỢC PHÉP sử dụng (Allowed wording concepts):
- *"thay đổi cấu hình SMBv1 quan sát được trên máy chủ"*
- *"cấu hình EnableSMB1Protocol chuyển từ True sang False"*
- *"tính năng FS-SMB1 vẫn duy trì trạng thái Installed trên hệ thống"*
- *"dịch vụ LanmanServer tiếp tục hoạt động"*
- *"sau can thiệp, phương ngữ NT LM 0.12 (SMBv1) không còn xuất hiện trong danh sách phương ngữ đàm phán của phép đo lại"*
- *"các phương ngữ SMB2/3 (2.0.2, 2.1, 3.0, 3.0.2) vẫn được ghi nhận từ trạm quét"*
- *"cổng 445/tcp tiếp tục mở và phản hồi gói tin SYN-ACK"*
- *"kết quả thực thi kịch bản smb-vuln-ms17-010 từ xa duy trì phân loại UNKNOWN / NO USABLE SCRIPT RESULT"*
- *"trạng thái bản vá hệ thống cục bộ vẫn được phân loại UNPATCHED dựa trên mốc chuẩn tệp driver srv.sys"*.

### 5.2. Khái niệm và tuyên bố BỊ NGHIÊM CẤM TUYỆT ĐỐI (Forbidden overclaims):
- **CẤM:** Không được viết *"biện pháp can thiệp đã loại bỏ lỗ hổng MS17-010"* hoặc *"đã khắc phục lỗ hổng"*.
- **CẤM:** Không được viết *"hệ thống đã trở nên an toàn"* (`system safe`) hoặc *"không còn nguy cơ tấn công"*.
- **CẤM:** Không được gọi việc tắt SMBv1 là *"đã cập nhật bản vá"* (`patched`) hoặc *"đã gỡ bỏ tính năng SMBv1"* (`feature uninstalled`).
- **CẤM:** Không sử dụng cụm từ trong manifest *"SMBv1 probe silenced"* làm sự thật khoa học hay lời giải thích nhân quả cho việc kịch bản NSE không có đầu ra.
- **CẤM:** Không được phỏng đoán các nguyên nhân không có trong log thô như *"không thể đàm phán SMBv1"* (`Couldn't negotiate SMBv1`), mã lỗi `NTSTATUS`, hay lỗi truy cập chia sẻ `IPC$`.
- **CẤM:** Không được tuyên bố *"toàn bộ các dịch vụ và ứng dụng phụ thuộc SMB2/3 đều hoạt động bình thường, không bị gián đoạn"* (`fully compatible`, `zero downtime`) khi chưa có kịch bản kiểm thử tải ứng dụng nghiệp vụ chuyên biệt.
- **CẤM:** Không đưa ra các kết luận xếp hạng hiệu quả giảm thiểu hoặc đánh giá rủi ro (thuộc thẩm quyền Chương 4).

---

## 6. Phân Định Rạch Ròi 4 Tầng Kỹ Thuật Độc Lập (Four-Layer Separation Discipline)

Để ngăn ngừa triệt để tình trạng nhầm lẫn các khái niệm an toàn thông tin, Mục 3.4 phải duy trì sự phân tách độc lập giữa **4 tầng kỹ thuật hoàn toàn khác nhau**:

```
+---------------------------------------------------------------------------------------+
| TẦNG 1: CẤU HÌNH DỊCH VỤ MÁY CHỦ (SMB Server Configuration)                           |
| - Thuộc tính: EnableSMB1Protocol = False | EnableSMB2Protocol = True                  |
| - Bản chất: Cờ cấu hình runtime của dịch vụ chia sẻ tệp LanmanServer.                 |
+---------------------------------------------------------------------------------------+
                                           | ĐỘC LẬP (Không đồng nhất với gỡ tính năng)
                                           v
+---------------------------------------------------------------------------------------+
| TẦNG 2: TÍNH NĂNG THÀNH PHẦN HỆ ĐIỀU HÀNH (Windows Feature Installation)              |
| - Thuộc tính: FS-SMB1 = Installed                                                     |
| - Bản chất: Gói thành phần phần mềm của Windows Server 2012 R2 vẫn tồn tại trên đĩa. |
+---------------------------------------------------------------------------------------+
                                           | ĐỘC LẬP (Không đồng nhất với cập nhật bản vá)
                                           v
+---------------------------------------------------------------------------------------+
| TẦNG 3: TRẠNG THÁI BẢN VÁ MÃ NHỊ PHÂN CỤC BỘ (Local Binary Patch State)               |
| - Thuộc tính: srv.sys = 6.3.9600.16421 < 6.3.9600.18604 -> UNPATCHED                  |
| - Bản chất: Mã nhị phân driver nhân xử lý SMB chưa được cài đặt bản sửa lỗi MS17-010. |
+---------------------------------------------------------------------------------------+
                                           | ĐỘC LẬP (Không đồng nhất với phán quyết quét)
                                           v
+---------------------------------------------------------------------------------------+
| TẦNG 4: PHÁN QUYẾT KỊCH BẢN RÀ QUÉT TỪ XA (Remote NSE Scanner Verdict)                |
| - Thuộc tính: smb-vuln-ms17-010 hoàn tất không có output -> UNKNOWN                   |
| - Bản chất: Kết quả quan sát giới hạn của công cụ quét mạng từ trạm Kali Linux.       |
+---------------------------------------------------------------------------------------+
```

### Các nguyên tắc phân định bắt buộc:
1. **Tầng 1 $\neq$ Tầng 2:** Tắt cờ cấu hình `EnableSMB1Protocol` không làm gỡ bỏ tính năng `FS-SMB1`.
2. **Tầng 1 $\neq$ Tầng 3:** Tắt SMBv1 là biện pháp hạn chế bề mặt tiếp xúc (hardening), không phải là hành động cập nhật bản vá mã nguồn driver (`srv.sys` vẫn là UNPATCHED).
3. **Tầng 3 $\neq$ Tầng 4:** Trạng thái thiếu bản vá nội tại (UNPATCHED) không tự động biến kết quả quét từ xa thành có lỗ hổng (VULNERABLE); và ngược lại, kết quả không xác định từ xa (UNKNOWN) không làm biến đổi máy chủ thành đã vá (PATCHED).
4. **CẤM:** Tuyệt đối không gộp 4 tầng này thành một khái niệm mơ hồ như "trạng thái an toàn của máy chủ" (overall security state).

---

## 7. Chuyển Tiếp Ý Niệm Sang Case C (Transition to Case C)

Phần kết của Mục 3.4 chỉ thực hiện một **chuyển tiếp ý niệm phương pháp luận (conceptual methodological transition)** sang Kịch bản giảm thiểu tiếp theo (Case C):

- **Nội dung chuyển tiếp:**
  * Case B đại diện cho nhóm giải pháp **can thiệp trực tiếp vào cấu hình dịch vụ nội tại của máy chủ mục tiêu** (host-level protocol configuration hardening).
  * Trong thực tế vận hành mạng doanh nghiệp, quản trị viên có thể đối mặt với các tình huống không được phép thay đổi cấu hình máy chủ cục bộ (do yêu cầu duy trì ứng dụng cũ hoặc chính sách kiểm soát máy chủ nghiêm ngặt).
  * Do đó, thực nghiệm tiếp tục khảo sát một lớp phòng thủ ở cấp độ khác biệt: **giải pháp kiểm soát và phân tách luồng dữ liệu trên đường truyền mạng** bằng tường lửa cầu nối trong suốt (Case C — pfSense Transparent Bridge).
- **Ranh giới nghiêm ngặt:**
  * **CẤM:** Tuyệt đối không tiết lộ trước kết quả đo đạc của Case C (như cổng filtered, rule log, v.v.).
  * **CẤM:** Tuyệt đối không so sánh hay đưa ra nhận định giải pháp nào "tốt hơn", "hiệu quả hơn" hay "toàn diện hơn" tại vị trí chuyển tiếp này.
