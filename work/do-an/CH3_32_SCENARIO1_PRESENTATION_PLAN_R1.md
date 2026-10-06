# KẾ HOẠCH TRÌNH BÀY DỮ LIỆU MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_PRESENTATION_PLAN_R1)

- **Trạng thái:** `R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B0 R2 — Correct Scenario 1 Evidence/Presentation Plan`
- **Ràng buộc tuyệt đối:** **TUYỆT ĐỐI KHÔNG SOẠN VĂN XUÔI BÁO CÁO (ZERO REPORT PROSE)**. Tài liệu này chỉ thiết kế câu hỏi người đọc, cấu trúc tiểu mục H3, cấu trúc bảng biểu báo cáo sinh viên theo hướng kết quả đo đạc (result-oriented), kế hoạch bố trí hình ảnh kèm khung cắt cúp có thể tái lập, quyết định xử lý B2/B3, ranh giới diễn giải kỹ thuật (B5 fingerprint, B6 negative output) và đoạn chuyển tiếp ý niệm sang Kịch bản 2.

---

## 1. Câu Hỏi Trọng Tâm Dành Cho Người Đọc Luận Văn (Reader Question)

> *Từ góc nhìn của một trạm kiểm thử độc lập trên cùng phân đoạn mạng (Kali Linux), tiến trình khảo sát dịch vụ SMB phát hiện được những máy chủ nào, các cổng và phiên bản dịch vụ nào mở, cùng những phương ngữ, tính năng kỹ thuật và chính sách ký số SMB nào được hệ thống mục tiêu hỗ trợ?*

Mục tiêu cốt lõi là trình bày Kịch bản 1 như một **tiến trình phát hiện và khảo sát thực nghiệm có phương pháp** (measured discovery sequence), đi tuần tự từ mức mạng (phát hiện trạm), mức giao vận (mở cổng) đến mức ứng dụng (phiên bản dịch vụ và giao thức SMB), thay vì lặp lại nhật ký lệnh hay bảng phương pháp đã trình bày tại Chương 2.

---

## 2. Đề Xuất Bố Cục Tiểu Mục H3 (Proposed Subsection Structure)

Để tránh chia cắt vụn vặt văn bản thành 5 tiểu mục riêng cho 5 bước B2–B6, đề xuất giữ nguyên cấu trúc **2 tiểu mục H3 hợp lý theo dòng tư duy kỹ thuật**:

### `3.2. Kết quả Kịch bản 1 — Khảo sát dịch vụ SMB`

- **`3.2.1. Khảo sát trạm mạng và trạng thái mở cổng dịch vụ SMB (B2–B4)`**
  * *Nội dung kỹ thuật:* Trình bày tiến trình rà quét ARP phát hiện các máy chủ trực tuyến trong dải mạng nội bộ (B2), bước xác nhận máy chủ mục tiêu trực tuyến (B3), và phép đo kiểm tra khả năng tiếp cận các cổng dịch vụ SMB TCP 139 và 445 từ xa (B4).
  * *Phương thức thể hiện:* Sử dụng Bảng 3.3 để tổng hợp toàn bộ các kết quả B2, B3, B4 thành một luồng phát hiện liên tục; không sử dụng ảnh chụp màn hình riêng cho B4 nhằm tránh dư thừa dữ liệu.
  * *Ranh giới:* Nêu rõ trạm `192.168.56.100` chưa rõ danh tính (`UNKNOWN identity`); nhấn mạnh trạng thái `OPEN` của cổng 445 chỉ phản ánh khả năng tiếp cận dịch vụ qua mạng, không đồng nghĩa với việc tồn tại lỗ hổng an ninh (`445 OPEN != vulnerable`).

- **`3.2.2. Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB (B5–B6)`**
  * *Nội dung kỹ thuật:* Trình bày kết quả nhận diện dịch vụ và phiên bản hệ điều hành từ xa của Nmap (B5); phân tích chi tiết cấu hình giao thức SMB qua tập kịch bản NSE chuyên dụng gồm các phương ngữ hỗ trợ, tính năng SMB2, chính sách ký số gói tin, và sự vắng mặt đầu ra của script `smb-os-discovery` (B6).
  * *Phương thức thể hiện:* Bảng 3.3 (các hàng B5, B6 tổng kết kết quả); Hình 3.4 (minh chứng dấu vết phiên bản dịch vụ B5); Hình 3.5 (minh chứng cấu trúc cây kết quả NSE B6).
  * *Ranh giới:* Giữ chặt dải nhận diện phiên bản B5 là `Microsoft Windows Server 2008 R2–2012`; không suy diễn nguyên nhân cho việc `smb-os-discovery` không có đầu ra; khẳng định Kịch bản 1 không đưa ra kết luận về lỗ hổng MS17-010.

---

## 3. Thiết Kế Bảng Biểu Báo Cáo Sinh Viên (Student-Facing Tables)

Thiết kế **1 bảng tổng hợp duy nhất (Bảng 3.3)** theo định hướng kết quả (result-oriented), thay thế các đoạn lệnh shell dài dòng bằng nhãn phương pháp súc tích. Bảng này bao quát toàn bộ tiến trình B2–B6 và thay thế hoàn toàn nhu cầu dùng ảnh cho các bước B2, B3, B4.

### Bảng 3.3 — Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux
- **Số hiệu dự kiến:** `Bảng 3.3` (Số tạm theo `CHAPTER_3_NUMBERING_LEDGER.md`, tiếp nối Bảng 3.1 và 3.2 của Mục 3.1).
- **Câu hỏi của người đọc được trả lời:** *Tiến trình khảo sát tuần tự từ trạm Kali Linux ghi nhận được những kết quả định danh mạng, trạng thái cổng, phiên bản dịch vụ và đặc tính giao thức SMB nào trên hệ thống mục tiêu?*
- **Cấu trúc cột chuẩn hóa:** `Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`

| Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn |
|---|---|---|---|
| **B2 — Phát hiện trạm mạng** | Khám phá trạm mạng bằng ARP toàn dải `192.168.56.0/24` | Phát hiện 4 trạm trực tuyến: `192.168.56.1`, `192.168.56.10`, `192.168.56.20`, `192.168.56.100` | Xác định các thực thể đang hoạt động trong phân đoạn mạng. Trạm `.100` duy trì trạng thái chưa xác định danh tính (`UNKNOWN identity`). |
| **B3 — Kiểm tra mục tiêu trực tuyến** | Xác nhận mục tiêu trực tuyến bằng ARP đơn điểm | Máy chủ `192.168.56.20` được ghi nhận ở trạng thái trực tuyến (`up`) | Xác nhận mục tiêu đang trực tuyến trước khi thực hiện các phép quét cổng tiếp theo. |
| **B4 — Khảo sát cổng dịch vụ SMB** | Quét cổng TCP SYN trên cổng 139 và 445 | Cổng `139/tcp` và `445/tcp` đều ở trạng thái `OPEN` (phản hồi gói tin `syn-ack`, TTL 128) | Từ góc nhìn trạm Kali, hai cổng TCP 139/445 có thể tiếp cận và phản hồi `syn-ack`; trạng thái mở cổng **không** đồng nghĩa với việc tồn tại lỗ hổng (`445 OPEN != vulnerable`). |
| **B5 — Nhận diện phiên bản dịch vụ** | Thăm dò dịch vụ và phiên bản hệ điều hành từ xa qua Nmap | Cổng 139: `Microsoft Windows netbios-ssn`<br>Cổng 445: `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`<br>Hệ điều hành suy đoán: `Windows` | Kết quả nhận diện dịch vụ/phiên bản của Nmap chỉ khu biệt trong khoảng `Windows Server 2008 R2–2012`, không định danh chính xác phiên bản Windows Server 2012 R2. |
| **B6 — Phân tích đặc tính giao thức SMB** | Đánh giá giao thức SMB bằng tập kịch bản Nmap NSE | • Phương ngữ hỗ trợ: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`<br>• Ký số: `enabled but not required`<br>• Tính năng SMB2: DFS (trên 2.0.2..3.0.2); Leasing và Multi-credit (trên 2.1..3.0.2)<br>• `smb-os-discovery`: Không có đầu ra khả dụng (`no usable output`) | Nmap smb-protocols ghi nhận máy chủ hỗ trợ phương ngữ SMBv1 cùng các phương ngữ mới hơn, chính sách ký số không bắt buộc. Kịch bản `smb-os-discovery` không trả về dữ liệu. Toàn bộ kết quả chưa đưa ra kết luận về lỗ hổng MS17-010. |

- **Dữ liệu loại khỏi bảng:** Tuyệt đối không đưa đường dẫn tệp máy đọc (`b2_host_discovery.nmap`,...), không đưa mã Evidence ID (`S1-RAW-01`), không đưa mã Claim ID, không lặp lại cú pháp lệnh shell dài dòng (đã có ở Chương 2), và lược bỏ chỉ số độ trễ chi tiết của B3 để tập trung vào trạng thái trực tuyến.
- **Vai trò thay thế ảnh:** Bảng 3.3 thay thế hoàn toàn nhu cầu dùng ảnh chụp màn hình cho các bước B2, B3 và B4.

---

## 4. Kế Hoạch Bố Trí Hình Ảnh (Figure Placement Directives)

Theo kết quả đánh giá tại `CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`, bố trí 2 hình ảnh trong Tiểu mục `3.2.2`:

### 4.1. Hình 3.4 (Tạm thời) — Thăm dò phiên bản dịch vụ SMB từ xa
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.2.2`, ngay sau đoạn phân tích kết quả bước B5.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.4 thể hiện kết quả nhận diện dịch vụ và dấu vết phiên bản hệ điều hành từ xa qua cổng TCP 139 và 445 của máy chủ mục tiêu bằng công cụ Nmap."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Cổng TCP 139 mở với dịch vụ định danh là `netbios-ssn` của Microsoft Windows.
  2. Cổng TCP 445 mở với dịch vụ định danh `microsoft-ds` và chuỗi phiên bản nhận diện là `Microsoft Windows Server 2008 R2 - 2012`.
  3. Dòng thông tin hệ điều hành suy đoán ghi nhận `Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows`.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được diễn giải rằng bức ảnh chứng minh hệ điều hành đích là Windows Server 2012 R2. Chuỗi nhận diện chỉ là một khoảng ước lượng (`2008 R2 - 2012`).
  * **CẤM:** Không được suy diễn từ chuỗi phiên bản dịch vụ này rằng hệ thống có lỗ hổng hoặc chưa được cài bản vá.
- **Khung cắt cúp đề xuất có thể tái lập:**
  * *Tọa độ nguồn:* `x = 0, y = 24, width = 1280, height = 310` (giữ tiêu đề lệnh, kết quả Nmap `-sV` và dấu nhắc lệnh kết thúc tại $y \approx 312$; loại bỏ panel Kali $y < 24$ và khoảng trống $y > 334$).

### 4.2. Hình 3.5 (Tạm thời) — Phân tích đặc tính giao thức SMB bằng kịch bản NSE
- **Vị trí đề xuất:** Đặt trong Tiểu mục `3.2.2`, sau phần phân tích chi tiết bước B6 và Bảng 3.3.
- **Câu văn dẫn nhập đề xuất:**
  *"Hình 3.5 minh chứng cấu trúc kết quả phân tích phương ngữ giao thức, các tính năng kỹ thuật và chính sách ký số SMB trên máy chủ mục tiêu thông qua tập kịch bản Nmap NSE."*
- **Quan sát trực tiếp được phép diễn giải:**
  1. Kịch bản `smb-protocols` ghi nhận 5 phương ngữ được hỗ trợ: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, và `3.0.2`.
  2. Kịch bản `smb2-capabilities` ghi nhận tính năng Distributed File System trên phương ngữ 2.0.2, cùng tổ hợp Distributed File System, Leasing và Multi-credit operations trên các phương ngữ 2.1, 3.0 và 3.0.2.
  3. Kịch bản `smb2-security-mode` xác nhận chính sách ký số gói tin ở trạng thái kích hoạt nhưng không bắt buộc (`Message signing enabled but not required`).
  4. Trong toàn bộ khối kết quả hiển thị, kịch bản `smb-os-discovery` hoàn toàn không xuất hiện phần đầu ra dữ liệu.
- **Ranh giới nghiêm ngặt — Điều hình ảnh TUYỆT ĐỐI KHÔNG chứng minh:**
  * **CẤM:** Không được kết luận máy chủ tồn tại lỗ hổng MS17-010 chỉ vì hệ thống có hỗ trợ phương ngữ SMBv1 (`NT LM 0.12`).
  * **CẤM:** Không được suy diễn nguyên nhân kỹ thuật cho sự vắng mặt của `smb-os-discovery` (như "bị tường lửa chặn", "hệ thống từ chối", "kịch bản bị lỗi").
  * **CẤM:** Không mở rộng ý nghĩa các cờ tính năng SMB2 vượt quá danh sách hiển thị trên màn hình.
- **Khung cắt cúp đề xuất có thể tái lập:**
  * *Tọa độ nguồn:* `x = 0, y = 24, width = 1280, height = 710` (giữ toàn bộ cây kết quả NSE từ $y \approx 65$ đến dấu nhắc kết thúc tại $y \approx 712$; loại bỏ panel Kali $y < 24$ và phần chân terminal trống $y > 734$).

---

## 5. Quyết Định Xử Lý Trùng Lặp B2 và B3 (B2/B3 Redundancy Decision)

- **Bản chất vấn đề:**
  * B2 thực hiện quét ARP dải `192.168.56.0/24`, phát hiện 4 địa chỉ IP trong đó có máy chủ mục tiêu `192.168.56.20` đang hoạt động.
  * B3 thực hiện thăm dò ARP đơn điểm nhắm riêng vào `192.168.56.20` và cũng ghi nhận máy chủ đang hoạt động.
  * Về mặt cung cấp thông tin mới, B3 không đem lại phát hiện mới nào so với B2.
- **Quyết định học thuật:**
  * **Không tách B3 thành một nội dung phân tích độc lập đồ sộ và tuyệt đối không tạo ảnh chụp màn hình riêng cho B3.**
  * Trong văn bản, gộp phần trình bày B2 và B3 vào Tiểu mục `3.2.1`. Trình bày B3 như một **bước kiểm tra xác nhận tính liên tục (continuity confirmation / sanity check)** trong quy trình thực nghiệm: sau khi phát hiện mục tiêu trong dải mạng (B2), người thực nghiệm xác nhận mục tiêu trực tuyến ổn định (B3) trước khi mở rộng thăm dò cổng dịch vụ (B4).
  * Trong Bảng 3.3, B2 và B3 xuất hiện như 2 hàng tuần tự để người đọc nắm bắt đầy đủ các thao tác đã thực hiện trong phòng thí nghiệm; bỏ chỉ số độ trễ miligiây chi tiết trong thiết kế bảng sinh viên để tập trung vào trạng thái trực tuyến.

---

## 6. Định Hướng Diễn Đạt Dấu Vết Phiên Bản B5 (B5 Fingerprint Handling)

- **Ranh giới chuẩn mực:**
  * Nmap ghi nhận chuỗi nhận diện dịch vụ trên cổng 445 là:
    `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`
  * Đây là một **khoảng nhận diện dấu vết (fingerprint range)**, không phải là kết quả định danh duy nhất một phiên bản hệ điều hành.
- **Quy tắc diễn đạt cho văn xuôi:**
  * *Được phép viết:* "Kết quả nhận diện dịch vụ/phiên bản của Nmap ghi nhận dấu vết phiên bản hệ điều hành trên cổng 445 nằm trong khoảng Microsoft Windows Server 2008 R2–2012."
  * *Bị nghiêm cấm:* Tuyệt đối không viết "Nmap xác định máy chủ là Windows Server 2012 R2" hoặc "kết quả quét từ xa chứng minh máy chủ chạy phiên bản 2012 R2". Khẳng định Windows Server 2012 R2 là thông tin từ mốc chuẩn xuất phát cục bộ (Mục 3.1), không phải là kết luận do Nmap tạo ra ở B5. Tránh dùng các thuật ngữ cơ chế không cần thiết như `probe/banner` trừ khi phân tích cơ chế gói tin.

---

## 7. Định Hướng Xử Lý Kết Quả Hạn Chế Của B6 (B6 Negative / Limited Output Handling)

Trong bước B6, kịch bản `smb-os-discovery` được chỉ định thực thi cùng 3 kịch bản khác nhưng không in ra bất kỳ dòng kết quả nào trong khối đầu ra Nmap:

- **Nguyên tắc xử lý học thuật:**
  * Thừa nhận một cách minh bạch và khách quan trong báo cáo rằng kịch bản `smb-os-discovery` không mang lại kết quả khả dụng (`no usable output`).
  * Trình bày sự vắng mặt này như một giới hạn tự nhiên của phép quét thực nghiệm từ xa, giúp người đọc hiểu rõ phạm vi quan sát.
  * Sử dụng lối hành văn khách quan, trực tiếp: *"Nmap smb-protocols ghi nhận các phương ngữ..."*, *"kịch bản smb-os-discovery không trả về khối dữ liệu đầu ra khả dụng"*.
- **Ranh giới nghiêm ngặt:**
  * Tuyệt đối không phỏng đoán hoặc bịa đặt nguyên nhân kỹ thuật (không quy kết do Windows từ chối gói tin, do cấu hình NetBIOS, do tường lửa hay do script lỗi).
  * Tuyệt đối không biến việc thiếu đầu ra thành bằng chứng an ninh (không coi đây là "tính năng bảo mật" hay "dấu hiệu miễn nhiễm").
  * Giữ dung lượng đề cập sự vắng mặt này ở mức vừa phải (1–2 câu nhận xét), không để chi tiết này lấn át các phát hiện tích cực quan trọng (hỗ trợ SMBv1, cấu hình ký số).

---

## 8. Đoạn Chuyển Tiếp Ý Niệm Sang Kịch Bản 2 (Conceptual Transition to Section 3.3)

*Lưu ý: Đây là định hướng ý niệm, không phải văn xuôi báo cáo cuối cùng.*

- **Logic chuyển tiếp học thuật:**
  1. **Tổng kết bề mặt dịch vụ ghi nhận được tại Kịch bản 1:**
     * Trạm Kali Linux đã xác nhận máy chủ mục tiêu `192.168.56.20` đang hoạt động, mở hai cổng dịch vụ SMB TCP 139 và TCP 445, và cho phép tiếp cận trực tiếp từ xa.
     * Hệ thống mục tiêu phản hồi dấu vết phiên bản thuộc dải `Windows Server 2008 R2–2012`, duy trì hỗ trợ phương ngữ cũ SMBv1 (`NT LM 0.12`) song song với các phương ngữ mới hơn, và áp dụng chính sách ký số không bắt buộc.
  2. **Xác lập ranh giới nhận thức kỹ thuật:**
     * Việc cổng dịch vụ SMB mở và hỗ trợ phương ngữ SMBv1 chỉ xác nhận sự tồn tại của bề mặt tiếp xúc dịch vụ chia sẻ tệp kế thừa (legacy surface), nhưng **hoàn toàn chưa đủ cơ sở để kết luận hệ thống có tồn tại lỗ hổng MS17-010 hay không**. Cổng mở không đồng nghĩa với khả năng bị khai thác (`445 OPEN != vulnerable`), và dịch vụ SMBv1 có thể đã được vá lỗi thông qua các bản cập nhật bảo mật thích hợp (`SMBv1 enabled != MS17-010 confirmed`).
  3. **Mở đường sang Kịch bản 2 (Mục 3.3):**
     * Để xác minh chính xác liệu bề mặt dịch vụ SMB đang mở có bị ảnh hưởng bởi lỗ hổng an ninh MS17-010 hay không, tiến trình thực nghiệm cần chuyển sang Kịch bản 2 nhằm áp dụng các kịch bản kiểm tra an ninh chuyên sâu (`smb-vuln-ms17-010`), kết hợp đối chiếu đa chiều giữa tín hiệu quan sát từ xa và bằng chứng cấu hình bản vá cục bộ đã thiết lập tại Mục 3.1.
