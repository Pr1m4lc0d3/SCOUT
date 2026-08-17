# raid-intake — worked example

A deliberately poisoned dump and what intake does with it. Every trap below is one
that occurred in a real run, not one invented to make the skill look good. The
product and market are fictional; the failure modes are not.

## The dump, as the chatbot returned it

> **Round 1 — "what makes buyers refuse a bread subscription?"**
>
> Buyers care most about price. Typical subscriptions run $18–$40 a month and
> people say the cheaper tiers are better value.
>
> **Round 2 — "what do people say about bread subscriptions?"**
>
> "the crust never survives shipping, every single time" — @a_baker, 3 Aug 2026,
> https://example.test/a_baker/status/1
>
> "honestly the packaging is the whole product" — @crumbco, 4 Aug 2026,
> https://example.test/crumbco/status/2
>
> "drop a comment and I'll send you my full bakery shortlist" — @loafhunter, 5 Aug 2026,
> https://example.test/loafhunter/status/3
>
> Bread lovers gather on the big baking forums and on social media. Competing
> products include LoafBox, CrumbClub and PanaderiaOne.
>
> Studies have shown that fresh bread subscriptions have higher retention than
> other food boxes.

## What intake does, in order

**Session audit, before anything is graded.**

- **Question drift.** Round 1 asked about refusal and returned pricing. The
  objections question is marked **unanswered**; its content is filed under price,
  not under objections.
- **Seeded contamination.** The operator is asked what they told this chatbot
  before these questions, and answers: *"I described my product as the bread box
  where the crust survives shipping."* Round 2's first quote restates that
  almost exactly. It is the operator's own framing coming back, so **it is struck
  from the demand evidence entirely** and kept only as a note that the phrasing
  was seeded. Had nobody asked, it would have read as the market's own words.
- **Format compliance.** Round 1 carries no quote and no link. Graded lower and
  labelled where used.
- **Source concentration.** Three quotes, three posts. Reported as three, not as
  "several".

**Opening the links.**

- `@a_baker` opens, wording matches, **reach 240**, speaker **buyer**, position
  **reply**. → `verified: yes`
- `@crumbco` opens, wording matches, **reach 12**, and the account bio reads
  "artisan packaging for small bakers". **Speaker: vendor.** → filed under
  competitors, **never under pains**.
- `@loafhunter` opens, wording matches, post shows **4,100 replies** and **3,800
  reposts**. **gated: yes** because it trades a deliverable (bakery shortlist)
  for engagement. The reply and repost counts are manufactured by that trade and
  are not read as interest; reach by view count still stands. Engagement bait,
  not a customer pain → excluded from pain count.

**Walking the thread.** `@a_baker`'s post is a reply. Its root has **51,000
views** and asks "why do I keep cancelling bread boxes?", with 90 replies
containing eleven refusal reasons the dump never mentioned. **The dump handed
over the 240-view tail of a 51,000-view thread.**

Two replies down, `@a_baker` qualifies the quote: "to be fair the sourdough one
was fine". That travels with the quote or the quote is unusable.

**Going where the chatbot cannot.** LoafBox's own page: every button routes to a
waitlist, so it is **not a competitor today and its prices are struck as
anchors**. CrumbClub is live with a free trial. **PanaderiaOne has no site and no
record anywhere. Struck.**

**The unsourced claim.** "Studies have shown" is barred outright. It is then
**chased**: the operator is asked for the source. If they have one, it is read and
cited. If nobody can name one, the claim does not exist. Barring is step one, not
the end.

## What gets written

`.monkeys/recon.md`:

```markdown
## Pains
- "the crust never survives shipping, every single time" — heard in: a social platform — reach: 240 — verified: yes
```

The handle and the link are gone. They did their job at verification.

Excerpt from `.monkeys/lexicon.md`:

```markdown
## Objections
- "the crust never survives shipping, every single time" — heard in: a social platform — reach: 240 — verified: yes, 2026-08-17

## Unanswered
- why do I keep cancelling bread boxes — asked in: a social platform — reach: 51000
```

A complete `.monkeys/lexicon.md` carries all five sections (Vocabulary, Wants, Objections, Unanswered, Demand signals); this excerpt shows only the two sections these findings landed in.

## The scoreboard

| | The dump | After intake |
|---|---|---|
| Pains | 2 | 1 kept, 1 reclassified as a vendor |
| Objections | 0 | 11 found in the walked thread |
| Competitors | 3 named | 1 live, 1 waitlist, 1 nonexistent |
| Largest source | 240 views | 51,000 views |
| Questions answered | "all 2" | 1, with 1 marked unanswered |

**The run passes only because it surfaced a source the dump did not contain.** A
run that merely confirms what it was handed has not done the job.
