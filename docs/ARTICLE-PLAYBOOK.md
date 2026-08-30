# Article Playbook

How a Jurassic Apparel article gets written. Follow this every time.

## Front matter

Every file in `content/articles/` opens with this block:

```yaml
---
title: "<the H1, written for humans>"
slug: <url-slug>
date: 2026-08-30
status: draft            # draft → approved → published
target_keyword: "<primary>"
target_volume: 1000      # as returned by Ubersuggest
target_sd: 28
target_intent: Commercial
seasonality: "Oct peak 5,400/mo"   # or "evergreen"
secondary_keywords:
  - "<term>"
shopify_blog: blog       # blog | dinosaur-facts | dinosaur-birthday-party
collections_linked:
  - handle: mamasaurus
    products: 17
word_count: 0
---
```

`collections_linked` records the product count **at time of writing**. If a collection
you want to link has 0 products, you cannot link it — that's a `BACKLOG.md` item.

## Structure

1. **Open with the reader's actual situation**, not a definition. They are shopping for a
   family Halloween costume in late August; meet them there. Two or three sentences.
2. **Answer the query early.** If the title promises ideas, the first idea appears above
   the fold. Never make someone scroll past preamble.
3. **H2 sections that map to how people actually decide** — by who it's for, by budget,
   by how much effort they want to spend. Not by product category.
4. **A comparison table** where there's a real decision to make. Tables earn featured
   snippets and they genuinely help.
5. **FAQ section** built from real "People Also Ask" style questions — sizing, shipping
   timing, care, whether it works for a group.
6. **Close with a clear next step**, singular. One link, not a wall of them.

## House voice

Warm, specific, a little playful — this is a dinosaur store, not a law firm. But never
cutesy at the expense of being useful.

**Do:**
- Name the actual product and what makes it work: *"the hooded blanket doubles as the
  costume if the night turns cold"*
- Give real constraints: sizing runs, shipping windows, what won't survive a wash
- Write like someone who has actually dressed a four-year-old for Halloween

**Don't:**
- "In today's fast-paced world" / "Look no further" / "Whether you're a X or a Y"
- Keyword stuffing. The target belongs in the H1, the first 100 words, and one H2 —
  because it fits there naturally.
- Fake urgency or invented scarcity
- Superlatives we can't support. "Popular" needs a reason; "best-selling" needs data.

## Internal linking

The rule that makes this work commercially:

- **3–6 links to collection or product pages** with real inventory, placed where they
  answer the sentence they're in — never a link dump at the bottom.
- **1–2 links to other articles** on the site, to build topical clusters.
- Check `data/catalog.json` for the handle and the product count before linking.
- Link text describes the destination: *"the Mamasaurus collection"*, not *"click here"*.

## Length

Match the intent, don't hit a number:

| Intent | Target |
|---|---|
| Transactional (buying one thing) | 900–1,400 words |
| Commercial comparison / gift guide | 1,400–2,200 words |
| Informational pillar / rescue rewrite | 2,500–4,000 words |

Depth wins where the query is broad; brevity wins where the reader wants to buy. A
rescue rewrite has to clear whatever is currently outranking us, which in practice means
the long end of that range.

## Before you commit

- [ ] Every linked collection verified non-empty in `data/catalog.json`
- [ ] Target keyword in H1, first 100 words, one H2 — reading naturally
- [ ] Meta description written, 150–160 characters
- [ ] No claim about a product that isn't true of the actual listing
- [ ] Front matter complete, `word_count` filled in
- [ ] It genuinely answers the query better than what's ranking now — if not, don't ship it
