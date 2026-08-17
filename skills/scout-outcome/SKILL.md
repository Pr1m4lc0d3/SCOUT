---
name: scout-outcome
description: Use when reviewing what a campaign or move actually did, closing out a retro, or deciding what to stop doing. Reads real captured analytics, grades the result into what moved, what stayed flat, and what to prune, and writes .monkeys/outcome.md.
---

# scout-outcome

This skill answers one question honestly: what did the last set of moves actually do? Not what they were supposed to do, not what they probably did. What a real, dated, sourced number says happened.

## 1. What actually goes wrong

The obvious failure is inventing a number. It is not the one that does the most damage. The one that does the damage is grading a run where everything "worked," because a retro like that has stopped doing its job. Every real set of moves produces some noise, some flat lines, and at least one thing not worth doing again. **A retro that finds everything worked is not a retro, it's a celebration wearing a retro's shape**, and it teaches nothing about what to stop.

## 2. Where results live

Never estimate a number and never recall one from memory of a prior session. Read it fresh, from where it was actually captured:

- **`F:\Analytics\snapshots`**: GA4 exports and other captured analytics. The source of record for traffic, conversion, and signup figures.
- **The `campaign.md` that ran**: what was actually attempted, and when, so a metric can be tied to a specific move rather than a vague window of time.
- **A prior `scout-geo` audit**, once that skill exists: discoverability numbers over time.

The full list of what to check and where, including how to handle a metric with no clean before/after snapshot, is in `references/measurement-checklist.md`. Read it before grading anything.

**Every figure gets a `source:` and an `on:` date.** Not "roughly last week," the actual date the file was captured or the number was pulled. A figure without both is not gradable; leave it out rather than approximate it.

## 3. Grade into three buckets

- **Moved**: a metric that changed, tied to the move that plausibly caused it, sourced and dated.
- **Flat**: a move that was made and a metric that was checked, and nothing changed. This is not a failure to record quietly; it's the finding.
- **Prune**: something to stop doing, justified by a null or negative result recorded above it. Not a vibe, not "this doesn't feel worth it." A specific Flat or a specific absence of a Moved line, cited.

**A null result is recorded as a null, never spun.** "Flat, but early days" or "flat, but building awareness" are not gradings, they're excuses standing in the place a finding should be. If the honest read is that nothing moved, write that nothing moved.

## 4. The signature discipline

**An outcome run only passes if it names at least one thing to prune.** If a full review of the last stretch of moves can't find a single thing worth stopping, the review wasn't rigorous enough. Something in every real batch of moves underperforms; finding it is the point of running this skill at all. Go back through Flat before concluding there's nothing to prune.

## 5. Write `.monkeys/outcome.md`

`assets/outcome_lint.py` checks this file's form: three required sections, each bullet's required fields, and that every `on:` value is a real `YYYY-MM-DD` date.

```markdown
# Outcome — what the last moves actually did

## Moved
- <the metric that moved> — by: <amount> — after: <the move> — source: <where measured> — on: <YYYY-MM-DD>

## Flat
- <a move that produced no measurable change> — measured: <what was checked> — source: <where> — on: <YYYY-MM-DD>

## Prune
- <what to stop doing> — because: <the null or negative result that justifies it>
```

Run `python assets/outcome_lint.py .monkeys/outcome.md` before handing off. It checks that every bullet carries the fields a human needs to verify it; it cannot and does not judge whether a move actually caused a metric to change, or whether a prune decision is the right call. Form only, never truth, the same discipline `raid-intake`'s `lexicon_lint.py` holds.

## 6. Floors

**Never invent a figure.** Not a plausible-looking round number, not a "roughly," not a recollection of what a dashboard probably showed. If it wasn't read from a source this run, it doesn't go in.

**This skill never publishes.** It stages a file for a human, and for `RAID` and `FORTRESS` to read. It doesn't post a retro, doesn't announce a metric, doesn't send anything anywhere.

**The handle, and the permalink, never enter the pack.** Where a moved metric traces back to a specific post or account, capture what it proved (the reach, the date, the number), then discard the identifying link the same way `raid-intake` discards one after verifying with it.

## 7. What this doesn't decide

It grades what happened. It does not decide the next play (`RAID`'s job), does not clear a claim for publication (`FORTRESS`'s job), and does not re-run the campaign that produced these numbers. Hand `outcome.md` to whoever plans the next round.

A worked run, including a null result that leads to a real prune, is in `../../examples/scout-outcome-worked-example.md`.
