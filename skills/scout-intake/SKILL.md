---
name: raid-intake
description: Use when research arrives as a chatbot dump, a pasted transcript, or someone else's summary rather than something you gathered. Grades it into recon.md and lexicon.md, and finds what the dump left out.
---

# raid-intake

Never fight where the money wins. This skill exists for the moment before that judgment can be made at all: when the only evidence anyone has is a wall of prose a chatbot produced, and nobody knows which parts of it are real.

## 1. What actually goes wrong

The obvious fear is invention. It is not the problem. Run this on a real dump and the links resolve, the quotes match, the dates drift by a day. The output is true.

**It is also unrepresentative, and that is the failure this skill exists to catch.** A chatbot answers the query string. It returns the reply that matched, not the post that mattered. It cannot see a view count, cannot tell a vendor from a buyer, and cannot tell you that the question you asked came back answered as a different question.

> **Your job is not detecting lies. It is detecting selection, context and standing.**

## 2. Audit the session before grading anything

Four checks on the dump as a whole. Each one catches something no per-quote check can see.

- **Question drift.** Does each answer address the question that was asked? Mark a question unanswered rather than filing its content under the wrong heading.
- **Seeded contamination.** Ask the operator once: *what did you tell this chatbot about your product before these questions?* Anything in the output matching that is their own words echoing back. Strike it from the demand evidence.
- **Format compliance.** Quotes and links, or summary only? A summary-only round is graded lower and labelled at the point of use, never in a footnote.
- **Source concentration.** Count distinct source posts, not quotes. Eleven quotes from three posts is three observations. Report both numbers.

## 3. Open every link, and record four things while it is open

X is a login wall, so `WebFetch` fails there; use the Playwright MCP browser on the operator's own session. Where no browser is available, every affected line stays `verified: no` with `reason: not checked`, and the run says so.

| Outcome | Grade |
|---|---|
| Opens, wording matches | `verified: yes` plus the date checked |
| Opens, wording differs or absent | `verified: no` — `reason: quote not found at source` |
| Will not resolve, or no browser | `verified: no` — `reason: not checked` |

**A failed fetch is never confirmation and never disproof.** Both invent a result the run did not produce.

Capture these while the page is already open, because a line without them misleads even when every word is right:

- `reach:` the view count. **No figure means the line is phrasing evidence only** and says so. Never counted as demand.
- `speaker:` buyer, builder or vendor, read off the account's own bio. **An account selling in the category is not market voice.**
- `position:` root or reply, plus the root's link.
- `gated:` yes where the post trades engagement for a deliverable. Its counts are manufactured.

A date off by one day is normal drift. Correct it and move on.

**Only `reach` graduates.** `speaker`, `position` and `gated` are working notes taken while the link is open, not pack fields — nothing in `lexicon.md` or `recon.md` has a place for them. They decide how a line is graded and classified: `speaker` sorts a quote into a pain or into the competitor pile, `position` tells you whether you are looking at the tail of a thread or the root, and `gated` marks a count as manufactured rather than earned. Once that judgment is made, all three are discarded, the same way the handle is discarded — **"The handle never enters the pack"** in section 9 covers them too. `position`'s root link is no exception: it exists to walk the thread in the next step, and once you've walked it, it goes with the rest.

## 4. Walk the thread

**The highest-yield step in this skill, and the one most easily skipped.** For every candidate from a threaded source, before grading:

- **Upward to the root.** The reply matched the query string; the parent is where the market is. Expect an order-of-magnitude difference in reach, sometimes several.
- **The author's own replies.** People qualify themselves in follow-ups. A quote used without them can state half a position as the whole of it.
- **The top replies to the root.** The densest source of pains, objections and vocabulary in the whole pipeline. Builders name their own products here, sceptics arrive unasked, the premise gets argued, and the ads show where money already is.

**A candidate whose thread has not been walked is not gradable.**

## 5. Go where the chatbot cannot

Free, no login, and per unit of effort this outperforms the dump itself.

| Source | What it settles |
|---|---|
| A code host's API | stars, forks, open issues, and **the last push date** |
| Its search API | the whole ecosystem ranked, in one call |
| A developer forum's search API | the most rigorous objections available anywhere |
| A community site, read in the browser | room measurement, where the JSON API refuses |
| **The vendor's own changelog** | kills or confirms "X just shipped Y" outright |
| **The artifact itself** | download it and count what is actually in it |

Two rules: **a competitor's price, features or shipping claims come from their own page, never a summary**; and **examine the artifact where you can get it**, because reading about a product gives its feature list while opening it gives the truth.

## 6. Qualify every competitor, because a name is not one

Five tests, each answerable at a source. Nothing enters `asymmetry.md` without them.

| Test | Fails when |
|---|---|
| Live? | every button routes to a waitlist |
| Free to try? | no trial, no free tier, not open source |
| Form | record it: hosted service, local install, or a repo to run |
| Core feature present? | it does the adjacent thing, not the thing |
| Real use? | see the metrics below |

**Anything failing the first test is recorded as not a competitor today, and its advertised prices are struck as anchors. Nobody has paid them.**

## 7. Four cheap metrics that overturn conclusions

- **Fork-to-star ratio.** A star is attention; a fork is intent to run. A project with sixty stars per fork went viral; one with four is being used. **Report the ratio wherever a star count is reported.**
- **Last push date.** Where it equals the creation date, the thing was abandoned on arrival. *Is anyone still shipping?* is a better question than *who has the most features?* and one call answers it.
- **Cross-post spread.** The same post in three rooms on the same day is a free A/B test of rooms. Read the vote counts.
- **Measure a room, never accept a described one.** Search the room for the topic and read what comes back. A busy room can be completely dead on your subject, and the room nobody named can carry it at thirty times the rate.

## 8. Write two files

`.monkeys/recon.md` keeps its existing contract exactly: `## Pains` and `## Rooms`, unchanged.

`.monkeys/lexicon.md` is this skill's own, and `assets/lexicon_lint.py` checks its form:

```markdown
# Lexicon — how this market talks, wants and refuses

## Vocabulary
- <the term, exactly as used> — heard in: <where> — verified: <yes, YYYY-MM-DD | no>

## Wants
- <what they want, in their words> — because: <the motive given> — verified: <yes, YYYY-MM-DD | no>

## Objections
- <what makes them refuse, in their words> — heard in: <where> — reach: <n|unknown> — verified: <yes, YYYY-MM-DD | no>

## Unanswered
- <a question asked in public that nobody answered> — asked in: <where> — reach: <n|unknown>

## Demand signals
- <the signal> — measure: <what was counted> — source: <where> — on: <YYYY-MM-DD> — verified: <yes, YYYY-MM-DD | no>
```

Run `python assets/lexicon_lint.py .monkeys/lexicon.md` before handing off. It checks that a line carries the fields a human needs; it cannot and does not judge whether anything is true.

**`## Objections` is why this file exists.** It is what positioning gets built against, and it is the question founders reliably forget to ask.

**`## Unanswered` is the rarest thing in the pack.** A question asked in public that nobody answered is a demand-shaped hole, and it is worth more than any stated want, because it names something a whole category has failed to supply.

## 9. Floors

**The handle never enters the pack.** Verify with the link, then discard it. `raid-recon` records the room, not the person, and the reason it gives binds here.

**A channel type is not a room.** No `## Rooms` line without an audience, a rule and an entry cost, all three read at the room itself.

**A vendor is not a buyer.** Their complaints about the market are positioning.

**Counter-evidence in the same thread travels with the quote.** Both go in, or neither is usable.

**An unsourced claim is barred, then chased.** "Studies have shown" cannot enter a draft. But barring it is step one: ask the operator for the source, then go and find it. **A barred claim is a research task, not a dead end.**

**A cross-domain citation is an analogy until proven otherwise.** Research about people is not evidence about software. Both can be true and sourced; never blur them into one claim.

**This skill never publishes.** RAID stages. A human sends.

## 10. What this doesn't decide

It grades the evidence and finds what the dump left out. It does not decide what to say about a competitor (`raid-asymmetry`), which room to enter (`raid-borrow`, `raid-stunt`), when (`raid-moment`), or what the copy says (`raid-draft`). Hand the files off.

The pastable questions are in `references/question-sheet.md`. A worked run on a poisoned dump is in `examples/raid-intake-worked-example.md`.
