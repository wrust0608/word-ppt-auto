# CHANGE CONTROL — X0

Trạng thái: `ACTIVE_GOVERNANCE_RULE`

## 1. Quyền thay đổi

- Người dùng: phê duyệt cuối đối với scope, outline, artifact LOCKED và chuyển gate.
- Reviewer/assistant: phát hiện conflict, đề xuất change, chấm PASS/REVISE/REJECT.
- Executor/agent: thực thi trong phạm vi đã giao; **không được tự đổi scope hoặc ground truth**.

## 2. Khi nào phải mở Change Request

- evidence mới làm thay đổi fact;
- GVHD/người dùng đổi yêu cầu;
- cần reopen artifact LOCKED;
- phát hiện mâu thuẫn đề cương ↔ report ↔ evidence;
- thêm/bỏ experiment;
- thay topology/platform/target;
- thay kết luận trung tâm;
- thay tiêu chí nghiệm thu.

## 3. Nội dung Change Request

1. Change ID.
2. Lý do.
3. Nguồn kích hoạt.
4. Artifact bị ảnh hưởng.
5. Evidence/RQ/rubric bị ảnh hưởng.
6. Risk.
7. Proposal.
8. Reviewer recommendation.
9. User decision.
10. Commit/version áp dụng.

## 4. Quy tắc

- Không xóa lịch sử để che conflict.
- Reopen LOCKED phải ghi rõ quyết định mới.
- Evidence mới không tự động trở thành canonical.
- Demo/rehearsal mới sau khi report khóa không được âm thầm thay canonical set.
- Nếu change làm thay đổi Ch3 fact, phải re-audit Ch3, Ch4, conclusion và slide.
