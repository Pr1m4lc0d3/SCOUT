---
name: scout
description: SCOUT front door. Find the truth by looking. Use when starting reconnaissance, intake, grading, or measurement work, or entering the SCOUT discipline for the first time. States the doctrine and floors, then routes to the skill that's live.
---

# scout

This is the front door. It holds the doctrine, the floors that bind every skill in this plugin, and the routing table. Read this once per adoption; route out of it for everything after.

## 1. The doctrine

Find the truth by looking.

`RAID` takes ground. `FORTRESS` guards the truth of what you say once it's public. SCOUT is the third leg: it establishes what's actually real before either of the other two acts on it. Reconnaissance finds who hurts and where. Intake grades evidence someone else handed you. Measurement finds out what your last moves actually did. None of that is persuasion, and none of it is defense. It's looking, honestly, and writing down what's there.

The discipline that makes this different from the other two: SCOUT's output is never copy. A pain, a room, a grade, a metric, none of it is written to be read by a customer. It's written to be read by `RAID` and `FORTRESS`, so the plays they build and the claims they clear stand on something that was actually checked.

## 2. The floors

These bind every SCOUT skill without exception.

**Never invent a figure.** A number that wasn't measured doesn't go in a pack file, not as a placeholder, not as a plausible-looking example, not as a rounding of something close. An absent number is absent.

**Source every number with a date.** A figure without where it came from and when it was checked is not evidence, it's an assertion wearing evidence's shape. `on: <YYYY-MM-DD>` is not decoration; it's the difference between a reading and a guess.

**A null result is a finding.** A metric that didn't move, a room that turned out dead, a claim that couldn't be checked: each one is worth recording exactly as it is. Spinning a null into a maybe, or dropping it because it's disappointing, throws away the one thing a null result is actually good for, which is stopping someone from trying the same dead thing again.

**Stage, never publish.** SCOUT produces packs, grades, and reports. It does not post, comment, submit, or send anything, and it does not perform an outward action on anyone's behalf. A human reads what SCOUT wrote and decides what to do with it.

**The handle, and the permalink, never enter a pack file.** Verify a claim with the link open, capture what the link proved, then discard the link and the account behind it. `raid-intake`'s rule binds here for the same reason: a pack file is read by people who were never meant to go looking for the person behind a quote.

## 3. Routing table

| Moment | Skill |
|---|---|
| Measuring what a campaign or move actually did, and what to stop doing | `scout-outcome` |
| Checking whether an AI assistant finds and correctly describes the product | `scout-geo` |

## 4. Joining later

Three more skills belong in this pack and aren't here yet: `scout-recon` (investigate a market: pains, rooms), `scout-intake` (grade a chatbot research dump into recon.md and lexicon.md), and `scout-provision` (establish what a product can prove: truth.md, voice.md, evidence-inventory.md). They migrate in from RAID in a later phase. Until then, `scout-outcome` and `scout-geo` are the whole of what's live.

## 5. Built-ins only

`scout-outcome` and `scout-geo` run on Read/Write/Edit, Glob/Grep, and Bash for their linters. Nothing here assumes any other plugin is installed, including RAID or FORTRESS. Where a pack file either reads (`campaign.md`, `lexicon.md`) doesn't exist yet, it says so rather than inventing one.
