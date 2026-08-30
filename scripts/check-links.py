#!/usr/bin/env python3
"""Verify every collection an article links to actually has inventory.

Linking to an empty collection is a bug (CLAUDE.md standing rules). Run before
every commit:  python3 scripts/check-links.py content/articles/<file>.md
With no argument, checks every article in content/articles/.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
catalog = json.load(open(ROOT / "data" / "catalog.json"))

EMPTY = {c["handle"]: c for c in catalog["empty_collections_do_not_link"]}
KNOWN = {c["handle"]: c["products"]
         for group in catalog["collections"].values() for c in group}

def check(path):
    text = path.read_text()
    handles = sorted(set(re.findall(r"/collections/([a-z0-9-]+)", text)))
    problems = []
    for h in handles:
        if h in EMPTY:
            problems.append(f"  {h:<30} EMPTY COLLECTION — remove this link")
        elif h not in KNOWN:
            problems.append(f"  {h:<30} not in catalog.json — verify, then add it to the map")
        else:
            print(f"  {h:<30} {KNOWN[h]:>4} products  ok")
    for p in problems:
        print(p)
    return problems

def main():
    targets = ([pathlib.Path(a) for a in sys.argv[1:]]
               or sorted((ROOT / "content" / "articles").glob("*.md")))
    failed = 0
    for t in targets:
        print(f"\n{t.name}")
        failed += len(check(t))
    print()
    if failed:
        print(f"FAIL — {failed} bad link(s). Fix before committing.")
        return 1
    print("PASS — every linked collection has inventory.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
