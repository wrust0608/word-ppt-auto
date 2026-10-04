# ROADMAP BLUEPRINT — TOÀN BỘ ĐỀ MỤC CÔNG VIỆC CẦN LÀM

Trạng thái: `STRUCTURE_DRAFT / NOT_EXECUTABLE`  
Ngày: 2026-10-05  
Mục đích: dựng đầy đủ cấu trúc công việc của đồ án trước khi đánh giá, khóa thứ tự và bắt đầu thực thi.

> Tài liệu này KHÔNG cho phép agent bắt đầu viết chương, sửa artifact LOCKED, chạy lại demo, dựng DOCX hoặc chuyển gate. Bước tiếp theo sau khi blueprint hoàn chỉnh là **ROADMAP AUDIT**, không phải thực thi.

# A. THIẾT KẾ VÀ PHÊ DUYỆT ROADMAP

## A1. Xác định hệ thống nguồn có thẩm quyền
### A1.1. Yêu cầu trực tiếp hiện tại của người dùng
### A1.2. Quy định và mẫu HUIT
### A1.3. Đề cương chi tiết đã duyệt
### A1.4. Hai kịch bản demo của giảng viên
### A1.5. Evidence canonical từ demo
### A1.6. Quy tắc/quality gates của repo
### A1.7. Báo cáo cũ và artifact lịch sử
### A1.8. Quy tắc xử lý khi các nguồn mâu thuẫn

## A2. Xác định toàn bộ sản phẩm cuối phải bàn giao
### A2.1. Báo cáo Markdown nguồn
### A2.2. Báo cáo DOCX chính thức
### A2.3. Hình, bảng, sơ đồ
### A2.4. Tài liệu tham khảo IEEE
### A2.5. Phụ lục kỹ thuật
### A2.6. Evidence package
### A2.7. Slide bảo vệ
### A2.8. Q&A bank
### A2.9. Demo runbook và rollback plan
### A2.10. Hồ sơ QA/bàn giao

## A3. Dựng Work Breakdown Structure toàn đồ án
### A3.1. Governance
### A3.2. Research design
### A3.3. Source/evidence management
### A3.4. Report architecture
### A3.5. Chapter production
### A3.6. Cross-chapter synthesis
### A3.7. Publication
### A3.8. Defense

## A4. Dựng Dependency Map
### A4.1. Việc nào phải hoàn tất trước việc nào
### A4.2. Artifact nào là prerequisite
### A4.3. Gate nào cần người dùng duyệt
### A4.4. Việc nào có thể làm song song
### A4.5. Việc nào tuyệt đối không được làm sớm

## A5. Dựng Gate & Acceptance Criteria
### A5.1. Gate dữ liệu
### A5.2. Gate nguồn
### A5.3. Gate lập luận
### A5.4. Gate chương
### A5.5. Gate tổng hợp
### A5.6. Gate xuất bản
### A5.7. Gate bảo vệ

## A6. Dựng Risk Register cho quá trình hoàn thiện
### A6.1. Evidence conflict
### A6.2. Historical artifact contamination
### A6.3. Overclaim
### A6.4. Missing source
### A6.5. Missing canonical data
### A6.6. Scope creep
### A6.7. Citation drift
### A6.8. Figure overload
### A6.9. DOCX layout regression
### A6.10. Defense/demo failure

# B. ĐỐI SOÁT QUY ĐỊNH, MỤC TIÊU VÀ PHẠM VI

## B1. Quy định HUIT
### B1.1. Cấu trúc bắt buộc
### B1.2. Định dạng
### B1.3. Heading
### B1.4. Bảng/hình
### B1.5. Citation IEEE
### B1.6. Phụ lục
### B1.7. Yêu cầu bảo vệ

## B2. Đề cương chi tiết
### B2.1. Mục tiêu
### B2.2. Nội dung
### B2.3. CLO/rubric
### B2.4. Sản phẩm/bằng chứng
### B2.5. Thời gian/phân công
### B2.6. Công nghệ/công cụ bắt buộc hoặc đề xuất

## B3. Kiểm tra drift giữa đề cương và repo
### B3.1. Chỉ thị stale “tránh demo”
### B3.2. VirtualBox vs VMware
### B3.3. Windows Server 2012 R2 vs Windows 7
### B3.4. Host-Only vs topology 3 VLAN lịch sử
### B3.5. pfSense Case C vs Windows Firewall Case C cũ
### B3.6. Metasploit trong scope vs canonical demo
### B3.7. Case A patch lịch sử vs evidence hiện tại

## B4. Khóa phạm vi nghiên cứu hiện hành
### B4.1. Nội dung trong phạm vi
### B4.2. Nội dung ngoài phạm vi
### B4.3. Nội dung chỉ được đề xuất, không được nhận là đã thực nghiệm
### B4.4. Ranh giới an toàn/đạo đức

# C. QUẢN TRỊ NGUỒN VÀ LIÊM CHÍNH HỌC THUẬT

## C1. Source Ledger
### C1.1. Microsoft
### C1.2. Nmap
### C1.3. NIST
### C1.4. NVD
### C1.5. Rapid7/Metasploit
### C1.6. Tài liệu học thuật bổ sung
### C1.7. Nguồn HUIT/quy định

## C2. Source Reconciliation
### C2.1. Nguồn verified
### C2.2. Nguồn recheck
### C2.3. Nguồn thay thế
### C2.4. Metadata
### C2.5. Citation location

## C3. Claim Integrity
### C3.1. SOURCE_FACT
### C3.2. AUTHOR_DATA
### C3.3. INTERPRETATION
### C3.4. PROPOSAL
### C3.5. COMMON_KNOWLEDGE

## C4. Citation Governance
### C4.1. IEEE toàn văn
### C4.2. Thứ tự first appearance
### C4.3. Citation-to-source trace
### C4.4. Không source orphan
### C4.5. Không citation orphan
### C4.6. Không dùng NotebookLM như nguồn trích dẫn

# D. QUẢN TRỊ TOÀN BỘ EVIDENCE DEMO

## D1. Environment/Baseline Evidence
### D1.1. VirtualBox
### D1.2. Kali
### D1.3. Windows Server 2012 R2
### D1.4. IP/NIC
### D1.5. Host-Only
### D1.6. SMB service
### D1.7. Windows Firewall preparation
### D1.8. Nmap/NSE
### D1.9. Patch/srv.sys baseline
### D1.10. Snapshot Before Demo

## D2. Scenario 1 Evidence
### D2.1. Kali network configuration
### D2.2. Host discovery
### D2.3. Target discovery/reachability
### D2.4. TCP 139/445
### D2.5. Service/version detection
### D2.6. SMB NSE enumeration
### D2.7. Raw output set
### D2.8. Scenario 1 conclusion boundary

## D3. Scenario 2 Evidence
### D3.1. NSE-SMB-01 ports
### D3.2. NSE-SMB-02 protocols
### D3.3. NSE-SMB-03 signing
### D3.4. NSE-SMB-04 MS17-010
### D3.5. Local patch ground truth
### D3.6. Remote verdict UNKNOWN
### D3.7. Scenario 2 conclusion boundary

## D4. Case B Evidence — Disable SMBv1
### D4.1. Before state
### D4.2. Intervention
### D4.3. After local state
### D4.4. Protocol retest
### D4.5. MS17-010 retest
### D4.6. Patch state unchanged
### D4.7. Differential conclusion

## D5. Case C Evidence — pfSense
### D5.1. pfSense topology
### D5.2. Transparent Bridge
### D5.3. Baseline pass behavior
### D5.4. Block rule
### D5.5. Rule ordering
### D5.6. Port retest
### D5.7. Firewall block log
### D5.8. MS17-010 retest
### D5.9. Windows local state unchanged
### D5.10. Differential conclusion

## D6. Historical/Non-canonical Evidence
### D6.1. Báo cáo demo cũ
### D6.2. Case A patch cũ
### D6.3. Windows Firewall Case C cũ
### D6.4. Old snapshot lineage
### D6.5. Windows 7 / 3 VLAN artifacts
### D6.6. Metasploit/exploit artifacts nếu có
### D6.7. Điều kiện phục hồi một artifact lịch sử thành canonical

## D7. Evidence Register
### D7.1. Evidence ID
### D7.2. Path
### D7.3. Type
### D7.4. Timestamp
### D7.5. Scenario
### D7.6. Supported claim
### D7.7. Forbidden inference
### D7.8. Canonical classification

## D8. Evidence QA
### D8.1. Raw vs screenshot
### D8.2. Raw vs manifest
### D8.3. Summary vs raw
### D8.4. Conflict report
### D8.5. SHA-256 canonical manifest
### D8.6. Secret/privacy scan

# E. THIẾT KẾ NGHIÊN CỨU VÀ LẬP LUẬN TOÀN CÔNG TRÌNH

## E1. Research Questions
### E1.1. RQ1 SMB architecture/security
### E1.2. RQ2 MS17-010 mechanism
### E1.3. RQ3 lab/detection methodology
### E1.4. RQ4 mitigation/evaluation

## E2. Objectives
### E2.1. O1
### E2.2. O2
### E2.3. O3
### E2.4. O4
### E2.5. RQ↔O consistency

## E3. Methodology
### E3.1. Literature analysis
### E3.2. Lab design
### E3.3. Controlled security testing
### E3.4. Differential before/after testing
### E3.5. Risk/mitigation analysis
### E3.6. Limitations

## E4. Central Argument
### E4.1. Port reachability
### E4.2. Protocol availability
### E4.3. Remote vulnerability signal
### E4.4. Local patch ground truth
### E4.5. Protocol mitigation
### E4.6. Network mitigation
### E4.7. Defense in depth
### E4.8. Residual risk

## E5. Claim Matrix
### E5.1. Theory claims
### E5.2. Environment claims
### E5.3. Experimental claims
### E5.4. Comparative claims
### E5.5. Recommendations
### E5.6. Limitations

# F. KIẾN TRÚC TOÀN BỘ BÁO CÁO

## F1. Phần đầu
### F1.1. Bìa/phụ bìa
### F1.2. Nhiệm vụ đề tài
### F1.3. Cam đoan
### F1.4. Cảm ơn
### F1.5. Tóm tắt tiếng Việt
### F1.6. Abstract
### F1.7. Mục lục
### F1.8. Danh mục từ viết tắt
### F1.9. Danh mục bảng
### F1.10. Danh mục hình

## F2. Mở đầu
### F2.1. Lý do chọn đề tài
### F2.2. Vấn đề nghiên cứu
### F2.3. Mục tiêu
### F2.4. Đối tượng/phạm vi
### F2.5. Phương pháp
### F2.6. Đóng góp
### F2.7. Cấu trúc báo cáo

## F3. Chương 1 — Cơ sở lý thuyết và công cụ
### F3.1. SMB architecture/protocol
### F3.2. Ports 139/445
### F3.3. SMBv1/v2/v3
### F3.4. SMB security/signing
### F3.5. MS17-010/CVE/EternalBlue
### F3.6. Cơ chế lỗi
### F3.7. Nmap/NSE
### F3.8. Firewall/pfSense/mitigation concepts
### F3.9. Tiêu chí phân tầng kết luận
### F3.10. Tổng kết

## F4. Chương 2 — Thiết kế và triển khai mô hình thực nghiệm
### F4.1. Yêu cầu thiết kế
### F4.2. Kiến trúc lab
### F4.3. Thành phần môi trường
### F4.4. Cấu hình mạng
### F4.5. SMB/Firewall/Patch baseline
### F4.6. Tool readiness
### F4.7. Snapshot/recovery
### F4.8. Thiết kế Scenario 1
### F4.9. Thiết kế Scenario 2
### F4.10. Thiết kế Case B
### F4.11. Thiết kế Case C
### F4.12. Thu thập/bảo toàn evidence
### F4.13. Tiêu chí đánh giá
### F4.14. Tổng kết

## F5. Chương 3 — Thực nghiệm và kết quả
### F5.1. Pre-test verification
### F5.2. Scenario 1
### F5.3. Scenario 2
### F5.4. Local patch-ground-truth reconciliation
### F5.5. Case B
### F5.6. Case C
### F5.7. Bảng kết quả tổng hợp
### F5.8. Negative/UNKNOWN observations
### F5.9. Inference boundaries
### F5.10. Tổng kết

## F6. Chương 4 — Đánh giá, rủi ro và khuyến nghị
### F6.1. Cross-case comparison
### F6.2. Reachability vs protocol vs vulnerability vs patch state
### F6.3. Hiệu quả disable SMBv1
### F6.4. Hiệu quả pfSense filtering
### F6.5. Vai trò patching
### F6.6. Defense-in-depth
### F6.7. Residual risk
### F6.8. Threats to validity
### F6.9. Operational/compatibility considerations
### F6.10. Khuyến nghị
### F6.11. Hướng phát triển
### F6.12. Tổng kết

## F7. Kết luận và kiến nghị
### F7.1. Trả lời RQ
### F7.2. Mức đạt mục tiêu
### F7.3. Đóng góp
### F7.4. Giới hạn
### F7.5. Kiến nghị/hướng tiếp theo

## F8. Tài liệu tham khảo

## F9. Phụ lục
### F9.1. Command/runbook
### F9.2. Raw output chọn lọc
### F9.3. Evidence index
### F9.4. Cấu hình
### F9.5. Troubleshooting nếu cần
### F9.6. Extra screenshots
### F9.7. Hash manifest

# G. HỢP ĐỒNG VÀ EVIDENCE MAP CHO TỪNG CHƯƠNG

## G1. Chapter 1 contract
## G2. Chapter 2 contract
## G3. Chapter 3 contract
## G4. Chapter 4 contract
## G5. Mỗi heading: question/claim/evidence/source/limit/budget
## G6. Figure/table plan
## G7. Appendix placement plan

# H. SẢN XUẤT VÀ REVIEW CHƯƠNG 1

## H1. Source reconciliation
## H2. Technical correctness
## H3. Logic/depth
## H4. Duplication pruning
## H5. Style/author voice
## H6. Citation audit
## H7. Chapter review
## H8. User approval

# I. SẢN XUẤT VÀ REVIEW CHƯƠNG 2

## I1. Draft
## I2. Evidence verification
## I3. Reproducibility review
## I4. Method/result separation
## I5. Figure/table review
## I6. Source/citation review
## I7. Logic/style review
## I8. User approval

# J. SẢN XUẤT VÀ REVIEW CHƯƠNG 3

## J1. Scenario 1 write-up
## J2. Scenario 2 write-up
## J3. Patch-ground-truth section
## J4. Case B write-up
## J5. Case C write-up
## J6. Summary matrix
## J7. 100% experimental claim trace
## J8. Raw/prose consistency audit
## J9. Negative result audit
## J10. Figure selection
## J11. User approval

# K. SẢN XUẤT VÀ REVIEW CHƯƠNG 4

## K1. Comparison framework
## K2. Mitigation-layer analysis
## K3. Risk assessment
## K4. Residual risk
## K5. Limitations/threats to validity
## K6. Recommendations
## K7. RQ4 answer
## K8. Source/claim review
## K9. User approval

# L. TỔNG HỢP TOÀN VĂN — G5

## L1. RQ answer matrix
## L2. Objective completion matrix
## L3. Introduction↔Conclusion consistency
## L4. Cross-chapter terminology
## L5. Cross-chapter data consistency
## L6. Global IEEE renumbering
## L7. Citation/reference audit
## L8. Figure/table cross-reference
## L9. Acronym consistency
## L10. Word-budget/anti-rambling pass
## L11. Academic-register review
## L12. Publication lint
## L13. User approval

# M. HÌNH, BẢNG VÀ PHỤ LỤC

## M1. Topology figure
## M2. Experimental flow figure
## M3. Scenario comparison table
## M4. Defense-layer comparison table
## M5. Evidence-to-claim table
## M6. Captions and source notes
## M7. Image quality/cropping
## M8. Appendix evidence selection
## M9. Remove redundant/troubleshooting visuals from main body

# N. XUẤT BẢN DOCX — G6

## N1. Lock Markdown
## N2. Apply HUIT formatting
## N3. Auto TOC
## N4. List of figures/tables
## N5. Heading numbering
## N6. Page numbering/section breaks
## N7. Tables/images/equations
## N8. IEEE bibliography
## N9. OpenXML/OfficeCLI validation
## N10. Render all pages
## N11. Page-by-page visual audit
## N12. Repair/regenerate loop
## N13. Final publication checklist
## N14. User approval

# O. HỒ SƠ BẢO VỆ — G7

## O1. Slide architecture
## O2. Research problem
## O3. Theory summary
## O4. Lab topology
## O5. Scenario 1
## O6. Scenario 2
## O7. Case B
## O8. Case C
## O9. Comparison
## O10. Limitations
## O11. Recommendations/conclusion
## O12. Q&A bank
## O13. Evidence quick index
## O14. Demo runbook
## O15. Snapshot/rollback plan
## O16. Demo rehearsal
## O17. Failure-mode plan
## O18. Member role allocation

# P. BÀN GIAO VÀ LƯU TRỮ

## P1. Final report package
## P2. Evidence package
## P3. Source/ledger package
## P4. Slide package
## P5. Demo/runbook package
## P6. QA reports
## P7. Version/commit identification
## P8. Secret/privacy final scan
## P9. Final archive manifest

# Q. VÒNG AUDIT ROADMAP TRƯỚC KHI THỰC THI

Sau khi A–P được xác nhận là đầy đủ, reviewer phải audit blueprint theo các tiêu chí sau.

## Q1. Coverage audit
- Mọi yêu cầu HUIT có nơi xử lý.
- Mọi mục tiêu/RQ có work item.
- Mọi nhóm evidence có work item.
- Mọi deliverable có owner/gate.
- Không có phần quan trọng chỉ “ngầm hiểu”.

## Q2. Logic/dependency audit
- Không viết trước khi evidence/contract sẵn sàng.
- Không xuất DOCX trước synthesis.
- Không làm defense từ nội dung chưa khóa.
- Không dùng artifact historical như canonical.

## Q3. Demo/evidence audit
- Scenario 1/2 và Case B/C có tuyến riêng.
- UNKNOWN/negative result được quản trị.
- Case A không bị tự động biến thành kết quả.
- Troubleshooting không lẫn evidence canonical.

## Q4. Academic audit
- Phân biệt source fact/author data/interpretation/proposal.
- RQ/O/method/results/conclusion khớp.
- Không overclaim.
- Có limitations và residual risk.

## Q5. Workload audit
- Workload demo được phản ánh đủ.
- Chương 3 và evidence QA nhận ưu tiên cao nhất.
- Word formatting không lấn át workstream học thuật.
- Có defense preparation.

## Q6. Roadmap score
Chỉ kích hoạt roadmap nếu đạt:
- Coverage >= 95/100
- Logic/dependencies >= 90/100
- Demo/evidence control >= 95/100
- Academic integrity >= 95/100
- HUIT compliance >= 95/100
- Không có BLOCKER.

Nếu chưa đạt: sửa blueprint và audit lại. Không bắt đầu execution.

# R. TRẠNG THÁI HIỆN TẠI

- A–P: mới là cấu trúc công việc đề xuất.
- Q: chưa audit chính thức.
- Không có phase thực thi nào được kích hoạt.
- `EXPERIMENTAL_TRUTH_MATRIX.md` đã tồn tại và được xem là đầu vào cho D/E/G, nhưng không có nghĩa các phase đó đã hoàn thành.
- Bước tiếp theo duy nhất: **review + audit ROADMAP BLUEPRINT**, sau đó mới khóa roadmap thực thi.
