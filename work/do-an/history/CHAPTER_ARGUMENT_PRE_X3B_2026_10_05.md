# Hợp đồng Chương 2: Thiết kế và triển khai mô hình thực nghiệm (Mô hình Causal-Chain & Phân đoạn mạng Doanh nghiệp)

- Tên chương: **CHƯƠNG 2. THIẾT KẾ VÀ TRIỂN KHAI MÔ HÌNH THỰC NGHIỆM**
- Mục tiêu trung tâm:
  Chuyển dịch toàn bộ mô hình nghiên cứu từ dạng quan sát hộp đen sang **mô hình chuỗi nhân quả (Causal-Chain Research Model)**. Thiết lập kiến trúc mạng phân đoạn doanh nghiệp mô phỏng (Enterprise Topology), mô hình hóa đường tấn công CVE-2017-0144/EternalBlue thành hệ thống tiền điều kiện hình thức $(R, S, D, V, E, C)$, chuẩn hóa máy trạng thái đơn biến 4 nấc snapshot ($S_0 \to S_1 \to S_2 \to S_3$) trên cùng một hệ thống Windows 7 SP1 x64 mục tiêu, và tích hợp trạm Windows client tại VLAN 30 làm đối chứng nghiệp vụ dương tính (Positive Business Control).
- Câu hỏi nghiên cứu chi phối: `RQ3` (*Mô hình lab cô lập cần được thiết kế như thế nào để phục vụ quét, nhận diện và xác minh an toàn trạng thái SMB mà không vi phạm nguyên tắc đạo đức?*).
- Mục tiêu kỹ thuật: `O3` (*Thiết kế kiến trúc lab cô lập và xây dựng bộ tiêu chí xác minh trạng thái an toàn SMB*).
- Luận điểm trung tâm: `C004` (*Kiểm thử an ninh SMB phải tuân thủ nguyên tắc an toàn, đạo đức và vận hành trong mô hình lab cô lập có cơ chế snapshot và quan hệ nhân quả có đối chứng*).
- Ngân sách từ: 3.500 – 4.500 từ.
- Trạng thái: `APPROVED_FOR_EXECUTION` (Đang triển khai biên soạn toàn văn).

---

## 1. MÔ HÌNH HÓA ĐƯỜNG TẤN CÔNG THEO HỆ THỐNG TIỀN ĐIỀU KIỆN (PRECONDITIONS)

Đường tấn công và xác minh lỗ hổng CVE-2017-0144 / EternalBlue không được xem xét như một hiện tượng nhị phân ("thành công / thất bại"), mà được phân rã thành một chuỗi điều kiện logic phụ thuộc tuần tự:

$$\text{Attack Path Success} \iff R \land S \land D \land V \land E \land (C \lor \neg \text{Reverse})$$

Trong đó, các biến tiền điều kiện được định nghĩa chính thức:
1. **$R$ (Network Reachability):** Khả năng tiếp cận dịch vụ qua mạng. Gói tin IP từ trạm kiểm thử có thể định tuyến và xuyên qua các chính sách lọc gói của Firewall/UTM để đến được cổng dịch vụ của máy mục tiêu (TCP 445 / 139).
2. **$S$ (Service Responsiveness):** Trạng thái hoạt động của dịch vụ. Tiến trình `LanmanServer` đang lắng nghe và phản hồi hợp lệ các bản tin bắt tay ba bước TCP (TCP Three-way Handshake) bằng gói tin mang cờ `SYN-ACK`.
3. **$D$ (Dialect Negotiation Compatibility):** Tính tương thích về phương ngữ giao thức. Máy chủ đồng ý thiết lập phiên truyền thông sử dụng phương ngữ SMBv1 (`NT LM 0.12`) trong gói tin phản hồi `SMB_COM_NEGOTIATE`.
4. **$V$ (Vulnerable Implementation State):** Tồn tại khiếm khuyết trong logic xử lý của hệ điều hành. Driver nhân `srv.sys` chưa được cài đặt bản vá an ninh (Unpatched), chứa lỗi tính toán sai lệch kích thước danh sách thuộc tính mở rộng (FEA) trong hàm `SrvOs2FeaListSizeToNt`.
5. **$E$ (Exploit & Memory Execution Success):** Quá trình bố trí bộ nhớ và chuyển hướng thực thi thành công. Thao tác sắp xếp Non-Paged Pool (Pool Grooming) hoàn tất, lỗi tràn bộ đệm ghi đè chính xác cấu trúc điều khiển mà không gây xung đột vùng nhớ nhân hoặc lỗi dừng hệ thống (BSOD).
6. **$C$ (Callback / Reverse Channel Establishment):** Khả năng thiết lập kênh liên lạc ngược. Payload thực thi trong không gian nhân khởi tạo thành công kết nối TCP ngược trở lại máy kiểm thử (khi sử dụng kiến trúc payload Reverse Shell / Reverse Meterpreter).

---

## 2. CHUỖI MÁY TRẠNG THÁI ĐƠN BIẾN (SINGLE-VARIABLE CAUSAL STATE MACHINE)

Loại bỏ hoàn toàn thiết kế kiểm thử song song nhiều máy mục tiêu thay đổi nhiều biến cùng lúc. Mô hình sử dụng **duy nhất một máy mục tiêu Windows 7 SP1 x64** vận hành qua chuỗi trạng thái snapshot đơn biến:

| Trạng thái Snapshot | Tên trạng thái kỹ thuật | Biến thay đổi duy nhất | Giá trị các tiền điều kiện | Mục tiêu nghiên cứu nhân quả |
|---|---|---|:---:|---|
| **$S_0$** | **Vulnerable Baseline** | Trạng thái nguyên bản (chưa can thiệp) | $R=1, S=1, D=1, V=1, E=?, C=?$ | Xác lập bề mặt tấn công ban đầu; kiểm chứng khả năng phát hiện ở cả 4 cấp độ. |
| **$S_1$** | **Patch Only** | Cài đặt gói cập nhật KB4012212; giữ nguyên SMBv1 ON và chính sách mạng | $R=1, S=1, D=1, \mathbf{V=0}, E=0, C=0$ | Chứng minh bản vá bẻ gãy $V$ ($V \to 0$) trong khi $R, S, D$ vẫn tồn tại nguyên vẹn. |
| **$S_2$** | **SMBv1 Disabled** | Giữ patch KB4012212; thực thi vô hiệu hóa SMBv1 (`SMB1 = 0`) | $R=1, S=1, \mathbf{D=0}, V=0, E=0, C=0$ | Chứng minh tắt SMBv1 bẻ gãy $D$ ($D \to 0$) trong khi TCP 445 và SMBv2 vẫn hoạt động. |
| **$S_3$** | **Firewall / Segmentation Hardened** | Giữ state $S_2$; cấu hình Firewall chặn VLAN 20 $\to$ VLAN 10 (TCP 445/139) | $\mathbf{R=0}, S=0, D=0, V=0, E=0, C=0$ | Chứng minh tường lửa bẻ gãy $R$ ($R \to 0$) từ góc độ Pentester bằng kiểm chứng PCAP đa điểm. |

### Vai trò của Trạm đối chứng nghiệp vụ dương tính (Positive Business Control):
Trạm máy trạm Windows tại **VLAN 30 (User)** thực hiện kết nối chia sẻ tệp hợp lệ tới máy chủ tại VLAN 10 qua giao thức SMBv2/v3 ở cả 4 trạng thái $S_0, S_1, S_2, S_3$. Việc duy trì kết nối nghiệp vụ thông suốt tại $S_1, S_2, S_3$ là bằng chứng khoa học khẳng định: **các biện pháp phòng thủ kỹ thuật triệt tiêu rủi ro an ninh nhưng không phá vỡ tính sẵn sàng của nghiệp vụ tổ chức**.

---

## 3. KHUNG TIÊU CHÍ KỸ THUẬT VÀ PHƯƠNG PHÁP LUẬN BẠCH HỘP

Mọi kỹ thuật kiểm thử và khảo sát trong Chương 2 bắt buộc phải được mô tả tường minh theo cấu trúc 10 thành phần chuẩn mực:
1. **Input:** Cú pháp lệnh, tham số cấu hình, cờ giao thức hoặc cấu trúc gói tin phát sinh.
2. **Preconditions:** Các tiền điều kiện bắt buộc phải thỏa mãn để kỹ thuật có thể kích hoạt.
3. **Internal Mechanism:** Cơ chế xử lý nội tại ở mức giao vận, giao thức SMB hoặc không gian nhân Windows.
4. **Observation Point:** Vị trí đặt điểm thu thập dữ liệu (Card mạng trạm Pentest, Firewall interface, Card mạng máy đích, Windows Event Log).
5. **Success Criterion:** Tiêu chí kỹ thuật lượng hóa để công nhận kỹ thuật thành công.
6. **Failure Criterion:** Tiêu chí nhận diện kỹ thuật thất bại (bao gồm việc phân định rõ giữa Fail an toàn và Lỗi sập hệ thống).
7. **Output / Evidence:** Dữ liệu đầu ra, dấu vết mạng và bằng chứng số thu được.
8. **Inference Boundary:** Ranh giới suy luận logic (những kết luận được phép rút ra và những điều tuyệt đối không được suy diễn).
9. **Limitation:** Giới hạn kỹ thuật, độ trễ hoặc khả năng phát sinh âm tính/dương tính giả.
10. **Defense Breakpoint:** Tiền điều kiện cụ thể nào trong chuỗi $(R, S, D, V, E, C)$ bị biện pháp phòng thủ vô hiệu hóa.

---

## 4. QUY ĐỊNH NGHIÊM NGẶT VỀ ĐÁNH GIÁ CẤP ĐỘ 4

- **Quy tắc công nhận PASS Cấp độ 4:** Cấp độ 4 chỉ được công nhận `PASS` khi có bằng chứng khách quan xác nhận mã thử nghiệm đã thực thi thành công trong không gian nhân (Command execution output, tạo phiên tương tác hợp lệ hoặc ghi nhận mã định danh tiến trình).
- **Quy tắc nhận diện sự cố:** Các hiện tượng màn hình xanh (BSOD - Bug Check `PAGE_FAULT_IN_NONPAGED_AREA`, `DRIVER_CORRUPTED_EXPOOL`), máy ảo tự khởi động lại (Reboot), treo cứng (Hang), mất kết nối TCP 445 hoặc hết thời gian chờ (Timeout) **tuyệt đối không được tính là khai thác thành công**, mà phải được phân loại chính xác là `EXPLOIT_FAILED (KERNEL_INSTABILITY / CRASH)`.

---

## 5. THIẾT KẾ MA TRẬN BẰNG CHỨNG (EVIDENCE MATRIX)

Toàn bộ quá trình thực nghiệm tại Chương 3 sẽ được đối chiếu vào Ma trận bằng chứng thiết kế trước tại Chương 2:

| Snapshot State | Windows Build & Hotfix | Cấu hình SMBv1 | Trạng thái Routing / Firewall | Nmap Raw / Reason | NSE Output / NT Status | Metasploit Console Log | Wireshark PCAP Data | Firewall Log Evidence | Trạng thái Cấp 1–4 |
|:---:|---|---|---|---|---|---|---|---|:---:|
| **$S_0$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_1$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_2$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
| **$S_3$** | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` | `[CẦN DỮ LIỆU]` |
