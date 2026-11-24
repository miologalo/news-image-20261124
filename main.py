#!/usr/bin/env python3
"""Entry point for news-image-20261124.

Copies the pre-rendered front page (entry.png, in this repository) to the
output directory as entry.png, the single image the competition grades.
Standard library only; no network. The output directory is /output, or
MAKEFUN_OUTPUT_DIR when set (local runs).

Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)

# Verify the output is a whole PNG within the competition cap (1 MiB).
# Fail loudly instead of handing the grader a corrupt or oversized file.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
data = TARGET.read_bytes()
if not data.startswith(PNG_MAGIC):
    raise SystemExit(f"error: {TARGET} is not a PNG file")
if len(data) > 1_048_576:
    raise SystemExit(f"error: {TARGET} is {len(data)} bytes, over the 1 MiB cap")
print(f"wrote {TARGET} ({len(data)} bytes)")
