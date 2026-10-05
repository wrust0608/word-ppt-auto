# X5 — REWRITE CHAPTER 2 FROM USER-APPROVED STRUCTURE

Trạng thái: `READY_FOR_EXECUTOR`  
Branch làm việc: `feature/x5-chapter-2-structural-revision`

Executor phải đọc và làm đúng file này. Không được tự mở rộng scope.

## Mục tiêu

Viết lại hoàn chỉnh `work/do-an/CHAPTER_2.md` theo cấu trúc đã được người dùng duyệt trong:

`origin/main:work/do-an/CHANGE_REQUEST_CR-2026-10-05-X5-STRUCTURE.md`

Chương 2 phải chính xác về kỹ thuật, bám evidence, có logic đồ án ATTT, không lan man, không viết như checklist vận hành, và không kể trước kết quả Chương 3.

## Quy trình bắt buộc

1. `git fetch origin`
2. checkout `feature/x5-chapter-2-structural-revision`
3. xác nhận clean state và HEAD.
4. Đọc toàn bộ các artifact theo thứ tự:

### Governance / structure
- `git show origin/main:work/do-an/CHANGE_REQUEST_CR-2026-10-05-X5-STRUCTURE.md`
- `git show origin/main:work/do-an/PROJECT_STATE.md`
- `git show origin/main:work/do-an/EXECUTION_PLAN_2026_10_05.md`
- `work/do-an/X5_STRUCTURAL_REVIEW_2026_10_05.md`

### Technical truth / evidence
- `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
- `work/do-an/EVIDENCE_REGISTER.md`
- `work/do-an/NEGATIVE_RESULT_POLICY.md`
- `work/do-an/CHAPTERS_2_4_EVIDENCE_MAP.md`
- `work/do-an/CLAIM_MATRIX_2_4.md`

### Sources
- `work/do-an/SOURCE_LEDGER.md`
- `work/do-an/SOURCE_RECONCILIATION_PLAN.md` nếu có

### Author voice / publication constraints
- `work/do-an/AUTHOR_VOICE.md`
- `work/do-an/AUTHOR_VOICE_CALIBRATION.md`
- `work/do-an/FIGURE_TABLE_BUDGET.md`
- `work/do-an/CHAPTER_2_CONTRACT.md`

### Historical candidate for technical facts only
- candidate cũ tại commit `ba0cd980a0075427959567d4793dc1e35b95773d`
- dùng để đối chiếu claim/evidence đã từng qua review;
- KHÔNG copy structure 9 H2 / 42 H3.

## Cấu trúc khóa

Dùng đúng 8 H2 / 25 H3 trong Change Request. Không thêm, bớt, đổi tên hoặc đổi thứ tự.

## Nguyên tắc viết

- Viết như một chương đồ án ATTT hoàn chỉnh, không phải runbook.
- Mỗi mục phải có vai trò duy nhất.
- Ưu tiên đoạn văn liên tục; bảng chỉ dùng khi thực sự giúp đối chiếu.
- Không dùng jargon quản trị repo như `canonical`, `ground truth`, `THEORETICAL_REFERENCE_ONLY` trong prose dành cho người đọc nếu có cách diễn đạt học thuật tự nhiên hơn.
- Có thể dùng các thuật ngữ kỹ thuật tiếng Anh đã quen thuộc như baseline, dialect, signing, filtered, raw output sau khi giải thích lần đầu.
- Không dùng ASCII art trong bản chính. Dùng placeholder hình có caption mô tả rõ nội dung cần dựng về sau.
- Không đặt danh mục tài liệu tham khảo riêng ở cuối Chương 2; chỉ giữ citation markers để bibliography toàn báo cáo xử lý ở G5/G6.
- Không bịa trải nghiệm, số liệu, lý do, output hoặc screenshot.

## Ranh giới Chương 2 / Chương 3

Chương 2 được phép:
- mô tả environment facts và baseline facts cần thiết;
- mô tả lệnh/script/phương pháp;
- mô tả loại output cần thu;
- mô tả tiêu chí diễn giải;
- mô tả biến can thiệp Case B/C.

Chương 2 không được:
- kể chi tiết observed result của Scenario 1/2;
- kể dialect list thực đo như kết quả;
- kể open/filtered transition như kết quả;
- trình bày firewall log như observation;
- trình bày kết quả Case B/C như đã phân tích xong;
- kết luận vulnerability từ SMBv1/open445.

Chi tiết observation thuộc Chương 3.

## Truth locks

Giữ tuyệt đối:
- Baseline: VirtualBox 7.2.20; Kali .56.10; Windows Server 2012 R2 Build 9600 .56.20; Host-Only; no NAT/Bridged/default route.
- Nmap 7.99.
- Snapshot Before Demo trên Kali + Windows.
- Baseline local SMB1=True, SMB2=True; LanmanServer Running/Automatic; 139/445 listen.
- Windows Firewall: allow TCP 139/445 chỉ từ Kali; default File and Printer Sharing group off.
- Patch state: UNPATCHED; numeric srv.sys 6.3.9600.16421; display version distinction không được làm sai.
- Scenario 1 safe NSE = smb-protocols, smb-os-discovery, smb2-security-mode, smb2-capabilities.
- Scenario 1 không kết luận MS17-010.
- Scenario 2: NSE01 ports, NSE02 protocols, NSE03 signing, NSE04 smb-vuln-ms17-010.
- NSE04 canonical verdict = UNKNOWN / NO USABLE SCRIPT RESULT.
- Case B = disable SMBv1; không patch.
- Case C = pfSense Transparent Bridge; filtering network path; không patch host.
- Case A patch = theoretical/reference only trong bộ evidence hiện hành.

## Source discipline

Chỉ dùng nguồn VERIFIED trong SOURCE_LEDGER cho claim mới.

Đặc biệt:
- NIST SP800-115 cho testing methodology.
- NIST SP800-41 cho firewall policy.
- Microsoft Direct-hosted SMB cho TCP445/139.
- Microsoft MS17-010 bulletin cho KB mapping.
- Microsoft SMB signing source cho signing.
- Nmap source `smb-protocols.nse` cho dialect detection.
- Nmap source `smb-vuln-ms17-010.nse` cho logic script.
- Microsoft enable/disable SMBv1/v2/v3 cho Case B.

Nếu cần dùng nguồn Microsoft “How to verify that MS17-010 is installed” cho ngưỡng `srv.sys 6.3.9600.18604`, KHÔNG tự thêm citation như thể ledger đã khóa. Hãy:
1. thêm nó vào một mục `SOURCE_LEDGER_PROPOSED_ADDITION_X5.md`;
2. ghi metadata + claim supported;
3. không sửa SOURCE_LEDGER locked trực tiếp;
4. báo external reviewer xử lý change control.

## Hình và bảng

Mục tiêu Ch2:
- 3–5 hình;
- 3–5 bảng.

Bắt buộc có:
1. topology baseline;
2. environment/baseline table;
3. evidence-layer model;
4. scenario flow hoặc phép đo matrix.

Có thể thêm:
5. differential-testing flow.

Không dùng screenshot nếu diagram/table diễn đạt tốt hơn.

Mỗi hình placeholder phải ghi:
- nội dung cần vẽ;
- mục đích;
- caption dự kiến;
- evidence/source cần đối chiếu.

## Chất lượng văn

- Ngôi thứ ba khách quan.
- Không mở đoạn bằng sáo ngữ.
- Không ép mọi đoạn có câu tổng kết.
- Không dùng “qua đó/từ đó/như vậy/đồng thời” theo công thức.
- Không dịch thô kiểu “sự thật mặt đất”, “bản tin” chung chung, “ngăn xếp mạng” nếu không thật sự phân tích stack.
- Ưu tiên câu trực tiếp cho ý đơn giản.
- Không dùng heading thay cho logic.
- Không lặp cùng một fact ở 3 mục khác nhau.

## Target length

Khoảng 3,800–4,500 từ.
Không cần cố đạt trần.
Nếu nội dung đầy đủ ở ~4,000 từ, giữ ngắn gọn.

## QA bắt buộc trước commit

Chạy:
- `uv run python scripts/validate_project.py`
- `uv run python -m unittest discover -s tests -p "test_*.py"`
- `uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md` nếu auditor tương thích với bibliography toàn cục; nếu không, báo rõ giới hạn thay vì sửa cấu trúc để chiều tool.
- `uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md`
- `git diff --check`

Kiểm thủ công:
- đúng 8 H2 / 25 H3;
- exact order;
- không result leakage;
- không UNKNOWN→SAFE;
- không FILTERED→PATCHED;
- không SMB1 disabled→PATCHED;
- không Case A result;
- không stale Windows 7/3 VLAN;
- không wildcard NSE;
- không pfSense trong baseline topology;
- mọi số phiên bản/IP/KB có nguồn/evidence đúng;
- mỗi H3 có chức năng riêng;
- không bibliography riêng cuối Ch2.

## File được phép sửa

Bắt buộc:
- `work/do-an/CHAPTER_2.md`
- `work/do-an/CHAPTER_2_X5_SELF_REVIEW.md`

Tùy điều kiện:
- `work/do-an/SOURCE_LEDGER_PROPOSED_ADDITION_X5.md`

Không sửa:
- EXPERIMENTAL_TRUTH_MATRIX
- EVIDENCE_REGISTER
- NEGATIVE_RESULT_POLICY
- SOURCE_LEDGER locked
- CHAPTER_3 / CHAPTER_4
- main
- DOCX

## Git

Commit trên:
`feature/x5-chapter-2-structural-revision`

Push branch.

Không merge main.

## Handoff cuối

Trả:
1. branch + commit SHA;
2. word count;
3. 8 H2 / 25 H3 check;
4. 3–5 hình / 3–5 bảng plan;
5. source/citation audit;
6. evidence/truth-boundary audit;
7. author-voice audit;
8. test/linter results;
9. diff stat;
10. open labels;
11. any proposed source addition.

Trạng thái cuối chỉ được ghi:
`X5_STRUCTURAL_REWRITE_READY_FOR_EXTERNAL_REVIEW`

Sau đó DỪNG.

External Reviewer sẽ kiểm tra artifact remote trực tiếp. Không tự tuyên bố PASS. Không mở X6.
