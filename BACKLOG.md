# Backlog — non-content work

Everything here needs **owner sign-off** (per `CEO-CHARTER.md`). The agent finds, verifies,
scopes and proposes. The owner executes or approves.

Ordered by value ÷ effort. Discovered 2026-08-30 unless noted.

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
   Scheduled into the 2026-10-01 monthly routine.
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
