# REQUIREMENT RECONCILIATION — X0

Trạng thái: `X0_DRAFT_FOR_REVIEW`  
Ngày: 2026-10-05

## 1. Nguồn ưu tiên

1. Yêu cầu trực tiếp hiện tại của người dùng.
2. Quy định/mẫu HUIT.
3. Đề cương chi tiết đã duyệt.
4. Hai kịch bản demo của giảng viên.
5. Evidence canonical + `EXPERIMENTAL_TRUTH_MATRIX.md`.
6. Quyết định repo còn hiệu lực.
7. Artifact/báo cáo lịch sử.

## 2. Mục tiêu đề tài phải được bảo toàn

Đề cương yêu cầu:
- hiểu SMB và SMBv1/v2/v3;
- giải thích 139/445, negotiation/session/resource access;
- phân tích MS17-010 và EternalBlue/CVE-2017-0144;
- phân biệt 445 open, SMBv1 enabled và unpatched/vulnerable state;
- mô tả vai trò Kali/Nmap/NSE/Metasploit;
- xây lab cô lập;
- thực hiện discovery/port/service/SMB identification;
- xây tiêu chí xác minh MS17-010;
- thu raw log/ảnh/bảng đối chiếu;
- đánh giá CIA/risk;
- áp dụng mitigation;
- retest;
- nhận diện residual risk/compatibility;
- hoàn thiện report/slide và bảo vệ phản biện.

## 3. Reconciliation theo evidence hiện tại

| Yêu cầu/claim | Trạng thái hiện tại | Quyết định |
|---|---|---|
| Oracle VirtualBox hoặc VMware | Canonical run dùng Oracle VirtualBox | Khóa VirtualBox cho bản chính thức |
| Kali + Windows target | Có | Giữ |
| Windows target thuộc phạm vi MS17-010 | Windows Server 2012 R2 Build 9600, local patch ground truth UNPATCHED | Giữ, mô tả đúng build/patch |
| Host-only/Internal | Baseline Host-Only | Khóa Host-Only baseline |
| Không Bridged với Windows chưa vá | Canonical baseline không Bridged | Giữ |
| Discovery / 139 / 445 / service / SMB dialect | Có canonical evidence | Đưa vào Ch3 |
| MS17-010 detection | Script canonical không sinh verdict usable | Ghi UNKNOWN; không ép VULNERABLE |
| Patch mitigation | Đề cương yêu cầu, nhưng canonical evidence Case A chưa có | Chưa được nhận là đã thực nghiệm; giữ như recommendation hoặc supplementary nếu evidence được audit |
| Disable SMBv1 | Có Case B canonical | Đưa vào Ch3/4 |
| Limit TCP 445 / segmentation | Có Case C pfSense canonical | Đưa vào Ch3/4; mô tả đúng phạm vi source/target |
| Metasploit | Đề cương yêu cầu nghiên cứu vai trò/module; canonical run không có exploit | Ch1 mô tả đúng vai trò/giới hạn; không claim đã exploit |
| Windows Event Viewer | Đề cương nêu môi trường/log phục vụ đối chiếu, canonical evidence hiện không khóa kết quả Event Viewer | Không tạo result nếu không có artifact |
| Snapshot/recovery | Có `Before Demo` | Giữ |
| Before/after matrix | Có Baseline / Case B / Case C | Đưa vào Ch4 |
| Residual risk / compatibility | Chưa là AUTHOR_DATA đầy đủ | Phân tích dựa trên evidence + source, tách proposal/limitation |

## 4. Drift phải loại khỏi canonical narrative

### 4.1. Scope stale
`PROJECT_PROFILE.md` và `RESEARCH_MAP.md` còn câu “tránh demo/kết quả demo”. Điều này đã hết hiệu lực vì evidence thật đã được cung cấp và người dùng yêu cầu soạn Ch2–4 dựa trên demo.

### 4.2. Topology stale
Windows 7 / 3 VLAN / Client đối chứng / Enterprise Topology trong `CHAPTER_ARGUMENT.md` và Ch2 cũ là historical design, không phải canonical run.

### 4.3. Case C stale
Windows Firewall Case C trong báo cáo cũ không được dùng; canonical Case C là pfSense Transparent Bridge.

### 4.4. Vulnerability verdict stale
`VULNERABLE / STATUS_INSUFF_SERVER_RESOURCES` của lượt cũ không đại diện cho canonical run 2026-10-04.

### 4.5. Patch Case A
Không được viết “đã patch và retest thành công” nếu chưa phục hồi/audit evidence cùng lineage.

### 4.6. Metasploit/exploit
Không được claim RCE, SYSTEM, Meterpreter, reverse shell, BSOD hoặc exploit success trong canonical run.

## 5. Điều chỉnh Research Question / Objective cần đề xuất

RQ/O hiện có thể giữ khung 4 câu hỏi, nhưng:
- RQ3 phải nói rõ xây dựng và đánh giá **quy trình quan sát/xác minh có kiểm soát**, không hứa remote scanner sẽ cho verdict.
- RQ4 nên dùng “đánh giá hiệu quả/giới hạn các lớp giảm thiểu” thay cho “triệt tiêu nguy cơ”.
- M3/M4 phải bỏ chỉ thị “tránh demo”.
- O4 phải phân biệt mitigation đã thực nghiệm (Case B/C) và mitigation được khuyến nghị (patch nếu chưa có canonical Case A).

## 6. Cấu trúc báo cáo theo HUIT

Giữ cấu trúc:
- Mở đầu
- Chương 1: Cơ sở lý thuyết & công cụ
- Chương 2: Thiết kế & triển khai mô hình lab
- Chương 3: Thực nghiệm kiểm thử SMB
- Chương 4: Đánh giá kết quả, rủi ro & khuyến nghị
- Kết luận/kiến nghị
- TLTK
- Phụ lục

## 7. Những thay đổi artifact cần phê duyệt ở X2/X3

- Reopen `PROJECT_PROFILE.md` cho scope/tool/platform stale.
- Reopen `RESEARCH_MAP.md` cho M3/M4/RQ4 wording.
- Reopen `OUTLINE.md` vì cấu trúc Ch2–4 stale.
- Archive/supersede `CHAPTER_ARGUMENT.md` cũ bằng contracts canonical.
- Không dùng `CHAPTER_2.md` cũ làm draft chính thức.

## 8. Kết luận X0

Không có mâu thuẫn nào buộc phải thay đổi mục tiêu cốt lõi của đề tài. Vấn đề nằm ở **artifact repo lịch sử chưa theo kịp demo thật**. Hướng xử lý là cập nhật governance/research artifacts theo evidence, không thay evidence để khớp báo cáo cũ.
