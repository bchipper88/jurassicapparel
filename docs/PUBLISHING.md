# Publishing — the handoff

**The agent publishes new articles directly to the live blog** under the standing approval
recorded at the bottom of this file. Everything is still written and version-controlled
here first — the repo remains the source of truth and the audit trail.

**Rewrites of existing live pages remain gated** and are delivered as briefs.

## Article lifecycle

```
draft  →  approved  →  published
```

Tracked in each article's front matter `status:` field, and in `KEYWORDS.md`.

### 1. draft
Written and committed to `content/articles/`. Named `YYYY-MM-DD-<slug>.md`.
Link check must pass: `python3 scripts/check-links.py`.

### 2. published
Converted with `scripts/md-to-shopify.py` and pushed live via the `articleCreate` mutation
on the Shopify Admin API. Record `live_url:`, `shopify_article_id:` and `published_at:` in
the front matter, flip `KEYWORDS.md` to ✅ Published, and note it in the daily update.

```bash
python3 scripts/md-to-shopify.py content/articles/<file>.md   # -> title/handle/body/summary/tags
# then articleCreate with blogId gid://shopify/Blog/50916753501 (the "blog" blog)
```

The converter strips the H1 (Shopify renders the title itself) and rewrites relative
`/collections` and `/products` links to absolute store URLs.

## Where each article goes

| Blog | Handle | Use for |
|---|---|---|
| Blog | `blog` | Commercial guides, gift guides, seasonal buying content |
| Dinosaur Facts | `dinosaur-facts` | Species and informational content (323 articles) |
| Dinosaur Birthday Party | `dinosaur-birthday-party` | Party content (currently 1 article) |
| Dinosaur Toys | `dinosaur-toys` | Toy content (currently 1 article) |

Set `shopify_blog:` in the front matter so the destination is unambiguous at publish time.

## Rescue briefs

Rewrites of existing live pages are higher-stakes than new articles — they change a page
that is already earning traffic. A rescue brief must contain:

1. **The URL** and its current position + volume, with the pull date
2. **Why it's underperforming** — usually thin content; say what's actually missing
3. **The full replacement copy**, ready to paste. Not notes, not an outline.
4. **What must not change** — the URL slug (never change it; the rankings live there),
   and any section currently earning a featured snippet
5. **The new title and meta description**
6. **A rollback note** — what the page said before, so it can be put back

Rescue briefs go in `content/rescues/` and are listed in the daily update as needing sign-off.

## When publishing is approved as a standing arrangement

If the owner grants standing approval to publish (rather than per-article), record it here
with the date and the exact scope granted, and update `CEO-CHARTER.md` to match. Until
that entry exists, every publish is individually gated.

**Standing approval granted 2026-08-30 by the owner (John Honochick).**

**Scope:** the agent may write and publish **new blog articles** directly to the live
Shopify blog, without per-article approval. It publishes, then logs the live URL and
Shopify article ID in the article front matter and in `KEYWORDS.md`.

**Not in scope:** rewriting or replacing existing live pages (the rescue queue), product
copy, collection descriptions, and theme changes. Those remain gated and are delivered as
briefs. A separate approval is outstanding for rescue rewrites.

**Rollback:** every published article is recorded with its `shopify_article_id`, so any
post can be unpublished or reverted from the Shopify admin, or by the agent on request.
