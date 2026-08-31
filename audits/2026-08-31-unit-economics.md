# Are we actually making money? — 12-month P&L reconstruction

**Date:** 2026-08-31
**Period:** 2026-09-01 … 2026-08-31 (trailing 12 months)
**Source:** Shopify ShopifyQL `sales` table; `orders.transactions.fees` (36-order sample, Jul–Aug 2026)

## Short answer

**Probably yes, but modestly — and I cannot prove it from the store's own data.**

Two of the four cost lines are not in Shopify at all. Depending on where they land, the year
was somewhere between roughly **break-even and about $5,400 profit**. That is a wide band, and
it is wide because of a recordkeeping gap, not because the business is unknowable.

## What is solid

Pulled directly, not estimated:

| Line | Amount |
|---|---:|
| Gross sales | $17,195.30 |
| Discounts | −$730.37 |
| Returns | −$1,524.71 |
| **Net sales** | **$14,940.22** |
| Taxes | $63.82 |
| **Total sales** (incl. shipping charged) | **$15,874.66** |
| Orders | 306 |
| AOV | $51.88 |
| Revenue / month | $1,322.89 |

**Payment processing: 3.79% effective.** Not the headline 2.9% + 30¢. Measured across 36 recent
orders: $86.41 of fees on $2,279.51 captured. The gap is international cards (3.49% + 49¢,
3.5%, 3.9%) plus currency-conversion surcharges (1.5–3% on top). One order, `#JA2074`, paid
4.99% + 3%. Projected across the year: **≈$602**.

**Shopify Basic:** $348/yr on annual billing, $468/yr monthly.

Subtotal of what is knowable: **$15,874.66 − $602 − $348 = $14,924.89 left to cover COGS and
apps.** That is **$48.77 per order**.

## What is missing, and why

### 1. COGS — not recorded anywhere in Shopify

**Every single product variant has `inventoryItem.unitCost = null`.** Checked 100+ variants
across sneakers, stickers, mugs, blankets and dog beds. Not one has a cost.

This is print-on-demand, so the real cost sits on the supplier's invoice — Printful, Printify,
Pillow Profits, teelaunch and the rest bill the card directly and none of it flows back into
Shopify. Consequence: Shopify's own profit reports are blank, and no dashboard in the stack can
answer "did we make money" without this.

### 2. App subscriptions — not readable through the API

**30 apps are installed.** Shopify's `AppSubscription` object is scoped to the querying app, so
an outside integration cannot read what the others charge. This has to come from
**Settings → Billing** in the admin.

Nine are print-on-demand fulfillment apps:

> Printful · Printify · Subliminator · Gooten · JetPrint · AOP+ · Pillow Profits ·
> teelaunch · DSers-AliExpress

The rest, excluding Shopify's own free ones (Messaging, Translate & Adapt, Search & Discovery,
Fraud Control, Flow, Command Center, Claude Connector):

> SB: FAQ | HelpCenter · Upsell.com (ex ReConvert) · Klaviyo · Judge.me Importer ·
> Tabs Studio · Plug in SEO · Theme Updater & Backups · Make · Section Star ·
> CWILL Popup Email · Hextom Bulk Product Edit · Zigpoll · Essential Free Shipping · Cart Lock

Several of those carry monthly fees. At $1,323/month of revenue, **every $130/month of app
spend is 10% of the top line.**

## The scenarios

POD cost of goods typically runs 45–65% of retail. App spend is the other axis.

| COGS | apps $75/mo | $150/mo | $225/mo | $300/mo |
|---:|---:|---:|---:|---:|
| **45%** | $6,287 | $5,387 | $4,487 | $3,587 |
| **50%** | $5,427 | $4,527 | $3,627 | $2,727 |
| **55%** | $4,567 | $3,667 | $2,767 | $1,867 |
| **60%** | $3,708 | $2,808 | $1,908 | $1,008 |
| **65%** | $2,848 | $1,948 | $1,048 | **$148** |

Annual profit after COGS, apps, Shopify and payment fees. Excludes ad spend (none known) and
any labour.

**The business does not go negative anywhere in a plausible range.** Even the worst corner —
65% COGS and $300/month of apps — lands at roughly break-even. That is the genuinely reassuring
finding.

### Break-even app spend

| If COGS is… | apps must stay under |
|---|---|
| 45% | $599/mo |
| 50% | $527/mo |
| 55% | $456/mo |
| 60% | $384/mo |
| 65% | $312/mo |

There is real headroom. The store is not on a knife edge.

### Per-order

| | |
|---|---:|
| AOV | $51.88 |
| less payment fee | −$1.97 |
| less COGS @ 55% | −$30.91 |
| **Contribution** | **$19.00** |

Every $100/month of fixed cost eats **$3.92** of that $19.00.

## Two things worth fixing

### Returns are 8.9% of gross — $1,524.71

High, and on print-on-demand it is a total loss: the supplier was paid, the item shipped, the
customer refunded, and a made-to-order product cannot be resold. Roughly **$840 of goods cost
destroyed** on top of the refunded revenue.

The published policy is made-to-order, ALL SALES FINAL, with replacement only for damage or
misprint. A 8.9% return rate against that policy means either the policy is not being enforced,
or a real quality/sizing problem is generating genuine damage claims. Worth reading the actual
refund reasons — it is the single largest recoverable leak visible in the data.

### The shipping policy page is empty

Flagged in the Klaviyo audit and still open. On a store where fulfilment takes days and comes
from many suppliers, a blank shipping page drives both support load and returns.

## The fix that makes this answerable permanently

Set `unitCost` on the variants. Shopify then reports gross profit natively, every order,
forever — and this reconstruction never has to be done again.

The catch: nine POD suppliers means nine different cost sheets, and cost varies by size and
placement. Doing it properly is a real afternoon. Doing the top 20 sellers is maybe an hour and
gets most of the value, since the tail contributes little.

Logged as **BACKLOG #9**.

## Honest limits of this analysis

- Payment-fee rate is extrapolated from 36 orders in Jul–Aug 2026. If the international mix
  shifted during the year, the $602 moves.
- App costs are entirely unknown. The table brackets them; it does not measure them.
- COGS is entirely unknown. Same.
- No advertising spend is included, because none is visible. If any exists, subtract it.
- No value is assigned to the owner's time.
