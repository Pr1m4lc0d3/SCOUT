# Discoverability audit checklist

The detail behind `SKILL.md` sections 2 and 3: where a query comes from, and how to run a
session clean enough that the result actually means something.

## The rule, stated once, applied everywhere below

**Run every query in a clean, memory-free session. Quote the assistant's answer verbatim. A
`found: no` is a finding, not a failure to fix before recording it.** A result read from a
session that already knows the product isn't evidence of discoverability, it's a reflection of
the operator's own prompting.

## Pulling queries from `lexicon.md`

`lexicon.md` (written by `scout-intake`) is the only source for a query in this audit.

| Section | What it gives you | How to turn it into a query |
|---|---|---|
| `## Unanswered` | A question asked in public that nobody answered, with the reach it was seen at | Ask it close to word for word; this is already the closest thing to a literal ask on record |
| `## Vocabulary` | A term or phrase heard exactly as the market uses it, with where it was heard | Wrap it in the plain question shape a buyer would type ("is there a tool that <the term>"), keeping the market's own words |

Do not draw a query from `## Wants`, `## Objections`, or `## Demand signals`. Those sections
carry motive and refusal, not the phrasing of a search. A query invented to sound like a
plausible ask, rather than pulled from a line someone actually typed or said, isn't a literal
ask and doesn't belong in `## Queries`.

**If `lexicon.md` has too few `Unanswered` or `Vocabulary` lines to draw a real query from**,
that's a gap in intake, not license to write one from imagination. Record fewer queries this
run and note the shortage for whoever runs `scout-intake` next, rather than padding the file
with guesses.

## Running a session that's actually clean

Before asking the first query, check every one of these:

- **Not logged in.** A signed-in account can carry account-level memory or personalization even
  in what looks like a fresh chat.
- **No prior turns about this product, or its market, in this session.** A session opened fresh
  for an unrelated task earlier today is not clean for this audit.
- **Nothing about the product pasted into the session this run.** Not the docs, not a summary,
  not "here's some context before you answer."
- **One query per session where the assistant supports it**, or at minimum, no query asked after
  an answer that named or described the product in an earlier turn of the same session. A later
  query in a session that already discussed the product is contaminated the same way a seeded
  chatbot dump is in `scout-intake`.

If a genuinely clean session can't be run this pass (no way to log out, no way to clear memory
on the assistant in question), skip that assistant for that query rather than recording a
compromised result. A missing result is honest; a compromised one reads as settled and is worse
than useless.

## Recording the result

- **`assistant:`** name it plainly (which AI, and that the session was clean), so a later run can
  check whether the same assistant's answer changed.
- **`found:`** `yes` or `no`, nothing else. See `SKILL.md` section 3 on why there's no partial
  state.
- **`as:`** the verbatim answer, or the relevant part of it. If it named a competitor instead,
  quote that. If it gave generic advice with no tool named, quote that too. The point is to
  capture exactly what a real asker would have read.
- **`on:`** the actual date the session ran, not the date the audit was written up.

## Writing a `Fix` line

A `Fix` line only exists because a specific `Results` line justifies it. `because:` cites that
line directly: which query, which assistant, what it got wrong or didn't find. A fix line with
no citation is a guess about what to build next, not a finding this audit produced.

This skill stages the fix. It does not write the page, edit the site, or publish anything;
that's a human's call, or `RAID`'s, once `discoverability.md` is handed off.
