# REPORT-WIDE ARGUMENT ENRICHMENT RESEARCH

Status: `R0_MANAGER_RESEARCH_COMPLETE`  
Date: 2026-10-06  
Purpose: extract useful reasoning/structure patterns from academic and professional vulnerability-assessment literature without copying their prose or importing unsupported technical claims.

## 1. Sources reviewed for report architecture

### A. NIST SP 800-115 — Technical Guide to Information Security Testing and Assessment
Source:
https://csrc.nist.gov/pubs/sp/800/115/final

Useful structural lesson:
- security assessment is a process, not a tool command;
- planning defines objectives, scope and constraints;
- discovery includes information gathering, scanning, service identification and vulnerability analysis;
- reporting occurs throughout the assessment;
- exploit/attack is a distinct validation phase, not something that can be inferred from scanning.

Application to this report:
- Chapter 2 must explain the order of measurements and why the experiment deliberately stops before exploit validation;
- Chapter 3 must report observations before interpretation;
- Chapter 4 must handle mitigation, residual risk and limitations.

### B. Goel & Mehtre (2015) — Vulnerability Assessment & Penetration Testing as a Cyber Defence Technology
Source:
https://doi.org/10.1016/j.procs.2015.07.458

Useful structural lesson:
- vulnerability assessment is proactive and should lead to remediation decisions;
- findings have value when connected to a repeatable process and defensive action, not when presented as isolated scanner output.

Application:
- connect Scenario 1/2 to the reason Case B/C exist;
- make retest part of the experimental logic;
- avoid a "command diary" style.

### C. Universitas Gadjah Mada thesis — Network Vulnerability Assessment di PPTIK Universitas Gadjah Mada
Source:
https://etd.repository.ugm.ac.id/penelitian/detail/37330

Useful structural lesson:
- network vulnerability assessment is framed from an operational need, then moves through environment/context acquisition, scanning and deeper validation;
- the assessment method is justified before findings are listed.

Application:
- Chapter 2 should state why each data source exists and why remote scanning alone is insufficient;
- Chapter 4 should connect technical findings to control decisions.

### D. University of Piraeus bachelor dissertation — Study and evaluation of open-source tools for security testing
Source:
https://dione.lib.unipi.gr/xmlui/handle/unipi/19530

Useful structural lesson:
- tool selection is part of methodology and should be tied to assessment objectives rather than described as a generic tool catalogue.

Application:
- Kali/Nmap/NSE should be explained by the measurement questions they answer;
- Metasploit should not remain as an active lab tool if it is not used in the canonical experiment.

### E. Politecnico di Torino master thesis — Vulnerability Assessment tools aggregator implementation
Source:
https://webthesis.biblio.polito.it/8017/

Useful structural lesson:
- vulnerability assessment should expose the observable attack surface while acknowledging tool limits;
- proactive assessment needs a coherent view across multiple observations.

Application:
- the report's distinctive contribution is the separation of network reachability, protocol surface, remote vulnerability signal and local patch state.

### F. Telkom University paper — Vulnerability Assessment ... Menggunakan Acunetix dan NMAP
Source:
https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/id/article/view/19972

Useful structural lesson:
- methodology, findings and remediation should be visibly connected;
- findings are stronger when the report makes clear what tool produced which class of evidence.

Application:
- Chapter 3 should use result-oriented tables;
- Chapter 4 should convert findings into bounded recommendations.

## 2. Technical authorities retained for factual claims

The report must continue to prefer primary/authoritative sources over sample reports.

Key existing authorities:
- Microsoft MS17-010 bulletin:
  https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010
- Microsoft MS17-010 verification guide:
  https://support.microsoft.com/en-us/security/how-to-verify-that-ms17-010-is-installed
- Nmap smb-vuln-ms17-010 documentation/source:
  https://nmap.org/nsedoc/scripts/smb-vuln-ms17-010.html
- NIST SP 800-115:
  https://csrc.nist.gov/pubs/sp/800/115/final
- Microsoft SMBv1 enable/disable guidance:
  https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3
- NIST SP 800-41 Rev.1 for firewall policy.

Sample reports/theses are **structural exemplars**, not truth authority for this lab.

## 3. Central thesis argument to use across the report

The report should no longer read as:

> "Open port → SMBv1 → run vulnerability script → mitigation."

That chain is too simplistic and invites invalid inference.

The report-wide argument should instead be:

> **Đánh giá an ninh SMB/MS17-010 phải phân tách các lớp quan sát khác nhau. Khả năng tiếp cận dịch vụ, phương ngữ giao thức được chấp nhận, tín hiệu từ công cụ kiểm tra lỗ hổng và trạng thái bản vá cục bộ không đồng nhất. Vì vậy, đề tài xây dựng một quy trình đo theo tầng, đối chiếu quan sát từ xa với trạng thái máy chủ, rồi kiểm thử hai biện pháp giảm thiểu ở hai lớp khác nhau để xác định chính xác "điều gì thay đổi" và "điều gì không thay đổi".**

This is the red thread of the whole report.

## 4. Three research questions expressed in reader-facing logic

The existing RQ1–RQ4 remain canonical. For prose flow, they should be grouped into three reader questions:

### Reader Question A — What creates the SMB/MS17-010 assessment problem?
- what SMB is;
- why ports 139/445 alone are not vulnerability proof;
- why SMBv1 matters;
- why MS17-010 is tied to SMBv1 implementation and patch state.

Main chapters: 1.

### Reader Question B — How can the state be measured without overclaiming?
- why an isolated/recoverable virtual lab is used;
- why measurement moves from host/service discovery → port state → version/protocol → signing → vulnerability-oriented NSE;
- why local patch verification is a separate axis;
- why an inconclusive scanner output must remain UNKNOWN.

Main chapters: 2–3.

### Reader Question C — What changes when defensive controls are applied?
- Case B changes protocol configuration/surface;
- Case C changes path/network reachability;
- neither is equivalent to applying the missing patch;
- each control has a different residual-risk profile.

Main chapters: 3–4.

## 5. Required logical rhythm inside technical sections

Every substantive technical subsection should answer six questions, but without turning them into explicit QA labels in student-facing prose:

1. **Why is this step needed?**
2. **What exactly is being measured or changed?**
3. **Why is this method/tool appropriate for that variable?**
4. **What was directly observed?**
5. **What conclusion is supported, and what conclusion is not supported?**
6. **Why does the next step logically follow?**

Recommended paragraph rhythm:

`reason → method → observation → bounded interpretation → transition`

This is the main mechanism for making the report feel authored rather than generated from a command log.

## 6. Chapter-specific enrichment

### Chapter 1 — Theory must prepare the experiment

Current strengths:
- detailed SMB mechanism;
- ports/dialects/signing;
- MS17-010 technical background;
- Nmap/NSE mechanism;
- inference boundaries.

Critical defects to correct:
1. stale statement says the lab machine is Windows 7;
2. the MS17-010 table calls Windows 7 SP1 the main target;
3. the risk-condition subsection says the project selected Windows 7 SP1 x64;
4. Metasploit is described as an active canonical tool;
5. an exploit module is described as part of the experiment;
6. the theory-to-lab table includes "actual exploitability" tested with Metasploit;
7. a process diagram ends with Metasploit validation;
8. the text discusses SYSTEM/exploit evidence as if it is part of project evidence.

Required revision:
- realign all lab references to Windows Server 2012 R2;
- use Microsoft verification threshold for Windows Server 2012 R2;
- retain EternalBlue/exploitation only as theoretical impact/background where it explains severity;
- explicitly state that canonical experiment does **not** perform exploit/RCE validation;
- remove Metasploit from active experimental methodology;
- refocus Chapter 1 tool section on Kali + Nmap + NSE + local Windows verification;
- make the end of Chapter 1 explain the four evidence axes used later:
  1. reachability/service exposure;
  2. protocol surface;
  3. remote vulnerability-oriented signal;
  4. local patch state.

### Chapter 2 — Move from "what was configured" to "why the design is valid"

Keep the approved 7 H2 / 20 H3 structure unless a bounded change is separately approved.

Add design rationale in-place:

#### 2.1
Explain:
- why a controlled, recoverable lab is necessary;
- why one scanner vantage point and one target simplify causal attribution;
- limitation: this also reduces generalizability.

#### 2.2
Explain:
- why Windows Server 2012 R2 is suitable for this canonical experiment: it matches the actual target and Microsoft provides explicit MS17-010 local-verification criteria;
- why Kali is the measurement station;
- why snapshots are used for repeatability/restoration, not as security evidence.

#### 2.3
Explain why Scenario 1 must precede Scenario 2:
- a vulnerability-oriented script is uninterpretable if host/service reachability and SMB surface have not first been established.

#### 2.4
Explain why four NSE measurements are separate:
- port state;
- dialects;
- signing;
- MS17-oriented script output.
Do not collapse them into one "security state."

#### 2.4.3
Strengthen the reason for local patch verification:
- a remote scanner can be inconclusive;
- Microsoft provides host-side KB/srv.sys verification;
- therefore local patch state is an independent evidence axis, not a fallback way to rewrite scanner output.

#### 2.5
Explain why Case B and Case C were selected:
- Case B = protocol-layer intervention;
- Case C = network-path intervention;
- both can be retested against the same baseline observations;
- this creates a controlled before/after comparison across different defense layers.

#### 2.6
Explain why raw outputs, local state and screenshots are kept:
- reproducibility;
- traceability;
- ability to distinguish observation from interpretation.

### Chapter 3 — Results must read as an experiment, not a screenshot album

For each section:
- first paragraph states the question answered by the section;
- results follow in measurement order;
- table compresses repeated facts;
- figure appears only when it adds direct visual evidence;
- final paragraph states the strongest supported result and the inference boundary;
- transition explains why the next experiment is necessary.

Do not introduce recommendation/risk ranking here.

Specific logic:
- 3.1 establishes the starting state needed for every later comparison;
- 3.2 establishes observable SMB exposure before any vulnerability-oriented inference;
- 3.3 tests the specialized remote signal and demonstrates why UNKNOWN must remain UNKNOWN;
- 3.4 asks what changes when SMBv1 is disabled while patch state remains unchanged;
- Case C asks what changes when the network path is filtered while Windows state remains unchanged;
- synthesis compares changes by layer, not by vague "more secure/less secure" language.

### Chapter 4 — This is where the thesis should become analytical

Required argument order:
1. define the four evidence axes;
2. interpret baseline risk without claiming remote VULNERABLE;
3. assess Case B as protocol-surface reduction;
4. assess Case C as reachability/access-control reduction;
5. explain patching as a distinct corrective control supported by Microsoft guidance, despite no canonical Case A;
6. compare defense layers by mechanism, coverage, dependency and residual risk;
7. evaluate CIA impact carefully;
8. disclose threats to validity;
9. give deployment recommendations in priority/order;
10. require retest after change.

The central conclusion should be:
- mitigation layers are complementary;
- disabling SMBv1 or filtering traffic changes exposure;
- these changes do not rewrite local patch state;
- remote UNKNOWN cannot be used as a safety certificate;
- patching, protocol hardening, access control and retesting form defense-in-depth.

## 7. What not to import from sample reports

Do not copy the common weaknesses observed in public lab reports:
- "445 open = vulnerable";
- "SMBv1 enabled = EternalBlue confirmed";
- "Nmap produced no warning = safe";
- adding exploitation only to make the demo look impressive;
- one screenshot per command;
- long tool descriptions disconnected from research questions;
- generic cybersecurity introductions unrelated to the lab;
- recommendations unsupported by observed results.

## 8. Desired final reader experience

A lecturer should be able to answer, without opening the repository:

1. Why was this topic worth testing?
2. Why were these exact systems/tools chosen?
3. Why is the measurement order valid?
4. What did each measurement establish?
5. What did it not establish?
6. Why was local patch verification necessary?
7. Why do Case B and Case C represent different controls?
8. What changed after each control?
9. What risk remains?
10. What should an administrator do, and in what order?

If any chapter cannot support these questions, the chapter is not yet final.
