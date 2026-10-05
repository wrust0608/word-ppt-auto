# NEGATIVE / INCONCLUSIVE RESULT POLICY — X1

Trạng thái: `ACTIVE_FOR_EXPERIMENTAL_WRITING`

## UNKNOWN
Dùng khi phép đo đã chạy nhưng dữ liệu không đủ để phân loại. Không được đổi thành SAFE, NOT VULNERABLE, VULNERABLE hay PATCHED.

## NO OUTPUT / NO USABLE SCRIPT RESULT
Mô tả hiện tượng công cụ. Không tự giải thích nguyên nhân nếu không có evidence.

## FILTERED
Cho phép kết luận đường truy cập từ vantage point hiện tại bị lọc. Không cho phép suy ra service local đã dừng, SMBv1 đã tắt, host đã vá hoặc lỗ hổng không tồn tại.

## TOOL FAILURE
Chỉ dùng khi có bằng chứng lỗi công cụ/execution. Tool failure khác UNKNOWN.

## CONFLICTING EVIDENCE
Nếu hai artifact cùng cấp mâu thuẫn, gắn conflict và dừng kết luận cho tới khi resolve.

## Retest
- Retest phải có lineage mới.
- Không ghi đè raw cũ.
- Differential mitigation phải phục hồi baseline trước khi đổi biến can thiệp độc lập.
- Kết quả retest chỉ thay canonical truth qua Change Control + reviewer approval.

## Canonical application
- Baseline NSE-SMB-04: UNKNOWN.
- Case B NSE-SMB-04: UNKNOWN.
- Case C: TCP 445 FILTERED từ Kali; không thể đánh giá MS17-010 qua đường quét đó.
- Local patch ground truth baseline: UNPATCHED; độc lập với remote verdict.
