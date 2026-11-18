"""make.fun news-image-20261117 entry: write the picture of 17 November 2026's world news to /output/entry.png.

The image is rendered ahead of time from scene.html by render.py and committed beside this file;
the grader runs with no network, so this program only copies those exact bytes (identical on every run).
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
shutil.copyfile(Path(__file__).resolve().parent / "entry.png", out_dir / "entry.png")
