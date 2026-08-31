# DNS reference — jurassicapparel.com

**Snapshot taken:** 2026-08-31, via public DNS resolution.
**Purpose:** rollback reference and pre-migration inventory for the Klaviyo sending-domain
work (`BACKLOG.md` K2).

> DNS cannot be enumerated from outside — the records below were found by probing names I
> guessed. **The authoritative list is whatever the Squarespace DNS panel shows.** Treat this
> as a safety net, not a complete zone dump.

## Who controls what

| Layer | Where | Note |
|---|---|---|
| Registrar | Tucows Domains Inc. | Registered 2019-10-12, expires **2026-10-12** |
| DNS host / control plane | **Shopify** | Shopify admin → Settings → Domains → DNS settings |
| Nameservers | `ns-cloud-a1..a4.googledomains.com` | **Shopify runs its DNS service on Google Cloud DNS.** These *are* Shopify's default nameservers. |
| Storefront | Shopify | A/AAAA at apex, CNAME on `www` |
| Business email | Zoho | `john@jurassicapparel.com` |

**Shopify's DNS panel is live and authoritative — edit records there.**

Proven empirically 2026-08-31: a `klaviyo-site-verification` TXT added in Shopify's panel
resolved in both Google's and Cloudflare's public resolvers within minutes, and pre-existing
Shopify-panel records (`_provider=shopify`, `google=google-site-verification=...`) resolve
publicly too.

> **Correction, recorded so it is not repeated.** Earlier in this work the Google Cloud DNS
> nameservers and the SOA hostmaster `cloud-dns-hostmaster.google.com` were read as evidence
> that DNS lived in a customer-owned Google Cloud project, and that Shopify's zone was
> orphaned. That was wrong on both counts — it is Shopify's own Cloud DNS infrastructure.
> A resolver test against records only visible in the Shopify panel settles it; NS records
> and SOA hostmasters do not identify the control plane.

### The real constraint

Shopify is the DNS host **and** its editor exposes only A, AAAA, CNAME, MX, TXT and SRV —
**no NS type** (inspected 2026-08-31). Klaviyo's sending-domain setup delegates
`email.jurassicapparel.com` via four NS records, so it cannot be completed on Shopify DNS.

Options:
1. **Ask Klaviyo support whether the CNAME-based sending domain setup is still available.**
   Avoids touching DNS hosting entirely. Cheapest — try first.
2. **Move DNS to Cloudflare** per [`DNS-MIGRATION-RUNBOOK.md`](DNS-MIGRATION-RUNBOOK.md).
   Shopify's own domain settings has a **Change** button beside "Shopify's Nameservers",
   which is the switch. Registration stays where it is; only nameservers move.

## Current records (2026-08-31)

| Type | Name | Value |
|---|---|---|
| A | `@` | `23.227.38.68` (Shopify) |
| AAAA | `@` | `2620:127:f00f:8::` (Shopify) |
| CNAME | `www` | `shops.myshopify.com` |
| MX | `@` | `mx.zoho.com` (10) |
| MX | `@` | `mx2.zoho.com` (20) |
| MX | `@` | `mx3.zoho.com` (50) |
| TXT | `@` | `tiktok-developers-site-verification=TKihfodSHkVAIeTlEL9ePjcaupz2Uj2S` |
| TXT | `_dmarc` | `v=DMARC1; p=none` |
| NS | `@` | `ns-cloud-a1..a4.googledomains.com` |

**Not present:** SPF record, any DKIM selector (probed `zmail`, `zoho`, `google`, `selector1/2`,
`k1/k2`, `s1/s2`, `dkim`, `default`, `mail`, `klaviyo`, `shopify`, `shopifyemail` — all empty),
CAA record, and any delegation of `email.jurassicapparel.com`.

## To add for Klaviyo

| Type | Host | Value |
|---|---|---|
| NS | `email` | `ns1.klaviyo.com` |
| NS | `email` | `ns2.klaviyo.com` |
| NS | `email` | `ns3.klaviyo.com` |
| NS | `email` | `ns4.klaviyo.com` |
| TXT | `@` | `klaviyo-site-verification=XJSW3M` |

These four NS records delegate the whole `email` subdomain to Klaviyo, which then manages
DKIM and SPF underneath it. **This does not change the visible From address** — see K2.

**Add these in Google Cloud DNS**, which supports NS record sets natively. Neither Shopify's
nor Squarespace's DNS editor exposes an NS record type (both inspected by the owner,
2026-08-31), but neither is the live DNS host, so that limitation does not apply.

### Fallbacks, only if the Cloud DNS zone is inaccessible

1. **Ask Klaviyo support for the CNAME-based sending domain setup.** Historically offered as
   an alternative to NS delegation — confirm with support rather than assuming.
2. **Move DNS to Cloudflare.** See [`DNS-MIGRATION-RUNBOOK.md`](DNS-MIGRATION-RUNBOOK.md).
   Nameserver change only; registration stays at Squarespace.

## Unrelated fixes worth doing in the same session

Both concern the Zoho business mailbox, which is currently sending unauthenticated:

1. **Add an SPF record.** Get the exact `include:` from Zoho's admin console — it varies by
   datacenter (US / EU / IN), so do not assume `include:zoho.com`.
2. **Add DKIM for Zoho.** Generate the selector in Zoho's admin console and publish the TXT.
3. **Add `rua=mailto:<address>` to the DMARC record** so reports are actually received.
   Currently `p=none` with no reporting address means it monitors and tells nobody.

Leave DMARC alignment unspecified (defaults to relaxed). **Do not set `adkim=s` or `aspf=s`** —
strict alignment would break the `email.` subdomain approach.

## Re-checking this snapshot

```bash
for t in A AAAA MX TXT NS; do
  curl -s "https://dns.google/resolve?name=jurassicapparel.com&type=$t" \
    | python3 -c "import json,sys;[print('$t',a['data']) for a in json.load(sys.stdin).get('Answer',[])]"
done
curl -s "https://dns.google/resolve?name=email.jurassicapparel.com&type=NS" \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print([a['data'] for a in d.get('Answer',[])] or 'not delegated')"
```
