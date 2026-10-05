# CHAPTER 2 CONTRACT — LOCKED_CANONICAL

Trạng thái: `APPROVED_FOR_DRAFTING_2026_10_05`

Question: Lab và quy trình kiểm thử được thiết kế thế nào để an toàn, tái lập, truy vết và đủ sức phân biệt các lớp bằng chứng SMB/MS17-010?

Conclusion target: Canonical lab sử dụng VirtualBox Host-Only với Kali và Windows Server 2012 R2, snapshot Before Demo, baseline SMB/patch rõ và hai kịch bản đo được thiết kế theo các lớp evidence riêng; Case B/C dùng differential testing với baseline phục hồi.

Main claims: X2-C01, X2-C02 + phương pháp A21/A22/A23.

Exclude: kết quả chi tiết scan; historical Windows 7/3 VLAN; troubleshooting diary; exploit result.

Required figures/tables: topology 1; environment table 1; scenario flow 1; evidence-layer table 1.

Target length: 3,500–4,500 words; vượt 15% phải review.
