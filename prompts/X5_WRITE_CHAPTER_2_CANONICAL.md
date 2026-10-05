# ANTIGRAVITY PROMPT — X5 / VIẾT LẠI CHƯƠNG 2 CANONICAL

Trạng thái nhiệm vụ: READY_FOR_EXECUTION
Phạm vi: CHỈ Chương 2.
Không viết Chương 3, Chương 4. Không dựng DOCX.

## 1. Vai trò

Bạn là executor. Người dùng là final approver. Reviewer bên ngoài sẽ chấm bản của bạn sau khi hoàn thành.
Bạn không được tự đổi scope, không tự đổi Experimental Truth Matrix và không tự tuyên bố PASS.

## 2. Đọc bắt buộc trước khi viết

Đọc theo thứ tự:

1. `AGENTS.md`
2. `.agents/skills/thesis-research-and-writing/SKILL.md`
3. `work/do-an/PROJECT_STATE.md`
4. `work/do-an/PROJECT_PROFILE.md`
5. `work/do-an/RESEARCH_MAP.md`
6. `work/do-an/OUTLINE.md`
7. `work/do-an/CHAPTER_ARGUMENT.md`
8. `work/do-an/CHAPTER_2_CONTRACT.md`
9. `work/do-an/CHAPTERS_2_4_EVIDENCE_MAP.md`
10. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
11. `work/do-an/EVIDENCE_REGISTER.md`
12. `work/do-an/NEGATIVE_RESULT_POLICY.md`
13. `work/do-an/CLAIM_MATRIX_2_4.md`
14. `work/do-an/SOURCE_LEDGER.md`
15. `work/do-an/AUTHOR_VOICE.md`
16. Hai kịch bản giảng viên và đề cương chi tiết nếu cần đối chiếu.

## 3. Mục tiêu Chương 2

Trả lời duy nhất câu hỏi:

“Mô hình lab và quy trình kiểm thử được thiết kế như thế nào để an toàn, tái lập, truy vết được và đủ khả năng phân biệt các lớp bằng chứng SMB/MS17-010?”

Chương 2 là **METHOD / DESIGN chapter**, không phải result chapter.

## 4. Cấu trúc bắt buộc

Bám chính xác `OUTLINE.md` phần Chương 2:

2.1. Yêu cầu và nguyên tắc thiết kế  
2.2. Kiến trúc môi trường thực nghiệm  
2.3. Chuẩn bị trạng thái baseline  
2.4. Phương pháp kiểm thử và mô hình bằng chứng  
2.5. Thiết kế Kịch bản 1  
2.6. Thiết kế Kịch bản 2  
2.7. Thiết kế kiểm thử biện pháp giảm thiểu  
2.8. Tiêu chí đánh giá kết quả  
2.9. Tổng kết Chương 2

Giữ các tiểu mục đã khóa trong OUTLINE.

## 5. Canonical facts bắt buộc

- Oracle VM VirtualBox.
- Kali Linux.
- Windows Server 2012 R2 Standard Evaluation, Build 9600.
- Kali: 192.168.56.10/24.
- Windows: 192.168.56.20/24.
- Baseline: Host-Only.
- Snapshot: `Before Demo`.
- SMB1=True, SMB2=True ở baseline.
- Patch ground truth baseline: `UNPATCHED`.
- Nmap 7.99 ở pre-demo.
- Scenario 1 = Nmap SMB 139/445.
- Scenario 2 = NSE-SMB-01..04.
- Case B = disable SMBv1.
- Case C = pfSense Transparent Bridge chặn TCP 139/445.
- Baseline remote NSE-MS17-010 canonical = UNKNOWN / NO USABLE SCRIPT RESULT.

## 6. Những gì tuyệt đối KHÔNG được viết như canonical

- Windows 7 SP1 x64.
- Enterprise topology 3 VLAN.
- Client VLAN 30 / positive business control.
- 4-state S0→S3 cũ.
- Case C = Windows Firewall.
- Case A patch = đã thực nghiệm thành công.
- Baseline NSE = VULNERABLE.
- STATUS_INSUFF_SERVER_RESOURCES nếu không có trong raw canonical.
- Metasploit exploit success/RCE/SYSTEM/Meterpreter.
- Wireshark/PCAP/Event Viewer result nếu không có canonical evidence.
- “100% an toàn”, “triệt để”, “hoàn hảo”, “không thể chối cãi”.

## 7. Cách dùng evidence trong Chương 2

Chương 2 được phép dùng evidence để chứng minh **môi trường và baseline có thật**, nhưng không được kể kết quả chi tiết của Scenario 1/2/Case B/C.

Ví dụ:
- được viết IP/OS/NIC/snapshot/baseline từ ENV-CORE IDs;
- được mô tả command family và tiêu chí đo dựa vào kịch bản;
- không được viết “kết quả quét cho thấy ...” ở mục thiết kế, trừ fact baseline cần thiết đã được khóa.

Mọi fact cấu hình phải truy được tới Evidence ID hoặc source.

## 8. Yêu cầu học thuật

- 3.500–4.500 từ mục tiêu.
- Không kéo dài chỉ để đạt số từ.
- Mỗi mục phải trả lời “tại sao thiết kế như vậy / nó bảo vệ tính hợp lệ của phép đo như thế nào”.
- Tách SOURCE_FACT, AUTHOR_DATA và INTERPRETATION.
- Giải thích lý do chọn Host-Only, snapshot, raw output, local patch ground truth và differential testing.
- Nêu inference boundary trước khi sang Chương 3.
- Patch phải xuất hiện như một lớp phòng thủ quan trọng nhưng chưa có canonical Case A result.
- Metasploit chỉ mô tả vai trò trong phạm vi nghiên cứu nếu cần, không biến thành bước demo đã thực hiện.

## 9. Hình và bảng

Theo `FIGURE_TABLE_BUDGET.md`:
- Chương 2: 3–5 hình, 3–5 bảng.
- Ưu tiên:
  - 1 sơ đồ topology canonical;
  - 1 sơ đồ flow/method;
  - bảng môi trường/IP;
  - bảng lớp bằng chứng;
  - bảng thiết kế Scenario 1/2;
  - bảng biến can thiệp Case B/C.
- Không nhét screenshot cài đặt/troubleshooting.
- Nếu chưa có sơ đồ final, dùng placeholder rõ ràng và ghi requirement; không tự tạo evidence giả.

## 10. Citation

- Dùng source đã verified trong `SOURCE_LEDGER.md`.
- Citation IEEE theo quy tắc repo.
- Evidence do nhóm thu không được giả thành nguồn học thuật.
- Không cite NotebookLM.
- Nếu một claim lý thuyết chưa có source verified: dùng `[CẦN NGUỒN]`, không tự chế citation.

## 11. File được phép sửa

Được sửa:
- `work/do-an/CHAPTER_2.md`
- tạo `work/do-an/CHAPTER_2_X5_SELF_REVIEW.md`
- cập nhật `PROJECT_STATE.md` chỉ để ghi trạng thái X5 draft/review, không tự PASS.

Không được sửa:
- `EXPERIMENTAL_TRUTH_MATRIX.md`
- raw evidence
- `PROJECT_PROFILE.md`
- `RESEARCH_MAP.md`
- `OUTLINE.md`
- chapter contracts
- Chương 3/4
- DOCX.

## 12. QA bắt buộc trước khi trả

- kiểm tra toàn bộ Chapter 2 với contract;
- kiểm tra fact config với Evidence IDs;
- citation audit;
- lint tiếng Việt học thuật;
- kiểm tra từ ngữ tuyệt đối hóa;
- kiểm tra không có result leakage từ Ch3;
- kiểm tra không còn Windows 7/3 VLAN/Client control;
- kiểm tra không có Case A canonical claim;
- báo word count;
- ghi mọi nhãn còn mở.

## 13. Đầu ra cuối lượt

Báo cáo:
1. file đã sửa/tạo;
2. word count;
3. bảng coverage 2.1–2.9;
4. citation/source QA;
5. evidence QA;
6. các claim/đoạn đã loại từ Ch2 cũ;
7. nhãn còn mở;
8. test/lint đã chạy;
9. git diff summary;
10. trạng thái: `X5_DRAFT_READY_FOR_EXTERNAL_REVIEW`.

Không tự ghi PASS.
