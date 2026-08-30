# Backlog — non-content work

Everything here needs **owner sign-off** (per `CEO-CHARTER.md`). The agent finds, verifies,
scopes and proposes. The owner executes or approves.

Ordered by value ÷ effort. Discovered 2026-08-30 unless noted.

---

## 0. The entire Christmas pajama line is unpublished 🔴 URGENT — found 2026-08-30

Eight products are sitting in **DRAFT** status with zero inventory:

| Product | Price |
|---|---|
| Merry Rex-Mas — Adult Dinosaur Christmas Pajama Set | $59.99 |
| Tree-Rex — Adult Dinosaur Christmas Pajamas | $59.99 |
| Fa Rawr Rawr — Adult Dinosaur Christmas Pajamas | $59.99 |
| Angry Merry Rex-mas — Adult Dinosaur Christmas Pajamas | $49.99 |
| Merry Rex-Mas — Kids Dinosaur Christmas Pajamas | $49.99 |
| Tree-Rex — Kids Dinosaur Christmas Pajamas | $49.99 |
| Fa Rawr Rawr — Kids Dinosaur Christmas Pajamas | $49.99 |
| Angry Merry Rex-mas — Kids Dinosaur Christmas Pajamas | $49.99 |

These are the highest-priced items in the catalog, they are family-matching (the format
that sells hardest at Christmas), and they are invisible to customers and to Google.

The demand is real and dated: **`dinosaur pajamas adult` peaks at 720/mo in December**
(390 average, SD 25, $0.97 CPC, Transactional intent). The `dinosaur-christmas` collection
already has 52 products, so the category is otherwise live.

**Why this is #0:** Christmas pajama searches ramp from October. A product published in
December has missed its own season. Publishing these takes minutes; the window does not
reopen for a year.

**Ask:** were these drafted deliberately (supplier problem, artwork issue), or did they
just never get flipped live? If they can be published, do it before the end of September
and the Christmas content queue in `KEYWORDS.md` gets a real destination to link to.

## 1. Five collections have zero products 🔴 HIGH

| Collection | Products | Cost of leaving it |
|---|---|---|
| `dinosaur-masks` | 0 | **"dino mask" = 9,900/mo, SD 30.** Highest-volume unserved term we found. |
| `dinosaur-beanie` | 0 | "dinosaur beanie" is already a tracked project keyword |
| `hooded-dinosaur-blankets` | 0 | "hooded dinosaur blanket" is a tracked keyword; the standalone product does 31 visits/mo |
| `personalized-dinosaur-shirt` | 0 | "custom dinosaur shirt" $1.78 CPC, "personalized dinosaur gifts" $1.88 CPC — the most commercially valuable terms in the set |
| `dinosaur-dress-socks` | 0 | `dinosaur-socks` (36) and `dinosaur-socks-mens` (34) are stocked — likely just needs merging |

An empty collection page is worse than no page: it gets crawled, adds thin content to the
site profile, and converts nobody. **Either stock them or unpublish them.**

**Ask:** which of these can be stocked from existing suppliers? `dinosaur-masks` first —
9,900/mo is worth a real merchandising conversation.

## 2. Three duplicate collection pairs 🔴 HIGH

- `dinosaur-ornaments` **and** `dinosaur-christmas-ornaments` — both 9 products
- `dinosaur-christmas-pajamas` **and** `dinosaur-christmas-pajamas-1` — both 7 products
- `miscellaneous` **and** `all-misc` — both 13 products

These are near-certainly the source of Ubersuggest's **HIGH-impact** `have_title_duplicates`
and `duplicate_meta_descriptions` audit flags. Duplicates split link equity and make Google
pick a canonical for us.

**Proposal:** keep the better-named URL of each pair, 301 the other to it. The Christmas
pair matters most — resolve before the November season.

## 3. One blog post is titled in Indonesian 🟡 MEDIUM

`/blogs/blog/flying-dinosaurs-the-complete-guide-to-prehistoric-creatures-of-the-sky-2`
renders as **"Dinosaurus Terbang: Panduan Lengkap Makhluk Prasejarah"** on an
English-language US store — while pulling ~64 visits/mo.

Also note the `-2` suffix: there is likely an original version of this post, meaning a
duplicate-content pair on top of the language problem.

**Proposal:** retitle to English, check for the original, consolidate if both exist.
Low effort, and it's currently on a page earning real traffic.

## 4. Thin content flagged site-wide 🟡 MEDIUM

Ubersuggest's audit flags `content_count_words` at **HIGH impact**. This is the same root
cause as the entire rescue queue in `KEYWORDS.md` — 323 `dinosaur-facts` articles ranking
in positions 20–40 because they are too short to compete.

Not a single fix; it is the Play 1 programme in `STRATEGY.md`. Listed here so the audit
flag is traceable to the work that resolves it.

**Ask:** approve a standing arrangement for rewrite briefs, so each one doesn't need a
separate round trip. This is the biggest single lever on the business and it is currently
gated on approval latency.

## 5. Missing meta descriptions + title length issues 🟢 LOW

Audit flags: `meta_description_empty` (medium), `title_long` (medium), `title_short` (medium).

Low individually; worth a single batch pass rather than fixing one at a time. Bundle into
the first rewrite batch once #4 is approved.

## 6. Category question: party supplies 🟢 LOW — needs a decision, not a fix

`dinosaur birthday party supplies` (6,600/mo, SD 34) and `dinosaur party decorations`
(5,400/mo) are unserved. The store has a `dinosaur-birthday-party` blog with exactly
**1 article**, which suggests this was started and dropped.

**Ask:** was party goods deliberately abandoned? If it's still interesting, there's
~12,000/mo of demand adjacent to inventory we already carry (`dinosaur-flags`,
`dinosaur-posters`, `dinosaur-stickers`, `toys`). If not, say so and the terms get
permanently marked ⏭️ Skip so we stop re-surfacing them.

## 7. Daily Routine fires without Ubersuggest/Shopify connectors 🟡 MEDIUM — infrastructure

The daily article Routine (`trig_012cPKMi3SWxBwrokr5QMJvr`, 11:00 UTC / 7am EDT) was
created from a Claude Code session, and triggers created that way **cannot carry MCP
connectors** on this account — the `connectors` parameter is rejected with
*"not available for this organization."*

**Consequence:** the daily session can read and write this repo and push to GitHub, but it
cannot call Ubersuggest for fresh keyword data or Shopify to verify inventory. It falls
back to the figures cached in `KEYWORDS.md` / `data/keywords.json` (2026-08-30 pull) and
the collection map in `data/catalog.json`, and it is instructed to say so in the update
rather than invent numbers.

**Fix (owner, ~2 minutes):** recreate or edit this Routine from the **claude.ai Routines
UI**, where Ubersuggest and Shopify can be attached as connectors. Same prompt, same
schedule. Then delete the API-created one so it doesn't double-run.

Until then the cached data is good for roughly a month of queue items — every entry in
`KEYWORDS.md` already carries verified volume, difficulty, CPC and intent. After that the
numbers go stale and the queue needs a manual refresh from a session like this one.
