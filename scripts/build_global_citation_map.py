"""Build the authorized report-wide IEEE map without editing canonical chapters."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'work' / 'do-an'
FILES = ['INTRODUCTION.md', 'CHAPTER_1.md', 'CHAPTER_2.md']


def urls(text):
    return [u.rstrip('.;,/').lower().replace('learn.microsoft.com/en-us/', 'learn.microsoft.com/')
            for u in re.findall(r'https?://[^\s|]+', text)]


def build():
    ledger = {}
    for line in (PROJECT / 'SOURCE_LEDGER.md').read_text(encoding='utf-8').splitlines():
        cells = [c.strip() for c in line.split('|')]
        if len(cells) > 8 and re.fullmatch(r'S\d{3}', cells[1]):
            ledger[cells[1]] = {'status': cells[2], 'urls': urls(cells[7])}
    aliases = {u: sid for sid, entry in ledger.items() for u in entry['urls']}
    aliases.update({
        'https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-115.pdf': 'S024',
        'https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-41r1.pdf': 'S025',
    })
    global_numbers, sources, mappings, hashes, bodies = {}, {}, {}, {}, []
    for name in FILES:
        path = PROJECT / name
        raw = path.read_bytes()
        hashes[name] = hashlib.sha256(raw).hexdigest()
        text = raw.decode('utf-8-sig')
        start = re.search(r'^\[\d+\]\s', text, re.M)
        if not start:
            raise ValueError(f'No bibliography: {name}')
        body = text[:start.start()]
        body = re.sub(r'^#{1,6}\s+TÀI LIỆU THAM KHẢO.*$', '', body, flags=re.M)
        references = dict((int(n), ref) for n, ref in re.findall(r'^\[(\d+)\]\s+(.+)$', text[start.start():], re.M))
        identities = {}
        for number, ref in references.items():
            matches = {aliases[u] for u in urls(ref) if u in aliases}
            if not matches and '/openspecs/windows_protocols/ms-smb2/' in ref:
                matches = {'S022'}
            if not matches and 'Nmap Network Scanning' in ref:
                matches = {'S017'}  # Chapter 2 cites the same book without its URL.
            if len(matches) != 1:
                raise ValueError(f'Unresolved identity: {name} [{number}]: {matches}')
            sid = matches.pop()
            if ledger[sid]['status'] != 'VERIFIED':
                raise ValueError(f'Unverified source: {sid}')
            identities[number] = sid
        plain = re.sub(r'```.*?```', '', body, flags=re.S)
        for match in re.finditer(r'\[(\d+)\]', plain):
            number = int(match[1])
            sid = identities[number]
            if sid not in global_numbers:
                global_numbers[sid] = len(global_numbers) + 1
                sources[sid] = references[number]
        mappings[name] = {str(n): global_numbers[sid] for n, sid in identities.items()}
        # One callback prevents cascading replacements such as 1->2->3.
        transformed = re.sub(r'\[(\d+)\]', lambda m: f'[{mappings[name][m[1]]}]', body)
        bodies.append(transformed.strip())
        assert path.read_bytes() == raw, 'Canonical input changed during map build'
    data = {'order': FILES, 'input_sha256': hashes, 'mappings': mappings,
            'sources': [{'number': number, 'source_id': sid, 'reference': sources[sid]}
                        for sid, number in global_numbers.items()]}
    (PROJECT / 'GLOBAL_CITATION_MAP.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# Ánh xạ IEEE toàn báo cáo', '',
             'Tác giả cho phép lập bảng chung ngày 2026-10-04. Thứ tự: Mở đầu → Chương 1 → Chương 2. '
             'Hai chương canonical được giữ nguyên; chỉ chuyển số trong bản ghép. Chương 3/4 chưa có bản nguồn nên chưa được đánh số trước.', '',
             'Danh mục trong Word Mở đầu là trích xuất từ bảng này. Khi ghép, bỏ danh mục riêng từng phần và chỉ đặt danh mục chung ở cuối. '
             'Nếu nội dung/thứ tự trích dẫn thay đổi, dựng lại bảng và audit bản ghép; SHA256 dưới đây xác định phiên bản áp dụng.', '',
             '## Phiên bản đầu vào', '', '| File | SHA256 |', '|---|---|']
    lines += [f'| {name} | {sha} |' for name, sha in hashes.items()]
    for name, mapping in mappings.items():
        lines += ['', f'## {name}', '', '| Số hiện có | Số chung khi ghép |', '|---|---|']
        lines += [f'| [{old}] | [{new}] |' for old, new in mapping.items()]
    lines += ['', '## Nguồn chung', '', '| IEEE | Ledger | Tài liệu |', '|---|---|---|']
    lines += [f'| [{number}] | {sid} | {sources[sid]} |' for sid, number in global_numbers.items()]
    lines += ['', '## Đối soát định danh', '',
              '- Trang CSRC và PDF NIST SP 800-115 là cùng S024; trang CSRC và PDF SP 800-41 Rev.1 là cùng S025.',
              '- Nmap Network Scanning ở Chương 2 không ghi URL nhưng tác giả, tiêu đề, nhà xuất bản và năm khớp S017/Chương 1.',
              '- Trang ví dụ MS-SMB2 thuộc đặc tả S022; hai trang MS-CIFS thuộc S028. Không tạo nguồn mới chỉ vì có URL mục con.',
              '- URL Microsoft Learn có hoặc không có tiền tố en-us được đối chiếu cùng trang tiếng Anh, gồm S023.',
              '- Tất cả định danh trong bảng ở trạng thái VERIFIED trong ledger. Bảng định danh không chứng nhận lại mọi luận điểm của hai chương.', '']
    (PROJECT / 'GLOBAL_CITATION_MAP.md').write_text('\n'.join(lines), encoding='utf-8')
    temp = ROOT / '.tmp' / 'introduction-final'
    temp.mkdir(parents=True, exist_ok=True)
    bibliography = '\n\n'.join(f'[{number}] {sources[sid]}' for sid, number in global_numbers.items())
    (temp / 'global-report-audit.md').write_text('\n\n'.join(bodies) + '\n\n## TÀI LIỆU THAM KHẢO\n\n' + bibliography + '\n', encoding='utf-8')
    print(json.dumps({'sources': len(sources), 'mappings': mappings, 'canonical_inputs_unchanged': True}, ensure_ascii=False))


if __name__ == '__main__':
    build()
