---
name: scout-geo
description: Use when checking whether an AI assistant finds and correctly describes the product, running a discoverability audit, or planning a weekly check of how the market's own tool (an AI chat assistant) answers a literal-ask query. Reads lexicon.md for the queries, runs them in a clean session, and writes .monkeys/discoverability.md.
---

# scout-geo

The market doesn't only search a search engine. Research behind this pack found people typing a plain, literal ask into an AI assistant: "does anyone know a tool that does X." This skill answers one question: when someone asks that, does the product show up, and does the assistant describe it right? Not whether it could, whether it does, checked today, in a session that has no reason to know the answer already.

## 1. What actually goes wrong

The failure that makes this skill worthless without noticing is running the check from a session that already knows the product: a logged-in account, a long-running chat that has this project's own docs pasted into it earlier, or an assistant that remembers a prior conversation. An answer from a session like that measures the operator's own influence on the assistant, not what a stranger asking cold would get. It will read as a pass. It is not a pass; it is a mirror.

## 2. Where the queries come from

Every query in this audit is a **literal-ask line**, taken from `lexicon.md`, never invented for the occasion. Two places in that file carry them:

- **`## Unanswered`**: a question asked in public that nobody answered. These are the closest thing to a recorded literal ask; the market already typed the words.
- **`## Vocabulary`**: a term heard exactly as the market uses it. Turn it into the plain question a buyer would actually type, keeping the market's own words, not marketing language.

A query invented from what sounds plausible is not a literal ask, it's a guess about how people talk. If `lexicon.md` doesn't have enough lines to draw from, that's a finding for `scout-intake` to fix, not a reason to write queries from imagination. `references/geo-checklist.md` has the full walk-through, including what to do when the file is thin.

## 3. Running the audit

For each query, open a fresh assistant session: no login, no project context pasted in, no prior turns about this product in that session. Ask the query exactly as written. Record what comes back before doing anything else with that session, including asking a follow-up that could nudge the answer.

**Quote how the assistant described the product verbatim.** Not a paraphrase, not "it named a competitor" without saying which. If it found the product but got the description wrong (the wrong category, the wrong price model, a feature it doesn't have), the verbatim quote is the only way a human reading the pack later can see exactly what's wrong and fix the source of that description.

**A `found: no` is the valuable finding, not a disappointing one.** It marks a demand-shaped hole: a real question the market asks, with nothing there to answer it. That's the gap `scout-geo` exists to surface. Recording it plainly, with the query and the date, is the whole point of running this skill.

**Never soften "not found" into "partially found."** There is no partial credit here. Either the assistant named this product in its answer, or it didn't. If it named a competitor, or invented something close but wrong, or answered with generic advice instead of a tool, that is `found: no`, described exactly as it happened in the `as:` field. Inventing a third state to make a run look less empty defeats the reason the field exists.

## 4. Write `.monkeys/discoverability.md`

`assets/geo_lint.py` checks this file's form: three required sections, each bullet's required fields, and that `found:` is `yes` or `no` and every `on:` is a real `YYYY-MM-DD` date.

```markdown
# Discoverability — can an AI find and describe the product

## Queries
- <a literal-ask query, taken from lexicon.md's literal-ask lines> — source: <lexicon.md, or where it was seen typed>

## Results
- <the query> — assistant: <which AI, clean session> — found: <yes|no> — as: <verbatim how it described the product, or what came up instead> — on: <YYYY-MM-DD>

## Fix
- <a discoverability gap to close> — because: <the result above that justifies it>
```

Run `python assets/geo_lint.py .monkeys/discoverability.md` before handing off. It checks that every bullet carries the fields a human needs to verify it; it cannot and does not judge whether the assistant's answer was actually checked in a clean session, or whether a fix is the right one. Form only, never truth, the same discipline `outcome_lint.py` holds.

## 5. Floors

**The clean-session rule binds every result in this file.** A result recorded from a session that wasn't clean isn't a lesser result, it doesn't belong in the file at all. If a clean session couldn't be run for a query, leave that query for next time rather than recording a compromised answer.

**Never invent a figure or a query.** Every query traces to a real line in `lexicon.md`. Every result is what an assistant actually said this run, quoted, not recalled from a prior audit or assumed to be unchanged.

**This skill never publishes.** It stages `discoverability.md` for a human, and for `RAID` to act on. It doesn't edit the site, doesn't post an answer anywhere the assistant might read it back, doesn't do anything but record what was found.

**The handle, and the permalink, never enter the pack.** Where a result touches a competitor's account or a specific person's post the assistant surfaced, capture what it proved and discard the identifying link, the same discipline `raid-intake` and `scout-outcome` hold.

## 6. What this doesn't decide

It measures whether the product is answerable today. It does not write the content that closes a gap (that's a human, or `RAID`, acting on the `Fix` line), does not touch the live site, and does not decide which gap to close first. Hand `discoverability.md` to whoever plans the next round.

A worked run, including a `found: no` that drives a `Fix` line, is in `../../examples/scout-geo-worked-example.md`.
