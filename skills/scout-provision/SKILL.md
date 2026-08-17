---
name: raid-provision
description: Use when pointing the machine at a new product, or when the pack has no supply-side files yet. Reads the product's own repo, data and artifacts and writes truth.md, voice.md and evidence-inventory.md under the verified discipline.
---

# raid-provision

Every other RAID skill studies the market. This one studies the product, and it exists because you cannot position a thing you have not established the truth of. It is the mirror of raid-intake: intake grades what a chatbot said about the world; provision grades what the product can actually prove about itself.

## 1. What actually goes wrong

The failure is not lying. It is the flattering inventory: a supply-side pack where every market want has a matching feature and nothing is marked unproven. A pack that neat is the tell, not the triumph.

> **Your job is not to list features. It is to separate what the product can prove from what it merely claims, and to write the limits down beside the claims.**

The market this machine sells into has learned to distrust the category's own vocabulary. The one thing that earns trust back is a product that flags its own limits unprompted. That asset is built here, or it is not built at all.

## 2. Read the product where its proof lives

The checklist is in `references/provision-checklist.md`. In order of weight:

- **Deployed output beats source.** Source shows intent; a signed record, an export, a log shows behaviour. Prefer the data directory over the codebase.
- **The changelog is the fact of what shipped.** A capability not in it is a plan.
- **A passing test is an exhibit.** Name it.
- **Pages and docs give voice, and give claims only where they can source them.** Never lift an adjective as a fact.

## 3. Write three files, and refuse the fourth

- **`truth.md`** keeps the FORTRESS contract exactly: `## Cleared` (claim — source), `## Uncleared` (fact — reason), `## Canonical source`. A claim with no source does not go under Cleared. `fortress-truth`'s `claim_lint.py` checks its form.
- **`voice.md`** keeps its contract: `## Sounds like` (trait — because), `## Never says` (word — because), `## Proof available` (proof — shows). Read the product's real voice; do not impose one.
- **`evidence-inventory.md`** is this skill's own file: `## Proven`, `## Claimed but unproven`, `## Limits`. Run `python assets/evidence_lint.py .monkeys/evidence-inventory.md` before hand-off. It checks form, never truth.
- **`numbers.md` you do not touch.** Its header says it is written by whoever holds the credentials and is never fetched by a skill. Remind the operator to fill it. **Never write a row.** An invented metric discredits the entire pack.

## 4. The inventory, honestly

Three sections, and the last two are the point.

- **`## Proven`** — a capability, the exhibit that proves it, the kind of proof, and whether it was verified at source and when. A stranger should be able to open the exhibit and check it.
- **`## Claimed but unproven`** — a capability asserted with no artifact behind it, and why not yet. This is not a weakness to hide; it is the list of what to go prove next.
- **`## Limits`** — the honest counter-fact that travels with a claim. If a capability is real but rare, or fragile, or single-provider by default, the limit is recorded beside it. A claim shipped without its limit is the failure this whole file prevents.

## 5. Floors

**Deployed output over source.** If both exist, the record wins.

**A claim with no exhibit is `Claimed but unproven`, never `Proven`.** No exception for a capability you are sure of. Sure is not checked.

**The limit travels with the claim.** A `## Proven` line whose real-world limit is known and omitted is malformed even when the linter passes, because the linter checks fields, not honesty. You check honesty.

**Never write `numbers.md`.** Remind, never fetch, never invent.

**This skill never publishes.** RAID stages. A human sends.

## 6. What this doesn't decide

It establishes what is true about the product. It does not decide what the market wants (`raid-recon`, `raid-intake`), what to say against a competitor (`raid-asymmetry`), or what the copy is (`raid-draft`, `raid-cite`). Those consume `truth.md` and `evidence-inventory.md`; they cannot run honestly without them.

A worked run is in `examples/raid-provision-worked-example.md`. The reading checklist is in `references/provision-checklist.md`.
