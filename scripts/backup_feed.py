#!/usr/bin/env python3
"""Fetch the bearblog.dev Atom feed and save each post under posts/."""
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

FEED_URL = "https://rcapitao.com/feed/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "posts"

ATOM_NS = "http://www.w3.org/2005/Atom"
NAMESPACES = {"atom": ATOM_NS}

IMG_SRC_RE = re.compile(r'<img[^>]+src="([^"]+)"')
OG_IMAGE_RE = re.compile(r'<meta\s+property="og:image"\s+content="([^"]*)"')


def sanitize_filename(value: str) -> str:
    value = value.strip()
    value = re.sub(r'[\\/:*?"<>|]', "-", value)
    return value or "untitled"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "bearblog-backup/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def parse_items(xml_bytes: bytes):
    root = ET.fromstring(xml_bytes)
    for entry in root.findall("atom:entry", NAMESPACES):
        title = (entry.findtext("atom:title", namespaces=NAMESPACES) or "Untitled").strip()
        updated = (entry.findtext("atom:updated", namespaces=NAMESPACES) or "").strip()
        guid = (entry.findtext("atom:id", namespaces=NAMESPACES) or "").strip()
        summary = (entry.findtext("atom:summary", namespaces=NAMESPACES) or "").strip()
        link_el = entry.find("atom:link", NAMESPACES)
        link = link_el.get("href", "").strip() if link_el is not None else guid
        content_el = entry.find("atom:content", NAMESPACES)
        body = (content_el.text or "").strip() if content_el is not None else ""
        tags = [cat.get("term") for cat in entry.findall("atom:category", NAMESPACES) if cat.get("term")]
        yield {
            "title": title,
            "link": link,
            "updated": updated,
            "guid": guid,
            "body": body,
            "tags": tags,
            "meta_description": summary,
        }


def fetch_meta_image(link: str) -> str:
    try:
        html = fetch(link).decode("utf-8", errors="replace")
    except Exception:
        return ""
    match = OG_IMAGE_RE.search(html)
    if not match:
        return ""
    return urllib.parse.urljoin(link, match.group(1))


def format_date(updated: str) -> str:
    try:
        return datetime.fromisoformat(updated).strftime("%Y-%m-%d")
    except ValueError:
        return "unknown-date"


def download_image(url: str, post_dir: Path) -> None:
    filename = sanitize_filename(Path(urllib.parse.urlparse(url).path).name)
    if not filename:
        return
    file_path = post_dir / filename
    if file_path.exists():
        return
    try:
        file_path.write_bytes(fetch(url))
    except Exception as exc:
        print(f"Failed to download image {url}: {exc}", file=sys.stderr)


def write_post(item: dict, post_dir: Path) -> None:
    tags = ", ".join(item["tags"])
    frontmatter = (
        "---\n"
        f"title: {item['title']}\n"
        f"link: {item['link']}\n"
        f"date: {item['updated']}\n"
        f"tags: {tags}\n"
        f"meta_description: {item['meta_description']}\n"
        f"meta_image: {item['meta_image']}\n"
        "---\n\n"
    )
    (post_dir / "post.md").write_text(frontmatter + item["body"] + "\n", encoding="utf-8")


def process_item(item: dict) -> None:
    date = format_date(item["updated"])
    name = sanitize_filename(item["title"])
    post_dir = OUTPUT_DIR / f"{date} - {name}"
    post_dir.mkdir(parents=True, exist_ok=True)

    item["meta_image"] = fetch_meta_image(item["link"])

    for image_url in IMG_SRC_RE.findall(item["body"]):
        download_image(image_url, post_dir)
    if item["meta_image"]:
        download_image(item["meta_image"], post_dir)

    write_post(item, post_dir)


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        xml_bytes = fetch(FEED_URL)
    except Exception as exc:
        print(f"Failed to fetch feed: {exc}", file=sys.stderr)
        return 1

    items = list(parse_items(xml_bytes))
    if not items:
        print("No items found in feed", file=sys.stderr)
        return 1

    for item in items:
        process_item(item)

    print(f"Saved {len(items)} post(s) to {OUTPUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
