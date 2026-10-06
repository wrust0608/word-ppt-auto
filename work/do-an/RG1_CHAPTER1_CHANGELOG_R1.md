# BÁO CÁO THAY ĐỔI VÀ HIỆU CHỈNH CHƯƠNG 1 (RG1_CHAPTER1_CHANGELOG_R1)
## BẢN TỔNG HỢP GIAI ĐOẠN RG1 R1 VÀ HIỆU CHỈNH RANH GIỚI RG1 R2

- **Giai đoạn thực hiện:** RG1 R2 — Hiệu chỉnh giới hạn kỹ thuật và chuẩn hóa nguồn học thuật sau Independent External Review R1.
- **Tệp sửa đổi:** `work/do-an/CHAPTER_1.md`
- **Nhánh:** `feature/rg1-ch1-argument-realignment`
- **Thời gian lập:** 06/10/2026

---

## 1. Tổng quan các nhóm vấn đề đã được khắc phục triệt để trong R2

Căn cứ báo cáo đánh giá độc lập bên ngoài `RG1_CHAPTER1_EXTERNAL_REVIEW_R1.md` (Điểm đánh giá R1: 84/100 – REVISE_BLOCKING), toàn bộ 9 nhóm vấn đề chặn (Blockers A–I) và 4 lưu ý biên tập đã được xử lý hoàn tất trong vòng R2:

| Nhóm vấn đề | Phạm vi phản ánh từ Reviewer | Giải pháp kỹ thuật và biên tập thực hiện trong R2 | Trạng thái |
| :--- | :--- | :--- | :---: |
| **Blocker A** | Bảng Source Audit R1 gán sai Source ID (suy đoán theo số trích dẫn) | Tái thiết lập toàn diện `RG1_CHAPTER1_SOURCE_AUDIT_R1.md` trực tiếp từ `SOURCE_LEDGER.md`. 100% (21/21) trích dẫn đều map chính xác vào các nguồn `VERIFIED`. Không dùng nguồn `RECHECK` hay nguồn giả định. | **ĐÃ GIẢI QUYẾT** |
| **Blocker B** | Thuật ngữ "ngưỡng an toàn" phóng đại hướng dẫn kiểm tra của Microsoft | Loại bỏ 100% cụm từ "ngưỡng an toàn". Đổi thành chuẩn mực: **"phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010"** ($\geq 6.3.9600.18604$). Ranh giới `UNPATCHED` chỉ giới hạn trong phạm vi MS17-010, không chứng nhận an toàn toàn hệ thống. | **ĐÃ GIẢI QUYẾT** |
| **Blocker C** | Diễn giải mã phản hồi Nmap NSE gán nguyên nhân nội bộ không có nguồn | Bỏ diễn giải "driver đã bổ sung cơ chế kiểm soát tham số". Giữ nguyên ánh xạ mã nguồn Nmap: `0xC0000205` $\rightarrow$ tín hiệu chưa vá; `0xC0000022`/`0xC0000008` $\rightarrow$ kịch bản ghi nhận "likely patched" và trả "This system is patched". Bổ sung ranh giới: kịch bản là detector MS17-010/CVE-2017-0143, không tự chứng minh khả năng khai thác CVE-2017-0144/EternalBlue. | **ĐÃ GIẢI QUYẾT** |
| **Blocker D** | Lý thuyết UNKNOWN vô tình gán nguyên nhân cho kết quả NSE04 lab | Phân biệt rõ: lý thuyết nêu các vị trí gián đoạn luồng có thể xảy ra; thực nghiệm ghi nhận nguyên trạng kết quả kịch bản không xuất dữ liệu khả dụng mà không gán nguyên nhân giả định. Giữ vững: `UNKNOWN != SAFE`. | **ĐÃ GIẢI QUYẾT** |
| **Blocker E** | Ngôn ngữ vô hiệu hóa SMBv1 quá tuyệt đối, mâu thuẫn Case B lab | Loại bỏ các từ "triệt tiêu hoàn toàn", "đóng kín bề mặt", "mọi gói tin". Phân biệt rõ: tắt cấu hình dịch vụ máy chủ (`EnableSMB1Protocol=$false`) khác với gỡ gói tính năng (`FS-SMB1 uninstalled`). Giữ vững: `SMBv1 disabled != FS-SMB1 uninstalled` và `SMBv1 disabled != PATCHED`. | **ĐÃ GIẢI QUYẾT** |
| **Blocker F** | Ngôn ngữ về cập nhật bản vá quá tuyệt đối hóa ("hoàn toàn miễn nhiễm") | Thay bằng: Gói cập nhật Microsoft xử lý các lỗ hổng thuộc phạm vi MS17-010. Đạt tiêu chí kiểm tra của Microsoft được phân loại là đã cập nhật đối với MS17-010, không cấu thành chứng nhận an toàn tuyệt đối toàn hệ thống. | **ĐÃ GIẢI QUYẾT** |
| **Blocker G** | Đoạn tác động Tính sẵn sàng (Availability) chứa xếp hạng xác suất vô căn cứ | Loại bỏ cụm từ "nguy cơ thường trực và có xác suất xảy ra cao nhất". Chỉ nêu: sự cố hỏng bộ nhớ nhân có thể gây BSOD/gián đoạn hoạt động, nên tính sẵn sàng là tác động an ninh cần xem xét. Không gán xác suất khi không có dữ liệu định lượng. | **ĐÃ GIẢI QUYẾT** |
| **Blocker H** | Lý thuyết Case C để lộ kết quả đo Chương 3 và khái quát sai về subnet | Bỏ cụm "chuyển từ open sang filtered", bỏ "không cần reboot", bỏ "cùng subnet không bảo vệ được". Nêu đúng bản chất: Tường lửa Transparent Bridge kiểm soát lưu lượng đi qua đường truyền; kết quả đo cụ thể trình bày ở Chương 3. `FILTERED != PATCHED`. | **ĐÃ GIẢI QUYẾT** |
| **Blocker I** | Đoạn Tái kiểm thử (Retest) tuyên bố duy trì toàn bộ nghiệp vụ ngoài phạm vi lab | Phân biệt khuyến nghị vận hành thực tế (nên kiểm tra tương thích ứng dụng) với phạm vi thực nghiệm đề tài (chỉ đo đạc lại các chỉ số/dialect/NSE đã khóa). Quan sát thấy SMB2/3 còn lại không đồng nghĩa chứng minh mọi tải công việc nghiệp vụ không gián đoạn. | **ĐÃ GIẢI QUYẾT** |
| **Lưu ý 13.1** | Diễn giải "SYSTEM thuộc không gian người dùng" | Viết lại chính xác: `SYSTEM` / `LocalSystem` là ngữ cảnh bảo mật và tài khoản người dùng có đặc quyền cao trong Windows; việc quan sát một tiến trình chạy với quyền SYSTEM không tự chứng minh mã đang thực thi trực tiếp ở chế độ nhân (Kernel Mode). | **ĐÃ GIẢI QUYẾT** |
| **Lưu ý 13.2** | Lý do chọn Windows Server 2012 R2 có từ ngữ thị trường thiếu nguồn ("phổ biến") | Loại bỏ các từ "phổ biến", "sát thực tế hạ tầng". Dẫn chứng 3 căn cứ có bằng chứng: (1) đối tượng thực nghiệm thực tế và thuộc phạm vi MS17-010; (2) Microsoft có tài liệu kiểm tra bản vá chính thức Article 4023262; (3) hỗ trợ đồng thời SMBv1 và SMB2/3 để phân tách độc lập các trục bằng chứng. | **ĐÃ GIẢI QUYẾT** |
| **Lưu ý 13.3** | Cụm từ "phản hồi chứng minh an toàn (negative result)" | Thay bằng: "kết quả âm tính theo tiêu chí của phép đo". Không coi kết quả âm tính của máy quét là chứng chỉ an toàn. | **ĐÃ GIẢI QUYẾT** |
| **Lưu ý 15** | Nguồn và số liệu thiệt hại của WannaCry / NotPetya | WannaCry dẫn chứng báo cáo Microsoft Threat Intelligence S015 [16]. NotPetya dẫn chứng báo cáo Microsoft Threat Intelligence S012 [13]. Loại bỏ số liệu tiền tệ quy đổi không có trong nguồn. Không dùng CISA S014 vì đang ở trạng thái RECHECK. | **ĐÃ GIẢI QUYẾT** |

---

## 2. Bảng kiểm tra và rà soát các từ khóa di sản và từ khóa nhạy cảm

Toàn bộ 14 từ khóa được yêu cầu kiểm toán trong RG1 R2 đã được quét tự động trên toàn văn bản `CHAPTER_1.md`:

| STT | Từ khóa kiểm tra | Số lượt xuất hiện trong văn xuôi | Số lượt trong URL thư mục | Phân loại và Đánh giá |
| :---: | :--- | :---: | :---: | :--- |
| 1 | `ngưỡng an toàn` | **0** | 0 | Đã thay bằng "phiên bản tệp `srv.sys` tối thiểu đã cập nhật đối với MS17-010". |
| 2 | `hoàn toàn miễn nhiễm` | **0** | 0 | Đã loại bỏ triệt để. |
| 3 | `triệt tiêu hoàn toàn` | **0** | 0 | Đã thay bằng cách diễn đạt giảm thiểu bề mặt tiếp xúc đo đạc. |
| 4 | `đóng kín bề mặt` | **0** | 0 | Đã loại bỏ triệt để (kể cả tại dòng 39). |
| 5 | `mọi gói tin` | **0** | 0 | Đã loại bỏ các câu khẳng định tuyệt đối hóa. |
| 6 | `xác suất xảy ra cao nhất` | **0** | 0 | Đã loại bỏ khỏi tiểu mục 1.2.5. |
| 7 | `phản hồi chứng minh an toàn` | **0** | 0 | Đã thay bằng "kết quả âm tính theo tiêu chí của phép đo". |
| 8 | `thuộc không gian người dùng` | **0** | 0 | Đã sửa thành ngữ cảnh bảo mật và tài khoản người dùng có đặc quyền cao. |
| 9 | `Client nghiệp vụ` | **0** | 0 | Không tồn tại trong văn bản. |
| 10 | `ba VLAN` | **0** | 0 | Không tồn tại trong văn bản. |
| 11 | `phân vùng khác` | **0** | 0 | Không tồn tại trong văn bản. |
| 12 | `Metasploit` | **0** | 0 | Không tồn tại trong văn bản. |
| 13 | `exploit/windows` | **0** | 1 | Chỉ xuất hiện trong chuỗi URL tham chiếu của tài liệu Rapid7 [14] (S013 trong `SOURCE_LEDGER.md`). 0 lượt trong văn xuôi. |
| 14 | `ms17_010_eternalblue` | **0** | 1 | Chỉ xuất hiện trong chuỗi URL tham chiếu của tài liệu Rapid7 [14] (S013 trong `SOURCE_LEDGER.md`). 0 lượt trong văn xuôi. |

*Đánh giá từ khóa "khai thác":* Toàn bộ 10 lượt xuất hiện của từ "khai thác" trong `CHAPTER_1.md` đã được rà soát thủ công. Tất cả đều nằm trong ngữ cảnh giải thích cơ chế lý thuyết FEA/Pool Grooming theo tài liệu Rapid7, tên tiêu đề chuẩn, hoặc các câu thiết lập ranh giới khẳng định đồ án không thực hiện hành vi khai thác xâm nhập. Không có bất kỳ câu nào khẳng định đồ án đã thực nghiệm khai thác.

---

## 3. Thống kê số lượng từ và cấu trúc tiêu đề

### 3.1. Thống kê từ (Word Count)
- **Trước chỉnh lý (Manager HEAD 5b5b5104):** 8.174 từ (341 dòng).
- **Sau chỉnh lý R1 (4cff2be):** 9.327 từ (369 dòng).
- **Sau hiệu chỉnh R2 (Hiện tại):** 9.385 từ tổng thể gồm bảng biểu và mã kỹ thuật (370 dòng). Khối lượng văn xuôi thuần túy đạt xấp xỉ 7.850 từ, hoàn toàn nằm trong dải mục tiêu chuẩn (7.000 – 8.500 từ).

### 3.2. Cấu trúc tiêu đề (Headings)
Giữ nguyên chính xác **26 tiêu đề**, bảo đảm không phá vỡ kiến trúc tổng thể của Chương 1:
- 1 tiêu đề H1 (Tên chương)
- 4 tiêu đề H2 (Các mục chính 1.1 đến 1.4)
- 19 tiêu đề H3 (Các tiểu mục kỹ thuật)
- 2 tiêu đề H2 kết thúc (TỔNG KẾT CHƯƠNG 1 và TÀI LIỆU THAM KHẢO)

---

## 4. Tổng kết kiểm toán danh mục trích dẫn

Danh mục tài liệu tham khảo gồm **21 tài liệu chuẩn mực IEEE**, được đánh số tuần tự [1] đến [21]. Tất cả đều ánh xạ trực tiếp và chính xác vào 21 nguồn `VERIFIED` trong `SOURCE_LEDGER.md`. Không có trích dẫn mồ côi, không có nguồn `RECHECK` được sử dụng, và không có nguồn giả định.
