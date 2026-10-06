# CHAPTER 3 NUMBERING LEDGER

Trạng thái: `ACTIVE_LOCK_LEDGER`
Date: 2026-10-06

Mục đích: khóa số Hình/Bảng giữa các section được viết độc lập.

## Current counters

- Next available table: **Bảng 3.3**
- Next available figure: **Hình 3.4**
- Approved numbering allocations: **1** (Section 3.1 presentation plan approved; prose pending)

## Lock rules

1. Evidence/presentation plan có thể đề xuất số tạm.
2. Chỉ sau **external review + user approval** mới ghi số chính thức vào ledger.
3. Section kế tiếp lấy counter từ HEAD của `feature/ch3-integration`.
4. Không renumber section đã approved nếu không có explicit reopen.
5. Khi bỏ một figure/table trước approval, counter chưa bị tiêu thụ.
6. Khi assembly, số đã khóa phải được giữ nguyên.

## Approved ranges

| Section | Tables locked | Figures locked | Approval reference | Next table | Next figure |
|---|---|---|---|---|---|
| 3.1 Baseline | Bảng 3.1–3.2 | Hình 3.1–3.3 | X7A0 external PASS + user approval 2026-10-06; prose pending X7A1 | 3.3 | 3.4 |
