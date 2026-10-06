# X7C0 EXTERNAL REVIEW R1 — SCENARIO 2 PLAN

Date: 2026-10-06  
Branch: `feature/x7c0-ch3-scenario2-plan`  
Executor R1 candidate: `4868942a5a6c86eb3feb03ce6110edfbcd2892e2`  
Verdict: **90/100 — REVISE_MINOR_BLOCKING**

## 1. Executive finding

The overall Scenario 2 presentation geometry is strong and should be preserved.

The plan correctly recognizes that NSE-SMB-01/02/03 repeat information already visible in Section 3.2 and that NSE-SMB-04, despite sparse output, is the most valuable direct figure for Section 3.3.

The following design direction passes:

- 2 proposed H3;
- 1 compact result table (Bảng 3.4);
- NSE01 screenshot DROP;
- NSE02 screenshot DROP;
- NSE03 screenshot DROP;
- NSE04 screenshot KEEP as tentative Hình 3.6;
- no second mini-table for UNKNOWN vs UNPATCHED;
- local UNPATCHED and remote UNKNOWN remain separate axes.

However, several factual and methodological wording issues must be corrected before user approval.

No redesign is required.

## 2. Score

| Category | Score |
|---|---:|
| Evidence coverage / isolation | 20/20 |
| Academic structure / reader flow | 19/20 |
| Figure/table selection | 20/20 |
| Technical interpretation boundaries | 17/20 |
| Provenance / factual transcription | 14/20 |
| **Total** | **90/100** |

Blocking corrections: **7 bounded issues**.

## 3. What passes

### 3.1 Figure selection — PASS

Independent visual inspection confirms:

- NSE01 is redundant with Section 3.2 B4 and is better summarized in Bảng 3.4.
- NSE02 is redundant with the dialect evidence already retained in Hình 3.5.
- NSE03 is redundant with signing output already retained in Hình 3.5.
- NSE04 is uniquely valuable because the command visibly specifies `smb-vuln-ms17-010`, the target is up, TCP 445 is open, Nmap reaches `Nmap done`, and no `Host script results:` block appears.

Keeping only NSE04 as the standard figure is academically preferable to four terminal screenshots.

### 3.2 Image provenance — PASS

Independent SHA-256 verification from repository bytes:

- NSE01: `56c0a8cbb22bee4f22a21587ec38581525881ed95c3eff40db930db91956fda4`
- NSE02: `e57de3aea8688fa73551bbc43b67a258907741de6ca09111219eec0a2413ceb0`
- NSE03: `5fc4507628dc0568ecea02ee5124558b0f0835bea289405ca316b124c1fe5cfe`
- NSE04: `c970e56481a920061416949ea7543dcb96f1f2f99635dbe201131073202e14ac`

The proposed NSE04 crop rectangle `x=0, y=24, width=1280, height=330` is suitable in principle and preserves the command, port state, completion line and returned shell prompt.

### 3.3 UNKNOWN / UNPATCHED architecture — PASS

The core logic is correct:

- remote NSE-SMB-04 = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- `UNKNOWN != SAFE`;
- local baseline patch state = `UNPATCHED`;
- local UNPATCHED does not convert remote UNKNOWN into VULNERABLE;
- no FALSE NEGATIVE classification;
- local and remote signing observations remain independent.

This conceptual split must be preserved in R2.

## 4. Blocking correction A — Baseline must not be renamed “Case A”

The transition currently says:

`Baseline Case A`.

This is forbidden by the project truth.

There is no completed canonical Case A patch experiment.

The approved experimental sequence contains:

- baseline;
- Scenario 1;
- Scenario 2;
- Case B;
- Case C.

Required correction:

Use wording equivalent to:

`Sau khi hoàn tất trạng thái baseline và hai kịch bản đo đạc ban đầu...`

Never call baseline “Case A”.

Do not imply Case A was executed.

## 5. Blocking correction B — Case B transition currently describes the wrong retest scope

The transition says Case B will:

`thực hiện lặp lại toàn bộ các phép đo khảo sát và kiểm tra lỗ hổng`.

This is factually wrong.

The approved Case B method repeats selected measurements:

- protocol retest (equivalent to NSE-SMB-02);
- MS17-010 script retest (equivalent to NSE-SMB-04).

It does not repeat all Scenario 2 measurements.

Required transition direction:

- one controlled factor changes: SMBv1 server configuration;
- selected protocol and MS17-010 measurements are repeated;
- do not reveal Case B results;
- do not call this “đánh giá hiệu quả” yet, because broad effectiveness analysis belongs to Chapter 4.

## 6. Blocking correction C — TCP OPEN must not become application/service readiness

Bảng 3.4 currently says:

`Hai cổng dịch vụ SMB sẵn sàng tiếp nhận kết nối qua mạng.`

Direct NSE01 evidence supports only:

- TCP 139/445 OPEN;
- SYN-ACK from the Kali vantage point.

Required wording:

`Từ trạm Kali, TCP 139 và 445 được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.`

Do not use:
- sẵn sàng tiếp nhận;
- file-sharing success;
- authenticated SMB access;
- workload availability.

Keep:
`445 OPEN != vulnerable`.

## 7. Blocking correction D — remove “necessary/prerequisite” theory from SMBv1 result

The plan and claim map describe SMBv1 presence as:

- `điều kiện cần`;
- `điều kiện tiên quyết cho khả năng bị ảnh hưởng`.

These theoretical formulations are unnecessary in a measured-results section and are not direct Scenario 2 observations.

Required wording:

- NSE-SMB-02 records `NT LM 0.12 (SMBv1)` plus 2.0.2 / 2.1 / 3.0 / 3.0.2;
- the Nmap annotation `[dangerous, but default]` may be reported as tool output;
- SMBv1 presence alone does not establish MS17-010.

Keep exactly:

`SMBv1 enabled != MS17-010 confirmed`.

Do not introduce a “necessary condition” claim in Section 3.3.

## 8. Blocking correction E — separate visible NSE04 facts from the UNKNOWN classification

The current artifacts sometimes overstate what the screenshot itself proves.

Directly visible / raw-supported facts:

- Nmap command specifies `--script smb-vuln-ms17-010`;
- target is up;
- TCP 445 is open;
- output reaches `Nmap done`;
- no `Host script results:` block is present;
- no Nmap/script error message is displayed in the recorded output.

Interpretation layer:

- remote classification = `UNKNOWN / NO USABLE SCRIPT RESULT`.

Required corrections:

1. Do not say the screenshot itself “proves UNKNOWN”; it proves the absence of a usable script result block. UNKNOWN is the bounded project classification of that observation.
2. Prefer `lệnh Nmap được thực thi với --script smb-vuln-ms17-010` over stronger internal-mechanism wording such as `script được nạp/kích hoạt`.
3. Do not claim the image proves the absence of every possible network/script cause. Say only that no corresponding error is displayed in the recorded output.
4. Remove unnecessary absolutes such as `hoàn toàn vắng mặt` and `bằng chứng không thể thay thế`.
5. The 1.35-second duration is factual but has no analytical value; omit it from the proposed public table and prose unless specifically needed.

The NSE04 image remains KEEP.

## 9. Blocking correction F — local UNPATCHED cross-reference must reuse the approved Section 3.1 formulation

The Scenario 2 plan currently restates local patch status too broadly as:

`Không tìm thấy KB4012213, KB4012216 hay các bản Rollup thay thế`.

The approved Section 3.1 finding is more precise:

- numeric `srv.sys = 6.3.9600.16421`;
- Microsoft minimum updated threshold = `6.3.9600.18604`;
- observed local hotfix inventory does not record KB4012213, KB4012216, or a mapped superseding update containing the MS17-010 fix;
- local classification = `UNPATCHED`.

R2 should not re-derive or broaden the patch analysis.

Preferred Scenario 2 wording:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

If details are repeated internally, preserve the exact “observed inventory” qualifier.

## 10. Blocking correction G — provenance / terminology inconsistencies

### 10.1 Wrong Nmap version in self-review

Self-review writes:

`Nmap 7.95`

Direct raw Scenario 2 evidence records:

`Nmap 7.99`.

Correct it.

Do not synthesize a raw header from memory.

Use the exact command-lineage matrix and direct raw header.

### 10.2 Do not claim a cause for `--privileged`

The project lock only requires two provenance layers:

- operator command does not contain `--privileged`;
- Nmap-recorded argv does contain normalized `--privileged`.

Do not add an unneeded causal statement such as “Nmap automatically inserted it because it ran as root” unless separately evidenced.

### 10.3 Measurement label is not an internal Evidence ID

The plan says student-facing tables must not use:

`Evidence ID (NSE-SMB-01)`.

This is incorrect categorization.

`NSE-SMB-01` through `NSE-SMB-04` are the approved measurement labels from Chapter 2 and are allowed in the student report.

Internal identifiers that must stay out of student prose include:

- `S2-RAW-01`;
- `S2-IMG-04`;
- `S2-C01`;
- repository file paths.

Fix this rule while keeping the table rows named NSE-SMB-01..04.

## 11. Additional bounded correction — exploitation scope claim

Claim `S2-C15` currently says Scenario 2:

`không gửi mã khai thác tấn công`.

That describes low-level script behavior beyond what the staged evidence establishes.

Use the project-level fact instead:

- no canonical exploitation step is present;
- no exploit/RCE/reverse-shell/Meterpreter result or artifact is present.

Do not characterize the internal packet/payload behavior of the NSE script unless supported by an approved source.

## 12. Lecturer / defense-readiness assessment

The plan's visual strategy is strong.

From a thesis examiner perspective, the best Section 3.3 geometry is indeed:

- one compact four-row Bảng 3.4;
- one Hình 3.6 focused on NSE-SMB-04;
- restrained reference back to repeated NSE01–03 observations;
- a clear explanation of why a completed scan without a verdict remains UNKNOWN;
- an explicit separation between remote UNKNOWN and local UNPATCHED.

The remaining issues are precision issues that a technical panel could challenge quickly. They must be corrected before user approval.

## 13. Final gate

Verdict:

`X7C0_R1_REVISE_MINOR_BLOCKING`

Do not open X7C1.

R2 must be a bounded correction of the four X7C0 planning artifacts only.

After R2, perform final independent external review before asking the user to approve the Scenario 2 plan.
