# Abandoned Cart v2 — email copy

Companion to [`abandoned-cart-v2.md`](abandoned-cart-v2.md). Three emails over three days.
House voice: warm, specific, plainspoken. No fake urgency, no discount until the last one.

## Cart contents block

`Checkout Started` carries line items on the event, so the cart renders **without** the
product catalog being synced. (Catalog sync — backlog K10 — is needed for *recommendations*,
not for showing someone their own cart.)

```liquid
{% for item in event.extra.line_items %}
  <img src="{{ item.image_url }}" width="120" alt="{{ item.title }}">
  <strong>{{ item.title }}</strong>
  {% if item.variant_title %}<br>{{ item.variant_title }}{% endif %}
  <br>Qty {{ item.quantity }} — ${{ item.line_price|floatformat:2 }}
{% endfor %}
```

Checkout link: `{{ event.extra.checkout_url }}`

**Verify these variable names against a live event preview before building.** Shopify's
payload shape varies between integration versions, and a silently-empty product block is
exactly what produces a 0.2% click rate — which is what the current flow does.

---

## Email 1 — 4 hours

**Subject:** You left a dinosaur behind
**Preview:** Still in your cart, still waiting.

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

*No discount, no countdown. Most people who abandon simply got interrupted, and a plain
reminder converts them without costing margin.*

---

## Email 2 — 24 hours

**Subject:** Still thinking it over?
**Preview:** Sizing, shipping, returns — the answers, in one place.

> Hi {{ first_name|default:"there" }},
>
> Your cart's still here. If you're weighing it up, here's what usually comes up:
>
> **Sizing.** Our adult pieces run 2XS through 6XL — genuinely wide, so you don't have to
> settle for "close enough." Between sizes and planning to layer? Size up.
>
> **Shipping.** [REPLACE WITH REAL POLICY — see note below]
>
> **If it's not right.** [REPLACE WITH REAL RETURNS POLICY]
>
> **[ CART CONTENTS BLOCK ]**
>
> **[ Finish checkout → ]**

⚠️ **The shipping and returns lines are placeholders.** Swap in the store's actual policy
before building. Do not ship invented policy text.

*This replaces the current email #2 ("Our dinosaurs are sad"), which recorded **zero clicks
in twelve months**. Objection handling beats personification.*

---

## Email 3 — 72 hours

**Subject:** Last call on your cart
**Preview:** Then we'll stop bothering you.

> Hi {{ first_name|default:"there" }},
>
> This is the last one — we're not going to keep emailing you about it.
>
> If the only thing standing between you and this cart is the price, here's [X]% off. Good
> for the next 48 hours.
>
> **{{ coupon_code }}**
>
> **[ CART CONTENTS BLOCK ]**
>
> **[ Apply the discount and check out → ]**
>
> And if it's just not the right time, no hard feelings. We'll be here.

**Set the discount at or below 10%.** The current flow ladders 10% → 10% → 15%, which
teaches repeat customers to abandon on purpose. One offer, once, at the end.

**Use a Klaviyo-generated unique coupon code, not a static one.** Static codes leak to
coupon sites and get redeemed by people who never abandoned anything.
