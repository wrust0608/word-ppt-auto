## 3.5. Kết quả Case C — Kiểm soát SMB bằng pfSense

Sau khi xác lập đường cơ sở và đánh giá can thiệp vô hiệu hóa SMBv1 ở mức máy chủ (Case B), nghiên cứu triển khai kịch bản can thiệp Case C nhắm vào lớp kiểm soát mạng. Trong topology Case C, đường thử nghiệm Kali → Windows được bố trí đi qua tường lửa pfSense hoạt động ở chế độ Transparent Bridge Layer 2 nhằm áp dụng chính sách lọc gói tin đối với các cổng SMB. Trọng tâm của Case C là đo đạc diện mạo dịch vụ từ xa, đối chiếu nhật ký tường lửa với kết quả quét mạng, và kiểm tra tính độc lập của trạng thái máy chủ cục bộ.

### 3.5.1. Thiết lập cầu nối pfSense và chính sách kiểm soát lưu lượng SMB

Để kiểm soát lưu lượng mà không thay đổi cấu trúc địa chỉ IP môi trường thử nghiệm, pfSense được cấu hình làm Transparent Bridge. Cầu nối `bridge0` gồm hai giao diện thành viên: `CASE_C_KALI` (gắn card mạng ảo `em2`) kết nối trạm Kali (`192.168.56.10/24`), và `CASE_C_WINDOWS` (gắn card mạng ảo `em3`) kết nối máy chủ Windows (`192.168.56.20/24`). Hai máy ảo duy trì cùng dải mạng phẳng `192.168.56.0/24` qua cầu nối Layer 2; phân đoạn quản trị tường lửa được tách riêng và không nằm trên đường thử nghiệm SMB.

Để các gói tin qua cầu nối chịu sự kiểm soát của bộ lọc pf, cấu hình nhân FreeBSD trên pfSense được thiết lập với hai tham số: `net.link.bridge.pfil_member = 1` và `net.link.bridge.pfil_bridge = 0`. Thiết lập này kích hoạt tính năng lọc gói tin tại giao diện thành viên tiếp nhận lưu lượng `CASE_C_KALI`.

Trên giao diện `CASE_C_KALI`, đề tài thiết lập hai quy tắc lọc có thứ tự ưu tiên xác định: quy tắc chặn (Block) lưu lượng IPv4 TCP từ trạm `192.168.56.10` tới máy chủ `192.168.56.20` trên các cổng SMB (`SMB_Ports`, gồm cổng 139 và 445), có bật cờ ghi nhật ký; và quy tắc cho phép đường cơ sở (Pass) đối với lưu lượng IPv4 `*` nhằm lưu thông các gói tin kiểm tra khác. Hình 3.9 ghi nhận danh mục quy tắc lọc và thứ tự sắp xếp trên giao diện `CASE_C_KALI` của pfSense.

![Hình 3.9](chapter3/presentation/3_5/Hinh_3_9_pfSense_Rule_Order.png)
*Hình 3.9. Cấu hình quy tắc kiểm soát lưu lượng SMB và thứ tự sắp xếp trên giao diện CASE_C_KALI của pfSense*

Hình 3.9 cho thấy quy tắc Block lưu lượng IPv4 TCP tới cổng `SMB_Ports` (Dòng 1) được đặt phía trên quy tắc Pass baseline (Dòng 2) trên giao diện `CASE_C_KALI`, đi kèm cờ ghi nhật ký được kích hoạt. Hình này xác nhận cấu hình và thứ tự hiển thị của ruleset; kết quả xử lý lưu lượng được đối chiếu bằng phép đo Nmap và nhật ký pfSense ở Mục 3.5.2.

Bảng 3.6 tổng hợp so sánh các tham số kiến trúc, chính sách quy tắc và trạng thái hệ thống giữa đường cơ sở và kịch bản Case C.

**Bảng 3.6. So sánh cấu hình, lưu lượng mạng và trạng thái hệ thống trước và sau khi áp dụng kiểm soát pfSense (Case C)**

| Tầng kiểm tra / Tham số đo đạc | Trước can thiệp (Baseline) | Sau can thiệp (Case C) | Diễn giải trực tiếp & Giới hạn kết luận |
|---|---|---|---|
| **Vị trí kiểm soát mạng / kiến trúc đường truyền** | Host-Only baseline; chưa có pfSense trên đường thử nghiệm Kali → Windows | Transparent Bridge (cầu nối `bridge0` trên đường thử nghiệm Kali → Windows) | Đường thử nghiệm Case C được bố trí qua pfSense Transparent Bridge trên dải mạng `192.168.56.0/24`. |
| **Chính sách lọc pfSense** | Chưa áp dụng ruleset pfSense Case C trên đường thử nghiệm | Block `IPv4 TCP` từ Kali (`192.168.56.10`) tới Windows (`192.168.56.20`) trên cổng 139, 445; bật ghi nhật ký | Ruleset chặn TCP 139/445 từ Kali tới Windows, có bật cờ ghi nhật ký. |
| **Thứ tự quy tắc trên giao diện kiểm thử** | Không áp dụng đối với pfSense Case C | Quy tắc Block SMB_Ports (Dòng 1) xếp trên quy tắc Pass baseline (Dòng 2) | Quy tắc Block SMB_Ports được đặt phía trên quy tắc Pass baseline. |
| **Trạng thái cổng TCP 139 từ xa**<br>(Từ trạm Kali Linux) | `OPEN (Phản hồi syn-ack)`<br>(Theo Mục 3.2) | `FILTERED`<br>(Lý do `no-response`) | FILTERED/no-response từ Kali; không suy ra cổng local đã đóng. |
| **Trạng thái cổng TCP 445 từ xa**<br>(Từ trạm Kali Linux) | `OPEN (Phản hồi syn-ack)`<br>(Theo Mục 3.2 / Mục 3.3) | `FILTERED`<br>(Lý do `no-response`) | FILTERED/no-response từ Kali; FILTERED != PATCHED. |
| **Nhật ký tường lửa pfSense**<br>(Giao diện `CASE_C_KALI`) | Không có log pfSense tương ứng vì pfSense chưa nằm trên đường baseline | Ghi nhận hành động Block đối với các gói tin TCP SYN từ Kali tới cổng 139 và 445 của Windows | Lưu lượng SMB SYN tương ứng được ghi nhận Block; không quy thuộc tuyệt đối theo tên rule. |
| **Phán quyết kiểm tra MS17-010 từ xa**<br>(Kịch bản `smb-vuln-ms17-010`) | `UNKNOWN`<br>(Theo Mục 3.3) | `UNKNOWN`<br>(Không có kết quả script) | Không có phán quyết usable; UNKNOWN != SAFE. |
| **Cấu hình giao thức SMBv1 cục bộ**<br>(`EnableSMB1Protocol`) | `True`<br>(Đang kích hoạt, theo Mục 3.1) | `True`<br>(Tiếp tục duy trì kích hoạt) | Metadata cuối Case C ghi nhận True; không có thao tác đổi cấu hình SMB. |
| **Dịch vụ chia sẻ tệp và listener cục bộ** | `LanmanServer : Running; lắng nghe cổng 139/445`<br>(Theo Mục 3.1) | `LanmanServer : Running; listener 139/445 hiện diện` | LanmanServer=Running, listener 139/445 hiện diện tại thời điểm kiểm tra. |
| **Trạng thái bản vá hệ thống cục bộ**<br>(Mã nhị phân driver `srv.sys`) | `UNPATCHED`<br>(Theo Mục 3.1) | `UNPATCHED`<br>(Case C không ghi nhận thao tác cài bản vá) | Vẫn phân loại UNPATCHED; không ghi nhận thao tác cài bản vá. |

Dữ liệu Bảng 3.6 phản ánh sự phân tách giữa hai tầng: chính sách lọc áp dụng trên đường truyền mạng, trong khi cấu hình dịch vụ máy chủ không ghi nhận thao tác can thiệp. Để đánh giá diện mạo dịch vụ thực tế, nghiên cứu tiến hành đo đạc lại từ trạm kiểm thử Kali Linux.

### 3.5.2. Kết quả đo đạc từ xa, đối chiếu nhật ký tường lửa và trạng thái máy chủ

Từ trạm Kali Linux, nghiên cứu thực hiện phép đo đạc lại trạng thái hai cổng SMB 139 và 445 qua lệnh Nmap với kỹ thuật quét SYN (`-sS`) và cờ ghi nhận nguyên nhân (`--reason`). Kết quả Nmap ghi nhận mục tiêu ở trạng thái up với arp-response trong topology Case C. Tuy nhiên, diện mạo dịch vụ từ xa đã thay đổi rõ rệt so với đường cơ sở. Hình 3.10 thể hiện kết quả quét cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense.

![Hình 3.10](chapter3/presentation/3_5/Hinh_3_10_Nmap_Filtered.png)
*Hình 3.10. Kết quả đo đạc trạng thái cổng SMB từ trạm Kali Linux qua đường thử nghiệm pfSense*

Trên Hình 3.10, cả hai cổng TCP 139 và TCP 445 đều được ghi nhận ở trạng thái `filtered` với lý do không nhận được phản hồi (`no-response`), trái ngược với trạng thái `open` kèm phản hồi `syn-ack` ở đường cơ sở. Trạng thái `filtered` chỉ phản ánh việc công cụ quét không nhận được gói tin phản hồi trên mạng; kết quả này không đồng nghĩa với việc các cổng dịch vụ trên máy chủ đã bị đóng (`closed`) hay dịch vụ chia sẻ tệp cục bộ bị tắt. Quan trọng hơn, trạng thái cổng bị lọc từ xa hoàn toàn không đồng nghĩa với việc hệ điều hành máy chủ đã được vá lỗ hổng (`FILTERED != PATCHED`).

Để kiểm tra diễn biến xử lý gói tin trên đường truyền, đề tài đối chiếu dữ liệu quét mạng với nhật ký tường lửa pfSense tại giao diện `CASE_C_KALI`. Hình 3.11 ghi nhận các dòng nhật ký tường lửa tương ứng với đợt đo đạc từ trạm Kali Linux. Trong các dòng log được trích, các trường lần lượt thể hiện hành động xử lý, thời điểm, giao diện, nhãn quy tắc, địa chỉ nguồn, địa chỉ đích và giao thức.

![Hình 3.11](chapter3/presentation/3_5/Hinh_3_11_pfSense_Block_Log.png)
*Hình 3.11. Nhật ký pfSense ghi nhận lưu lượng TCP SYN tới các cổng SMB bị chặn trên đường thử nghiệm*

Dữ liệu hiển thị tại Hình 3.11 ghi nhận 4 sự kiện chặn liên tiếp với biểu tượng hành động chặn màu đỏ (`X`), tương ứng lưu lượng từ nguồn `192.168.56.10` hướng tới đích `192.168.56.20` trên cổng 139 và 445, mang cờ TCP SYN (`TCP:S`) trên giao diện `CASE_C_KALI`. Trong lượt Case C, Nmap ghi nhận TCP 139/445 ở trạng thái FILTERED, đồng thời log pfSense ghi nhận lưu lượng TCP SYN tương ứng từ Kali tới các cổng này bị Block trên đường pfSense. Đề tài xác lập đây là sự đối chiếu liên tầng giữa phép đo quét mạng từ xa và nhật ký thiết bị kiểm soát đường truyền. Việc đối chiếu này dựa trên sự tương đồng về địa chỉ IP, cổng dịch vụ và cờ giao thức mà không giả định hai hệ thống có sự đồng bộ đồng hồ tuyệt đối.

Ảnh nhật ký hiển thị nhãn quy tắc không trùng với tên được ghi trong tệp ghi nhận lượt chạy Case C. Vì vậy, báo cáo chỉ sử dụng ảnh để xác nhận hành động Block đối với lưu lượng SMB SYN tương ứng trên đường truyền, không dùng ảnh này để quy thuộc tuyệt đối cho một tên quy tắc cụ thể. Cụ thể, ảnh tại Hình 3.11 hiển thị nhãn `CASE C baseline pass Kali to Windows (100000104)`, trong khi tệp ghi nhận lượt chạy Case C gán cho quy tắc `CASE C - Block SMB Kali to Windows (1000000104)`. Đề tài bảo tồn nguyên vẹn sự không thống nhất này như một ranh giới khách quan của bộ bằng chứng thực nghiệm và không đưa ra suy đoán chủ quan.

Tiếp theo, trạm Kali Linux đo đạc lại dấu hiệu lỗ hổng MS17-010 bằng kịch bản `smb-vuln-ms17-010` trên cổng 445. Phiên quét hoàn tất trong 0.51 giây, cổng 445 hiển thị `filtered microsoft-ds` và không xuất hiện khối kết quả `Host script results:`. Phép đo NSE-SMB-04 ghi nhận TCP 445 ở trạng thái FILTERED và không cung cấp phán quyết lỗ hổng khả dụng; kết quả được phân loại UNKNOWN / NO USABLE SCRIPT RESULT. Nguyên nhân ở mức cơ chế nội bộ của script không được xác lập từ bộ bằng chứng hiện có. Kết quả này không đồng nghĩa với việc máy chủ đã an toàn hay nguy cơ đã được loại bỏ (`UNKNOWN != SAFE`).

Đối với máy chủ Windows Server 2012 R2, Case C không ghi nhận ảnh chụp màn hình cục bộ mới do không can thiệp trực tiếp lên máy chủ. Dựa trên mốc xác lập tại Mục 3.1, Case C không ghi nhận thao tác thay đổi cấu hình SMB hoặc cài bản vá trên Windows. Trạng thái ghi nhận cuối lượt Case C cho thấy SMB1=True, SMB2=True, LanmanServer=Running, listener cục bộ 139/445 hiện diện và trạng thái bản vá vẫn được phân loại UNPATCHED dựa trên phiên bản số so sánh bản vá của driver `srv.sys` là `6.3.9600.16421`. Các quan sát FILTERED từ Kali được đối chiếu với các bản ghi Block tương ứng trên pfSense; việc này không làm thay đổi phân loại bản vá cục bộ của máy chủ.

Kết quả Case C cho thấy trạng thái quan sát từ xa trên đường mạng và trạng thái bản vá cục bộ là hai lớp thông tin khác nhau: TCP 139/445 được ghi nhận FILTERED từ Kali, trong khi máy chủ vẫn được phân loại UNPATCHED. Việc cổng dịch vụ bị lọc trên đường thử nghiệm không đồng nghĩa với máy chủ đã được vá lỗi (`FILTERED != PATCHED`). Sự so sánh đối chiếu đa chiều giữa ba trạng thái — đường cơ sở, vô hiệu hóa SMBv1 (Case B) và kiểm soát mạng bằng pfSense (Case C) — sẽ được tổng hợp tại Mục 3.6 tiếp theo.
