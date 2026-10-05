# EVIDENCE CONFLICT REPORT — X1

Trạng thái: `X1_REVIEW_PENDING`
Ngày: 2026-10-05

| ID | Mâu thuẫn | Nguồn lịch sử/thấp hơn | Nguồn canonical | Quyết định |
|---|---|---|---|---|
| CF-01 | Baseline NSE-MS17-010 bị mô tả là `VULNERABLE` | báo cáo demo cũ | Scenario 2 raw `NSE-SMB-04_ms17010.*` | Canonical verdict = `UNKNOWN / NO USABLE SCRIPT RESULT` |
| CF-02 | Báo cáo cũ nêu `STATUS_INSUFF_SERVER_RESOURCES` | historical report | canonical raw không có Host script result | Cấm dùng NTSTATUS này cho canonical run |
| CF-03 | Case B cũ mô tả lỗi thương lượng SMBv1 cụ thể | historical report | Case B raw không có usable verdict | Giữ `UNKNOWN`; không bịa error string |
| CF-04 | Case C cũ dùng Windows Firewall | historical report | pfSense canonical setup/rules/log/raw | Canonical Case C = pfSense Transparent Bridge |
| CF-05 | Case A patch được mô tả đã hoàn tất | historical report | không có canonical Case A directory trong ALL.zip | `HISTORICAL_ONLY` |
| CF-06 | Old topology Windows 7 + 3 VLAN + client control | old repo artifacts | canonical Environment/PreDemo | Dùng Windows Server 2012 R2 + Kali + Host-Only baseline |
| CF-07 | Old snapshot names | old report/state | `Before_Demo_Snapshots.txt` | Canonical snapshot = `Before Demo` |
| CF-08 | pfSense port screenshot duplicate | `pfSense_CaseC_09_NSE01_Ports.png` | `..._CANONICAL.png` + raw | Bản không `_CANONICAL` bị loại |
| CF-09 | `filtered = safe/patched` | prose risk | pfSense raw + Windows local state | Chỉ kết luận reachability từ Kali bị lọc |
| CF-10 | `SMBv1 disabled = patched` | prose risk | Case B local state + patch baseline | Cấm; patch state không đổi |

Nếu phục hồi evidence Case A hoặc chạy lại demo sinh kết quả mới, phải mở Change Request và audit lineage trước khi thay canonical truth.
