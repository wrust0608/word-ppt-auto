# BÁO CÁO TỰ ĐÁNH GIÁ KẾ HOẠCH BẰNG CHỨNG MỤC 3.2 SCENARIO 1 (CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1)

- **Trạng thái:** `X7B0_SCENARIO1_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7B0 — Scenario 1 Evidence & Presentation Plan Only`
- **Ngày thực hiện:** 2026-10-06
- **Ghi chú chuẩn mực:** Báo cáo này trình bày kết quả tự rà soát kỹ thuật khách quan của kế hoạch bằng chứng và trình bày Kịch bản 1 (Mục 3.2) trước khi chuyển giao cho quy trình đánh giá ngoài độc lập (Independent External Review). Tác giả tuyệt đối **không tự ý công bố PASS**; trạng thái nghiệm thu chỉ được quyết định sau thẩm định ngoài và sự phê duyệt của người dùng.

---

## 1. Bảng Chỉ Số Thống Kê Tổng Hợp (Summary Metrics)

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
| **Số lượng tệp văn xuôi Mục 3.2 bị tạo trước** | **0** | Tuân thủ tuyệt đối quy tắc ZERO PROSE của pha lập kế hoạch |
| **Số lượng ảnh cắt cúp presentation bị tạo trước** | **0** | Tuân thủ quy tắc không tạo ảnh phái sinh trước khi kế hoạch được phê duyệt |
| **Số lượng vi phạm cách ly bằng chứng (Scenario 2 / Case B / Case C)** | **0** | 100% cách ly, không rò rỉ bất kỳ dữ liệu từ các kịch bản sau |

---

## 2. Thẩm Tra Quyết Định Trùng Lặp B2 và B3 (B2/B3 Duplication Audit)

- **Hiện trạng dữ liệu:**
  * Bước B2 (`b2_host_discovery`): Quét ARP dải `192.168.56.0/24`, phát hiện 4 địa chỉ IP trong đó có máy chủ mục tiêu `192.168.56.20`.
  * Bước B3 (`b3_target_alive`): Thăm dò ARP đơn điểm tới `192.168.56.20`, xác nhận máy chủ trực tuyến (độ trễ 0,00034 s).
  * Cả hai bước đều không có ảnh chụp màn hình trong bộ bằng chứng đã stage (chỉ có tệp máy đọc thô).
- **Quyết định học thuật:**
  * **Hợp nhất diễn giải trong văn bản:** Trình bày cả B2 và B3 trong cùng Tiểu mục `3.2.1`. B3 được định vị là bước kiểm tra xác nhận tính liên tục (continuity confirmation) trong quy trình thực nghiệm trước khi tiến hành quét cổng chuyên sâu, không chiếm dung lượng phân tích lớn.
  * **Trình bày dạng bảng:** B2 và B3 xuất hiện như 2 hàng tuần tự trong Bảng 3.3, bảo đảm tính minh bạch về trình tự thực nghiệm của phòng lab.
  * **Không tạo ảnh phái sinh:** Tuyệt đối không tự ý dựng ảnh giả mạo cho B2/B3 từ văn bản thô.

---

## 3. Thẩm Tra Định Danh Thực Thể `192.168.56.100` (.56.100 Identity Audit)

- **Hiện trạng:** Quét ARP bước B2 phát hiện địa chỉ `192.168.56.100` có phản hồi trong phân đoạn mạng.
- **Ranh giới kiểm tra:**
  * Toàn bộ các tài liệu kế hoạch, bảng biểu và ma trận claim map đều giữ nguyên định danh của thực thể này là **`UNKNOWN identity`**.
  * Tuyệt đối không phỏng đoán, không gán định danh DHCP server, router ảo hay bất kỳ vai trò giả định nào cho `.56.100`.
  * Số lượng suy diễn vi phạm định danh `.56.100`: **0**.

---

## 4. Thẩm Tra Ranh Giới Dấu Vết Phiên Bản B5 (B5 Fingerprint Boundary Audit)

- **Hiện trạng:** Nmap `-sV` trên cổng 445 trả về chuỗi nhận diện `Microsoft Windows Server 2008 R2 - 2012 microsoft-ds`.
- **Ranh giới kiểm tra:**
  * Kế hoạch trình bày xác định đây là **khoảng nhận diện dấu vết (fingerprint range)** của Nmap (`Microsoft Windows Server 2008 R2–2012`).
  * Tuyệt đối không tuyên bố B5 định danh chính xác máy chủ là Windows Server 2012 R2.
  * Khẳng định rõ rằng phiên bản Windows Server 2012 R2 chỉ được xác lập từ kiểm toán cục bộ tại mốc xuất phát Mục 3.1, không phải do Nmap khám phá từ xa ở B5.
  * Số lượng tuyên bố quá đà về phiên bản tại B5: **0**.

---

## 5. Thẩm Tra Đặc Tính Giao Thức SMB B6 (B6 Signing, Dialect & Capability Audit)

- **Hiện trạng:** Nmap NSE thực thi 4 kịch bản trên cổng 139/445.
- **Ranh giới kiểm tra:**
  * **Phương ngữ:** Liệt kê chuẩn xác 5 phương ngữ được ghi nhận trong tệp thô: `NT LM 0.12 (SMBv1)`, `2.0.2`, `2.1`, `3.0`, `3.0.2`.
  * **Ký số:** Ghi nhận chính xác chuỗi kết quả `Message signing enabled but not required`.
  * **Khability:** Bám sát chính xác các tính năng ghi nhận trong output: Distributed File System (trên 2.0.2); DFS, Leasing, Multi-credit operations (trên 2.1, 3.0, 3.0.2). Không tự ý bổ sung hoặc suy diễn ý nghĩa các cờ tính năng vượt quá kết quả quét.
  * Số lượng sai lệch tham số B6: **0**.

---

## 6. Thẩm Tra Đầu Ra Hạn Chế Của `smb-os-discovery` (Negative Output Audit)

- **Hiện trạng:** Kịch bản `smb-os-discovery` được cấu hình chạy trong bước B6 nhưng hoàn toàn không xuất hiện kết quả trong khối đầu ra Nmap.
- **Ranh giới kiểm tra:**
  * Báo cáo ghi nhận trung thực hiện tượng: **không có đầu ra khả dụng (`no usable output`)**.
  * Tuyệt đối không bịa đặt nguyên nhân kỹ thuật (không quy kết do tường lửa, do hệ điều hành chặn, do cấu hình NetBIOS hay do kịch bản lỗi).
  * Không coi việc thiếu đầu ra là bằng chứng an toàn hay bằng chứng định danh hệ điều hành.
  * Số lượng suy diễn vi phạm về `smb-os-discovery`: **0**.

---

## 7. Thẩm Tra Ngăn Ngừa Tuyên Bố Lỗ Hổng MS17-010 (MS17-010 Overclaim Audit)

- **Hiện trạng:** Kịch bản 1 là kịch bản khảo sát bề mặt dịch vụ SMB thông thường (Service & Protocol Discovery), chưa thực thi kịch bản kiểm tra lỗ hổng chuyên sâu (`smb-vuln-ms17-010`).
- **Ranh giới kiểm tra:**
  * Cổng 445 mở (`OPEN`) và hỗ trợ SMBv1 (`NT LM 0.12`) chỉ chứng minh bề mặt tiếp xúc dịch vụ kế thừa đang tồn tại.
  * Cổng mở và có SMBv1 **hoàn toàn không đồng nghĩa với việc tồn tại lỗ hổng MS17-010** (`445 OPEN != vulnerable`, `SMBv1 enabled != MS17-010 confirmed`).
  * Khóa chặt chẽ ranh giới: Kịch bản 1 không đưa ra bất kỳ phán quyết nào về lỗ hổng MS17-010; việc kiểm định lỗ hổng được chuyển tiếp trọn vẹn sang Kịch bản 2 (Mục 3.3).
  * Số lượng nhận định quá đà về lỗ hổng MS17-010 trong toàn bộ các tài liệu kế hoạch: **0**.

---

## 8. Thẩm Tra Tính Cách Ly Bằng Chứng (Evidence-Isolation Audit)

- **Phạm vi thẩm tra:** Toàn bộ dữ liệu kế hoạch được xây dựng hoàn toàn độc lập trên bộ bằng chứng Kịch bản 1 (`work/do-an/chapter3/evidence/scenario1/`).
- **Cách ly với các phân đoạn khác:**
  * Không sử dụng bất kỳ tệp dữ liệu nào từ `scenario2/` (Kịch bản 2).
  * Không sử dụng dữ liệu từ `case_b/` (Biện pháp vô hiệu hóa SMBv1) hoặc `case_c/` (Tường lửa pfSense).
  * Chỉ kế thừa các sự thật mốc xuất phát đã được phê duyệt từ Mục 3.1 làm ngữ cảnh liên tục cần thiết (địa chỉ IP Kali, địa chỉ IP Windows, kiểm toán cục bộ).
  * Số lượng vi phạm cách ly dữ liệu: **0**.

---

## 9. Các Điểm Cần Lưu Ý Trong Trình Bày Cho Đánh Giá Ngoài (Presentation Nuances)

1. **Phương án phân bổ hình ảnh (2 hình vs. 1 hình):**
   - Kế hoạch đề xuất phương án chính là 2 hình (Hình 3.4 cho B5 version fingerprint và Hình 3.5 cho B6 NSE protocol profile) nhằm cung cấp trực quan trọn vẹn cả hai tầng nhận diện dịch vụ và giao thức.
   - Kế hoạch cũng đã chuẩn bị phương án rút gọn 1 hình (chỉ giữ B6 làm Hình 3.4, đưa B5 hoàn toàn vào Bảng 3.3) nếu hội đồng phản biện ưu tiên tối đa tính cô đọng của văn bản.
2. **Khả năng đọc trên khổ giấy A4:**
   - Cả hai hình đề xuất (Hình 3.4 và Hình 3.5) đều có định hướng cắt cúp loại bỏ viền desktop Kali thừa để phóng to vùng chữ dòng lệnh, bảo đảm khi dàn trang A4 portrait người đọc xem rõ từng tham số kỹ thuật mà không bị mờ nhòe.
3. **Tính trung lập của văn phong:**
   - Kế hoạch loại bỏ toàn bộ các thuật ngữ kiểm toán nội bộ (`canonical`, `gate`, `governance`, `Single Source of Truth`, `Evidence ID`, `Claim ID`, `layer L1..L5`) khỏi thiết kế bảng biểu và cấu trúc đề mục sinh viên, bảo đảm văn phong khoa học, khách quan, đúng chất một luận văn an toàn thông tin.

---

## 10. Trạng Thái Kết Thúc Của Executor

Kế hoạch bằng chứng và phương án trình bày cho Mục 3.2 Kịch bản 1 đã được xây dựng hoàn chỉnh, nghiêm ngặt và đồng bộ qua 4 tài liệu:
1. `CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`
2. `CH3_32_SCENARIO1_PRESENTATION_PLAN_R1.md`
3. `CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
4. `CH3_32_SCENARIO1_PLAN_SELF_REVIEW_R1.md`

**Trạng thái chính thức:**  
`X7B0_SCENARIO1_PLAN_R1_READY_FOR_EXTERNAL_REVIEW`
