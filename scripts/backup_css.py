#!/usr/bin/env python3
"""Fetch rcapitao.com and save the CSS found inside <style> tags, keeping only the 3 most recent versions."""
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SITE_URL = "https://rcapitao.com/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "css"
KEEP_VERSIONS = 3

STYLE_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.DOTALL | re.IGNORECASE)
VERSION_FILE_RE = re.compile(r"^style-\d{4}-\d{2}-\d{2}\.css$")


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "bearblog-backup/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def prune_old_versions() -> None:
    versions = sorted(
        (f for f in OUTPUT_DIR.glob("style-*.css") if VERSION_FILE_RE.match(f.name)),
        key=lambda f: f.name,
    )
    for old_file in versions[:-KEEP_VERSIONS]:
        old_file.unlink()


def main() -> int:
    try:
        html = fetch(SITE_URL).decode("utf-8", errors="replace")
    except Exception as exc:
        print(f"Failed to fetch site: {exc}", file=sys.stderr)
        return 1

    blocks = STYLE_RE.findall(html)
    if not blocks:
        print("No <style> block found", file=sys.stderr)
        return 1

    css = "\n\n".join(block.strip() for block in blocks)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    date = datetime.utcnow().strftime("%Y-%m-%d")
    output_file = OUTPUT_DIR / f"style-{date}.css"
    output_file.write_text(css + "\n", encoding="utf-8")

    prune_old_versions()

    print(f"Saved CSS to {output_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
