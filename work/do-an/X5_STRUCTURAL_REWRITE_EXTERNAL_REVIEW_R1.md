# X5 STRUCTURAL REWRITE — EXTERNAL REVIEW ROUND 1

Ngày: 2026-10-05  
Nguồn handoff: agent local execution log / draft.  
Kết luận: `REJECT_AS_CANDIDATE / RECOVERABLE_DRAFT`

## 1. Score

| Hạng mục | Điểm |
|---|---:|
| Compliance / workflow | 5/15 |
| Academic depth / reasoning | 15/20 |
| Technical accuracy | 9/20 |
| Sources / traceability | 7/15 |
| Structure | 10/10 |
| Author Voice / readability | 8/10 |
| QA / artifact consistency | 3/10 |
| **Tổng** | **57/100** |

Blocker: YES.

## 2. Điều đã đạt

- User-approved structure được triển khai đúng theo danh sách thực tế: 8 H2 / 27 H3.
- Target length khoảng 4.3k từ phù hợp contract.
- Không quay về cấu trúc 42 H3.
- Mạch chương research design → lab/baseline → evidence method → Scenario 1 → Scenario 2 → mitigation → evaluation → summary được giữ.
- Figure/table budget nằm trong khung.
- Author voice có cải thiện so với bản cũ.

Lưu ý governance: Change Request trước ghi nhầm “25 H3”; danh sách heading thực tế cộng lại là 27. Đây là lỗi đếm của reviewer/prompt, không phải lỗi executor. Từ vòng này canonical structure count = 8 H2 / 27 H3.

## 3. Blocker A — Không làm việc trên remote repository thật

Agent không tìm được clone repo, sau đó tự tạo Git repository mới ở `D:\SHARE_ALL\BAOCAO` bằng `git init`.

Hệ quả:
- commit `b032d9400474a65dac7d53f361137194848d3d7b` chỉ là local commit;
- commit không tồn tại trên GitHub repository `wrust0608/word-ppt-auto`;
- remote branch `feature/x5-chapter-2-structural-revision` vẫn chứa candidate cũ;
- validation scripts / linter / repo governance artifacts không có trong repo local tự tạo;
- self-review không thể được coi là repo-level QA.

Không được dùng `git init` để thay thế repo thật trong vòng corrective.

## 4. Blocker B — Fabricated / contaminated NSE result

Draft ghi rằng `smb-vuln-ms17-010` trả:

`State: Risk factor: High - Server might be vulnerable to MS17-010, can't be sure`

Canonical Experimental Truth Matrix khóa:
- raw NSE-SMB-04 không sinh usable Host script result/verdict;
- canonical classification = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- không có message trên trong raw canonical.

Phải xóa toàn bộ message/cảnh báo này và mọi suy luận dựa trên nó.

## 5. Blocker C — NO OUTPUT bị gán nguyên nhân

Draft ghi NO OUTPUT xảy ra khi điều kiện script không thỏa để kích hoạt hàm output.

Không có canonical evidence cho nguyên nhân này.

Chương 2 chỉ được định nghĩa:
- script không cung cấp usable output trong lượt đo;
- không suy đoán nguyên nhân nếu raw/source không chứng minh.

## 6. Blocker D — FILTERED định nghĩa quá mạnh

Draft ghi filtered biểu thị packet bị block/drop bởi cơ chế lọc trung gian.

General method phải theo Nmap semantics:
- scanner không nhận đủ phản hồi để phân loại open/closed.

Chỉ ở Case C, sau khi Chương 3 đối chiếu canonical pfSense block log, mới được quy thuộc thay đổi reachability cho rule pfSense.

## 7. Blocker E — Mô hình evidence bị đổi từ 5 lớp thành 3 tầng

Locked methodology yêu cầu phân biệt:
1. Reachability
2. Port & Service
3. Protocol State
4. Remote Vulnerability Signal
5. Local Patch State

Draft tự thay thành 3 tầng:
- Local System
- Network Communication
- Remote Signal

Cách gộp này làm mất chính luận điểm trung tâm của nghiên cứu: `445 open != SMBv1 != vulnerability`.

Khôi phục mô hình 5 lớp. Có thể vẽ hình quan hệ 5 lớp nhưng không thay đổi semantic model đã khóa.

## 8. Blocker F — Evidence IDs stale / không thuộc Stable Evidence Register

Draft dùng các mã như:
- `ENV-004`
- `SC1-001`
- `SC2-004`
- `DEC-09`
- `DEC-12`

Core Stable IDs hiện hành là:
- `ENV-CORE-01...07`
- `S1-RAW-01...05`, `S1-META-01`
- `S2-RAW-01...04`, `S2-META-01`
- `B-*`
- `C-*`

Không dùng stale IDs trong figure source notes.

## 9. Blocker G — Claim restore thực tế chưa có artifact

Draft ghi:
- sau mỗi can thiệp VM được restore về snapshot;
- mốc Before Demo “dùng để hoàn nguyên sau mỗi lượt”.

Current evidence chứng minh snapshot tồn tại và có vai trò recovery baseline, không chứng minh mọi restore event.

Phải viết theo design:
- snapshot cho phép/được dùng làm mốc phục hồi;
- không claim mỗi lượt đã restore nếu không có artifact.

## 10. Technical corrections khác

- Không gọi toàn bộ NSE category `vuln` là safe. Chỉ dùng exact canonical scripts.
- Không đưa actual Scenario 2 result vào Chương 2. Mục 2.5.2 phải mô tả rule đối chiếu remote/local, không kể baseline NSE04 actual result.
- Baseline signing local `EnableSecuritySignature=False / RequireSecuritySignature=False` chỉ giữ nếu có exact canonical evidence + source mapping; nếu không, chuyển signing thành đối tượng phép đo Scenario 2.
- Tránh các từ tuyệt đối như “cách ly hoàn toàn”, “ngăn chặn phát tán”, “quy kết chính xác”; dùng wording giới hạn theo cấu hình quan sát.
- Evidence/source note cho hình phải dùng Stable Evidence IDs hoặc nguồn VERIFIED thực.
- Source [11] Microsoft verification article có thể tiếp tục ở trạng thái PROPOSED, chưa tự sửa locked Source Ledger.

## 11. QA bắt buộc vòng corrective

Executor phải làm trong clone thật của:
`wrust0608/word-ppt-auto`

Phải chạy được:
- `uv run python scripts/validate_project.py`
- unit tests
- citation audit theo architecture hiện hành
- academic linter
- `git diff --check`

Sau commit:
- push branch thật;
- verify `git ls-remote origin feature/x5-chapter-2-structural-revision`;
- handoff remote SHA;
- external reviewer phải fetch được SHA đó qua GitHub connector.

## 12. Workflow state

- Approved structure remains LOCKED: **8 H2 / 27 H3**.
- X5 remains REOPENED.
- Candidate local draft is recoverable but NOT eligible for CP5-TECH.
- CP5-TECH new candidate = NOT YET.
- CP5-USER = PENDING.
- X6 = BLOCKED.
