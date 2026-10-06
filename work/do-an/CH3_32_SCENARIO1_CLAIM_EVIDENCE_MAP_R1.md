# MA TRẬN ÁNH XẠ LUẬN ĐIỂM – BẰNG CHỨNG MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1)

- **Trạng thái:** `R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B0 — Scenario 1 Evidence & Presentation Plan Only`
- **Mục tiêu:** Thiết lập tính truy vết 100% giữa từng kết luận dự kiến trong báo cáo của Kịch bản 1 với bằng chứng thực nghiệm trực tiếp và các ranh giới kỹ thuật đã được khóa.
- **Quy tắc nghiêm ngặt:**
  1. Sử dụng bằng chứng thô/trực tiếp trước siêu dữ liệu vận hành.
  2. Cột `Mã bằng chứng nội bộ (Stable Evidence ID)` sử dụng các mã đã đăng ký trong `CHAPTER_3_SECTION_EVIDENCE_MAP.md` và `CHAPTER_3_EVIDENCE_INDEX.md`: `S1-RAW-01` đến `S1-RAW-05` (tương ứng `S1-01` đến `S1-05`), `S1-IMG-02`, `S1-IMG-03`, và `S1-META-01` (`S1-06`).
  3. Cột `Câu văn được phép sử dụng (Allowed wording)` định hình câu văn chuẩn mực, đóng khung ranh giới kỹ thuật, không dùng từ ngữ tuyệt đối hóa.
  4. Cột `Suy diễn bị nghiêm cấm (Forbidden expansion)` nêu rõ các suy diễn vượt bằng chứng mà hội đồng phản biện có thể bắt lỗi.
  5. Đây là tài liệu QA và quản trị nội bộ; không đưa mã Claim ID, Evidence ID hay đường dẫn tệp vào văn xuôi báo cáo sinh viên.

---

## 1. Bảng Ánh Xạ Luận Điểm – Bằng Chứng Chi Tiết (Claim–Evidence Matrix)

| Claim ID | Tiểu mục đề xuất | Luận điểm tóm tắt (Short report claim) | Tệp bằng chứng trực tiếp (Direct/raw artifact) | Mã bằng chứng nội bộ (Stable Evidence ID) | Mã nguồn tham chiếu ngoài (External Source ID) | Câu văn được phép sử dụng (Allowed wording) | Suy diễn bị nghiêm cấm (Forbidden expansion) | Trạng thái (Status) |
|---|---|---|---|---|---|---|---|---|
| `S1-C01` | 3.2.1 | Phát hiện các trạm mạng hoạt động trong dải mạng nội bộ qua ARP | `scenario1/b2_host_discovery.{nmap,xml,gnmap}` | `S1-RAW-01` (`S1-01`) | — | Quét ARP toàn dải `192.168.56.0/24` từ trạm Kali Linux phát hiện 4 địa chỉ IP đang hoạt động trên phân đoạn mạng, bao gồm `192.168.56.1`, `192.168.56.10`, `192.168.56.20` và `192.168.56.100`. | Không suy diễn dải mạng có các trạm ẩn khác không phản hồi ARP; không mở rộng phạm vi ra ngoài phân đoạn lab. | `VERIFIED` |
| `S1-C02` | 3.2.1 | Định danh của thực thể `192.168.56.100` chưa xác định (UNKNOWN) | `scenario1/b2_host_discovery.{nmap,xml,gnmap}` | `S1-RAW-01` (`S1-01`) | — | Địa chỉ IP `192.168.56.100` ghi nhận phản hồi trong phân đoạn mạng nhưng danh tính và vai trò của thực thể này duy trì trạng thái chưa xác định (`UNKNOWN identity`). | **NGHIÊM CẤM:** Tuyệt đối không tự ý gán bất kỳ định danh cụ thể nào cho host `.56.100` (như "máy chủ DHCP", "router ảo", "trạm bổ trợ"). Không suy đoán từ địa chỉ MAC hay cấu hình mạng bên ngoài. | `VERIFIED` |
| `S1-C03` | 3.2.1 | Kiểm tra tính trực tuyến của máy chủ mục tiêu trước khi quét cổng | `scenario1/b3_target_alive.{nmap,xml,gnmap}` | `S1-RAW-02` (`S1-02`) | — | Phép thăm dò ARP đơn điểm tới máy chủ mục tiêu `192.168.56.20` xác nhận máy chủ đang trực tuyến với độ trễ phản hồi tức thời là `0,00034 s` (`0.00034s latency`). | Không suy đoán trạng thái cổng hay mức độ tải của máy chủ từ phản hồi trực tuyến. | `VERIFIED` |
| `S1-C04` | 3.2.1 | Cổng dịch vụ TCP 139 (netbios-ssn) ở trạng thái mở từ xa | `scenario1/b4_smb_ports.{nmap,xml,gnmap}`, `scenario1/Scenario1_B4_SMB_Ports.png` | `S1-RAW-03` (`S1-03`) | — | Phép quét TCP SYN từ trạm Kali ghi nhận cổng `139/tcp` ở trạng thái `OPEN` với dịch vụ `netbios-ssn`, căn cứ trên gói tin phản hồi `syn-ack` với `ttl=128`. | Không suy diễn cổng mở đồng nghĩa dịch vụ đã sẵn sàng tiếp nhận chia sẻ tệp không giới hạn. | `VERIFIED` |
| `S1-C05` | 3.2.1 | Cổng dịch vụ TCP 445 (microsoft-ds) ở trạng thái mở từ xa | `scenario1/b4_smb_ports.{nmap,xml,gnmap}`, `scenario1/Scenario1_B4_SMB_Ports.png` | `S1-RAW-03` (`S1-03`) | — | Phép quét TCP SYN từ trạm Kali ghi nhận cổng `445/tcp` ở trạng thái `OPEN` với dịch vụ `microsoft-ds`, căn cứ trên gói tin phản hồi `syn-ack` với `ttl=128`. | Không suy diễn quyền hạn truy cập của người dùng từ xa chỉ từ gói tin SYN-ACK của cổng. | `VERIFIED` |
| `S1-C06` | 3.2.1 | Ranh giới kỹ thuật: Cổng 445 mở không đồng nghĩa với tồn tại lỗ hổng | `scenario1/b4_smb_ports.{nmap,xml,gnmap}` | `S1-RAW-03` (`S1-03`) | — | Trạng thái `OPEN` của cổng 445 chỉ phản ánh khả năng tiếp cận dịch vụ từ xa qua mạng; cổng mở độc lập và không đồng nghĩa với việc hệ thống tồn tại lỗ hổng bảo mật (`445 OPEN != vulnerable`). | **NGHIÊM CẤM:** Không được biến kết quả mở cổng 445 thành kết luận hệ thống có lỗ hổng hoặc dễ bị khai thác bởi MS17-010. | `VERIFIED` |
| `S1-C07` | 3.2.2 | Dấu vết phiên bản dịch vụ từ xa của Nmap trên cổng 139 và 445 | `scenario1/b5_smb_version.{nmap,xml,gnmap}`, `scenario1/Scenario1_B5_SMB_Version.png` | `S1-RAW-04` (`S1-04`), `S1-IMG-02` | — | Phép thăm dò phiên bản dịch vụ từ xa của Nmap ghi nhận dịch vụ cổng 139 là `Microsoft Windows netbios-ssn` và cổng 445 là `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`. | Không suy đoán phiên bản dịch vụ vượt quá chuỗi văn bản Nmap nhận diện được. | `VERIFIED` |
| `S1-C08` | 3.2.2 | Ranh giới kỹ thuật: Dấu vết phiên bản là khoảng nhận diện, không định danh chính xác 2012 R2 | `scenario1/b5_smb_version.{nmap,xml,gnmap}`, `scenario1/Scenario1_B5_SMB_Version.png` | `S1-RAW-04` (`S1-04`), `S1-IMG-02` | — | Kết quả nhận diện hệ điều hành từ xa qua Nmap chỉ là một khoảng dấu vết ước lượng (`Microsoft Windows Server 2008 R2–2012`), không định danh chính xác phiên bản hệ điều hành máy chủ là Windows Server 2012 R2. | **NGHIÊM CẤM:** Tuyệt đối không tuyên bố kết quả B5 chứng minh hệ điều hành là Windows Server 2012 R2. Khẳng định Windows Server 2012 R2 chỉ dựa trên kiểm toán cục bộ mốc xuất phát tại Mục 3.1. | `VERIFIED` |
| `S1-C09` | 3.2.2 | Máy chủ hỗ trợ 5 phương ngữ SMB, bao gồm phương ngữ cũ SMBv1 | `scenario1/b6_smb_nse.{nmap,xml,gnmap}`, `scenario1/Scenario1_B6_SMB_NSE_A.png` | `S1-RAW-05` (`S1-05`), `S1-IMG-03` | — | Kịch bản `smb-protocols` ghi nhận máy chủ hỗ trợ 5 phương ngữ SMB: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, và `3.0.2`, xác nhận ngăn xếp SMB sẵn sàng đàm phán phương ngữ cũ SMBv1. | **NGHIÊM CẤM:** Sự hiện diện của phương ngữ SMBv1 không đồng nghĩa với việc đã xác nhận hệ thống dính lỗ hổng MS17-010 (`SMBv1 enabled != MS17-010 confirmed`). | `VERIFIED` |
| `S1-C10` | 3.2.2 | Chính sách ký số gói tin SMB từ xa là kích hoạt nhưng không bắt buộc | `scenario1/b6_smb_nse.{nmap,xml,gnmap}`, `scenario1/Scenario1_B6_SMB_NSE_A.png` | `S1-RAW-05` (`S1-05`), `S1-IMG-03` | — | Kịch bản `smb2-security-mode` xác định chính sách ký số gói tin của máy chủ mục tiêu ở trạng thái kích hoạt nhưng không bắt buộc (`Message signing enabled but not required`). | Không suy diễn chính sách ký số là điều kiện tiên quyết duy nhất cho việc tấn công hoặc bảo vệ trước lỗ hổng MS17-010. | `VERIFIED` |
| `S1-C11` | 3.2.2 | Các khả năng kỹ thuật SMB2 được ghi nhận trên từng phương ngữ | `scenario1/b6_smb_nse.{nmap,xml,gnmap}`, `scenario1/Scenario1_B6_SMB_NSE_A.png` | `S1-RAW-05` (`S1-05`), `S1-IMG-03` | — | Kịch bản `smb2-capabilities` ghi nhận tính năng `Distributed File System` trên phương ngữ 2.0.2; cùng tổ hợp `Distributed File System`, `Leasing`, `Multi-credit operations` trên các phương ngữ 2.1, 3.0 và 3.0.2. | Không mở rộng danh sách tính năng hay tự suy diễn các cơ chế kỹ thuật không có trong văn bản đầu ra của Nmap. | `VERIFIED` |
| `S1-C12` | 3.2.2 | Kịch bản `smb-os-discovery` không mang lại kết quả khả dụng | `scenario1/b6_smb_nse.{nmap,xml,gnmap}`, `scenario1/Scenario1_B6_SMB_NSE_A.png` | `S1-RAW-05` (`S1-05`), `S1-IMG-03` | — | Kịch bản `smb-os-discovery` không trả về đầu ra dữ liệu khả dụng (`no usable output`) trong kết quả thực thi Nmap của Kịch bản 1. | **NGHIÊM CẤM:** Không được tự suy diễn nguyên nhân cho việc vắng mặt đầu ra (không quy kết do tường lửa chặn, hệ thống từ chối hay kịch bản lỗi); không coi sự vắng mặt này là bằng chứng an toàn. | `VERIFIED` |
| `S1-C13` | 3.2.2 | Ranh giới tổng thể Kịch bản 1: Không đưa ra kết luận về lỗ hổng MS17-010 | Toàn bộ bộ bằng chứng Kịch bản 1 | `S1-RAW-01`..`05`, `S1-IMG-02`..`03` | — | Tiến trình khảo sát dịch vụ tại Kịch bản 1 chỉ xác lập các thuộc tính về trạng thái mở cổng, phiên bản dịch vụ và giao thức SMB từ xa; toàn bộ kết quả này chưa đủ cơ sở và không đưa ra kết luận về lỗ hổng MS17-010. | **NGHIÊM CẤM:** Tuyệt đối không tuyên bố Kịch bản 1 chứng minh máy chủ "dễ bị tấn công", "tồn tại lỗ hổng MS17-010" hay "đã được bảo vệ an toàn". Phán quyết về lỗ hổng thuộc về Kịch bản 2. | `VERIFIED` |

---

## 2. Thống Kê Ma Trận Luận Điểm Kịch Bản 1
- **Tổng số luận điểm:** 13 luận điểm (`S1-C01` đến `S1-C13`).
- **Phân bổ theo tiểu mục H3:**
  * Tiểu mục `3.2.1` (Khảo sát trạm mạng và trạng thái mở cổng SMB): 6 luận điểm (`S1-C01` đến `S1-C06`).
  * Tiểu mục `3.2.2` (Nhận diện phiên bản dịch vụ và đặc tính giao thức SMB): 7 luận điểm (`S1-C07` đến `S1-C13`).
- **Thẩm tra mã bằng chứng ổn định (Stable Evidence IDs):**
  * 100% sử dụng các mã đã đăng ký: `S1-RAW-01` đến `S1-RAW-05`, `S1-IMG-02`, `S1-IMG-03`, `S1-META-01`.
- **Tỷ lệ bằng chứng trực tiếp/thô:** 100% (Mọi claim đều có tệp dữ liệu thô Nmap hoặc ảnh chụp terminal trực tiếp tương ứng).
- **Rà soát ranh giới kỹ thuật nghiêm ngặt (Boundary & Overclaim Audit):**
  * Gán danh tính cho host `.56.100`: **0** (Duy trì nghiêm ngặt trạng thái `UNKNOWN`).
  * Đồng nhất cổng 445 OPEN với tồn tại lỗ hổng: **0** (`445 OPEN != vulnerable` được khóa chặt chẽ).
  * Đồng nhất dấu vết phiên bản B5 với Windows Server 2012 R2 chính xác: **0** (Chỉ ghi nhận khoảng `2008 R2–2012`).
  * Đồng nhất hỗ trợ SMBv1 với xác nhận lỗ hổng MS17-010: **0** (`SMBv1 enabled != MS17-010 confirmed`).
  * Bịa đặt nguyên nhân cho `smb-os-discovery`: **0** (Ghi nhận trung thực `no usable output`).
  * Tuyên bố phán quyết lỗ hổng MS17-010 trong Kịch bản 1: **0** (Khóa ranh giới chặt chẽ sang Kịch bản 2).
- **Trạng thái thẩm tra:** 100% đạt trạng thái `VERIFIED`.
