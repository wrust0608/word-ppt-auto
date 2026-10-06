# X7D1 SECTION 3.4 CASE B — EXTERNAL REVIEW R1

Date: 2026-10-07  
Branch: `feature/x7d1-ch3-caseb-draft`  
Executor candidate: `55c35e8e3ca2b1ef331c51f265d8e4712a3381c0`

Verdict: **88/100 — REVISE_BLOCKING**

## 1. Overall finding

R1 is close to approval.

The approved structure is correct:
- 1 H2;
- 2 H3;
- Bảng 3.5;
- Hình 3.7;
- Hình 3.8.

The two derived crops are visually good and preserve the intended evidence.

The technical story is also basically correct:
- SMB1 server configuration changes True -> False;
- FS-SMB1 remains Installed;
- LanmanServer is observed Running;
- TCP 445 remains OPEN in the retest;
- NT LM 0.12 is absent from the retest dialect list;
- local patch state remains UNPATCHED;
- remote MS17 result remains UNKNOWN / NO USABLE SCRIPT RESULT.

No structural rewrite is required.

However, R1 still contains a small group of statements that exceed the evidence boundary, one factual error in the crop manifest, unnecessary repetition, and one out-of-scope repository-infrastructure modification.

## 2. What passes

### Presentation geometry — PASS
- Hình 3.7 crop `872x310` is readable and focused.
- Hình 3.8 crop `1280x400` is readable and preserves the complete command/result/prompt.
- no Before image;
- no Action image;
- no combined NSE04 image.

### Bảng 3.5 — PASS
The eight-row comparison remains consistent with the approved X7D0 plan.

### UNKNOWN boundary — PASS
The draft correctly states:
- no usable script verdict;
- cause not established;
- `UNKNOWN != SAFE`.

### Chapter boundary — PASS
No Case C result is leaked and no Chapter 4 solution ranking is introduced.

## 3. Blocker A — unrelated modification of `scripts/validate_project.py`

The X7D1 commit changes six files, including:

`scripts/validate_project.py`

This task is a Chapter 3 writing/crop task. It is not authorized to carry a project-validator behavior change.

The validator change may be a reasonable infrastructure fix, but it must not ride inside the Case B content commit.

R2 requirement:
- restore `scripts/validate_project.py` byte-for-byte to the X7D1 starting HEAD `2b2bf5bd41f40f899f7e59d39bd7d3184c051751`;
- do not modify any project infrastructure file.

If `validate_project.py` then reports only a false-positive link caused by Markdown examples inside the manager prompt, report that exact QA limitation in the handoff; do not modify the validator again.

## 4. Blocker B — causal explanation for TCP 445 OPEN exceeds the approved wording boundary

Current draft says the port remains open:

> "... do dịch vụ LanmanServer vẫn đang chạy để phục vụ các phương ngữ SMB2 và SMB3."

and later:

> "Cổng 445 vẫn mở, cho phép luồng dữ liệu tiếp cận dịch vụ chia sẻ tệp."

These statements go beyond the locked X7D0 wording.

The direct Case B observation is only:
- host up;
- `445/tcp open microsoft-ds`;
- four dialect values recorded.

R2 requirement:
- remove the causal phrase about why TCP 445 is OPEN;
- remove the claim that OPEN "allows traffic to access the file-sharing service";
- use the direct wording:
  `Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại.`

Keep:
`445 OPEN != vulnerable`.

Also revise the earlier baseline sentence:
> "Mốc xuất phát này cho phép máy chủ tiếp nhận cả SMBv1 lẫn SMB2/3."

Prefer:
> "Ở mốc trước can thiệp, các phép đo đã trình bày tại Mục 3.2 ghi nhận cả SMBv1 và các phương ngữ SMB2/3."

This separates configuration from remote observation.

## 5. Blocker C — protocol-retest prose is too causal / too strong

Current draft says:

> "Phép đo này chứng minh rằng khi cờ EnableSMB1Protocol chuyển thành False, máy chủ không còn đưa SMBv1 vào danh sách phương ngữ phản hồi..."

The experiment records an after-state; one retest does not need a strong causal "chứng minh rằng" formulation.

R2 requirement:
Use evidence-bounded wording such as:

> "Trong phép đo lại sau can thiệp, kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ."

Optional:
> "Kết quả này phù hợp với thay đổi cấu hình SMBv1 đã ghi nhận trên máy chủ."

Do not say:
- successful negotiation;
- successful handshake;
- server "no longer accepts" SMBv1;
- complete protocol removal.

## 6. Blocker D — local patch lineage is overstated

Current draft says:

> "driver srv.sys chưa từng được cập nhật."

and earlier says the intervention:
> "không thay đổi mã nhị phân driver."

The evidence supports:
- local state in Section 3.1 was UNPATCHED;
- Case B manifest records unchanged srv.sys;
- Case B contains no patch-install action.

It does not support a lifetime statement that the driver "has never been updated".

R2 requirement:
Use:

> "Trạng thái bản vá cục bộ tiếp tục được giữ ở phân loại UNPATCHED theo mốc đã xác lập tại Mục 3.1 và metadata của Case B; Case B không ghi nhận thao tác cài bản vá."

Do not say:
- `srv.sys chưa từng được cập nhật`;
- Hình 3.7 re-measured srv.sys;
- the intervention itself proves binary files did not change.

If mentioning unchanged binary state, attribute it explicitly to the Case B metadata/lineage, not the screenshot.

## 7. Blocker E — crop manifest contains a factual column error

In the Hình 3.7 crop manifest, R1 says:

> `LanmanServer` ở trạng thái `Running` (chế độ khởi động `Running`).

The screenshot has columns:
- Name
- Status
- StartType

and shows:
- `LanmanServer`
- `Running` under **Status**.

The crop does not visibly provide `Running` as StartType.

R2 requirement:
- delete the claim `chế độ khởi động Running`;
- state only that `LanmanServer` is observed with Status = Running;
- do not infer an unreadable/blank StartType value from the crop.

Also prefer "FS-SMB1 remains Installed" over unnecessary claims about exact component files "being on disk".

## 8. Blocker F — product-level repetition is still too high

The prose count is 1,385 words, at the top edge of the prompt target.

More importantly, the same facts are repeated in:
- local-boundary paragraph;
- Bảng 3.5;
- UNKNOWN paragraph;
- four-layer numbered list;
- conclusion.

The current roadmap explicitly requires Chapter 3 to avoid becoming a QA-like collection of repeated safeguards.

R2 requirement:
- target approximately **1,100–1,250 prose words**;
- keep all technical meaning;
- use Bảng 3.5 as the compression device;
- collapse the four-layer numbered list into one concise synthesis paragraph;
- merge repetitive UNKNOWN/OPEN boundary wording where possible;
- keep one concise conclusion.

Do not delete necessary evidence boundaries; state each important boundary once at the point where it matters.

## 9. Minor editorial corrections required in R2

Replace:
> "Dấu nhắc lệnh kết thúc xác nhận phiên kiểm tra hoàn tất bình thường."

with:
> "Dấu nhắc PowerShell xuất hiện trở lại sau các lệnh kiểm tra."

This avoids treating the prompt itself as a proof of overall success.

In the conclusion, replace:
> "Can thiệp đã thu hẹp bề mặt phương ngữ nhưng cổng 445 vẫn mở đối với mạng nội bộ."

with a direct measurement formulation, for example:
> "Sau can thiệp, danh sách phương ngữ ghi nhận từ trạm Kali không còn NT LM 0.12, trong khi TCP 445 vẫn được ghi nhận OPEN."

Avoid generalizing from the Kali vantage point to the entire internal network.

## 10. R2 scope

Keep unchanged:
- section headings;
- Bảng 3.5 structure;
- figure numbering;
- approved crop rectangles;
- derived images unless a byte-for-byte regeneration is needed;
- X7D0 technical locks.

Modify only:
- `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- `work/do-an/CH3_34_CASEB_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`
- revert `scripts/validate_project.py` to the starting HEAD.

Do not open Case C.
Do not assemble Chapter 3.
Do not build Word.

## 11. Final gate

Current verdict:

`X7D1_CASEB_R1_REVISE_BLOCKING`

After R2:
- independently recheck raw NSE02/NSE04;
- visually recheck Hình 3.7/Hình 3.8;
- recheck the draft as a student-facing thesis section;
- if clean, issue final external PASS and ask for explicit user approval before integration/X7E.
