# CHANGE REQUEST — X5 CHAPTER 2 PRODUCT-ALIGNED REVISION

Status: `APPROVED_FOR_EXECUTION`  
Date: 2026-10-06  
Branch: `feature/x5-chapter-2-product-aligned`

## 1. Reason for revision

The demo-style R4 chapter passed presentation review but was written before the final evidence audit of `ALL(1).zip`.

The source package has now been normalized and locked by:
- `EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
- `TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
- `CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
- `COMMAND_LINEAGE_MATRIX.md`
- `EVIDENCE_USE_POLICY_ALL_ZIP.md`
- `CANONICAL_NMAP_TEXT_OUTPUTS.md`

R4 remains the style/reference baseline only.

This revision aligns Chapter 2 with the actual product evidence without reusing the ZIP folder structure as the report structure.

## 2. Presentation principle

Chapter 2 must answer, in order:

1. What is being tested and on what baseline model?
2. What final pre-demo state was established?
3. How is Scenario 1 performed?
4. How is Scenario 2 performed?
5. Which two mitigations were actually tested?
6. Which experimental data is valid for later analysis?
7. How does this lead to Chapter 3?

Keep language simple, technical and report-like.

Do not write like:
- QA memo;
- project governance note;
- evidence audit report;
- leader handoff.

## 3. Locked structure — 7 H2 / 20 H3

# CHƯƠNG 2. XÂY DỰNG MÔ HÌNH VÀ THIẾT KẾ KỊCH BẢN THỰC NGHIỆM

## 2.1. Phạm vi và mô hình thực nghiệm
### 2.1.1. Mục tiêu và phạm vi thực nghiệm
### 2.1.2. Mô hình mạng ở trạng thái baseline
### 2.1.3. Thành phần và thông số môi trường

## 2.2. Chuẩn bị và xác nhận trạng thái ban đầu
### 2.2.1. Cấu hình mạng và hai máy ảo
### 2.2.2. Chuẩn bị Kali Linux và công cụ Nmap/NSE
### 2.2.3. Chuẩn bị Windows Server, SMB và Windows Firewall
### 2.2.4. Xác định trạng thái bản vá MS17-010
### 2.2.5. Snapshot và kiểm tra trước thực nghiệm

## 2.3. Kịch bản 1 — Khảo sát dịch vụ SMB bằng Nmap
### 2.3.1. Mục tiêu và dữ liệu cần quan sát
### 2.3.2. Quy trình quét và các lệnh thực hiện
### 2.3.3. Giới hạn kết luận của Kịch bản 1

## 2.4. Kịch bản 2 — Kiểm tra dấu hiệu MS17-010 bằng NSE
### 2.4.1. Mục tiêu và điều kiện thực hiện
### 2.4.2. Bốn phép đo NSE-SMB-01 đến NSE-SMB-04
### 2.4.3. Đối chiếu kết quả từ xa với trạng thái bản vá nội bộ

## 2.5. Kiểm thử hai biện pháp giảm thiểu đã thực hiện
### 2.5.1. Nguyên tắc đối chiếu trước và sau can thiệp
### 2.5.2. Vô hiệu hóa SMBv1 trên Windows Server
### 2.5.3. Kiểm soát SMB bằng pfSense Transparent Bridge

## 2.6. Dữ liệu thực nghiệm và nguyên tắc sử dụng
### 2.6.1. Dữ liệu được thu thập và lưu trữ
### 2.6.2. Phạm vi dữ liệu dùng cho đánh giá
### 2.6.3. Nguyên tắc diễn giải kết quả

## 2.7. Tổng kết chương

## 4. Product-alignment locks

### Baseline
- VirtualBox report wording: use `7.2.20`; do not use stale `r170876`.
- Kali `.56.10/24`; Windows `.56.20/24`.
- one Host-Only NIC per Kali/Windows in final pre-demo baseline.
- no NAT/Bridged NIC for those two VMs in final pre-demo baseline.
- no default route in those VMs at final pre-demo state.
- Nmap 7.99 final pre-demo.
- `Before Demo` snapshot exists after the snapshot step.

### Patch state
- display FileVersion String: `6.3.9600.16384`.
- numeric `srv.sys`: `6.3.9600.16421`.
- Microsoft minimum updated version: `6.3.9600.18604`.
- local classification: `UNPATCHED`.
- Microsoft KB/version rules require official Microsoft source citation.
- do not claim omniscient update history; phrase local hotfix absence as observed inventory.

### Scenario 1
Use exact operator command forms from `COMMAND_LINEAGE_MATRIX.md`.

Do not silently add `-Pn`.

B1:
`ip addr show`
`ip route show`

B2–B6 must preserve the executed flags:
- `-PR`
- `-T3`
- `--max-retries 2`
- B5 `--version-intensity 5`
- B6 exact four scripts.

### Scenario 2
Present all four operator commands, not only NSE-SMB-04.

Do not insert raw-only `--privileged` into the operator command unless explicitly explaining raw argv provenance.

### Case B
Actual intervention:
`Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force`

Actual retests:
- `smb-protocols`
- `smb-vuln-ms17-010`

No restart.
No uninstall.
No claim of patching.

### Case C
Case C has its own topology.

Data plane:
`Kali .56.10 -> ATTT-PFS-KALI -> pfSense em2 -> bridge0 -> em3 -> ATTT-PFS-WIN -> Windows .56.20`

Management plane:
`Host .57.1 <-> Host-Only #2 <-> pfSense em1 .57.2`

Direct evidence:
- CASE_C_KALI=em2;
- CASE_C_WINDOWS=em3;
- bridge0 membership;
- pfil_member=1;
- pfil_bridge=0;
- configured Block rule .56.10 -> .56.20 TCP 139/445, logging enabled;
- block row above pass row.

Metadata-supported:
- pfil_onlyip=1;
- Internal Network names;
- management addresses;
- pfSense CE 2.9.0-RELEASE;
- snapshot metadata.

Do not present metadata-supported facts as screenshot-proven facts.

### Case C log conflict
Chapter 2 should not claim exact log-rule attribution.

Allowed:
- design includes the configured block rule;
- later evaluation will compare port reachability and firewall log evidence.

Forbidden:
- “the log proves that the named block rule matched.”

### Case A
Remove Case A from the Chapter 2 experimental matrix and from the list of performed mitigations.

Patching appears:
- in 2.2.4 as baseline patch-state verification;
- in Chapter 4 as mitigation/recommendation/theoretical comparison.

Do not present it as a completed experiment.

## 5. Timebase and cross-layer locks

Do not compare Kali, Windows, pfSense and host timestamp strings as one clock.

Do not identify Scenario 1 host `.56.100`.

Keep local signing flags and remote Nmap signing result as separate observations.

## 6. Section 2.6 boundary

2.6 must be short and readable.

### Allowed primary data for Chapter 3
- final pre-demo/local state;
- Scenario 1 raw;
- Scenario 2 raw;
- Case B local before/action/after + raw retests;
- Case C final configuration screenshots + canonical raw retests + canonical firewall log.

### Exclude from main result claims
- HostRepair;
- pre-repair/aborted/debug Case C artifacts;
- old reports;
- summary prose that exceeds raw/direct evidence;
- superseded screenshots.

Do not expose internal evidence IDs heavily in the report prose.

## 7. Figures/tables target

Recommended:
- Figure 2.1 — baseline topology.
- Figure 2.2 — Case C transparent-bridge topology.

Tables:
- Table 2.1 — baseline environment.
- Table 2.2 — Scenario 1 steps and operator commands.
- Table 2.3 — Scenario 2 four measurements and operator commands.
- Table 2.4 — Baseline vs Case B vs Case C: intervention and retest design.

Do not include Case A as an experimental row.

## 8. Chapter boundary

Chapter 2 = setup + method.

Do not leak detailed measured results such as:
- exact open/filtered outcomes;
- final SMB dialect list;
- final NSE UNKNOWN result;
- before/after observed result tables.

Those belong to Chapter 3.

It is acceptable to state baseline local configuration required to define the experimental starting state.

## 9. Workflow

R4 candidate:
`38057dc2c9c35fce593d5a784d6df8ad9465282e`

New branch:
`feature/x5-chapter-2-product-aligned`

R4 prose may be reused only where it remains accurate.

The product-aligned revision must be externally reviewed again.

CP5-USER remains PENDING.
X6 remains BLOCKED.
