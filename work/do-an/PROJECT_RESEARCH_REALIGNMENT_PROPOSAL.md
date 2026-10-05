# PROJECT / RESEARCH REALIGNMENT PROPOSAL — X2

Trạng thái: PROPOSED_CHANGES_TO_LOCKED_ARTIFACTS

## PROJECT_PROFILE.md
Đề xuất:
1. Bỏ câu “tránh demo và kết quả demo”.
2. Khóa Oracle VirtualBox là platform canonical hiện hành; có thể ghi đề cương cho phép VMware/VirtualBox nhưng thực nghiệm sử dụng VirtualBox.
3. Giữ Metasploit trong đối tượng nghiên cứu/công cụ, thêm giới hạn: không có canonical exploitation result.
4. Thêm evidence canonical Scenario 1/2, Case B/C vào dữ liệu hiện có.
5. Thêm G7_DEFENSE vào deliverables/gates của project-level roadmap.

## RESEARCH_MAP.md
Đề xuất:
- RQ3: “Mô hình lab cô lập và quy trình kiểm thử nào cho phép phân biệt reachability, trạng thái giao thức, tín hiệu phát hiện và patch ground truth một cách có kiểm soát?”
- RQ4: thay “triệt tiêu nguy cơ” bằng “đánh giá hiệu quả và giới hạn các lớp giảm thiểu đối với reachability, protocol surface và patch state”.
- M3: dùng canonical Nmap/NSE + local Windows evidence; không còn chỉ thị tránh demo.
- M4: dùng before/after Case B/C + tài liệu hardening; patch Case A chỉ là proposal nếu chưa có evidence.
- Phạm vi: thêm demo canonical vào trong phạm vi; ngoài phạm vi gồm exploit/RCE thực tế nếu không có evidence.
- Tiêu chí: bổ sung 100% experimental claims traceable to evidence ID.

## ARGUMENT_MAP.md
Đề xuất supersede phần Ch2–4 bằng ARGUMENT_MAP_2_4_PROPOSED.md; không xóa lịch sử C001–C006.

## CLAIM_MATRIX.md
Đề xuất bổ sung X2-C01..X2-C15, không dùng nhãn “[CẦN DỮ LIỆU] toàn bộ lab” nữa; chỉ giữ thiếu dữ liệu cho Case A/performance/exploit.
