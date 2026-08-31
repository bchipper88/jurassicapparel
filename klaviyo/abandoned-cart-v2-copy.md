# Abandoned Cart v2 — email content (BUILT on the store's own design)

Attached to draft flow `Vc6TWN`. Structure: [`abandoned-cart-v2.md`](abandoned-cart-v2.md).

| # | Source design | Clone | Attached | Message |
|---|---|---|---|---|
| 1 | `RyJx3A` (orig. Email #1) | `SCtH98` | `SWKuvf` | `WYwMth` |
| 2 | `WemSB2` (orig. Email #2) | `TaRvqm` | `SCet7F` | `QYe6jd` |
| 3 | `SU488n` (orig. Final) | `X4dhEn` | `Yi28Sb` | `Uz5Rkb` |

All `SYSTEM_DRAGGABLE` — editable in Klaviyo's visual editor.

## Why these are clones of the originals

A first attempt built three hand-coded `CODE` templates from scratch. That was wrong on
three counts, and the originals were never even opened before replacing them:

1. **The Liquid was broken.** The rebuild used `{{ item.image_url }}`, `{{ item.title }}`,
   `{{ item.line_price }}`. Klaviyo's Shopify cart syntax — which the originals use
   correctly — is `{{ item.product.images.0.src|missing_product_image }}`,
   `{{ item.product.title }}`, `{% currency_format item.line_price %}`. The rebuilt emails
   would have rendered **empty product blocks**: exactly the failure being warned about.
2. **No empty-cart guard.** The originals wrap the loop in `{% if event.extra.line_items %}`.
3. **`CODE` templates are not editable in the drag-and-drop editor.** Swapping
   `SYSTEM_DRAGGABLE` for `CODE` would have removed the owner's ability to edit their own
   emails without touching HTML.

The originals also carry a branded header, a Men's/Women's/Boys/Girls nav bar, a full-width
hero image, Facebook and Instagram links, and full Outlook/MSO compatibility — none of which
the rebuild had.

**Lesson recorded: look at the asset before deciding it needs replacing.** Poor flow
performance was structural (five emails, Smart Sending off, bad addresses). It was not
evidence the design was bad, and it was never evidence about the design at all.

## Unverified claims that were written and removed

Both were invented, and both are false against the store's own data:

- *"Our adult pieces go from 2XS all the way to 6XL."* Checked on **one** product (Realistic
  Jurassic pajamas, genuinely 2XS–6XL) and generalised to the whole range. A sample of twelve
  active adult products runs **S–XL or S–2XL**, a couple to 3XL. **None reach 6XL.**
- *"which is why sizes never sell out."* Invented. Contradicted by zero-inventory products
  across the catalog.
- *"A real person reads it."* A promise about customer service with no basis. Needs the
  owner's confirmation before it appears anywhere.

Also corrected earlier: an invented *"send it back"* returns line. The real policy is
made-to-order, **all sales final**, with replacement or refund for damaged or misprinted
items within 30 days.

## Copy edits still to make, in the visual editor

**Email 1** — original copy ("Thanks for stomping by!") is fine as-is. No discount. Ready.

**Email 2** — currently the original "Our dinosaurs are sad" copy, which recorded **zero
clicks in twelve months**. Replace with objection handling built only on verified facts:
made-to-order (so nothing sells out of stock), all sales final, damaged/misprinted replaced
or refunded within 30 days. **Do not restate a size range** — it varies by product. Leave
shipping timing out entirely, or add the real window; the Shopify shipping policy body is
empty so there is no verified figure.

**Email 3** — currently the original 15%-off design. **Lower 15% to 10% or below.** The old
flow laddered 10/10/15 across three emails, which teaches repeat customers to abandon
deliberately. Use a Klaviyo coupon backed by a Shopify discount so codes are unique per
recipient; a static code leaks to coupon sites.

## Superseded templates, safe to delete

The abandoned hand-coded attempt: `VGAs4Y`, `Xkm4V3`, `VR2sFX` (library) and `XLNAJb`,
`SYwYEQ`, `T39eRH` (message copies). Not referenced by any flow.
