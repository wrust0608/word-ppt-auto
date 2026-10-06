# BẢN ĐỒ LẬP LUẬN — CANONICAL REPORT-WIDE 2026-10-06

Trạng thái: `LOCKED_ARGUMENT_ARCHITECTURE / PROSE_NOT_YET_REAPPROVED`

Nguồn điều khiển:
- `RESEARCH_MAP.md`
- `REPORT_WIDE_ARGUMENT_ENRICHMENT_RESEARCH.md`
- `REPORT_WIDE_ARGUMENT_CONTRACT.md`
- `EXPERIMENTAL_TRUTH_MATRIX.md`
- Chapter 3 evidence locks.

Bản lập luận lịch sử trước ngày 2026-10-06 bị supersede nếu xung đột với tài liệu này.

## Kết luận trung tâm dự kiến

Đánh giá an ninh SMB liên quan MS17-010 không thể rút gọn thành một phán quyết duy nhất từ trạng thái cổng hoặc một lần chạy công cụ. Khả năng tiếp cận dịch vụ, phương ngữ SMB được ghi nhận, tín hiệu từ kịch bản kiểm tra lỗ hổng và trạng thái bản vá cục bộ là các lớp thông tin khác nhau. Đề tài vì vậy xây dựng quy trình đo theo tầng, đối chiếu quan sát từ xa với trạng thái máy chủ, sau đó kiểm thử hai biện pháp giảm thiểu ở hai lớp khác nhau để xác định chính xác thành phần nào thay đổi và thành phần nào không thay đổi.

## Chuỗi lập luận canonical

| Claim ID | Luận điểm | Loại | Cơ sở chính | Ranh giới |
|---|---|---|---|---|
| C001 | Việc nhìn thấy TCP 139/445 mở chỉ xác nhận khả năng tiếp cận dịch vụ ở tầng mạng từ vị trí đo; muốn hiểu bề mặt SMB cần đo tiếp phương ngữ và thuộc tính giao thức | Phương pháp | Nmap, Microsoft SMB, AUTHOR_DATA Scenario 1 | `445 OPEN != vulnerable` |
| C002 | Sự hiện diện của SMBv1 là một điều kiện giao thức có liên quan đến MS17-010 nhưng không tự xác nhận máy chủ đang bị lỗ hổng | Cơ chế/Phương pháp | Microsoft MS17-010; SMB docs | `SMBv1 enabled != MS17-010 confirmed` |
| C003 | Kết quả từ `smb-vuln-ms17-010` là một tín hiệu thăm dò từ xa. Khi script không sinh phán quyết khả dụng, trạng thái phải giữ là UNKNOWN thay vì suy diễn thành an toàn hay có lỗ hổng | Phương pháp | Nmap script/docs; AUTHOR_DATA Scenario 2 | `UNKNOWN != SAFE`; không bịa nguyên nhân |
| C004 | Trạng thái bản vá cục bộ là một trục kiểm chứng độc lập. Với Windows Server 2012 R2, có thể đối chiếu KB và phiên bản `srv.sys` với ngưỡng Microsoft công bố | Kiểm chứng | Microsoft MS17-010 verification guide; AUTHOR_DATA baseline | Local UNPATCHED không tự biến remote UNKNOWN thành VULNERABLE |
| C005 | Case B tác động vào cấu hình/bề mặt giao thức: SMBv1 được vô hiệu hóa trong cấu hình máy chủ và không còn xuất hiện trong phép đo phương ngữ sau can thiệp; điều này không đồng nghĩa với việc máy chủ đã được vá | Kết quả/Diễn giải | AUTHOR_DATA Case B + Microsoft SMBv1 guidance | `SMBv1 disabled != PATCHED`; không suy rộng workload compatibility |
| C006 | Case C tác động vào đường tiếp cận mạng: pfSense có thể làm lưu lượng SMB từ vị trí đo bị lọc/chặn trong khi trạng thái cục bộ của Windows không đổi | Kết quả/Diễn giải | AUTHOR_DATA Case C + NIST firewall guidance | `FILTERED != PATCHED`; không dùng rule label mâu thuẫn để quy thuộc quá mức |
| C007 | Patching, protocol hardening và network access control giải quyết các lớp vấn đề khác nhau; kết quả của đề tài ủng hộ cách tiếp cận defense-in-depth và retest thay vì coi một biện pháp đơn lẻ là chứng chỉ an toàn | Phân tích | C001–C006 + Microsoft/NIST | Không có canonical Case A patch experiment; không định lượng hiệu quả ngoài dữ liệu |

## Mạch lập luận giữa các chương

```text
CHƯƠNG 1
SMB hoạt động thế nào?
MS17-010 liên quan tới lớp nào?
Một phép đo có thể chứng minh gì / không chứng minh gì?
        |
        v
CHƯƠNG 2
Vì sao cần lab có kiểm soát?
Vì sao đo theo thứ tự host -> port -> protocol -> remote signal -> local patch?
Vì sao chọn Case B và Case C làm hai lớp can thiệp khác nhau?
        |
        v
CHƯƠNG 3
Baseline thực tế là gì?
Kịch bản 1 quan sát bề mặt nào?
Kịch bản 2 trả về tín hiệu gì?
Case B thay đổi gì / giữ nguyên gì?
Case C thay đổi gì / giữ nguyên gì?
        |
        v
CHƯƠNG 4
Các khác biệt đó có ý nghĩa gì với rủi ro?
Mỗi control giải quyết lớp nào?
Rủi ro còn lại là gì?
Vì sao vẫn cần patch + hardening + access control + retest?
```

## Các cách giải thích cạnh tranh phải xử lý

| ID | Cách diễn giải dễ gặp | Kết luận canonical |
|---|---|---|
| ALT-01 | "TCP 445 mở nên máy chắc chắn dính MS17-010" | Bác bỏ. Cổng mở chỉ chứng minh khả năng tiếp cận dịch vụ từ vị trí đo |
| ALT-02 | "SMBv1 bật nên EternalBlue đã được xác nhận" | Bác bỏ. SMBv1 là điều kiện giao thức có liên quan, không phải phán quyết lỗ hổng |
| ALT-03 | "NSE không báo vulnerable nên máy an toàn" | Bác bỏ. Canonical run = UNKNOWN / NO USABLE SCRIPT RESULT |
| ALT-04 | "Máy UNPATCHED nên có thể ghi remote verdict là VULNERABLE" | Bác bỏ. Local patch state và remote verdict là hai trục độc lập |
| ALT-05 | "Tắt SMBv1 nghĩa là đã vá MS17-010" | Bác bỏ. Case B thay đổi cấu hình giao thức, không cài patch |
| ALT-06 | "Port FILTERED sau pfSense nghĩa là Windows đã hết lỗ hổng" | Bác bỏ. Case C thay đổi đường tiếp cận, không thay đổi binary patch state |
| ALT-07 | "Một control duy nhất đủ để tuyên bố an toàn" | Không được hỗ trợ. Mỗi control có phạm vi tác động và residual risk khác nhau |

## Điều đề tài có thể kết luận

- Có thể mô tả chính xác bề mặt SMB quan sát được tại từng trạng thái.
- Có thể phân biệt remote scanner signal với local patch verification.
- Có thể so sánh before/after của Case B và Case C theo lớp tác động.
- Có thể lập luận defense-in-depth từ sự khác biệt cơ chế giữa các control.
- Có thể đề xuất patching dựa trên nguồn chính thức và trạng thái UNPATCHED.

## Điều đề tài không được kết luận

- Không có bằng chứng canonical về khai thác RCE thành công.
- Không có reverse shell/Meterpreter/SYSTEM session canonical.
- Không được gọi remote NSE04 là false negative.
- Không được suy ra UNKNOWN là SAFE hoặc NOT VULNERABLE.
- Không có Case A patch thực nghiệm hoàn chỉnh để so sánh trước/sau.
- Không có benchmark hiệu năng hoặc workload compatibility toàn diện.
- Không được tổng quát hóa kết quả một target/một nguồn đo thành mọi hệ thống Windows/SMB.

## Mục tiêu trình bày

Mỗi chương phải đóng góp một mắt xích cần thiết cho kết luận trung tâm. Nếu một đoạn lý thuyết, bảng, công cụ hoặc hình ảnh không giúp người đọc hiểu một mắt xích trong chuỗi trên, cần xem xét tinh giản hoặc loại bỏ.
