"""
check_source_inventory.py — Read-only extractor and inventory verifier.
Reads CHAPTER_3_DRAFT_R2.md, extracts all tables and data rows (line numbers, labels),
and compares them against CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md inventory.
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def extract_tables_from_draft(draft_path: Path):
    with open(draft_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    tables = []
    current_table = None
    in_table = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Detect table caption
        cap_match = re.match(r"^\*\*(Bảng\s+3\.\d+)\.\s+([^*]+)\*\*", stripped)
        if cap_match:
            current_table = {
                "id": cap_match.group(1),
                "caption": cap_match.group(2).strip(),
                "caption_line": idx,
                "header_line": None,
                "data_rows": []
            }
            tables.append(current_table)
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            if current_table and current_table["header_line"] is None:
                current_table["header_line"] = idx
                continue
            # Separator line |---|---|...
            if re.match(r"^\|(\s*:?-+:?\s*\|)+$", stripped):
                continue
            # Data row
            if current_table:
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                label = cells[0] if cells else ""
                current_table["data_rows"].append({
                    "line": idx,
                    "label": label,
                    "raw": stripped,
                    "cells": cells
                })

    return tables

def extract_inventory_from_migration_map(map_path: Path):
    with open(map_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match rows in Section 3.1: | STT | Source Key | Vị trí gốc | Nhãn hàng / Nội dung dữ kiện gốc | ...
    pattern = r"^\|\s*(\d+)\s*\|\s*`?(SRC-TBL-\d+)`?\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
    inventory = []
    for line in content.splitlines():
        m = re.match(pattern, line.strip())
        if m:
            inventory.append({
                "stt": int(m.group(1)),
                "key": m.group(2),
                "loc": m.group(3).strip(),
                "label": m.group(4).strip(),
                "content": m.group(5).strip(),
                "dest": m.group(6).strip(),
                "action": m.group(7).strip(),
                "note": m.group(8).strip()
            })
    return inventory

def verify():
    repo_root = Path(__file__).resolve().parent.parent
    draft_path = repo_root / "work" / "do-an" / "CHAPTER_3_DRAFT_R2.md"
    map_path = repo_root / "work" / "do-an" / "CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md"

    print(f"Reading draft: {draft_path}")
    tables = extract_tables_from_draft(draft_path)
    print(f"Extracted {len(tables)} tables from draft:")
    total_draft_rows = 0
    flat_draft_rows = []
    for t in tables:
        count = len(t["data_rows"])
        total_draft_rows += count
        print(f"  - {t['id']} (caption line {t['caption_line']}): {count} data rows")
        for r in t["data_rows"]:
            flat_draft_rows.append((t["id"], r["line"], r["label"]))

    print(f"Total draft table rows extracted: {total_draft_rows}")
    if total_draft_rows != 53:
        print(f"ERROR: Expected 53 data rows, got {total_draft_rows}", file=sys.stderr)
        sys.exit(1)

    print(f"\nReading migration map: {map_path}")
    inventory = extract_inventory_from_migration_map(map_path)
    print(f"Found {len(inventory)} items in SRC-TBL inventory.")
    if len(inventory) != 53:
        print(f"ERROR: Expected 53 inventory items, got {len(inventory)}", file=sys.stderr)
        sys.exit(1)

    print("\nComparing draft extracted rows with inventory items:")
    mismatches = 0
    for idx, (inv, (t_id, line_num, draft_label)) in enumerate(zip(inventory, flat_draft_rows), start=1):
        key = inv["key"]
        inv_loc = inv["loc"]
        # Check if line_num is in inv_loc
        expected_line_str = f"L{line_num}"
        has_line = expected_line_str in inv_loc or str(line_num) in inv_loc
        if not has_line:
            print(f"  [MISMATCH LINE] {key}: Draft line {line_num} vs Inv loc '{inv_loc}'")
            mismatches += 1
        else:
            print(f"  [OK] {key}: Line {line_num} ({t_id}) | Draft label: '{draft_label[:40]}...'")

    if mismatches > 0:
        print(f"\nFound {mismatches} mismatches!", file=sys.stderr)
        sys.exit(1)

    print("\nVerification PASSED: 53 draft table rows match 53 inventory items perfectly!")

    # Check Narrative blocks in migration map
    print("\nChecking Narrative blocks (SRC-NAR-01..26):")
    nar_pattern = r"^\|\s*(\d+)\s*\|\s*`?(SRC-NAR-\d+)`?\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
    with open(map_path, "r", encoding="utf-8") as f:
        map_content = f.read()

    nar_items = []
    for line in map_content.splitlines():
        m = re.match(nar_pattern, line.strip())
        if m:
            nar_items.append({
                "stt": int(m.group(1)),
                "key": m.group(2),
                "loc": m.group(3).strip(),
                "content": m.group(4).strip(),
                "dest": m.group(5).strip(),
                "action": m.group(6).strip(),
                "note": m.group(7).strip()
            })

    print(f"Found {len(nar_items)} narrative fact blocks.")
    if len(nar_items) != 26:
        print(f"ERROR: Expected 26 narrative blocks, got {len(nar_items)}", file=sys.stderr)
        sys.exit(1)

    for nar in nar_items:
        print(f"  [OK] {nar['key']}: {nar['loc']} -> {nar['action']}")

    # Check total denominator: 53 + 26 = 79
    total_denom = len(inventory) + len(nar_items)
    print(f"\nTotal inventory denominator: {len(inventory)} table rows + {len(nar_items)} narrative blocks = {total_denom} items.")

    # Check Claim matrix (Claim-01..41)
    print("\nChecking Claim Matrix (Claim-01..41):")
    claim_pattern = r"^\|\s*\*\*(Claim-\d+)\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|"
    claims = []
    for line in map_content.splitlines():
        m = re.match(claim_pattern, line.strip())
        if m:
            claims.append({
                "id": m.group(1),
                "loc": m.group(2).strip(),
                "evidence": m.group(3).strip(),
                "ev_type": m.group(4).strip(),
                "fact": m.group(5).strip(),
                "section": m.group(6).strip(),
                "action": m.group(7).strip(),
                "boundary": m.group(8).strip()
            })
    print(f"Found {len(claims)} claims in Claim Matrix.")
    if len(claims) != 41:
        print(f"ERROR: Expected 41 claims, got {len(claims)}", file=sys.stderr)
        sys.exit(1)

    print("\nAuditing claim evidence file paths...")
    missing_files = 0
    for c in claims:
        # extract file paths from evidence column
        # e.g., chapter3/evidence/...
        paths = re.findall(r"chapter3/evidence/[a-zA-Z0-9_\-\./]+", c["evidence"])
        for p in paths:
            # check if exists under work/do-an/
            full_p = repo_root / "work" / "do-an" / p
            if not full_p.exists():
                print(f"  [MISSING FILE] {c['id']}: {p} not found at {full_p}")
                missing_files += 1
            else:
                pass
    if missing_files > 0:
        print(f"ERROR: {missing_files} evidence files missing!", file=sys.stderr)
        sys.exit(1)
    print("All referenced evidence file paths in Claim Matrix exist!")

if __name__ == "__main__":
    verify()
