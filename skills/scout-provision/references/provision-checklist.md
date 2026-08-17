# Provision checklist — where a product's proof actually lives

Read these before writing a single line of `truth.md`. Each is a place a real
capability leaves a trace; a claim with no trace in any of them is not proven.

## Where to read
- **The deployed data directory.** Signed records, attestations, exports, logs.
  This is where "it did the thing" is provable rather than asserted. Prefer it
  over source: source shows intent, output shows behaviour.
- **The changelog.** What actually shipped, with dates. A capability not in the
  changelog is a plan, not a fact.
- **The test suite.** A passing test is evidence a behaviour holds; name the test
  as the exhibit.
- **The product's own pages and docs.** For `voice.md`: how the product already
  speaks. For `truth.md`: only claims the docs can source, never their adjectives.
- **The pricing / licensing source of truth**, for any money claim.

## The three files you write
- **`truth.md`** — `## Cleared` (claim — source), `## Uncleared` (fact — reason),
  `## Canonical source`. One claim per line, each traceable to an exhibit or a page.
- **`voice.md`** — `## Sounds like` (trait — because), `## Never says` (word —
  because), `## Proof available` (proof — shows). Read from how the product
  already writes, not from how you would write it.
- **`evidence-inventory.md`** — `## Proven`, `## Claimed but unproven`, `## Limits`.
  Run `python assets/evidence_lint.py .monkeys/evidence-inventory.md` before hand-off.

## The one file you do NOT write
- **`numbers.md`.** Its own header says it is written by whoever holds the
  credentials and is never fetched by a skill. **Do not put a row in it.** Remind
  the operator to fill it, and if it already exists you may note whether it is
  empty. An empty table is honest; an invented row is the one thing that discredits
  the whole pack.

## The prompts to the operator
- "What can this product prove that a stranger could check in ten seconds?"
- "What does it claim that has no artifact behind it yet?" (that is `## Claimed but unproven`)
- "What is the honest limit that has to travel with each claim?" (that is `## Limits`)
- "Fill `numbers.md` yourself from the dashboards; I will not invent a metric."
