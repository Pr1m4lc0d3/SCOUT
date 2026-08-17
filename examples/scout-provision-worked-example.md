# raid-provision — worked example

A product read into a supply-side pack. The product is fictional; the failure
modes are real. It shows the one move that matters: refusing to file a claim as
Proven when only intent, not output, backs it.

## The product, as its own docs describe it

> **CrustBox** is a bread subscription. Our site says: "every loaf arrives with
> the crust intact, always." The changelog for v2 says "added tamper-evident,
> crush-resistant packaging." Our test suite has `test_packaging_survives_drop`.
> We believe retention is high. We think customers love the crust guarantee.

## What provision does, in order

**Read where proof lives.**

- The **deployed record**: a returns log at `data/returns/` shows 2 crust-damage
  returns in 400 orders since the v2 packaging shipped. That is an exhibit.
- The **changelog** confirms the packaging shipped, with a date. Fact.
- The **test** `test_packaging_survives_drop` passes. An exhibit for the drop
  claim, not for "always".
- The **site copy** says "always". Nothing sources "always"; the returns log
  sources "2 in 400". The adjective is not lifted.

**Refuse the flattering line.** "Every loaf arrives with the crust intact,
always" cannot go under `## Proven`. The record shows 2 failures. It becomes a
`## Limits` line beside the real, provable claim.

**Refuse numbers.md.** "We believe retention is high" is a metric with no
credentialed source in reach. The operator is reminded to fill `numbers.md`
from the billing dashboard. **No row is written.**

## What gets written

`.monkeys/truth.md`:

```markdown
## Cleared
- crush-resistant packaging shipped in v2 — source: changelog 2026-06
- the packaging survives a drop test — source: test_packaging_survives_drop

## Uncleared
- crusts "always" survive shipping — reason: returns log shows 2 in 400, not always
```

`.monkeys/evidence-inventory.md`:

```markdown
## Proven
- crush-resistant packaging survives a drop test — exhibit: test_packaging_survives_drop — kind: passing test — verified: yes, 2026-08-17
- crust damage is rare under v2 packaging — exhibit: data/returns/ (2 in 400) — kind: returns log — verified: yes, 2026-08-17

## Claimed but unproven
- customers love the crust guarantee — reason: no review or survey artifact exists yet

## Limits
- 2 of 400 v2 orders were returned for crust damage — bears on: any "always intact" claim
```

`.monkeys/numbers.md`: **untouched.** A note is handed to the operator: "fill
retention from the billing dashboard; I did not invent it."

## The scoreboard

| | The docs claimed | After provision |
|---|---|---|
| "always intact" | a headline | moved to Limits; the real claim is "rare damage, 2 in 400" |
| drop-proof | asserted | Proven, exhibit named |
| "customers love it" | asserted | Claimed but unproven, no artifact |
| retention "high" | asserted | refused; numbers.md left for the operator |

**The run passes only because it moved a claim the product was proud of out of
Proven.** A provision run that files everything the product asserts as Proven has
not done the job.
