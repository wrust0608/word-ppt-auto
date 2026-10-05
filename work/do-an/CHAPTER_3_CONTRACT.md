# CHAPTER 3 CONTRACT — LOCKED_CANONICAL

Trạng thái: `LOCKED_WAITING_FOR_X6`

Question: Các phép đo canonical thực tế cho thấy gì về reachability, SMB protocol state, remote MS17-010 signal, patch ground truth và tác động của Case B/C?

Conclusion target: Baseline có 139/445 open, SMBv1 hiện diện và local state UNPATCHED nhưng remote NSE verdict UNKNOWN. Disable SMBv1 thay protocol surface mà không patch host; pfSense làm 139/445 filtered từ Kali mà không thay local patch state.

Main claims: X2-C03..X2-C11, X2-C13.

Mandatory rule: 100% result claims phải trace tới Evidence ID.

Exclude: Case A như canonical result; RCE/SYSTEM/Metasploit success; output từ historical report không có raw canonical; troubleshooting.

Required visuals: tổng 8–12 hình chính. Scenario 1 ưu tiên 2–3 hình; Scenario 2 2–3 hình; Case B khoảng 2 hình; Case C 3–4 hình. Raw/troubleshooting/ảnh lặp chuyển phụ lục. Summary matrix 1–2 bảng.

Target length: 4,500–6,000 words; chất lượng evidence quan trọng hơn số từ.
