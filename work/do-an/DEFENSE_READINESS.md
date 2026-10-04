# Defense Readiness

- Phạm vi: lớp review **project-local**, chỉ áp dụng cho `work/do-an`.
- Quyết định: DEC-24, người dùng yêu cầu trực tiếp ngày 2026-10-04.
- Trạng thái artifact: `ACTIVE_PROJECT_REVIEW_LAYER`. Không phải trạng thái đạt của chương hoặc của tác giả.

## 1. Mục đích

Defense Readiness kiểm tra người đứng tên đồ án cần hiểu và bảo vệ được phần nào của các luận điểm, diễn giải và quyết định quan trọng. Một phát biểu đúng, có nguồn và được viết rõ vẫn cần được xét về vai trò trong nghiên cứu, giới hạn bằng chứng và phần tác giả phải giải thích khi bảo vệ.

Đây không phải AI detector, không tạo lỗi hoặc làm văn bản “giống người”. Lớp này không thay evidence review, không thay author voice, không tạo dữ liệu, trải nghiệm, quyết định hoặc lý do của tác giả. Author voice xét cách tác giả diễn đạt; Defense Readiness xét nội dung tác giả cần làm chủ. Hai trách nhiệm được giữ riêng.

Thứ tự ưu tiên giữ nguyên: yêu cầu hiện tại → quy định/mẫu chính thức → quyết định đã khóa → nguồn/dữ liệu đã xác minh → quy trình nghiên cứu và lập luận → giọng tác giả → linter. Defense Readiness nằm **bên trong quy trình nghiên cứu và lập luận**; không đứng cao hơn HUIT, quyết định LOCKED, nguồn, dữ liệu hoặc claim boundary. Không tạo G7, G4.5 hoặc đổi cấu trúc G0–G6.

## 2. Thứ tự áp dụng

**Evidence → Logic → Defense Readiness → Trim/Simplify → Academic register / Author Voice → Linter → User approval.**

Evidence review kiểm nguồn, dữ liệu và phạm vi hỗ trợ trước. Logic review kiểm đường suy luận từ bằng chứng tới kết luận. Sau đó Defense Readiness xác định phần cần tác giả giải thích và liệu độ sâu có phục vụ câu hỏi nghiên cứu. Khi thiếu bằng chứng, phải quay lại evidence review; không viết mềm đi để che khoảng trống. Trim/Simplify chỉ tiến hành khi vẫn bảo toàn điều kiện, nguồn và nội dung bắt buộc.

Áp dụng chuỗi này như bước con trong review chương G4, không tạo cổng mới. Tại G5, dùng các thẻ để đối chiếu quyết định xuyên chương, giới hạn kết luận và nhu cầu của chi tiết sâu. Quyền phê duyệt chương/cổng vẫn thuộc người dùng theo trạng thái dự án.

## 3. Phạm vi

Không lập Defense Card cho từng câu. Bắt buộc có thẻ cho luận điểm trung tâm, diễn giải từ bằng chứng, quyết định phương pháp, quyết định thiết kế, kết luận chính, claim chuyển tiếp quan trọng giữa chương và chi tiết sâu có thể bị hỏi “vì sao đồ án cần biết điều này?”.

Định nghĩa nền tảng thông thường chỉ cần chính xác, có căn cứ và cần thiết. Chỉ nâng thành thẻ nếu định nghĩa được dùng làm tiền đề quan trọng hoặc xuất hiện bất đồng về nghĩa/giới hạn.

Mỗi thẻ xác định: claim nói gì; thuộc loại nào; nguồn/dữ liệu hỗ trợ tới đâu; vì sao nội dung cần có; tác giả phải giải thích điều gì; độ sâu cần làm chủ; có gán lý do chưa xác nhận hay không. Dùng các loại mô tả `source fact`, `data/observation`, `interpretation`, `author decision`, `method/design decision`, `conclusion`. Đây là phân loại phục vụ review, không thay hệ loại hoặc trạng thái của CLAIM_MATRIX.

Đặt ID riêng `DR-C1-xx` và liên kết C001–C006/RQ/O khi có. Không tạo quan hệ giả nếu chưa xác định được. Quyết định đã khóa chứng minh phạm vi được duyệt; không tự chứng minh tác giả đã giải thích được quyết định đó.

## 4. Decision Tree

1. **Nội dung bắt buộc theo đề cương/trường?** Giữ; kiểm bằng chứng; nếu quá sâu thì đơn giản hóa ở mức phù hợp mà không bỏ phần bắt buộc. Nếu bằng chứng thiếu, ghi `EVIDENCE_GAP`, không dùng mức dễ hiểu để thay nguồn.
2. **Luận điểm trung tâm?** Phải có thẻ, dù văn bản đang trôi chảy hoặc nguồn đã VERIFIED.
3. **Kiến thức nền cần cho luận điểm sau?** Giữ mức tối thiểu đủ làm tiền đề; không cần thẻ cho mọi định nghĩa.
4. **Chi tiết phụ không phục vụ RQ, mục tiêu, phương pháp hoặc claim chính?** Đánh dấu `REMOVE_CANDIDATE`, nêu căn cứ đề xuất. Không tự xóa, đặc biệt khi quyết định đã LOCKED hoặc nội dung bắt buộc.
5. **Lựa chọn, lý do hoặc quan điểm được gán cho tác giả nhưng chưa có xác nhận?** Ghi `AUTHOR_CONFIRM` và `[CẦN TÁC GIẢ XÁC NHẬN]` tại thẻ/state; không điền lý do thay tác giả. Nếu lựa chọn đã khóa, chỉ xác nhận phần lý do/giải thích còn thiếu, không yêu cầu duyệt lại lựa chọn đã được duyệt.
6. **Claim mạnh hơn evidence?** Ghi `EVIDENCE_GAP`, chỉ rõ bước suy luận vượt nguồn/dữ liệu và tuyến kiểm tra tiếp. Không dùng Defense Readiness để che thiếu nguồn, xóa marker hoặc biến kết quả dự kiến thành kết quả đã đo.

Các nhánh có thể cùng áp dụng. Mỗi thẻ có một trạng thái chính; ưu tiên xử lý khoảng trống evidence, rồi phần author confirmation, sau đó nhu cầu simplify/remove. Ghi các vấn đề còn lại trong Evidence boundary hoặc Author must explain, không tạo trạng thái thứ sáu. Việc tác giả chưa trả lời được không tự dẫn tới xóa nội dung.

## 5. Trạng thái

| Trạng thái | Ý nghĩa và cách xử lý |
|---|---|
| READY | Evidence/logic, tính cần thiết và mức giải thích đã được đối chiếu; có bản giải thích/phản hồi thực của tác giả được truy vết cho phần cần làm chủ. Reviewer ghi căn cứ, người review và ngày. Không tự READY vì câu đúng hoặc quyết định đã khóa; không đồng nghĩa user approval của chương/cổng. |
| SIMPLIFY | Nội dung cần thiết, nhưng mức chi tiết vượt nhu cầu của RQ/phương pháp hoặc làm phần cần giải thích không rõ. Đề xuất mức cần giữ; không mất bằng chứng, giới hạn hoặc yêu cầu trường. Việc sửa chương tuân thủ phạm vi được cho phép. |
| AUTHOR_CONFIRM | Thiếu xác nhận cho lý do/lựa chọn được gán cho tác giả, hoặc chưa có phản hồi thực để xác nhận tác giả giải thích được phần quan trọng. Giữ `[CẦN TÁC GIẢ XÁC NHẬN]`, ghi câu hỏi cụ thể và quyết định nào đã khóa để tránh hỏi duyệt lại. |
| EVIDENCE_GAP | Nguồn/dữ liệu chưa đủ, có mâu thuẫn chưa xử lý hoặc suy luận mạnh hơn phần hỗ trợ. Quay lại evidence/logic review; không viết mềm, tự điền dữ liệu hoặc tự sửa LOCKED để chuyển READY. |
| REMOVE_CANDIDATE | Chi tiết phụ không phục vụ RQ/O/phương pháp/claim chính và không bắt buộc. Là đề xuất biên tập có căn cứ, không lệnh xóa và không dùng thay cho xử lý thiếu nguồn. |

Không dùng điểm số AI/human hoặc điểm số làm chủ. Khi tác giả trả lời, ghi hoặc liên kết phản hồi đúng nội dung họ cung cấp; không tạo trước câu trả lời rồi coi đó là lời của họ. Thẻ chỉ có thể chuyển READY sau đối chiếu lại bằng chứng, logic và phản hồi; giải thích đúng một phần không chứng minh toàn bộ chương đã được làm chủ.

## 6. Defense Card Template

| Field | Content |
|---|---|
| Section / Claim ID | |
| Claim type | |
| Claim | |
| Evidence / Data | |
| Evidence boundary | |
| Why needed | |
| Author must explain | |
| Likely defense question | |
| Status | |

Trong Evidence / Data ghi nguồn/artifact/DEC và vị trí hỗ trợ; nếu có xác nhận tác giả, ghi vị trí phản hồi, ngày và reviewer. Evidence boundary giữ phần chưa biết và phạm vi không được suy ra. Why needed là vai trò nội dung đối với nghiên cứu, không tự gán động cơ cá nhân. Author must explain nêu yêu cầu giải thích, không dựng câu trả lời mẫu thành lời tác giả.

`DEC_ID_COLLISION_HISTORICAL`: PROJECT_STATE có nhiều quyết định lịch sử cùng mang ID DEC-22 hoặc DEC-23. Khi Defense Card dẫn một trong hai ID này, phải ghi **ID + tên quyết định + ngày**, kèm vị trí trong PROJECT_STATE để phân biệt các mục cùng ngày. Không chỉ dẫn ID, không tự renumber và không chọn quyết định theo thứ tự xuất hiện. Đối chiếu bảng định danh lịch sử trong PROJECT_STATE; nếu chưa xác định được quyết định nào hỗ trợ claim, giữ marker tương ứng và ghi rõ phần chưa xác định.

## 7. Quy tắc bảo toàn

- Không sửa claim boundary để tác giả dễ trả lời hơn; không xóa nguồn, dữ liệu, marker hoặc điều kiện bất định.
- Không bịa author rationale, trải nghiệm, động cơ hoặc quyết định. Quyết định đã duyệt và bằng chứng làm chủ là hai hồ sơ khác nhau.
- Không xóa nội dung bắt buộc của institution; không sửa HUIT, citation/source/data policy hoặc quyết định LOCKED.
- Không tự động chèn Defense Check vào luận văn. Không đưa Defense Card hoặc câu hỏi bảo vệ vào DOCX nộp trường.
- Không xem READY là user approval hoặc toàn dự án PASS. Không tự PASS author mastery.
- Không đưa lớp này vào core skill, templates hoặc AUTHOR_VOICE; cross-reference chỉ qua state, roadmap và prompt tiếp quản của dự án.

## 8. Pilot Chương 1 hiện tại

Đọc `CHAPTER_1.md` tại commit `f30be66ebb7bfd949f36908d451991caf4420737` để phân tích, **không sửa chương**. Pilot không chạy lab, không tái kiểm NotebookLM hoặc chứng nhận lại từng nguồn gốc. Source IDs dẫn về hồ sơ evidence hiện có để review tiếp; không thay IEEE của chương. Các khẳng định hoặc lý do đang có trong bản nháp không được tự coi là phản hồi bảo vệ của tác giả.

### DR-C1-01 — Trọng tâm CVE-2017-0144

| Field | Content |
|---|---|
| Section / Claim ID | §1.2.1–1.2.2; C002; RQ2/O2 |
| Claim type | method/design decision; author decision đối với lý do được gán cho nhóm |
| Claim | Đồ án lấy CVE-2017-0144 làm trọng tâm trong nhóm MS17-010; bản nháp gán lý do không yêu cầu xác thực và tác động SMBv1 cho nhóm. |
| Evidence / Data | RESEARCH_MAP RQ2/O2 và phạm vi; DEC-09/DEC-11–13 ghi phạm vi và chuẩn hóa kỹ thuật. CLAIM_MATRIX C002; SOURCE_LEDGER S005/S011/S013 là tuyến nguồn. Chưa có phản hồi tác giả bảo vệ lý do lựa chọn. |
| Evidence boundary | Trọng tâm đã được duyệt không phải lý do cá nhân đã xác nhận; không dùng cơ chế một CVE đại diện mọi CVE trong bulletin. Không có kết quả kiểm chứng lab tại thẻ này. |
| Why needed | Xác định đối tượng phân tích để RQ2 không mở rộng thành mọi lỗi SMB. |
| Author must explain | Phân biệt bulletin, CVE và mã khai thác; nêu quan hệ giữa trọng tâm được duyệt và câu hỏi/tiêu chí của đồ án. `[CẦN TÁC GIẢ XÁC NHẬN]` phần lý do đang được gán cho nhóm. Không hỏi duyệt lại phạm vi. |
| Likely defense question | Vì sao chọn CVE này và phần nào của MS17-010 không thể suy ra từ phân tích nó? |
| Status | AUTHOR_CONFIRM |

### DR-C1-02 — Vì sao dùng khung bốn mức

| Field | Content |
|---|---|
| Section / Claim ID | §1.4; C003; RQ3/O3 |
| Claim type | interpretation; method/design decision |
| Claim | Khung tách mức cổng, SMBv1, dấu hiệu lỗ hổng và tác động xác minh để tổ chức bằng chứng. |
| Evidence / Data | CLAIM_MATRIX C003; DEC-12/13/17/18 ghi tiêu chí và điều kiện cấp 4. S017/S018/S022/S029/S030/S013 là tuyến nguồn cho phép đo. Chưa có phản hồi bảo vệ của tác giả. |
| Evidence boundary | Khung là cách tổ chức phương pháp của đồ án, không tự nhận tiêu chuẩn do NIST hoặc nhà cung cấp công cụ công bố. Nguồn cho từng phép đo không tự chứng minh tính độc lập giữa các mức hoặc mastery của tác giả. |
| Why needed | Nối dữ liệu công cụ với tiêu chí và kịch bản ở các chương sau. |
| Author must explain | Nêu câu hỏi riêng của từng mức, lý do không gộp thành một kết quả nhị phân và cách xử lý chưa đủ dữ liệu. `[CẦN TÁC GIẢ XÁC NHẬN]` bản giải thích thực của nhóm, không phê duyệt lại khung đã khóa. |
| Likely defense question | Bốn mức giải quyết vấn đề gì mà một nhãn vulnerable không thể giải quyết? |
| Status | AUTHOR_CONFIRM |

### DR-C1-03 — Mỗi mức chứng minh và không chứng minh gì

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.2–1.3.3, §1.4.1–1.4.4; C003 |
| Claim type | interpretation; conclusion |
| Claim | Bản nháp nêu ý nghĩa từng mức, gồm suy ra sẵn sàng tiếp nhận SMB từ SYN-ACK, nạp driver từ dialect và điều kiện mục tiêu không phù hợp từ kết nối đóng/không phản hồi. |
| Evidence / Data | CLAIM_MATRIX C003 chỉ hỗ trợ giới hạn theo phép đo; ledger S017 về SYN scan, S029 về nhận diện phiên bản, S018/S030 về các nhánh thăm dò và lỗi; phần diễn giải bổ sung của CLAIM_MATRIX. Chưa có dữ liệu máy/phiên kiểm thử. |
| Evidence boundary | Cần kiểm riêng bước nhảy từ phản hồi truyền tải sang ứng dụng, từ dialect sang trạng thái nội tại và từ không phản hồi sang nguyên nhân. Hồ sơ hiện không đủ để nhận mọi suy luận đó đã được chứng minh. Marker dữ liệu các chương khác vẫn giữ. |
| Why needed | Ngăn kết luận port open = SMBv1 = vulnerable = exploitable; đây là cầu nối trực tiếp từ quan sát tới đánh giá. |
| Author must explain | Với từng mức, chỉ ra điều quan sát trực tiếp, điều suy ra có điều kiện và điều vẫn chưa biết. Nêu cách phân biệt không xác minh được với đã chứng minh không có lỗ hổng. |
| Likely defense question | Nếu 445 mở nhưng yêu cầu SMB không trả lời, hoặc khai thác không tạo phiên, nhóm được kết luận gì? |
| Status | EVIDENCE_GAP |

### DR-C1-04 — Chuỗi Nmap → NSE → Metasploit

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.2–1.3.5; C003/C004; RQ3/O3 |
| Claim type | method/design decision |
| Claim | Bản nháp sắp công cụ theo khảo sát kết nối, kiểm tra giao thức/dấu hiệu và xem xét xác minh sâu hơn. |
| Evidence / Data | RESEARCH_MAP M3/O3; DEC-13 về module; CLAIM_MATRIX C003/C004; S017/S018/S029/S030/S013/S027. Phạm vi công cụ có trong dự án, không có phản hồi nhóm chứng minh làm chủ hoặc log chạy ở pilot. |
| Evidence boundary | Tên công cụ không tự chứng minh độ sâu hoặc hiệu quả; auxiliary scanner và exploit có nhiệm vụ khác nhau. Thứ tự trong thiết kế không chứng minh mọi bước đã được thực hiện. Chữ độc lập được review riêng tại DR-C1-05. |
| Why needed | Gắn lựa chọn công cụ với câu hỏi và bằng chứng thay vì chỉ giới thiệu tính năng. |
| Author must explain | Với mỗi bước, nêu đầu vào, đầu ra, lý do dùng đầu ra ở bước sau và khi nào phải dừng ở mức chưa xác định. `[CẦN TÁC GIẢ XÁC NHẬN]` cách nhóm giải thích trình tự, không tự điền động cơ lựa chọn. |
| Likely defense question | Vì sao auxiliary scanner không thay thế bước xác minh tác động và vì sao không bắt đầu bằng exploit? |
| Status | AUTHOR_CONFIRM |

### DR-C1-05 — Đối chiếu công cụ có độc lập không

| Field | Content |
|---|---|
| Section / Claim ID | §1.3.4–1.3.5; C003 |
| Claim type | interpretation; conclusion |
| Claim | Bản nháp gọi quét Metasploit và đối chiếu với NSE là độc lập, có thể làm tăng độ tin cậy chỉ báo. |
| Evidence / Data | SOURCE_LEDGER S030 ghi scanner dùng cùng dấu hiệu IPC$/FID 0; S018/S030 và mục đối chiếu nguồn gốc là tuyến kiểm cơ chế. CLAIM_MATRIX C003 không xác lập tính độc lập của sai số hoặc phép đo. |
| Evidence boundary | Hai lần chạy hoặc hai công cụ không tự chứng minh bằng chứng độc lập. Chưa có đối soát phụ thuộc, sai số hoặc dữ liệu xác thực hiệu quả tăng độ tin cậy; phải quay về evidence/logic review. |
| Why needed | Ảnh hưởng trực tiếp tới mức chắc chắn khi cùng hai công cụ báo vulnerable. |
| Author must explain | Phân biệt đối chiếu output, khác cách triển khai và độc lập về nguồn tín hiệu/giả định. Xác định bằng chứng nội tại hoặc phép đo khác cần đối chiếu. Không viết mềm để che khoảng trống. |
| Likely defense question | Hai công cụ cùng báo vulnerable có loại được cùng một nguyên nhân sai hay không? |
| Status | EVIDENCE_GAP |

### DR-C1-06 — Đối chiếu hộp đen và trạng thái nội tại

| Field | Content |
|---|---|
| Section / Claim ID | §1.4.5 và cầu nối Chương 1 → Chương 2; C003/C004 |
| Claim type | interpretation; method/design decision |
| Claim | Kết quả từ góc nhìn máy kiểm thử cần đối chiếu với bản vá, cấu hình SMB và điều kiện mạng để giới hạn kết luận về Server. |
| Evidence / Data | CHAPTER_ARGUMENT phần tiền điều kiện/ma trận bằng chứng; DEC-17/18 ghi thiết kế và góc nhìn máy kiểm thử so với nội tại Server. CLAIM_MATRIX C003/C004; SOURCE_LEDGER S024. Quyết định phương pháp đã khóa; dữ liệu thực nghiệm còn mở theo DEC-03. |
| Evidence boundary | Hồ sơ thiết kế không phải kết quả quan sát. Phần LOCKED còn mâu thuẫn đã ghi trong PROJECT_STATE; không tự đổi các giá trị/trạng thái để thẻ đạt. Đối chiếu nội tại cũng phải cùng mục tiêu và lượt kiểm tra. |
| Why needed | Nối giới hạn phép đo ở Chương 1 với cách thu thập/đối chứng ở Chương 2. |
| Author must explain | Vì sao cùng phản hồi mạng có thể cần các dữ kiện nội tại khác nhau; dữ liệu nào phân biệt chặn kết nối với cập nhật sửa lỗi. `[CẦN TÁC GIẢ XÁC NHẬN]` bản giải thích, không duyệt lại thiết kế đã khóa. |
| Likely defense question | Khi NSE không thấy dấu hiệu, nhóm kiểm bản vá và cấu hình như thế nào trước khi kết luận? |
| Status | AUTHOR_CONFIRM |

### DR-C1-07 — Mức FEA cần làm chủ

| Field | Content |
|---|---|
| Section / Claim ID | §1.2.3; C002; RQ2/O2 |
| Claim type | source fact; interpretation về mức cần trình bày |
| Claim | Phần cơ chế mô tả tính kích thước, cấp phát, sao chép và khả năng ghi ngoài vùng đệm; có tên hai hàm xử lý FEA. |
| Evidence / Data | SOURCE_LEDGER S013 và ghi chú đối chiếu SrvOs2FeaListSizeToNt/SrvOs2FeaToNt; CLAIM_MATRIX C002 và phần diễn giải cơ chế; DEC-09/12/13 ghi yêu cầu phân tích. Không có bản giải thích tác giả hoặc reverse engineering do nhóm thực hiện. |
| Evidence boundary | Nhóm cần phân biệt kích thước cấp phát với lượng ghi, sự cố với thực thi mã; không tự nhận đã phân tích nhị phân hoặc quan sát kernel. Ví dụ kích thước giả định trong hồ sơ lịch sử không phải dữ liệu. Tên hàm có nguồn không chứng minh nhóm cần trình bày mọi chi tiết triển khai. |
| Why needed | Trả lời cơ chế của RQ2 và giải thích rủi ro kiểm thử; chỉ giữ chi tiết sâu khi nó phục vụ bước suy luận này. |
| Author must explain | Giải thích quan hệ kích thước → cấp phát → ghi ngoài vùng đệm và vì sao lỗi không tự bảo đảm khai thác thành công. `[CẦN TÁC GIẢ XÁC NHẬN]` mức nhóm giải thích được và vai trò của tên hàm; nếu cần simplify, vẫn giữ chuỗi cơ chế bắt buộc và nguồn. |
| Likely defense question | Nếu bỏ tên hàm, nhóm còn giải thích được lỗi và điều kiện tác động không; vì sao tên hàm cần có? |
| Status | AUTHOR_CONFIRM |

### DR-C1-08 — Cấp 4 và giới hạn kết luận xuyên chương

| Field | Content |
|---|---|
| Section / Claim ID | §1.4.4–1.4.5; C003/C004; CHAPTER_ARGUMENT mục 4 |
| Claim type | conclusion; method/design decision |
| Claim | Chương 1 dùng quyền tương tác để xác minh thực thi mã; hợp đồng Chương 2 đã khóa có tiêu chí yêu cầu mã chạy trong không gian nhân và nêu output/phiên/process ID làm ví dụ bằng chứng. |
| Evidence / Data | DEC-17/18; CHAPTER_ARGUMENT mục 4; SOURCE_LEDGER ghi nguồn S013 không chứng minh output SYSTEM là quan sát trực tiếp Kernel Mode. PROJECT_STATE đã ghi CONFLICT_LOCKED. Pilot không có log xác minh mức nào. |
| Evidence boundary | Không tự đồng nhất phiên tương tác, quyền hệ thống và quan sát thực thi trong nhân. Tiêu chí ở hai artifact cần được xử lý theo quy trình evidence/locked decision, không sửa ngầm bằng rule này. Crash không phải thành công; không có dữ liệu thì chưa đánh giá kết quả. |
| Why needed | Bảo đảm Chương 3/4 không báo PASS mạnh hơn điều bằng chứng thực sự hỗ trợ. |
| Author must explain | Xác định mục tiêu nào cần chứng minh, bằng chứng nào chỉ hỗ trợ thực thi/đặc quyền và dữ liệu nào còn thiếu cho yêu cầu mức nhân; phân biệt tiêu chí dự kiến với kết quả. |
| Likely defense question | Phiên chạy với quyền SYSTEM có tự chứng minh nhóm quan sát được mã thực thi trong kernel không? |
| Status | EVIDENCE_GAP |

## 9. Theo dõi pilot và bước tiếp theo

Pilot có **8 thẻ: 5 AUTHOR_CONFIRM, 3 EVIDENCE_GAP, 0 READY**. Không suy ra tác giả không hiểu; hiện chưa có phản hồi bảo vệ để xác nhận. Chưa dùng SIMPLIFY/REMOVE_CANDIDATE vì không đủ căn cứ để kết luận chi tiết hiện tại cần giảm hoặc bỏ mà không xử lý evidence/ownership trước.

- `[CẦN TÁC GIẢ XÁC NHẬN]`: DR-C1-01/02/04/06/07, thu bản giải thích thực, không phê duyệt lại quyết định đã khóa.
- DR-C1-03/05/08 quay về evidence và logic; lưu khoảng trống tại state. Không sửa chương, nguồn, dữ liệu hoặc artifact LOCKED trong task tích hợp này.
- Tại G5, claim trọng tâm phải có READY có căn cứ, hoặc AUTHOR_CONFIRM đã được người dùng xử lý và phản hồi được đối chiếu để cập nhật thẻ; không để nhãn chờ nhưng coi là đã giải quyết. EVIDENCE_GAP chưa đóng không được xem là đạt.
- Bước tiếp theo trong lượt review chương được cho phép: đối chiếu các gap và thu phản hồi theo thẻ, rồi xử lý trim/giọng/lint và xin duyệt. Hoàn tất tích hợp rule không phải project PASS.
