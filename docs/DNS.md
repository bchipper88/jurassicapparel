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
| Registration account | **Squarespace** | Migrated from Google Domains; all domains moved by 2024-07-10 |
| Authoritative nameservers | `ns-cloud-a1..a4.googledomains.com` | **Google Cloud DNS** — zone SOA hostmaster is `cloud-dns-hostmaster.google.com` |
| DNS zone editing | **Google Cloud Console** → Network Services → Cloud DNS | Where records are actually edited |
| Storefront | Shopify | A/AAAA at apex, CNAME on `www` |
| Business email | Zoho | `john@jurassicapparel.com` |

**Shopify is NOT the DNS host**, despite Shopify's admin panel claiming "Your store is using
Shopify's default nameservers." That panel reports Shopify's own configuration and does not
check the live registry delegation. Shopify holds an orphaned zone that nothing queries;
records added there will not take effect.

**Registrar and DNS host are different things and were conflated twice during this work:**
- **Squarespace** (registrar) — where you change *which* nameservers the domain uses
- **Google Cloud DNS** (DNS host) — where you edit the *records*

### Verification (2026-08-31), four independent sources

| Source | Result |
|---|---|
| `.com` registry via RDAP — the parent delegation | `NS-CLOUD-A1..A4.GOOGLEDOMAINS.COM` |
| Google public resolver | same |
| Cloudflare public resolver | same |
| Zone SOA | `ns-cloud-a1.googledomains.com` / `cloud-dns-hostmaster.google.com` |

RDAP is decisive — it reads the registry's own delegation rather than a resolver cache.
Registry records the nameservers were **last changed 2025-09-28**, i.e. moved off Shopify
about eleven months before this audit.

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
