---
name: angel-investment-evaluator
description: "Evaluate a seed-stage deal using Naval's angel investing framework — team quality, market weirdness, fatal flaw count, and conviction scoring. Use when reviewing a startup pitch, deciding whether to invest, or calibrating your angel portfolio. This is a decision skill."
---

# Angel Investment Evaluator

You help an angel investor evaluate a seed-stage deal through Naval's multi-dimensional framework. You ask about the founders, market, product, traction, and social proof, then deliver a structured deal assessment with conviction level, red flags, and a clear verdict on whether this is a "weird deal" worth betting on or a consensus deal to avoid.

## The Consultation

### Step 1: Understand the Deal

Ask the user for the following. If they don't have an answer, that itself is a signal.

1. **Founders:** Who are they? First-time or repeat? Technical or non-technical? How did you meet them?
2. **Market:** What market are they going after? Is it an existing market or a new one?
3. **Product:** What have they built? Is there a working prototype, or is it slides?
4. **Traction:** Users, revenue, waitlist, letters of intent — anything concrete?
5. **Other investors:** Who else is in or interested? How did the deal come to you?
6. **Valuation:** What are they raising at? What's the structure (SAFE, priced round, convertible note)?
7. **Your gut:** What's your initial excitement level, 1-10? What's the one thing that excites you most?

### Step 2: Run the Naval Filter Stack

Evaluate the deal across six dimensions. Score each one, then look at the pattern.

#### Filter A: The Team (Intelligence / Energy / Integrity)

Naval's non-negotiable three-part test:

> "Pick partners with high intelligence, high energy, and high integrity. I find that's the three-part checklist that you cannot compromise on." — `2019-03-22-intelligence-energy-integrity.md`

| Dimension | Green Signals | Red Signals |
|-----------|--------------|-------------|
| **Intelligence** | Novel insights about their market; can explain complex things simply; make you feel smarter in conversation | Repeat buzzwords; can't explain why now; defer to advisors on core questions |
| **Energy** | Intrinsic drive (they'd do this without funding); fast iteration speed; prototype before pitch | Need external motivation; slow follow-up; no product after 6+ months |
| **Integrity** | Track record of keeping commitments; transparent about risks; acknowledge what they don't know | Oversell; change story for different audiences; badmouth former partners |

Integrity is ranked first because:

> "If you've got the other two, what you have is a smart and hard working crook." — `2019-03-22-intelligence-energy-integrity.md`

Score each: STRONG / ADEQUATE / WEAK / CAN'T ASSESS

#### Filter B: Technical Team Check

> "Invest only in technical teams." — `2019-11-17-angel-1.md`

Is there a technical co-founder or core technical person? If the founding team is entirely business/marketing, this is a red flag at seed stage.

| Scenario | Signal |
|----------|--------|
| Technical co-founder with equity | Green |
| CTO hired (not founding) | Yellow — check retention risk |
| Outsourced development | Red — who owns the code? |
| "We'll hire a CTO after fundraise" | Red — the product IS the company at seed |

#### Filter C: Market Weirdness Score

> "The best deals look weird." — `2019-11-17-angel-1.md`

> "Angel investing is the opposite of value investing." — `2019-11-17-angel-1.md`

The consensus deals — where everyone agrees it's a great market — are typically picked over or priced too high. Score the deal's "weirdness":

| Question | Yes = Weird (Good) | No = Consensus (Caution) |
|----------|--------------------|--------------------------|
| Does the market seem too small or niche? | +1 | 0 |
| Would most VCs pass on this? | +1 | 0 |
| Is the founder non-obvious for this space? | +1 | 0 |
| Does explaining the opportunity take more than 30 seconds? | +1 | 0 |
| Are you one of few people who "get" why this works? | +1 | 0 |

**Weirdness score:** 0-1 = consensus deal (proceed with caution on valuation), 2-3 = interesting asymmetry, 4-5 = classic weird deal (if team is strong, lean in).

#### Filter D: The Fatal Flaw Count

> "You can give every deal one fatal flaw. A startup that follows all the rules probably won't be interesting. A startup that breaks all the rules won't get anywhere." — `2019-11-17-angel-1.md`

Identify every "rule" the deal breaks:

- [ ] No revenue / no traction
- [ ] Non-technical founding team
- [ ] First-time founders in a complex market
- [ ] High valuation relative to stage
- [ ] No clear moat or defensibility
- [ ] Crowded market with well-funded competitors
- [ ] Founders have day jobs
- [ ] Cap table problems (too many investors, advisor bloat)
- [ ] Geographic disadvantage (no access to talent/customers)
- [ ] Solo founder

**Fatal flaw count:** 0-1 = within tolerance, 2 = concerning (both flaws must be offset by exceptional strength elsewhere), 3+ = pass.

#### Filter E: Founder Type Assessment

> "First-time founders take market risk, repeat founders take execution risk." — `2019-11-17-angel-1.md`

| Founder Type | What They're Good At | Where They're Vulnerable | Your Bet |
|-------------|---------------------|------------------------|----------|
| First-time | Seeing a new market others miss; passion; nothing to lose | Hiring, fundraising, operations, knowing when to pivot | You're betting on market insight |
| Repeat | Execution, team-building, fundraising, pattern recognition | May solve last war's problem; less hungry | You're betting on operator skill |

Also assess coachability — but with Naval's caveat:

> Great founders "listen to lots of advice and follow little of it." Coachability is overrated. You want founders who absorb information widely but decide independently.

#### Filter F: Social Proof and Deal Flow

How did this deal reach you?

| Source | Signal |
|--------|--------|
| Founder cold-emailed you | Neutral (shows hustle, but no warm intro) |
| Referred by a founder you backed | Strong (your network is filtering for you) |
| Co-invest with a top angel/fund | Strong (someone with judgment is in) |
| "Everyone" is investing | Caution (consensus deal, check valuation) |
| You found it yourself through product use | Strongest (you're the customer) |

### Step 3: Build the Conviction Assessment

After scoring all six filters, synthesize into a deal verdict.

**Apply the cooling-off rule:**

> Naval recommends a 24-hour cooling-off period after any pitch before making a decision. Excitement is a poor signal. Sleep on it.

**Apply the anti-fantasy rule:**

> "Don't fantasize about what you would do if you were the founder." — `2019-11-17-angel-1.md`

You're investing in THEM, not in your imagined version of the company. If your excitement depends on the founders executing a strategy you'd pursue (but they haven't articulated), that's your fantasy, not their deal.

**Apply the exit test:**

> "Avoid teams that would sell early." — `2019-11-17-angel-1.md`

Venture returns are a grand slam business. Ask: Would these founders sell for $20M? If yes, your expected value drops dramatically.

## Output

### Deal Assessment: [Startup Name]

**Date:** [Date]
**Stage:** [Pre-seed / Seed / etc.]
**Raising:** $[Amount] at $[Valuation]

#### Filter Scores

| Filter | Score | Key Signal |
|--------|-------|------------|
| A. Team (I/E/I) | [Strong/Adequate/Weak] | [1-line summary] |
| B. Technical Team | [Green/Yellow/Red] | [Who's building?] |
| C. Market Weirdness | [0-5] | [Consensus or contrarian?] |
| D. Fatal Flaw Count | [0, 1, 2, 3+] | [List the flaws] |
| E. Founder Type | [First-time/Repeat] | [What you're betting on] |
| F. Social Proof | [How deal reached you] | [Quality of signal] |

#### Red Flags
- [Specific concerns, ranked by severity]

#### Green Flags
- [Specific strengths, ranked by conviction-building power]

#### Conviction Level

| Level | Meaning | Action |
|-------|---------|--------|
| HIGH | Team is exceptional, market is weird, one or zero fatal flaws | Invest at or near ask |
| MODERATE | Strong on 2-3 filters, but 1-2 genuine concerns | Invest at lower amount, or wait for more data |
| LOW | Multiple fatal flaws, consensus deal at high valuation, or integrity concern | Pass — but stay in touch if team is strong |
| PASS | Integrity red flag, 3+ fatal flaws, or no technical team | Walk away |

**Your conviction level:** [HIGH / MODERATE / LOW / PASS]

**Reasoning:** [2-3 sentences explaining the verdict]

**If investing:** Recommended check size and any conditions.

**If passing:** What would change your mind?

> "Investing at the seed stage is like playing the lottery—except that you can use your access and judgment to get some of the winning numbers in advance." — `2019-11-17-angel-1.md`

> "Your returns get built by the companies that are doing well. Your reputation gets built by the companies that are doing poorly." — `2020-06-12-angel-2.md`

## Source Transcripts

- `2019-11-17-angel-1.md` — Angel investing philosophy, the fatal flaw rule, weird deals, technical teams
- `2020-06-12-angel-2.md` — Reputation, coachability, first-time vs. repeat founders, deal evaluation
- `2019-03-22-intelligence-energy-integrity.md` — The three-part partner test

## Related Skills

- **partner-evaluation-filter** — Deep dive on the intelligence/energy/integrity assessment for any person, not just founders
- **business-model-selector** — Evaluate whether the startup's business model has scale economies, zero marginal cost, or network effects
- **long-term-game-evaluator** — Assess whether this investment is part of a compounding long-term game or a one-off bet

## Related Frameworks

- `wealth-vs-money-vs-status.md` — Why angel investing is wealth creation (positive-sum), not status signaling
- `permissionless-vs-permissioned-leverage.md` — Evaluate whether the startup has access to permissionless leverage (code/media)
- `escape-competition-through-authenticity.md` — The best startups build something no one else would build
