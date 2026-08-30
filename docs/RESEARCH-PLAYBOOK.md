# Research Playbook — Ubersuggest

Project ID: `0e2631241f9cf7baf7365d47f86c68d8b505def60561bb15a58bbc2651875e39`
**Always pass `locId: 2840`.** Numbers from a global lookup are not comparable to
anything already in `KEYWORDS.md`.

## Daily — verify one keyword

```
keyword_overview(keyword: "<target>", locId: 2840)
```

Returns `search_volume`, `seo_difficulty`, `cpc`, `competition`, `search_intent`, and a
13-month `monthly_searches` series.

**Read the seasonality series every time.** It is the field that changes decisions most and
gets ignored most. `family dinosaur costume` averages 1,000/mo — and runs 90 in February,
5,400 in October. The average would have told you it was a mediocre target; the curve told
us to ship it in August.

### Difficulty thresholds at DA 17

| SD | Verdict |
|---|---|
| ≤ 30 | Winnable — write it |
| 31–40 | Stretch — only with a genuinely better page, or existing rank on the URL |
| > 40 | Skip, unless we have an unfair advantage (existing position, unique inventory) |

## Expanding a cluster

```
keyword_suggestions(keywords: ["<seed>"], locId: 2840)   # up to 3 seeds, flat list
match_keywords(...)                                       # when you need paging/sorting
```

Returns a lot. Pull it into a file and filter rather than reading it inline.

## Monthly — the opportunity scan

```
seo_opportunities(project_id: "<id>")
```

**This response is ~930k characters and will not fit in context.** It gets written to a
file. Filter with `jq`:

```bash
F=<path-the-tool-reports>

# Striking distance: we rank 8-40 on something big
jq -r '[.opportunities[] | select(.subtype=="existing_content") | .item
  | select(.position >= 8 and .position <= 40 and .volume >= 1500)]
  | unique_by(.keyword) | sort_by(-.volume) | .[:25]
  | .[] | "\(.volume) pos\(.position) sd\(.sd) | \(.keyword) -> \(.path)"' "$F"

# New content: real volume, winnable difficulty, no page yet
jq -r '[.opportunities[] | select(.subtype=="new_content") | .item
  | select(.volume >= 800 and .sd <= 35)]
  | unique_by(.keyword) | sort_by(-.volume) | .[:35]
  | .[] | "\(.volume) sd\(.sd) $\(.cpc) | \(.keyword)"' "$F"

# The site audit flags, with impact
jq -c '.opportunities[] | select(.type=="SITE_AUDIT") | {subtype, impact, effort}' "$F"
```

`unique_by(.keyword)` matters — the raw list repeats keywords across locations and will
make one opportunity look like six.

## Weekly — rank tracking

```
project_position_info(project_id: "<id>", startDate: "<today-30>", endDate: "<today>")
```

91 keywords tracked (limit 100). Reading the response:
- `done: true` means final. Don't re-poll expecting different data.
- `status: "ok"` with both positions `null` means **not ranking in the top 100** — that's
  a final answer, not a loading state.
- `status: "pending"` only happens on brand-new projects.

Append the result to `data/metrics.json` as a new dated entry. Never overwrite.

## Other tools worth knowing

| Tool | Use |
|---|---|
| `domain_overview` | Monthly traffic trend + top organic keywords |
| `domain_top_pages` | Which URLs actually earn traffic — the rescue shortlist starts here |
| `serp_analysis` | Who we're up against before committing to a hard term |
| `content_ideas` | What's earning shares/links on a topic |
| `google_suggestions` | Cheap long-tail expansion, no credit cost |
| `site_audit` / `site_audit_pages` | Technical issues, per-page |
| `article_title_suggestions` | Headline options once the target is locked |

## Recording standards

- Quote figures as returned, with the date of the pull.
- If a call fails, record `volume unavailable (<reason>, <date>)` and move on. Never
  substitute a guess. An honest gap is recoverable later; a fabricated number quietly
  corrupts every ranking decision built on top of it.
- Estimates get `est.` and a stated basis (usually a sibling keyword's real figure).
