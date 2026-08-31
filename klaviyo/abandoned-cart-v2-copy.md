# Abandoned Cart v2 — email content (BUILT)

All three templates are built in Klaviyo and attached to draft flow `Vc6TWN`.
This file records what they say and why. Structure: [`abandoned-cart-v2.md`](abandoned-cart-v2.md).

| # | Library template | Attached copy | Message |
|---|---|---|---|
| 1 | `VGAs4Y` | `XLNAJb` | `WYwMth` |
| 2 | `Xkm4V3` | `SYwYEQ` | `QYe6jd` |
| 3 | `VR2sFX` | `T39eRH` | `Uz5Rkb` |

Klaviyo clones a library template into a message-owned copy on attach. Edit the **attached**
copy in the flow; the library version is the pristine source.

## Design

Hand-coded HTML, 600px, table-based, mobile media queries, bulletproof buttons, preheader
text, plain-text alternative, CAN-SPAM footer with the account's registered address, and
`{% unsubscribe %}` on every email.

Palette: `#202223` ink (the account's own stored brand colour), `#EFEBE4` paper, `#24402F`
deep green for buttons, `#C97B3F` amber reserved for the offer. The stored Klaviyo brand
palette is auto-generated greys with no real brand colour, so the green and amber are a
considered addition rather than something pulled from brand assets. The real brand logo is
used, from Klaviyo's stored asset.

## Cart block

Renders from the `Checkout Started` event — **no catalog sync required** (K10 is only needed
for recommendations):

```liquid
{% for item in event.extra.line_items %}
  {{ item.image_url }} · {{ item.title }} · {{ item.variant_title }}
  Qty {{ item.quantity }} · ${{ item.line_price|floatformat:2 }}
{% endfor %}
```
Button target: `{{ event.extra.checkout_url }}`

⚠️ **Verify these against a live event preview before going live.** Shopify payload shapes
vary by integration version, and a silently-empty product block is what produces a 0.2%
click rate — which is what the old flow does.

## Email 1 — 4 hours · no discount

**You left a dinosaur behind** / *Still in your cart, still waiting.*

Short. Cart, one button, and an offer to reply with questions. Most abandons are
interruptions, and a plain reminder converts them without costing margin.

## Email 2 — 24 hours · no discount

**Still thinking it over?** / *Sizing, how it is made, and what happens if it arrives wrong.*

Three objection blocks, all built on **verified** facts:

1. **Sizing runs 2XS–6XL** — confirmed against the Realistic Jurassic pajamas product.
2. **Everything is made to order** — from the live Shopify refund policy. Framed as the
   upside (nothing sells out) while stating plainly that it means all sales are final.
3. **Damaged or misprinted gets replaced or refunded within 30 days** — from the same policy,
   including "do not send it back to the manufacturer."

> **This corrects a real error.** The earlier draft of this file invented a returns line
> reading *"Send it back. We'd rather you have the right one."* Their actual policy is
> **all sales are final** because everything is made to order. That invented copy would have
> promised customers something the business does not offer. Always pull the policy.

**One placeholder remains, and it is deliberate:** an amber dashed box marked
**REPLACE OR DELETE THIS BOX BEFORE GOING LIVE** where shipping timing belongs. The Shopify
shipping policy body is **empty**, so there was no real delivery window to quote and none was
invented. It is styled to be impossible to miss.

## Email 3 — 72 hours · one offer

**Last call on your cart** / *Then we will stop bothering you.*

Explicitly the final email, which earns the right to ask once. Ends by releasing the
customer — no manufactured urgency.

**Placeholder:** the code renders as `COUPONCODE` with an amber box beneath explaining the
swap. A Klaviyo coupon backed by a matching Shopify discount is needed, then the dynamic tag
so each recipient gets a unique code — a static code leaks to coupon sites. The discount
percentage is a commercial decision, so none was set; the spec recommends **10% or below**,
since the old flow laddered 10/10/15 and taught repeat customers to abandon deliberately.

## The two remaining placeholders

Both are commercial or factual gaps only the owner can fill, both are visually unmissable,
and neither was papered over with invented text:

1. Email 2 — shipping/delivery window (Shopify shipping policy is empty)
2. Email 3 — coupon code and discount percentage
