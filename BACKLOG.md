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

**Action:** pause the flow (owner, 2026-08-31 — Klaviyo → Flows → set `RsULBu` to Draft).
Replacement designed: [`klaviyo/abandoned-cart-v2.md`](klaviyo/abandoned-cart-v2.md) — full
build spec with trigger, filters, timing, all three emails and a five-point relaunch gate.

Core fix is the trigger: `Checkout Started` instead of `Added to Cart`. Added to Cart fires
on any session touching the cart, including bots, and resolves to whatever profile it can —
which is the most likely source of the 38.65% bounce. Checkout Started only fires after a
human types an email into checkout.

Diagnosis is inferred from metrics, not read off the flow config. Confirm the current trigger
when opening the flow; if it already says Checkout Started, the fault is in the audience
filters and we should re-diagnose before rebuilding.

**Blocked on:** owner builds it in Klaviyo. The agent cannot — the Klaviyo MCP connection
dropped after the audit, and building flows would need approval regardless.

## K2. No authenticated sending domain 🟠 HIGH

`get_sending_domains` is empty — all mail goes out on Klaviyo's shared infrastructure with
no DKIM/SPF on `jurassicapparel.com`. Reputation is pooled with every other sender on that
shared resource, and Gmail shows a "via klaviyomail.com" line under the sender name.

**Setup:** Klaviyo → Settings → Domains → add a sending subdomain (`email.jurassicapparel.com`).
Klaviyo emits 3–4 CNAMEs; add them wherever the domain's DNS lives (likely Shopify admin →
Settings → Domains). Then add a DMARC TXT record at `_dmarc.jurassicapparel.com`, starting
at `p=none` to monitor before tightening.

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
