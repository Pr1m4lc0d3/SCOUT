# scout-outcome: worked example

A retro on three weeks of moves for a fictional product. The product and the numbers are
invented for this example; the failure mode they demonstrate (a retro that almost let a dead
channel keep running) is not.

## What ran

`campaign.md` shows three moves in the window: a launch post on a public forum thread, a
changelog post pointing back to the repo, and a weekly cross-post of the changelog into a
general Discord channel that had no prior relationship to the product.

## Opening the sources

**GA4.** `F:\Analytics\snapshots\2026-07-20-ga4.csv` (before) and
`F:\Analytics\snapshots\2026-08-10-ga4.csv` (after) both open. Newsletter signups: 18 to 60,
read directly off the two files. Landing page conversion rate: 3.1% to 3.0%, functionally
unchanged across the same window.

**GitHub.** The repo's own API, queried on 2026-08-12: stars up from 41 to 50, forks up from 6
to 9. Fork-to-star ratio holds close to the same band before and after; the increase reads as
attention, not a shift in who is actually running the thing.

**Discord.** The general channel's own message search, run on 2026-08-13: the weekly cross-post
appears four times across the window. Zero replies, zero reactions, and the channel's own
"new member" role log shows no join event traceable to any of the four posts.

## Grading

The forum post and the changelog post both tie to real, dated movement. The Discord cross-post
ties to nothing, checked directly at the source rather than assumed dead from a gut feeling.
That is the null result this run exists to catch, and it gets recorded exactly as it is, not
softened into "still building awareness there."

## What gets written

`.monkeys/outcome.md`:

```markdown
# Outcome — what the last moves actually did

## Moved
- newsletter signups — by: +42 — after: the launch post on the forum thread — source: F:\Analytics\snapshots\2026-08-10-ga4.csv — on: 2026-08-10
- repo stars — by: +9 — after: the changelog post — source: a code host's own API — on: 2026-08-12

## Flat
- landing page conversion rate — measured: signups over unique visitors, 3.1% before vs 3.0% after — source: F:\Analytics\snapshots\2026-08-10-ga4.csv — on: 2026-08-10
- Discord general channel joins attributable to the cross-post — measured: the channel's own new-member role log against four post dates — source: the Discord channel's own message and member search — on: 2026-08-13

## Prune
- the weekly cross-post of the changelog into the general Discord channel — because: four posts across three weeks produced zero replies, zero reactions, and zero attributable joins per the Flat line above; the channel was never a room this product had standing in
```

## The scoreboard

| | Before grading | After grading |
|---|---|---|
| Moves reviewed | 3 | 3 |
| Moved | assumed 3 | 2, sourced |
| Flat | assumed 0 | 2, including one that looked fine until checked |
| Prune | none proposed | 1, cited against a measured null |

**The run passes only because it found something to stop.** Had the Discord line been left as
"still early, worth continuing," the retro would have produced two Moved lines and a vague
feeling about the third, which is not a graded outcome, it's an unexamined assumption with a
date stamped on it.
