# X5 — REWRITE CHAPTER 2 IN SIMPLE DEMO-STYLE

Trạng thái: `READY_FOR_EXECUTOR`  
Branch: `feature/x5-chapter-2-demo-style`

## Mục tiêu

Viết lại hoàn chỉnh Chương 2 theo kiểu **báo cáo đồ án ATTT có demo**: đơn giản, dễ hiểu, đúng trọng tâm, đọc tự nhiên như một chương mô tả xây dựng lab và kịch bản thực hành.

Không viết như:
- báo cáo trình leader;
- technical design review;
- QA/audit memo;
- evidence-governance document.

## Căn cứ bắt buộc

Đọc theo thứ tự:

1. `origin/main:work/do-an/CHANGE_REQUEST_CR-2026-10-05-X5-DEMO-STYLE.md`
2. `origin/main:work/do-an/PROJECT_STATE.md`
3. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
4. `work/do-an/EVIDENCE_REGISTER.md`
5. `work/do-an/NEGATIVE_RESULT_POLICY.md`
6. `work/do-an/SOURCE_LEDGER.md`
7. `work/do-an/AUTHOR_VOICE.md`
8. R5 technical baseline tại commit `97faf32564191ab0b590bf02e287c6c4935cbbdc`

R5 là nguồn technical facts/reference, KHÔNG phải mẫu cấu trúc hay giọng trình bày.

## Cấu trúc khóa

# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH THỰC NGHIỆM VÀ KỊCH BẢN DEMO

## 2.1. Mô hình thực nghiệm
### 2.1.1. Mục tiêu của mô hình
### 2.1.2. Sơ đồ và thành phần của mô hình
### 2.1.3. Thông số môi trường thực nghiệm

## 2.2. Cài đặt và cấu hình môi trường
### 2.2.1. Cấu hình mạng Host-Only trên VirtualBox
### 2.2.2. Cấu hình máy Kali Linux
### 2.2.3. Cấu hình máy Windows Server 2012 R2
### 2.2.4. Cấu hình SMB và Windows Firewall
### 2.2.5. Kiểm tra bản vá MS17-010 và tạo snapshot

## 2.3. Kịch bản Demo 1 — Khảo sát dịch vụ SMB bằng Nmap
### 2.3.1. Mục tiêu và phạm vi
### 2.3.2. Quy trình và các lệnh thực hiện
### 2.3.3. Nội dung cần quan sát và giới hạn kết luận

## 2.4. Kịch bản Demo 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE
### 2.4.1. Mục tiêu và điều kiện ban đầu
### 2.4.2. Quy trình kiểm tra NSE-SMB-01 đến NSE-SMB-04
### 2.4.3. Đối chiếu với trạng thái bản vá và giới hạn kết luận

## 2.5. Kiểm thử các biện pháp giảm thiểu
### 2.5.1. Nguyên tắc kiểm thử trước và sau can thiệp
### 2.5.2. Case B — Vô hiệu hóa SMBv1
### 2.5.3. Case C — Kiểm soát TCP 139/445 bằng pfSense
### 2.5.4. Vai trò của cập nhật bản vá

## 2.6. Thu thập dữ liệu phục vụ đánh giá
### 2.6.1. Log và ảnh chụp thực nghiệm
### 2.6.2. Nguyên tắc diễn giải kết quả

## 2.7. Tổng kết chương

Tổng: **7 H2 / 20 H3**.

Không thêm heading.
Không thêm framework phụ.

## Nguyên tắc trình bày

Người đọc phải có cảm giác:

“Đây là lab được dựng như thế nào → cấu hình ra sao → Demo 1 làm gì → Demo 2 làm gì → thử giảm thiểu ra sao → dữ liệu nào sẽ được dùng ở Chương 3.”

Mỗi subsection phải trả lời một câu hỏi trực tiếp.

Ưu tiên:
- câu ngắn và rõ;
- thông số thật;
- lệnh thật;
- sơ đồ thật;
- bảng gọn;
- flow demo dễ theo dõi.

Không ưu tiên:
- khái niệm governance;
- mô hình evidence phức tạp;
- taxonomy dài;
- giải thích triết lý phương pháp;
- thuật ngữ nội bộ repo.

## Những thứ PHẢI BỎ khỏi prose chính

Không dùng:
- `canonical`
- `ground truth`
- `truth matrix`
- `evidence layer model` như framework chính
- `gate`
- `CP5`
- `locked candidate`
- mã Evidence ID dày đặc trong đoạn văn.

Evidence IDs chỉ dùng trong:
- self-review;
- figure/source note nội bộ nếu thật sự cần;
- QA mapping.

## Technical facts không được thay đổi

- VirtualBox 7.2.20.
- Kali: `192.168.56.10/24`.
- Windows Server 2012 R2 Standard Evaluation Build 9600: `192.168.56.20/24`.
- Baseline Host-Only, 1 NIC/VM, no NAT, no Bridged, no default Internet route.
- Nmap 7.99.
- LanmanServer Running / Automatic.
- TCP 139/445 listening.
- SMB1=True, SMB2=True.
- Windows Firewall chỉ allow TCP 139/445 từ Kali; không mở toàn bộ File and Printer Sharing group.
- Local patch state = UNPATCHED.
- srv.sys numeric = 6.3.9600.16421.
- minimum updated threshold = 6.3.9600.18604.
- Snapshot `Before Demo` trên Kali và Windows.

## Demo 1

Mô tả theo đúng logic thực hành:

1. kiểm tra IP/route;
2. host discovery `192.168.56.0/24`;
3. xác nhận `192.168.56.20`;
4. quét TCP 139/445;
5. service/version;
6. 4 NSE scripts:
   - `smb-protocols`
   - `smb-os-discovery`
   - `smb2-security-mode`
   - `smb2-capabilities`
7. lưu output;
8. kết thúc.

Demo 1 chỉ khảo sát SMB.
Không kết luận MS17-010.

## Demo 2

Mô tả 4 bước rõ ràng:

- NSE-SMB-01: TCP 139/445.
- NSE-SMB-02: `smb-protocols`.
- NSE-SMB-03: `smb2-security-mode`.
- NSE-SMB-04: `smb-vuln-ms17-010`.

Có thể mô tả ngắn cơ chế script dựa theo Nmap official source:
- IPC$;
- transaction on FID 0;
- phân tích status code.

Không kể actual output của run hiện hành trong Chương 2.

Giới hạn phải nói dễ hiểu:
- không có output usable không có nghĩa là an toàn;
- kết quả từ xa phải đối chiếu với trạng thái bản vá trên Server.

## Case B

Nêu:
- lệnh tắt SMBv1;
- mục đích;
- sau đó chạy lại phép đo nào;
- tắt SMBv1 không đồng nghĩa đã patch.

Không biến thành framework “protocol-layer mitigation”.

## Case C

Nêu đơn giản:
- chèn pfSense Transparent Bridge;
- block TCP 139/445 từ Kali đến Windows;
- bật log;
- chạy lại scan/NSE;
- firewall chỉ chặn đường truy cập, không vá Windows.

Canonical tunables phải đúng:
- `pfil_member=1`
- `pfil_bridge=0`
- `pfil_onlyip=1`

Không đưa pfSense vào topology baseline.

## Case A / Patching

Chỉ nói:
- patching là giải pháp chuẩn;
- kiểm tra KB/file version;
- bộ evidence hiện hành không có Case A experiment hoàn chỉnh;
- không trình bày như đã chạy demo.

## Mục 2.6

Giữ ngắn.

Chỉ cần nói:
- Nmap/NSE output lưu `.nmap/.xml/.gnmap`;
- ảnh chụp phải cho thấy VM/terminal khi cần;
- nguyên tắc đọc kết quả:
  - open445 != vulnerable;
  - SMBv1 != MS17-010;
  - UNKNOWN != SAFE;
  - FILTERED != PATCHED;
  - disable SMB1 != PATCHED.

Không tạo “mô hình năm lớp” ở đây.

## Hình và bảng

Mục tiêu đơn giản:

Hình:
1. Sơ đồ mô hình lab baseline.
2. Flow Demo 1.
3. Flow Demo 2.
4. Flow trước/sau Case B–Case C.

Bảng:
1. Cấu hình môi trường.
2. Các bước/lệnh Demo 1.
3. Các bước/lệnh Demo 2.
4. So sánh thiết kế Baseline / Case B / Case C.

Không tạo bảng taxonomy evidence.

## Văn phong

Viết như báo cáo đồ án sinh viên kỹ thuật tốt:
- rõ;
- trực tiếp;
- dễ đọc;
- không cố “học thuật hóa” câu đơn giản;
- không dùng từ nội bộ quản lý dự án;
- không viết như SOP hay checklist khô cứng;
- không kéo dài giải thích nếu một bảng/lệnh đã nói đủ.

Giữ ngôi thứ ba khách quan.

Không dùng “tôi/chúng tôi”.

## Target length

Khoảng **3.200–4.000 từ**.

Không cố đạt trần.

Ưu tiên đơn giản và đúng trọng tâm.

## Files được phép sửa

- `work/do-an/CHAPTER_2.md`
- `work/do-an/CHAPTER_2_X5_SELF_REVIEW.md`

Không sửa:
- Truth Matrix
- Evidence Register
- Negative Result Policy
- Source Ledger
- Chapter 3
- Chapter 4
- main governance files

## QA bắt buộc

Chạy:
- validator;
- unit tests;
- academic linter;
- citation audit;
- `git diff --check`.

Kiểm thủ công:
- 7 H2 / 20 H3;
- không governance jargon;
- không Evidence ID spam;
- không result leakage;
- không Case A fake result;
- không UNKNOWN→SAFE;
- không FILTERED→PATCHED;
- không SMB1 disabled→PATCHED;
- không pfSense trong baseline topology.

## Git

Làm trên:

`feature/x5-chapter-2-demo-style`

Push remote.

Không merge main.

## Handoff

Trả:
1. commit SHA;
2. remote SHA;
3. word count;
4. 7 H2 / 20 H3;
5. figure/table inventory;
6. technical truth audit;
7. “demo-style vs technical-review-style” audit;
8. QA results;
9. clean status.

Trạng thái cuối:

`X5_DEMO_STYLE_R1_READY_FOR_EXTERNAL_REVIEW`

Sau đó DỪNG.

Không tự tuyên bố PASS.
Không mở X6.
