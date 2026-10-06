# RG1 — CHAPTER 1 CANONICAL REALIGNMENT & ARGUMENT ENRICHMENT

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/rg1-ch1-argument-realignment`  
Manager base: `e8659013b8a77f3b38031d9c762945f80f302a62`

## 0. Objective

Rewrite **Chapter 1 only** so it becomes a coherent theoretical foundation for the current canonical experiment.

This is not a cosmetic rewrite.

The current Chapter 1 contains stale remnants from an older Windows 7 / Metasploit / exploitation design. Those remnants must be removed or reframed.

The revised Chapter 1 must prepare the reader to understand the actual canonical lab:

- Kali Linux measurement station;
- Windows Server 2012 R2 target;
- Nmap/NSE remote measurements;
- local Windows patch verification;
- no canonical exploit/RCE result;
- Scenario 1 / Scenario 2;
- Case B protocol hardening;
- Case C network access-control mitigation.

## 1. Start and lineage

Run:

```bash
git fetch origin
git checkout feature/rg1-ch1-argument-realignment
git pull --ff-only origin feature/rg1-ch1-argument-realignment
git status --short
git rev-parse HEAD
git merge-base --is-ancestor e8659013b8a77f3b38031d9c762945f80f302a62 HEAD
```

If lineage fails, STOP.

## 2. Mandatory read order

Read fully:

1. `work/do-an/CHANGE_REQUEST_CR-2026-10-06-REPORT-WIDE-ARGUMENT-ENRICHMENT.md`
2. `work/do-an/REPORT_WIDE_ARGUMENT_ENRICHMENT_RESEARCH.md`
3. `work/do-an/REPORT_WIDE_ARGUMENT_CONTRACT.md`
4. `work/do-an/RESEARCH_MAP.md`
5. `work/do-an/ARGUMENT_MAP.md`
6. `work/do-an/EXPERIMENTAL_TRUTH_MATRIX.md`
7. `work/do-an/AUTHOR_VOICE.md`
8. `work/do-an/SOURCE_LEDGER.md`
9. `work/do-an/SOURCE_RECONCILIATION_PLAN.md`
10. `work/do-an/CHAPTER_1.md`
11. `work/do-an/DEPTH_REVIEW_2026_10_04.md`
12. `work/do-an/PILOT_CHAPTER_REVIEW.md`

Then inspect approved Chapter 2 and completed Chapter 3 headings only for continuity:
- `work/do-an/CHAPTER_2.md`
- `work/do-an/CH3_31_BASELINE_DRAFT_R1.md`
- `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
- `work/do-an/CH3_33_SCENARIO2_DRAFT_R1.md`

Do not rewrite Chapters 2–4 in RG1.

## 3. Authority

For experiment scope and facts:

1. current `EXPERIMENTAL_TRUTH_MATRIX.md`;
2. current `RESEARCH_MAP.md`;
3. current `ARGUMENT_MAP.md`;
4. current approved Chapter 2 / Chapter 3 facts;
5. verified primary sources in `SOURCE_LEDGER.md`.

Historical Chapter 1 wording loses authority when it conflicts with the above.

## 4. Central narrative Chapter 1 must support

Chapter 1 should make the reader understand this sequence:

1. SMB is the service/protocol family being assessed.
2. TCP 139/445 expose paths to SMB but an open port is not a vulnerability verdict.
3. SMBv1 matters because MS17-010 affects SMBv1 server handling.
4. Presence of SMBv1 still does not prove MS17-010 is exploitable.
5. Nmap/NSE can produce remote observations, but a scanner verdict is not identical to local patch state.
6. Microsoft provides host-side patch verification for Windows Server 2012 R2.
7. Therefore the experiment later separates:
   - reachability/service exposure;
   - protocol surface;
   - remote vulnerability-oriented signal;
   - local patch state.
8. Defensive controls later operate on different layers:
   - patching = corrective host update;
   - disabling SMBv1 = protocol hardening;
   - pfSense filtering = network access control.
9. The canonical experiment does not perform RCE exploitation.

## 5. Mandatory stale-content audit

Before writing, search Chapter 1 for at least:

```text
Windows 7
Metasploit
ms17_010_eternalblue
auxiliary/scanner
exploit/windows
SYSTEM
khai thác
thực thi mã thử nghiệm
Client nghiệp vụ
ba VLAN
phân vùng khác
sau vá
```

Record every hit in the changelog and classify:
- KEEP_AS_THEORY
- REWRITE
- REMOVE

No stale hit may remain unreviewed.

## 6. Required structural direction

Keep the broad Chapter 1 architecture:

- 1.1 SMB fundamentals
- 1.2 MS17-010
- 1.3 tools / measurement basis
- 1.4 evaluation / mitigation principles
- chapter conclusion

Do not radically expand the number of headings.

### 6.1 Section 1.1

Keep the technical explanation of:
- SMB client/server;
- SMBv1/v2/v3;
- TCP 139/445;
- request/response and negotiation.

Required fixes:
- any sentence that calls Windows 7 the lab target must be removed/replaced;
- references to modern SMB signing/encryption must not be falsely applied to Windows Server 2012 R2 if unsupported;
- add a short natural transition explaining why protocol/dialect observations become necessary in later measurements.

Do not turn 1.1 into an SMB encyclopedia.

### 6.2 Section 1.2

Keep:
- MS17-010 bulletin;
- relevant CVE background;
- EternalBlue as theoretical severity/context;
- patch/hotfix concepts;
- impact.

Critical distinction:
- theory may explain that successful exploitation can lead to RCE;
- report must never imply this project performed or confirmed canonical RCE.

The affected-software / patch table must:
- identify **Windows Server 2012 R2** as the canonical lab target;
- use KB4012213 / KB4012216 and minimum updated srv.sys 6.3.9600.18604 where relevant;
- not label Windows 7 as the experimental target.

In the "conditions" subsection:
- canonical target = Windows Server 2012 R2;
- remove the old reason based on Metasploit compatibility;
- rationale should connect to actual experiment and Microsoft verification data.

### 6.3 Section 1.3

Required structure:

#### 1.3.1 Kali Linux
Keep concise:
- role as security-testing workstation;
- relation to actual lab.

#### 1.3.2 Nmap
Explain by measurement role:
- host/service discovery;
- SYN port state;
- service/version observation.

#### 1.3.3 Nmap Scripting Engine
Explain:
- smb-protocols;
- smb2-security-mode;
- smb-vuln-ms17-010;
- direct script behavior and limits.

Must explicitly support the later rule:
`UNKNOWN != SAFE`.

#### 1.3.4 Replace the current Metasploit section

Replace:
`1.3.4. Nền tảng kiểm thử Metasploit Framework`

with a subsection centered on **local patch verification**.

Recommended heading:

`1.3.4. Cơ sở xác minh trạng thái bản vá cục bộ trên Windows Server 2012 R2`

Explain:
- KB/hotfix verification;
- srv.sys version verification;
- Microsoft minimum updated version 6.3.9600.18604;
- why host-side verification is independent of remote scanning.

Do not claim the Chapter 3 result here.

#### 1.3.5 Theory-to-experiment bridge

Rebuild the table so it maps theory to the actual canonical measurements.

Rows should cover:
- TCP 139/445;
- SMB dialects;
- SMB signing;
- remote MS17-010-oriented NSE signal;
- local patch state;
- Case B protocol hardening;
- Case C network access control;
- retest.

Remove:
- Metasploit;
- active exploit validation;
- "actual exploitability" as an experiment row;
- MSF Auxiliary.

The table should answer:
"What variable is being observed, by what method, and what does it not prove?"

## 7. Section 1.4 must be fundamentally realigned

### 7.1 Replace the old four ascending "levels"

The current framework culminates in canonical exploit validation and is incompatible with the project.

Replace it with a **four-axis evidence model**, not a ladder:

1. Network reachability / service exposure.
2. Protocol surface.
3. Remote vulnerability-oriented scanner signal.
4. Local patch state.

The axes are independent enough that one cannot overwrite another.

Use a comparison table rather than "Level 1 → Level 4 exploit".

Mandatory boundaries:
- `445 OPEN != vulnerable`
- `SMBv1 enabled != MS17-010 confirmed`
- `UNKNOWN != SAFE`
- local UNPATCHED does not convert remote UNKNOWN into VULNERABLE.

### 7.2 Limits / false interpretation subsection

Strengthen the logic around:
- collection failure vs interpretation error;
- no result vs negative result;
- remote observation vs host state;
- why multiple observations are needed.

Do not mention Metasploit cross-checking.

Do not claim a false negative unless evidence proves it.

### 7.3 Mitigation principles subsection

Rewrite around **control layers**:

- patching:
  - official corrective action;
  - not experimentally performed as canonical Case A;
- SMBv1 disable:
  - protocol-surface reduction;
  - compatibility caveat;
  - not equal patching;
- firewall/pfSense:
  - network-path/access-control layer;
  - not equal patching;
- retest:
  - confirms the targeted observable changed;
  - does not grant an "overall safe" certificate.

Remove stale old-topology language:
- "Client nghiệp vụ";
- "phân vùng khác";
- three-VLAN logic.

Do not leak Case C results.

## 8. Intro and transitions

Add a short Chapter 1 opening that explains why the theory is organized this way.

It should not be generic cybersecurity background.

It should say, in academic Vietnamese, that the chapter provides only the concepts required to distinguish:
- service reachability;
- protocol behavior;
- vulnerability-oriented signal;
- patch state;
- defensive control layer.

At the end of major sections, add short transitions only when they make the reasoning clearer.

Do not use the same formula repeatedly.

## 9. Author voice

Must follow `AUTHOR_VOICE.md`.

Required:
- academic Vietnamese;
- neutral third person;
- natural prose;
- no internal workflow vocabulary;
- no "canonical", "gate", "evidence ID", "ground truth" in student-facing text;
- avoid translated jargon that sounds unnatural;
- use Client / Server only where already appropriate;
- prefer concrete technical subject over abstract corporate wording.

Avoid:
- "bản tin" as generic protocol data;
- "ngăn xếp mạng" in ordinary connection explanations;
- template-like opening paragraphs;
- excessive bolded slogan rules.

The five inference boundaries may appear where genuinely useful, but do not turn Chapter 1 into a checklist.

## 10. Source discipline

Use only verified sources already allowed by `SOURCE_LEDGER.md` unless a new source is independently verified and entered into the ledger.

Primary sources preferred.

At minimum, verify every revised claim involving:
- Windows Server 2012 R2 MS17-010 patch threshold;
- Nmap script behavior;
- SMBv1 disable guidance;
- SMB protocol/signing behavior.

Do not cite the sample theses/reports as technical authority.

They are structural exemplars only.

## 11. Bibliography/citation audit

After revision:

- every visible [n] must resolve;
- bibliography numbering must be sequential;
- no orphan bibliography entry;
- no cited source missing from bibliography;
- no source left only because old Metasploit prose was removed;
- no accidental reuse of a reference number for a different source.

If references [21]/[22] become unused, remove them and normalize numbering as needed.

Record exact citation changes in the source audit.

## 12. Length and depth

Current Chapter 1 is approximately 8k words.

Target:
- approximately 7,000–8,500 words;
- depth retained;
- stale/excess tool material removed;
- rationale and transitions added without rambling.

Do not inflate word count merely to meet a target.

## 13. Files to modify/create

Allowed modification:
- `work/do-an/CHAPTER_1.md`

Allowed new files:
- `work/do-an/RG1_CHAPTER1_CHANGELOG_R1.md`
- `work/do-an/RG1_CHAPTER1_SOURCE_AUDIT_R1.md`
- `work/do-an/RG1_CHAPTER1_SELF_REVIEW_R1.md`

Do not modify:
- Chapter 2;
- Chapter 3;
- Chapter 4;
- evidence;
- screenshots;
- Experimental Truth Matrix;
- report-wide argument contract;
- research map;
- argument map;
- SOURCE_LEDGER unless a genuinely new technical source is required. Prefer not to add one in RG1.

Do not build DOCX.

## 14. Changelog requirements

The changelog must include:

1. every stale Windows 7 lab-target reference and resolution;
2. every Metasploit/active-exploit reference and resolution;
3. every old-topology/Client-business reference and resolution;
4. structural changes to 1.3.4 / 1.3.5 / 1.4.1;
5. citation-number changes;
6. word-count before/after;
7. headings before/after.

## 15. Source audit requirements

For each major technical subsection:
- list the principal verified sources used;
- state any claim removed because source support was insufficient;
- confirm Windows Server 2012 R2 patch threshold;
- confirm Nmap script interpretation boundary;
- confirm SMBv1 disable guidance.

## 16. Self-review — lecturer test

Answer PASS/FAIL with evidence:

1. Does Chapter 1 use Windows Server 2012 R2 as the only canonical lab target?
2. Is Metasploit absent as an active experimental tool?
3. Is canonical exploit/RCE validation absent?
4. Does theory still explain why MS17-010 is serious?
5. Can a reader understand why port/dialect/scanner/patch state are distinct?
6. Does the chapter explain why local patch verification is necessary?
7. Does the mitigation discussion distinguish patching / protocol hardening / network access control?
8. Is the old three-VLAN/business-client model absent?
9. Does Chapter 1 naturally prepare Chapter 2?
10. Are citations complete and defensible?
11. Does the prose sound like a Vietnamese student technical report rather than an internal QA document?

Any FAIL = do not commit.

## 17. Project QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
git diff --check
```

Also run any existing citation/publication lint relevant to Chapter 1.

## 18. Git

Commit message:

`rewrite(ch1): realign theory with canonical SMB experiment`

Push:
`feature/rg1-ch1-argument-realignment`

Do not merge.

## 19. Final handoff

Return:

1. branch;
2. starting SHA;
3. final local/remote SHA;
4. files changed;
5. Chapter 1 word count before/after;
6. heading count before/after;
7. stale-reference audit;
8. Metasploit/exploit removal audit;
9. Windows Server 2012 R2 alignment audit;
10. four-axis framework summary;
11. bibliography/citation audit;
12. project QA;
13. git status;
14. remaining non-blocking concerns.

Final state:

`RG1_CH1_R1_READY_FOR_EXTERNAL_REVIEW`

Then STOP.

Do not start RG2.
Do not rewrite Chapter 2.
Do not rewrite Chapter 3.
Do not build DOCX.
