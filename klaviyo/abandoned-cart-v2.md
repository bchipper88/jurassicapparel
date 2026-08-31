# Abandoned Cart v2 — build spec

**Status:** DRAFT — not built, not live
**Written:** 2026-08-31
**Replaces:** `Abandoned Cart Reminder (Email)`, flow ID `RsULBu` (paused 2026-08-31)
**Owner action required:** build in Klaviyo, then pass the relaunch gate at the bottom

---

## What we're fixing

The old flow, trailing 12 months:

| Metric | Old flow | Welcome Series | |
|---|---|---|---|
| Recipients | 6,187 | 1,475 | 77% of flow volume |
| Open rate | 5.2% | 32.4% | 6× gap, same subscriber base |
| Click rate | 0.20% | 1.52% | |
| Bounce rate | **12.77%** | 2.17% | 790 bounces |
| Revenue | $166.07 | $868.03 | 16% of revenue from 77% of sends |

One message (`SbKzEd`) bounced **695 of 1,798 sends — 38.65%** and drew the account's only
two spam complaints.

**Diagnosis.** A 38% bounce rate means the flow is emailing addresses that were never
validly collected. Combined with the 6× open-rate gap against a flow mailing overlapping
people, the most likely cause is that the trigger is **`Added to Cart`** rather than
**`Checkout Started`**.

That distinction is the whole problem. `Added to Cart` fires on any session that touches the
cart — bots, scrapers, price-checkers — and Klaviyo attaches it to whatever profile it can
resolve, including stale ones. `Checkout Started` only fires after a human has typed an email
address into checkout, which structurally guarantees a real, recently-confirmed address.

*This diagnosis is inferred from the metrics, not read off the flow config — confirm the
current trigger when you open the flow. If it already says Checkout Started, the problem is
in the audience filters instead and we should look again before rebuilding.*

---

## Flow configuration

### Trigger
**Metric: `Checkout Started`** (Shopify integration, metric ID `RWsZMn`)

### Trigger settings
- **Flow entry:** allow re-entry, max once per 30 days per profile
- **Smart Sending:** ON — skip anyone emailed in the last 16 hours
- **UTM tracking:** ON

### Flow filters — evaluated before every message
These are what stop the flow emailing people it shouldn't:

1. `Placed Order` **zero times since starting this flow** — the critical one. Stops mailing
   people who already bought. Its absence is likely part of why click rate was 0.20%.
2. `Checkout Started` **zero times in the last 30 minutes** — lets someone finish a checkout
   in progress without getting chased.
3. Profile is **subscribed to email marketing** (Klaviyo enforces, listed for completeness).

### Temporary reputation guard — first 30 days only
While sender reputation recovers from the old flow's 790 bounces, add one more filter:

4. `Opened Email` **at least once in the last 180 days**, OR profile created in the last
   30 days.

This keeps the relaunch on known-good addresses. **Remove it once bounce rate holds under 2%
for 30 days** — leaving it in permanently would suppress legitimate new customers.

### Timing

| Step | Delay | Cumulative |
|---|---|---|
| Email 1 | 4 hours after trigger | 4h |
| Email 2 | 20 hours after Email 1 | 24h |
| Email 3 | 48 hours after Email 2 | 72h |

4 hours on the first send avoids catching people who are still mid-session comparing options.
Worth A/B testing 1 hour against 4 once the flow is stable — some catalogs do better with the
faster nudge.

### Discount strategy

**Email 1: no discount. Email 2: no discount. Email 3: 10%, expires in 48 hours.**

The Welcome Series already carries a discount. Adding a second one at the cart trains people
to abandon on purpose, and it gives margin away to the majority who would have converted from
a plain reminder. Holding the incentive to the third message means only the genuinely
hesitant ever see it.

---

## Cart contents block

`Checkout Started` carries the line items on the event, so the cart renders **without**
needing the product catalog synced. (Catalog sync — backlog K10 — is required for
*recommendations*, not for showing someone their own cart.)

```liquid
{% for item in event.extra.line_items %}
  <img src="{{ item.image_url }}" width="120" alt="{{ item.title }}">
  <strong>{{ item.title }}</strong>
  {% if item.variant_title %}<br>{{ item.variant_title }}{% endif %}
  <br>Qty {{ item.quantity }} — ${{ item.line_price|floatformat:2 }}
{% endfor %}
```

Checkout link: `{{ event.extra.checkout_url }}`

**Verify these variable names against a live event preview in your account before building.**
Shopify's payload shape varies between integration versions, and a silently-empty product
block is exactly the kind of thing that produces a 0.20% click rate.

---

## Email 1 — 4 hours

**Subject:** You left a dinosaur behind
**Preview text:** Still in your cart, still waiting.

> Hi {{ first_name|default:"there" }},
>
> You were this close. Your cart's still sitting here, and nothing in it has wandered off yet.
>
> **[ CART CONTENTS BLOCK ]**
>
> **[ Finish checkout → ]**
>
> If something got in the way — a size question, a shipping question — just reply to this
> email. A real person reads it.

*No discount. No countdown. No pressure. Most people who abandon simply got interrupted, and
a plain reminder converts them without costing margin.*

---

## Email 2 — 24 hours

**Subject:** Still thinking it over?
**Preview text:** Sizing, shipping, returns — the answers, in one place.

> Hi {{ first_name|default:"there" }},
>
> Your cart's still here. If you're weighing it up, here's what usually comes up:
>
> **Sizing.** Our adult pieces run 2XS through 6XL — genuinely wide, so you don't have to
> settle for "close enough." Between sizes and planning to layer? Size up.
>
> **Shipping.** Orders ship in about two business days. If you're buying for a specific date,
> order about two weeks out and you're comfortable.
>
> **If it's not right.** Send it back. We'd rather you have the right one than keep something
> you don't wear.
>
> **[ CART CONTENTS BLOCK ]**
>
> **[ Finish checkout → ]**

*Objection handling, not persuasion. The three questions above are what actually stop apparel
purchases. Replace the shipping and returns specifics with your real policy before building —
I have written what is typical, not what is verified.*

---

## Email 3 — 72 hours

**Subject:** Last call — 10% off your cart
**Preview text:** Expires in 48 hours. Then we'll stop bothering you.

> Hi {{ first_name|default:"there" }},
>
> This is the last one — we're not going to keep emailing you about it.
>
> If the only thing standing between you and this cart is the price, here's 10% off. It's good
> for the next 48 hours.
>
> **{{ coupon_code }}**
>
> **[ CART CONTENTS BLOCK ]**
>
> **[ Apply the discount and check out → ]**
>
> And if it's just not the right time, no hard feelings. We'll be here.

*Use a Klaviyo-generated unique coupon code, not a static one — static codes leak to coupon
sites and get used by people who were never going to abandon anything.*

---

## Relaunch gate — do not set Live until all five pass

1. [ ] Trigger confirmed as **`Checkout Started`**, not `Added to Cart`
2. [ ] Flow filter `Placed Order zero times since starting this flow` is present
3. [ ] Preview against a real recent `Checkout Started` event — **the cart block renders
       actual products with images and prices.** An empty block here is the single most
       likely build error.
4. [ ] Temporary 180-day engagement filter in place for the first 30 days
5. [ ] Soft launch: set live, then **watch the first 72 hours.** Bounce rate must come in
       **under 2%.** If it doesn't, pause again — the address problem is upstream of this
       flow and rebuilding won't have fixed it.

## What good looks like

Old flow: 5.2% open, 0.20% click, 12.77% bounce, $0.031 revenue per recipient.

The Welcome Series on the same list does 32.4% open and $0.60 per recipient, which is the
realistic ceiling to aim at. A working abandoned cart flow typically outperforms a welcome
series on revenue per recipient, because the intent is higher — so if this lands anywhere
near $0.60, it is worth roughly **$3,700 a year** on the same 6,187 sends the old flow was
already making, against $166 today.

Treat that as an order-of-magnitude target, not a forecast. The honest floor is: anything
above $0.10 per recipient triples current performance.
