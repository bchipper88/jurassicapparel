# Why the daily Routine stalls on permissions

**Status as of 2026-08-31: the Routine fires but does not complete. This is a defect, not a
design choice.**

## What actually happened

Routine `trig_012cPKMi3SWxBwrokr5QMJvr` ("Jurassic Apparel — daily article", cron `0 11 * * *`)
fired on 2026-08-31 at 11:44 UTC / 7:44am EDT. It produced nothing:

- no `updates/2026-08-31.md`
- no `content/articles/2026-08-31-*.md`
- no commit on `claude/lehigh-valley-routines-keywords-hvzg9g`

It sat waiting for a human to approve its first tool call, and there was no human.

## The mechanism

Each firing spawns a **fresh session** — new container, empty repo, no conversation history.
Fresh sessions start in the **default permission mode**, which prompts before every Bash
command and every MCP tool call. The routine's very first action is `git clone`. That prompts.
Nobody is watching at 7am, so it hangs there until the container is reclaimed.

Being listed in the trigger's `allowed_tools` (`Bash`, `Read`, `Write`, `Edit`, …) means a tool
is *available*. It does not mean each call is *pre-approved*. Those are different gates.

## What is NOT the problem

An earlier note in `BACKLOG.md` (#7) claimed the Routine had no MCP connectors because it was
created through the API. **That was wrong.** Reading the trigger's `mcp_connections` shows both
are attached:

| Connector | URL |
|---|---|
| Ubersuggest | `https://ubersuggest-mcp.neilpatelapi.com/mcp` |
| Shopify | `https://setup.shopify.com/mcp` |

Klaviyo is not attached, but the daily article routine does not need it.

## The other defect found while checking: wrong outcome branch

The trigger's session context carries:

```
outcomes[0].git_repository.git_info.branches = ["claude/wizardly-clarke"]
```

That is an auto-generated branch name, not ours. The prompt tells the session to work on
`claude/lehigh-valley-routines-keywords-hvzg9g`. Even once permissions are fixed, work may land
on the wrong branch — which is why no `claude/wizardly-clarke` exists on the remote either
(the run never got far enough to push anything).

## Fix, part 1 — permission mode (owner action, claude.ai Routines UI)

The permission mode is set when the session is created and is not exposed by the API call that
created this trigger. It has to be set in the UI:

1. claude.ai → Routines → **Jurassic Apparel — daily article**
2. Set the permission mode so the session does not block on approval prompts
3. Set the outcome branch to `claude/lehigh-valley-routines-keywords-hvzg9g`

## Fix, part 2 — scoped allowlist (owner action, one file)

A repo-level `.claude/settings.json` narrows what an unattended session may do without asking.
The Routine clones this repo, so project settings apply to it.

**The agent is blocked from writing this file itself** — Claude Code's auto-mode classifier
refuses to let an agent author its own permissions file. That guardrail is correct and should
not be worked around. Create it by hand at `.claude/settings.json`:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Write",
      "Edit",

      "Bash(git *)",
      "Bash(git *:*)",

      "Bash(python3 scripts/check-links.py *)",
      "Bash(python3 scripts/md-to-shopify.py *)",
      "Bash(python3 scripts/check-links.py:*)",
      "Bash(python3 scripts/md-to-shopify.py:*)",

      "Bash(cat *)",
      "Bash(ls *)",
      "Bash(head *)",
      "Bash(tail *)",
      "Bash(grep *)",
      "Bash(rg *)",
      "Bash(find *)",
      "Bash(wc *)",
      "Bash(diff *)",
      "Bash(jq *)",
      "Bash(sed *)",
      "Bash(mkdir *)",
      "Bash(date *)",
      "Bash(echo *)",
      "Bash(pwd)",

      "mcp__Ubersuggest__keyword_overview",
      "mcp__Ubersuggest__keyword_metrics",
      "mcp__Ubersuggest__keyword_suggestions",
      "mcp__Ubersuggest__google_suggestions",
      "mcp__Ubersuggest__match_keywords",
      "mcp__Ubersuggest__serp_analysis",
      "mcp__Ubersuggest__estimate_serp_clicks",
      "mcp__Ubersuggest__seo_opportunities",
      "mcp__Ubersuggest__domain_overview",
      "mcp__Ubersuggest__domain_keywords",
      "mcp__Ubersuggest__domain_top_pages",
      "mcp__Ubersuggest__page_keywords",
      "mcp__Ubersuggest__page_overview",
      "mcp__Ubersuggest__content_ideas",
      "mcp__Ubersuggest__competitors",
      "mcp__Ubersuggest__list_projects",
      "mcp__Ubersuggest__get_project",
      "mcp__Ubersuggest__project_position_info",
      "mcp__Ubersuggest__backlinks_overview",
      "mcp__Ubersuggest__traffic_value",

      "mcp__Shopify__graphql_query",
      "mcp__Shopify__graphql_schema",
      "mcp__Shopify__search_products",
      "mcp__Shopify__search_collections",
      "mcp__Shopify__get-product",
      "mcp__Shopify__get-collection",
      "mcp__Shopify__get-inventory-levels",
      "mcp__Shopify__get-shop-info",
      "mcp__Shopify__search_docs_chunks"
    ],

    "ask": [
      "mcp__Shopify__graphql_mutation",
      "mcp__Shopify__create-product",
      "mcp__Shopify__update-product",
      "mcp__Shopify__create-collection",
      "mcp__Shopify__update-collection",
      "mcp__Shopify__add-to-collection",
      "mcp__Shopify__create-discount",
      "mcp__Klaviyo__create_flow",
      "mcp__Klaviyo__update_flow",
      "mcp__Klaviyo__update_flow_action",
      "mcp__Klaviyo__create_email_template",
      "mcp__Klaviyo__update_email_template",
      "mcp__Klaviyo__create_campaign",
      "mcp__Klaviyo__update_campaign"
    ],

    "deny": [
      "Bash(rm -rf *)",
      "mcp__Shopify__bulk-update-product-status",
      "mcp__Shopify__set-inventory",
      "mcp__Shopify__switch-shop",
      "mcp__Klaviyo__send_campaign",
      "mcp__Klaviyo__delete_flow",
      "mcp__Klaviyo__delete_email_template",
      "mcp__Klaviyo__bulk_import_profiles",
      "mcp__Klaviyo__bulk_suppress_profiles",
      "mcp__Klaviyo__bulk_unsuppress_profiles",
      "mcp__Klaviyo__request_profile_deletion"
    ]
  }
}
```

### Why it is shaped this way

- **`Bash(python3 *)` is deliberately absent.** Unrestricted Python is arbitrary code
  execution — it would route around every other rule in the file. Only the two scripts the
  routine actually runs are allowed.
- **`ask` encodes the charter.** Every gated surface — product copy, collections, theme,
  discounts, live Klaviyo flows — is listed so it stops even when nobody remembers the rule.
- **`deny` beats everything, including a permissive session mode.** Campaign sends, bulk
  profile operations and inventory writes cannot fire by accident.

## The publishing gap this leaves

`CLAUDE.md` step 5 publishes via `articleCreate`, which is
`mcp__Shopify__graphql_mutation`. That tool name covers *every* Shopify mutation — product
edits, collection changes, theme changes. Permission rules match on tool name and cannot be
scoped to a single mutation, so allowlisting it would open all of them.

It is therefore in `ask`, not `allow`. **Consequence: the unattended routine can research,
write, link-check and commit an article, but the live publish will still wait for approval.**

Two honest options:

1. **Accept the gap.** The routine drafts and commits daily; the owner approves the publish.
   Loses same-day publishing on days the owner is unavailable.
2. **Move publishing out of the MCP path.** A script using a scoped Shopify Admin token with
   write access to blog articles only, invoked as `Bash(python3 scripts/publish-article.py *)`.
   Narrower than allowlisting `graphql_mutation`, and restores same-day publishing.

Option 2 is the better end state. It is not built yet.

## Until both fixes land

The daily routine does not run unattended. `CLAUDE.md` describes the intended job; it is not
yet what happens at 7am.
