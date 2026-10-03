from __future__ import annotations

import sys
from pathlib import Path

import pdfplumber


def main(source: Path, destination: Path) -> None:
    chunks: list[str] = [f"# {source.name}"]
    with pdfplumber.open(source) as pdf:
        for index, page in enumerate(pdf.pages, start=1):
            chunks.extend(["", f"## Page {index}", "", page.extract_text() or "[NO TEXT]"])
    destination.write_text("\n".join(chunks), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
