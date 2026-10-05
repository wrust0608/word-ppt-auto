# X5 DEMO-STYLE — EXTERNAL REVIEW R1

Ngày: 2026-10-05  
Candidate branch: `feature/x5-chapter-2-demo-style`  
Candidate commit: `aec00df5efe9dd35d3a031becb1a056695ad2994`  
Kết luận: `REVISE_BLOCKING / PRESENTATION_DIRECTION_APPROVED`

## 1. Điểm

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 10/15 |
| Academic depth / reasoning | 14/20 |
| Technical accuracy | 8/20 |
| Sources / traceability | 6/15 |
| Structure | 10/10 |
| Academic style / readability | 9/10 |
| QA / artifact consistency | 9/10 |
| **Tổng** | **66/100** |

Blocker: YES.

## 2. Điều đạt

- Hướng trình bày demo-style đúng hơn R5.
- 7 H2 / 20 H3 hợp lý, dễ theo dõi.
- Lab -> cấu hình -> Demo 1 -> Demo 2 -> mitigation -> dữ liệu -> tổng kết là đúng nhịp đồ án thực hành.
- Ít governance jargon, không Evidence ID spam.
- Các lệnh được đưa vào code block và người đọc dễ tìm.
- Word count và QA hình thức đạt.
- Remote commit tồn tại thật.

## 3. Blocker A — Research artifact không đủ mức bằng chứng cho các kết luận đã tuyên bố

Artifact tuyên bố đã khảo sát 8 công trình từ PTIT/HUIT/UIT/ACTVN và rút ra pattern chi tiết về topology, code block, screenshot, bảng, before-after.

Tuy nhiên log executor chủ yếu thể hiện web search, không cho thấy quá trình mở/đọc toàn văn từng tài liệu trước khi tạo artifact. Một số tài liệu PTIT xác minh được ở mức metadata/abstract nhưng PDF toàn văn bị restricted. Vì vậy không được trình bày các pattern chi tiết như đã quan sát trực tiếp từ full text nếu chưa truy cập được.

Bắt buộc R2:
- với từng nguồn phải có URL/handle;
- ghi access level: FULL_TEXT / ABSTRACT_ONLY / METADATA_ONLY;
- chỉ rút pattern tương ứng với mức nội dung thật sự đọc được;
- nguồn không xác minh được phải bỏ;
- không dùng tên đồ án tự suy đoán.

Research chỉ được học presentation, tuyệt đối không được sinh technical facts mới.

## 4. Blocker B — Demo 1 hồi quy khỏi kịch bản lecturer/canonical

Draft rút Demo 1 thành 4 bước và thay bước discovery bằng `ping`.

Canonical Scenario 1:
1. B1 Kali IP/route;
2. B2 host discovery `192.168.56.0/24`;
3. B3 target alive `192.168.56.20`;
4. B4 SYN 139/445;
5. B5 service/version;
6. B6 exact 4 safe NSE scripts;
7. lưu raw;
8. interpretation boundary.

Phải giữ flow này nhưng trình bày đơn giản. Không được đơn giản hóa bằng cách đổi nội dung kịch bản.

## 5. Blocker C — smb-vuln-ms17-010 có argument tự tạo

Draft dùng:
`--script-args unsafe=0`

Nmap NSEDoc chính thức không liệt kê argument này cho `smb-vuln-ms17-010`.

Phải bỏ hoàn toàn `unsafe=0` và câu giải thích rằng nó “bảo đảm không kích hoạt nhánh khai thác bộ nhớ”.

Cơ chế chỉ mô tả theo official source:
- connect IPC$;
- transaction on FID 0;
- check returned status codes.

## 6. Blocker D — Demo 2 taxonomy vượt canonical policy

Draft thêm:
- `NOT VULNERABLE`;
- True Positive;
- True Negative;
- Sai lệch cảnh báo.

Đối với report hiện hành, giữ đơn giản:
- remote script có usable verdict thì ghi đúng verdict;
- canonical run hiện có `UNKNOWN / NO USABLE SCRIPT RESULT`;
- UNKNOWN không được đổi thành SAFE / NOT VULNERABLE / VULNERABLE;
- local patch state được kiểm tra độc lập.

Không cần confusion-matrix terminology ở Chương 2.

## 7. Blocker E — Bảng mitigation chứa các kết quả kỳ vọng sai

Bảng 2.2 hiện ghi:
- Baseline: “phát hiện MS17-010”;
- Case B: “triệt tiêu MS17-010”;
- Case C: “chặn thăm dò”;
- Case A: “máy an toàn”.

Sai với Truth Matrix.

Phải thay bằng tiêu chí cần kiểm tra, không phải kết quả mong muốn:
- Baseline: đo ports/protocols/NSE + local patch;
- Case B: kiểm tra SMB1 còn xuất hiện hay không; patch state không đổi;
- Case C: kiểm tra reachability từ Kali và log rule; host state không đổi;
- Case A: reference only / not measured.

## 8. Blocker F — Case B bị thêm thao tác và retest không canonical

Draft thêm:
- `Restart-Computer -Force`;
- chạy lại toàn bộ NSE-SMB-01 -> 04.

Canonical action:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Canonical retest evidence:
- protocols;
- MS17-010.

Không thêm restart hoặc phép đo thực tế nếu evidence/kịch bản lecturer không yêu cầu.

## 9. Blocker G — pfSense version và policy sai canonical

Draft ghi pfSense 2.7.2.

Canonical run = pfSense CE 2.9.0.

Policy canonical:
TCP `192.168.56.10 -> 192.168.56.20:139,445`, logging enabled.

Phải ghi source + destination + ports, không viết rule như chặn mọi nguồn.

Tunables R1 đang đúng:
- pfil_member=1
- pfil_bridge=0
- pfil_onlyip=1

## 10. Blocker H — Case A bị biến thành kết luận thực nghiệm/lý thuyết quá mạnh

Draft viết:
- KB4012213 là “giải pháp duy nhất”;
- nâng driver từ exact local version lên exact threshold;
- “loại bỏ hoàn toàn”;
- “máy an toàn”;
- Case B “triệt tiêu bề mặt tấn công MS17-010”.

Phải quay về boundary:
- patching là biện pháp trực tiếp thay đổi patch state;
- applicable direct KB: KB4012213 / KB4012216 hoặc superseding update;
- threshold 6.3.9600.18604 dùng để verify patched state;
- Case A không có canonical experiment;
- không nói safe/triệt để/hoàn toàn.

## 11. Blocker I — Dữ liệu thu thập bị bịa thêm

Draft thêm như fact/procedure:
- tcpdump/tshark đã cài;
- .pcap capture;
- Event Viewer logs;
- timestamp screenshot requirements.

Core evidence hiện hành khóa:
- Nmap/NSE raw .nmap/.xml/.gnmap;
- screenshots;
- pfSense log;
- local PowerShell/system state.

Nếu tcpdump/tshark/.pcap/Event Viewer không có trong approved scenario/evidence, phải bỏ khỏi Chương 2. Không lấy chúng từ report mẫu.

## 12. Blocker J — Snapshot restore biến design thành observed event

Draft nói phục hồi snapshot sau mỗi ca/phiên can thiệp.

Evidence chứng minh snapshot `Before Demo` tồn tại; không có artifact cho từng restore event.

Viết:
“snapshot được dùng làm mốc phục hồi khi cần trước khi đổi biến can thiệp.”

Không claim mọi lần đã restore.

## 13. Overclaims cần loại

Bỏ:
- “cách ly hoàn toàn”;
- “ngăn chặn rò rỉ gói tin”;
- “chặn toàn bộ truy cập ngoài phạm vi”;
- “hoàn toàn vắng mặt” nếu chỉ kiểm tra mapping cụ thể;
- “ngưỡng an toàn” -> “minimum updated version / ngưỡng phiên bản đã cập nhật”;
- “triệt tiêu”;
- “an toàn triệt để”.

## 14. Bibliography architecture

Không thêm `# TÀI LIỆU THAM KHẢO` riêng vào CHAPTER_2.md nếu repository dùng bibliography toàn báo cáo.

Citation sequence có thể được audit ở chapter-level, nhưng reference list vẫn thuộc final synthesis.

## 15. Research direction decision

Research-first direction: KEEP.

Nhưng R2 phải tách:
- VERIFIED_PRESENTATION_PATTERN;
- INFERENCE_FROM_METADATA;
- UNVERIFIED_SOURCE (remove from conclusions).

Không để “tham khảo báo cáo ngoài” thay đổi technical truth của project.

## 16. Workflow state

- 7 H2 / 20 H3: RETAIN.
- Demo-style direction: APPROVED.
- Candidate R1: REVISE_BLOCKING.
- CP5-USER: PENDING.
- X6: BLOCKED.
