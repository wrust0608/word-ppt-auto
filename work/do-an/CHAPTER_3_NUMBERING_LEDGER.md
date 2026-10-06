# CHAPTER 3 NUMBERING LEDGER

Trạng thái: `ACTIVE_LOCK_LEDGER`
Date: 2026-10-06

Mục đích: khóa số Hình/Bảng giữa các section được viết độc lập.

## Current counters

- Next available table: **Bảng 3.6**
- Next available figure: **Hình 3.9**
- Approved numbering allocations: **4** (Sections 3.1–3.3 fully approved; Section 3.4 Case B presentation plan USER APPROVED / LOCKED)

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
| 3.1 Baseline | Bảng 3.1–3.2 | Hình 3.1–3.3 | X7A0 plan approval + X7A1 99/100 external PASS + user approval 2026-10-06 | 3.3 | 3.4 |

| 3.2 Scenario 1 | Bảng 3.3 | Hình 3.4–3.5 | X7B0 plan approval + X7B1 99/100 external PASS + user approval 2026-10-06 | 3.4 | 3.6 |

| 3.3 Scenario 2 | Bảng 3.4 | Hình 3.6 | X7C0 plan approval + X7C1 99/100 external PASS + user approval 2026-10-06 | 3.5 | 3.7 |

| 3.4 Case B | Bảng 3.5 | Hình 3.7–3.8 | X7D0 99/100 external PASS + user approval 2026-10-06; prose pending X7D1 after WR1/WR2 | 3.6 | 3.9 |
