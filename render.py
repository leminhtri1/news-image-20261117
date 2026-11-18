"""Render scene.html to entry.png with a headless Chromium browser (run once, by hand, outside the grader).

The grader has no network and no browser, so the PNG is rendered here and committed; main.py only copies it.
Usage: python render.py [path-to-chrome-or-edge]
"""
import os
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "google-chrome", "chromium", "chromium-browser",
]
LIMIT_BYTES = 1048576


def find_browser() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    for c in CANDIDATES:
        if os.path.isfile(c) or shutil.which(c):
            return c
    sys.exit("no Chrome/Edge found: pass its path")


def png_size(data: bytes) -> tuple[int, int]:
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    return struct.unpack(">II", data[16:24])


def main() -> None:
    out = HERE / "entry.png"
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([
            find_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--user-data-dir={profile}",
            "--window-size=1024,1024", f"--screenshot={out}", (HERE / "scene.html").as_uri(),
        ], check=True, capture_output=True, timeout=120)
    data = out.read_bytes()
    w, h = png_size(data)
    print(f"entry.png: {w}x{h}, {len(data)} bytes")
    if w > 1024 or h > 1024 or len(data) > LIMIT_BYTES:
        sys.exit("entry.png breaks the 1024x1024 / 1 MiB limit")


if __name__ == "__main__":
    main()
