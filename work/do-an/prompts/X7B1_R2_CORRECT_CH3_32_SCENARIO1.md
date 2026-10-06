# X7B1 R2 — CORRECT SECTION 3.2 SCENARIO 1 DRAFT

Status: `READY_FOR_EXECUTOR`  
Branch: `feature/x7b1-ch3-scenario1-draft`  
R1 candidate: `2bff0dead870f838284a02eea148f4c468263584`

## 0. Objective

Correct only the bounded issues identified in:

`work/do-an/X7B1_CH3_32_EXTERNAL_REVIEW_R1.md`

Do not redesign Section 3.2.

Preserve:
- exactly 1 H2 + 2 H3;
- Bảng 3.3 exactly as approved unless a reviewer wording correction below explicitly applies outside the table;
- exactly Hình 3.4 and Hình 3.5;
- current derived crop files and crop manifest;
- all X7B0 numbering and figure decisions.

Do not write Section 3.3.

## 1. Start

Run:

```bash
git fetch origin
git checkout feature/x7b1-ch3-scenario1-draft
git pull --ff-only origin feature/x7b1-ch3-scenario1-draft
git status --short
git rev-parse HEAD
```

Read first:

1. `work/do-an/X7B1_CH3_32_EXTERNAL_REVIEW_R1.md`
2. `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
3. `work/do-an/CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1.md`
4. `work/do-an/CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`
5. `work/do-an/CH3_32_SCENARIO1_CROP_MANIFEST_R1.md`
6. Scenario 1 B2–B6 raw .nmap files.

## 2. Allowed files to modify

Modify only:

- `work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md`
- `work/do-an/CH3_32_SCENARIO1_DRAFT_SELF_REVIEW_R1.md`
- `work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`

The third file is authorized for **provenance-only SHA correction** described in Section 7 below.

Do not modify:
- source evidence;
- derived images;
- crop manifest unless a direct mismatch is discovered;
- Bảng/Hình numbering;
- Section 3.1;
- claim map;
- truth matrix;
- Scenario 2/Case B/Case C.

## 3. Correct B3 wording

Replace any wording that implies ARP B3 guarantees service readiness.

The meaning must be only:

`B3 xác nhận mục tiêu 192.168.56.20 vẫn đang trực tuyến trước khi thực hiện các phép đo tiếp theo.`

Forbidden:
- bảo đảm tính sẵn sàng;
- sẵn sàng tiếp nhận kết nối;
- proves SMB is available.

## 4. Correct B4 wording

Remove application-level/absolute wording such as:

`dịch vụ chia sẻ tệp ... hoàn toàn có thể tiếp cận`.

Use the directly supported observation:

`Từ góc nhìn của trạm Kali, hai cổng TCP 139 và 445 của mục tiêu được ghi nhận ở trạng thái OPEN và phản hồi SYN-ACK.`

Retain:

`445 OPEN != vulnerable`.

Do not claim:
- firewall causality;
- authenticated SMB access;
- file-sharing workload success.

## 5. Remove security-assurance sentence

Delete:

`Một hệ thống kích hoạt SMBv1 vẫn có thể được bảo vệ an toàn nếu đã được áp dụng đầy đủ các bản vá bảo mật tương ứng.`

Do not replace it with another general recommendation or safety claim.

Keep only the bounded result:

`SMBv1 enabled != MS17-010 confirmed`.

## 6. Separate local and remote signing

Delete wording that says remote signing is:

`phù hợp với cấu hình ký số cục bộ tại Mục 3.1`.

The remote result must stand independently:

`smb2-security-mode ghi nhận Message signing enabled but not required.`

Optional bounded cross-reference:

`Đây là kết quả quan sát từ xa và được ghi nhận độc lập với các cờ cấu hình cục bộ tại Mục 3.1.`

Do not call the two layers matching/confirming.

## 7. B5 and transition wording

### B5

Replace absolute wording:

`hoàn toàn không thể`

with a measurement-bounded formulation:

`các phản hồi từ xa này chưa đủ căn cứ để định danh chính xác duy nhất phiên bản Windows Server 2012 R2`.

### Final transition

Do not promise Scenario 2 will definitively determine vulnerability.

Use meaning equivalent to:

`Mục 3.3 tiếp tục sử dụng các phép đo NSE chuyên biệt để kiểm tra dấu hiệu liên quan đến MS17-010.`

Do not reveal the Scenario 2 outcome.

## 8. Provenance-only correction to approved figure-selection metadata

In:

`work/do-an/CH3_32_SCENARIO1_FIGURE_SELECTION_R1.md`

change only the two stale SHA-256 source values:

### B5

From:
`18fbe98f79fbe44147cf75cf145377f0a8c2bdf14f24d62b9a1da87ec44ee789`

To:
`05699e248fa66ab224adc6809fb057a282d86c29c3ce2851823e07bd874f6466`

### B6

From:
`63200a40f0d2c949c25bb3ca5dbe003ba732c48bf0a0be3b76a084eb87cf1aa2`

To:
`b5b236cbe695b530b44e0af592f010f1f49bef9f5da427b9958fd9020bd651f8`

Do not change:
- KEEP/DROP;
- Hình 3.4/3.5;
- crop rectangle;
- caption;
- structure;
- any other X7B0 decision.

This is a factual provenance correction only.

## 9. Rebuild self-review claim audit from approved claim map

The R1 self-review claim numbering is shifted.

Use the exact approved mapping from:

`CH3_32_SCENARIO1_CLAIM_EVIDENCE_MAP_R1.md`

At minimum preserve:

- S1-C01 = four observed hosts;
- S1-C02 = .56.100 UNKNOWN;
- S1-C03 = target .56.20 up;
- S1-C04 = TCP 139 OPEN;
- S1-C05 = TCP 445 OPEN;
- S1-C06 = 445 OPEN != vulnerable;
- S1-C07 = B5 service/version fingerprint;
- S1-C08 = B5 fingerprint precision limit;
- S1-C09 = observed SMB dialects;
- S1-C10 = remote signing;
- S1-C11 = recorded SMB2 capabilities;
- S1-C12 = smb-os-discovery no usable output;
- S1-C13 = Scenario 1 does not establish MS17-010.

Do not invent a separate Claim ID for B3 continuity.

Remove or correct the internal self-review latency `0.00030s`; direct B3 raw is `0.00034s`, but preferably omit exact latency because it has no analytical role.

## 10. Keep the figures unchanged

Do not regenerate or modify:

- `Hinh_3_4_SMB_Version.png`
- `Hinh_3_5_SMB_NSE.png`

The final external review has independently confirmed their actual SHA-256:

- Hình 3.4:
  `513f3356792eec5f449003a43f5fa8520a7fda94d8e10d4edbb6ef62fc064964`
- Hình 3.5:
  `45faf0f03f57ce35707e1825f555fcbb6ad5e9fdee5daac7f849351ec2360a66`

The crop manifest currently matches and should remain unchanged unless your own byte verification proves otherwise.

## 11. Writing-quality pass

After technical corrections, reread Section 3.2 as a lecturer.

Prefer:
- measured observation;
- restrained interpretation;
- natural Vietnamese;
- direct explanation of what the figure proves.

Avoid:
- `hoàn toàn` where not directly supported;
- security assurance;
- repetitive self-justifying sentences;
- Chapter 4-style commentary.

Do not shorten the section aggressively merely to reduce word count.

## 12. Required searches

Search the draft for:

- `bảo đảm tính sẵn sàng`
- `hoàn toàn có thể tiếp cận`
- `được bảo vệ an toàn`
- `phù hợp với cấu hình ký số cục bộ`
- `hoàn toàn không thể`
- `xác minh chính xác liệu`

All must be **0** after correction.

Also verify:
- no `-Pn`;
- no exact identity for .56.100;
- no exact OS inference from B5;
- no MS17-010 verdict;
- no Scenario 2 outcome.

## 13. QA

Run:

```bash
uv run python scripts/validate_project.py
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python .agents/skills/thesis-research-and-writing/scripts/lint_vi_academic.py work/do-an/CH3_32_SCENARIO1_DRAFT_R1.md
git diff --check
```

Run citation audit if applicable exactly as in R1.

Verify source evidence bytes unchanged.

## 14. Git

Commit:

`fix(ch3): correct scenario1 section 3.2 R2`

Push:

`feature/x7b1-ch3-scenario1-draft`

Do not merge.

## 15. Handoff

Return:

1. starting SHA;
2. local/remote R2 SHA;
3. modified file list;
4. exact before/after wording for each prose blocker;
5. provenance SHA correction summary;
6. corrected claim-map audit summary;
7. final word count;
8. table/figure count;
9. source/derived image hash verification;
10. required-search results;
11. QA results;
12. clean git status.

Final state:

`X7B1_CH3_32_SCENARIO1_DRAFT_R2_READY_FOR_FINAL_EXTERNAL_REVIEW`

Then STOP.

Do not open X7C.
Do not write Section 3.3.
Do not write Chapter 4.
