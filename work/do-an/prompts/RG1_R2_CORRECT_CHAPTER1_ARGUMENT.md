# RG1 R2 — CORRECT CHAPTER 1 TECHNICAL & SOURCE BOUNDARIES

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/rg1-ch1-argument-realignment`  
R1 candidate: `4cff2beb0e3823112d60e08d21f89773783ccf81`

## 0. Objective

Correct only the bounded issues identified in:

`work/do-an/RG1_CHAPTER1_EXTERNAL_REVIEW_R1.md`

Do not redesign Chapter 1.

Preserve the successful R1 architecture:
- Windows Server 2012 R2 canonical target;
- no Metasploit as active lab tool;
- no canonical exploit/RCE validation;
- 1.3.4 local patch verification;
- 1.3.5 theory-to-experiment bridge;
- 1.4.1 four-axis evidence model.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/rg1-ch1-argument-realignment
git pull --ff-only origin feature/rg1-ch1-argument-realignment
git status --short
git rev-parse HEAD
```

Read first:
1. `work/do-an/RG1_CHAPTER1_EXTERNAL_REVIEW_R1.md`
2. `work/do-an/CHAPTER_1.md`
3. `work/do-an/RG1_CHAPTER1_SOURCE_AUDIT_R1.md`
4. `work/do-an/SOURCE_LEDGER.md`
5. `work/do-an/REPORT_WIDE_ARGUMENT_CONTRACT.md`
6. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`.

## 2. Allowed modifications

Modify only:
- `work/do-an/CHAPTER_1.md`
- `work/do-an/RG1_CHAPTER1_CHANGELOG_R1.md`
- `work/do-an/RG1_CHAPTER1_SOURCE_AUDIT_R1.md`
- `work/do-an/RG1_CHAPTER1_SELF_REVIEW_R1.md`

Do not modify:
- SOURCE_LEDGER;
- Research Map;
- Argument Map;
- Experimental Truth Matrix;
- Chapters 2–4;
- evidence;
- DOCX.

If a sentence cannot be supported by an existing VERIFIED source, narrow/remove it.

Do not add a new source merely to preserve an overclaim.

## 3. Rebuild Source Audit from the real ledger

The current Source Audit contains many incorrect Source-ID mappings.

Rebuild every row using the actual current `SOURCE_LEDGER.md`.

Important examples:
- S005 = Microsoft MS17-010 bulletin;
- S007 = SMB security enhancements;
- S011 = NVD CVE-2017-0144;
- S013 = Rapid7 EternalBlue technical source;
- S015 = Microsoft WannaCrypt;
- S017 = Gordon Lyon / Nmap Network Scanning;
- S018 = Nmap `smb-vuln-ms17-010.nse`;
- S025 = NIST SP 800-41 Rev.1;
- S026 = Kali Linux;
- S029 = `smb-protocols.nse`;
- S031 = Microsoft SMB 3.1.1 pre-authentication integrity;
- S032 = Microsoft MS17-010 local verification.

Do not invent RFC mappings that are not in the ledger.

Do not cite S014, S001, S003, S004, S009, S016 or S019 as VERIFIED support for a new claim because they are RECHECK.

For every bibliography item in Chapter 1, record its real ledger Source ID or state that it is an already verified equivalent source if applicable.

The Source Audit must no longer claim "1:1 verified" unless the row truly matches.

## 4. Correct Microsoft patch-verification terminology

Replace all:
- `ngưỡng an toàn`;
- `safety threshold`.

Use:
- `phiên bản srv.sys tối thiểu đã cập nhật`;
- `minimum updated srv.sys version`.

For Windows Server 2012 R2:
`6.3.9600.18604`.

Keep classification bounded:
- updated / not updated for MS17-010;
- `UNPATCHED` for MS17-010 where applicable.

Do not imply whole-system safety.

## 5. Correct Nmap script interpretation

Base wording on the actual Nmap source.

Allowed:
- `0xc0000205` -> script treats as unpatched/vulnerable signal;
- `0xc0000022` and `0xc0000008` -> script logs "likely patched" and returns "This system is patched."

Do not say those error codes prove:
- a particular internal parameter-check mechanism;
- a specific patch implementation path.

Add the distinction:
- the script is an MS17-010 remote detector;
- its report metadata uses CVE-2017-0143;
- this does not by itself prove CVE-2017-0144/EternalBlue exploitability in this project's host.

Keep local patch verification independent.

## 6. Correct UNKNOWN theory vs canonical experiment

In theory:
- describe that the script can fail to obtain a usable probe result at connection/session/read stages.

Do not state:
- canonical NSE04 had no result because of anonymous IPC$ denial;
- canonical NSE04 had no result because of filtering/timeout;
- any known cause for the project's no-output result.

For the project:
`UNKNOWN / NO USABLE SCRIPT RESULT`
and:
`cause not established`.

## 7. Remove absolute SMBv1 language

Search Chapter 1 and support artifacts for:
- `triệt tiêu`
- `hoàn toàn bề mặt`
- `đóng kín`
- `mọi gói tin`
- `loại bỏ hoàn toàn tính năng SMBv1`
- `bắt buộc`

Correct contextually.

For Case B/theory use:
- SMBv1 server configuration is disabled;
- measured `NT LM 0.12` no longer appears in the later retest;
- this reduces/removes the observed SMBv1 server protocol surface from that measurement path.

Mandatory:
`SMBv1 disabled != FS-SMB1 uninstalled`
`SMBv1 disabled != PATCHED`.

Do not describe `Set-SmbServerConfiguration -EnableSMB1Protocol $false` as uninstalling the Windows feature.

## 8. Bound patching wording

Remove:
- `hoàn toàn miễn nhiễm`;
- `triệt để tận gốc`;
- universal claims that an exploit can no longer cause the overflow.

Use:
- Microsoft updates address the MS17-010 vulnerabilities covered by the bulletin;
- meeting Microsoft's local verification criterion supports classification as updated for MS17-010.

Do not convert patch status into a whole-system security guarantee.

## 9. Fix availability-impact prose

Remove probability ranking:
- `xác suất xảy ra cao nhất`.

Use:
- kernel-memory corruption can lead to instability/BSOD;
- therefore availability impact is a relevant risk.

Do not claim every malformed or probe packet can crash the server.

## 10. Fix Case C theory

Chapter 1 must not publish Case C results.

Remove/rewrite:
- `open -> filtered` as if already observed;
- "no reboot needed";
- "same subnet cannot be protected".

Use:
- firewall filtering can restrict SMB reachability for traffic traversing the controlled path;
- actual observed Nmap state is reported later in Chapter 3;
- traffic that does not traverse the controlled firewall path is outside that control;
- filtering does not change local patch state.

Do not leak the actual Case C outcome.

## 11. Fix retest/workload continuity

Do not say the project's retest confirms:
- SMB2 file-sharing workload works normally;
- no interruption;
- compatibility.

Separate:
- operational recommendation: compatibility should be tested after legacy-protocol changes;
- project evidence: selected Case B retests cover configuration/dialects/NSE only.

Explicitly preserve:
- remaining SMB2/3 dialect observations do not prove full workload continuity.

## 12. Fix SYSTEM wording

Replace wording equivalent to:
`SYSTEM belongs to user space`.

Use:
- SYSTEM/LocalSystem is a Windows security context/account with extensive local privileges;
- observing a SYSTEM security context is not itself evidence that code executed in kernel mode.

Do not conflate identity/security context with processor execution mode.

## 13. Fix target-selection rationale

Remove unsupported market/generalization language:
- "phổ biến";
- "phản ánh sát thực tế hạ tầng";
- other prevalence claims without source.

Use evidence-based rationale:
- Windows Server 2012 R2 is the actual experiment target;
- it is in the MS17-010 affected-product family;
- Microsoft publishes explicit KB/srv.sys verification criteria;
- it supports the protocol-state vs patch-state comparison required by the design.

## 14. Fix negative-result language

Replace:
`phản hồi chứng minh an toàn (negative result)`

with:
`kết quả âm tính theo tiêu chí của phép đo`.

No scanner negative result is a general certificate of safety.

## 15. Campaign-source audit

Recheck WannaCry/NotPetya claims against the actual bibliography and ledger.

Use:
- Microsoft WannaCrypt source for WannaCry;
- Microsoft Petya/NotPetya source for NotPetya.

Do not claim CISA support if the cited chapter sources are Microsoft and ledger S014 remains RECHECK.

Remove unsupported quantitative damage claims unless the cited VERIFIED source explicitly supports them.

## 16. Required search audit

Before handoff, search all four RG1 files for:

```text
ngưỡng an toàn
hoàn toàn miễn nhiễm
triệt tiêu hoàn toàn
đóng kín bề mặt
mọi gói tin
xác suất xảy ra cao nhất
phản hồi chứng minh an toàn
thuộc không gian người dùng
Client nghiệp vụ
ba VLAN
phân vùng khác
Metasploit
exploit/windows
ms17_010_eternalblue
```

Student-facing Chapter 1 must have zero problematic uses.

Some terms such as "khai thác" may remain as theory; manually review every occurrence.

## 17. Source-audit integrity tests

Programmatically verify:
- every Source ID mentioned in RG1 source audit exists in SOURCE_LEDGER;
- every Source ID title/organization in the audit matches the ledger row;
- no RECHECK Source ID is presented as VERIFIED support;
- chapter bibliography references are mapped to the correct actual source;
- no invented pfSense/CISA/RFC mapping remains.

Include the audit output in the handoff.

## 18. Self-review

Update the self-review honestly.

Do not say 11/11 PASS unless:
- source audit is actually correct;
- no Chapter 3 result leakage remains;
- no full workload-continuity claim remains;
- no whole-system safety claim remains.

## 19. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CHAPTER_1.md
git diff --check
```

Also run citation/bibliography consistency audit.

## 20. Git

Commit:
`fix(ch1): correct technical and source boundaries R2`

Push:
`feature/rg1-ch1-argument-realignment`

Do not merge.

## 21. Handoff

Return:
1. starting SHA;
2. final local/remote SHA;
3. modified file list;
4. all nine blocker groups with before/after summary;
5. corrected Source-ID mapping audit;
6. RECHECK-source usage audit;
7. patch terminology audit;
8. Nmap code-path wording audit;
9. UNKNOWN cause-boundary audit;
10. SMBv1 disable-vs-uninstall audit;
11. Case C no-result-leak audit;
12. workload-continuity audit;
13. SYSTEM wording audit;
14. citation/bibliography audit;
15. word count/headings;
16. QA results;
17. clean git status.

Final state:
`RG1_CH1_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open RG2.
Do not modify Chapter 2.
Do not modify Chapter 3.
Do not build DOCX.
