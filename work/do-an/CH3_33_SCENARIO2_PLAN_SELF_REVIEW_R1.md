# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.3 SCENARIO 2 R1 (CH3_33_SCENARIO2_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7C0_SCENARIO2_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7C0 — Scenario 2 Evidence & Presentation Plan Only`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan và toàn diện của phiên bản R1 đối với Kịch bản 2. Tác giả tuyệt đối **không tự ý công bố PASS**; trạng thái nghiệm thu chính thức chỉ được quyết định sau khi có kết quả thẩm định ngoài độc lập (Independent External Review) và sự phê duyệt chính thức của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp (Summary Metrics)

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
| **Số lượng byte bằng chứng gốc bị thay đổi** | **0** | 100% bằng chứng gốc được bảo tồn nguyên vẹn |
| **Số lượng tệp văn xuôi Mục 3.3 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo thật trên đĩa** | **0** | Chỉ đề xuất tọa độ cắt cúp có thể tái lập trong kế hoạch; không tạo tệp phái sinh |
| **Số lượng vi phạm cách ly bằng chứng (Case B / Case C)** | **0** | 100% cách ly, không sử dụng bất kỳ dữ liệu nào từ Case B hay Case C |

---

## 2. Thẩm Tra Tính Trùng Lặp Với Mục 3.2 (Redundancy-with-3.2 Audit)

Kịch bản 2 lặp lại một số phép đo thuộc tính đã xuất hiện ở Kịch bản 1 (Mục 3.2):
- `NSE-SMB-01` trùng lặp về mặt quan sát trạng thái cổng 139/445 với bước B4 của Mục 3.2.
- `NSE-SMB-02` trùng lặp về 5 phương ngữ SMB với kết quả `smb-protocols` của bước B6 (Hình 3.5).
- `NSE-SMB-03` trùng lặp về kết quả ký số `enabled but not required` với bước B6 (Hình 3.5).

**Quyết định thiết kế và xử lý trùng lặp:**
1. **Không tạo "album ảnh terminal" dư thừa:** Đã ra quyết định **DROP** cho cả 3 ảnh `Scenario2_NSE01_Ports.png`, `Scenario2_NSE02_Protocols.png`, và `Scenario2_NSE03_Signing.png`. Việc đưa thêm 3 ảnh chụp màn hình này sẽ gây lặp lại vô ích nội dung đã thấy ở Bảng 3.3 và Hình 3.5.
2. **Tổng hợp có hệ thống qua Bảng 3.4:** Toàn bộ kết quả của 3 phép đo tiền đề được tích hợp súc tích vào 3 hàng đầu của Bảng 3.4, giúp người đọc nắm bắt đầy đủ bối cảnh kỹ thuật mà không tốn diện tích trang in.
3. **Giữ lại duy nhất ảnh độc bản NSE-SMB-04:** Khẳng định giá trị thực nghiệm cốt lõi của ảnh `Scenario2_NSE04_MS17010.png` (Hình 3.6) vì đây là lần đầu tiên kịch bản chuyên dụng MS17-010 được kích hoạt, minh chứng trực quan việc hoàn tất quét không có phán quyết lỗ hổng.

---

## 3. Thẩm Tra Nguồn Gốc Dòng Lệnh (Command-Lineage Audit)

Kiểm toán nguồn gốc dòng lệnh giữa lớp người vận hành thao tác và lớp đối số do Nmap ghi nhận:
- **Lớp người vận hành (Operator/Manifest/Screenshot layer):**
  * NSE-SMB-01: `sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20`
  * NSE-SMB-02: `nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20`
  * NSE-SMB-03: `nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20`
  * NSE-SMB-04: `nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20`
- **Lớp đối số thô do Nmap ghi nhận (Raw argv layer):**
  * Trong phần header của tệp thô `.nmap` và `.xml`, Nmap tự động chuẩn hóa đối số khi thực thi dưới quyền root thành:
    `# Nmap 7.95 scan initiated ... as: nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 --privileged 192.168.56.20`
- **Kết quả thẩm tra:**
  * Kế hoạch xác định rõ đây là **hai tầng dữ liệu nguồn gốc khác nhau**: người vận hành **không gõ** `--privileged`, cờ này do Nmap tự động chèn vào chuỗi argv nội bộ.
  * Kế hoạch **không tự ý hòa giải hoặc "sửa" lớp này thành lớp kia**.
  * Trong thiết kế Bảng 3.4 công khai, sử dụng nhãn phương pháp súc tích thay vì sao chép dòng lệnh dài dòng, triệt tiêu hoàn toàn rủi ro gây tranh cãi về cú pháp lệnh.
  * Tuyệt đối không tự ý thêm `sudo`, `-Pn`, hay bất kỳ tùy chọn nào vào sai tầng dữ liệu.

---

## 4. Thẩm Tra Ranh Giới Kỹ Thuật Từng Phép Đo (Technical Boundary Audits)

### 4.1. Phép đo NSE-SMB-01 (Port Boundary Audit)
- Kết quả quan sát: `139/tcp open` và `445/tcp open`, `syn-ack ttl 128`.
- Ranh giới kiểm tra: Trạng thái `OPEN` của cổng 445 chỉ chứng minh khả năng tiếp cận dịch vụ qua mạng từ trạm Kali, hoàn toàn **không đồng nghĩa với việc tồn tại lỗ hổng an ninh** (`445 OPEN != vulnerable`).
- Vi phạm quy kết lỗ hổng từ cổng mở: **0**.

### 4.2. Phép đo NSE-SMB-02 (SMBv1 / MS17-010 Boundary Audit)
- Kết quả quan sát: Hỗ trợ 5 phương ngữ SMB, bao gồm `NT LM 0.12 (SMBv1)`.
- Ranh giới kiểm tra: Sự hiện diện của phương ngữ SMBv1 chỉ là điều kiện cần về giao thức kế thừa, **hoàn toàn không đồng nghĩa với việc xác nhận hệ thống dính lỗ hổng MS17-010** (`SMBv1 enabled != MS17-010 confirmed`). Cụm từ "dangerous, but default" trong output của Nmap là chú thích chung của công cụ, không phải là phán quyết lỗ hổng trên mục tiêu.
- Vi phạm quy kết lỗ hổng từ SMBv1: **0**.

### 4.3. Phép đo NSE-SMB-03 (Signing Layer Independence Audit)
- Kết quả quan sát: `Message signing enabled but not required` trên phương ngữ 3.0.2.
- Ranh giới kiểm tra: Đây là quan sát ký số từ xa qua đàm phán giao thức của Nmap, **độc lập với cờ cấu hình nội bộ `RequireSecuritySignature` tại Mục 3.1**. Không khái quát hóa cho mọi phương ngữ khác, và không dùng quan sát này để xác nhận hay hòa giải với cấu hình cục bộ.
- Vi phạm hòa giải ký số: **0**.

### 4.4. Phép đo NSE-SMB-04 (Negative / No-Output Audit)
- Kết quả quan sát: Kịch bản được gọi, mục tiêu trực tuyến, cổng 445 mở, phiên quét kết thúc trong 1.35 giây, **hoàn toàn vắng mặt khối kết quả Host script results**.
- Ranh giới kiểm tra:
  * Phân loại chuẩn xác: `UNKNOWN / NO USABLE SCRIPT RESULT`.
  * Cấm tuyệt đối các phán quyết bịa đặt: `VULNERABLE`, `SAFE`, `NOT VULNERABLE`, `PATCHED`.
  * Không gọi kịch bản "thất bại" (failed) khi không có thông báo lỗi từ Nmap.
  * Không bịa đặt mã lỗi phản hồi NTSTATUS.
  * Không phỏng đoán các nguyên nhân không có căn cứ (như lỗi tường lửa, lỗi script).
- Vi phạm bịa đặt phán quyết hoặc nguyên nhân: **0**.

---

## 5. Thẩm Tra Khóa Logic Cốt Lõi `UNKNOWN != SAFE`

- Một sai lầm kinh điển trong đánh giá an toàn thông tin là xem việc công cụ không phát hiện ra lỗ hổng là minh chứng cho việc hệ thống đã an toàn.
- Kế hoạch trình bày R1 đã quán triệt sâu sắc nguyên tắc:
  > **`UNKNOWN != SAFE`** (Không có kết quả khả dụng hoàn toàn KHÔNG đồng nghĩa với an toàn).
- Văn bản kế hoạch khẳng định việc Nmap không trả về phán quyết lỗ hổng chỉ phản ánh giới hạn nhận diện của công cụ quét từ xa trong điều kiện thực nghiệm cụ thể, không chứng minh máy chủ miễn nhiễm hoặc đã được vá lỗi.
- Số lượng vi phạm suy diễn an toàn từ kết quả UNKNOWN: **0**.

---

## 6. Thẩm Tra Tính Độc Lập Giữa Mốc Cục Bộ UNPATCHED Và Quan Sát Từ Xa UNKNOWN

- Kế hoạch thiết lập ranh giới tách biệt tuyệt đối giữa hai trục dữ liệu:
  * **Trục nội tại cục bộ (Mục 3.1):** Máy chủ Windows Server 2012 R2 chưa được cài đặt bản cập nhật bảo mật KB4012213/KB4012216 (`UNPATCHED`).
  * **Trục đo đạc từ xa (Mục 3.3):** Kịch bản NSE `smb-vuln-ms17-010` không sinh đầu ra khả dụng (`UNKNOWN / NO USABLE SCRIPT RESULT`).
- **Rà soát cấm suy diễn chéo:**
  * Không dùng mốc `UNPATCHED` cục bộ để ép phán quyết từ xa thành `VULNERABLE`.
  * Không dùng kết quả từ xa `UNKNOWN` để phủ định mốc cục bộ thành `SAFE` hoặc `PATCHED`.
  * Không tuyên bố sự khác biệt giữa hai trục là mâu thuẫn hay sai sót dữ liệu.
- Vi phạm suy diễn chéo giữa hai trục: **0**.

---

## 7. Thẩm Tra Ngăn Chặn Thuật Ngữ "Âm Tính Giả" (False Negative Prohibition Audit)

- Thuật ngữ "âm tính giả" (false negative) giả định trước rằng kết quả từ xa *đáng lẽ phải* trả về VULNERABLE vì hệ thống cục bộ là UNPATCHED, từ đó áp đặt định kiến chủ quan lên phép đo thực nghiệm.
- **Kết quả rà soát:** Trong toàn bộ các câu văn được phép sử dụng (Allowed wording) của 15 luận điểm và toàn bộ nội dung kế hoạch trình bày, **tuyệt đối không xuất hiện thuật ngữ "âm tính giả" / "false negative"** (ngoại trừ các điều cấm trong phần audit này).
- Số lượng sử dụng sai lệch thuật ngữ false negative: **0**.

---

## 8. Thẩm Tra Ngăn Chặn Rò Rỉ Khai Thác / RCE (Exploit / RCE Leakage Audit)

- Kịch bản 2 là một kịch bản rà quét an ninh từ xa bằng kịch bản Nmap NSE, hoàn toàn không phải là kịch bản khai thác tấn công (Exploitation / Penetration Testing).
- **Kết quả rà soát:**
  * Tuyệt đối không nhắc đến mã khai thác (exploit payload), khung khai thác (Metasploit), hay việc chiếm quyền điều khiển hệ thống.
  * Không tuyên bố khai thác thành công hay thất bại.
  * Luận điểm `S2-C15` đã khóa chặt ranh giới này.
- Số lượng vi phạm rò rỉ khai thác / RCE: **0**.

---

## 9. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- Toàn bộ kế hoạch X7C0 chỉ sử dụng:
  * 17 tệp bằng chứng Kịch bản 2 đã stage tại `work/do-an/chapter3/evidence/scenario2/`;
  * Bằng chứng mốc chuẩn cục bộ Mục 3.1 (`ENV-CORE-03`, `ENV-CORE-05`) phục vụ đối chiếu giới hạn phân loại;
  * Mã nguồn ngoài Microsoft S032 phục vụ ánh xạ mã bản vá KB.
- Tuyệt đối không sử dụng, không tham chiếu và không trích xuất bất kỳ tệp dữ liệu nào từ:
  * Thư mục `case_b/` (Biện pháp tắt SMBv1);
  * Thư mục `case_c/` (Biện pháp tường lửa pfSense);
  * Các bản thảo và kết luận thuộc phạm vi Chương 4.
- Số lượng vi phạm cách ly bằng chứng: **0**.

---

## 10. Các Vấn Đề Trình Bày Mở / Cần Lưu Ý Trong Pha Soạn Thảo (Open Items for Drafting)

1. **Khung cắt cúp đề xuất cho Hình 3.6:** Khung cắt cúp đề xuất `x = 0, y = 24, width = 1280, height = 330` được thiết kế tối ưu cho trang in A4 portrait. Khi bước sang pha phê duyệt hoặc tạo ảnh phái sinh, cần bảo đảm công cụ crop giữ đúng tỷ lệ và cỡ chữ dễ đọc.
2. **Phương án dự phòng 2 hình:** Nếu người phản biện ngoài hoặc hội đồng yêu cầu đưa thêm ảnh danh sách phương ngữ ngay tại Mục 3.3, phương án kích hoạt `Scenario2_NSE02_Protocols.png` làm Hình 3.6 (và NSE04 thành Hình 3.7) đã sẵn sàng để chuyển đổi mà không làm thay đổi cấu trúc bảng và luận điểm.
3. **Giữ nghiêm kỷ luật ZERO PROSE:** Bản thân tài liệu kế hoạch này không chứa văn xuôi hoàn chỉnh của báo cáo; toàn bộ việc soạn thảo văn xuôi sẽ được thực hiện tại pha X7C1 sau khi kế hoạch được phê duyệt.

---

## 11. Kết Luận Và Trạng Thái Cuối Cùng Của Executor

Kế hoạch trình bày bằng chứng Mục 3.3 Kịch bản 2 (X7C0) đã được hoàn thiện với độ chính xác và tính kỷ luật học thuật cao nhất, đáp ứng trọn vẹn mọi yêu cầu của prompt và các ranh giới thực nghiệm đã khóa.

- **Trạng thái chính thức đề xuất:**
  `X7C0_SCENARIO2_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
