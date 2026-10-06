# X7C1 EXTERNAL REVIEW R1 — SECTION 3.3 SCENARIO 2

Date: 2026-10-06  
Branch: `feature/x7c1-ch3-scenario2-draft`  
Executor R1 candidate: `f9c3d13d3036113a21dcb5221598426a6da3f7da`  
Verdict: **87/100 — REVISE_BLOCKING**

## 1. Executive finding

The approved X7C0 presentation geometry has been implemented correctly:

- exactly 1 H2 + 2 H3;
- exactly 1 Bảng 3.4;
- exactly 1 Hình 3.6;
- no NSE01/02/03 screenshot duplication;
- the Hình 3.6 crop is visually clear and preserves command, port state, `Nmap done`, and returned shell prompt;
- the Case B transition does not reveal Case B results;
- the core `UNKNOWN != SAFE` and local-UNPATCHED-vs-remote-UNKNOWN separation is present.

However, the R1 prose is not yet ready for user approval.

Several passages regress from the reviewer-final X7C0 wording and reintroduce stronger interpretations that were deliberately removed during planning. The self-review also contains factual QA contradictions.

No redesign and no new crop are required.

## 2. Score

| Category | Score |
|---|---:|
| Structure / experimental flow | 19/20 |
| Table / figure / crop implementation | 20/20 |
| Core UNKNOWN / UNPATCHED boundary | 18/20 |
| Evidence-bounded technical wording | 15/20 |
| Student-facing voice / self-review fidelity | 15/20 |
| **Total** | **87/100** |

Blocking correction groups: **6**.

## 3. What passes

### 3.1 Structure — PASS

Keep exactly:

- `3.3.1. Khảo sát điều kiện kết nối và thuộc tính giao thức SMB (NSE-SMB-01 đến NSE-SMB-03)`
- `3.3.2. Đánh giá dấu hiệu lỗ hổng MS17-010 và đối chiếu trạng thái bản vá (NSE-SMB-04)`

No additional H3/H4 is needed.

### 3.2 Presentation — PASS

Keep:

- Bảng 3.4 only;
- Hình 3.6 only;
- no presentation images for NSE01/02/03.

The current Hình 3.6 crop is visually suitable and does not need regeneration.

### 3.3 Core classification logic — PASS

The draft correctly preserves the central distinction:

- remote NSE-SMB-04 = `UNKNOWN / NO USABLE SCRIPT RESULT`;
- UNKNOWN is not a literal Nmap string;
- `UNKNOWN != SAFE`;
- local patch state = `UNPATCHED`;
- local UNPATCHED does not convert remote UNKNOWN into VULNERABLE;
- remote UNKNOWN does not erase local UNPATCHED.

This architecture must remain unchanged in R2.

## 4. Blocking correction A — dialect wording regressed from the approved plan

The reviewer-final X7C0 plan deliberately narrowed the dialect wording to:

`smb-protocols ghi nhận 5 phương ngữ`.

R1 reintroduces stronger statements such as:

- `đàm phán và lập danh mục các phương ngữ ... mà ... chấp thuận`;
- `máy chủ hỗ trợ 5 phương ngữ`;
- `hỗ trợ đàm phán`;
- `Hỗ trợ đa phương ngữ`;
- `tính tương thích ngược`.

These are unnecessary stronger interpretations.

Required correction in prose and Bảng 3.4:

- say that `smb-protocols` **recorded/listed five dialects**;
- list the five observed values;
- retain the literal `[dangerous, but default]` annotation;
- do not infer additional protocol-support semantics beyond the observed output.

Also remove:

`Chú thích này phản ánh ... tính chất mất an toàn của giao thức SMB thế hệ đầu tiên.`

In Section 3.3, report the annotation as tool output; do not convert it into a broader risk statement.

Keep:

`SMBv1 enabled != MS17-010 confirmed`.

## 5. Blocking correction B — signing explanation should remain measurement-bounded

The direct NSE-SMB-03 output is:

`Message signing enabled but not required`

for dialect 3.0.2.

R1 adds a general explanatory statement that the mechanism:

`bảo vệ tính toàn vẹn gói tin`

and that clients are not required to establish signing.

This theory is not needed to report the measurement and would require external support if expanded.

Required wording direction:

- report the exact remote result;
- say it applies to the recorded 3.0.2 output;
- preserve independence from local signing flags;
- do not expand into a general signing-security explanation in this results section.

## 6. Blocking correction C — NSE04 prose/table/manifest regressed from reviewer-final precision

The reviewer-final X7C0 plan explicitly avoided several expressions that R1 reintroduced.

### 6.1 Table

R1 Bảng 3.4 says:

`Kết quả này phản ánh giới hạn của phép đo từ xa`.

Remove this.

Use:

`Kết quả này chỉ cho phép phân loại là chưa xác định trong phạm vi phép đo; nguyên nhân của việc không có đầu ra script khả dụng không được xác lập. UNKNOWN != SAFE.`

The missing result does not establish *why* the tool produced no usable verdict.

### 6.2 Script execution wording

R1 says:

- NSE-SMB-04 `được kích hoạt`;
- the measurement `gọi kịch bản chuyên biệt`.

Prefer the directly evidenced formulation:

`Lệnh Nmap được thực thi với tùy chọn --script smb-vuln-ms17-010.`

Do not describe unobserved internal loading/activation mechanics.

### 6.3 Completion wording

R1 says:

- `dấu nhắc shell trả về bình thường`;
- crop manifest says `phiên quét kết thúc bình thường`.

The direct evidence is narrower:

- output reaches the `Nmap done` line;
- a shell prompt appears afterward;
- no corresponding error is displayed in the recorded output.

Use those visible facts.

Do not characterize the process as “normal” beyond what is displayed.

### 6.4 Cause wording

R1 says the cause:

`không thể xác định`.

Use the locked wording:

`nguyên nhân ... không được xác lập từ bộ bằng chứng hiện có`.

This avoids a universal impossibility claim.

The crop image itself must remain unchanged.

## 7. Blocking correction D — local UNPATCHED restatement is broader than Section 3.1

The preferred Scenario 2 cross-reference is already sufficient:

`Mục 3.1 đã phân loại trạng thái bản vá cục bộ là UNPATCHED; dữ kiện này được giữ độc lập với kết quả NSE từ xa.`

R1 then restates the patch evidence using:

- `ngưỡng cập nhật an toàn tối thiểu`;
- `các bản cập nhật thay thế tương ứng`.

These phrases are broader than the approved Section 3.1 wording.

Preferred R2 action:

**Remove the detailed re-derivation from Section 3.3** and keep the restrained cross-reference to 3.1.

If detail is retained, it must match the locked formulation exactly:

- numeric `srv.sys = 6.3.9600.16421`;
- Microsoft minimum updated version threshold = `6.3.9600.18604`;
- the **observed local hotfix inventory** does not record KB4012213, KB4012216, or a **mapped superseding update containing the MS17-010 fix**.

Do not use “safe threshold” or an omniscient claim about all replacement updates.

## 8. Blocking correction E — exploitation paragraph is over-expanded for student prose

The approved boundary is simple:

- Scenario 2 contains no exploitation step;
- no exploitation/RCE result is claimed.

R1 expands this into a list of:

- RCE;
- reverse shell;
- Meterpreter.

This is not technically false, but it is unnecessary for the student-facing results section and makes the prose resemble an internal scope memo.

Preferred R2 wording:

`Kịch bản 2 dừng ở phạm vi rà quét NSE; không có bước khai thác hoặc kết quả thực thi mã từ xa được ghi nhận trong kịch bản này.`

Do not list exploit-session tooling in student prose.

The internal self-review may retain the detailed scope terms if needed.

## 9. Blocking correction F — self-review contains demonstrably false QA statements

### 9.1 Word-count range

Self-review reports:

- prose words = **1,719**;
- target = approximately **1,100–1,600**;
- then states the draft is “within” that range.

That is false.

R2 should lightly tighten repetition and target approximately **1,300–1,550 prose words**.

Do not remove substantive evidence merely to reduce length.

### 9.2 Forbidden-term result contradicts the actual draft

The handoff/self-review claims:

`Meterpreter / reverse shell = 0`

but the actual R1 student prose contains both terms, together with `RCE`.

This means the reported search result does not describe the final draft bytes.

R2 must:

1. perform all searches **after the final edit**;
2. report actual counts;
3. never report zero when the term exists;
4. preferably remove these detailed exploit-session terms from student prose as required above.

### 9.3 Self-review wording must follow final draft bytes

Update any internal rows that still say:

- dialects were “negotiated successfully”;
- shell returned “normally”;
- scan completed “normally”.

The self-review must describe the final R2 text, not an older draft state.

## 10. Lecturer / thesis-defense assessment

The scientific structure is good, but the current prose occasionally sounds more certain than the evidence.

A defense panel can reasonably ask:

- “Nmap only lists dialects; why are you claiming broader protocol support semantics?”
- “What evidence says the scan was ‘normal’ rather than simply reaching Nmap done?”
- “Why does a missing Host script block prove a scanner limitation?”
- “Why are you re-deriving patch state in 3.3 when 3.1 already established it?”
- “Why does your self-review say forbidden terms are absent when they are visibly in the draft?”

R2 should make these questions easy to answer by narrowing the prose to direct evidence.

## 11. Final gate

Verdict:

`X7C1_R1_REVISE_BLOCKING`

Do not open X7D.

R2 must be a bounded correction only.

After R2, perform a final independent external review before asking the user to approve Section 3.3.
