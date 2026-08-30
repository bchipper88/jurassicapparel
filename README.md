# Jurassic Apparel — Agent Operations Repo

This repository is **not the storefront**. The storefront is Shopify (`jurassicapparel.com`).

This repo is the **operational database and memory** for the AI agent that runs growth for
Jurassic Apparel. Every decision, keyword, article, metric and daily update is committed
here so that state survives between sessions and every change has an audit trail.

Modeled on the operating routines proven at `bchipper88/lv-directory` (Lehigh Valley Best),
adapted from a local directory to a DTC ecommerce catalog.

## What lives here

| Path | Purpose |
|---|---|
| `CEO-CHARTER.md` | The agent's mandate, decision rights, and what requires owner sign-off |
| `STRATEGY.md` | The current diagnosis, the plays, and why. Reviewed monthly. |
| `KEYWORDS.md` | **The content queue.** Status-tracked keyword database (LV format). |
| `BACKLOG.md` | Non-content work: catalog fixes, technical SEO, merchandising |
| `content/articles/` | Every article written, as markdown, dated + slugged |
| `updates/` | Daily agent update log — one file per working day |
| `data/catalog.json` | Snapshot of Shopify collections & blogs (the internal-link map) |
| `data/keywords.json` | Machine-readable keyword database |
| `data/metrics.json` | Traffic/ranking snapshots over time |
| `docs/` | Playbooks: how to research, how to write, how to publish |

## The daily loop

```
1. RESEARCH   Ubersuggest → verify volume/difficulty for the next queued keyword
2. DECIDE     Pick the target. Log the reasoning.
3. WRITE      Draft the article per docs/ARTICLE-PLAYBOOK.md
4. COMMIT     Article + KEYWORDS.md status + updates/YYYY-MM-DD.md → GitHub
5. REPORT     Daily update states what shipped, what it targets, what's next
```

Full detail in `CLAUDE.md`.

## Reading the state of the business in 30 seconds

```bash
cat updates/$(ls updates | tail -1)     # what happened most recently
grep -c '✅ Published' KEYWORDS.md      # articles shipped
head -40 STRATEGY.md                    # what we're betting on
```
