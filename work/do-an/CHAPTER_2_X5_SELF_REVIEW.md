# BÁO CÁO TỰ ĐÁNH GIÁ CHƯƠNG 2 THEO PHONG CÁCH DEMO / THỰC NGHIỆM
## (X5 DEMO-STYLE SELF-REVIEW R1)

**Thời điểm thực hiện:** 2026-10-05
**Vai trò thực hiện:** Executor / Writing Agent
**Tài liệu đánh giá:** `work/do-an/CHAPTER_2.md`
**Tài liệu nghiên cứu tham chiếu:** `work/do-an/X5_DEMO_STYLE_REFERENCE_REVIEW.md`
**Nhánh làm việc:** `feature/x5-chapter-2-demo-style`
**Yêu cầu thay đổi:** `CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE.md`
**Trạng thái đề xuất:** `X5_DEMO_STYLE_R1_RESEARCHED_AND_READY_FOR_EXTERNAL_REVIEW`

---

## 1. Tổng quan cấu trúc và dung lượng

- **Tiêu đề chương:** `# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO`
- **Số lượng phân mục:** Đạt chính xác **7 H2** và **20 H3** (100% khớp đề cương CR-2026-10-05-X5-DEMO-STYLE).
- **Dung lượng từ:** **3.863 từ** (nằm trọn vẹn trong khoảng ngân sách yêu cầu **3.200 – 4.000 từ**).
- **Kiến trúc trực quan:**
  - 02 sơ đồ trực quan Mermaid (Hình 2.1 — Sơ đồ topo mạng kết nối VirtualBox; Lưu đồ 4 bước quy trình Demo 1).
  - 02 bảng tổng hợp tinh gọn (Bảng 2.1 — Thông số kỹ thuật các máy ảo; Bảng 2.2 — Ma trận kiểm thử vi sai).
  - Khối lệnh bash và PowerShell tường minh, có chú thích tham số và mục đích rõ ràng.
- **Trích dẫn khoa học IEEE:** 11 nguồn tài liệu tham khảo (`[1]` đến `[11]`), xuất hiện tuần tự từ 1 đến 11, kết thúc bằng mục `# TÀI LIỆU THAM KHẢO`.

---

## 2. Reference-pattern compliance

Mục này trả lời trực tiếp 6 câu hỏi bắt buộc đối chiếu với nghiên cứu phong cách trình bày từ các đồ án thực tế:

### 2.1. Chương 2 đã áp dụng pattern nào từ research?
1. **Topology trước, cấu hình chi tiết sau:** Mở đầu Mục 2.1 bằng Sơ đồ topo mạng (Hình 2.1) trước khi trình bày Bảng 2.1 thông số môi trường, học tập từ pattern chuẩn của các đồ án ATTT PTIT/UIT.
2. **Gom thông số môi trường vào 1 bảng duy nhất:** Thay vì chia nhỏ cấu hình thành nhiều đoạn rời rạc, toàn bộ phần cứng, OS, build, IP, card mạng, cổng, dịch vụ được quy tụ trong Bảng 2.1.
3. **Demo presentation theo chuẩn thực nghiệm:** Cả Demo 1 và Demo 2 đều được tổ chức theo cấu trúc: *Mục tiêu & phạm vi $\rightarrow$ Điều kiện ban đầu $\rightarrow$ Quy trình từng bước & Lệnh thực thi $\rightarrow$ Nội dung quan sát & Ranh giới an ninh*.
4. **Tách biệt tuyệt đối quy trình và kết quả (Separation of Procedure and Results):** Toàn bộ số liệu quét thực tế, bảng chi tiết kết quả NSE, ảnh chụp kết quả và đánh giá chuyên sâu được bảo lưu hoàn toàn cho Chương 3. Chương 2 chỉ tập trung mô tả phương pháp, kịch bản, lệnh và điều kiện quan sát.
5. **Code block kèm giải thích tham số:** Mọi lệnh thực thi (`nmap`, `ping`, `Set-SmbServerConfiguration`, `Get-HotFix`) đều được đặt trong khối lệnh riêng biệt, có giải thích rõ mục đích từng cờ lệnh (`-sS`, `-sV`, `-Pn`, `--reason`, `--script`, `-oA`, `unsafe=0`).

### 2.2. Pattern nào chủ động không dùng?
1. **Chụp ảnh từng màn hình cài đặt (Next-Click Screenshotting):** Không đưa vào ảnh chụp cài đặt VirtualBox, cài đặt Windows hay các bước nhấp chuột thông thường. Thay vào đó, mô tả cấu hình thông qua câu lệnh PowerShell và thông số mạng cốt lõi.
2. **Lạm dụng heading phân mảnh (Heading Spam):** Không chia nhỏ mục thành H4/H5 hoặc các heading chỉ chứa 1–2 câu văn. Cấu trúc được khóa chặt chẽ ở 7 H2 và 20 H3 với độ dài đồng đều từ 80 đến 250 từ/mục.
3. **Chép lại lý thuyết nền tảng:** Không trình bày lại cơ chế hoạt động chi tiết của giao thức SMB hay phân tích mã khai thác EternalBlue trong chương thực nghiệm (nội dung này thuộc Chương 1).
4. **Bảng biểu lặp lại văn bản:** Bảng 2.1 và Bảng 2.2 có cấu trúc cô đọng, đóng vai trò bảng tra cứu nhanh, không lặp lại nguyên văn các câu văn mô tả.

### 2.3. Có đoạn nào vẫn giống leader/QA report không?
- **Không.** Toàn bộ các thuật ngữ mang tính điều hành dự án hoặc kiểm duyệt nội bộ (như "Canonical baseline", "Truth matrix", "Gate", "DEC-xx", "CP5-TECH", "Evidence Register") đã được loại bỏ 100% khỏi văn phong của chương.
- Văn bản được viết hoàn toàn bằng giọng văn học thuật kỹ thuật sinh viên: trung tính, trực tiếp, tập trung vào mô tả môi trường, thao tác cấu hình, quy trình rà quét và phân tích an ninh.

### 2.4. Có đoạn nào còn quá abstract không?
- **Không.** Toàn bộ quy trình đều được cụ thể hóa bằng các tham số kỹ thuật thực tế:
  - Địa chỉ IP cụ thể: `192.168.56.10/24`, `192.168.56.20/24`, gateway adapter `192.168.56.1/24`.
  - Cổng và dịch vụ cụ thể: TCP 139, TCP 445, dịch vụ `LanmanServer`.
  - Phiên bản driver cụ thể: `srv.sys` phiên bản `6.3.9600.16421` (ngưỡng an toàn `6.3.9600.18604`).
  - Lệnh Nmap và PowerShell đầy đủ tham số có thể chạy lại trực tiếp trên máy tính.

### 2.5. Người đọc có thể làm theo Demo 1 và Demo 2 không?
- **Hoàn toàn có thể làm theo.** Người đọc chỉ cần thiết lập VirtualBox Host-Only theo Bảng 2.1, cấu hình IP tĩnh và dịch vụ theo Mục 2.2, sau đó mở terminal Kali Linux thực thi tuần tự các lệnh trong Mục 2.3.2 (Demo 1) và Mục 2.4.2 (Demo 2) là có thể tái hiện chính xác môi trường và thu được các tệp dữ liệu `-oA`.

### 2.6. Có phần nào có thể cắt mà không mất thông tin không?
- Bản thảo đã trải qua 3 vòng hiệu chỉnh vi mô và tinh gọn từ 4.363 từ xuống 3.863 từ. Mọi câu văn thừa thãi, trùng lặp ý hoặc rườm rà đã được lược bỏ. Toàn bộ các câu văn hiện tại đều mang thông tin kỹ thuật, tham số môi trường hoặc ranh giới suy luận an toàn cần thiết, không thể cắt bớt thêm mà không làm giảm tính chặt chẽ của phương pháp luận.

---

## 3. Kiểm tra tính toàn vẹn kỹ thuật (Technical Truth Verification)

Bản thảo đảm bảo bảo toàn 100% các dữ kiện kỹ thuật nền tảng, không hồi quy:
1. **Nền tảng ảo hóa:** Oracle VM VirtualBox 7.2.20 r170876; mạng Host-Only `192.168.56.0/24`, tắt VirtualBox DHCP Server, không NAT/Bridged, không Default Gateway.
2. **Trạm kiểm thử (Attacker):** Kali Linux 64-bit Kernel 6.12.33-amd64 [2], 2 vCPU, 4096 MB RAM, IP tĩnh `192.168.56.10/24`, giao diện `eth0`, Nmap 7.99, `tcpdump`, `tshark`.
3. **Trạm mục tiêu (Target):** Windows Server 2012 R2 Standard Evaluation Build 9600 (RTM nguyên bản), 2 vCPU, 4096 MB RAM, IP tĩnh `192.168.56.20/24`, giao diện `Ethernet`.
4. **Dịch vụ mạng:** Dịch vụ máy chủ SMB `LanmanServer` khởi động tự động (`Automatic`), đang chạy (`Running`), lắng nghe trên TCP 445 (Direct-hosted SMB) và TCP 139 (NetBIOS Session Service qua TCP/IP) [3].
5. **Cấu hình giao thức:** `EnableSMB1Protocol = True`, `EnableSMB2Protocol = True`, tính năng `FS-SMB1` được cài đặt đầy đủ.
6. **Tường lửa trạm đích:** Windows Firewall bật (`Enabled`), luật Inbound cho phép TCP 139 và TCP 445 duy nhất từ địa chỉ nguồn `192.168.56.10`.
7. **Trạng thái bản vá:** `Get-HotFix` xác nhận vắng mặt KB4012213 và KB4012216 [4]; tệp driver `srv.sys` đạt phiên bản `6.3.9600.16421` (< `6.3.9600.18604` [5]), hệ thống ở trạng thái chưa vá (`UNPATCHED`).
8. **Kiểm soát biến:** Lưu điểm khôi phục snapshot `Before Demo` trên cả hai máy ảo VirtualBox trước khi thực hiện mọi phép đo.
9. **Kịch bản Demo 1:** Kiểm tra ping $\rightarrow$ Quét TCP SYN cổng 139, 445 (`-sS -Pn --reason -oA`) [6] $\rightarrow$ Nhận diện dịch vụ (`-sV -Pn -oA`) $\rightarrow$ Kịch bản NSE an toàn (`smb-protocols` [7], `smb-os-discovery`, `smb2-security-mode` [8], `smb2-capabilities`). Xác định rõ ranh giới: cổng mở không đồng nghĩa có lỗ hổng (`open != vulnerable`).
10. **Kịch bản Demo 2:** Bộ 4 phép đo chuẩn hóa `NSE-SMB-01` đến `NSE-SMB-04`. Cơ chế của `smb-vuln-ms17-010`: kết nối pipe `IPC$`, gửi gói tin giao dịch SMB tới FID 0, phân tích mã lỗi trả về (`STATUS_INSUFF_SERVER_RESOURCES` hoặc `STATUS_INVALID_HANDLE`) [9]; sử dụng `--script-args unsafe=0` để đảm bảo an toàn. Xác định rõ: kết quả từ xa không xác định không đồng nghĩa máy an toàn (`UNKNOWN != SAFE`).
11. **Giải pháp giảm thiểu rủi ro:**
    - Phương pháp kiểm thử vi sai trước và sau can thiệp (before-after test) dựa trên việc khôi phục snapshot `Before Demo`.
    - **Case B (Vô hiệu hóa SMBv1):** PowerShell `Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force` [10], xác thực bằng `Get-SmbServerConfiguration`. Xác định rõ ranh giới: tắt SMBv1 không đồng nghĩa driver đã được vá (`SMBv1 disabled != PATCHED`).
    - **Case C (Tường lửa phân đoạn mạng pfSense):** pfSense 2.7.2 chèn giữa hai máy ảo theo mô hình cầu nối trong suốt (Transparent Bridge) L2 [11]; cấu hình 3 tham số nhân bắt buộc: `net.link.bridge.pfil_member = 1`, `net.link.bridge.pfil_bridge = 0`, `net.link.bridge.pfil_onlyip = 1`; luật tường lửa chặn TCP 139 và TCP 445 đến `.20` có ghi nhật ký; cổng chuyển sang `filtered`. Xác định rõ ranh giới: cổng bị lọc không đồng nghĩa máy chủ đã vá lỗi (`FILTERED != PATCHED`).
    - **Case A (Cập nhật bản vá chính thức):** KB4012213 sửa lỗi trực tiếp trong driver nhân `srv.sys` [4], [5], so sánh ưu nhược điểm với Case B và Case C.
12. **Thu thập dữ liệu và Diễn giải:** Lưu trữ đồng thời 3 định dạng Nmap (`-oA`), nhật ký bắt gói tin `.pcap` bằng `tcpdump`/`tshark`, log Event Viewer/pfSense; áp dụng đầy đủ 6 nguyên tắc suy luận an toàn khi chuyển tiếp sang Chương 3.

---

## 4. Kiểm tra văn phong và quy tắc trình bày

- **Không chứa Evidence ID:** Toàn bộ các mã định danh nội bộ (`EVD-RAW-...`) không xuất hiện trong nội dung văn bản.
- **Không chứa Governance Jargon:** Không còn từ ngữ kiểu "canonical baseline", "truth matrix", "gate", "CP5".
- **Không rò rỉ kết quả (No Result Leakage):** Chương 2 hoàn toàn không chứa bảng số liệu đo đạc chi tiết của Chương 3 hay ảnh chụp kết quả scan thành công/thất bại.
- **Lệnh thực thi rõ ràng:** Lệnh được trình bày trong các code block có định dạng cú pháp rõ ràng, đi kèm chú giải cờ lệnh.
- **Sơ đồ và bảng biểu tinh gọn:** 2 hình vẽ (1 topo mạng, 1 lưu đồ quy trình) và 2 bảng thông số kỹ thuật.
- **Kiểm tra linter học thuật:** Script `lint_vi_academic.py` ghi nhận: **error=0, warning=0, info=0** (hoàn toàn sạch sẽ, không còn cảnh báo câu dài VI011).
- **Kiểm tra trích dẫn IEEE:** Script `audit_ieee_citations.py` ghi nhận: **11/11 trích dẫn hợp lệ, tuần tự từ 1 đến 11, không lỗi orphan hay missing**.

---

## 5. Kết luận và đề xuất

Bản thảo Chương 2 đã hoàn thành toàn diện theo phong cách đồ án thực nghiệm an toàn thông tin, dung lượng 3.863 từ đạt chuẩn, cấu trúc 7 H2 / 20 H3 vững chắc, bảo toàn nguyên vẹn chân lý kỹ thuật và tuân thủ các quy tắc trình bày rút ra từ nghiên cứu tham khảo.

Đề xuất chuyển giao bản thảo tới Hội đồng / External Reviewer để tiến hành kiểm duyệt độc lập:

**Trạng thái đề xuất:** `X5_DEMO_STYLE_R1_RESEARCHED_AND_READY_FOR_EXTERNAL_REVIEW`
