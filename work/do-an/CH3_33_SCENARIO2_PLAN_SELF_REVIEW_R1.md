# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.3 SCENARIO 2 R2 (CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7C0_SCENARIO2_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C0 R2 — Correct Scenario 2 Evidence/Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan của phiên bản R2 sau khi tiếp thu đầy đủ và khắc phục triệt để 7 vấn đề nêu trong báo cáo đánh giá ngoài `X7C0_SCENARIO2_PLAN_EXTERNAL_REVIEW_R1.md`. Tác giả tuyệt đối **không tự ý công bố PASS**; trạng thái nghiệm thu chính thức chỉ được quyết định sau khi có kết quả thẩm định ngoài độc lập lần cuối và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp R2 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng / Trạng thái | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số tệp bằng chứng Kịch bản 2 đã thẩm tra** | **17** | Thẩm tra 100% tệp trong `work/do-an/chapter3/evidence/scenario2/` |
| **Số lượng bộ ba tệp thô máy đọc (Raw triplets)** | **4** (12 tệp) | Đầy đủ 4 bộ ba (`.nmap`, `.xml`, `.gnmap`): NSE-SMB-01 (ports), NSE-SMB-02 (protocols), NSE-SMB-03 (signing), NSE-SMB-04 (ms17-010) |
| **Số lượng ảnh chụp màn hình gốc đã thẩm tra thị giác** | **4** | `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png`, `Scenario2_NSE04_MS17010.png` |
| **Số lượng tệp siêu dữ liệu thực thi đã thẩm tra** | **1** | `Scenario2_Run_Manifest.txt` |
| **Số lượng ảnh phân loại KEEP (Giữ lại)** | **1** | `Scenario2_NSE04_MS17010.png` (Hình 3.6 tạm thời) |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng)** | **0** | (Có phương án dự phòng 2 hình ghi nhận tại mục 4 của tài liệu chọn ảnh) |
| **Số lượng ảnh phân loại DROP (Loại bỏ)** | **3** | `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, `Scenario2_NSE03_Signing.png` (Trùng lặp với Mục 3.2, tích hợp vào Bảng 3.4) |
| **Số lượng tiểu mục H3 đề xuất cho Mục 3.3** | **2** | `3.3.1` (Điều kiện kết nối & thuộc tính SMB) và `3.3.2` (Dấu hiệu MS17-010 & đối chiếu bản vá) |
| **Số lượng bảng biểu đề xuất cho Mục 3.3** | **1** | `Bảng 3.4` (Trình tự và kết quả các phép đo NSE trên dịch vụ SMB từ trạm Kali Linux) |
| **Số lượng hình ảnh đề xuất cho Mục 3.3** | **1** | `Hình 3.6` (Kết quả thực thi kịch bản smb-vuln-ms17-010 từ trạm Kali Linux) |
| **Số lượng hàng luận điểm ánh xạ (Claim-Map Rows)** | **15** | 15 claims (`S2-C01` đến `S2-C15`), 100% đạt trạng thái `VERIFIED` |
| **Số lần xuất hiện cụm “Baseline Case A” trong kế hoạch hiện hành** | **0** | Đã loại bỏ 100%; chỉ dùng “baseline” hoặc “trạng thái baseline” |
| **Số lần phiên bản sai “Nmap 7.95” còn tồn tại** | **0** | Đã sửa chính xác thành “Nmap 7.99” theo tệp thô trực tiếp |
| **Số lần cụm “sẵn sàng tiếp nhận” xuất hiện trong bảng/mô tả công khai** | **0** | Đã thay thế bằng việc ghi nhận TCP 139/445 OPEN và phản hồi SYN-ACK |
| **Số lần lập luận SMBv1 là “điều kiện cần / tiên quyết”** | **0** | Đã loại bỏ hoàn toàn; chỉ ghi nhận 5 phương ngữ được `smb-protocols` liệt kê |
| **Tách biệt quan sát trực tiếp và phân loại UNKNOWN của NSE-SMB-04** | **Đạt** | Làm rõ ảnh chứng minh việc không xuất hiện script result; UNKNOWN là phân loại phương pháp luận |
| **Đối chiếu trạng thái bản vá cục bộ UNPATCHED** | **Đạt** | Tái sử dụng chuẩn xác công thức đã phê chuẩn tại Mục 3.1 |
| **Chuyển tiếp Case B ghi nhận các phép đo được chọn lặp lại** | **Đạt** | Ghi rõ chỉ lặp lại retest phương ngữ và retest MS17-010; không dùng “lặp lại toàn bộ” |
| **Số lượng tuyên bố “không gửi mã khai thác” trong S2-C15** | **0** | Đã chuẩn hóa thành: không có bước khai thác canonical và không có artifact/kết quả RCE/Meterpreter |
| **Phân biệt nhãn phép đo và mã nội bộ** | **Đạt** | `NSE-SMB-01..04` được phép dùng trong báo cáo; mã nội bộ (`S2-RAW-*`, `S2-IMG-*`, `S2-C*`) được bảo vệ |
| **Số lượng byte bằng chứng gốc bị thay đổi** | **0** | 100% bằng chứng gốc được bảo tồn nguyên vẹn |
| **Số lượng tệp văn xuôi Mục 3.3 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo thật trên đĩa** | **0** | Chỉ đề xuất tọa độ cắt cúp có thể tái lập trong kế hoạch; không tạo tệp phái sinh |
| **Số lượng vi phạm cách ly bằng chứng (Case B / Case C)** | **0** | 100% cách ly, không sử dụng bất kỳ dữ liệu nào từ Case B hay Case C |

---

## 2. Thẩm Tra Tính Trùng Lặp Với Mục 3.2 (Redundancy-with-3.2 Audit)

Kịch bản 2 lặp lại một số phép đo thuộc tính đã xuất hiện ở Kịch bản 1 (Mục 3.2):
- `NSE-SMB-01` lặp lại quan sát trạng thái cổng 139/445 của bước B4.
- `NSE-SMB-02` lặp lại 5 phương ngữ SMB của bước B6 (Hình 3.5).
- `NSE-SMB-03` lặp lại kết quả ký số `enabled but not required` của bước B6 (Hình 3.5).

**Quyết định thiết kế và xử lý trùng lặp:**
1. **Không tạo album ảnh terminal dư thừa:** Đã ra quyết định **DROP** cho cả 3 ảnh `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, và `Scenario2_NSE03_Signing.png`. Việc đưa thêm 3 ảnh chụp màn hình này sẽ gây lặp lại vô ích nội dung đã thấy ở Bảng 3.3 và Hình 3.5.
2. **Tổng hợp có hệ thống qua Bảng 3.4:** Toàn bộ kết quả của 3 phép đo tiền đề được tích hợp súc tích vào 3 hàng đầu của Bảng 3.4, giúp người đọc nắm bắt đầy đủ bối cảnh kỹ thuật mà không tốn diện tích trang in.
3. **Giữ lại duy nhất ảnh độc bản NSE-SMB-04:** Khẳng định giá trị thực nghiệm của ảnh `Scenario2_NSE04_MS17010.png` (Hình 3.6) vì đây là lần đầu tiên kịch bản chuyên dụng MS17-010 được thực thi với tùy chọn `--script smb-vuln-ms17-010`, minh chứng trực quan việc phiên quét hoàn tất và không xuất hiện phán quyết lỗ hổng.

---

## 3. Thẩm Tra Nguồn Gốc Dòng Lệnh Và Phiên Bản Nmap (Command-Lineage & Version Audit)

Kiểm toán nguồn gốc dòng lệnh giữa lớp người vận hành thao tác và lớp đối số do Nmap ghi nhận:
- **Lớp người vận hành (Operator/Manifest/Screenshot layer):**
  * NSE-SMB-01: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`
  * NSE-SMB-02: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`
  * NSE-SMB-03: `nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`
  * NSE-SMB-04: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`
- **Lớp đối số thô do Nmap ghi nhận (Raw argv layer):**
  * Trong phần header của tệp thô `.nmap` và `.xml`, Nmap ghi nhận phiên bản chính xác là **`Nmap 7.99`** (đã sửa chữa sai sót ghi `7.95` tại bản R1):
    `# Nmap 7.99 scan initiated Sat Oct  3 22:10:40 2026 as: /usr/lib/nmap/nmap --privileged -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`
- **Kết quả thẩm tra nguồn gốc:**
  * Kế hoạch xác định rõ hai tầng dữ liệu nguồn gốc độc lập: người vận hành **không gõ** `--privileged`, cờ này xuất hiện trong chuỗi argv do Nmap ghi nhận nội bộ. Kế hoạch không đưa ra suy đoán nguyên nhân vì sao Nmap chèn cờ này khi chưa có nguồn chứng minh độc lập.
  * Kế hoạch **không tự ý hòa giải hoặc "sửa" lớp này thành lớp kia**.
  * Trong thiết kế Bảng 3.4 công khai, sử dụng nhãn phép đo chuẩn hóa (`NSE-SMB-01` đến `NSE-SMB-04`) thay vì sao chép dòng lệnh dài dòng.
  * Tuyệt đối không tự ý thêm `sudo`, `-Pn`, hay bất kỳ tùy chọn nào vào sai tầng dữ liệu.

---

## 4. Thẩm Tra Ranh Giới Kỹ Thuật Từng Phép Đo (Technical Boundary Audits)

### 4.1. Phép đo NSE-SMB-01 (Port Boundary Audit)
- Kết quả quan sát: Cổng 139/tcp và 445/tcp ở trạng thái `OPEN`, phản hồi `syn-ack`, `ttl 128`.
- Hiệu chỉnh R2: Loại bỏ cụm từ suy diễn "sẵn sàng tiếp nhận kết nối qua mạng". Wording chuẩn mực: *Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.*
- Ranh giới kiểm tra: Trạng thái `OPEN` của cổng 445 chỉ chứng minh khả năng tiếp cận dịch vụ qua mạng từ trạm Kali, hoàn toàn **không đồng nghĩa với việc tồn tại lỗ hổng an ninh** (`445 OPEN != vulnerable`). Không suy diễn kết nối SMB tầng ứng dụng thành công hay tính sẵn sàng của tải chia sẻ tệp.

### 4.2. Phép đo NSE-SMB-02 (SMBv1 / MS17-010 Boundary Audit)
- Kết quả quan sát: Hỗ trợ 5 phương ngữ SMB: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`. Chú thích `[dangerous, but default]` là đầu ra nguyên văn của công cụ.
- Hiệu chỉnh R2: Loại bỏ toàn bộ các lập luận lý thuyết xem SMBv1 là "điều kiện cần" hoặc "điều kiện tiên quyết cho khả năng bị ảnh hưởng".
- Ranh giới kiểm tra: Sự hiện diện của phương ngữ SMBv1 **hoàn toàn không đồng nghĩa với việc xác nhận hệ thống dính lỗ hổng MS17-010** (`SMBv1 enabled != MS17-010 confirmed`). Cụm từ "dangerous, but default" trong output của Nmap là chú thích chung của công cụ, không phải là phán quyết lỗ hổng trên mục tiêu.

### 4.3. Phép đo NSE-SMB-03 (Signing Layer Independence Audit)
- Kết quả quan sát: `Message signing enabled but not required` trên phương ngữ 3.0.2.
- Ranh giới kiểm tra: Đây là quan sát ký số từ xa qua đàm phán giao thức của Nmap, **độc lập với cờ cấu hình nội bộ `RequireSecuritySignature` tại Mục 3.1**. Không khái quát hóa cho mọi phương ngữ khác, và không dùng quan sát này để xác nhận hay hòa giải với cấu hình cục bộ.

### 4.4. Phép đo NSE-SMB-04 (Negative / Indeterminate Output Audit)
- Tách biệt rõ ràng hai lớp:
  * **Quan sát trực tiếp (Direct Observation):** Lệnh Nmap được thực thi với tùy chọn `--script smb-vuln-ms17-010`, mục tiêu trực tuyến, cổng 445 mở, phiên quét hoàn tất với thông báo `Nmap done`, không xuất hiện khối kết quả `Host script results:`, và không có thông báo lỗi hiển thị trong đầu ra ghi nhận.
  * **Phân loại phương pháp luận của đề án (Project Classification):** `UNKNOWN / NO USABLE SCRIPT RESULT`.
- Hiệu chỉnh R2:
  * Khẳng định rõ `UNKNOWN` không phải là chuỗi ký tự nguyên văn do Nmap in ra màn hình.
  * Không tuyên bố ảnh chụp màn hình tự nó "chứng minh UNKNOWN"; ảnh chụp màn hình hỗ trợ quan sát trực tiếp về việc không xuất hiện khối kết quả script.
  * Không nhấn mạnh chỉ số thời gian `1.35 seconds` trong Bảng 3.4 công khai hay văn xuôi tương lai vì không mang giá trị phân tích an ninh.
  * Loại bỏ các từ ngữ tuyệt đối hóa như "hoàn toàn vắng mặt", "bằng chứng không thể thay thế".
  * Cấm tuyệt đối các phán quyết bịa đặt: `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, `PATCHED`.
  * Không gọi kịch bản "thất bại" (failed) khi không có thông báo lỗi từ Nmap. Không bịa đặt mã lỗi NTSTATUS.

---

## 5. Thẩm Tra Khóa Logic Cốt Lõi `UNKNOWN != SAFE`

- Quán triệt sâu sắc nguyên tắc:
  > **`UNKNOWN != SAFE`** (Không có kết quả khả dụng hoàn toàn KHÔNG đồng nghĩa với an toàn).
- Văn bản kế hoạch chỉ ghi nhận rằng phép đo từ xa không cung cấp phán quyết lỗ hổng khả dụng; nguyên nhân của việc không có đầu ra script không được xác lập. Kết quả này không chứng minh máy chủ an toàn hay đã được khắc phục lỗ hổng.
- Số lượng vi phạm suy diễn an toàn từ kết quả UNKNOWN: **0**.

---

## 6. Thẩm Tra Tính Độc Lập Giữa Mốc Cục Bộ UNPATCHED Và Quan Sát Từ Xa UNKNOWN

- Tái sử dụng chuẩn xác công thức đã phê chuẩn tại Mục 3.1:
  > *Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa (srv.sys = 6.3.9600.16421 thấp hơn ngưỡng tối thiểu 6.3.9600.18604; danh mục hotfix quan sát được không ghi nhận KB4012213, KB4012216 hoặc bản cập nhật thay thế đã được ánh xạ là chứa bản sửa lỗi MS17-010).*
- Không viết các phát biểu mang tính toàn tri rằng toàn bộ lịch sử hệ thống thiếu bản vá; chỉ giới hạn trong danh mục hotfix quan sát được.
- Rà soát cấm suy diễn chéo:
  * Không dùng mốc `UNPATCHED` cục bộ để ép phán quyết từ xa thành `VULNERABLE`.
  * Không dùng kết quả từ xa `UNKNOWN` để phủ định mốc cục bộ thành `SAFE` hoặc `PATCHED`.
  * Không tuyên bố sự khác biệt giữa hai trục là mâu thuẫn hay "âm tính giả".

---

## 7. Thẩm Tra Ngăn Chặn Thuật Ngữ "Âm Tính Giả" (False Negative Prohibition Audit)

- Thuật ngữ "âm tính giả" (false negative) giả định trước rằng kết quả từ xa *đáng lẽ phải* trả về VULNERABLE, từ đó áp đặt định kiến chủ quan lên phép đo thực nghiệm.
- **Kết quả rà soát:** Trong toàn bộ các câu văn được phép sử dụng (Allowed wording) của 15 luận điểm và toàn bộ nội dung kế hoạch trình bày, **tuyệt đối không xuất hiện thuật ngữ "âm tính giả" / "false negative"** (ngoại trừ các dòng cấm đoán trong phần audit này).
- Số lượng vi phạm: **0**.

---

## 8. Thẩm Tra Ngăn Chặn Rò Rỉ Khai Thác / RCE (Exploit / RCE Leakage Audit)

- Kịch bản 2 được trình bày trong phạm vi rà quét NSE từ xa; bộ bằng chứng không chứa bước khai thác canonical hay artifact/kết quả RCE, reverse shell hoặc Meterpreter.
- Hiệu chỉnh R2 cho `S2-C15`: Loại bỏ câu chữ mô tả hành vi gói tin nội bộ "không gửi mã khai thác tấn công". Thay thế bằng ranh giới cấp độ dự án:
  > *Không có bước khai thác canonical và không có artifact/kết quả RCE, reverse shell hoặc Meterpreter trong Kịch bản 2.*
- Tuyệt đối không nhắc đến payload khai thác, khung Metasploit, hay việc chiếm quyền điều khiển hệ thống.
- Số lượng vi phạm: **0**.

---

## 9. Thẩm Tra Đoạn Chuyển Tiếp Sang Case B (Transition to Case B Audit)

- **Loại bỏ hoàn toàn cụm từ “Baseline Case A”:** Baseline không phải là Case A. Đã thay thế thành: *Sau khi hoàn tất trạng thái baseline và hai kịch bản đo đạc ban đầu...*
- **Sửa phạm vi đo đạc lặp lại:** Loại bỏ cách nói "lặp lại toàn bộ các phép đo". Ghi nhận chính xác: *tiến hành cấu hình vô hiệu hóa giao thức SMBv1 trên máy chủ Windows Server 2012 R2, sau đó thực hiện lặp lại các phép đo được chọn (bao gồm phép đo kiểm tra phương ngữ và phép đo kiểm tra kịch bản MS17-010) để đối chiếu sự thay đổi về danh mục phương ngữ và phản hồi từ xa.*
- **Bảo toàn kết quả:** Không tiết lộ bất kỳ số liệu hay kết quả cụ thể nào của Case B; loại bỏ cụm từ "đánh giá hiệu quả" trong chuyển tiếp vì việc đánh giá hiệu quả thuộc về Chương 4.

---

## 10. Thẩm Tra Phân Biệt Nhãn Phép Đo Và Mã Bằng Chứng Nội Bộ (Identifier Taxonomy Audit)

- `NSE-SMB-01`, `NSE-SMB-02`, `NSE-SMB-03`, `NSE-SMB-04` là **nhãn phép đo (measurement labels)** được phê chuẩn từ phương pháp thực nghiệm tại Chương 2. Chúng được phép xuất hiện trong Bảng 3.4 và văn bản báo cáo.
- Các mã định danh quản trị nội bộ tuyệt đối không xuất hiện trong nội dung báo cáo sinh viên gồm:
  * Mã bằng chứng nội bộ: `S2-RAW-01` đến `S2-RAW-04`, `S2-IMG-01` đến `S2-IMG-04`, `S2-META-01`;
  * Mã luận điểm: `S2-C01` đến `S2-C15`;
  * Đường dẫn tệp trong kho lưu trữ.
- Đã chỉnh sửa quy tắc trong tài liệu kế hoạch trình bày để không gọi nhầm nhãn phép đo là Evidence ID.

---

## 11. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- Toàn bộ kế hoạch X7C0 R2 chỉ sử dụng:
  * 17 tệp bằng chứng Kịch bản 2 đã stage tại `work/do-an/chapter3/evidence/scenario2/`;
  * Bằng chứng mốc chuẩn cục bộ Mục 3.1 (`ENV-CORE-03`, `ENV-CORE-05`) phục vụ đối chiếu giới hạn phân loại;
  * Mã nguồn ngoài Microsoft S032 phục vụ ánh xạ mã bản vá KB.
- Tuyệt đối không sử dụng, không tham chiếu và không trích xuất bất kỳ tệp dữ liệu nào từ:
  * Thư mục `case_b/` (Biện pháp tắt SMBv1);
  * Thư mục `case_c/` (Biện pháp tường lửa pfSense);
  * Các bản thảo và kết luận thuộc phạm vi Chương 4.
- Số lượng vi phạm cách ly bằng chứng: **0**.

---

## 12. Kết Luận Và Trạng Thái Cuối Cùng Của Executor

Bốn tài liệu kế hoạch X7C0 đã được hiệu chỉnh hoàn tất theo chuẩn mực nghiêm ngặt nhất của vòng R2:
- [CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_FIGURE_SELECTION_R1.md)
- [CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_PRESENTATION_PLAN_R1.md)
- [CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_CLAIM_EVIDENCE_MAP_R1.md)
- [CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1.md](file:///e:/word_ppt-auto/work/do-an/CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1.md)

- **Trạng thái chính thức đề xuất:**
  `X7C0_SCENARIO2_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
