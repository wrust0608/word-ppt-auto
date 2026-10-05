# X5 PRODUCT-ALIGNED — REWRITE CHAPTER 2 AGAINST FINAL EVIDENCE LOCK

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x5-chapter-2-product-aligned`

## 0. Goal

Revise Chapter 2 so it matches the actual completed product evidence in `ALL(1).zip`.

Keep the simple demo-report style from R4.

Do NOT reuse the ZIP folder structure as a report outline.

Do NOT open Chapter 3.

Do NOT invent new experiments.

## 1. Repository

Repository:
`wrust0608/word-ppt-auto`

Checkout:
```bash
git fetch origin
git checkout feature/x5-chapter-2-product-aligned
git pull --ff-only origin feature/x5-chapter-2-product-aligned
git status --short
git rev-parse HEAD
```

R4 starting candidate:
`38057dc2c9c35fce593d5a784d6df8ad9465282e`

## 2. Read order — mandatory

Read from `origin/main` before editing:

1. `work/do-an/CHANGE_REQUEST_CR-2026-10-06-X5-PRODUCT-ALIGNED.md`
2. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_AUDIT_R3_FINAL_LOCK.md`
3. `work/do-an/evidence/ALL_2026_10_06/TIMEBASE_AND_CROSS_LAYER_LOCKS.md`
4. `work/do-an/evidence/ALL_2026_10_06/CANONICAL_EVIDENCE_MAP_ALL_ZIP.md`
5. `work/do-an/evidence/ALL_2026_10_06/COMMAND_LINEAGE_MATRIX.md`
6. `work/do-an/evidence/ALL_2026_10_06/EVIDENCE_USE_POLICY_ALL_ZIP.md`
7. `work/do-an/evidence/ALL_2026_10_06/CANONICAL_NMAP_TEXT_OUTPUTS.md`
8. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
9. `work/do-an/AUTHOR_VOICE.md`

R4 Chapter 2 is a style baseline only.

## 3. Locked structure

Use exactly:

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

Exactly 7 H2 / 20 H3.

Do not add headings.

## 4. Baseline facts

Use:
- Oracle VM VirtualBox 7.2.20.
- Kali `192.168.56.10/24`.
- Windows Server 2012 R2 Standard Evaluation Build 9600 `192.168.56.20/24`.
- baseline: one Host-Only NIC per Kali/Windows VM.
- no NAT/Bridged NIC for those two VMs at final pre-demo state.
- no default route in those VMs at final pre-demo state.
- Host-Only network `192.168.56.0/24`.
- Nmap 7.99 at final pre-demo state.
- `Before Demo` snapshot exists after the snapshot step.

Do not use stale `r170876`.

Do not identify host `.56.100`.

## 5. Patch-state wording

Local observed state:
- FileVersion String `6.3.9600.16384`.
- numeric `srv.sys 6.3.9600.16421`.
- local classification `UNPATCHED`.

Microsoft minimum updated version:
- `6.3.9600.18604`.

KB/update mapping:
- KB4012213;
- KB4012216;
- or superseding update.

Academic report must cite official Microsoft sources for KB/version mapping.

Do not write:
“Windows has never received any rollup.”

Prefer:
“the observed local hotfix inventory does not show KB4012213, KB4012216, or an update in the project mapping that contains the MS17-010 fix.”

## 6. Scenario 1 exact operator commands

Use the operator-command column in `COMMAND_LINEAGE_MATRIX.md`.

B1:
```bash
ip addr show
ip route show
```

B2:
```bash
sudo nmap -sn -PR 192.168.56.0/24 -T3 --max-retries 2 -oA b2_host_discovery
```

B3:
```bash
sudo nmap -sn -PR 192.168.56.20 -T3 --max-retries 2 -oA b3_target_alive
```

B4:
```bash
sudo nmap -sS -p 139,445 192.168.56.20 -T3 --max-retries 2 --reason -oA b4_smb_ports
```

B5:
```bash
sudo nmap -sS -sV --version-intensity 5 -p 139,445 192.168.56.20 -T3 --max-retries 2 -oA b5_smb_version
```

B6:
```bash
sudo nmap -sS -p 139,445 --script smb-protocols,smb-os-discovery,smb2-security-mode,smb2-capabilities 192.168.56.20 -T3 --max-retries 2 -oA b6_smb_nse
```

Do not add `-Pn`.

Use one compact table for:
Step | Command | Purpose | What to observe.

Do not leak measured result values into Chapter 2.

## 7. Scenario 2 exact operator commands

Present all four:

NSE-SMB-01:
```bash
sudo nmap -sS -p 139,445 -n -T3 --max-retries 2 --reason -oA evidence/nse-smb/NSE-SMB-01_ports 192.168.56.20
```

NSE-SMB-02:
```bash
nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20
```

NSE-SMB-03:
```bash
nmap -p 445 -n -T3 --max-retries 2 --script smb2-security-mode -oA evidence/nse-smb/NSE-SMB-03_signing 192.168.56.20
```

NSE-SMB-04:
```bash
nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

Do not add literal `--privileged` to these operator commands.

If raw argv provenance is discussed at all, explain separately and briefly.

## 8. Scenario 2 interpretation boundary

Method section may say:
- remote script result must be recorded exactly;
- no usable verdict is `UNKNOWN / NO USABLE SCRIPT RESULT`;
- local patch state is checked independently.

Do not state the actual canonical Scenario 2 result in a results table here.

Do not invent a cause for missing output.

## 9. Signing lock

Do not collapse:
- local PowerShell signing flags;
- remote Nmap `smb2-security-mode`.

If Chapter 2 needs signing:
- describe what NSE-SMB-03 measures remotely;
- do not rewrite local properties as the remote result.

## 10. Case B

Actual intervention:
```powershell
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
```

Actual retests:
```bash
nmap -p 445 -n -T3 --max-retries 2 --script smb-protocols -oA evidence/nse-smb/NSE-SMB-02_protocols 192.168.56.20

nmap -p 445 -n -T3 --max-retries 2 --script smb-vuln-ms17-010 -oA evidence/nse-smb/NSE-SMB-04_ms17010 192.168.56.20
```

No reboot.
No uninstall.
No full NSE01–04 retest claim.
No patch claim.

## 11. Case C topology

Chapter 2 must contain a dedicated Case C topology figure or figure placeholder.

Data plane:
`Kali .56.10 -> ATTT-PFS-KALI -> pfSense em2 -> bridge0 -> pfSense em3 -> ATTT-PFS-WIN -> Windows .56.20`

Management:
`Host .57.1 <-> Host-Only #2 <-> pfSense em1 .57.2`

Important evidence grades:
- direct screenshot: CASE_C_KALI=em2, CASE_C_WINDOWS=em3;
- direct screenshot: bridge0 membership;
- direct screenshot: `pfil_member=1`, `pfil_bridge=0`;
- metadata-supported: `pfil_onlyip=1`;
- metadata-supported: Internal Network names, management IPs, CE 2.9.0 and snapshot.

Write naturally.
Do not expose evidence-grade jargon in prose.

## 12. Case C rule design

Configured rule:
- Action Block.
- IPv4 TCP.
- CASE_C_KALI side.
- source `192.168.56.10`.
- destination `192.168.56.20`.
- destination SMB ports 139/445.
- logging enabled.
- block row above baseline pass row.

Case C retest design:
- ports NSE-SMB-01 equivalent;
- MS17-010 NSE-SMB-04 equivalent.

Do not write detailed measured result here.

## 13. Case C conflict boundary

Do not claim:
“the firewall log proves the named Block rule matched.”

The direct log screenshot has an unresolved visible rule-label conflict.

Chapter 2 only needs to describe:
- the configured rule;
- the plan to compare reachability and firewall logs in Chapter 3.

Do not mention the internal conflict unless needed to explain evidence selection; preferably keep it out of Chapter 2 prose.

## 14. Remove Case A from experimental design

There is no completed Case A experiment.

Do not include:
- Case A row in experimental table;
- Case A as third performed mitigation.

Patching remains:
- baseline patch-state verification in 2.2.4;
- later recommendation/comparison in Chapter 4.

## 15. Before/after method wording

Do not claim a strict single-variable experiment for Case C.

Prefer:
“giữ nguyên các trạng thái quan trọng của Kali/Windows khi có thể, áp dụng từng biện pháp riêng và thực hiện lại các phép đo phù hợp để so sánh với baseline.”

## 16. Section 2.6

Keep concise.

### 2.6.1
Describe:
- `.nmap`;
- `.xml`;
- `.gnmap`;
- screenshots;
- local PowerShell state;
- pfSense configuration/logs.

### 2.6.2
Explain in normal report language that later evaluation uses the final/canonical experiment set.

Allowed for main Chapter 3 results:
- final pre-demo/local state;
- Scenario 1 final raw;
- Scenario 2 final raw;
- Case B before/action/after + final raw retests;
- Case C final config screenshots + canonical raw retests + canonical firewall log.

Do not use as main results:
- HostRepair;
- aborted/pre-repair/debug runs;
- old reports;
- summary claims exceeding direct/raw evidence;
- superseded screenshot.

Do not dump internal Evidence IDs into report prose.

### 2.6.3
Keep the five boundaries:
- 445 open != vulnerable
- SMBv1 enabled != MS17-010 confirmed
- UNKNOWN != SAFE
- FILTERED != PATCHED
- SMBv1 disabled != PATCHED

## 17. Timebase rule

Do not compare displayed timestamps across Kali/Windows/pfSense/host as one unified timeline.

Do not write synthetic chronological clock claims.

## 18. Tables and figures

Target:

Figure 2.1 — Baseline topology.
Figure 2.2 — Case C transparent bridge topology.

Table 2.1 — Baseline environment.
Table 2.2 — Scenario 1 steps/commands.
Table 2.3 — Scenario 2 steps/commands.
Table 2.4 — Baseline / Case B / Case C intervention and retest design.

No Case A row.

## 19. Writing style

Write as a strong undergraduate ATTT project report:
- direct;
- readable;
- technical;
- no governance jargon;
- no evidence-audit prose;
- no self-congratulatory claims;
- no unnecessary framework.

R4’s simple style is the target.

## 20. Files allowed to edit

Only:
- `work/do-an/CHAPTER_2.md`
- `work/do-an/CHAPTER_2_X5_SELF_REVIEW.md`

Do not edit:
- evidence layer;
- truth matrix;
- Chapter 3;
- Chapter 4;
- project state.

## 21. Self-review

Explicitly check:
- exact operator commands;
- no stale `r170876`;
- no `-Pn` in Scenario 1;
- all four Scenario 2 commands present;
- no Case A experiment;
- Case C topology correct;
- pfil_onlyip evidence wording not overstated;
- no exact named-rule log attribution;
- no cross-system clock inference;
- .56.100 not identified;
- no result leakage.

## 22. QA

Run:
```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_2.md
uv run python scripts/audit_ieee_citations.py work/do-an/CHAPTER_2.md
git diff --check
```

## 23. Git

Commit on:
`feature/x5-chapter-2-product-aligned`

Suggested message:
`rewrite(ch2): align chapter with final product evidence`

Push remote.

Do not merge main.

## 24. Handoff

Return:
1. commit SHA;
2. remote SHA;
3. word count;
4. 7 H2 / 20 H3 verification;
5. list of structural changes from R4;
6. exact-command audit;
7. Case C topology audit;
8. Case A removal confirmation;
9. result-leakage audit;
10. QA results;
11. clean status.

Final status:
`X5_PRODUCT_ALIGNED_R1_READY_FOR_EXTERNAL_REVIEW`

Stop.

Do not self-declare PASS.
Do not open Chapter 3.
