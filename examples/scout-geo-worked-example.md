# scout-geo: worked example

A discoverability audit for a fictional product: a desktop app that runs a council of AI
agents on a hard decision and hands back a decision record. The product and the assistant
answers below are invented for this example; the failure mode they demonstrate (a real gap
that a warm session would have hidden) is not.

## Pulling the queries

`lexicon.md` carries two lines worth drawing from:

- `## Unanswered`, asked in a forum thread and seen at a reach of 3400: "is there a tool that
  runs a council of AI agents on a hard decision, not just one model."
- `## Vocabulary`, heard in the same forum thread and used by three separate replies the same
  way: "decision council."

Both become literal-ask queries, kept close to the words actually used rather than rewritten
into marketing language.

## Running the audit

Two fresh sessions, one per assistant, neither signed in, neither carrying any prior turn
about this product or its market.

**Assistant A, clean session, asked the Unanswered line verbatim.** It suggested convening a
panel of human advisors and offered to help draft discussion questions. It named no software
at all. `found: no`.

**Assistant B, clean session, asked "is there a decision council app."** It named a note-taking
app with a "meeting summary" feature and described it as a tool for capturing what a group
decided. That's a real product, but it isn't this one, and it doesn't run a council or preserve
dissent. `found: no`, because naming the wrong tool with the wrong description is not a partial
find, it's a miss with a plausible-sounding wrong answer, which is worse than silence because a
reader might stop looking.

Neither result got softened. The first pass at drafting this file read "Assistant B: partially
found, found something adjacent." That line was rewritten before it shipped, because "adjacent"
is a state this file doesn't have.

## What gets written

`.monkeys/discoverability.md`:

```markdown
# Discoverability — can an AI find and describe the product

## Queries
- "is there a tool that runs a council of AI agents on a hard decision, not just one model" — source: lexicon.md Unanswered
- "is there a decision council app" — source: lexicon.md Vocabulary, "decision council"

## Results
- is there a tool that runs a council of AI agents on a hard decision, not just one model — assistant: Assistant A, clean session — found: no — as: suggested convening a panel of human advisors and offered to draft discussion questions; named no software — on: 2026-08-17
- is there a decision council app — assistant: Assistant B, clean session — found: no — as: named a note-taking app with a meeting-summary feature, described as capturing what a group decided; not this product, no council, no dissent preserved — on: 2026-08-17

## Fix
- publish a page answering "is there a tool that runs a council of AI agents on a hard decision, not just one model" verbatim in its own words — because: the first Results line above found no software named at all, a clean demand-shaped hole
- publish a page that names and distinguishes this product from a meeting-summary tool by category ("a council of models, not a summary of a meeting") — because: the second Results line above shows an assistant filling the gap with the wrong product
```

## The scoreboard

| | Before the audit | After the audit |
|---|---|---|
| Queries checked | assumed answerable | 2, both checked in a clean session |
| Found | assumed yes | 0 of 2 |
| Fix lines | none staged | 2, each cited to a specific result |

**The run is only useful because both results are `found: no`, recorded plainly.** A version of
this file that called Assistant B's answer "partially found, since it found a related tool" would
have hidden the actual gap: nothing on the internet currently tells an asker this product exists,
and the two most likely queries a real buyer would type both come back empty or wrong.
