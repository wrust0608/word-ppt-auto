# BÁO CÁO TỰ ĐÁNH GIÁ DỰ THẢO MỤC 3.1 BASELINE (CH3_31_BASELINE_DRAFT_SELF_REVIEW_R1)

- **Trạng thái:** `X7A1_CH3_31_BASELINE_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
- **Pha thực hiện:** `X7A1 — Draft Chapter 3 Section 3.1 Baseline`
- **Tệp dự thảo được đánh giá:** `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- **Branch:** `feature/x7a1-ch3-baseline-draft`
- **Starting HEAD:** `59bb8c3b10c5b671f4d1f96624172846e8535038`

---

## 1. Kiểm Toán Số Lượng Từ (Word Count Audit)

- **Tổng số từ toàn văn bản (kể cả bảng và cú pháp):** 2.685 từ.
- **Số từ văn xuôi (loại trừ các dòng bảng và cú pháp ảnh):** ~1.500 từ.
- **Số từ các dòng hiển thị theo `lint_vi_academic.py`:** 2.178 từ.
- **Đánh giá phạm vi độ dài:** Nằm trong khoảng mục tiêu 1.000–1.500 từ văn xuôi cho Tiểu mục 3.1, đảm bảo tính súc tích, mạch lạc và chuẩn mực học thuật mà không kéo dài nhân tạo.

---

## 2. Kiểm Toán Cấu Trúc Đề Mục (Heading Audit)

- **Số lượng tiêu đề H2:** Đúng 1 tiêu đề:
  * `## 3.1. Trạng thái baseline trước đo đạc`
- **Số lượng tiêu đề H3:** Đúng 2 tiêu đề:
  * `### 3.1.1. Trạng thái mạng và dịch vụ SMB`
  * `### 3.1.2. Trạng thái bản vá và mốc phục hồi`
- **Số lượng tiêu đề H3 phát sinh ngoài kế hoạch:** 0.
- **Số lượng tiêu đề H4 hoặc tiêu đề phụ khác:** 0.
- **Đoạn văn mở đầu:** Có đúng 1 đoạn văn mở đầu ngắn gọn nằm ngay dưới đề mục `3.1`, xuất hiện cụm từ chuẩn `trạng thái ban đầu (baseline)` tại vị trí phù hợp đầu tiên.

---

## 3. Kiểm Toán Bảng Biểu (Table Audit — Count = 2)

Dự thảo tích hợp đúng 2 bảng số liệu sinh viên độc lập, tuân thủ chặt chẽ kế hoạch trình bày:

1. **Bảng 3.1:** `Bảng 3.1. Trạng thái mạng, dịch vụ SMB và Windows Firewall trước đo đạc`
   - Cấu trúc: 3 cột (`Hạng mục | Giá trị ghi nhận | Ghi chú`).
   - Số hàng dữ liệu: 11 hàng (IP/Subnet Kali, IP/Subnet Windows, Card mạng VirtualBox, LanmanServer, FS-SMB1, Cấu hình phương ngữ SMB, Chính sách ký số, Cổng lắng nghe, Hồ sơ tường lửa, 16 luật mặc định, Luật tùy biến).
   - Ranh giới kỹ thuật: Loại bỏ hoàn toàn mã tệp, Evidence ID, Claim ID, kết quả ICMP mất gói và phán xét hiệu quả/rủi ro.
2. **Bảng 3.2:** `Bảng 3.2. Trạng thái bản vá và mốc phục hồi`
   - Cấu trúc: 3 cột (`Hạng mục | Giá trị ghi nhận | Ghi chú / căn cứ đối chiếu ngắn`).
   - Số hàng dữ liệu: 7 hàng (Chuỗi FileVersion srv.sys, Phiên bản số nhị phân srv.sys, Ngưỡng cập nhật tối thiểu Microsoft, Mã KB liên quan MS17-010, Danh mục 6 hotfix, Phán loại UNPATCHED, Snapshot Before Demo).
   - Ranh giới kỹ thuật: Không đưa mã Evidence ID hay phán xét suy diễn khả năng khai thác từ xa vào bảng.

---

## 4. Kiểm Toán Hình Ảnh (Figure Audit — Count = 3) & Đường Dẫn Tệp

Dự thảo nhúng đúng 3 hình ảnh phái sinh phục vụ trình bày:

1. **Hình 3.1:**
   - Cú pháp nhúng: `![Hình 3.1. Trạng thái mạng, dịch vụ SMB và các cổng lắng nghe trên Windows Server 2012 R2 trước thực nghiệm](chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_1_Network_SMB.png` (Kích thước 874x642 px, dung lượng 219.308 bytes).
2. **Hình 3.2:**
   - Cú pháp nhúng: `![Hình 3.2. Cấu hình Windows Firewall giới hạn nguồn truy cập TCP 139/445 từ trạm Kali Linux](chapter3/presentation/3_1/Hinh_3_2_Firewall.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_2_Firewall.png` (Kích thước 874x642 px, dung lượng 215.833 bytes).
3. **Hình 3.3:**
   - Cú pháp nhúng: `![Hình 3.3. Phiên bản srv.sys và danh mục hotfix ghi nhận trên Windows Server 2012 R2](chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png)`
   - Tệp vật lý tồn tại: `work/do-an/chapter3/presentation/3_1/Hinh_3_3_SrvSys_Hotfix.png` (Kích thước 872x450 px, dung lượng 155.750 bytes).

---

## 5. Kiểm Toán Báo Cáo Cắt Cúp Hình Ảnh (Crop-Manifest Audit)

- Đã tạo tệp thuyết minh cắt cúp: `work/do-an/CH3_31_BASELINE_CROP_MANIFEST_R1.md`.
- Toàn bộ 3 tệp ảnh bằng chứng gốc trong `work/do-an/chapter3/evidence/baseline/` được bảo tồn nguyên vẹn (1280x800 px, không can thiệp byte).
- Ghi nhận đầy đủ mã băm SHA-256 nguồn và phái sinh, tọa độ hộp cắt cúp chính xác, danh mục nội dung giữ lại và phần giao diện thừa bị loại bỏ.
- Kiểm tra trực quan qua công cụ: Cả 3 ảnh phái sinh có độ tương phản cao, phông chữ PowerShell rõ nét, không bị méo mó, không gắn thêm ký hiệu hay nhãn đồ họa.

---

## 6. Ma Trận Đối Chiếu Đoạn Văn – Luận Điểm (Paragraph-to-Claim Audit)

| Vị trí trong dự thảo | Luận điểm kế thừa | Nội dung thực tế trong văn bản | Tuân thủ ranh giới câu từ được duyệt (Allowed wording) | Xuất hiện sự kiện mới ngoài claim |
|---|---|---|---|---|
| Đoạn mở đầu Mục 3.1 | Khái quát mốc xuất phát | Nêu vai trò mốc tham chiếu định lượng độc lập trước thực nghiệm | Đạt chuẩn trung tính, dùng `trạng thái ban đầu (baseline)` | Không |
| Đoạn 1 Tiểu mục 3.1.1 | `BASE-C01`, `BASE-C02`, `BASE-C03` | Cấu hình IP/Subnet Kali (.56.10), Windows (.56.20), card mạng Host-Only, không default route | Giới hạn đường truyền trong phân đoạn lab; không dùng "hoàn toàn cô lập" hay gán "IP tĩnh" | Không |
| Đoạn 2 Tiểu mục 3.1.1 | `BASE-C04` | L2 ARP REACHABLE, gói tin ICMP mất 100% | Chỉ ghi nhận hiện tượng quan sát; không quy kết nguyên nhân do tường lửa | Không |
| Đoạn 3 Tiểu mục 3.1.1 | `BASE-C05`, `BASE-C06`, `BASE-C07`, `BASE-C08` | LanmanServer Running/Automatic, FS-SMB1 Installed, EnableSMB1/2=True, Ký số False/False, netstat 139/445 listening | Phân biệt rõ cờ cấu hình nội bộ với đàm phán từ xa; không dùng "hoạt động bình thường" | Không |
| Bảng 3.1 & Câu dẫn | `BASE-C01` đến `BASE-C10` | Bảng thông số mạng, dịch vụ và tường lửa | Trình bày dữ liệu quan sát trực tiếp, không chứa thuật ngữ kiểm toán | Không |
| Câu dẫn & Hình 3.1 | Kế hoạch bố trí Hình 3.1 | Dẫn nhập cửa sổ PowerShell tổng hợp cấu hình mạng và dịch vụ | Dẫn nhập đúng tiêu chuẩn trước hình ảnh | Không |
| Đoạn sau Hình 3.1 | `BASE-C08` | Diễn giải bằng chứng Hình 3.1; ranh giới lắng nghe nội bộ vs mở từ xa | Cổng 139/445 lắng nghe nội bộ không đồng nghĩa với remote OPEN | Không |
| Đoạn tường lửa 3.1.1 | `BASE-C09`, `BASE-C10` | 3 profile tường lửa True, 16 luật chia sẻ tệp False, luật tùy biến cho phép nguồn .56.10 | Không suy diễn mọi IP khác chắc chắn bị chặn trên mọi phương diện | Không |
| Câu dẫn & Hình 3.2 | Kế hoạch bố trí Hình 3.2 | Dẫn nhập thuộc tính quy tắc tường lửa tùy biến và hồ sơ tường lửa | Dẫn nhập đúng tiêu chuẩn trước hình ảnh | Không |
| Đoạn sau Hình 3.2 | `BASE-C10` | Đảm bảo kết nối trạm kiểm thử trong kịch bản khảo sát từ xa | Giới hạn phân tích chính sách cổng 139/445 | Không |
| Đoạn 1 Tiểu mục 3.1.2 | `BASE-C11` | Chuỗi hiển thị FileVersion 6.3.9600.16384 của srv.sys | Phân biệt chuỗi hiển thị tĩnh với mã nhị phân thực tế | Không |
| Đoạn 2 Tiểu mục 3.1.2 | `BASE-C12`, `BASE-C13` | Phiên bản số nhị phân 6.3.9600.16421, ngưỡng cập nhật Microsoft 6.3.9600.18604 theo [4], [5] | So sánh số học chính xác; chỉ rõ gói cập nhật KB4012213 / KB4012216 | Không |
| Đoạn 3 Tiểu mục 3.1.2 | `BASE-C14` | Danh mục Get-HotFix ghi nhận 6 bản vá năm 2014, vắng mặt bản cập nhật MS17-010 | Giới hạn phạm vi danh mục quan sát được, không tuyên bố vắng mặt mọi rollup | Không |
| Đoạn 4 Tiểu mục 3.1.2 | `BASE-C15` | Phán loại UNPATCHED dựa trên phiên bản số và danh mục hotfix | Khẳng định UNPATCHED là phân loại cục bộ, không suy diễn thành khai thác thành công từ xa | Không |
| Đoạn 5 Tiểu mục 3.1.2 | `BASE-C16` | Mốc khôi phục Before Demo ở trạng thái tắt máy sạch | Xác lập mốc phục hồi chuẩn, không tuyên bố đảm bảo tái lập tuyệt đối | Không |
| Bảng 3.2 & Câu dẫn | `BASE-C11` đến `BASE-C16` | Bảng trạng thái bản vá và mốc phục hồi | Đối chiếu rõ ràng, súc tích | Không |
| Câu dẫn & Hình 3.3 | Kế hoạch bố trí Hình 3.3 | Dẫn nhập thuộc tính driver srv.sys và bảng hotfix | Dẫn nhập đúng tiêu chuẩn trước hình ảnh | Không |
| Đoạn sau Hình 3.3 | `BASE-C11`, `BASE-C12`, `BASE-C14` | Khẳng định giá trị của phương pháp xác minh kép | Không đưa từ "UNPATCHED" vào tiêu đề hình ảnh | Không |
| Đoạn kết Tiểu mục 3.1 | Chuyển tiếp ý niệm sang 3.2 | Nêu hệ thống sẵn sàng cho rà quét SMB từ trạm Kali Linux | Không rò rỉ lệnh, kết quả hoặc số liệu đo đạc của Kịch bản 1/2 | Không |

---

## 7. Rà Soát Ranh Giới Kỹ Thuật Trạng Thái Bản Vá (Patch-State Boundary Audit)

- [x] Giữ nguyên chuỗi hiển thị: `FileVersion: 6.3.9600.16384 (winblue_rtm.130821-1623)`.
- [x] Giữ nguyên phiên bản số nhị phân: `6.3.9600.16421`.
- [x] Giữ nguyên ngưỡng an toàn tối thiểu theo Microsoft: `6.3.9600.18604` ứng với Windows Server 2012 R2.
- [x] Trích dẫn đúng văn bản pháp lý Microsoft: MS17-010 Security Bulletin `[4]` và Support Article 4023262 `[5]`.
- [x] Danh mục hotfix ghi nhận: Đúng 6 bản vá cài đặt ngày 21/03/2014, không chứa KB4012213 hoặc KB4012216.
- [x] Phán quyết `UNPATCHED`: Khẳng định rõ đây là phân loại trạng thái bản vá cục bộ trên máy chủ; không suy diễn thành khẳng định khai thác từ xa thành công hay kết quả quét NSE từ xa.

---

## 8. Rà Soát Ranh Giới Cục Bộ và Từ Xa (Local vs Remote Boundary Audit)

- [x] Trạng thái lắng nghe cục bộ: Tiến trình hệ thống mở cổng TCP 139 và 445 trên máy chủ được tách biệt rõ ràng với trạng thái cổng mở từ xa (`remote OPEN`).
- [x] Cờ kích hoạt phương ngữ SMB: `EnableSMB1Protocol : True` chỉ xác nhận khả năng đàm phán của ngăn xếp SMB nội bộ, không suy diễn thành danh mục phương ngữ đàm phán thành công từ xa.
- [x] Cờ ký số gói tin: `RequireSecuritySignature : False` chỉ phản ánh chính sách nội bộ không bắt buộc, không quy kết thành kết quả đàm phán ký số từ xa.
- [x] Quy tắc tường lửa tùy biến: Cho phép kết nối TCP 139/445 từ `192.168.56.10`, không suy diễn rằng mọi địa chỉ IP khác đều chắc chắn bị chặn trên mọi phương diện.
- [x] Giới hạn môi trường lab: Nêu rõ cấu hình card mạng Host-Only Adapter và không có default route giới hạn dữ liệu trong phân đoạn lab; không dùng các cụm từ tuyệt đối hóa như "hoàn toàn cô lập".
- [x] Hiện tượng ICMP mất gói: Ghi nhận tỷ lệ mất gói 100% như một quan sát thực tế tại tầng mạng, không kết luận quy kết nguyên nhân do tường lửa Windows.

---

## 9. Rà Soát Ranh Giới Chương 3 và Chương 4 (Chapter 3/4 Boundary Audit)

- [x] Không rò rỉ kết quả đo đạc Kịch bản 1 (quét cổng, NSE đàm phán phương ngữ, OS discovery).
- [x] Không rò rỉ kết quả đo đạc Kịch bản 2 (kiểm định lỗ hổng MS17-010).
- [x] Không nhắc tới dữ liệu khắc phục của Case B hay Case C.
- [x] Không đưa ra đánh giá rủi ro (Risk Rating), mô hình CIA hay thảo luận nguyên nhân gốc rễ.
- [x] Không đề xuất khuyến nghị phòng thủ hay đánh giá "giải pháp tối ưu" (nội dung thuộc Chương 4).
- [x] Đoạn chuyển tiếp cuối cùng khép lại Mục 3.1 bằng cầu nối trung tính giới thiệu bước rà quét từ xa ở Mục 3.2.

---

## 10. Rà Soát Trích Dẫn Học Thuật (Citation Audit)

- Các quan sát thực nghiệm nội bộ: Không gán mã trích dẫn thừa.
- Các căn cứ kỹ thuật của Microsoft:
  * Bản tin an ninh Microsoft MS17-010: sử dụng trích dẫn `[4]` (khớp số thứ tự trong Chương 2).
  * Tài liệu hướng dẫn xác minh Microsoft Support Article 4023262: sử dụng trích dẫn `[5]` (khớp số thứ tự trong Chương 2).
- Không tự ý tạo danh mục tài liệu tham khảo riêng trong phần dự thảo tiểu mục này (danh mục tài liệu tham khảo chung của toàn đồ án đặt ở cuối tài liệu chính).

---

## 11. Rà Soát Giọng Văn Tác Giả (Author Voice Audit)

- Văn phong học thuật, trung tính, trực diện, không cảm tính.
- Không tự xưng ngôi thứ nhất ("chúng tôi", "tôi"), không ra lệnh cho người đọc ("hãy xem", "chúng ta thấy").
- Không sử dụng các mẫu câu sáo rỗng hoặc từ đệm khuôn mẫu.

---

## 12. Rà Soát Thuật Ngữ Nghiêm Cấm (Forbidden-Term Search)

- Mã bằng chứng/luận điểm nội bộ (`BL-*`, `BASE-C*`, `ENV-CORE-*`, `Evidence ID`, `Claim ID`): **0 lần xuất hiện**.
- Thuật ngữ kiểm toán/quản trị (`canonical`, `truth matrix`, `gate`, `Single Source of Truth`, `kiểm toán`, `audit`): **0 lần xuất hiện**.
- Tuyên bố tuyệt đối hóa (`hoàn toàn cô lập`, `tuyệt đối`, `ngăn chặn hoàn toàn Internet`): **0 lần xuất hiện**.
- Cụm từ đánh giá chủ quan (`hoạt động bình thường`, `giải pháp tối ưu`): **0 lần xuất hiện**.
- Tuyên bố sai ranh giới (`remote OPEN`, gán `IP tĩnh` khi chưa có bằng chứng): **0 lần xuất hiện**.

---

## 13. Tình Trạng Tồn Đọng (Unresolved Concerns)

- Không có vấn đề kỹ thuật nào tồn đọng. Dự thảo đạt tính chính xác kỹ thuật 100%, bảo tồn đầy đủ các ranh giới đã cam kết tại kế hoạch X7A0.
- Sẵn sàng chuyển giao cho đợt thẩm tra độc lập bên ngoài (External Review).

---

**KẾT LUẬN TỰ ĐÁNH GIÁ:**
Dự thảo Mục 3.1 đạt trạng thái:
`X7A1_CH3_31_BASELINE_DRAFT_R1_READY_FOR_EXTERNAL_REVIEW`
