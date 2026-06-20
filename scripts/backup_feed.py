#!/usr/bin/env python3
"""Fetch the bearblog.dev RSS feed and save each post under bearblog-backup/."""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://rcapitao.com/feed/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "bearblog-backup"

NAMESPACES = {"content": "http://purl.org/rss/1.0/modules/content/"}


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
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "Untitled").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        guid = (item.findtext("guid") or link).strip()
        description = (item.findtext("description") or "").strip()
        content_encoded = (item.findtext("content:encoded", namespaces=NAMESPACES) or "").strip()
        body = content_encoded or description
        yield {
            "title": title,
            "link": link,
            "pub_date": pub_date,
            "guid": guid,
            "body": body,
        }


def format_date(pub_date: str) -> str:
    try:
        return parsedate_to_datetime(pub_date).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return "unknown-date"


def write_post(item: dict) -> None:
    date = format_date(item["pub_date"])
    name = sanitize_filename(item["title"])
    post_dir = OUTPUT_DIR / f"{date} - {name}"
    post_dir.mkdir(parents=True, exist_ok=True)
    file_path = post_dir / "post.md"
    frontmatter = (
        "---\n"
        f"title: {item['title']}\n"
        f"link: {item['link']}\n"
        f"guid: {item['guid']}\n"
        f"date: {item['pub_date']}\n"
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
