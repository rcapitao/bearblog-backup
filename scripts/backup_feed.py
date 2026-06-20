#!/usr/bin/env python3
"""Fetch the bearblog.dev Atom feed and save each post under posts/."""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

FEED_URL = "https://rcapitao.com/feed/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "posts"

ATOM_NS = "http://www.w3.org/2005/Atom"
NAMESPACES = {"atom": ATOM_NS}


def sanitize_filename(value: str) -> str:
    value = value.strip()
    value = re.sub(r'[\\/:*?"<>|]', "-", value)
    return value or "untitled"


def fetch_feed(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "bearblog-backup/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def parse_items(xml_bytes: bytes):
    root = ET.fromstring(xml_bytes)
    for entry in root.findall("atom:entry", NAMESPACES):
        title = (entry.findtext("atom:title", namespaces=NAMESPACES) or "Untitled").strip()
        updated = (entry.findtext("atom:updated", namespaces=NAMESPACES) or "").strip()
        guid = (entry.findtext("atom:id", namespaces=NAMESPACES) or "").strip()
        link_el = entry.find("atom:link", NAMESPACES)
        link = link_el.get("href", "").strip() if link_el is not None else guid
        content_el = entry.find("atom:content", NAMESPACES)
        body = (content_el.text or "").strip() if content_el is not None else ""
        yield {
            "title": title,
            "link": link,
            "updated": updated,
            "guid": guid,
            "body": body,
        }


def format_date(updated: str) -> str:
    try:
        return datetime.fromisoformat(updated).strftime("%Y-%m-%d")
    except ValueError:
        return "unknown-date"


def write_post(item: dict) -> None:
    date = format_date(item["updated"])
    name = sanitize_filename(item["title"])
    file_path = OUTPUT_DIR / f"{date} - {name}.md"
    frontmatter = (
        "---\n"
        f"title: {item['title']}\n"
        f"link: {item['link']}\n"
        f"guid: {item['guid']}\n"
        f"date: {item['updated']}\n"
        "---\n\n"
    )
    file_path.write_text(frontmatter + item["body"] + "\n", encoding="utf-8")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        xml_bytes = fetch_feed(FEED_URL)
    except Exception as exc:
        print(f"Failed to fetch feed: {exc}", file=sys.stderr)
        return 1

    items = list(parse_items(xml_bytes))
    if not items:
        print("No items found in feed", file=sys.stderr)
        return 1

    for item in items:
        write_post(item)

    print(f"Saved {len(items)} post(s) to {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
