# SCOUT

### Find the truth by looking

SCOUT is the investigation third of **THE MAVERICK'S MONKEYS**, a set of Claude Code plugins that
together make an agent competent at marketing a product with no budget. `RAID` takes ground.
`FORTRESS` guards the truth of what you say once it's public. SCOUT establishes what's actually
real before either of them acts on it: reconnaissance, intake, grading, and measuring what your
last moves actually did.

**The other two halves: [`RAID`](https://github.com/Pr1m4lc0d3/RAID) and
[`FORTRESS`](https://github.com/Pr1m4lc0d3/FORTRESS).**

## Why a third pack

RAID and FORTRESS both assume the evidence they act on is already sound: a pain that was really
said, a room that's really active, a fact that really checks out. Something has to go establish
that before either of them can trust it, and it isn't the same discipline as taking ground or
guarding a claim. Looking honestly at what's actually there, and writing down what you found
including the parts that disappoint, is its own job. SCOUT is that job.

## Status

Phase 1 of this pack. One skill is live:

| Skill | Job |
|---|---|
| **`scout`** | Front door: doctrine, the floors that bind every skill here, and the routing table. |
| **`scout-outcome`** | Measures what the last moves actually did, against real captured numbers, and grades the result into what moved, what stayed flat, and what to stop doing. |

Four more skills belong in this pack and are on their way in a later phase, migrating from RAID
(`scout-recon`, `scout-intake`, `scout-provision`) or built new (`scout-geo`). Until then this repo
ships exactly what's above, nothing pre-announced as done that isn't.

## The floors

**Never invent a figure.** **Source every number with a date.** **A null result is a finding, never
spun.** **Stage, never publish; a human sends.** **The handle and the permalink never enter a pack
file.** Full statement of each in `skills/scout/SKILL.md`.

## Install

```
/plugin marketplace add Pr1m4lc0d3/SCOUT
/plugin install scout@scout
```

Or point the marketplace command at wherever this repository is checked out locally
(`.claude-plugin/marketplace.json` at the repo root).

## Where this came from

Deliberon is a Windows desktop app that runs a council of AI agents on a hard decision and hands
back a Decision Record: dissent preserved, every claim marked as proved, asserted, or estimated.

SCOUT is part of the marketing method built to sell it, published in full because a method you
cannot read is a method you cannot check.

Pay once, it's yours, no subscription. Thirty days of the full council with no account and no
card. Runs on your machine with your own model keys.

https://deliberon.com
