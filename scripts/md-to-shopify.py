#!/usr/bin/env python3
"""Convert an article markdown file into the payload Shopify's articleCreate wants.

Splits front matter from body, renders the body to HTML (tables + FAQ headings
intact), strips the H1 (Shopify renders the title separately), and rewrites
relative /collections and /products links to absolute store URLs.

Usage: python3 scripts/md-to-shopify.py content/articles/<file>.md
Emits JSON on stdout: {title, handle, body, summary, tags}
"""
import json, re, sys, pathlib
import markdown

STORE = "https://jurassicapparel.com"

def parse(path):
    raw = pathlib.Path(path).read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        sys.exit(f"{path}: no front matter")
    fm_text, body_md = m.group(1), m.group(2)

    fm = {}
    for line in fm_text.splitlines():
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km and km.group(2).strip():
            fm[km.group(1)] = km.group(2).strip().strip('"')

    # Shopify renders the title itself; drop the leading H1 from the body.
    body_md = body_md.lstrip()
    body_md = re.sub(r"^#\s+.*?\n", "", body_md, count=1).lstrip()

    html = markdown.markdown(body_md, extensions=["tables", "attr_list"])
    # Relative store links -> absolute.
    html = re.sub(r'href="(/(?:collections|products)/)', f'href="{STORE}\\1', html)

    tags = ["dinosaur costume", "halloween", "family costume", "dinosaur apparel"]
    if fm.get("target_keyword"):
        tags.insert(0, fm["target_keyword"])

    return {
        "title": fm.get("title", ""),
        "handle": fm.get("slug", ""),
        "body": html,
        "summary": fm.get("meta_description", ""),
        "tags": sorted(set(tags)),
        "_blog": fm.get("shopify_blog", "blog"),
    }

if __name__ == "__main__":
    print(json.dumps(parse(sys.argv[1]), indent=2))
