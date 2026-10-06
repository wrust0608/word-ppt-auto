# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.5 CASE C R2 (CH3_35_CASEC_PRESENTATION_PLAN_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7E0 R2 — Correct Case C Evidence/Presentation Plan`
- **Ràng buộc cốt lõi:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI BÁO CÁO (ZERO REPORT PROSE)**. Tài liệu này chỉ thiết kế câu hỏi người đọc, cấu trúc tiểu mục H3, thiết kế Bảng 3.6 so sánh theo định hướng kết quả (result-oriented), kế hoạch bố trí hình ảnh kèm ranh giới diễn giải, giải pháp xử lý mâu thuẫn nhãn luật nhật ký tường lửa, xử lý ranh giới trục thời gian và cách thức trình bày hiện trạng máy chủ nội tại độc lập với dữ liệu mạng.

---

## 1. Câu Hỏi Trọng Tâm Dành Cho Người Đọc Luận Văn (Reader Question)

> *Khi đường thử nghiệm giữa trạm kiểm thử Kali Linux và máy chủ mục tiêu Windows Server 2012 R2 được bố trí đi qua cầu nối trong suốt pfSense (Transparent Bridge) và áp dụng chính sách kiểm soát lưu lượng chặn các cổng SMB (TCP 139 và 445), khả năng tiếp cận dịch vụ từ xa thay đổi như thế nào, tường lửa ghi nhận lưu lượng mạng ra sao, phép đo đạc lại kịch bản MS17-010 phản ánh điều gì, và những thuộc tính cục bộ nào (giao thức, tiến trình chia sẻ tệp, trạng thái bản vá) trên máy chủ Windows được ghi nhận duy trì theo mốc point-in-time?*

Câu hỏi này định hình Mục 3.5 thành một **nghiên cứu thực nghiệm đối chứng đa tầng (cross-layer comparative experiment)**:
1. **Làm rõ bản chất can thiệp ở tầng mạng (Network Access Control):** Trong topology Case C, đường thử nghiệm Kali $\to$ Windows được bố trí đi qua `bridge0` của pfSense với chính sách chặn lưu lượng TCP hướng tới các cổng 139 và 445 từ trạm Kali; đây là cơ chế kiểm soát đường truyền mạng, không thay đổi mã nguồn, không gỡ bỏ tính năng, không tắt dịch vụ chia sẻ tệp và không cài đặt bản vá trên máy chủ Windows.
2. **Khảo sát phản hồi mạng từ xa:** Cổng 139 và 445 chuyển từ trạng thái mở (`OPEN`) ở baseline sang trạng thái bị lọc (`FILTERED`) với lý do không nhận được phản hồi (`no-response`).
3. **Đối chiếu liên tầng qua nhật ký tường lửa:** Nhật ký hệ thống pfSense ghi nhận hành động chặn (`Block`) đối với các gói tin TCP SYN tương ứng gửi tới cổng 139 và 445. Đồng thời, kế hoạch xử lý minh bạch mâu thuẫn nhãn luật trong dữ liệu nhật ký mà không đưa ra tuyên bố vượt bằng chứng.
4. **Trình bày trung thực kết quả kiểm tra MS17-010 từ xa:** Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại chuẩn xác là **`UNKNOWN / NO USABLE SCRIPT RESULT`**. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có. Giữ nguyên ranh giới bất định **`UNKNOWN != SAFE`**.
5. **Khóa chặt trạng thái máy chủ nội tại theo mốc point-in-time:** Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Metadata cuối Case C ghi nhận `SMB1=True`, `SMB2=True`, `LanmanServer=Running`, các listener cục bộ 139/445 hiện diện và trạng thái bản vá hệ thống cục bộ duy trì **`UNPATCHED`** (`srv.sys` canonical numeric version = `6.3.9600.16421`). Khóa chặt nguyên lý cốt lõi: **`FILTERED != PATCHED`**.

---

## 2. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

### 2.1. Đánh giá các phương án phân chia tiểu mục
- **Phương án 3 tiểu mục (Thiết lập cầu nối & Chính sách, Kết quả quét mạng & Nhật ký, Trạng thái máy chủ & Đối chiếu ranh giới):** Việc tách riêng một tiểu mục cho trạng thái máy chủ cục bộ sẽ gặp khó khăn vì trong Case C, máy chủ Windows không có thao tác can thiệp trực tiếp nào và không có ảnh chụp console mới; tiểu mục này sẽ bị ngắn và thiếu tính đối xứng.
- **Phương án 1 tiểu mục duy nhất (Toàn bộ 3.5 gom chung):** Khiến phần văn bản trở nên quá dài, dồn ép từ khâu thiết lập chính sách tường lửa đến kết quả đo đạc Nmap, đối chiếu nhật ký và phân tích ranh giới vào một mạch duy nhất, gây khó khăn cho người đọc khi theo dõi tiến trình thực nghiệm.
- **Phương án 2 tiểu mục (Khuyến nghị chính thức):** Nhóm theo hai cụm tư duy kỹ thuật mạch lạc và đối xứng:
  1. *Tiểu mục 3.5.1:* Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB (tập trung vào hạ tầng kiểm soát đường truyền và quy tắc tường lửa).
  2. *Tiểu mục 3.5.2:* Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ (tập trung vào dữ liệu đo đạc thực tế, nhật ký đối chứng và phân định rạch ròi 4 tầng an ninh).
  Bố cục 2 H3 này duy trì tính đồng nhất hoàn hảo với quy mô 2 H3 đã được áp dụng thành công tại Mục 3.1, Mục 3.2, Mục 3.3 và Mục 3.4.

### 2.2. Bố cục đề xuất chính thức

### `3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense`

- **`3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB`**
  * *Nội dung kỹ thuật:*
    - Trình bày mô hình kiểm soát mạng: Trong topology Case C, đường thử nghiệm Kali $\to$ Windows được bố trí đi qua `bridge0` của pfSense (cầu nối Layer 2 Transparent Bridge ghép nối giao diện `CASE_C_KALI` / `em2` và `CASE_C_WINDOWS` / `em3`).
    - Làm rõ nguyên lý đường truyền: Trạm Kali (`192.168.56.10`) và máy chủ Windows (`192.168.56.20`) duy trì cùng dải mạng IP phẳng `/24`, không thay đổi gateway, nhưng đường thử nghiệm giữa hai nút mạng được đưa qua cầu nối pfSense.
    - Trình bày cấu hình tham số lọc cầu nối (FreeBSD sysctl tunables): `net.link.bridge.pfil_member = 1` và `net.link.bridge.pfil_bridge = 0`, chuyển việc kiểm soát gói tin sang các giao diện thành viên của cầu nối.
    - Trình bày chính sách quy tắc tường lửa trên giao diện `CASE_C_KALI`:
      * Quy tắc chặn (Block rule): Hành động `Block`, giao thức `IPv4 TCP`, nguồn `192.168.56.10`, đích `192.168.56.20`, cổng đích thuộc alias `SMB_Ports` (139, 445), trạng thái `keep state`, bật ghi nhật ký (`Log packets that are handled by this rule`).
      * Quy tắc cho phép (Baseline Pass rule): Hành động `Pass`, cho phép các lưu lượng IPv4 khác từ Kali tới Windows.
    - Trình bày thứ tự quy tắc thực tế: Bảng danh sách quy tắc trên giao diện `CASE_C_KALI` ghi nhận quy tắc Block được đặt ở vị trí Dòng 1, phía trên quy tắc Pass ở Dòng 2. Báo cáo ghi nhận thứ tự sắp xếp thực tế trong cấu hình mà không đưa ra phân tích lý thuyết dài dòng.
  * *Phương thức thể hiện:* Sử dụng **Hình 3.9** (minh chứng trực quan danh sách quy tắc và thứ tự Block nằm trên Pass) kết hợp với nửa phần đầu của **Bảng 3.6**; văn xuôi kỹ thuật mô tả chính xác các tham số cấu hình.

- **`3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ`**
  * *Nội dung kỹ thuật:*
    - Trình bày kết quả đo đạc lại trạng thái cổng từ xa (NSE-SMB-01 retest):
      * Trạm Kali Linux thực thi lệnh Nmap SYN scan (`-sS`) nhắm vào cổng 139 và 445 của máy chủ `192.168.56.20` qua đường truyền cầu nối.
      * Máy chủ vẫn phản hồi gói tin ARP (`Host is up, received arp-response`), xác nhận kết nối vật lý Layer 2 thông suốt qua bridge.
      * Cả hai cổng đều được ghi nhận ở trạng thái `filtered`: `139/tcp filtered netbios-ssn no-response` và `445/tcp filtered microsoft-ds no-response`.
    - Trình bày kết quả đối chiếu liên tầng qua nhật ký tường lửa pfSense (System Logs Firewall):
      * Trong lượt Case C, Nmap ghi nhận TCP 139/445 ở trạng thái FILTERED, đồng thời log pfSense ghi nhận lưu lượng TCP SYN tương ứng từ Kali tới các cổng này bị Block trên đường pfSense trên giao diện `CASE_C_KALI`.
      * Xử lý minh bạch mâu thuẫn nhãn luật: Báo cáo chỉ kết luận lưu lượng SMB SYN tương ứng bị chặn trên đường truyền, không khẳng định tên nhãn quy tắc cụ thể nào đã khớp do mâu thuẫn giữa nhãn hiển thị trên ảnh log (`CASE C baseline pass... (100000104)`) và bản ghi manifest (`CASE C - Block SMB... (1000000104)`).
    - Trình bày kết quả đo đạc kịch bản MS17-010 từ xa (NSE-SMB-04 retest):
      * Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại chuẩn xác là **`UNKNOWN / NO USABLE SCRIPT RESULT`**.
      * Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.
      * Giữ vững ranh giới bất định **`UNKNOWN != SAFE`**.
    - Trình bày hiện trạng máy chủ Windows nội tại theo mốc point-in-time:
      * Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Metadata cuối Case C ghi nhận `SMB1=True`, `SMB2=True`, `LanmanServer=Running`, các listener cục bộ 139/445 hiện diện và trạng thái bản vá hệ thống cục bộ duy trì **`UNPATCHED`** (`srv.sys` canonical numeric version = `6.3.9600.16421`).
      * Không suy diễn tính liên tục không gián đoạn (zero downtime) hay tuyên bố toàn vẹn lịch sử nhị phân.
    - Phân tích ranh giới phương pháp luận và đối chiếu 4 tầng:
      * Khóa chặt nguyên lý cốt lõi: **`FILTERED != PATCHED`** (Trạng thái cổng bị lọc từ xa không đồng nghĩa với máy chủ đã được vá lỗ hổng).
      * Khóa chặt nguyên lý bất định: **`UNKNOWN != SAFE`** (Việc không nhận được cảnh báo lỗ hổng từ xa không đồng nghĩa với máy chủ đã an toàn hay hết lỗ hổng).
      * Khẳng định tính độc lập giữa kiểm soát mạng và trạng thái máy chủ: Tường lửa pfSense thiết lập kiểm soát trên đường thử nghiệm giữa hai nút mạng; cấu hình SMBv1 cục bộ vẫn `True` và trạng thái bản vá nội tại vẫn `UNPATCHED`.
      * Loại bỏ suy diễn quá mức: Không tuyên bố việc bypass tường lửa chắc chắn sẽ khai thác thành công.
  * *Phương thức thể hiện:* Sử dụng **Bảng 3.6** (bảng so sánh đối chứng toàn diện), **Hình 3.10** (kết quả quét cổng FILTERED từ Kali), **Hình 3.11** (nhật ký pfSense ghi nhận chặn lưu lượng SYN) và văn xuôi phân tích ranh giới nghiêm ngặt.

---

## 3. Thiết Kế Bảng Biểu Báo Cáo Sinh Viên (Student-Facing Tables)

Thiết kế **1 bảng tổng hợp duy nhất (Bảng 3.6)** theo định hướng kết quả (result-oriented), đối chiếu toàn bộ các trục thông số trước và sau khi áp dụng kiểm soát pfSense.

### Bảng 3.6 — So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense (Case C)

- **Số hiệu chính thức:** `Bảng 3.6` (Tiếp nối Bảng 3.1–3.2 ở Mục 3.1, Bảng 3.3 ở Mục 3.2, Bảng 3.4 ở Mục 3.3, và Bảng 3.5 ở Mục 3.4).
- **Câu hỏi của người đọc được trả lời:** *Khi đặt đường thử nghiệm qua tường lửa cầu nối pfSense và áp dụng chính sách chặn cổng SMB, đường truyền mạng, khả năng phản hồi dịch vụ từ xa, nhật ký tường lửa và hiện trạng máy chủ nội tại biến đổi ra sao so với mốc xuất phát ban đầu?*
- **Cấu trúc cột chuẩn hóa:** `Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case C) | Diễn giải trực tiếp & Giới hạn kết luận`

| Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case C) | Diễn giải trực tiếp & Giới hạn kết luận |
|---|---|---|---|
| **Vị trí kiểm soát mạng**<br>(Kiến trúc đường truyền) | Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali $\to$ Windows | Đường thử nghiệm đi qua pfSense Transparent Bridge (`bridge0`, kết nối `em2` và `em3`) | **Đường thử nghiệm được đưa qua tường lửa cầu nối**<br>Đường thử nghiệm Kali $\to$ Windows được bố trí đi qua cầu nối Layer 2 của pfSense. Tham số nhân `pfil_member=1` chuyển quyền lọc gói sang giao diện thành viên. |
| **Chính sách lọc gói tin pfSense**<br>(Giao diện `CASE_C_KALI`) | Chưa áp dụng ruleset pfSense Case C trên đường thử nghiệm | Áp dụng quy tắc `BLOCK`<br>Cổng `SMB_Ports` (139, 445), cờ ghi log | **Chính sách chặn SMB được thiết lập**<br>Tường lửa cấu hình quy tắc chặn lưu lượng TCP từ `192.168.56.10` tới `192.168.56.20` trên các cổng 139 và 445, đồng thời kích hoạt tính năng ghi nhật ký. |
| **Thứ tự thực thi quy tắc**<br>(Rule Evaluation Order) | Không áp dụng đối với pfSense Case C | Quy tắc `BLOCK` đặt trên quy tắc `PASS`<br>(Đánh giá ưu tiên Dòng 1) | **Quy tắc chặn nằm trên quy tắc cho phép**<br>Bảng quy tắc hiển thị quy tắc Block ở Dòng 1, phía trên quy tắc Pass ở Dòng 2; lưu lượng SMB được đối chiếu với quy tắc chặn trước. |
| **Trạng thái cổng TCP 139 từ xa**<br>(Quét từ trạm Kali Linux) | `OPEN`<br>(Phản hồi `syn-ack`, Mục 3.2) | `FILTERED`<br>(Lý do: `no-response`) | **Cổng 139 không còn phản hồi gói tin**<br>Trạm Kali ghi nhận trạng thái `filtered` do gói tin thăm dò không nhận được phản hồi (`no-response`). Trạng thái này không đồng nghĩa với việc dịch vụ NetBIOS cục bộ đã tắt. |
| **Trạng thái cổng TCP 445 từ xa**<br>(Quét từ trạm Kali Linux) | `OPEN`<br>(Phản hồi `syn-ack`, Mục 3.2) | `FILTERED`<br>(Lý do: `no-response`) | **Cổng 445 chuyển sang trạng thái bị lọc**<br>Trạm Kali ghi nhận trạng thái `filtered` do không nhận được phản hồi (`no-response`). Trạng thái cổng bị lọc trên mạng không đồng nghĩa với việc máy chủ đã được vá (`FILTERED != PATCHED`). |
| **Ghi nhận nhật ký tường lửa pfSense**<br>(System Logs Firewall) | Không có log pfSense tương ứng vì pfSense chưa nằm trên đường baseline | Ghi nhận hành động `Block`<br>Gói tin TCP cờ SYN tới cổng 139, 445 | **Lưu lượng SMB SYN bị chặn trên đường truyền pfSense**<br>Nhật ký pfSense ghi nhận các gói tin TCP SYN từ trạm Kali tới cổng 139/445 của máy chủ bị chặn. Do sai lệch nhãn trong ảnh log, báo cáo không khẳng định tên nhãn quy tắc cụ thể đã khớp. |
| **Phán quyết kiểm tra MS17-010**<br>(Kịch bản `smb-vuln-ms17-010`) | `UNKNOWN`<br>(Theo Mục 3.3) | `UNKNOWN`<br>(Không có kết quả kịch bản) | **Phán quyết từ xa duy trì không xác định**<br>Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có. `UNKNOWN != SAFE`. |
| **Cấu hình máy chủ SMBv1**<br>(`EnableSMB1Protocol`) | `True`<br>(Đang kích hoạt, Mục 3.1) | `True`<br>(Metadata ghi nhận duy trì kích hoạt) | **Cấu hình giao thức cục bộ không thay đổi**<br>Thuộc tính cấu hình máy chủ SMBv1 duy trì `True`. Biện pháp kiểm soát mạng Case C hoàn toàn không tác động hay vô hiệu hóa giao thức SMBv1 trên hệ điều hành mục tiêu. |
| **Dịch vụ chia sẻ tệp cục bộ**<br>(`LanmanServer`) | `Running`<br>(Đang hoạt động, Mục 3.1) | `Running`<br>(Listener cục bộ 139/445 hiện diện) | **Dịch vụ chia sẻ tệp duy trì hoạt động cục bộ**<br>Metadata ghi nhận LanmanServer tiếp tục ở trạng thái Running và các listener 139/445 hiện diện trên máy chủ. Tường lửa chỉ kiểm soát đường truyền mạng bên ngoài, không can thiệp tiến trình nội bộ máy chủ. |
| **Trạng thái bản vá hệ thống**<br>(Mã nhị phân driver `srv.sys`) | `UNPATCHED`<br>(`6.3.9600.16421`, Mục 3.1) | `UNPATCHED`<br>(Không cài đặt bản vá) | **Máy chủ tiếp tục ở trạng thái chưa vá**<br>Phiên bản số chuẩn của `srv.sys` dùng để đối chiếu bản vá là `6.3.9600.16421`; Case C không ghi nhận thao tác cài bản vá. Khóa chặt nguyên lý phương pháp luận: `FILTERED != PATCHED`. |

### Quy tắc nghiêm ngặt đối với Bảng 3.6:
- **ĐƯỢC PHÉP:** Sử dụng các danh từ kỹ thuật chuẩn hóa (`Transparent Bridge`, `BLOCK`, `PASS`, `FILTERED`, `no-response`, `TCP SYN`, `UNKNOWN`, `EnableSMB1Protocol`, `LanmanServer`, `srv.sys`, `UNPATCHED`).
- **CẤM:** Không đưa cú pháp dòng lệnh thô hoặc chuỗi đối số argv của Nmap (`--privileged`, `-T3`, `--max-retries 2`, `-oA ...`).
- **CẤM:** Không đưa mã định danh quản trị nội bộ hoặc đường dẫn tệp trong kho lưu trữ.
- **CẤM:** Không đưa các phán quyết ngoài phạm vi bằng chứng như `PATCHED`, `SAFE`, `NOT VULNERABLE`, `IMMUNE`, `ELIMINATED EXPLOITABILITY`.

---

## 4. Kế Hoạch Bố Trí Hình Ảnh (Figure Placement Directives)

Theo kết quả thẩm tra tại `CH3_35_CASEC_FIGURE_SELECTION_R1.md`, bố trí **3 hình ảnh chính thức (Hình 3.9, Hình 3.10, Hình 3.11)** theo Phương án A khuyến nghị:

### 4.1. Hình 3.9 — Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự ưu tiên trên giao diện CASE_C_KALI của tường lửa pfSense
- **Vị trí đề xuất:** Tiểu mục `3.5.1`, ngay sau đoạn mô tả cấu hình quy tắc trên giao diện `CASE_C_KALI`.
- **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_08_Rule_Order.png`.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.9 thể hiện giao diện quản lý quy tắc tường lửa trên giao diện CASE_C_KALI của pfSense, ghi nhận cấu hình quy tắc chặn lưu lượng SMB và thứ tự ưu tiên thực thi trên bộ lọc gói tin."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Thẻ ngữ cảnh giao diện mạng đang chọn là `CASE_C_KALI`.
  2. Tiêu đề bảng danh sách quy tắc: `Rules (Drag to Change Order)`.
  3. Bảng danh sách quy tắc gồm hai dòng:
     - Dòng 1: Hành động chặn (biểu tượng X đỏ), có kích hoạt ghi log, giao thức `IPv4 TCP`, nguồn `192.168.56.10`, đích `192.168.56.20`, cổng đích `SMB_Ports`.
     - Dòng 2: Hành động cho phép (dấu kiểm xanh), giao thức `IPv4 *`, nguồn `192.168.56.10`, đích `192.168.56.20`, cổng đích bất kỳ (`*`).
  4. Quy tắc Block được đặt ở vị trí phía trên (Dòng 1), quy tắc Pass baseline được đặt ở vị trí phía dưới (Dòng 2).
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh lưu lượng mạng thực tế đã bị chặn (hành vi chặn thực tế chỉ được chứng minh qua kết quả đo đạc Nmap và nhật ký sau đó).
  * **CẤM:** Không được diễn giải hình ảnh này chứng minh máy chủ Windows đã an toàn hay dịch vụ SMB trên máy chủ đã dừng.
  * **CẤM:** Không đưa ra các câu khẳng định lý thuyết tuyệt đối hóa kiểu "bảo đảm nếu đặt dưới thì hoàn toàn vô hiệu".

### 4.2. Hình 3.10 — Kết quả đo đạc trạng thái cổng dịch vụ SMB từ trạm Kali Linux qua đường truyền tường lửa pfSense
- **Vị trí đề xuất:** Tiểu mục `3.5.2`, ngay sau đoạn phân tích kết quả quét cổng của trạm Kali.
- **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png`.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.10 thể hiện kết quả quét cổng dịch vụ SMB từ trạm kiểm thử Kali Linux nhắm vào máy chủ mục tiêu khi đường truyền dữ liệu đi qua tường lửa pfSense."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Lệnh Nmap thực thi: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`.
  2. Máy chủ mục tiêu phản hồi gói tin ARP (`Host is up, received arp-response`).
  3. Cổng `139/tcp` hiển thị trạng thái `filtered`, dịch vụ `netbios-ssn`, lý do chẩn đoán `no-response`.
  4. Cổng `445/tcp` hiển thị trạng thái `filtered`, dịch vụ `microsoft-ds`, lý do chẩn đoán `no-response`.
  5. Địa chỉ MAC của máy chủ phản hồi qua ARP là `08:00:27:55:71:CE`.
  6. Phiên quét hoàn tất trong 1.33 giây.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Tuyệt đối không được viết rằng cổng bị đóng (`closed`) hay dịch vụ trên máy chủ đã tắt. Nmap ghi nhận rõ ràng lý do là `no-response` (không nhận được phản hồi).
  * **CẤM:** Không được đánh đồng trạng thái `filtered` với việc máy chủ đã được vá (`FILTERED != PATCHED`).

### 4.3. Hình 3.11 — Nhật ký tường lửa pfSense ghi nhận hành vi chặn các gói tin TCP SYN hướng tới cổng dịch vụ SMB (Provisional Crop)
- **Vị trí đề xuất:** Tiểu mục `3.5.2`, ngay sau đoạn đối chiếu liên tầng giữa kết quả quét Nmap và hành vi can thiệp của pfSense.
- **Tệp nguồn:** `work/do-an/chapter3/evidence/case_c/pfSense_10_Block_Log_CANONICAL.png`.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.11 trích xuất nhật ký tường lửa pfSense (System Logs Firewall) ghi nhận các gói tin TCP SYN từ trạm kiểm thử hướng tới các cổng dịch vụ SMB của máy chủ bị chặn lại trên giao diện CASE_C_KALI."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Cột `Action` hiển thị biểu tượng X đỏ, xác nhận hành động chặn gói tin (`Block`).
  2. Giao diện ghi nhận là `CASE_C_KALI`.
  3. Địa chỉ nguồn là `192.168.56.10` (trạm Kali) với các cổng nguồn động (39801, 39803, 39804).
  4. Địa chỉ đích là `192.168.56.20` (máy chủ Windows) với các cổng đích là `139` và `445`.
  5. Giao thức và cờ TCP là `TCP:S` (gói tin bắt tay khởi tạo kết nối TCP SYN).
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM TUYỆT ĐỐI:** Không được viết rằng ảnh chụp nhật ký chứng minh chính xác quy tắc `CASE C - Block SMB Kali to Windows` đã khớp. Biểu tượng trên ảnh hiển thị chuỗi nhãn `CASE C baseline pass Kali to Windows (100000104)`.
  * **CÔNG THỨC KẾT LUẬN DUY NHẤT:** Chỉ kết luận: *"Lưu lượng TCP SYN tương ứng từ trạm Kali tới các cổng 139 và 445 của máy chủ Windows được ghi nhận bị chặn (Block) trên đường truyền đi qua pfSense."*
  * **CẤM:** Không được ghép giờ hiển thị trên pfSense (`14:20:18`) và giờ trên Kali (`03:20:18`) thành một trục thời gian tuyệt đối duy nhất.
  * **TÌNH TRẠNG CẮT CÚP:** Đề xuất cắt cúp hiện tại là PROVISIONAL; bắt buộc kiểm tra trực tiếp vùng hiển thị trước khi chốt tọa độ tại X7E1.

---

## 5. Xử Lý Chuyên Sâu Sai Lệch Nhãn Luật Nhật Ký Tường Lửa (Rule-Label Conflict Resolution)

### 5.1. Bản chất của mâu thuẫn
- Ảnh gốc `pfSense_10_Block_Log_CANONICAL.png` hiển thị:
  * Biểu tượng hành động: X đỏ (`Block`).
  * Giao diện: `CASE_C_KALI`.
  * Nhãn mô tả khi di chuột / hiển thị quy tắc: `CASE C baseline pass Kali to Windows (100000104)`.
- Tài liệu điều hành và báo cáo tiến trình (`pfSense_Remediation_Run_Manifest.txt` dòng 79 và `RUN4_PAUSE_STATE_REPORT.txt` Mục 21) ghi chép:
  * Hành động: `Block (Logged)`.
  * Quy tắc chịu trách nhiệm: `CASE C - Block SMB Kali to Windows (1000000104)`.
- Đây là một sai lệch thực tế giữa văn bản giao diện hiển thị trong ảnh chụp WebGUI pfSense và bản ghi manifest của người thực nghiệm.

### 5.2. Nguyên tắc học thuật và giải pháp xử lý trong báo cáo
1. **Không che giấu, không tự ý chỉnh sửa ảnh:** Giữ nguyên vẹn tính chân thực của dữ liệu lịch sử.
2. **Phân định rạch ròi hai tầng chứng minh:**
   - *Tầng 1 (Sự tồn tại và thứ tự của quy tắc):* Ảnh `pfSense_08_Rule_Order.png` chứng minh quy tắc chặn TCP cổng SMB với tính năng ghi log tồn tại và được đặt ở Dòng 1, phía trên quy tắc Pass.
   - *Tầng 2 (Hành vi can thiệp thực tế của tường lửa):* Ảnh `pfSense_10_Block_Log_CANONICAL.png` chứng minh các gói tin TCP SYN từ `192.168.56.10` tới `192.168.56.20:139` và `:445` đã bị tường lửa pfSense chặn lại (hành động `Block`).
3. **Giới hạn câu chữ (Bounded wording):**
   - Báo cáo sinh viên **tuyệt đối không khẳng định tên nhãn quy tắc cụ thể nào đã khớp trong nhật ký**.
   - Diễn đạt trung thực: *"Nhật ký tường lửa pfSense ghi nhận lưu lượng TCP SYN thăm dò cổng SMB từ trạm Kali tới máy chủ Windows bị chặn lại trên giao diện CASE_C_KALI. Do có sự sai lệch giữa chuỗi nhãn hiển thị trong giao diện nhật ký và bản ghi điều hành, báo cáo ghi nhận khách quan hành vi chặn lưu lượng mạng thực tế của tường lửa mà không đưa ra khẳng định tuyệt đối về định danh quy tắc nội bộ."*

---

## 6. Xử Lý Ranh Giới Trục Thời Gian (Timebase & Clock-Domain Boundary)

### 6.1. Hiện trạng dữ liệu thời gian
- Trên trạm Kali Linux: Đầu ra lệnh Nmap hiển thị thời gian bắt đầu quét là `Sun Oct 4 03:20:18 2026 -0400`.
- Trên giao diện WebGUI pfSense: Các dòng nhật ký chặn gói tin hiển thị thời gian `Oct 4 14:20:18` và `14:20:19`.
- Khoảng cách hiển thị chênh lệch xấp xỉ 11 giờ.

### 6.2. Ranh giới bắt buộc
1. **Không đồng bộ wall-clock:** Môi trường thực nghiệm gồm các máy ảo độc lập không được cấu hình một máy chủ NTP chung để chuẩn hóa múi giờ và đồng hồ tuyệt đối.
2. **CẤM:** Không được viết các câu khẳng định giả định như *"Lúc 03:20:18 trên Kali tương đương chính xác 14:20:18 trên pfSense"* hoặc xây dựng một dòng thời gian thống nhất giả tạo.
3. **Quy tắc văn phong:** Trong văn xuôi báo cáo Mục 3.5, **ưu tiên không đưa chuỗi thời gian chi tiết (timestamp) vào câu chữ** nếu không thật sự cần thiết. Mối quan hệ tương ứng giữa lệnh quét và nhật ký được thiết lập thông qua bộ bốn thông số mạng (Địa chỉ IP nguồn `.56.10`, IP đích `.56.20`, cổng đích `139/445`, cờ giao thức `TCP SYN`), tiến trình chạy thực nghiệm có kiểm soát và sự trùng khớp về giây (`:18`, `:19`).

---

## 7. Phân Định Trạng Thái Máy Chủ Nội Tại Và Nguồn Gốc Chứng Cứ

### 7.1. Phân biệt dữ liệu mạng và dữ liệu máy chủ
- Tường lửa pfSense là thiết bị mạng trung gian (Network Layer). Mọi hình ảnh chụp từ pfSense (`pfSense_03` đến `pfSense_10`) chỉ phản ánh cấu hình của tường lửa và lưu lượng đi qua tường lửa.
- Trạng thái nội tại của máy chủ Windows Server 2012 R2 gồm:
  * Thuộc tính cấu hình `EnableSMB1Protocol : True`, `EnableSMB2Protocol : True`.
  * Tính năng hệ điều hành `FS-SMB1 : Installed`.
  * Dịch vụ chia sẻ tệp `LanmanServer : Running`, tiếp tục mở và các listener cục bộ 139/445 hiện diện trên máy chủ.
  * Trạng thái bản vá hệ thống duy trì **`UNPATCHED`** (`srv.sys` canonical numeric version = `6.3.9600.16421`, phân biệt với chuỗi hiển thị `6.3.9600.16384`).
- Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows.

### 7.2. Quy tắc dẫn nguồn chứng cứ (Provenance Rule)
- Báo cáo phải nêu rõ: Trạng thái máy chủ Windows trong Case C được kế thừa từ mốc xuất phát ban đầu (Mục 3.1) và được xác nhận bởi siêu dữ liệu kiểm toán hệ thống (`RUN4_PAUSE_STATE_REPORT.txt`).
- **TUYỆT ĐỐI KHÔNG ám chỉ rằng các ảnh chụp màn hình pfSense trực tiếp chứng minh trạng thái máy chủ cục bộ.**

---

## 8. Khóa Chặt 4 Tầng Kỹ Thuật Và Ranh Giới Phương Pháp Luận

Để bảo đảm báo cáo đạt chuẩn mực cao nhất và không bị bắt lỗi tại hội đồng bảo vệ, Mục 3.5 thiết lập hệ thống ranh giới "bất khả xâm phạm":

1. **`FILTERED != PATCHED`:**
   - Cổng 139 và 445 hiển thị `filtered` từ xa qua mạng chỉ chứng minh lưu lượng mạng bị tường lửa chặn lại trên đường truyền.
   - Trạng thái này hoàn toàn không đồng nghĩa với việc mã nhị phân driver `srv.sys` của Windows đã được vá hay lỗ hổng MS17-010 đã được khắc phục.
2. **`UNKNOWN != SAFE`:**
   - Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả phân loại `UNKNOWN / NO USABLE SCRIPT RESULT`.
   - Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có.
   - Kết quả chưa xác định tuyệt đối không được đánh đồng với an toàn (`SAFE`) hay không có lỗ hổng (`NOT VULNERABLE`).
3. **`445 FILTERED != SMBv1 disabled`:**
   - Cổng bị lọc từ xa không đồng nghĩa với việc giao thức SMBv1 trên máy chủ đã bị vô hiệu hóa hay tính năng `FS-SMB1` đã bị gỡ bỏ. Cấu hình SMBv1 cục bộ vẫn `True`.
4. **Không suy diễn về kết quả bypass:**
   - Không đưa ra các tuyên bố vượt quá bằng chứng như *"Nếu vượt qua được tường lửa thì chắc chắn sẽ tấn công RCE thành công"*. Đề tài chỉ ghi nhận thực nghiệm trong phạm vi các kịch bản đo đạc đã thực hiện.
5. **Không đưa kết luận hiệu quả hay xếp hạng rủi ro của Chương 4 vào Chương 3:**
   - Mục 3.5 chỉ trình bày sự thật thực nghiệm (Empirical Facts). Toàn bộ việc so sánh tổng hợp sẽ thuộc về Mục 3.6, và việc đánh giá hiệu quả, khuyến nghị kiến trúc phòng thủ thuộc về Chương 4.
