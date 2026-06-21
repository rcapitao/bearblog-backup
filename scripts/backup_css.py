#!/usr/bin/env python3
"""Fetch rcapitao.com and save the CSS found inside <style> tags."""
import re
import sys
import urllib.request
from pathlib import Path

SITE_URL = "https://rcapitao.com/"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "css" / "style.css"

STYLE_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.DOTALL | re.IGNORECASE)


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "bearblog-backup/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


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
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(css + "\n", encoding="utf-8")

    print(f"Saved CSS to {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
