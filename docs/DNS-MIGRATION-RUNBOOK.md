# Runbook — move DNS to Cloudflare

**Why:** Klaviyo's sending-domain setup requires **NS records** to delegate
`email.jurassicapparel.com`. Neither Shopify's nor Squarespace's DNS editor supports the NS
record type (both confirmed by inspection, 2026-08-31). Cloudflare does, it is free, and the
zone is only 8 records.

**Scope:** nameserver change only. **The domain registration stays at Squarespace.** This is
not a transfer; no auth code, no 60-day lock, no risk to ownership.

**Time:** ~20 minutes of work, plus propagation.
**Rollback:** set the nameservers back to `ns-cloud-a1..a4.googledomains.com` at Squarespace.
The Squarespace zone is not deleted by this, so rollback restores the previous state.

---

## ⚠️ The one thing that will break the store

Cloudflare defaults new A/AAAA/CNAME records to **proxied** — the orange cloud. **Every
record pointing at Shopify must be set to "DNS only" (grey cloud).**

Proxying a Shopify store through Cloudflare breaks Shopify's SSL provisioning and produces
redirect loops or certificate errors. Shopify terminates TLS itself and expects to see the
visitor directly.

Set to **DNS only**: the apex `A`, the apex `AAAA`, and `www`. MX and TXT records cannot be
proxied, so they take care of themselves.

---

## Step 1 — Pre-flight

Confirm the live zone still matches [`docs/DNS.md`](DNS.md) before starting:

```bash
for t in A AAAA MX TXT NS; do
  curl -s "https://dns.google/resolve?name=jurassicapparel.com&type=$t" \
    | python3 -c "import json,sys;[print('$t',a['data']) for a in json.load(sys.stdin).get('Answer',[])]"
done
curl -s "https://dns.google/resolve?name=www.jurassicapparel.com&type=CNAME" \
  | python3 -c "import json,sys;[print('CNAME',a['data']) for a in json.load(sys.stdin).get('Answer',[])]"
```

Also **screenshot the Squarespace DNS panel.** It is the authoritative list; the probe above
can only find records whose names were guessed.

## Step 2 — Add the domain to Cloudflare

1. Create a free Cloudflare account, **Add a site** → `jurassicapparel.com` → Free plan.
2. Cloudflare scans and auto-imports what it can find. **It will miss records it cannot
   guess** — the same limitation as the probe above.
3. Compare its import against the Squarespace panel and add anything missing by hand.

## Step 3 — Verify the record set inside Cloudflare *before* switching

Every row below must be present and correct. Do not proceed until it is.

| Type | Name | Value | Proxy |
|---|---|---|---|
| A | `@` | `23.227.38.68` | **DNS only** 🔴 |
| AAAA | `@` | `2620:127:f00f:8::` | **DNS only** 🔴 |
| CNAME | `www` | `shops.myshopify.com` | **DNS only** 🔴 |
| MX | `@` | `mx.zoho.com` priority 10 | n/a |
| MX | `@` | `mx2.zoho.com` priority 20 | n/a |
| MX | `@` | `mx3.zoho.com` priority 50 | n/a |
| TXT | `@` | `tiktok-developers-site-verification=TKihfodSHkVAIeTlEL9ePjcaupz2Uj2S` | n/a |
| TXT | `_dmarc` | `v=DMARC1; p=none` | n/a |

Plus the new Klaviyo records — add them now, so they go live with the switch:

| Type | Name | Value |
|---|---|---|
| NS | `email` | `ns1.klaviyo.com` |
| NS | `email` | `ns2.klaviyo.com` |
| NS | `email` | `ns3.klaviyo.com` |
| NS | `email` | `ns4.klaviyo.com` |
| TXT | `@` | `klaviyo-site-verification=XJSW3M` |

**Do not enable Cloudflare DNSSEC yet.** Turn it on only after everything resolves cleanly;
a DNSSEC mismatch during a nameserver change is painful to debug.

## Step 4 — Switch the nameservers at Squarespace

Cloudflare gives you two nameservers (e.g. `xxx.ns.cloudflare.com`, `yyy.ns.cloudflare.com`).

Squarespace → Domains → `jurassicapparel.com` → **Nameservers** → use custom nameservers →
replace all four `ns-cloud-*.googledomains.com` entries with Cloudflare's two → save.

Registry propagation is usually well under an hour but can take up to 48. During the window
some resolvers answer from Google and some from Cloudflare — which is harmless **as long as
both zones hold the same records**, which is why Step 3 comes first.

## Step 5 — Verify

```bash
# nameservers moved?
curl -s "https://dns.google/resolve?name=jurassicapparel.com&type=NS" \
  | python3 -c "import json,sys;[print(a['data']) for a in json.load(sys.stdin).get('Answer',[])]"

# store still resolving to Shopify?
curl -s "https://dns.google/resolve?name=jurassicapparel.com&type=A" \
  | python3 -c "import json,sys;[print(a['data']) for a in json.load(sys.stdin).get('Answer',[])]"

# mail still routed to Zoho?  (do not skip this one)
curl -s "https://dns.google/resolve?name=jurassicapparel.com&type=MX" \
  | python3 -c "import json,sys;[print(a['data']) for a in json.load(sys.stdin).get('Answer',[])]"

# Klaviyo delegation live?
curl -s "https://dns.google/resolve?name=email.jurassicapparel.com&type=NS" \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print([a['data'] for a in d.get('Answer',[])] or 'not delegated yet')"
```

Then by hand:
- [ ] `https://jurassicapparel.com` loads with a valid certificate
- [ ] `https://www.jurassicapparel.com` redirects correctly
- [ ] **Send a test email to `john@jurassicapparel.com` from an outside address and confirm
      it arrives.** Mail breakage is the highest-cost failure mode here and the easiest to
      miss, because nothing looks wrong until someone tells you they emailed you.
- [ ] Place a test order or at least reach checkout

## Step 6 — Klaviyo

Only once `email.jurassicapparel.com` returns Klaviyo's nameservers: go back to Klaviyo and
click **Verify**. Klaviyo then provisions DKIM/SPF underneath the delegated subdomain itself.

**Then stop.** Do not start sending on the new domain until K1 (the abandoned cart flow) is
fixed and the list is cleaned — a fresh sending domain starts at zero reputation and the
first sends define it. See K2's sequencing note.

## Step 7 — While you are in there

Three fixes for the Zoho mailbox, which currently sends with neither SPF nor DKIM:

1. **SPF** — get the exact `include:` from Zoho's admin console; it varies by datacenter.
2. **DKIM** — generate the selector in Zoho admin, publish the TXT it gives you.
3. **DMARC** — add `rua=mailto:<address>` so the reports go somewhere. Keep `p=none` for now.

Leave alignment unspecified so it stays relaxed. **Never set `adkim=s` or `aspf=s`** — strict
alignment breaks the `email.` subdomain delegation.
