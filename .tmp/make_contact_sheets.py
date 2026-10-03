from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw


def main(folder: Path) -> None:
    pages = sorted(folder.glob("*.png"))
    target_width = 620
    gap = 24
    label_height = 34
    for sheet_index in range(0, len(pages), 4):
        group = pages[sheet_index : sheet_index + 4]
        rendered = []
        for page in group:
            image = Image.open(page).convert("RGB")
            height = round(image.height * target_width / image.width)
            rendered.append((page.name, image.resize((target_width, height))))
        width = target_width * 2 + gap * 3
        cell_height = max(image.height for _, image in rendered) + label_height
        height = cell_height * 2 + gap * 3
        canvas = Image.new("RGB", (width, height), "#d9d9d9")
        draw = ImageDraw.Draw(canvas)
        for index, (name, image) in enumerate(rendered):
            col, row = index % 2, index // 2
            x = gap + col * (target_width + gap)
            y = gap + row * (cell_height + gap)
            draw.text((x, y), name, fill="black")
            canvas.paste(image, (x, y + label_height))
        output = folder / f"contact-{sheet_index // 4 + 1}.png"
        canvas.save(output)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
