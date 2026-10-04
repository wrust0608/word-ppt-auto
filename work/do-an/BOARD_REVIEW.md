# BOARD REVIEW — Phiếu chấm của hội đồng

Trạng thái: REJECT_ROUND — THEORY_REVIEW_2026_10_05

## Phạm vi chấm
- Bản được chấm: `ATTT_DACN_01_demo.docx` do tác giả cung cấp ngày 2026-10-05.
- Phần đã có nội dung thực chất: Mở đầu + Chương 1.
- Chương 2–4 hiện chủ yếu là khung mục nên **không trừ như thể đây là bản báo cáo cuối**, nhưng file tổng thể chưa thể coi là báo cáo hoàn chỉnh.
- Chuẩn chính: rubric repo + HUIT. Benchmark bên ngoài chỉ dùng hiệu chuẩn kỳ vọng.

## Điểm

| Tiêu chí | Điểm tối đa | Điểm | Nhận xét |
|---|---:|---:|---|
| Chính xác kỹ thuật và đúng phạm vi | 30 | 23 | Phần MS17-010 và ranh giới suy luận khá tốt; còn các phát biểu khái quát quá mức và bảng SMB trộn đặc tính theo nhiều thế hệ Windows/dialect mà chưa giới hạn. |
| Bằng chứng và trích dẫn | 20 | 2 | Gần như không có citation IEEE trong thân bài; trang tài liệu tham khảo chưa có danh mục. Đây là lỗi nghiêm trọng nhất theo chuẩn repo. |
| Chiều sâu phân tích và lập luận | 20 | 16 | Mạch cổng mở → SMBv1 → dấu hiệu → xác minh/tác động là điểm mạnh. Phần đầu chương vẫn thiên về giáo trình/liệt kê và lặp kiến thức. |
| Cấu trúc và văn phong học thuật | 15 | 10 | Bố cục dễ theo dõi nhưng nhiều bullet, lặp nội dung, lỗi đánh số/typo, caption và bảng chưa chuẩn; “nhóm em/em” chưa nhất quán. |
| Khả năng bảo vệ trước hội đồng | 10 | 8 | Có ý thức về giới hạn, False/Unknown và crash ≠ exploit success. Tuy nhiên sẽ khó trả lời “nguồn nào?”, “tại sao chọn 4 mức?”, “đóng góp của nhóm là gì?” nếu giữ bản hiện tại. |
| Liêm chính học thuật | 5 | 5 | Không giả dữ liệu thực nghiệm; nhiều câu đã chủ động hạ mức kết luận và nêu giới hạn. |

**Tổng: 64/100 — REJECT_ROUND**

Lưu ý: nếu chỉ đánh giá chất lượng tư duy/nội dung và tạm bỏ qua lỗi citation, bản lý thuyết nằm khoảng 78–82/100. Điểm chính thức vẫn là 64 vì repo coi khả năng truy vết nguồn là điều kiện cốt lõi, không phải phần trang trí.

## Điểm mạnh cần giữ

1. Phân biệt rõ bốn tầng bằng chứng: khả năng tiếp cận cổng, dialect SMBv1, dấu hiệu MS17-010 và tác động/xác minh sâu.
2. Không suy ra “cổng 445 mở = có MS17-010”.
3. Không suy ra “SMBv1 bật = chưa vá”.
4. Không coi timeout/denied/crash là bằng chứng hệ thống an toàn hoặc RCE thành công.
5. Phần cơ chế CVE-2017-0144 đã đi đúng hướng: cấp phát → ghi vượt biên → mất ổn định/chuyển hướng thực thi là các bước khác nhau.
6. Có nêu giới hạn phép đo từ xa và nhu cầu đối chiếu trạng thái bên trong.
7. Văn phong nhìn chung tiết chế hơn các bản tự chấm cũ, ít tuyệt đối hóa.

## Lỗi bắt buộc sửa — mức P0

### P0-01. Thiếu citation IEEE và bibliography
Toàn bộ claim về:
- kiến trúc SMB;
- thuật toán signing/encryption;
- dialect và Windows version;
- MS17-010/CVE;
- FEA/kernel pool;
- WannaCry/NotPetya;
- hành vi Nmap NSE/NT Status;
- Metasploit;
đều phải truy về nguồn gốc.

Không được “rải citation cho có”. Mỗi citation phải hỗ trợ đúng phạm vi câu.

### P0-02. Bảng SMBv1/v2/v3 đang trộn nhiều thế hệ
Các dòng SMBv3 về AES-GMAC, SMB over QUIC/UDP 443, AES-256, RDMA/Multichannel thuộc các dialect/hệ Windows khác nhau. Nếu gom hết vào cột “SMBv3” mà không ghi điều kiện phiên bản sẽ khiến người đọc hiểu mọi SMBv3 đều có toàn bộ đặc tính đó.

Yêu cầu:
- tách dialect/phiên bản hoặc thêm cột “điều kiện/phiên bản Windows”;
- tuyệt đối không áp đặc tính Windows 11/Server 2022/2025 cho Windows 7 lab;
- phân biệt giao thức hỗ trợ tính năng với kết nối thực tế đang bật tính năng.

### P0-03. Một số phát biểu quá mạnh hoặc chưa chính xác về ngữ nghĩa
Cần rà:
- “SMB là giao thức truyền thông mặc định cho các dịch vụ mạng nội bộ Windows” — quá rộng;
- “SMBv1 ... cho phép kẻ tấn công chiếm quyền điều khiển máy tính” — phải giới hạn theo lỗ hổng/điều kiện, không gộp toàn SMBv1;
- “dữ liệu gửi đi ở dạng văn bản rõ” — nên dùng “không có SMB Encryption tích hợp / không được mã hóa bởi SMB”, vì dữ liệu SMB là nhị phân chứ không phải literal plaintext;
- “445 bị chặn thì tự động fallback 139” — Microsoft mô tả khi cả direct-host và NBT cùng bật, Windows thử hai phương thức và dùng phương thức phản hồi trước; không nên diễn đạt thành quy tắc fallback tuần tự tuyệt đối;
- “cổng 139 phụ thuộc NetBIOS name thay vì DNS” — cần giới hạn theo cấu hình/transport, tránh nói như quy tắc phổ quát.

### P0-04. Hình và bảng chưa đủ chuẩn học thuật
- Hình luồng SMB cần nguồn hoặc ghi rõ “nhóm tự tổng hợp từ ...”.
- Caption phải theo chuẩn HUIT, ví dụ “Hình 1.1 ...”, không chỉ “Hình 1”.
- Bảng SMB cần số bảng, tên bảng, nguồn.
- Nếu tự tổng hợp, phải chỉ ra nguồn dữ liệu của từng nhóm đặc tính.

## Lỗi mức P1 — logic và lập luận

### P1-01. Phần Mở đầu mới thiên về động cơ học tập, chưa xác lập đóng góp
“Nhóm muốn tìm hiểu”, “củng cố kiến thức” phù hợp động cơ sinh viên nhưng chưa đủ cho lập luận học thuật.

Cần trả lời rõ:
- bài toán cụ thể là gì;
- sai lầm/khó khăn nào trong đánh giá SMB mà đồ án muốn xử lý;
- sản phẩm/đóng góp của nhóm là gì;
- tiêu chí nào cho biết mục tiêu đã đạt.

### P1-02. Mục tiêu dùng động từ khó đánh giá
“Tìm hiểu”, “tìm hiểu MS17-010” khó chấm hoàn thành.

Nên chuyển thành đầu ra đo được:
- phân tích cơ chế;
- xây dựng mô hình;
- xác định tiêu chí;
- thu thập/đối chiếu bằng chứng;
- so sánh trước/sau hardening.

### P1-03. Phương pháp nghiên cứu còn chung
“kết hợp tài liệu và thực nghiệm” chưa đủ để tái lập.

Phải nêu tối thiểu:
- loại đánh giá;
- đối tượng;
- biến/trạng thái;
- dữ liệu thu;
- cách đối chiếu;
- tiêu chí thành công/thất bại/Unknown;
- nguyên tắc khôi phục và kiểm soát rủi ro.

### P1-04. Bốn mức xác minh là đóng góp tốt nhưng chưa được “định danh”
Đây là phần mạnh nhất của Chương 1 nhưng chưa nói:
- đây là khung do nhóm đề xuất hay kế thừa;
- vì sao đúng 4 mức;
- mỗi mức trả lời câu hỏi nào;
- bằng chứng nào cho phép chuyển mức;
- có bắt buộc tuần tự hay chỉ là khung phân loại.

Nếu xử lý tốt, đây có thể trở thành một đóng góp phương pháp của đồ án.

### P1-05. Chương 1 còn lặp và thiên về giáo trình
Khái niệm Client–Server, negotiate/session/tree connect, cổng 139/445 được giải thích nhiều lần bằng prose, bullet và sơ đồ.

Cần cắt lặp, giữ kiến thức chỉ khi nó phục vụ:
- một phép kiểm tra ở Chương 2/3;
- một ranh giới suy luận;
- một biện pháp hardening.

### P1-06. Phần công cụ còn giống danh mục sản phẩm
Kali, Nmap, NSE, Metasploit được mô tả hợp lý nhưng chưa đủ lý do chọn.

Cần chuyển trọng tâm từ “công cụ là gì” sang:
- nó đo cái gì;
- quan sát ở đâu;
- output nào là bằng chứng;
- không được suy luận gì từ output đó;
- tại sao công cụ này phù hợp hơn một phép kiểm tra khác.

## Lỗi mức P2 — cấu trúc, trình bày, ngôn ngữ

1. Mở đầu có hai mục số 4: “Phương pháp...” rồi “Nguyên tắc an toàn...”.
2. Dùng lẫn “nhóm em” và “em”.
3. Có typo như “hhệ điều hành”.
4. Nhiều đoạn bullet dài làm tài liệu giống giáo trình/slides hơn luận văn.
5. Một số thuật ngữ dịch nặng: “mã lệnh điều khiển”, “gói tin văn bản rõ”, “kênh giao tiếp an toàn” cần rà theo đúng tầng kỹ thuật.
6. Chương 2 trong file có dòng “2.4.” dang dở; Chương 4 có “Tổng hợp kết quảz”.
7. Trang “TÀI LIỆU THAM KHẢO” chưa có nội dung.
8. Chưa thấy danh mục hình/bảng/viết tắt trong bản demo mặc dù HUIT yêu cầu phần đầu đầy đủ ở bản xuất bản.

## Các câu hội đồng có thể hỏi

1. Tại sao nhóm chia quá trình xác minh thành đúng bốn mức? Đây là tiêu chuẩn nào hay do nhóm đề xuất?
2. Nếu Nmap trả `STATUS_INSUFF_SERVER_RESOURCES`, bằng chứng nào cho phép em nói máy “có khả năng chưa vá”? False positive/negative nằm ở đâu?
3. Nếu SMBv1 đang bật nhưng KB đã cài thì mức 2 và mức 3 khác nhau thế nào?
4. Vì sao crash/BSOD không được coi là bằng chứng exploit thành công?
5. Em chứng minh thế nào rằng lỗ hổng nằm ở cơ chế FEA chứ không phải chỉ lặp lại mô tả của Metasploit?
6. SMBv3 trong bảng của em là dialect nào? Windows 8 có SMB over QUIC không?
7. AES-GMAC áp dụng từ môi trường nào? Có liên quan gì đến Windows 7 mục tiêu của em?
8. Tại sao em chọn Nmap + NSE + Metasploit? Hai scanner cùng dựa vào một NT Status có thực sự là hai bằng chứng độc lập không?
9. Nếu cổng 445 `filtered`, em có quyền kết luận SMB không hoạt động không?
10. Đóng góp của nhóm khác gì so với việc đọc tài liệu Microsoft rồi chạy công cụ có sẵn?
11. Điều gì làm mô hình của em có khả năng tái lập?
12. Kết quả nào sẽ làm em bác bỏ nhận định ban đầu của chính mình?
13. Tại sao em dùng từ “ý nghĩa khoa học” nếu hiện phần lớn Chương 1 là tổng hợp kiến thức có sẵn?
14. Nguồn nào chứng minh từng dòng trong bảng SMB?
15. Khi một probe bị ACCESS_DENIED, em phân biệt “đã vá”, “bị policy chặn” và “không đủ dữ liệu” như thế nào?

## Yêu cầu vòng tiếp theo cho agent

Mục tiêu vòng sau **không phải viết thêm Chương 2**. Phải nâng Mở đầu + Chương 1 lên tối thiểu 80/100 trước.

Thứ tự bắt buộc:
1. Gắn claim-source bằng IEEE từ nguồn gốc đã có trong SOURCE_LEDGER.
2. Sửa/giới hạn các claim kỹ thuật P0-02/P0-03.
3. Chuẩn hóa hình, bảng và nguồn.
4. Viết lại Mở đầu theo “vấn đề → mục tiêu đo được → phương pháp → đóng góp → giới hạn”.
5. Định danh rõ khung bốn mức xác minh và ranh giới suy luận.
6. Cắt lặp Chương 1; mỗi mục phải chỉ ra nó phục vụ phép kiểm tra/phòng thủ nào.
7. Chuyển phần công cụ từ mô tả sản phẩm sang logic đo lường/bằng chứng.
8. Chạy citation audit + style lint.
9. Nộp lại với bảng “claim quan trọng → nguồn → vị trí nguồn → câu sau sửa”.

Agent không được tự nâng PASS và không được dựng DOCX cuối ở vòng này.
