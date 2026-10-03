# KichBan-Nmap-SMB-139-445.docx

## Paragraphs

P0001 [Normal]: KỊCH BẢN THỰC NGHIỆM
P0002 [Normal]: "Phát hiện máy, quét cổng TCP 139/445 và nhận diện dịch vụ SMB bằng Nmap"
P0003 [Block Text]: Lưu ý: Đây là bản soạn thảo kịch bản dùng cho khóa luận. Các lệnh chỉ được thực thi sau khi có phê duyệt.
P0004 [Block Text]: Kịch bản tuân thủ chặt các ràng buộc cấp phép: chỉ tương tác 192.168.56.0/24, tốc độ ≤ T3, giới hạn retry, chỉ quét cổng cần thiết, không khai thác, không brute-force, không NSE thuộc nhóm exploit/intrusive/brute/dos (chỉ dùng script nhóm safe/discovery).
P0006 [Heading 1]: 1. Mục tiêu và phạm vi
P0007 [Heading 2]: 1.1. Mục tiêu
P0008 [First Paragraph]: Xây dựng và thực hiện quy trình trinh sát mạng (network reconnaissance) có kiểm soát trong môi trường lab nhằm:
P0009 [Compact]: Phát hiện máy hoạt động (host discovery) trong dải mạng lab.
P0010 [Compact]: Xác định máy mục tiêu và kiểm tra trạng thái hai cổng SMB điển hình: TCP 139 (NetBIOS Session Service) và TCP 445 (SMB over TCP / Microsoft-DS).
P0011 [Compact]: Nhận diện dịch vụ và phiên bản SMB, liệt kê các dialect (giao thức) SMB được hỗ trợ bằng các NSE script an toàn.
P0012 [Compact]: Lưu và phân tích kết quả một cách khách quan, không kết luận có lỗ hổng chỉ vì cổng mở.
P0013 [Heading 2]: 1.2. Phạm vi được cấp phép (In-scope)
P0014 [Heading 2]: 1.3. Ngoài phạm vi (Out-of-scope) — TUYỆT ĐỐI KHÔNG
P0015 [Compact]: Không quét Internet, mạng cơ quan/trường, hoặc bất kỳ IP nào ngoài 192.168.56.0/24.
P0016 [Compact]: Không khai thác lỗ hổng (no exploitation), không brute-force tài khoản.
P0017 [Compact]: Không dùng NSE nhóm exploit, intrusive, brute, dos.
P0018 [Compact]: Không quét toàn bộ 65535 cổng khi không cần thiết; chỉ quét cổng liên quan mục tiêu thực nghiệm.
P0020 [Heading 1]: 2. Điều kiện tiên quyết
P0021 [Compact]: Quyền hợp pháp: Có văn bản/biên bản cấp phép thực nghiệm trên lab 192.168.56.0/24 (đính kèm phần phụ lục khóa luận).
P0022 [Compact]: Cách ly mạng: VMware ở chế độ Host-only, không NAT/Bridge ra Internet trong lúc thực nghiệm (giảm rủi ro quét nhầm ngoài phạm vi).
P0023 [Compact]: Máy Kali:
P0024 [Compact]: Nmap phiên bản ≥ 7.90 (nmap --version).
P0025 [Compact]: Quyền root/sudo (cần cho ARP scan -PR và SYN scan -sS).
P0026 [Compact]: Card mạng gắn đúng vào host-only (vmnet/eth) với IP 192.168.56.10.
P0027 [Compact]: Máy mục tiêu: Đang bật, kết nối cùng host-only network, IP 192.168.56.20.
P0028 [Compact]: Thư mục lưu kết quả đã tạo sẵn, ví dụ ~/khoaluan/lab-smb/.
P0029 [Compact]: Đồng hồ/nhật ký: Ghi lại thời điểm bắt đầu–kết thúc mỗi bước để phục vụ báo cáo.
P0031 [Heading 1]: 3. Sơ đồ địa chỉ IP
P0032 [Source Code]: VMware Host-only Network: 192.168.56.0/24 (Không kết nối Internet) ┌───────────────────────────────────────────────────────────────┐ │ │ │ ┌──────────────────────┐ ┌──────────────────────┐ │ │ │ KALI LINUX │ │ WINDOWS TARGET │ │ │ │ (Máy kiểm thử) │ │ (Máy mục tiêu) │ │ │ │ │ Nmap │ │ │ │ │ IP: 192.168.56.10 │ ───────► │ IP: 192.168.56.20 │ │ │ │ Nmap 7.90+ (root) │ scan │ SMB: TCP 139/445 │ │ │ └──────────────────────┘ └──────────────────────┘ │ │ │ │ (Có thể có VMware host adapter, thường .1, ví dụ 192.168.56.1)│ └───────────────────────────────────────────────────────────────┘
P0034 [Heading 1]: 4. Danh sách công cụ
P0036 [Heading 1]: 5. Các bước thực hiện (tổng quan)
P0038 [Heading 1]: 6–9. Lệnh Nmap từng bước + Ý nghĩa tham số + Kết quả mong đợi + Pass/Fail
P0039 [Block Text]: Quy ước chung: -T3 (tốc độ Normal, không gây tải cao), --max-retries 2 (giới hạn thử lại), lưu kết quả bằng -oA (xuất đồng thời normal .nmap, XML .xml, grepable .gnmap).
P0040 [Heading 2]: BƯỚC 1 — Kiểm tra cấu hình mạng trên Kali (không dùng Nmap)
P0041 [Source Code]: ip addr show ip route show
P0042 [First Paragraph]: Ý nghĩa:
P0043 [Compact]: ip addr show — liệt kê interface và IP; xác nhận interface host-only đang mang IP 192.168.56.10.
P0044 [Compact]: ip route show — kiểm tra bảng định tuyến, đảm bảo lưu lượng tới 192.168.56.0/24 đi qua đúng interface host-only.
P0045 [First Paragraph]: Kết quả mong đợi: Thấy IP 192.168.56.10/24 trên interface host-only; có route trực tiếp (link) tới 192.168.56.0/24.
P0046 [Body Text]: Pass/Fail: Pass nếu IP Kali đúng 192.168.56.10 và route /24 tồn tại. Fail nếu IP sai/không có interface host-only → dừng, sửa cấu hình VMware trước khi tiếp tục.
P0048 [Heading 2]: BƯỚC 2 — Phát hiện host đang hoạt động trong dải lab (ARP discovery)
P0049 [Source Code]: sudo nmap -sn -PR 192.168.56.0/24 -T3 --max-retries 2 -oA b2_host_discovery
P0050 [First Paragraph]: Ý nghĩa từng tham số:
P0051 [Body Text]: Kết quả mong đợi: Danh sách các host "Host is up", trong đó có 192.168.56.20 (và thường 192.168.56.1 là host adapter). Mỗi host kèm địa chỉ MAC (do ARP).
P0052 [Body Text]: Pass/Fail: Pass nếu Nmap báo tối thiểu 1 host up và 192.168.56.20 xuất hiện. Fail nếu không phát hiện host nào → xử lý theo mục 12.
P0054 [Heading 2]: BƯỚC 3 — Xác nhận máy mục tiêu còn hoạt động
P0055 [Source Code]: sudo nmap -sn -PR 192.168.56.20 -T3 --max-retries 2 -oA b3_target_alive
P0056 [First Paragraph]: Ý nghĩa: Giống B2 nhưng thu hẹp về đúng 1 IP mục tiêu để xác nhận trước khi quét cổng, tránh gửi probe thừa ra toàn dải.
P0057 [Body Text]: Kết quả mong đợi: Host 192.168.56.20 is up, có MAC address.
P0058 [Body Text]: Pass/Fail: Pass nếu host up. Fail nếu "host down" → kiểm tra máy target/firewall (mục 12).
P0060 [Heading 2]: BƯỚC 4 — Kiểm tra trạng thái TCP 139 & 445
P0061 [Source Code]: sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports
P0062 [First Paragraph]: Ý nghĩa từng tham số:
P0063 [Body Text]: Kết quả mong đợi (một trong các khả năng):
P0064 [Compact]: 139/tcp open netbios-ssn và 445/tcp open microsoft-ds (target bật SMB) — hoặc
P0065 [Compact]: filtered (firewall chặn) — hoặc closed.
P0066 [First Paragraph]: Pass/Fail: Pass khi Nmap trả về trạng thái rõ ràng cho cả 2 cổng (open/closed/filtered) — bản thân việc xác định được trạng thái là mục tiêu, không bắt buộc phải "open". Fail nếu không nhận được phản hồi/không kết luận được trạng thái.
P0068 [Heading 2]: BƯỚC 5 — Nhận diện dịch vụ và phiên bản SMB
P0069 [Source Code]: sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version
P0070 [First Paragraph]: Ý nghĩa từng tham số:
P0071 [Body Text]: Kết quả mong đợi: Cột SERVICE/VERSION mô tả netbios-ssn, microsoft-ds, kèm thông tin như Windows ... microsoft-ds hoặc Samba smbd ... (nếu là Linux/Samba). Có thể suy ra hệ điều hành cấp cao.
P0072 [Body Text]: Pass/Fail: Pass nếu nhận diện được service name (và version nếu có). Fail nếu -sV không trả thông tin dù cổng open → tăng nhẹ intensity hoặc bổ sung NSE ở B6.
P0074 [Heading 2]: BƯỚC 6 — Liệt kê giao thức/dialect SMB bằng NSE an toàn
P0075 [Source Code]: sudo nmap -sS -p 139,445 \ --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities \ 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse
P0076 [First Paragraph]: Ý nghĩa các script (đều thuộc nhóm safe/discovery, KHÔNG intrusive/exploit/brute/dos):
P0077 [Body Text]: Kết quả mong đợi: Danh sách dialect (ví dụ hiển thị SMBv1 enabled/disabled, 2.0.2, 2.1, 3.x…), tên máy/OS, trạng thái signing.
P0078 [Body Text]: Pass/Fail: Pass nếu ít nhất smb-protocols trả về danh sách dialect. Fail nếu tất cả script không trả dữ liệu (thường do 445 filtered) → ghi nhận và xử lý theo mục 12.
P0079 [Block Text]: Ghi chú tuân thủ: 4 script trên chỉ đọc thông tin cấu hình/định danh. Không dùng smb-vuln-* (nhóm vuln/intrusive) vì nằm ngoài phạm vi cấp phép.
P0081 [Heading 2]: BƯỚC 7 — Lưu kết quả 3 định dạng
P0082 [First Paragraph]: Việc lưu đã được thực hiện tự động ở mỗi bước qua -oA, tạo ra bộ ba file:
P0083 [Body Text]: Ví dụ trích nhanh cổng mở từ grepable và (tùy chọn) xuất HTML:
P0084 [Source Code]: grep -E "139|445" b4_smb_ports.gnmap xsltproc b6_smb_nse.xml -o b6_smb_nse.html
P0085 [First Paragraph]: Pass/Fail: Pass nếu tồn tại đủ .nmap, .xml, .gnmap cho các bước B2–B6.
P0087 [Heading 2]: BƯỚC 8 — Phân tích kết quả (khách quan)
P0088 [First Paragraph]: Tổng hợp và diễn giải, tuân thủ nguyên tắc không suy diễn lỗ hổng:
P0089 [Compact]: Ghi nhận: cổng nào open/closed/filtered, dialect nào được hỗ trợ, signing bật hay tắt, OS/computer name.
P0090 [Compact]: Chỉ mô tả hiện trạng cấu hình. Ví dụ: "TCP 445 open, hỗ trợ SMBv1" là quan sát cấu hình, KHÔNG đồng nghĩa "máy có lỗ hổng". Việc có lỗ hổng cần đánh giá riêng (ngoài phạm vi bài này) qua patch level, CVE, v.v.
P0091 [Compact]: Nêu khuyến nghị mang tính quan sát (vd: "nên xác minh thêm cấu hình signing/SMBv1 theo chính sách") thay vì kết luận rủi ro.
P0093 [Heading 1]: 10. Bảng ghi nhận kết quả (mẫu điền khi thực hiện)
P0095 [Heading 1]: 11. Danh sách bằng chứng cần chụp
P0096 [Compact]: Ảnh ip addr / ip route xác nhận IP 192.168.56.10 (B1).
P0097 [Compact]: Ảnh kết quả host discovery hiển thị 192.168.56.20 is up + MAC (B2, B3).
P0098 [Compact]: Ảnh trạng thái cổng 139/445 kèm cột REASON (B4).
P0099 [Compact]: Ảnh kết quả -sV với Service/Version (B5).
P0100 [Compact]: Ảnh output NSE (dialect, OS, signing) (B6).
P0101 [Compact]: Ảnh ls -l thư mục kết quả cho thấy đủ bộ file .nmap/.xml/.gnmap (B7).
P0102 [Compact]: (Tùy chọn) Ảnh file HTML sinh từ xsltproc.
P0103 [Compact]: Ảnh đồng hồ/nhật ký ghi thời điểm bắt đầu–kết thúc (chứng minh nằm trong cửa sổ được phép).
P0104 [Compact]: Lưu bản sao các file .nmap/.xml làm phụ lục khóa luận.
P0106 [Heading 1]: 12. Các tình huống lỗi và cách xử lý
P0108 [Heading 1]: 13. Phần kết luận thực nghiệm (khung mẫu để hoàn thiện sau khi chạy)
P0109 [First Paragraph]: Sau khi thực hiện, phần kết luận nên nêu:
P0110 [Compact]: Xác nhận quy trình: Đã phát hiện host, xác định 192.168.56.20, kiểm tra được trạng thái TCP 139/445, nhận diện dịch vụ/phiên bản và liệt kê dialect SMB bằng NSE an toàn — toàn bộ trong phạm vi cấp phép, ≤ T3, retry giới hạn, chỉ cổng cần thiết.
P0111 [Compact]: Tóm tắt hiện trạng quan sát được (điền từ Bảng mục 10): cổng open/filtered, dialect hỗ trợ, signing, OS.
P0112 [Compact]: Giới hạn của thực nghiệm: Chỉ là trinh sát/định danh; không đánh giá lỗ hổng, không khai thác. Cổng SMB mở không đồng nghĩa có lỗ hổng.
P0113 [Compact]: Hướng phát triển (khuyến nghị, ngoài phạm vi bài này): đánh giá cấu hình signing/SMBv1 theo chính sách bảo mật, kiểm tra patch level — thực hiện trong một thực nghiệm riêng có cấp phép tương ứng.
P0114 [Compact]: Giá trị học thuật: Minh họa quy trình reconnaissance chuẩn, có kiểm soát, có đạo đức và tuân thủ phạm vi — phù hợp làm cơ sở phương pháp trong khóa luận.

## Tables

### Table 1
R001: Hạng mục | Giá trị
R002: Dải mạng duy nhất được phép | 192.168.56.0/24 (VMware Host-only)
R003: Máy kiểm thử (attacker) | Kali Linux — 192.168.56.10
R004: Máy mục tiêu (target) | Windows Server/Client — 192.168.56.20

### Table 2
R001: Thiết bị | IP | Vai trò | Cổng quan tâm
R002: Kali Linux | 192.168.56.10 | Máy nguồn quét | —
R003: Windows Target | 192.168.56.20 | Đối tượng thực nghiệm | TCP 139, TCP 445
R004: VMware host adapter | 192.168.56.1 (thường) | Gateway host-only | —

### Table 3
R001: Công cụ | Mục đích trong bài
R002: Nmap 7.90+ | Host discovery, port scan, service/version detection, NSE an toàn
R003: NSE scripts (nhóm safe/discovery) | smb-protocols, smb-os-discovery, smb2-security-mode, smb2-capabilities
R004: ip / ifconfig | Kiểm tra cấu hình mạng Kali
R005: ping | Kiểm tra kết nối L3 cơ bản (tùy chọn)
R006: grep, awk, less | Phân tích file kết quả grepable/normal
R007: xsltproc (tùy chọn) | Chuyển XML → HTML để trình bày trong khóa luận

### Table 4
R001: Bước | Nội dung | Mục tiêu thực nghiệm tương ứng
R002: B1 | Kiểm tra cấu hình mạng trên Kali | MT 1
R003: B2 | Phát hiện host đang hoạt động trong /24 (ARP) | MT 2
R004: B3 | Xác nhận máy mục tiêu 192.168.56.20 còn sống | MT 3
R005: B4 | Quét trạng thái TCP 139 & 445 (SYN scan) | MT 4
R006: B5 | Nhận diện dịch vụ & phiên bản SMB | MT 5
R007: B6 | Liệt kê dialect SMB bằng NSE an toàn | MT 6
R008: B7 | Lưu kết quả 3 định dạng (normal/XML/grepable) | MT 7
R009: B8 | Phân tích khách quan kết quả | MT 8

### Table 5
R001: Tham số | Ý nghĩa
R002: sudo | ARP scan cần quyền raw socket
R003: -sn | Ping scan — chỉ phát hiện host, không quét cổng
R004: -PR | Dùng ARP request để phát hiện host (chính xác nhất trong LAN host-only, không phụ thuộc ICMP bị chặn)
R005: 192.168.56.0/24 | Dải quét — đúng phạm vi cấp phép
R006: -T3 | Timing template Normal (≤ yêu cầu)
R007: --max-retries 2 | Tối đa 2 lần gửi lại probe → giảm nhiễu/tải
R008: -oA b2_host_discovery | Lưu cả 3 định dạng với tiền tố tên file

### Table 6
R001: Tham số | Ý nghĩa
R002: -sS | TCP SYN scan (half-open) — gửi SYN, đọc SYN/ACK hoặc RST, không hoàn tất bắt tay; nhanh, nhẹ
R003: -p 139,445 | Chỉ quét đúng 2 cổng cần thiết (đúng nguyên tắc tối thiểu hóa)
R004: --reason | Hiển thị lý do Nmap kết luận trạng thái (vd syn-ack, reset) — tăng tính minh bạch cho báo cáo
R005: còn lại | như B2

### Table 7
R001: Tham số | Ý nghĩa
R002: -sV | Version detection — dò tên/phiên bản dịch vụ trên cổng mở
R003: --version-intensity 5 | Cường độ dò mức trung bình (0–9); giữ ở 5 để cân bằng độ chính xác và mức độ "ồn"
R004: -p 139,445 | Chỉ 2 cổng SMB

### Table 8
R001: Script | Chức năng
R002: smb-protocols | Liệt kê các dialect SMB được hỗ trợ (SMBv1, SMB2, SMB3…)
R003: smb-os-discovery | Lấy thông tin OS, computer name, domain/workgroup qua SMB
R004: smb2-security-mode | Cho biết signing SMB2 có được yêu cầu/bật hay không
R005: smb2-capabilities | Liệt kê khả năng (capabilities) của các dialect SMB2

### Table 9
R001: Định dạng | Đuôi file | Dùng để
R002: Normal | .nmap | Đọc trực tiếp, chụp minh họa
R003: XML | .xml | Lưu trữ có cấu trúc, chuyển HTML
R004: Grepable | .gnmap | Trích lọc nhanh bằng grep/awk

### Table 10
R001: Bước | Lệnh (tóm tắt) | Thời gian | Kết quả quan sát | Pass/Fail | Ghi chú
R002: B1 | ip addr / ip route |  | IP Kali = ? |  | 
R003: B2 | nmap -sn -PR /24 |  | Số host up = ? ; có .20? |  | 
R004: B3 | nmap -sn -PR .20 |  | .20 up? MAC=? |  | 
R005: B4 | nmap -sS -p139,445 |  | 139=?/445=? (reason) |  | 
R006: B5 | nmap -sV -p139,445 |  | Service/Version=? |  | 
R007: B6 | nmap --script smb-* |  | Dialect=? Signing=? OS=? |  | 
R008: B7 | Kiểm tra file -oA |  | Đủ .nmap/.xml/.gnmap? |  | 
R009: B8 | Phân tích |  | Tóm tắt hiện trạng |  | 

### Table 11
R001: Tình huống | Nguyên nhân thường gặp | Cách xử lý (trong phạm vi)
R002: B2 không phát hiện host nào | Sai interface/IP Kali; VMware chưa gắn host-only | Kiểm tra lại ip addr; gắn đúng vmnet host-only; đảm bảo Kali .10
R003: .20 báo "host down" | Máy target tắt; firewall chặn ARP/ICMP | Bật lại target; vì -PR dùng ARP nên hầu như luôn thấy nếu cùng L2; kiểm tra target cùng subnet
R004: 139/445 hiển thị filtered | Windows Firewall chặn | Ghi nhận là "filtered" (kết quả hợp lệ); KHÔNG cố vượt firewall bằng evasion (ngoài phạm vi)
R005: -sV không ra version | Dịch vụ ẩn banner | Dùng NSE B6 để bổ sung thông tin; không nâng intensity quá cao
R006: NSE báo ERROR: Script execution failed | 445 filtered/không truy cập được | Xác nhận lại B4; nếu filtered thì ghi nhận, không ép chạy
R007: "You requested a scan type which requires root" | Thiếu quyền cho -sS/-PR | Chạy với sudo
R008: Quét chậm bất thường | Nhiều retry do mất gói | Giữ --max-retries 2; kiểm tra tải VMware; không tăng -T vượt T3
R009: Lỡ nhập IP ngoài phạm vi | Gõ nhầm dải | Dừng ngay (Ctrl+C); chỉ dùng 192.168.56.0/24; ghi nhận sự cố vào nhật ký
