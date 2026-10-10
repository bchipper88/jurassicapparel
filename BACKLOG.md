# Backlog — non-content work

Everything here needs **owner sign-off** (per `CEO-CHARTER.md`). The agent finds, verifies,
scopes and proposes. The owner executes or approves.

Ordered by value ÷ effort. Discovered 2026-08-30 unless noted.

### Monthly review — 2026-10-01

**Closed this month:** #0 (deliberate), #3 (title now English), #23 (structural fix), #33 (paged
recount). #13's agent-side fix is done; its owner-side toy decision is still open.

**If the owner does five things this month, in this order:**
1. **#36:** swap 3 links in the new pillow post to the collection that ranks, and pick
   `dinosaur-pillows-cases` as the canonical pillow collection. About 5 minutes.
2. **#21 + #22:** a live `dinosaur-pajamas` collection before the December peak.
3. **#30 / #25:** stocking shipping times and the empty shipping policy page, before
   Christmas orders start.
4. **Flying-dinosaurs rescue** (KEYWORDS.md): fix the cut-off title and write a meta
   description, on the page that ranks #13–30 for eight terms worth 5,400–27,100/mo each.
5. **#2 / #36:** 301 the four duplicate collection pairs.

Everything else stands as written below.

---

## 0. ~~Christmas pajama line unpublished~~ ✅ RESOLVED 2026-08-30 — deliberate

Eight Christmas pajama products (4 adult $49.99–$59.99, 4 kids $49.99) sit in DRAFT with
zero inventory. Raised as urgent on 2026-08-30 because `dinosaur pajamas adult` peaks at
720/mo in December and the products were invisible to search.

**Owner's answer: they are in draft on purpose.** Closed — no action.

**Standing instruction for the agent: do not re-flag these.** If Christmas pajama content
gets queued, do not link to these products or assume they will be live. Point Christmas
content at the [`dinosaur-christmas` collection](https://jurassicapparel.com/collections/dinosaur-christmas)
(52 products) and `christmas-dinosaur-stockings` (15) instead.

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
- `dinosaur-throw-pillow` **and** `dinosaur-pillows-cases` — the same 11 products *(added 2026-10-01, see #36)*

These are near-certainly the source of Ubersuggest's **HIGH-impact** `have_title_duplicates`
and `duplicate_meta_descriptions` audit flags. Duplicates split link equity and make Google
pick a canonical for us.

**Proposal:** keep the better-named URL of each pair, 301 the other to it. The Christmas
pair matters most — resolve before the November season.

## 3. ~~One blog post is titled in Indonesian~~ ✅ RESOLVED — verified 2026-10-01

The live page now renders an English `<title>` and body (last edited 2026-02-22, so the
2026-08-30 finding most likely came from stale crawl data). The `-2` URL is the only published
copy; the original and `-1` versions are unpublished drafts, so there is no live duplicate.
What remains is folded into the **flying-dinosaurs rescue** (KEYWORDS.md): the `<title>` is cut
off at "…of the S" and there's no meta description of its own. This page now ranks #13–30 for
eight terms worth 5,400–27,100/mo each, so that rescue is worth doing.

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

## 7. Daily Routine stalls on permission prompts 🔴 HIGH — infrastructure

**Corrected 2026-08-31.** The earlier version of this item said the Routine had no MCP
connectors because it was created through the API. That was wrong — I asserted it without
reading the trigger back. Reading `trig_012cPKMi3SWxBwrokr5QMJvr` shows Ubersuggest and
Shopify **are both attached** under `mcp_connections`. Klaviyo is not, and does not need
to be for this routine.

The real defect is permissions. The Routine fired 2026-08-31 at 11:44 UTC (7:44am EDT) and
produced **nothing** — no `updates/2026-08-31.md`, no article, no commit. Each firing
spawns a fresh session in the **default permission mode**, which prompts before every Bash
command and MCP call. The first action is `git clone`. That prompt has no one to answer it
at 7am, so the session hangs until the container is reclaimed.

Being listed in the trigger's `allowed_tools` makes a tool *available*, not *pre-approved*.
Those are separate gates, and only the second one matters here.

**Also found:** the trigger's outcome branch is `claude/wizardly-clarke` — an auto-generated
name, not `claude/lehigh-valley-routines-keywords-hvzg9g`. Work could land on the wrong
branch once the routine actually runs.

**Corrected again, same day, after the owner opened the Permissions tab.** It reads:

> ⓘ Claude created this routine, so it runs in Auto mode — connector calls are checked by a
> classifier

There is no mode selector. My previous instruction — "set a permission mode that doesn't block"
— described a control that does not exist here. The mode is locked *because Claude created the
Routine*, so it cannot be fixed by editing the Routine.

Auto mode never prompts a human. MCP calls go to a classifier; a denial tells the agent to stop
and ask the owner. At 7am nobody answers, and the run ends.

**Fix (owner): create the Routine yourself** from claude.ai → Routines → New. A human-created
Routine is not locked to Auto mode. Same schedule (`0 11 * * *`), same two connectors, outcome
branch `claude/lehigh-valley-routines-keywords-hvzg9g`, same prompt. Then delete
`trig_012cPKMi3SWxBwrokr5QMJvr` so they don't double-run.

`.claude/settings.json` (`docs/ROUTINE-PERMISSIONS.md`) is worth adding as defense in depth but
is **not** the fix — settings rules govern prompting, not the Auto-mode classifier.

**Known remaining gap after both fixes:** `articleCreate` runs through
`mcp__Shopify__graphql_mutation`, a tool name that covers every Shopify mutation including
product, collection and theme writes. Permission rules match tool names and cannot be scoped
to one mutation, so it stays in `ask` — the routine will draft and commit unattended but the
live publish will still wait for approval. See item #8 for the fix.

Full write-up: `docs/ROUTINE-PERMISSIONS.md`.

## 8. Publishing needs a narrow path that isn't `graphql_mutation` 🟡 MEDIUM

Same-day publishing is granted by the charter but cannot be automated safely today, because
the only tool that can create an article is also the tool that can rewrite the storefront.

**Fix:** `scripts/publish-article.py`, using a Shopify Admin API token scoped to blog article
write only, allowlisted as `Bash(python3 scripts/publish-article.py *)`. Strictly narrower
than allowlisting `graphql_mutation`, and it restores unattended same-day publishing.

Needs: a custom app in Shopify admin with `write_content` scope, the token in the Routine's
environment variables, and the script. Not built.

## 12. The blog is cannibalising itself on gift guides 🔴 HIGH — added 2026-09-05

Found while verifying today's target against live content. The `blog` blog holds **85
articles**. Twelve of them target the same commercial intent:

**Published, all live, all competing with each other:**

| Article | Published |
|---|---|
| The Ultimate Dinosaur Gift Guide: 25 Prehistoric Presents They Will Actually Love | 2026-01-28 |
| Dinosaur Valentines Day Gifts That Will Make Their Heart Go Rawr | 2026-02-03 |
| The Ultimate Guide to Dinosaur Gifts for Adults Who Never Outgrew Their Dino Phase | 2026-02-19 |
| Dinosaur Gifts for Girlfriend: Unique Ideas She'll Actually Love | 2026-03-07 |
| Dinosaur Christmas Gifts: The Ultimate 2026 Guide for Dino Lovers | 2026-03-07 |
| 25+ Dinosaur Gift Ideas for Every Prehistoric Enthusiast | 2026-03-10 |

**Plus six unpublished drafts on the same intent**, including four near-identical copies of
*"The Ultimate Guide to Dinosaur Gifts: 15 Prehistoric Presents for Every Fan"*.

Six live pages chasing `dinosaur gifts` (1,600/mo, SD 21, $1.10 CPC, 4,400 in December) means
Google picks one and the rest split the link equity. **This is a concrete, page-level instance
of the Day 1 finding that we rank for more and earn less.**

Duplicates are not limited to gift guides. Also live or drafted more than once:
*Flying Dinosaurs* (×3, one published), *Spinosaurus mirabilis / Hell Heron* (×4),
*Foskeia pelendonum* (**×2, both published**), *Doolysaurus* (×2), *Stegosaurus Facts* (×2,
one published), *Triceratops Facts* (×2, one published), *Dinosaurs for Adults* (×2),
*The Dinosaur Aesthetic* (×2), *Scientists Just Found a 2-Pound Dinosaur* (×2),
*Ultimate Dinosaur Birthday Party Guide* (×2), *Dinosaur Hoodie* guides (×2 drafts, plus a
stray `2026-02-22-dinosaur-hoodie-guide`).

There is also an article literally titled **"Test Post - DELETE ME"** sitting in the blog.

**Proposal:** one consolidation pass. For each cluster, pick the canonical URL (the one with
rankings — check `page_overview` before choosing), merge the best material into it, 301 the
rest, and delete the unpublished duplicates and the test post. Gated under the charter, so it
comes as a brief.

**Process change made today, no approval needed:** the queue is now checked against live blog
content before a keyword is written, not only against keyword metrics. The old queue was built
from Ubersuggest alone, which is how `dinosaur gifts` got queued as new content when six live
pages already served it.

**Update 2026-09-24 — the brief is written, and the risk is lower than assumed.**
`content/rescues/2026-09-24-dinosaur-gifts-consolidation.md` carries the full 1,909-word
replacement copy, link-checked, ready to publish on approval. (It exists because a second
session that day wrote the article before running the check above, and the check caught it —
the guard works.)

Ran the `page_overview` check this item asked for. The result removes the hard part:
`page_overview` returns `noData` for both generic guides, and **no gift-guide URL appears
anywhere in the domain's top ~180 ranking keywords by traffic** (`domain_keywords`, locId 2840,
2026-09-24). Six pages, twelve months, no rankings between them.

So there is **no incumbent ranking to protect**, and the canonical can be chosen on URL quality
instead. The brief proposes a clean `/blogs/blog/dinosaur-gifts` (none of the six is
exact-match), 301s from the three generic guides, and keeping girlfriend / Christmas /
Valentine's as separate intents with their own volume. December peak is ~10 weeks out; done in
the next fortnight it settles before the season.

## 13. Collections that are full of DRAFT products read as empty 🟠 HIGH — added 2026-09-05

`data/catalog.json` counts **all** products in a collection, published or not. Two collections
pass the link check while showing a customer almost nothing:

| Collection | Counted | Actually ACTIVE |
|---|---|---|
| `toys` | 30 | **0 — every one of the 30 is DRAFT** |
| `dinosaur-jewelry` | 6 | **1** |

`scripts/check-links.py` would have waved through a link to `/collections/toys`. It is not a
zero-product collection by the catalog's definition, but it is an empty page to a shopper and
to Google — the same defect as BACKLOG #1, hidden behind a number that looks fine.

**Two fixes, and they are separate:**

1. *Agent-side, no approval needed:* the monthly `catalog.json` refresh must record ACTIVE
   product counts, not total counts, and `check-links.py` should fail on an active count of 0.
   ~~Scheduled into the 2026-10-01 monthly routine.~~ **✅ Done 2026-09-24 — see #23.** Figures
   above independently re-confirmed the same day. Remaining: extend `active` counts from the 15
   verified collections to the whole catalog at the 2026-10-01 refresh.
2. *Owner:* decide what happens to the 30 drafted toys. `dinosaur toys` is a real term and
   the `dinosaur-toys` blog exists with 1 article. Either publish them or unpublish the
   collection. **Not urgent and not a re-flag of the Christmas pajamas (#0) — different SKUs,
   no prior decision recorded.**

## 14. Merchandising gap: no adult one-piece garment 🟡 MEDIUM — added 2026-09-05

Today's queued target, `dinosaur onesie adult`, had to be skipped because the catalog contains
no adult onesie. A product search across *onesie*, *jumpsuit*, *kigurumi*, *union suit*,
*romper* and *one-piece* returns nothing for adults.

What that costs, at US volumes verified 2026-09-05:

| Keyword | Avg/mo | October | SD |
|---|---|---|---|
| dinosaur onesie | 3,600 | **12,100** | 26 |
| dinosaur onesie adult | 1,900 | **6,600** | 25 |

Both are inside the winnable band for a DA-17 site, both peak hard in October, and both are
transactional. That is ~18,700 searches in October alone against difficulty we can beat, and
we cannot honestly write a word of it.

**Ask:** is an adult dinosaur onesie or union suit sourceable from any of the nine POD apps
already installed? If yes it is a strong October SKU and the content is ready to write. If not,
say so and both terms get permanently marked ⏭️ Skip so they stop coming back round the queue.

## 15. Two ACTIVE shoe products cannot be bought 🟠 HIGH — added 2026-09-23

*Dinosaur Stomp - Women's High Heels* (`womens-high-heels`) and *Dinosaur Skeleton - Women's
High Heels* (`dinosaur-skeleton-womens-high-heels`) are ACTIVE and sit in
`dinosaur-shoes-dinosaur-sneakers`, `dinosaur-shoes-womens` and `shoes-adult`. Unlike every
other shoe, they **track inventory, have 0 units, and are set to DENY overselling** — so they
show as sold out. Every other made-to-order shoe has inventory tracking switched off.

A shopper browsing the womens shoes collection hits two dead ends at $79.99 each. The listing
also says "Estimated shipping time is 2-4 weeks" — the same made-to-order wording as the
sneakers — which suggests the tracking setting is a mistake rather than a real stock-out.

**Ask (inventory is gated):** if the heels are still producible, switch off inventory
tracking to match the other shoes; if not, unpublish them. The Day 3 article does not mention
heels for this reason.

## 16. Shoe titles misstate their size range 🟡 MEDIUM — added 2026-09-23

Found while writing the shoes guide; all read from the live listings 2026-09-23.

| Product | Title says | Sizes actually offered |
|---|---|---|
| `splatter-dinos-kids-dinosaur-shoes` | "Kid's Dinosaur Shoes" | Women's + Men's only — **no kids' sizes** |
| `pastel-dinosaurs-kids-dinosaur-sneaker` | "Kids Dinosaur Sneaker" | Women's + Men's only — **no kids' sizes** |
| `tiny-dinos-blue-dinosaur-sneakers` | (in kids collection) | Kids' run starts at youth 1, not child 11 |

A parent who clicks "Kid's" and finds only adult sizes bounces. Both products are in
`dinosaur-shoes-for-kids`, so they also pad that collection with two shoes a child can't wear.

Also: *Color Your Own Dinosaur Shoe* still carries "(Currently experiencing delays)" in its
shipping copy twice. If the delay is over, that line is costing conversions; if it isn't, the
other listings are understating lead time.

**Ask (product copy is gated):** retitle or add kids' sizes to the two mislabelled sneakers;
confirm whether the "delays" note is current.

## 17. Live Christmas-gifts post links out to a third-party site 🟠 HIGH — added 2026-09-24

`/blogs/blog/dinosaur-christmas-gifts-the-ultimate-2026-guide-for-dino-lovers` (published
2026-03-07) — the only Christmas post on the blog — sends readers to **thebestchristmas.co**
with four outbound links ("check out The Best Christmas — they've got everything from gift
guides…"). It also recommends things we don't sell (excavation kits, replica skulls, museum
memberships), links only to `/collections/all`, `/collections/kids` and
`/collections/dinosaur-shirts` rather than to the 52-product `dinosaur-christmas` collection,
and repeats its closing footer paragraph twice, inside an unclosed `<ol>`.

Outbound links like these are usually a paid or swapped placement. Either way, the store's one
Christmas article is sending December traffic to someone else's site. It also belongs to the
gift-guide cluster in #12.

**Ask (editing live pages is gated):** do you know why the links are there? If not, remove
them. The Day 4 ornaments guide deliberately does not link to this post.

## 18. Merchandising gap: no dinosaur Christmas sweater 🟡 MEDIUM — added 2026-09-24

`dinosaur christmas sweater` — 720/mo avg, **2,900 Nov / 4,400 Dec**, SD 26, $0.15 CPC
(Ubersuggest, locId 2840, 2026-09-24). Checked as today's target; skipped on inventory. There
is no knit or "ugly" sweater in the catalog. The only Christmas crewnecks are two sweatshirts
(*T-Rex Winter Forest*, *Merry Little Rexmas*). A product titled *Ugly Dinosaur Sweater - Adult
Dinosaur Shirt* exists but is a **t-shirt**, and it's in DRAFT.

**Ask:** can one of the installed POD apps do an all-over-print "ugly sweater" style knit or
sweatshirt? If it can be listed by late October, the article is ready to write for November.

## 19. "Personalized" ornament has no visible personalization field 🟡 MEDIUM — added 2026-09-24

*Watercolor Dino Ornament - Personalized* ($17.99, ACTIVE) has a listing photo showing a name
("JESSICA") printed under the dinosaur, but the only options are **Shape** and **Design**. The
product page HTML contains no text input or `properties[...]` field. If no app injects one with
JavaScript, a customer cannot enter a name and will get the ornament without one.

**Ask (product settings are gated):** open the product page and try to add a name. If it isn't
possible, either add a personalization field or retitle the product and change the photo. The
Day 4 article describes it as a watercolor ceramic ornament and makes no personalization claim.

## 20. Mug priced lower in the larger size 🟢 LOW — added 2026-09-24

*T-Rex Winter Forest - Dinosaur Mug*: 11 oz $19.99, 15 oz $21.99, **20 oz $21.50**. Every other
Christmas mug is $23.99 for 20 oz. Probably a typo. Pricing is gated.

---

# Klaviyo — added 2026-08-30

Full findings in [`audits/2026-08-30-klaviyo.md`](audits/2026-08-30-klaviyo.md).
Klaviyo produced **$1,092.08 and 15 orders in the last 12 months** from 14,316 sends.

## K1. Abandoned Cart flow is damaging sending reputation 🔴 URGENT

12.77% flow bounce rate (790 bounces). One message, `SbKzEd`, bounced **695 of 1,798 sends
— 38.65%**, and drew the account's only spam complaints. Open rate 5.2% against the Welcome
Series' 32.4% on an overlapping audience.

A bounce rate this high risks account throttling and suppresses inbox placement for every
other email, including the Welcome Series that actually works.

**Diagnosis corrected 2026-08-31 by reading the flow config.** The earlier claim — that the
flow triggered on Added to Cart and lacked a purchaser exclusion — was **wrong**. It already
triggers on `Checkout Started` (`RWsZMn`) and already filters `Placed Order` = 0 since flow
start. Trigger and audience logic are fine.

The real problems:
1. **Smart Sending is OFF on all six messages** — no guard against over-mailing. One flag each.
2. **Five emails over eight days.** Emails 2–5 open at 4.6–5.6% and click at 0.0–0.3%;
   email #2 recorded **zero clicks in twelve months**.
3. **Discount ladder 10% → 10% → 15%** across emails 3–5, which trains repeat abandonment.
4. **An A/B test created 2024-09-11 has never run** — both variations show zero sends in
   12 months while the control took all 1,798.
5. **The 38.65% bounce is upstream, in Shopify.** Email #1 bounces at 38.65%, emails #2–5 at
   1.6–2.9% — the signature of a first send hitting invalid addresses that then get
   suppressed. Since the trigger is `Checkout Started`, every one of those was typed into
   the Shopify checkout. **That is bot or junk checkout traffic and no Klaviyo change fixes
   it.** Needs Shopify-side investigation: bot protection at checkout, and whether the bad
   checkouts share IP ranges, disposable email domains, or zero-value carts.

**Action:** pause the flow (owner, Klaviyo → Flows → `RsULBu` → Draft), then investigate #5
on the Shopify side. Rebuild spec: [`klaviyo/abandoned-cart-v2.md`](klaviyo/abandoned-cart-v2.md)
(structure) and [`klaviyo/abandoned-cart-v2-copy.md`](klaviyo/abandoned-cart-v2-copy.md) (copy).

**Built 2026-08-31:** flow **`Vc6TWN`** — *[DRAFT] Abandoned Cart v2 - 3 emails / 3 days* —
created via API in `draft` status (every action also `draft`, so it cannot send).
https://www.klaviyo.com/flow/Vc6TWN/edit

Structure verified: trigger `Checkout Started`, `Placed Order` = 0 since flow start, re-entry
once per 7 days, 4h → +20h → +48h, **Smart Sending on for all three messages**, UTM tracking
on. **All three emails now use the store's own design** — clones of the original templates
(`SCtH98`, `TaRvqm`, `X4dhEn`), attached as `SWKuvf`, `SCet7F`, `Yi28Sb`, all
`SYSTEM_DRAGGABLE` so they stay editable in the visual editor.

A first attempt hand-coded replacements without ever opening the originals. It was wrong:
the Liquid used `item.image_url` / `item.title` / `item.line_price` instead of Klaviyo's
Shopify syntax (`item.product.images.0.src|missing_product_image`, `item.product.title`,
`currency_format`), so the carts would have rendered **empty**; it had no empty-cart guard;
and `CODE` templates cannot be edited in the drag-and-drop editor. The originals also carry
a branded header, category nav, hero image, social links and Outlook compatibility.

Unverified claims written and then removed: *"adult pieces go 2XS to 6XL"* (true of one
product; a sample of twelve adult products runs S–XL or S–2XL, none reach 6XL), *"sizes never
sell out"* (contradicted by zero-inventory products), and *"a real person reads it"*.

Two deliberate placeholders remain, both visually flagged in the emails: the shipping window
in email 2 (the Shopify shipping policy body is **empty**, so nothing was invented) and the
coupon code plus discount percentage in email 3 (a commercial decision).

**Blocked on the owner:** add the email content, replace the placeholder shipping/returns
copy, add the temporary 180-day engagement guard in the UI, pause `RsULBu`, and investigate
the Shopify checkout junk traffic behind the 38.65% bounce.

## K2. No authenticated sending domain 🟠 HIGH

`get_sending_domains` is empty — all mail goes out on Klaviyo's shared infrastructure with
no DKIM/SPF on `jurassicapparel.com`. Reputation is pooled with every other sender on that
shared resource, and Gmail shows a "via klaviyomail.com" line under the sender name.

**Setup:** Klaviyo → Settings → Domains → add a sending subdomain (`email.jurassicapparel.com`).
Klaviyo emits 3–4 CNAMEs; add them wherever the domain's DNS lives (likely Shopify admin →
Settings → Domains). Then add a DMARC TXT record at `_dmarc.jurassicapparel.com`, starting
at `p=none` to monitor before tightening.

**Shopify IS the DNS host — proven 2026-08-31.** A TXT record added in Shopify's DNS panel
resolved publicly within minutes in both Google's and Cloudflare's resolvers. Shopify runs
its DNS service on Google Cloud DNS, which is why the registry shows
`ns-cloud-a1..a4.googledomains.com` — those *are* Shopify's default nameservers.

*Two earlier findings in this file were wrong and have been corrected: DNS is not in a
customer-owned Google Cloud project, and it is not managed at Squarespace. NS records and
SOA hostmasters identify infrastructure, not the control plane. Full detail and the
verification method: [`docs/DNS.md`](docs/DNS.md).*

**Status:** the `klaviyo-site-verification=XJSW3M` TXT at `@` is **done and live**.

**Blocker:** the four NS records delegating `email` to `ns1..ns4.klaviyo.com` cannot be added
— Shopify's DNS editor offers only A, AAAA, CNAME, MX, TXT, SRV. No NS type.

Two ways through:
1. **Ask Klaviyo support whether the CNAME-based sending domain setup is still available.**
   Avoids touching DNS hosting. Try this first — it costs one support ticket.
2. **Move DNS to Cloudflare** — [`docs/DNS-MIGRATION-RUNBOOK.md`](docs/DNS-MIGRATION-RUNBOOK.md).
   The switch is Shopify's own **Change** button under Settings → Domains → Nameservers.
   Registration does not move. ⚠️ Cloudflare proxies new records by default; the apex A,
   apex AAAA and `www` must all be set to **DNS only** or Shopify's SSL breaks.

**The From address does not change.** An email carries two sender identities: the *header
From* the recipient sees, and the *Return-Path / DKIM domain* that SPF and DKIM check. The
sending subdomain only sets the second. Recipients still see
`Jurassic Apparel <john@jurassicapparel.com>`.

This passes DMARC because alignment defaults to **relaxed**, which accepts any subdomain of
the same organizational domain — `email.jurassicapparel.com` aligns with
`jurassicapparel.com`. **Do not set strict alignment** (`adkim=s` / `aspf=s`); that is the
one setting that would break it.

Adding these CNAMEs does not touch the root domain's MX records, so mail to
john@jurassicapparel.com keeps arriving exactly as now, and replies still route via Reply-To.

Use a subdomain rather than the root deliberately: it isolates marketing sender reputation
from business email, so a bad campaign cannot damage supplier and customer correspondence.
Prefer `email.` or `send.` over `mail.`, which is likelier to collide with an existing record.

**Downgraded from URGENT to HIGH on 2026-08-30.** The strict Google/Yahoo SPF+DKIM+DMARC
mandate binds senders at 5,000+ messages/day; at ~1,300 subscribers we are well under it,
so this is an optimization rather than a compliance problem. K1 is the real emergency.

**Sequencing — this matters.** A new sending domain starts with zero reputation, and the
first sends on it set how mailbox providers judge us. Do NOT authenticate and then mail the
full list: that burns a fresh domain on the same dead addresses bouncing today.

Correct order: **fix K1 → clean the list (K3) → authenticate → send to the engaged segment
first**, ramping volume over ~2 weeks. Doing it backwards wastes the exercise.

## K3. No suppression on any campaign 🔴 HIGH

Every campaign has `excluded: []`. Sends have gone to *Preview List* (Klaviyo's internal
default) and *SMS Subscribers* (a phone list). *Old List Upload* appears in 5 campaigns; the
March 2026 send including it bounced at **20.87%**.

**Action:** build an "Engaged 90 day" segment and send only to it until reputation recovers.

## K4. Zero segments exist 🟠 HIGH

The segments API returns an empty array. Every campaign is a full-list blast. Build:
engaged 30/60/90, customers vs never-purchased, VIP, unengaged 180+ (suppress), and category
interest (kids / adult / accessories).

## K5. No campaign sent since 22 March 2026 🟠 HIGH

Five campaigns in twelve months, none in over five months. Best performer of the year was
"T-Rex Diet Facts" (33.9% open, 2.10% click) — our own blog content, beating the promotional
sends. Restart at 2–4/month, content-led.

## K6. Missing flows 🟠 HIGH

Seven flows exist; three are shipping notifications and one is a two-year-old draft.
Missing entirely: **post-purchase** (the expensive gap for a repeat-purchase apparel brand),
back-in-stock, second-purchase/cross-sell, sunset, price drop, birthday/VIP.
The **Customer Winback** flow has been in draft since Sept 2024.

## K7. Back-in-stock subscriptions collected but unserved 🟠 HIGH

`Subscribed to Back in Stock` is live and collecting; no flow exists to notify anyone.
Compounds with the out-of-stock inventory found in the storefront audit (kids' sneakers,
Mamasaurus tees). Customers are asking to be told and nothing tells them.

## K8. Browse Abandonment fired 15 times in a year 🟠 MEDIUM

Opens at 35.7% when it fires, so the message is fine — the trigger isn't. Note `Viewed
Product` comes from the API integration rather than Shopify; verify Klaviyo's onsite
JavaScript is installed and firing on product pages.

## K9. SMS delivering ~14–24% 🟡 MEDIUM

Shipping flows deliver 15–24 messages per ~100–132 recipients. That pattern means A2P 10DLC
registration is incomplete or rejected. No SMS marketing campaign has ever been sent.

## K10. Product catalog not synced 🟡 MEDIUM

`get_catalog_items` is empty. No dynamic product blocks, no recommendations, no reliable
product imagery in cart/browse emails.

## K11. List growth apparatus is one un-optimized popup 🟡 MEDIUM

~1,300 subscribers. The Email Popup has not been edited since 10 Sept 2024 and has no A/B
test. A "Black Friday deals" form has been in **draft since 11 Sept 2024** — two Black
Fridays have passed.

---

# Unit economics — added 2026-08-31

## 9. No cost of goods recorded on any variant 🔴 HIGH — blocks all profit reporting

`inventoryItem.unitCost` is **null on every product variant** — checked 100+ across sneakers,
stickers, mugs, blankets and dog beds. Not one has a cost.

**Consequence:** Shopify's native profit reports are blank, and the question "am I making
money" cannot be answered from the store's own data. It had to be reconstructed by hand
(`audits/2026-08-31-unit-economics.md`), and even then the answer is a range — roughly
break-even to ~$5,400/yr — rather than a number.

Print-on-demand makes this awkward: nine fulfilment apps are installed (Printful, Printify,
Subliminator, Gooten, JetPrint, AOP+, Pillow Profits, teelaunch, DSers), each with its own cost
sheet, and cost varies by size and print placement.

**Fix:** set `unitCost` on the top ~20 sellers first — about an hour, and captures most of the
value since the tail contributes little. Full catalog is an afternoon. After that Shopify
reports gross profit per order natively, forever.

Owner action — the agent cannot do this (product writes are gated by the charter).

## 10. 30 apps installed; subscription cost unknown 🟠 HIGH

`AppSubscription` is scoped to the querying app, so app spend is not readable through the API.
It has to be read from **Settings → Billing**.

At $1,323/month of revenue, every $130/month of app spend is 10% of the top line. Nine POD apps
are installed but the store cannot plausibly be using all nine — each redundant one that
carries a monthly fee is pure loss.

**Fix (owner, ~10 minutes):** open Settings → Billing, total the monthly charges, and cancel
any POD app not actively fulfilling orders. Record the total in
`audits/2026-08-31-unit-economics.md` so the profit range collapses to a number.

## 11. Returns are 8.9% of gross — $1,524.71/yr 🟠 HIGH

Against a published policy of made-to-order, **ALL SALES FINAL**, replacement only for damage
or misprint. On print-on-demand a return is a total loss: supplier paid, item shipped, customer
refunded, product unresellable. Roughly **$840 of goods cost destroyed** on top of the refunded
revenue.

Either the policy is not being enforced, or there is a real quality/sizing problem generating
genuine damage claims. **Read the actual refund reasons on the 12 months of returns** — this is
the largest recoverable leak visible in the data.

---

*Items 21-24 discovered 2026-09-24 while verifying sleepwear inventory for the `dinosaur pajamas`
article. Logged by a second run on the same day as items 17-20; the two sets do not overlap.*

## 21. No `dinosaur-pajamas` collection exists, and the term is the best-value keyword we own 🔴 HIGH — added 2026-09-24

`dinosaur pajamas` is **1,600/mo, SD 17, $1.57 CPC** (Ubersuggest, locId 2840, 2026-09-24),
peaking at 2,900/mo in December. SD 17 is the joint-lowest difficulty of anything with real
volume in `KEYWORDS.md` — the same difficulty as `dinosaur shirt`, which the rescue queue
calls the best single opportunity in the repo. The $1.57 CPC is the **highest of any keyword
in the entire queue**.

The store already ranks **#14** for it on a single product page
(`/products/realistic-jurassic-adult-dinosaur-pajamas`, 59 est. clicks/mo) at DA 16 — and a
DA-18 competitor sits at #4 on this SERP, so page 1 is reachable.

There is no collection page for it. The three ACTIVE sleepwear SKUs are scattered:

| Product | Price | Sizes | Status |
|---|---|---|---|
| Realistic Jurassic – Adult Dinosaur Pajamas | $49.99–$58.99 | 2XS–6XL | ACTIVE |
| Dino Fossils – Adult Dinosaur Pajamas | $50.00–$58.47 | 2XS–6XL | ACTIVE |
| Frosted Dino Cookie – Women's Pajama Shorts | $31.99–$33.99 | XS–2XL | ACTIVE |

**Fix (owner, ~10 minutes):** create a `dinosaur-pajamas` collection holding those three
products. A commercial collection URL is a far better ranking asset for a transactional term
than a single product page, and today's article is written to link into it the moment it
exists. Collection creation is gated by the charter, so the agent cannot do this.

## 22. Two duplicate `dinosaur-christmas-pajamas` collections, both storefront-empty 🟠 HIGH — added 2026-09-24

Two collections with the **identical title** "Dinosaur Christmas Pajamas":
`dinosaur-christmas-pajamas` and `dinosaur-christmas-pajamas-1`. Each lists 7 products, and
every one of those products is DRAFT with 0 inventory — so **both collections render empty to
customers** while still being crawlable.

This is almost certainly feeding the HIGH-impact duplicate-title and duplicate-meta flags in
the Ubersuggest site audit (see item 2).

Note this is *not* a re-flag of BACKLOG #0. The products being in draft is the owner's
deliberate decision and stands. The problem is that two duplicate, customer-facing, empty
collection pages exist regardless.

**Fix (owner):** delete or merge the `-1` duplicate; leave the primary alone unless the draft
decision changes.

**Agent side — done 2026-09-24:** both handles were moved into
`empty_collections_do_not_link` in `data/catalog.json`, so `scripts/check-links.py` now blocks
any article that tries to link them. Verified failing.

## 23. `check-links.py` counted products without checking publish status 🟠 HIGH — added 2026-09-24

The link checker read product *counts* from `data/catalog.json` and passed any collection with
a count above zero. `dinosaur-christmas-pajamas` has a count of 7 and would have passed — while
rendering as an empty page to every customer who clicked through.

The standing rule "never link a collection with zero products" was therefore enforceable only
against collections that were empty in the catalog snapshot, not against collections that are
*effectively* empty because their members are unpublished or out of stock.

**Fixed 2026-09-24** for the two known cases by blocklisting them. **Still open:** the weekly
`data/catalog.json` refresh should count only ACTIVE products, so this class of bug cannot
recur silently. That is an agent-side fix and is scheduled into the Monday routine.

**Also fixed 2026-09-24, independently and more generally — the "still open" half above is
done.** A concurrent run hit the same bug from the gifting side and implemented the structural
fix rather than blocklisting case by case:

- `data/catalog.json` now carries a `draft_heavy_do_not_link` list **and** verified `active`
  counts per collection.
- `scripts/check-links.py` fails on any blocklisted collection and prints "N live / M" wherever
  an active count is recorded. Regression-tested: `/collections/toys` now fails the check.

ACTIVE counts verified live 2026-09-24 for the 15-collection gifting set: `toys` **0 of 30**,
`dinosaur-jewelry` **1 of 6**, `dinosaur-christmas` 43/52, `dinosaur-ties` 7/9,
`dinosaur-stickers` 29/31, `dinosaur-socks` 35/36; the rest fully active. This independently
confirms #13's figures.

Two runs finding this bug the same day, from opposite ends of the catalog, is the argument for
the structural fix over per-case blocklists. **Remaining:** extend `active` counts from the 15
verified collections to the whole catalog at the 2026-10-01 refresh.


## 24. `Dino Nuggies – Women's Pajama Shorts` is DRAFT while its sibling is ACTIVE 🟡 MEDIUM — added 2026-09-24

`dino-nuggies-womens-pajama-shorts` sits in DRAFT with 59,994 units of inventory available,
while the near-identical `frosted-dino-cookie-womens-pajama-shorts` is ACTIVE and selling.
Same garment, same price band ($31.99).

This is not covered by BACKLOG #0 — it is not a Christmas product — so it looks like an
oversight rather than a decision. Publishing it would double the pajama-shorts range at zero
cost, ahead of the Nov–Dec sleepwear peak.

**Fix (owner, ~2 minutes):** set the product to ACTIVE, or confirm the draft is intentional so
the agent stops surfacing it.
## 25. The shipping policy page is empty 🔴 HIGH — Q4 conversion risk — added 2026-09-24

`shopPolicies` returns `SHIPPING_POLICY` with an **empty body**. The store publishes a shipping
policy page with nothing on it.

The refund policy by contrast is thorough and clear (made-to-order, **all sales final**,
replacement or refund for damage or misprint, request within 30 days, item unused and in
original packaging) — so this is a gap, not a pattern.

It matters most right now. These are made-to-order products, so the customer's real question in
November and December is "production time *plus* shipping time — will it arrive by the 25th?"
Days 3 and 4 both had to derive order-by dates from individual listings' shipping estimates
because the policy page says nothing. Every visitor who goes looking for that answer finds a
blank page and leaves.

**Fix (owner, ~15 minutes):** Settings → Policies → Shipping policy. Even a rough production +
transit range beats an empty page, and it would let the blog cite one source instead of
reverse-engineering dates per product.

## 26. Three different contact addresses across the legal pages 🟢 LOW — added 2026-09-24

The privacy policy gives `john.honochick@gmail.com` (a personal address) alongside the LLC's
registered address; the Contact policy gives `john@jurassicapparel.com`; the terms of service
give `info@jurassicapparel.com`. Three addresses, one personal, on the pages customers read
when deciding whether a store is legitimate.

**Fix:** use the domain address consistently.

## 27. The Routine fires multiple times a day, and the runs collide 🟠 HIGH — infrastructure — added 2026-09-24

**Three scheduled runs fired on 2026-09-24.** Day 4 published the ornaments guide; two further
runs each started on a stale clone, each researched a keyword, each wrote a full article, and
each then discovered on `git push` that the day was already done.

Nothing was lost — both later runs caught it and neither published, so the one-article-a-day
rule held. But the cost is real:

- **Two full articles written for one publishing slot.** One became a gated brief
  (`content/rescues/2026-09-24-dinosaur-gifts-consolidation.md`), one became tomorrow's post.
  Salvageable, but by luck rather than design.
- **Three-way merge conflicts** in `KEYWORDS.md`, `data/keywords.json`, `data/catalog.json`,
  `BACKLOG.md` and `updates/2026-09-24.md`, all resolved by hand.
- **Duplicate backlog numbering** — two runs independently filed a `check-links.py` item as #23,
  and two independently found the draft-collection bug. Merged, but it is a sign of the pattern.
- **Wasted Ubersuggest quota**, three sets of overlapping keyword pulls in one day.

The root cause is not visible from inside a session: it is either several schedules pointing at
the same prompt, or one schedule retrying. `docs/ROUTINE-PERMISSIONS.md` already documents the
permission-prompt stall, and a stalled run that gets retried would produce exactly this.

**Ask (owner, ~5 minutes):** open the Routine settings and confirm how many schedules target
this prompt. If there is more than one, delete the extras. If there is one that retries, the
stall in #7 is the thing to fix.

**Agent-side mitigation, already in effect:** every run now starts with
`git fetch && git pull` before reading the queue, and checks `updates/` for today's date before
writing. That turns a collision into a cheap no-op instead of a wasted article.

## 28. `md-to-shopify.py` needs the `markdown` package, and fresh containers don't have it 🟢 LOW — tooling — added 2026-09-25

On 2026-09-25 the publish step failed with `ModuleNotFoundError: No module named 'markdown'`
until I ran `pip install markdown` by hand. Every fresh Routine container will fail the same
way. **Fix:** add `pip install markdown` to the Routine environment's setup script, or have the
script fall back to a clear error that names the install command. It costs a minute per run
now, but a run that doesn't know the fix could mark the day blocked.

## 29. All 15 stocking listings promise a "personalized stocking" that can't be personalized 🟡 MEDIUM — product copy — added 2026-09-26

Every listing in `christmas-dinosaur-stockings` says *"we create your personalized stocking
with care"* in its shipping block, but none of them has a name field or any personalization
option (one variant each: `13" × 19.3''`). A shopper who searches "personalized dinosaur
stocking" and lands here will expect a name on the cuff. Same pattern as #19 (the ornament).
**Fix (owner, product copy — gated):** change "personalized" to "custom-printed" in the shipping
block, or add a personalization field. The Day 6 article says plainly that no name option exists.

## 30. Stockings ship in 10–30 business days — the longest window in the Christmas range 🟠 HIGH — Q4 conversion risk — added 2026-09-26

The stocking listings quote **2–5 business days production + 10–30 business days shipping**
(12–35 door to door) against 3–8 for the pajamas and 3–6 for the ornaments. Working back from the
slowest estimate, a stocking for Christmas Eve must be ordered by **November 3**; the search peak
(1,900/mo) is November–December, so much of the demand arrives after the safe window closes.
**Asks (owner):** (a) check whether the print provider offers a faster shipping tier for this
product and whether 30 days is still accurate; (b) consider an order-by line on the collection page
(collection copy is gated). The Day 6 article carries the order-by dates.

Also noted, not a bug: *Merry Christmas* is $33.55 while the other 14 are $34.99. Probably a
leftover price; worth a glance.

## 31. No birthday (non-Christmas) dinosaur wrapping paper — half the keyword's demand is unserved 🟡 MEDIUM — merchandising — added 2026-09-27

`dinosaur wrapping paper` does 1,600/mo on average, and the curve has a year-round floor of
**880–1,600/mo** (Jan–Oct) before the Christmas spike (Nov 2,400, Dec 4,400; Ubersuggest locId
2840, 2026-09-27). That floor is birthday wrap. All six products in
`dinosaur-christmas-wrapping-paper` are Christmas prints, so for ten months of the year the Day 7
article can only tell searchers we don't have what they want.
**Ask (owner, catalog — gated):** list two or three non-seasonal dinosaur wrapping papers
(e.g. a birthday print, a plain T. rex pattern) on the same blank as the Christmas range. The
print provider and product template already exist, so this is design work, not sourcing. Once
listed, the article gets a birthday section and the page earns all year.
Also noted: the Christmas listings' own copy says the paper is "ideal for birthdays", which a
Santa-hat print isn't. Product copy, gated.

## 32. Mug catalog: a mis-typed color-changing mug, inconsistent prices, and no care info 🟡 MEDIUM — catalog / product copy — added 2026-09-28

Found while counting mugs for the Day 8 article (live Shopify, 2026-09-28):

- **Raptor Watching – Disappearing Dinosaur Mug is typed `Mug`, not `Mug - Disappearing`**, so the
  smart collection `disappearing-dinosaur-mug` (rule: product type) holds 2 of the 3 color-changing mugs.
  Fix: set its product type to `Mug - Disappearing`. *(Product edit, gated.)*
- **The color-changing mugs are priced three different ways:** Retro Rex $24.99 / $29.99 (11/15 oz),
  Raptor Watching $24.99 (11 oz), and Possessed Rex $19.99 / $21.99, the same as a plain mug. One of
  these is probably wrong. *(Pricing, gated.)*
- **Two more odd 20 oz prices** beyond #20: *Dinosaurs Never Had Coffee* 20 oz is **$23.54** (every
  other 20 oz is $23.99), and T-Rex Winter Forest is still $21.50. *(Pricing, gated.)*
- **No mug listing says whether it's dishwasher or microwave safe.** It's the most common question
  about a printed mug, and the article has to say "the listings don't say". Asking the print provider
  and adding one care line to the shared description template would answer it for all 84. *(Product copy, gated.)*

## 33. ~~`catalog.json` active counts were capped at one page (50)~~ ✅ RESOLVED 2026-10-01

Monthly refresh re-counted every collection from a full paged list of the 109 DRAFT and 1
UNLISTED products. `phone-cases` is **62/62** ACTIVE (not 50), `dinosaur-mugs` **85/85**, and
`dinosaur-socks` 35 ACTIVE + 1 UNLISTED. All 100 live collections now carry an `active` count.

## 34. Christmas products missing from the `dinosaur-christmas` collection, and an odd toddler-dress price 🟡 MEDIUM — catalog — added 2026-09-29

Found while counting the collection for the Day 9 hub (live Shopify, 2026-09-29; paged count
**45 ACTIVE / 52**, the other 7 being the deliberate pajama drafts, #0):

- **Two ACTIVE Christmas products are not in `dinosaur-christmas`:** the *Merry Little Rexmas*
  sweatshirt and the *Christmas Arms Rex* mug. The hub links both directly, but anyone browsing the
  collection page (the hub's closing link) won't see them. The *Christmas Arms Rex* tee and the
  *T-Rex Winter Forest* mug are members, so it's a missed tag rather than a policy.
  **Fix (owner, collection membership — gated):** add both products to the collection.
- **The *Dino Christmas Party* toddler dress is $59.37.** The *Christmas Cookies* dress is the same
  blank (same description and size guide) at **$34.99**. $59.37 looks like a leftover
  cost-plus calculation. The hub links only the $34.99 dress. *(Pricing, gated.)*
- Both toddler dresses are sleeveless summer sundresses listed as Christmas wear. The hub
  suggests layering. If the print provider has a long-sleeve dress blank, it would suit December
  better. *(Merchandising, low.)*

## 35. Toddler range gaps: no toddler-size shoes or backpack, a wrong size guide, and one birthday shirt 🟡 MEDIUM — merchandising / product copy — added 2026-09-30

Found while checking inventory for the Day 10 `dinosaur gifts for 3 year olds` guide (live Shopify,
2026-09-30):

- **Kids' shoes start at 11 Child (EU 28).** Every one of the 27 ACTIVE kids' shoes has 11C as its
  smallest size, which is bigger than many three-year-olds wear. `dinosaur gifts for 3 year olds`
  (320/mo, $1.14 CPC) and `for 2 year olds` (90/mo) can't be sold a shoe. The article tells readers
  to check their child's size first and points shoes at four- and five-year-olds.
  **Fix (merchandising):** if the print provider offers toddler sizes (7T–10T), add them.
- **Backpacks are full-size.** 13 of 14 are 16⅞″ × 12¼″ with a 15″ laptop sleeve; only *Neon Rex*
  has a "Child (Ages 4 to 7)" size. A preschool-size backpack would serve the 3-year-old gift term
  and the back-to-school `dinosaur backpack` curve (Jul 22,200/mo). *(Merchandising.)*
- **Wrong size guide on *Cute Baby Dinosaurs – Girl Toddler Dinosaur Shirt*.** Its variants are
  2T–7, but its description shows the big-kid 8–20 size chart. A parent sizing a 3T from that
  chart gets the wrong numbers. The sibling *POW Dinosaur Shirt* has the correct 2T–7 chart.
  **Fix (owner, product copy — gated):** paste the 2T–7 chart.
- **Only one birthday product.** `dinosaur birthday shirt` is 390/mo, SD 28, flat all year
  (260–480), but *Happy Birthday – T-Rex* is the only ACTIVE product with "birthday" in its title.
  An "I'm 3 / Three-Rex"-style age-number range would serve this term, the by-age gift terms, and
  the `dinosaur-birthday-party` blog. *(Merchandising.)*

## 36. Pillow range: two identical collections, blank alt text, and square listings missing size and shipping info 🟡 MEDIUM — catalog / product copy — added 2026-10-01

Found while checking inventory for the Day 11 `dinosaur pillow` article (live Shopify, 2026-10-01):

- **`dinosaur-throw-pillow` and `dinosaur-pillows-cases` hold the same 11 products.** That's a
  fourth duplicate pair to add to #2. The articles link `dinosaur-throw-pillow` only.
  **Fix (owner, gated):** keep **`dinosaur-pillows-cases`**, which ranks **#14 for "dinosaur
  pillows" (1,300/mo)**, #5 for "dinosaur throw pillow" and #9 for "dinosaur accent pillow".
  Then 301 `dinosaur-throw-pillow` to it.
- **My miss, 2026-10-01: today's article links the duplicate, not the collection that ranks.**
  The pre-write cannibalisation check ran `page_keywords` on `/collections/dinosaur-throw-pillow`.
  It came back empty, but that URL is the duplicate that doesn't rank. The domain-level pull an
  hour later showed `/collections/dinosaur-pillows-cases` at #14. The new post and that
  collection now both target the term. A guide and a collection page usually serve different
  intents and can both rank, but the post should pass authority to the page that ranks, not to
  its duplicate. **Fix (owner, about 1 minute, gated because the post is live):** in
  `/blogs/blog/dinosaur-pillows`, change the 3 links from `/collections/dinosaur-throw-pillow` to
  `/collections/dinosaur-pillows-cases`. The repo copy will be updated to match once approved.
  Process fix (agent-side, done today): `docs/RESEARCH-PLAYBOOK.md` now requires a domain-level
  check (`domain_keywords` + tracked positions) for the exact term, not one guessed URL.
- **8 of 9 ACTIVE pillows have blank image alt text** (Jurassic Fuji is the exception, with a
  generic "Dinosaur Throw Pillow"). Image search is a real channel for a visual product like this,
  and blank alt text is also an accessibility gap. **Fix (owner, product copy, gated):** one line
  per image naming the dinosaur and shape, e.g. "Triceratops-shaped dinosaur pillow, 16 inch".
- **The three square pillows share one generic description** with no production or shipping time,
  where the shaped pillows give 2–5 + 4–13 business days. *American Pride T-Rex* is a single
  "Default Title" variant with no size stated anywhere. The article gives no delivery date for
  the square pillows and no size for American Pride, because neither is on the listing.
  **Fix (owner, product copy, gated):** add the size and the shipping block.
- **`catalog.json` had the split wrong:** it said 5 shaped and 4 square. The live count is 6
  shaped and 3 square. Corrected in the 2026-10-01 refresh.
- **A 7th shaped pillow is in DRAFT:** *Neon Dinos – Dinosaur Pillow* (`neon-dinos-dinosaur-pillow`),
  in no collection. If it's sellable, publishing it and adding it to the pillow collection costs
  nothing. *(Owner decision.)*

## 37. Monthly catalog refresh, 2026-10-01: drafts hiding behind demand 🟡 MEDIUM — merchandising — added 2026-10-01

From the full DRAFT/UNLISTED pass (109 DRAFT, 1 UNLISTED, 910 ACTIVE):

- **`dinosaur beanie` is 390/mo, SD 23 and tracked; `dinosaur-beanie` is empty (#1).** A beanie
  product exists, *Pastel Dinos – Dinosaur Beanie*, but it's DRAFT and in no collection.
  Publishing it into `dinosaur-beanie` would turn an empty collection (a liability) into a
  winter page. *(Owner decision.)*
- **Four more collections are storefront-empty because every product in them is DRAFT:**
  `on-sale` (4: dropship toys/socks), `personalized` (2 pillows), `dinosaur-earrings` (2), and
  `dinosaur-christmas-pajamas-1` (7, deliberate per #0). All four are now in
  `draft_heavy_do_not_link`, and the articles don't link them. Unpublishing the first three
  would stop them rendering as empty pages. *(Owner, gated.)*
- **22 live collections were missing from `catalog.json`.** They're now mapped under
  `unmapped_2026_10_01` with ACTIVE counts. Worth knowing: `dinosaur-leggings-plus-size` (15/15),
  `dinosaur-nuggie-clothing` (21/23), `america-dinosaurs` (16/17), `womens-dinosaur-sweatshirts` (6/6).
- **No total changed among the 73 mapped collections since 2026-08-30**, and the five empty
  collections in #1 are still empty. The catalog hasn't moved in a month, so the merchandising
  items in this file (#1, #14, #18, #21, #31, #35) are the bottleneck, not content.

---

## 38. Sock range: a stale 2020 sock post, two stray duplicate listings, a one-size "sized" sock, and missing shipping/size info 🟡 MEDIUM — catalog / product copy — added 2026-10-02

Found while reading all 36 `dinosaur-socks` listings for the Day 12 article.

- **`xray-sock` and `mashup-sock` look like stray duplicates.** Lowercase titles ("XRAY sock",
  "mashup sock"), $18.63 instead of $19.99, both ACTIVE and in the collection next to the real
  *X-Ray Dinosaur Dress Socks* and *Dinosaur Dress Socks - Mashup Dinosaurs*. Owner: confirm and
  DRAFT them, or retitle and reprice.
- **Space Dino's (`space-dinos-dinosaur-socks`) is listed in size M only**, though its copy says
  "3 different sizes". It is the sock page that ranks (#33 for "dinosaur socks"), so shoppers
  outside M land on it and bounce. Add S and L, or fix the copy.
- **Sized S/M/L listings give no shipping time** (Multi-Color Dinos, Space Dino's, Pink and
  Yellow Brontosaurus). The one-size listings do (4–5 + 2–5 or 2–5 + 3–6 business days).
  Multi-Color Dinos also has no size chart; only Pink and Yellow Brontosaurus has one.
- **Typo:** "Orange Stegasaurus Socks" (Stegosaurus).
- No kids' socks exist (smallest fit women's 5); `dinosaur socks for kids` shows 0 volume in
  Ubersuggest, so this is a note, not a merchandising ask.
- **The 2020 blog post `/blogs/blog/dinosaur-socks` is stale and holds the handle.** *The Best
  Dinosaur Socks Money Can Buy* ranks for nothing, says "we have dinosaur socks for kids… for
  toddlers" (we don't), and its kids section links `kids-dinosaur-socks-5-pack`, which no longer
  exists. Replacement copy is ready: `content/rescues/2026-10-02-dinosaur-socks-rewrite.md`.
  Owner: approve the in-place rewrite (or say yes and the next run does it via `articleUpdate`).

## 39. Sticker range: no wall decals for 2,900/mo of wall demand, a size guide offering a size that isn't sold, and generic handles 🟡 MEDIUM — merchandising / product copy — added 2026-10-03

Found while reading all 31 `dinosaur-stickers` listings for the Day 13 article.

- **Wall stickers are the biggest unserved sticker demand.** `dinosaur stickers wall` 1,600/mo,
  SD 27 and `dinosaur stickers for wall` 1,300/mo, SD 16 (Ubersuggest, locId 2840, 2026-10-03).
  Our largest sticker is 6″ square (or the 15″ × 3.75″ strip). The article says so plainly. If a
  print partner offers wall decals, this is a cheap category to add: Owner decision.
- **Dryptosaurus's size guide lists 15″ × 3.75″, but the listing only sells 3″/4″/5.5″.** Only
  Nipponosaurus River, Neon Bambiraptor and Synthwave Dinosaur actually offer the strip. The
  opaque-art range shares one description, so the other 7 single-size-set listings likely carry the
  same mismatch (verified on Dryptosaurus only). Either add the variant or trim the size guide.
- **Two descriptions, one headline.** Both ranges open "Vinyl Dinosaur Stickers", but only the
  original range claims waterproof. If the opaque range is waterproof too, saying so would help.
- **Typo:** "T-Rex Mendala - Sticker" (Mandala).
- **Generic handles:** Rex's First Snowman is `/products/square-stickers`, Target Rex is
  `/products/kiss-cut-stickers`, T-Rex Sunset is `/products/brown-dinosaur-sticker`, Raptor
  Watching is `/products/raptor-watching-1`. Renaming needs 301s, so low priority.
- **Two DRAFTs in the collection:** 80's Rex (looks finished, same variants as the live range) and
  a "Dinosaur Sticker Pack" with an imported marketplace-style handle. Publish 80's Rex if it was
  left in draft by accident.

## 40. Purse range: a stale "experiencing delays" banner, a size chart hosted off-site, and a kids' tag on adult bags 🟡 MEDIUM — product copy — added 2026-10-04

Found while reading all 24 `dinosaur-purses` listings for the Day 14 article.

- **The three canvas saddle bags** (Blue & Gold Dinos, Chalkboard Rex, Watercolor Plesiosaur) say
  "(Currently experiencing delays)" with 10–15 business days shipping, *and* "Estimated shipping
  time is 2–4 weeks" in the same description. If the delay is over, the banner is costing
  Christmas sales; if it isn't, the two estimates should agree. Blue & Gold Dinos is the page that
  ranks **#8 for `dinosaur purse`** (1,000/mo), so it's the one shoppers actually land on.
- **Their size chart is images only**, and one of the four is hot-linked from `i.postimg.cc`, a
  free third-party image host. If that host drops it, the chart disappears. Re-upload it to
  Shopify Files, and put the measurements in text so search engines (and the blog) can use them.
- **Tags:** 10 of the 19 faux leather crossbodies are tagged `Girls`, and Flower Power is titled
  "Cute Kids Dinosaur Purse", but it's the same 11″ × 8″ adult bag with a 14″ minimum strap drop.
  Fine as a teen bag; misleading for a young child. The article says so.
- **Brand demand we can't serve:** `dinosaur purse coach` 3,600/mo and `coach dinosaur purse`
  2,400/mo (locId 2840, 2026-10-04) are searches for another company's product. Logged so nobody
  writes for them.

## 41. Blanket range: a woven blanket with a typo, no size and no lead time; a hot-linked image on a hooded blanket 🟢 LOW — product copy — added 2026-10-05

Found while reading all 10 `dinosaur-blankets` listings for the Day 15 article.

- **Jurassic Painting woven blanket** ($75): the title says "Blaket" and the handle is
  `jurassic-painting-woven-dinosaur-blaket`. The listing gives **no dimensions and no make/ship
  time**, so the article can't give a Christmas order-by date for it and tells shoppers to check
  first. Fix the title (keep the handle, or add a 301 if it changes), and add size + lead time.
- **Hover Board hooded blanket:** the description's only size image is hot-linked from
  `i.postimg.cc` (same free host as the purse chart in #40). Its sizes (Youth 60″×45″, Adult
  80″×60″) and lead time ("3–7 days to tracking, 7–10 days shipping", business or calendar not
  stated) also differ from Dino Friends (80″×55″ / 60″×41″, 2–7 + 4 business days). Both are
  correct per their listings; the article states each separately. Worth putting the Hover Board
  text in the same format as the others, and saying "US only" if it is.
- **Inventory tracking:** both of these listings have tracking off (inventory 0, still
  purchasable). Not a problem, just noted so nobody reads "0" as sold out.
- The `hooded-dinosaur-blankets` collection is still empty (see #1). The two hooded products live
  in `dinosaur-blankets`; adding them there would give `hooded dinosaur blanket` (320/mo, Dec 720,
  SD 25) a real landing page.

## 42. Sweatshirt range: an unpublished duplicate sweatshirt post, a youth sweatshirt in no sweatshirt collection, a broken size-chart header, and Rexmas still outside Christmas 🟡 MEDIUM — blog / catalog — added 2026-10-06

Found while writing the Day 16 `dinosaur-sweatshirts` article.

- **Unpublished duplicate draft.** The `blog` blog holds *Dinosaur Sweatshirt: Your Complete Guide
  to Cozy Prehistoric Style* (`gid://shopify/Article/578687860886`, handle
  `dinosaur-sweatshirt-your-complete-guide-to-cozy-prehistoric-style`), created 2026-03-19, **never
  published**. Because it was never live, it ranks for nothing and didn't block today's post. But
  if anyone publishes it now, it splits `dinosaur sweatshirt` across two pages. It also claims
  things the store doesn't sell: embroidered and "minimalist" designs, scientifically accurate
  feathered dinosaurs, kids' sweatshirts in general, "consistent sizing" (the premium blank runs
  small). It has two duplicate footer paragraphs as well. **Recommend deleting it, or at least
  leaving it unpublished.** Owner's call; I haven't touched it.
- **The youth sweatshirt is in neither sweatshirt collection.** *9 Halloween Dinos - Youth Dinosaur
  Sweatshirt* (`youth-crewneck-sweatshirt`) is ACTIVE and only sits in the kids/boys/girls apparel
  collections. Shoppers browsing sweatshirts never see it. Its handle is also the generic
  `youth-crewneck-sweatshirt` (like `unisex-premium-sweatshirt` for Skeleton & Pumpkins).
- **The youth size chart is misaligned.** The headers read Length / Chest / Sleeve Length, but each
  row has four cells (size, then three numbers), so the size column has no header and every
  measurement sits under the wrong label. The article points shoppers to the chart without quoting
  it. Fix: add a "Size" header cell.
- **Men's and women's sweatshirt collections are identical** (same six unisex products). Fine for
  browsing, but both compete for `dinosaur sweatshirt`; neither is tracked. A single
  `dinosaur-sweatshirts` collection would be the natural landing page.
- **#34 still open:** Merry Little Rexmas is still not in `dinosaur-christmas` (checked 2026-10-06);
  T-Rex Winter Forest is. Two Christmas sweatshirts, and the Christmas collection shows one.
- `Dino Jungle - Dinosaur Sweatshirt` is DRAFT (not linked). If it's meant to sell, it's a 7th adult
  design waiting.

## 43. Backpack range: "Kids" titles on full-size bags, one listing with no shipping info, and missing image alt text 🟢 LOW — product copy — added 2026-10-07

Found while reading all 14 `dinosaur-backpack` listings for the Day 17 `dinosaur-backpacks` article
(live Shopify, 2026-10-07).

- **"Kids" in the name, adult-size bag.** Nine titles say "Kids Dinosaur Backpack" (one says
  "Girls"), but 13 of the 14 bags are the same 16⅞″ × 12¼″ × 3⅞″ full-size blank with a 15″ laptop
  sleeve. A parent of a five-year-old reads "Kids" as "child-sized". The article says plainly that
  only the Neon Rex comes in a child size. **Fix (owner, product copy — gated):** drop "Kids" from
  the titles or add a "full size, best for ages 8+" line to each description.
- **Typo:** *Jungle T-Rex - Kids DInosaur Backpack* (capital I).
- **Dinosaur Skeletons has no shipping block.** Its description is the raw print-provider copy
  (ends "Blank product components sourced from China") with no "Sold Exclusively" header and no
  lead time, unlike the other 13. The article tells readers to allow the longer window.
- **Neon Rex** says "Jurassi Backpacks" (typo) and gives no dimensions, fabric or laptop-sleeve
  detail for any of its three sizes. Worth adding the measurements per size.
- **Image alt text:** Colorful Fossils, Playful Dinosaur Doodles, Mixed Dinos and Dinosaur
  Skeletons have empty featured-image alt text; Construction Dinos' is "Product mockup". Small
  SEO/accessibility fix.
- **Rank note, not a fault:** `/collections/dinosaur-backpack` jumped 16 → #2 for `dinosaur
  backpacks` on the 10-07 pull, but sits #24 for the singular. If the owner ever edits the
  collection description, using the singular in its first line would be the cheapest rank gain
  available here (gated, collection copy).

## 44. Tote range: "every sticker" in the tote shipping text, no care or closure info, and an unexplained color option 🟢 LOW — product copy — added 2026-10-08

Found while reading all 48 `dinosaur-tote-bag` listings for the Day 18 `dinosaur-tote-bags` article
(live Shopify, 2026-10-08).

- **"We custom print every sticker."** The shipping block shared by the older polyester totes and the
  sized poly-cotton totes was copied from the sticker listings (seen on all six of those checked in
  full: Up Close, Last of the Dinosaurs, Tiny Dino, Realistic Raptor, Freedom Forever, Pink Retro
  T-Rex). The six newer totes say "every order". **Fix (owner, product copy — gated):** replace "sticker" with "order".
- **What does Black / Red / Yellow change?** 33 totes offer a Color option of Black, Red or Yellow,
  but no description says whether it's the handle, the trim or the bag. The article tells readers
  to check the photos. One line in the description would settle it.
- **No care instructions, closure or pocket info** on any tote. The FAQ answers "the listings don't
  say". A care line (and "open top, no inner pocket" if true) would remove the most common doubt.
- **Neon Rex tote** gives no size, unlike the four other poly-cotton totes; it also has no "Shipping
  Info" block, just the "2–4 days + 2–4 weeks" sentence.
- **Sized totes, same price at every size.** 13″, 16″ and 18″ are all $24.99. Possibly deliberate,
  but the 18″ is underpriced against the 13″ if blank costs differ. Owner's call.
- **Typo:** "Realistic Triceratops - DinosaurTote bag" (missing space; handle
  `realistic-triceratops-dinosaurtote-bag`). Three realistic titles use lower-case "bag".

## 45. Tie range: a `<style>` block that restyles the whole product page, no tie length, no image alt text 🟢 LOW — product copy / technical — added 2026-10-09

Found while reading all nine `dinosaur-ties` listings for the Day 19 `dinosaur-ties` article
(live Shopify, 2026-10-09).

- **Each of the 7 ACTIVE tie descriptions embeds a full HTML `<meta>` + `<style>` block** whose rules
  target `body`, `h2`–`h5`, `p` and `ul` (Arial font, white background, centered headings, 20px side
  margins). Inline in a product description, those rules apply to the *whole product page*, not just
  the description, so the tie pages can render in a different font and layout from the rest of the
  theme. **Fix (owner, product copy — gated):** delete the `<meta>` and `<style>` lines from the
  seven descriptions; the text and lists underneath don't need them. Worth checking other print-on-
  demand imports from the same period (Oct 2024 image timestamps) for the same block.
- **No length or width** on any tie. The article has to say "one size; the listing doesn't give a
  length". Ties are one of the few items where buyers ask (tall wearers, skinny-tie preference). One
  line per listing settles it.
- **No care instructions.** The article recommends spot-clean and hang dry as the cautious default.
- **Generic description copy:** all seven say "Whether it's a playful T-Rex, a sleek Velociraptor, or a
  dazzling fossil pattern", including Dino Nuggies, which is none of those. A one-line design
  description per tie would help both buyers and search.
- **Featured images have empty alt text** on all seven ties (same pattern as #43).
- **Two older ties are DRAFT** in the collection (Forest Dino Tie, Beige Dinosaur Tie, both $19.99 with
  the old "Est. 10 Business Days" shipping block), plus a DRAFT "Neck Ties" product outside it. Not
  linked. Owner's call whether to revive or delete; no action needed if deliberate.

## 46. Shirt cluster: tag-filter views rank instead of the real collections; no slippers for a 4,400/mo December term; a kids' header on the women's tanks 🟡 MEDIUM — SEO / merchandising / product copy — added 2026-10-10

Found while verifying the Day 20 target (`ladies dinosaur shirt`) and its fallbacks (live Shopify and
Ubersuggest, locId 2840, 2026-10-10).

- **The URLs Google ranks for our shirt terms are tag-filter views of `adult-dinosaur-shirt`, not the
  dedicated collections.** `/collections/adult-dinosaur-shirt/women's` is #11 for `ladies dinosaur shirt`
  (390/mo); `/collections/adult-dinosaur-shirt/men's` is #10 for `button up dinosaur shirt` (320/mo) and
  #8 for `funny dinosaur shirts` (170/mo). The dedicated `womens-shirts` collection (41 live) doesn't
  appear in the top 14 for its own head term. Tag views have no copy of their own, so they can't be
  rescued directly. **Proposal (owner, theme/collection — gated):** decide whether tag views should
  canonicalize to the matching dedicated collection (`/women's` → `womens-shirts`,
  `/men's` → `mens-dinosaur-t-shirts`) so the authority they've earned lands on a page we can write
  copy for. Until then, every shirt term in the queue hits the "our page already ranks" rule.
- **`dinosaur slippers` is 1,900/mo (Oct 2,900, Nov 3,600, Dec 4,400), SD 23, and we sell none.**
  Largest unserved Christmas term found this month. Merchandising note only; too late for this
  December unless a print-on-demand slipper can be listed within days.
- **`womens-shirts` includes items that aren't women's shirts:** *Dinosaur Nuggies – Men's T-shirt*,
  *Oviraptor* and other unisex adult shirts, and *Mamasaurus – Girl / Boy*. The unisex ones are
  reasonable; the "Men's" title in a women's collection isn't.
- **All women's tank top listings say "Dino-Mite Kids T-Shirt – Shipping Information"** above their
  shipping block (checked on Pastel Dinos). Copy-paste header; product copy fix (gated).
- **Women's relaxed tee listings have no size chart** (the unisex tees and the tanks do), and carry the
  same page-wide `<style>` block as the ties (#45).
