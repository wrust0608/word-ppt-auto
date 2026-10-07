import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'work/do-an/CH3_REDESIGN_TABLE_FIGURE_LEDGER_R1.md',
    'work/do-an/CH3_REDESIGN_EVIDENCE_VISUAL_BLUEPRINT_R1.md',
    'work/do-an/CH3_REDESIGN_CONTENT_MIGRATION_MAP_R1.md'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'=== Checking {fpath} ({len(lines)} lines) ===')

    # Check tables column count
    in_table = False
    col_count = 0
    mismatch_count = 0
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            # count cells, accounting for escaped pipes
            cells = [c for c in re.split(r'(?<!\\)\|', stripped)[1:-1]]
            if not in_table:
                in_table = True
                col_count = len(cells)
            else:
                if len(cells) != col_count:
                    print(f'  [MISMATCH] L{idx}: expected {col_count} cols, got {len(cells)} cols: {stripped[:50]}...')
                    mismatch_count += 1
        else:
            in_table = False

    if mismatch_count == 0:
        print('  All tables column counts OK!')

    # Check for |r=1. fragment
    fragment_found = False
    for idx, line in enumerate(lines, 1):
        if '|r=1.' in line or 'r=1.' in line:
            print(f'  [FRAGMENT] L{idx}: {line.strip()}')
            fragment_found = True
    if not fragment_found:
        print('  No fragment |r=1. found.')

    # Check for ETM-C02 without dash
    etm_typo_found = False
    for idx, line in enumerate(lines, 1):
        if 'ETM-C02' in line:
            print(f'  [ETM-C02 TYPO] L{idx}: {line.strip()}')
            etm_typo_found = True
    if not etm_typo_found:
        print('  No ETM-C02 typo found.')
