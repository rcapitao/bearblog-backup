#!/usr/bin/env python3
import urllib.request
import xml.etree.ElementTree as ET

FEED_URL = "https://rcapitao.com/feed/"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "bearblog-backup/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


xml_bytes = fetch(FEED_URL)
root = ET.fromstring(xml_bytes)
ns = {"atom": "http://www.w3.org/2005/Atom"}
entry = root.find("atom:entry", ns)
print("=== FIRST ENTRY RAW XML ===")
print(ET.tostring(entry, encoding="unicode"))

link_el = entry.find("atom:link", ns)
post_url = link_el.get("href")
print("=== POST URL ===", post_url)

html = fetch(post_url).decode("utf-8", errors="replace")
print("=== POST HTML HEAD (first 6000 chars) ===")
print(html[:6000])
