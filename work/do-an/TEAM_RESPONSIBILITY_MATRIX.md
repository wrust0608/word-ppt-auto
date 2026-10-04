# TEAM RESPONSIBILITY MATRIX — X0

Trạng thái: `ROLE_STRUCTURE_DEFINED / MEMBER_ASSIGNMENT_PENDING_IF_NEEDED`

Mục tiêu của artifact này là xác định **trách nhiệm cần có**, không tự gán tên thành viên nếu chưa có quyết định phân công hiện hành.

| Role | Trách nhiệm | Không được tự làm |
|---|---|---|
| Final Approver | duyệt scope, outline, chương, publication, defense | không cần trực tiếp tạo mọi artifact |
| Lead Reviewer / QA | audit logic, source, evidence, rubric, chấm gate | không bịa dữ liệu hoặc tự đổi scope |
| Executor / Writing Agent | tạo artifact, draft, lint, QA kỹ thuật theo prompt | không tự PASS, không sửa truth matrix |
| Evidence Custodian | giữ cấu trúc evidence, ID, hash, provenance | không đổi raw output |
| Demo Operator | vận hành VM/demo theo runbook | không mở rộng mục tiêu ngoài lab |
| Chapter Owner | chịu trách nhiệm nội dung một chương | không bỏ qua cross-review |
| Cross Reviewer | kiểm chương không do mình sở hữu | không sửa ground truth |
| Defense Coordinator | slide/Q&A/rehearsal/member allocation | không tạo claim mới ngoài report |

## Yêu cầu trước X11
Trước defense phải gán thành viên thật cho:
- demo operator;
- Ch1 theory lead;
- Ch2 lab/method lead;
- Ch3 result lead;
- Ch4/risk lead;
- Q&A backup;
- evidence/rollback custodian.
