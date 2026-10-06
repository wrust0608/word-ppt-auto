# RG1 CHAPTER 1 EXTERNAL REVIEW R1

Date: 2026-10-06  
Branch: `feature/rg1-ch1-argument-realignment`  
Executor candidate: `4cff2beb0e3823112d60e08d21f89773783ccf81`  
Verdict: **84/100 — REVISE_BLOCKING**

## 1. Executive finding

The R1 rewrite is directionally much stronger than the historical Chapter 1.

What should be preserved:
- Windows Server 2012 R2 is now the canonical target;
- Metasploit is removed as an active experimental tool;
- exploit/RCE remains theory only;
- 1.3.4 is correctly reoriented toward local patch verification;
- the old linear "four levels ending in exploitation" model is replaced by a four-axis evidence model;
- Chapter 1 now creates a much clearer bridge toward Chapters 2 and 3.

However, R1 is not ready for approval because several new statements overstate what the primary sources or canonical experiment support, and the source-audit artifact contains extensive Source-ID mapping errors.

No structural rewrite is required.

## 2. Score

| Category | Score |
|---|---:|
| Canonical experiment alignment | 19/20 |
| Chapter-level logic and flow | 19/20 |
| Technical precision / inference boundaries | 15/20 |
| Source/citation provenance | 13/20 |
| Author voice / academic readability | 18/20 |
| **Total** | **84/100** |

Blocker groups: **9 bounded correction groups**.

## 3. What passes

### 3.1 Canonical-target correction — PASS
R1 successfully removes Windows 7 as the active lab target and uses Windows Server 2012 R2.

### 3.2 Metasploit / exploit-as-method removal — PASS
Metasploit is no longer an active canonical lab tool. RCE exploitation is explicitly separated from the performed experiment.

### 3.3 Four-axis architecture — PASS
The replacement of the old linear "level 1 -> exploit" ladder with:
1. reachability;
2. protocol surface;
3. remote scanner signal;
4. local patch state
is the correct report-wide logic.

### 3.4 Local patch verification subsection — PASS in concept
Using Microsoft host-side verification to explain why remote scan output and local patch state are independent is academically strong.

## 4. Blocker A — Source Audit is not trustworthy in its current form

`RG1_CHAPTER1_SOURCE_AUDIT_R1.md` claims 1:1 mapping to `SOURCE_LEDGER.md`, but many mappings are objectively wrong.

Examples:
- audit says 1.1.4 uses RFC 1001/1002 as `S005`, while `S005` in the ledger is Microsoft MS17-010;
- audit says 1.2.1 Microsoft MS17-010 is `S007`, while ledger `S007` is SMB security enhancements and `S005` is the bulletin;
- audit says 1.2.3 Rapid7/NVD use `S001, S025`, while actual ledger entries are `S013` and `S011`;
- audit says 1.2.5 Rapid7 = `S025`, but `S025` is NIST SP 800-41;
- audit says 1.2.6 uses CISA `S014, S031`, but `S031` is Microsoft SMB 3.1.1 pre-authentication integrity;
- audit says Kali = `S017`, while Kali is `S026`;
- audit says Nmap = `S018`, while Nmap Network Scanning is `S017`;
- audit says 1.3.3 includes `S019`, which is a RECHECK Metasploit book;
- audit says pfSense documentation is represented by `S015`, but `S015` is Microsoft WannaCrypt.

This invalidates the audit's statement that all technical claims are mapped 1:1.

Required:
- rebuild the source audit from the actual current `SOURCE_LEDGER.md`;
- do not invent Source IDs;
- do not map a bibliography entry to a ledger source merely because the numbering looks similar;
- do not use RECHECK sources for new claims;
- if a chapter claim is unsupported by a VERIFIED source, narrow/remove the claim rather than fabricating a mapping.

## 5. Blocker B — "safe threshold" language overstates Microsoft's patch-verification guidance

Microsoft's support page calls `6.3.9600.18604` the **minimum updated srv.sys version** for Windows 8.1 / Windows Server 2012 R2.

Do not call it:
- `ngưỡng an toàn`;
- "safety threshold";
- proof the whole server is secure.

Required wording:
- `phiên bản srv.sys tối thiểu đã cập nhật đối với MS17-010`;
- `minimum updated srv.sys version`.

The classification `UNPATCHED` may remain bounded to MS17-010.

## 6. Blocker C — Nmap patched-branch interpretation is too causal

The actual Nmap source:
- treats `0xc0000205` as the unpatched signal;
- logs `STATUS_ACCESS_DENIED` / `STATUS_INVALID_HANDLE` as **likely patched**;
- returns the string `This system is patched.`.

The source does **not** prove the causal explanation currently written in R1:
> "driver đã được bổ sung cơ chế kiểm soát tham số"

Required:
- describe what the script maps those error codes to;
- do not infer a specific internal patch mechanism from those branches unless independently sourced;
- preserve the distinction between tool output and local patch verification.

Also clarify that the Nmap script reports MS17-010 broadly and its output metadata identifies CVE-2017-0143; do not use the script result as direct experimental proof specifically of CVE-2017-0144/EternalBlue exploitability.

## 7. Blocker D — UNKNOWN theory must not assign the canonical no-output cause

R1 lists network filtering, timeout, anonymous IPC$ denial as causes that can prevent the probe.

These can be presented only as **possible failure points in the script path**, not as the cause of the project's canonical NSE04 no-output result.

Required student-facing distinction:
- theory: the script can fail before/while obtaining the probe response;
- experiment: the canonical run produced no usable script verdict and the cause was not established.

Keep:
`UNKNOWN != SAFE`.

Do not write a sentence that lets a reader infer the project knows why NSE04 produced no output.

## 8. Blocker E — SMBv1 hardening language is too absolute and conflicts with Case B evidence

R1 currently uses wording such as:
- "loại bỏ hoàn toàn tính năng SMBv1";
- "đóng kín bề mặt tấn công cũ";
- "loại bỏ hoàn toàn bề mặt tiếp xúc";
- "triệt tiêu hoàn toàn bề mặt tiếp xúc";
- "mọi gói tin thăm dò hay tấn công ... đều bị chặn ngay từ Negotiate".

This is too strong and also conflicts with the canonical Case B observation:
- `EnableSMB1Protocol=False`;
- `FS-SMB1=Installed`.

Required:
- distinguish disabling the SMBv1 **server protocol configuration** from uninstalling the Windows feature;
- say the measured SMBv1 dialect no longer appears after the server configuration change;
- describe this as protocol-surface reduction / removal of the measured SMBv1 server path;
- do not claim every SMBv1 attack path is universally eliminated;
- preserve `SMBv1 disabled != FS-SMB1 uninstalled`;
- preserve `SMBv1 disabled != PATCHED`.

## 9. Blocker F — Patching and "complete immunity" wording is too absolute

R1 says a patched host is:
- "hoàn toàn miễn nhiễm" to the FEA overflow;
- patching "xử lý triệt để tận gốc";
- exploit code "không còn khả năng" to trigger the overflow.

Required:
- state that Microsoft updates address the MS17-010 vulnerabilities covered by the bulletin;
- a host meeting the Microsoft patch-verification criteria is classified as updated for MS17-010;
- do not convert this into an overall security guarantee;
- avoid universal language about every exploit variant/path.

This is especially important because Chapter 4 must later discuss residual risk and defense-in-depth.

## 10. Blocker G — Availability-risk paragraph contains unsupported probability language

Section 1.2.5 says availability is:
> "nguy cơ thường trực và có xác suất xảy ra cao nhất"

The cited Rapid7 material can support a crash/BSOD risk during kernel exploitation, but this probability ranking is not established.

Required:
- remove the "highest probability" ranking;
- say kernel-memory corruption can cause instability/BSOD and therefore availability impact is a relevant risk;
- do not state probabilities without data.

Also avoid implying any malformed probe can cause a crash.

## 11. Blocker H — Case C theory leaks results and includes an invalid same-subnet generalization

R1 currently says:
- the port changes from `open` to `filtered`;
- the firewall protects without server reboot;
- the control cannot protect if the threat originates from a host in the same internal segment.

Problems:
1. `open -> filtered` is an experimental Case C result and belongs in Chapter 3, not Chapter 1 theory.
2. No-reboot language is unnecessary here.
3. "same subnet" does not determine whether traffic traverses an inline transparent bridge; topology/path does.

Required Chapter 1 wording:
- firewall policy can restrict SMB reachability for traffic that traverses the controlled path;
- whether traffic is observed as filtered is measured later;
- traffic that bypasses the controlled firewall path is outside that control;
- network filtering does not alter local patch state.

Do not reveal Case C result.

## 12. Blocker I — Retest paragraph claims workload validation the project did not perform

R1 requires retest to confirm:
> "chia sẻ tệp qua SMBv2 vẫn duy trì khả năng hoạt động bình thường"

The canonical experiment does not contain a full SMB2/3 workload-continuity test.

Required:
- separate **operational best practice** from **what this project measured**;
- operationally, compatibility testing is advisable after disabling a legacy protocol;
- in this project, Case B retest only establishes the selected configuration/dialect/NSE observations;
- it does not prove full SMB2/3 workload continuity or zero downtime.

This must align with the already locked Case B plan.

## 13. Additional editorial corrections

### 13.1 SYSTEM wording
Do not say SYSTEM "belongs to user space."

Better:
- SYSTEM / LocalSystem is a Windows security context/account;
- observing a SYSTEM security context is not by itself proof that code was executing in kernel mode.

Microsoft documentation explicitly separates security context from user-mode/kernel-mode execution.

### 13.2 Windows Server 2012 R2 selection rationale
Avoid unsupported claims such as:
- "phổ biến";
- "phản ánh sát thực tế hạ tầng".

Prefer evidence-based rationale:
- it is the actual target used in the experiment;
- it is covered by MS17-010;
- Microsoft provides explicit host-side verification criteria;
- it exposes the protocol/patch distinctions the experiment needs to measure.

### 13.3 "negative result proves safe"
Replace:
> "nhận được phản hồi chứng minh an toàn (negative result)"

with:
> "kết quả âm tính theo tiêu chí của phép đo".

A negative result is not a general proof of safety.

## 14. R2 scope

R2 is a bounded technical/source correction.

Keep:
- the Chapter 1 heading architecture;
- 1.3.4 local patch-verification focus;
- 1.3.5 theory-to-experiment bridge;
- 1.4.1 four-axis model;
- overall report logic.

Do not restore:
- Metasploit;
- Windows 7 as the lab target;
- exploit validation;
- old VLAN/client model.

## 15. Final gate

Verdict:

`RG1_CH1_R1_REVISE_BLOCKING`

After R2:
- independently recheck Chapter 1;
- independently recheck the entire Source Audit against `SOURCE_LEDGER.md`;
- if clean, issue final external PASS;
- only after explicit user approval may RG2 Chapter 2 enrichment open.
