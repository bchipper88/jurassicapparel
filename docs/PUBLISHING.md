# Publishing — the handoff

**The agent does not publish to the live storefront.** (`CEO-CHARTER.md`.) Articles are
written, staged and version-controlled here; the owner publishes.

## Article lifecycle

```
draft  →  approved  →  published
```

Tracked in each article's front matter `status:` field, and in `KEYWORDS.md`.

### 1. draft
Written and committed to `content/articles/`. Named `YYYY-MM-DD-<slug>.md`.
Listed in the daily update with its target keyword and the numbers behind it.

### 2. approved
The owner has read it and said go. Update `status: approved` and note the date in the
day's update.

### 3. published
Live on the store. Record the live URL in the front matter as `live_url:`, flip
`KEYWORDS.md` to ✅ Published with the date and slug, and note it in the update.

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

*No standing approval granted as of 2026-08-30.*
