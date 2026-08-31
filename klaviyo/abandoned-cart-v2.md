---
status: BUILT AS DRAFT in Klaviyo — not live, no content yet
written: 2026-08-31
supersedes: the 2026-08-30 version of this file, whose core diagnosis was wrong
replaces: flow RsULBu "Abandoned Cart Reminder (Email)"
built_flow_id: Vc6TWN
built_at: 2026-08-31T00:54:32Z
---

## Built

Flow **`Vc6TWN`** — *[DRAFT] Abandoned Cart v2 - 3 emails / 3 days*
→ https://www.klaviyo.com/flow/Vc6TWN/edit

Created via API 2026-08-31, **status `draft`**, every action `draft`. It cannot send.

Verified in the create response:

| | |
|---|---|
| Trigger | `Checkout Started` (`RWsZMn`) |
| Profile filter | `Placed Order` = 0 since flow start (`YzLKy5`) **+** not in this flow in last 7 days |
| Re-entry | once per 7 days |
| Timing | 4h → +20h → +48h (72h total) |
| Smart Sending | **on, all three messages** |
| UTM tracking | on |
| Templates | **`null` on all three — no content yet** |

Message IDs: `WYwMth` (1 of 3), `QYe6jd` (2 of 3), `Uz5Rkb` (3 of 3).

### Still to do before it can go live

1. **Add email content.** All three messages have subject and preview text but no template.
   Copy is in [`abandoned-cart-v2-copy.md`](abandoned-cart-v2-copy.md). Left empty
   deliberately — reusing the old templates would have carried the 10/10/15 discount ladder
   into the new flow, where it could be published by accident.
2. **Replace the placeholder shipping and returns lines** in email 2 with the real policy.
3. **Add the temporary engagement guard** (opened in last 180 days OR profile created in
   last 30 days). Not built via API — the property name for profile creation date was
   uncertain and a wrong guess would have silently filtered everyone. Add it in the UI.
4. **Pause the old flow `RsULBu`.**
5. **Investigate the Shopify checkout junk traffic** — the 38.65% bounce. This flow does not
   fix it.
6. Then work the relaunch gate at the bottom of this file.

# Abandoned Cart v2 — build spec

## Correction first

The 2026-08-30 draft of this spec said the flow was probably triggering on **Added to Cart**
without a purchaser exclusion, and that fixing those two things was the whole job. **Both
claims were wrong.** They were inferred from performance metrics rather than read off the
flow, and the flow API says otherwise:

- Trigger is already **`Checkout Started`** (metric `RWsZMn`).
- The profile filter already includes **`Placed Order` count = 0 since flow start**
  (metric `YzLKy5`), plus a *not in this flow in the last 7 days* condition.
- Re-entry is already capped at once per 7 days.

The trigger and audience logic are correct. The problems are elsewhere, and they are real.

---

## What the flow actually does today

Reconstructed from the flow-actions graph:

```
Checkout Started
  └ 3 hours    → A/B test → Email #1  "You left some dinosaurs behind..."
  └ +2 days    → split    → Email #2  "Our dinosaurs are sad"
  └ +2 days    → split    → Email #3  "Here's 10% off your dinosaur apparel"
  └ +2 days    → split    → Email #4  "Don't let your discount go extinct"   (10% off)
  └ +2 days    → split    → Email #5  "24 Hours Only - 15% Off"
```

**Five emails across eight days.** Trailing 12 months:

| # | Message | Subject | Recipients | Open | Click | Bounce |
|---|---|---|---|---|---|---|
| 1 | `SbKzEd` | You left some dinosaurs behind... | 1,798 | 6.07% | 0.36% | **38.65%** |
| 2 | `VLBkFb` | Our dinosaurs are sad | 1,121 | 5.61% | 0.00% | 2.94% |
| 3 | `VLakmb` | Here's 10% off your dinosaur apparel | 1,099 | 4.84% | 0.28% | 2.18% |
| 4 | `T6fCUW` | Don't let your discount go extinct | 1,089 | 4.96% | 0.09% | 1.93% |
| 5 | `R7CeBT` | 24 Hours Only - 15% Off | 1,080 | 4.61% | 0.28% | 1.57% |

---

## The five real problems

### 1. Smart Sending is OFF on every message 🔴

`smart_sending_enabled: false` on all six messages. Smart Sending is the guard that stops
Klaviyo emailing someone who has already had a message in the last ~16 hours. With it off,
this flow can hit the same person five times in eight days *on top of* any campaign.

This is the single easiest fix in the account and it is one flag per message.

### 2. Five emails over eight days is far too long 🔴

Cart intent decays in hours, not a week. By email #4 — day six — the customer has bought
elsewhere or moved on. All that remains is the unsubscribe risk.

Emails 2–5 average **4.6–5.6% open and 0.0–0.3% click**. They are not persuading anyone;
they are just spending reputation. Note email #2 recorded **zero clicks in a year.**

### 3. The discount ladder trains abandonment 🔴

Email #3 offers 10%. Email #4 offers 10% again. Email #5 offers 15%.

Anyone who abandons twice learns the pattern: wait a week, get 15%. That is a permanent
margin leak, and it makes the Welcome Series discount worth less too.

### 4. The A/B test has never run 🟠

Action `68684583` is an A/B test created 2024-09-11 with two variations
(`SLewvn` "Variation A", `S9dtSK` "Variation B"). **Neither appears in the 12-month flow
report at all** — zero sends. Meanwhile the control `SbKzEd` took all 1,798. The test has
been sitting inert for two years.

### 5. The bounce problem is upstream, in Shopify — not in this flow 🔴

This is the important one, and the earlier spec got it backwards.

Email #1 bounces at **38.65%**. Emails #2–5 bounce at **1.6–2.9%**. That gradient is the
signature of a first send hitting a pool containing many invalid addresses, hard-bouncing
them, and Klaviyo suppressing them — so later messages only reach the survivors.

Since the trigger is `Checkout Started`, every one of those addresses was **typed into your
Shopify checkout**. A ~38% invalid rate at that step means junk is entering checkout: bot
traffic, scripted checkout attempts, or fake-address form abuse.

**No amount of Klaviyo configuration fixes this.** Rebuilding the flow will not stop it. It
needs investigating on the Shopify side — bot protection / captcha at checkout, and a look
at whether those checkouts share patterns (same IP ranges, disposable email domains,
zero-value carts).

---

## Proposed v2

### Keep unchanged
- Trigger: `Checkout Started` (`RWsZMn`)
- Profile filter: `Placed Order` = 0 since flow start (`YzLKy5`)
- Re-entry: once per 7 days

### Change

| Setting | Now | v2 |
|---|---|---|
| Message count | 5 | **3** |
| Duration | 8 days | **3 days** |
| First delay | 3 hours | 4 hours |
| Smart Sending | **off** | **on, every message** |
| Discounts | 10% / 10% / 15% across #3–5 | **one offer, final email only** |
| A/B test | inert, 2 years | remove |

### Sequence

| Step | Delay | Purpose | Discount |
|---|---|---|---|
| 1 | 4 hours | The reminder. Cart contents, one button. | none |
| 2 | +20 hours (24h) | Objection handling — sizing, shipping, returns. | none |
| 3 | +48 hours (72h) | Last call. | one offer, 48h expiry |

Copy for all three is in [`abandoned-cart-v2-copy.md`](abandoned-cart-v2-copy.md), carried
over from the previous draft — that part still stands, since it was never dependent on the
trigger diagnosis.

### Add during recovery only

While reputation recovers, add a profile filter: **has opened an email in the last 180 days
OR profile created in the last 30 days.** Remove it once bounce holds under 2% for 30 days.

This is a tourniquet, not a fix. The fix is #5 above.

---

## Relaunch gate

1. [ ] Shopify checkout bot/junk traffic investigated — the 38% bounce has a known cause
2. [ ] Smart Sending confirmed ON for all three messages
3. [ ] A/B test action removed
4. [ ] Preview against a real recent `Checkout Started` event — cart block renders products
5. [ ] Soft launch, watch 72 hours, **bounce must come in under 2%**

If bounce is still high after the rebuild, that confirms #5: the addresses are bad at
source and the flow is only the messenger.

## Expected value

Old flow: $166.07 from 6,187 sends — $0.031 per recipient.
Welcome Series on the same list: $0.60 per recipient.

Reaching even $0.10 per recipient triples current performance. Cutting from 5 sends to 3
also cuts volume ~40%, so the reputation cost falls even if revenue only holds flat.
