# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.2 SCENARIO 1 R2 (CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7B0_SCENARIO1_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B0 R2 — Correct Scenario 1 Evidence/Presentation Plan`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan của phiên bản R2 sau khi tiếp thu đầy đủ các yêu cầu trong báo cáo đánh giá ngoài `X7B0_SCENARIO1_PLAN_EXTERNAL_REVIEW_R1.md`. Tác giả tuyệt đối **không tự ý công bố PASS**; trạng thái nghiệm thu chỉ được quyết định sau thẩm định ngoài lần cuối và sự phê duyệt của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp R2 (Summary Metrics)

| Chỉ số kiểm tra (Audit Metric) | Số lượng thực tế | Ghi chú chi tiết |
|---|:---:|---|
| **Tổng số tệp bằng chứng Kịch bản 1 đã thẩm tra** | **19** | Thẩm tra 100% tệp trong `work/do-an/chapter3/evidence/scenario1/` (15 tệp thô + 1 manifest + 3 ảnh PNG) |
| **Số lượng bộ ba tệp thô máy đọc (Raw triplets) B2–B6** | **5** | Đầy đủ 5 bộ ba (`.nmap`, `.xml`, `.gnmap`): B2 host discovery, B3 target alive, B4 SMB ports, B5 SMB version, B6 SMB NSE |
| **Số lượng ảnh chụp màn hình gốc đã thẩm tra** | **3** | `Scenario1_B4_SMB_Ports.png`, `Scenario1_B5_SMB_Version.png`, `Scenario1_B6_SMB_NSE_A.png` |
| **Số lượng ảnh phân loại KEEP (Giữ lại)** | **2** | `Scenario1_B5_SMB_Version.png` (Hình 3.4 tạm), `Scenario1_B6_SMB_NSE_A.png` (Hình 3.5 tạm) |
| **Số lượng ảnh phân loại OPTIONAL (Dự phòng)** | **0** | (Có phương án thay thế rút gọn: B5 chuyển OPTIONAL, B6 là hình duy nhất) |
| **Số lượng ảnh phân loại DROP (Loại bỏ)** | **1** | `Scenario1_B4_SMB_Ports.png` (Dữ liệu cổng ngắn, tích hợp hoàn toàn vào Bảng 3.3) |
| **Số lượng tiểu mục H3 đề xuất cho Mục 3.2** | **2** | `3.2.1` (Khảo sát trạm mạng & cổng SMB) và `3.2.2` (Phiên bản dịch vụ & đặc tính giao thức SMB) |
| **Số lượng bảng biểu đề xuất cho Mục 3.2** | **1** | `Bảng 3.3` (Trình tự và kết quả khảo sát dịch vụ SMB từ trạm Kali Linux) |
| **Số lượng hình ảnh đề xuất cho Mục 3.2** | **2** | `Hình 3.4` (Thăm dò phiên bản dịch vụ) và `Hình 3.5` (Phân tích đặc tính giao thức SMB) |
| **Số lượng hàng luận điểm ánh xạ (Claim-Map Rows)** | **13** | 13 claims (`S1-C01` đến `S1-C13`), 100% đạt trạng thái `VERIFIED` |
| **Số lần xuất hiện cờ bị thêm sai `-Pn` trong 4 artifact X7B0** | **0** | Đã loại bỏ 100% cờ `-Pn` trong cả 4 tệp kế hoạch R2 |
| **Số lần xuất hiện địa chỉ MAC sai `08:00:27:1B:32:04`** | **0** | Đã loại bỏ hoàn toàn; giá trị gốc trong bằng chứng trực tiếp là `08:00:27:55:71:CE` |
| **Độ trễ chi tiết B3 (`0,00034 s`) trong thiết kế bảng sinh viên** | **Đã loại bỏ** | Bảng 3.3 công khai chỉ ghi nhận trạng thái trực tuyến (`up`), không đưa độ trễ |
| **Số lượng tuyên bố quá đà về OS chính xác tại B5** | **0** | Giữ chặt khoảng nhận diện `Microsoft Windows Server 2008 R2–2012` |
| **Định danh thực thể `.56.100`** | **UNKNOWN** | Duy trì nghiêm ngặt nhãn `UNKNOWN identity`, không gán DHCP/router ảo |
| **Số lượng phán quyết lỗ hổng MS17-010 tại Kịch bản 1** | **0** | Tuyệt đối không đưa ra phán quyết MS17-010 trong Kịch bản 1 |
| **Số lượng byte bằng chứng gốc bị thay đổi** | **0** | 100% bằng chứng gốc được bảo tồn nguyên vẹn |
| **Số lượng tệp văn xuôi Mục 3.2 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo trước** | **0** | Không tạo ảnh phái sinh trước khi kế hoạch được phê duyệt |
| **Số lượng vi phạm cách ly bằng chứng (Scenario 2 / Case B / Case C)** | **0** | 100% cách ly, không rò rỉ bất kỳ dữ liệu từ các kịch bản sau |

---

## 2. Thẩm Tra Việc Loại Bỏ Cờ Bị Thêm Sai `-Pn` (-Pn Parameter Audit)

- **Vấn đề tại bản R1:** R1 đã vô tình đưa cờ `-Pn` vào mô tả lệnh B4, B5, B6 trong bảng đánh giá ảnh và Bảng 3.3, trái ngược với dòng lệnh thực thi ghi nhận trong `Scenario1_Run_Manifest.txt`, các tệp thô `.nmap` và bảng phương pháp của Chương 2.
- **Xử lý triệt để tại bản R2:**
  * Toàn bộ 4 tệp kế hoạch X7B0 đã được rà soát và loại bỏ 100% cờ `-Pn`.
  * Các dòng lệnh thực thi chính xác từ bằng chứng gốc được chuẩn hóa:
    - B4: `sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports`
    - B5: `sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version`
    - B6: `sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse`
  * Trong Bảng 3.3 của báo cáo sinh viên, thay thế các đoạn lệnh bằng các **nhãn phương pháp súc tích** (*Khám phá trạm mạng bằng ARP*, *Xác nhận mục tiêu trực tuyến bằng ARP*, *Quét cổng TCP SYN*, *Thăm dò dịch vụ và phiên bản hệ điều hành từ xa qua Nmap*, *Đánh giá giao thức SMB bằng tập kịch bản Nmap NSE*), loại bỏ nguy cơ lệch pha dòng lệnh với Chương 2.
  * **Kết quả tìm kiếm `-Pn` trong 4 artifact X7B0:** **0 kết quả**.

---

## 3. Thẩm Tra Địa Chỉ MAC B4 (B4 MAC Address Audit)

- **Vấn đề tại bản R1:** R1 ghi nhận nhầm giá trị MAC tại bước B4 thành `08:00:27:1B:32:04`.
- **Đối chiếu thực tế:** Tệp thô `b4_smb_ports.nmap` và ảnh chụp màn hình `Scenario1_B4_SMB_Ports.png` đều ghi nhận địa chỉ MAC thực tế là `08:00:27:55:71:CE`.
- **Xử lý triệt để tại bản R2:**
  * Đã loại bỏ hoàn toàn giá trị sai `08:00:27:1B:32:04`.
  * Trong mô tả tệp tại bảng chọn ảnh, đã ghi nhận chuẩn xác `08:00:27:55:71:CE`.
  * Trong thiết kế Bảng 3.3 công khai, lược bỏ hoàn toàn trường MAC vì không đóng góp vào câu hỏi trọng tâm của người đọc Mục 3.2.
  * **Kết quả tìm kiếm `08:00:27:1B:32:04`:** **0 kết quả**.

---

## 4. Thẩm Tra Thiết Kế Bảng 3.3 Theo Hướng Kết Quả (Result-Oriented Table Audit)

- **Điều chỉnh cấu trúc cột:**
  * Chuyển đổi từ `Bước khảo sát | Kỹ thuật / Công cụ | Kết quả ghi nhận chính | Ý nghĩa kỹ thuật / Giới hạn quan sát` sang:
    `Bước khảo sát | Phép đo | Kết quả ghi nhận | Diễn giải trực tiếp / giới hạn`
  * Thay thế toàn bộ đoạn mã lệnh shell dài dòng bằng tên phép đo khoa học, súc tích.
- **Xử lý bước B3:**
  * Lược bỏ chỉ số độ trễ `0,00034 s` khỏi ô kết quả hiển thị cho sinh viên.
  * Ô kết quả của B3 được chuẩn hóa thành: `Máy chủ 192.168.56.20 được ghi nhận ở trạng thái trực tuyến (up)`.

---

## 5. Thẩm Tra Ranh Giới Dấu Vết Phiên Bản B5 (B5 Fingerprint Boundary Audit)

- **Hiện trạng:** Nmap trên cổng 445 trả về chuỗi nhận diện `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`.
- **Ranh giới kiểm tra R2:**
  * Kế hoạch trình bày xác định đây là **khoảng nhận diện dấu vết (fingerprint range)** của Nmap (`Microsoft Windows Server 2008 R2–2012`).
  * Thay thế các thuật ngữ cơ chế không cần thiết (`probe/banner`) bằng cụm từ chuẩn mực: `kết quả nhận diện dịch vụ/phiên bản của Nmap`.
  * Tuyệt đối không tuyên bố B5 định danh chính xác máy chủ là Windows Server 2012 R2.
  * Khẳng định rõ rằng phiên bản Windows Server 2012 R2 chỉ được xác lập từ kiểm toán cục bộ tại mốc xuất phát Mục 3.1, không phải do Nmap khám phá từ xa ở B5.
  * **Số lượng tuyên bố quá đà về phiên bản tại B5:** **0**.

---

## 6. Thẩm Tra Đặc Tính Giao Thức SMB B6 (B6 Signing, Dialect & Capability Audit)

- **Hiện trạng:** Nmap NSE thực thi 4 kịch bản trên cổng 139/445.
- **Ranh giới kiểm tra R2:**
  * **Phương ngữ:** Sử dụng lối hành văn khách quan, trực tiếp: *"Kịch bản smb-protocols của Nmap ghi nhận 5 phương ngữ..."*: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`.
  * **Ký số:** Ghi nhận chính xác chuỗi kết quả `Message signing enabled but not required`.
  * **Khả năng kỹ thuật:** Bám sát chính xác các tính năng ghi nhận trong output: Distributed File System (trên 2.0.2); DFS, Leasing, Multi-credit operations (trên 2.1, 3.0, 3.0.2). Không tự ý mở rộng hay suy diễn ý nghĩa các cờ tính năng vượt quá kết quả quét.
  * **smb-os-discovery:** Ghi nhận trung thực hiện tượng: **không có đầu ra khả dụng (`no usable output`)**, không suy đoán nguyên nhân lỗi hay coi đây là dấu hiệu an toàn.
  * **Số lượng sai lệch tham số B6:** **0**.

---

## 7. Thẩm Tra Ngăn Ngừa Tuyên Bố Lỗ Hổng MS17-010 (MS17-010 Overclaim Audit)

- **Hiện trạng:** Kịch bản 1 là kịch bản khảo sát bề mặt dịch vụ SMB thông thường (Service & Protocol Discovery), chưa thực thi kịch bản kiểm tra lỗ hổng chuyên sâu (`smb-vuln-ms17-010`).
- **Ranh giới kiểm tra R2:**
  * Cổng 445 mở (`OPEN`) và hỗ trợ SMBv1 (`NT LM 0.12`) chỉ chứng minh bề mặt tiếp xúc dịch vụ kế thừa đang tồn tại.
  * Cổng mở và có SMBv1 **hoàn toàn không đồng nghĩa với việc tồn tại lỗ hổng MS17-010** (`445 OPEN != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`).
  * Khóa chặt chẽ ranh giới: Kịch bản 1 không đưa ra bất kỳ phán quyết nào về lỗ hổng MS17-010; việc kiểm định lỗ hổng được chuyển tiếp trọn vẹn sang Kịch bản 2 (Mục 3.3).
  * **Số lượng nhận định quá đà về lỗ hổng MS17-010:** **0**.

---

## 8. Thẩm Tra Khung Cắt Cúp Có Thể Tái Lập (Reproducible Crop Rectangles Audit)

Trong pha X7B0 R2, đã bổ sung tọa độ nguồn `(x, y, width, height)` dự kiến cho hai ảnh KEEP mà không tạo ảnh phái sinh thật:
1. **Hình 3.4 (từ `Scenario1_B5_SMB_Version.png` $1280 \times 800\,\text{px}$):**
   - Khung cắt cúp: `x = 0, y = 24, width = 1280, height = 310` (vùng `[0, 24, 1280, 334]`).
   - Giữ nguyên toàn bộ câu lệnh, bảng cổng/phiên bản, dòng MAC, dòng Service Info và dấu nhắc kết thúc.
   - Loại bỏ panel trên ($y < 24$) và 466px khoảng trống terminal phía dưới.
2. **Hình 3.5 (từ `Scenario1_B6_SMB_NSE_A.png` $1280 \times 800\,\text{px}$):**
   - Khung cắt cúp: `x = 0, y = 24, width = 1280, height = 710` (vùng `[0, 24, 1280, 734]`).
   - Giữ nguyên toàn bộ khối lệnh NSE và cây kết quả 3 script.
   - Loại bỏ panel trên ($y < 24$) và khoảng trống chân terminal ($y > 734$).

---

## 9. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- **Phạm vi dữ liệu:** Chỉ sử dụng duy nhất các tệp bằng chứng thuộc thư mục `work/do-an/chapter3/evidence/scenario1/`.
- **Cách ly với các phân đoạn khác:**
  * Tuyệt đối không sử dụng bất kỳ tệp dữ liệu nào từ `scenario2/`, `case_b/` hoặc `case_c/`.
  * Không đưa ra bất kỳ kết luận hay nhận định thuộc phạm vi Chương 4.
  * **Số lượng vi phạm cách ly dữ liệu:** **0**.

---

## 10. Danh Mục Báo Cáo Rà Soát Theo Yêu Cầu R2 (Mandatory Reporting Items)

Theo đúng quy định tại Mục 9 của prompt X7B0 R2, báo cáo tự đánh giá ghi nhận xác nhận rõ ràng:
- `-Pn` final search count = 0 (trong toàn bộ mô tả phương pháp và bảng biểu kế hoạch);
- wrong B4 MAC final search count = 0;
- B3 latency removed from public table design;
- B5 exact-OS overclaim count = 0;
- .56.100 identity remains UNKNOWN;
- MS17-010 verdict count = 0;
- no evidence bytes changed;
- no Section 3.2 prose created.

---

## 11. Trạng Thái Kết Thúc Của Executor

Bốn tài liệu kế hoạch X7B0 đã được sửa đổi và chuẩn hóa hoàn tất:
1. `CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`
2. `CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`
3. `CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
4. `CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1.md`

**Trạng thái chính thức:**  
`X7B0_SCENARIO1_PLAN_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`
