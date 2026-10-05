# Sổ nguồn

Trạng thái hợp lệ: `CANDIDATE`, `INGESTED`, `VERIFIED`, `REJECTED`, `RECHECK`.

| Source ID | Trạng thái | Tác giả/cơ quan | Năm | Tiêu đề | Loại | DOI/URL | Notebook | Vị trí bằng chứng | Chất lượng | Dùng cho |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | RECHECK | Andrew S. Tanenbaum et al. | 2021 | Computer Networks (6th ed.) | Textbook | Pearson | NO | Chưa nhập bản toàn văn vào notebook | Cao | Chỉ được dùng lại sau khi tác giả cung cấp bản được phép sử dụng và vị trí trang |
| S002 | VERIFIED | Microsoft Learn | 2026 | Direct hosting of SMB over TCP/IP | Tech Doc | https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip | YES | Summary: hai phương thức được thử khi đều bật; More information: 4-byte header, port 139/445; không hỗ trợ chi tiết RST | Cao | [2] Cơ chế phân định cổng TCP 139 (NBT) và 445 (Direct-hosted SMB) |
| S003 | RECHECK | Pavel Yosifovich et al. | 2017 | Windows Internals, Part 1 (7th ed.) | Textbook | Microsoft Press | NO | Chưa nhập bản toàn văn vào notebook | Cao | Chỉ được dùng lại sau khi xác minh bản sách và vị trí trang |
| S004 | RECHECK | Andrea Allievi et al. | 2021 | Windows Internals, Part 2 (7th ed.) | Textbook | Microsoft Press | NO | Chưa nhập bản toàn văn vào notebook | Cao | Chỉ được dùng lại sau khi xác minh bản sách và vị trí trang |
| S005 | VERIFIED | Microsoft | 2017 | Microsoft Security Bulletin MS17-010 – Critical | Official Bulletin | https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010 | YES | Danh mục 6 CVE, ma trận KB theo hệ điều hành Windows | Cao | [5] Định danh bulletin MS17-010, ma trận bản vá KB chính thức |
| S006 | VERIFIED | Microsoft Learn | 2025 | What is SMB File Sharing for Windows and Windows Server? | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview | YES | Usage; SMB features; SMB components; SMB dialects | Cao | Đặc tính SMB, vai trò client/server và bảng dialect hiện hành; thay URL cũ không nhập được |
| S007 | VERIFIED | Microsoft Learn | 2025 | SMB security enhancements | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security | YES | AES-128-CCM/GCM, AES-CMAC/GMAC, Pre-auth Integrity SHA-512 | Cao | [7] Chi tiết các cơ chế an ninh, thuật toán mã hóa/ký số của SMBv3 |
| S008 | VERIFIED | Microsoft Learn | 2025 | Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3 | YES | Thủ tục PowerShell, Registry, GPO bật/tắt SMB | Cao | [8] Hướng dẫn vô hiệu hóa SMBv1 và quản lý cấu hình giao thức |
| S009 | RECHECK | Chris McNab | 2016 | Network Security Assessment (3rd ed.) | Book | O'Reilly Media | NO | Chưa nhập bản toàn văn vào notebook | Cao | Không dùng cho claim mới cho tới khi có bản được phép và vị trí trang; thay bằng S025 cho chính sách tường lửa |
| S010 | VERIFIED | Microsoft Security Response Center (MSRC) | 2017 | Eternal Synergy Exploit Analysis | Tech Analysis | https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/ | YES | Phân tích cơ chế exploit CVE-2017-0143 | Cao | [10] Ánh xạ chính thức CVE-2017-0143 với EternalSynergy |
| S011 | VERIFIED | NIST | 2017 | CVE-2017-0144 Detail | Vulnerability DB | https://nvd.nist.gov/vuln/detail/CVE-2017-0144 | YES | CVSS score, CWE-119, thông số kỹ thuật lỗ hổng | Cao | [11] Định danh lỗ hổng CVE-2017-0144 (không dùng ngoài phạm vi) |
| S012 | VERIFIED | Microsoft Threat Intelligence | 2017 | New ransomware, old techniques: Petya adds-worm capabilities | Threat Report | https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/ | YES | Phân tích Petya/NotPetya, CVE-2017-0145 EternalRomance | Cao | [12] Ánh xạ CVE-2017-0145 với EternalRomance và mã độc NotPetya |
| S013 | VERIFIED | Rapid7 | 2017 | MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption | Exploit DB | https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/ | YES | Phân tích SrvOs2FeaToNt, pool grooming, module Metasploit | Cao | [13] Cơ chế kỹ thuật FEA root cause và rủi ro BSOD khi khai thác |
| S014 | RECHECK | Cybersecurity and Infrastructure Security Agency (CISA) | 2017 | Alert (TA17-132A): Indicators Associated With WannaCry Ransomware | Technical Alert | https://www.cisa.gov/news-events/alerts/2017/05/12/indicators-associated-wannacry-ransomware | ERROR | URL hiện không được NotebookLM nhập; cần tìm bản lưu trữ chính thức hoặc PDF tương đương | Cao | Không dùng cho claim mới cho tới khi khôi phục nguồn |
| S015 | VERIFIED | Microsoft Threat Intelligence | 2017 | WannaCrypt ransomware worm targets out-of-date systems | Threat Report | https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/ | YES | Lây lan qua SMB trên máy chưa vá; hướng dẫn cập nhật và hạn chế kết nối | Cao | Cơ chế lây lan và hướng dẫn phòng vệ; không dùng số liệu 150 quốc gia chưa đối chiếu |
| S016 | RECHECK | Georgia Weidman | 2014 | Penetration Testing: A Hands-On Introduction to Hacking | Book | No Starch Press | NO | Chưa nhập bản toàn văn vào notebook | Cao | Không dùng cho claim mới; dùng S024 cho quy trình kiểm thử có kiểm soát |
| S017 | VERIFIED | Gordon Lyon | 2009 | Nmap Network Scanning: The Official Nmap Project Guide | Book | Insecure.Com LLC / https://nmap.org/book/ | YES | Port Scanning, -sS, -sV, -O, Scripting Engine | Cao | [17] Cơ sở lý thuyết quét cổng, phân biệt -sV và -O |
| S018 | VERIFIED | Paulino Calderon & Nmap Project | 2017 | smb-vuln-ms17-010.nse Script Source Code | Source Code | https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse | YES | Mã nguồn NSE: opcode 0x25, PeekNamedPipe 0x2300, 0xC0000205 | Cao | [18] Bằng chứng mã nguồn trực tiếp cho logic nhận diện của Nmap NSE |
| S019 | RECHECK | David Kennedy et al. | 2024 | Metasploit: The Penetration Tester's Guide (2nd ed.) | Book | No Starch Press | NO | Chưa nhập bản toàn văn vào notebook | Cao | Không dùng cho claim mới; thông tin module hiện dùng S013 và tài liệu gốc công cụ |
| S020 | VERIFIED | Microsoft Learn | 2025 | What is Microsoft SMB Protocol and CIFS Protocol? | Tech Doc | https://learn.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview | YES | Overview; dialect; file, print, authentication functions | Cao | Khái niệm SMB/CIFS và phạm vi chức năng giao thức |
| S021 | VERIFIED | Microsoft Open Specifications | 2026 | [MS-SMB]: Server Message Block (SMB) Protocol | Protocol Specification | https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb/f210069c-7086-4dc2-885e-861d837df688 | YES | Published specification and protocol behavior | Rất cao | Đặc tả sơ cấp cho SMBv1/CIFS và cấu trúc bản tin |
| S022 | VERIFIED | Microsoft Open Specifications | 2026 | [MS-SMB2]: Server Message Block (SMB) Protocol Versions 2 and 3 | Protocol Specification | https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/ | YES | Published version; SMB 2/3 behavior | Rất cao | Đặc tả sơ cấp cho SMBv2/v3, dialect negotiation và message flow |
| S023 | VERIFIED | Microsoft Learn | 2024 | What is Server Message Block signing? | Tech Doc | https://learn.microsoft.com/windows-server/storage/file-server/smb-signing-overview | YES | Signing behavior, requirements and compatibility | Cao | SMB Signing, điều kiện triển khai và giới hạn tương thích |
| S024 | VERIFIED | K. Scarfone et al., NIST | 2008 | SP 800-115: Technical Guide to Information Security Testing and Assessment | Standard/Guide | https://csrc.nist.gov/pubs/sp/800/115/final | YES | Planning; conducting tests; analyzing findings; mitigation | Rất cao | Phạm vi ủy quyền, lập kế hoạch kiểm thử, kiểm soát tác động và báo cáo kết quả |
| S025 | VERIFIED | K. Scarfone and P. Hoffman, NIST | 2009 | SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy | Standard/Guide | https://csrc.nist.gov/pubs/sp/800/41/r1/final | YES | Firewall policy; selection; configuration; testing and management | Rất cao | Chính sách cổng, phân đoạn và kiểm thử hiệu lực tường lửa |
| S026 | VERIFIED | Kali Linux Project | n.d. | What is Kali Linux? | Official Documentation | https://www.kali.org/docs/introduction/what-is-kali-linux/ | YES | About Kali Linux; penetration testing and security auditing focus | Cao | Mô tả Kali Linux và lý do sử dụng làm trạm kiểm thử |
| S027 | VERIFIED | Rapid7 | n.d. | Metasploit Framework | Official Documentation | https://docs.rapid7.com/metasploit/msf-overview/ | NO | Metasploit Framework; Finding Modules; phân loại Exploit/Auxiliary/Payload; đọc gốc ngày 2026-10-04 | Cao | Mô tả nền tảng và vai trò module; xác minh tương đương qua nguồn gốc, chưa nhập notebook |
| S028 | VERIFIED | Microsoft | n.d. | MS-CIFS: Per SMB Session; Receiving a Tree Connect Response | Protocol Specification | https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c42729fb-c655-424f-8d9a-44825d609b86; https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cifs/c7cb45aa-f923-4cd4-a9d5-4a1418e41d42 | NO | UID trong Session Setup response; TID và quan hệ với UID ở mục 3.2.5.4; đọc gốc ngày 2026-10-04 | Cao | Định danh phiên/tài nguyên SMBv1; xác minh tương đương, chưa nhập notebook |

| S029 | VERIFIED | Paulino Calderon / Nmap Project | n.d. | smb-protocols.nse Script Source Code | Source Code | https://svn.nmap.org/nmap/scripts/smb-protocols.nse | NO | description; action gọi smb.list_dialects; nhánh không có phiên bản được chấp nhận; đọc gốc 2026-10-04 | Cao | Phép nhận diện phiên bản và giới hạn khi không có output; xác minh tương đương, chưa nhập notebook |
| S030 | VERIFIED | Rapid7 | n.d. | MS17-010 SMB RCE Detection | Source Code | https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/smb/smb_ms17_010.rb | NO | Description; run_host; do_smb_setup_tree; do_smb_ms17_010_probe; đọc gốc 2026-10-04 | Cao | Scanner dùng cùng dấu hiệu IPC$/FID 0, các nhánh phản hồi/lỗi và tùy chọn bổ sung; chưa nhập notebook |

| S031 | VERIFIED | Microsoft | n.d. | SMB 3.1.1 Pre-authentication integrity in Windows 10 | Archived official technical article | https://learn.microsoft.com/en-us/archive/blogs/openspecification/smb-3-1-1-pre-authentication-integrity-in-windows-10 | NO | Summary; Overview; Pre-auth integrity hash, SHA-512; guest/anonymous exception; đọc gốc 2026-10-04 | Cao | Giải thích giá trị băm trong tạo khóa và giới hạn phiên; chưa nhập notebook |

| S032 | VERIFIED | Microsoft Support | 2017 | How to verify that MS17-010 is installed | Official Support / Verification Guide | https://support.microsoft.com/en-us/security/how-to-verify-that-ms17-010-is-installed | NO | Method 1 + Method 2: Windows 8.1 / Windows Server 2012 R2; KB4012213/KB4012216; minimum updated srv.sys 6.3.9600.18604; PowerShell/file-version verification | Rất cao | Xác minh MS17-010 bằng KB/file version; ngưỡng srv.sys cho Windows Server 2012 R2 |

## Nguồn bị loại

| Source ID | Lý do loại | Luận điểm bị ảnh hưởng |
|---|---|---|
| M. E. Aminanto et al. (IEEE Access 2019) | Chưa xác minh được bản ghi độc lập công khai (DOI/record); nội dung bài báo deep learning không trực tiếp hỗ trợ cho bối cảnh lây lan WannaCry. Đã thay bằng nguồn chính thức CISA [14] và Microsoft Threat Intelligence [15]. | Bối cảnh lây lan WannaCry diện rộng |

## Kiểm tra đồng bộ NotebookLM ngày 2026-10-04

- MCP và phiên đăng nhập: `PASS`.
- Notebook kiểm tra: lấy từ cấu hình cục bộ; không lưu ID riêng tư trong Git.
- Trạng thái ban đầu: 0 nguồn, trái với cột `Notebook=YES` trước khi audit.
- Đã nhập thành công 19 nguồn công khai; hai URL cũ hiển thị lỗi nhập là URL cũ của S006 và S014.
- Smoke test sau nhập nguồn: NotebookLM xác định Direct-hosted SMB dùng TCP 445, trỏ đúng tài liệu Microsoft Learn và không suy diễn cổng mở thành tồn tại MS17-010.
- Các sách chưa có bản toàn văn trong notebook được chuyển `RECHECK/NO`; không được dùng cho claim mới cho tới khi có bản hợp lệ và vị trí trang.

## Danh sách truy vấn còn thiếu

| ID | Thông tin cần tìm | Luận điểm liên quan | Mức ưu tiên | Trạng thái |
|---|---|---|---|---|
| Q001 | Chi tiết mã lỗi buffer overflow/heap grooming trong srv.sys cho CVE-2017-0144 | Cơ chế lỗ hổng mức nhân của MS17-010 | Cao | REOPENED_RECHECK (S003 chưa khả dụng; kiểm tra chi tiết từ S013/S005, không dùng bulletin làm nguồn cho toàn bộ root cause) |
| Q002 | Khuyến nghị hardening SMB từ CIS Benchmark và Microsoft Security Baseline | Khuyến nghị phòng thủ đa tầng | Trung bình | REOPENED_RECHECK (S009 chưa khả dụng; Microsoft/NIST không tự đáp ứng yêu cầu CIS Benchmark/Security Baseline; kiểm lại phạm vi hoặc ghi chưa đủ nguồn) |

## Metadata đối chiếu nguồn gốc ngày 2026-10-04

S006: Last updated 2025-11-27; S020: Last updated 2025-07-10. Đã sửa năm 2026 sang năm cập nhật 2025, không coi năm truy cập là năm xuất bản. Xem SOURCE_RECONCILIATION_PLAN.md cho vị trí và giới hạn hỗ trợ. Chưa tái kiểm tra NotebookLM trong phiên này.

## Đối chiếu cho lượt tăng chiều sâu 2026-10-04

S007: ngày cập nhật hiển thị 2025-07-01; dùng các mục SMB Encryption, Prerequisites, Considerations và Preauthentication integrity. Giới hạn hạ cấp ở tài liệu phải giữ: bảo vệ SMB 3.1.1 xuống 2.x không đồng nghĩa với bảo vệ xuống 1.0. S023: tiêu đề hiện hành “What is Server Message Block signing?”, ngày cập nhật 2024-10-25; dùng How signing works, không áp mặc định hệ thống hiện đại cho Windows 7.

S013: Description, quan hệ SrvOs2FeaListSizeToNt → SrvOs2FeaToNt/memmove và chuyển hướng tại srvnet; nguồn không chứng minh output SYSTEM là quan sát trực tiếp Kernel Mode. S017: phần TCP SYN (Stealth) Scan, bảng 5.2 và giải thích thiếu phản hồi. S018: check_ms17010 và action; phân biệt phản hồi của Transaction với thất bại trước đó. S022: ví dụ 4.3, các bước xác thực nhiều lượt và trạng thái MORE_PROCESSING_REQUIRED. S025: SP 800-41 Rev.1, mục 2.1.2, trang in 2-4, bảng trạng thái kết nối.

Những vị trí trên được đọc trực tiếp ở nguồn gốc. Cột Notebook YES của các nguồn cũ phản ánh lần nhập trước; không xác nhận nội dung notebook đã đồng bộ với trang hiện hành. S029/S030 được xác minh tương đương trong ledger, Notebook NO. Ví dụ vùng nhớ 64/80 byte và các tình huống Server là minh họa giả định, không lấy từ nguồn và không phải dữ liệu thực nghiệm.

S031 bổ sung vì trang S007 hiện hành giải thích băm mật mã nhưng không nêu riêng SHA-512; dùng bài kỹ thuật gốc liên kết từ S023, không suy ra thuật toán chỉ từ trang overview. Bài minh họa không thay đặc tả chuẩn cho chi tiết triển khai.
