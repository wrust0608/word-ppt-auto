# Sổ nguồn

Trạng thái hợp lệ: `CANDIDATE`, `INGESTED`, `VERIFIED`, `REJECTED`, `RECHECK`.

| Source ID | Trạng thái | Tác giả/cơ quan | Năm | Tiêu đề | Loại | DOI/URL | Notebook | Vị trí bằng chứng | Chất lượng | Dùng cho |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | VERIFIED | Andrew S. Tanenbaum et al. | 2021 | Computer Networks (6th ed.) | Textbook | Pearson | YES | Application Layer, NetBIOS, Client-Server model | Cao | [1] Mô hình mạng OSI/TCP, đặc tính chatty protocol của SMBv1 |
| S002 | VERIFIED | Microsoft Learn | 2023 | Direct hosting of SMB over TCP/IP | Tech Doc | https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/direct-hosting-of-smb-over-tcpip | YES | Dual-SYN probing, 4-byte header, port 139/445 | Cao | [2] Cơ chế phân định cổng TCP 139 (NBT) và 445 (Direct-hosted SMB) |
| S003 | VERIFIED | Pavel Yosifovich et al. | 2017 | Windows Internals, Part 1 (7th ed.) | Textbook | Microsoft Press | YES | System Architecture, Kernel Mode, Non-Paged Pool | Cao | [3] Kiến trúc nhân Windows, driver srv.sys, cơ chế cấp phát bộ nhớ pool |
| S004 | VERIFIED | Andrea Allievi et al. | 2021 | Windows Internals, Part 2 (7th ed.) | Textbook | Microsoft Press | YES | Networking, File Systems, Named Pipes, RPC | Cao | [4] Network Redirector, Server service, Named Pipes và IPC$ |
| S005 | VERIFIED | Microsoft | 2017 | Microsoft Security Bulletin MS17-010 – Critical | Official Bulletin | https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010 | YES | Danh mục 6 CVE, ma trận KB theo hệ điều hành Windows | Cao | [5] Định danh bulletin MS17-010, ma trận bản vá KB chính thức |
| S006 | VERIFIED | Microsoft Learn | 2023 | Overview of file sharing using the SMB 3 protocol in Windows Server | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-overview | YES | SMB compounding, features across dialects | Cao | [6] Đặc tính kỹ thuật SMBv2/SMBv3, cải tiến hiệu năng |
| S007 | VERIFIED | Microsoft Learn | 2023 | SMB security enhancements | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security | YES | AES-128-CCM/GCM, AES-CMAC/GMAC, Pre-auth Integrity SHA-512 | Cao | [7] Chi tiết các cơ chế an ninh, thuật toán mã hóa/ký số của SMBv3 |
| S008 | VERIFIED | Microsoft Learn | 2025 | Detect, enable, and disable SMBv1, SMBv2, and SMBv3 in Windows | Tech Doc | https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3 | YES | Thủ tục PowerShell, Registry, GPO bật/tắt SMB | Cao | [8] Hướng dẫn vô hiệu hóa SMBv1 và quản lý cấu hình giao thức |
| S009 | VERIFIED | Chris McNab | 2016 | Network Security Assessment (3rd ed.) | Book | O'Reilly Media | YES | Windows/SMB Assessment, Network Segmentation | Cao | [9] Đánh giá rủi ro mạng, phân đoạn mạng và kiểm soát cổng SMB |
| S010 | VERIFIED | Microsoft Security Response Center (MSRC) | 2017 | Eternal Synergy Exploit Analysis | Tech Analysis | https://msrc.microsoft.com/blog/2017/05/eternal-synergy-exploit-analysis/ | YES | Phân tích cơ chế exploit CVE-2017-0143 | Cao | [10] Ánh xạ chính thức CVE-2017-0143 với EternalSynergy |
| S011 | VERIFIED | NIST | 2017 | CVE-2017-0144 Detail | Vulnerability DB | https://nvd.nist.gov/vuln/detail/CVE-2017-0144 | YES | CVSS score, CWE-119, thông số kỹ thuật lỗ hổng | Cao | [11] Định danh lỗ hổng CVE-2017-0144 (không dùng ngoài phạm vi) |
| S012 | VERIFIED | Microsoft Threat Intelligence | 2017 | New ransomware, old techniques: Petya adds-worm capabilities | Threat Report | https://www.microsoft.com/en-us/security/blog/2017/06/27/new-ransomware-old-techniques-petya-adds-worm-capabilities/ | YES | Phân tích Petya/NotPetya, CVE-2017-0145 EternalRomance | Cao | [12] Ánh xạ CVE-2017-0145 với EternalRomance và mã độc NotPetya |
| S013 | VERIFIED | Rapid7 | 2017 | MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption | Exploit DB | https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/ | YES | Phân tích SrvOs2FeaToNt, pool grooming, module Metasploit | Cao | [13] Cơ chế kỹ thuật FEA root cause và rủi ro BSOD khi khai thác |
| S014 | VERIFIED | Cybersecurity and Infrastructure Security Agency (CISA) | 2017 | Alert (TA17-132A): Indicators Associated With WannaCry Ransomware | Technical Alert | https://www.cisa.gov/news-events/alerts/2017/05/12/indicators-associated-wannacry-ransomware | YES | Phân tích chỉ báo lây nhiễm WannaCry qua cổng 445 SMBv1 | Cao | [14] Dẫn chứng cảnh báo chính thức về chiến dịch mã độc WannaCry |
| S015 | VERIFIED | Microsoft Threat Intelligence | 2017 | WannaCrypt ransomware worm targets out-of-date systems | Threat Report | https://www.microsoft.com/en-us/security/blog/2017/05/12/wannacrypt-ransomware-worm-targets-out-of-date-systems/ | YES | Thống kê tác động WannaCry trên 150 quốc gia, lây lan SMB | Cao | [15] Dẫn chứng số liệu tác động diện rộng và cơ chế lây lan WannaCry |
| S016 | VERIFIED | Georgia Weidman | 2014 | Penetration Testing: A Hands-On Introduction to Hacking | Book | No Starch Press | YES | Lab Setup, Ethics, Snapshot Baseline | Cao | [16] Nguyên tắc xây dựng phòng lab cô lập và đạo đức kiểm thử |
| S017 | VERIFIED | Gordon Lyon | 2009 | Nmap Network Scanning: The Official Nmap Project Guide | Book | Insecure.Com LLC / https://nmap.org/book/ | YES | Port Scanning, -sS, -sV, -O, Scripting Engine | Cao | [17] Cơ sở lý thuyết quét cổng, phân biệt -sV và -O |
| S018 | VERIFIED | Paulino Calderon & Nmap Project | 2017 | smb-vuln-ms17-010.nse Script Source Code | Source Code | https://svn.nmap.org/nmap/scripts/smb-vuln-ms17-010.nse | YES | Mã nguồn NSE: opcode 0x25, PeekNamedPipe 0x2300, 0xC0000205 | Cao | [18] Bằng chứng mã nguồn trực tiếp cho logic nhận diện của Nmap NSE |
| S019 | VERIFIED | David Kennedy et al. | 2024 | Metasploit: The Penetration Tester's Guide (2nd ed.) | Book | No Starch Press | YES | Auxiliary Scanner, Exploit Modules, Payloads | Cao | [19] Kiến trúc Metasploit, phân định module phụ trợ và khai thác |

## Nguồn bị loại

| Source ID | Lý do loại | Luận điểm bị ảnh hưởng |
|---|---|---|
| M. E. Aminanto et al. (IEEE Access 2019) | Chưa xác minh được bản ghi độc lập công khai (DOI/record); nội dung bài báo deep learning không trực tiếp hỗ trợ cho bối cảnh lây lan WannaCry. Đã thay bằng nguồn chính thức CISA [14] và Microsoft Threat Intelligence [15]. | Bối cảnh lây lan WannaCry diện rộng |

## Danh sách truy vấn còn thiếu

| ID | Thông tin cần tìm | Luận điểm liên quan | Mức ưu tiên | Trạng thái |
|---|---|---|---|---|
| Q001 | Chi tiết mã lỗi buffer overflow/heap grooming trong srv.sys cho CVE-2017-0144 | Cơ chế lỗ hổng mức nhân của MS17-010 | Cao | CLOSED (Đã chuẩn hóa cơ chế FEA qua S013, S003, S005) |
| Q002 | Khuyến nghị hardening SMB từ CIS Benchmark và Microsoft Security Baseline | Khuyến nghị phòng thủ đa tầng | Trung bình | CLOSED (Đã tích hợp 6 nguyên tắc phòng thủ qua S007, S008, S009) |
