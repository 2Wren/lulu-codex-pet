#!/usr/bin/env python3
"""校验噜噜的精灵表，并把它整理成仓库发布素材。

按 Codex 官方 Pets 插件的 v2 规范校验 ~/.codex/pets/lulu（或 --source 指定的目录），
然后写出：

  lulu/pet.json           原样复制
  lulu/spritesheet.webp   原样复制（1536x2288，8x11，Codex 桌面端和 ChatGPT 通用）
  lulu/previews/*.png     每个状态一张 APNG 动图，供 README 展示
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("需要 Pillow：python3 -m pip install pillow")

CELL_W, CELL_H = 192, 208
COLS = 8
V1_ROWS = 9
V2_ROWS = 11
MAX_BYTES = 20 * 1024 * 1024

# (状态, 行号, 每帧时长 ms)，与 Pets 插件的 references/animation-rows.md 一致
STATES = [
    ("idle", 0, [280, 110, 110, 140, 140, 320]),
    ("running-right", 1, [120] * 7 + [220]),
    ("running-left", 2, [120] * 7 + [220]),
    ("waving", 3, [140] * 3 + [280]),
    ("jumping", 4, [140] * 4 + [280]),
    ("failed", 5, [140] * 7 + [240]),
    ("waiting", 6, [150] * 5 + [260]),
    ("running", 7, [120] * 5 + [220]),
    ("review", 8, [150] * 5 + [280]),
]
# 第 9、10 行：16 个顺时针注视方向，000° 为向上
LOOK_ROWS = (9, 10)
LOOK_FRAME_MS = 120
REQUIRED_FRAMES = sum(len(d) for _, _, d in STATES) + COLS * len(LOOK_ROWS)  # 73


def row_label(row):
    for name, state_row, _ in STATES:
        if state_row == row:
            return name
    return f"look-directions 第 {row} 行"


def used_columns(row):
    for _, state_row, durations in STATES:
        if state_row == row:
            return len(durations)
    return COLS


def cell(sheet, row, col):
    x, y = col * CELL_W, row * CELL_H
    return sheet.crop((x, y, x + CELL_W, y + CELL_H))


def transparent_mask(im):
    return im.getchannel("A").point(lambda v: 255 if v == 0 else 0)


def clean(im):
    """把完全透明像素的 RGB 清零，避免导出后残留色块。"""
    blank = Image.new("RGBA", im.size, (0, 0, 0, 0))
    return Image.composite(blank, im, transparent_mask(im))


def has_rgb_residue(im):
    r, g, b, _ = im.split()
    colored = ImageChops.lighter(ImageChops.lighter(r, g), b).point(lambda v: 255 if v else 0)
    return ImageChops.multiply(colored, transparent_mask(im)).getbbox() is not None


def validate(manifest, sheet, sheet_bytes):
    errors, warnings = [], []

    for key in ("id", "displayName", "description", "spritesheetPath"):
        value = manifest.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"pet.json 缺少 {key}")
    version = manifest.get("spriteVersionNumber")
    if type(version) is not int or version != 2:
        errors.append(f"pet.json 的 spriteVersionNumber 应为数字 2，当前为 {version!r}")

    if not 0 < sheet_bytes <= MAX_BYTES:
        errors.append(f"精灵表大小为 {sheet_bytes} 字节，应在 20 MiB 以内")

    expected = (COLS * CELL_W, V2_ROWS * CELL_H)
    if sheet.size != expected:
        errors.append(f"精灵表尺寸为 {sheet.size[0]}x{sheet.size[1]}，v2 应为 {expected[0]}x{expected[1]}")
        if sheet.size == (COLS * CELL_W, V1_ROWS * CELL_H):
            errors.append("这是 v1（8x9）精灵表，请用 Codex 的 Pets 插件升级到 v2（补上两行注视方向）")
        return errors, warnings

    for row in range(V2_ROWS):
        label = row_label(row)
        for col in range(COLS):
            bbox = cell(sheet, row, col).getchannel("A").getbbox()
            if col >= used_columns(row):
                if bbox is not None:
                    hint = "（旧版 hatch-pet 的中立帧，Pets 插件规范要求留空）" if (row, col) == (0, 6) else ""
                    errors.append(f"{label} 第 {col} 格应完全透明，但有像素{hint}")
            elif bbox is None:
                errors.append(f"{label} 第 {col} 帧是空的")
            elif bbox[0] == 0 or bbox[1] == 0 or bbox[2] == CELL_W or bbox[3] == CELL_H:
                warnings.append(f"{label} 第 {col} 帧贴到格子边缘，可能被裁切")

    if has_rgb_residue(sheet):
        warnings.append("精灵表的透明像素残留 RGB 值（预览图已自动清理）")

    return errors, warnings


def write_apng(frames, durations, path):
    frames[0].save(
        path,
        format="PNG",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=1,
        blend=0,
    )


def main():
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    repo = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description="校验噜噜桌宠并生成仓库发布素材")
    parser.add_argument(
        "--source",
        type=Path,
        default=codex_home / "pets" / "lulu",
        help="含 pet.json 和精灵表的目录（默认 $CODEX_HOME/pets/lulu）",
    )
    parser.add_argument("--out", type=Path, default=repo / "lulu", help="发布目录（默认仓库内的 lulu/）")
    args = parser.parse_args()

    manifest_path = args.source / "pet.json"
    if not manifest_path.is_file():
        sys.exit(f"找不到 {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sheet_path = args.source / manifest.get("spritesheetPath", "spritesheet.webp")

    with Image.open(sheet_path) as raw:
        if raw.format not in ("PNG", "WEBP"):
            sys.exit(f"{sheet_path} 应为 PNG 或 WebP，当前为 {raw.format}")
        if "A" not in raw.getbands():
            sys.exit(f"{sheet_path} 没有透明通道")
        sheet = raw.convert("RGBA")

    errors, warnings = validate(manifest, sheet, sheet_path.stat().st_size)
    for message in warnings:
        print(f"警告：{message}")
    if errors:
        for message in errors:
            print(f"错误：{message}")
        sys.exit(1)

    out = args.out
    previews = out / "previews"
    previews.mkdir(parents=True, exist_ok=True)

    for src in (manifest_path, sheet_path):
        dst = out / src.name
        if not (dst.exists() and dst.samefile(src)):
            shutil.copy2(src, dst)

    for name, row, durations in STATES:
        frames = [clean(cell(sheet, row, col)) for col in range(len(durations))]
        write_apng(frames, durations, previews / f"{name}.png")

    look = [clean(cell(sheet, row, col)) for row in LOOK_ROWS for col in range(COLS)]
    write_apng(look, [LOOK_FRAME_MS] * len(look), previews / "look-directions.png")

    print(f"已校验 {manifest['displayName']}（{manifest['id']}），v2 · {REQUIRED_FRAMES} 帧（9 个状态 + 16 个注视方向）")
    print(f"发布素材已写入 {out}")


if __name__ == "__main__":
    main()
