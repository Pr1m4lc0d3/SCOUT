# Measurement checklist

Where a number comes from decides whether it belongs in `outcome.md`. This checklist is the
detail behind `SKILL.md` section 2: read it before grading anything into Moved, Flat, or Prune.

## The rule, stated once, applied everywhere below

**Read real captured analytics. Source every figure with a date. Never estimate or invent a
number.** A figure recalled from a prior session, rounded to look tidier, or extrapolated from a
trend line is not a measurement, it's a guess wearing a measurement's shape. If the source can't be
opened this run, the figure doesn't go in this run.

## Where results live

| Source | What it settles | How to read it |
|---|---|---|
| `F:\Analytics\snapshots` | GA4 exports, and any other analytics captured to disk | Open the specific dated file. Do not average across files without saying so; report the single snapshot used. |
| The `campaign.md` that ran | What move was actually attempted, and when | Tie every Moved or Flat bullet to a specific line in that file, so the `after:` field names a real, dated action, not a guess at what probably happened. |
| A prior `scout-geo` audit, once that skill exists | Discoverability numbers over time | Compare the two most recent audits, dated, never a single reading against an assumed baseline. |
| A code host's API or a community's own analytics page | Stars, forks, room activity, referral counts | Same standard as `scout-intake`'s sourcing rule: read the API or the page itself, never a summary of it. |

## Before writing a Moved line

- Is there a real before-and-after snapshot, both dated? A single reading with nothing to compare
  it to is not a moved metric, it's one number.
- Does the `after:` field name a specific move that actually happened, not a general period of
  activity? "After the launch post on the forum" is checkable. "After recent efforts" is not.
- Is the `by:` amount read directly off the two snapshots, not estimated from a percentage someone
  remembers?

## Before writing a Flat line

- Was the metric actually checked, not merely assumed unchanged because nobody looked? `measured:`
  names what was actually pulled and compared.
- Is the source the same kind of snapshot a Moved line would use? A Flat verdict deserves the same
  rigor as a Moved one, not a lower bar because the answer is less exciting.

## Before writing a Prune line

- Does `because:` cite a specific Moved or Flat line above it, or a specific absence (a room
  measured and found dead, a channel that produced zero attributable signups across a stated
  window)? A prune with no citation is an opinion, not a finding.
- Has the underperforming move actually run long enough to judge? A move given one day and killed
  is not a measured null, it's an impatient guess.

## What this checklist cannot do

It cannot tell you whether the source itself is trustworthy, whether a snapshot was captured
correctly, or whether a metric moving for an unrelated reason got wrongly attributed to a move
that didn't cause it. That judgment stays with whoever is running `scout-outcome`; the checklist
only keeps a fabricated number from ever entering the file.
