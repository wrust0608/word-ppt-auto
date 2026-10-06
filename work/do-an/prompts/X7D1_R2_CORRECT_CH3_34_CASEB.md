# X7D1 R2 — CORRECT SECTION 3.4 CASE B

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7d1-ch3-caseb-draft`  
R1 candidate: `55c35e8e3ca2b1ef331c51f265d8e4712a3381c0`

## 0. Objective

Apply a bounded R2 correction to Section 3.4 based on:

`work/do-an/X7D1_CH3_34_EXTERNAL_REVIEW_R1.md`

Do not redesign the section.

The R1 structure, Bảng 3.5, Hình 3.7 and Hình 3.8 are retained.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7d1-ch3-caseb-draft
git pull --ff-only origin feature/x7d1-ch3-caseb-draft
git status --short
git rev-parse HEAD
```

The branch must contain the reviewer commit that added:
- `X7D1_CH3_34_EXTERNAL_REVIEW_R1.md`
- this R2 prompt.

Read the external review fully before editing.

## 2. Allowed changes

Modify only:
- `work/do-an/CH3_34_CASEB_DRAFT_R1.md`
- `work/do-an/CH3_34_CASEB_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_34_CASEB_CROP_MANIFEST_R1.md`
- `scripts/validate_project.py` only to **revert it exactly to the X7D1 starting HEAD**.

Do not modify:
- images;
- raw evidence;
- approved X7D0 plan;
- Chapter 2;
- Sections 3.1–3.3;
- roadmap files.

## 3. Revert the out-of-scope validator change

Restore:

`scripts/validate_project.py`

exactly from:

`2b2bf5bd41f40f899f7e59d39bd7d3184c051751`

Example:

```bash
git checkout 2b2bf5bd41f40f899f7e59d39bd7d3184c051751 -- scripts/validate_project.py
```

Do not edit the validator again.

If project validation then reports only a broken-link false positive caused by Markdown examples in the manager prompt, record that exact limitation in the handoff. Do not change infrastructure to make the task green.

## 4. Fix TCP 445 wording

Remove causal/generalized wording such as:
- `do dịch vụ LanmanServer vẫn đang chạy để phục vụ...`
- `cho phép luồng dữ liệu tiếp cận dịch vụ chia sẻ tệp`
- `mốc xuất phát này cho phép máy chủ tiếp nhận...`

Use direct measured wording:

`Từ trạm Kali, TCP 445 được ghi nhận ở trạng thái OPEN trong phép đo lại.`

For the pre-intervention state, cross-reference the earlier remote measurements instead of claiming capability from configuration alone.

Keep:
`445 OPEN != vulnerable`.

## 5. Fix protocol-retest causality

Remove:

`Phép đo này chứng minh rằng khi cờ EnableSMB1Protocol chuyển thành False, máy chủ không còn đưa SMBv1 vào danh sách phương ngữ phản hồi...`

Use:

`Trong phép đo lại sau can thiệp, kịch bản smb-protocols ghi nhận 2.0.2, 2.1, 3.0 và 3.0.2; NT LM 0.12 (SMBv1) không xuất hiện trong danh sách phương ngữ.`

Optionally add:

`Kết quả này phù hợp với thay đổi cấu hình SMBv1 đã ghi nhận trên máy chủ.`

Do not say:
- successful negotiation;
- successful handshake;
- SMBv1 was fully removed;
- server no longer accepts SMBv1.

## 6. Fix patch-state lineage

Remove:
- `driver srv.sys chưa từng được cập nhật`;
- any lifetime-history claim;
- any implication that Hình 3.7 re-measured srv.sys.

Use:

`Trạng thái bản vá cục bộ tiếp tục được giữ ở phân loại UNPATCHED theo mốc đã xác lập tại Mục 3.1 và metadata của Case B; Case B không ghi nhận thao tác cài bản vá.`

If mentioning binary state, attribute it to Case B metadata, not to the screenshot/action alone.

## 7. Correct Hình 3.7 crop manifest

The crop shows:
- Name = LanmanServer
- Status = Running

Do not say:
- `StartType = Running`
- `chế độ khởi động Running`.

The StartType value is not visibly established by this crop.

State only:
`LanmanServer được ghi nhận với Status = Running.`

Also prefer:
`FS-SMB1 được ghi nhận Installed`
instead of unnecessary claims about exact feature files being physically present on disk.

## 8. Compress the report section

Target:
- approximately **1,100–1,250 prose words**;
- preserve 1 H2 / 2 H3;
- preserve Bảng 3.5;
- preserve Hình 3.7 and Hình 3.8.

Use Bảng 3.5 to carry repeated before/after facts.

Collapse the numbered four-layer restatement into one concise synthesis paragraph.

Do not repeat:
- `UNKNOWN != SAFE` multiple times;
- `445 OPEN != vulnerable` multiple times;
- full local before/after values after they are already in Bảng 3.5.

The section should read as a thesis result section, not a safeguards checklist.

## 9. Editorial precision

Replace:
`Dấu nhắc lệnh kết thúc xác nhận phiên kiểm tra hoàn tất bình thường.`

with:
`Dấu nhắc PowerShell xuất hiện trở lại sau các lệnh kiểm tra.`

Conclusion should stay direct and vantage-bounded.

Preferred concept:

`Sau can thiệp, danh sách phương ngữ ghi nhận từ trạm Kali không còn NT LM 0.12, trong khi TCP 445 vẫn được ghi nhận OPEN; trạng thái bản vá cục bộ vẫn UNPATCHED và phép đo MS17-010 vẫn UNKNOWN.`

Then transition to Case C without revealing its result.

## 10. Preserve all existing hard boundaries

Still required:
- `SMBv1 disabled != FS-SMB1 uninstalled`
- `SMBv1 disabled != PATCHED`
- `445 OPEN != vulnerable`
- `UNKNOWN != SAFE`

No:
- false negative;
- SAFE / NOT VULNERABLE;
- patched claim;
- syn-ack for Case B retest;
- NTSTATUS/IPC$ cause;
- workload continuity;
- zero downtime;
- Case C result;
- Chapter 4 analysis.

## 11. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_34_CASEB_DRAFT_R1.md
git diff --check
```

If `validate_project.py` fails only because of a manager-prompt Markdown-code false positive, report it explicitly instead of editing the validator.

Verify:
- presentation image SHAs unchanged;
- raw evidence SHAs unchanged;
- no files outside the allowed list changed.

## 12. Commit

Commit:

`fix(ch3): correct Case B section 3.4 R2`

Push:

`feature/x7d1-ch3-caseb-draft`

Do not merge.

## 13. Handoff

Return:
1. starting reviewer HEAD;
2. final local/remote SHA;
3. changed files;
4. prose word count/paragraph count;
5. each external-review blocker and exact fix;
6. validator-revert confirmation;
7. TCP 445 wording audit;
8. protocol-causality audit;
9. patch-lineage audit;
10. crop-manifest StartType correction;
11. repetition/compression audit;
12. QA results;
13. clean git status.

Final state:

`X7D1_CASEB_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open X7E.
Do not write Case C.
Do not assemble Chapter 3.
Do not build Word.
