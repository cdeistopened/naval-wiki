---
name: business-model-selector
description: "Evaluate your business model against Naval's three-tier hierarchy — scale economies, zero marginal cost, and network effects. Use when choosing a business model, evaluating whether your product can scale, or deciding between service vs. product vs. platform. This is a decision skill."
---

# Business Model Selector

You help someone evaluate and select a business model using Naval's hierarchy of business model properties. You ask about their product, market, and capabilities, then score their model against three tiers and deliver specific recommendations for upgrading toward zero-marginal-cost and network-effect businesses.

## The Consultation

### Step 1: Understand What They're Building

Ask the user for:

1. **Product/service description:** What do you sell or plan to sell? In one sentence.
2. **Delivery mechanism:** How does the customer get value? (In-person service, physical product, software, content, marketplace, etc.)
3. **Current unit economics:** What does it cost you to serve one additional customer? (If they don't know, that's the first problem.)
4. **Target market:** Who buys this? How many of them exist?
5. **Technical capability:** Can you (or your team) write code? Create media? Build software?
6. **Current stage:** Idea, prototype, revenue, scaling?

### Step 2: Score Against Naval's Three-Tier Hierarchy

Naval identifies three business model properties that create durable competitive advantage. Each tier is more powerful than the last. Most businesses have zero of these. The best businesses have all three.

#### Tier 1: Scale Economies

> "The more you produce, the cheaper it gets." — `2019-04-22-business-models.md`

Scale economies mean your per-unit cost drops as volume increases. This is the weakest form of advantage — it helps but doesn't protect.

| Question | Yes | No |
|----------|-----|-----|
| Does your cost per unit decrease as you serve more customers? | +1 | 0 |
| Do you have fixed costs that get amortized across more units? | +1 | 0 |
| Would a 10x increase in customers reduce per-unit cost by 2x or more? | +1 | 0 |
| Can a new competitor match your unit costs on day one? | 0 (bad) | +1 (good) |

**Scale economy score:** 0-1 = no scale economies, 2-3 = moderate, 4 = strong.

**Examples by score:**
- Consulting firm (0) — every new client costs roughly the same to serve
- Manufacturing (2) — fixed costs amortize, but competitors can build factories
- Amazon retail (4) — warehouse network and purchasing power create compounding cost advantage

#### Tier 2: Zero Marginal Cost of Reproduction

> "Creating another copy is free." — `2019-04-22-business-models.md`

This is where the leverage fundamentally changes. Once you build the thing, distributing it costs nothing. Software, media, digital products, and information businesses live here.

> "Code and media are permissionless leverage. They're the leverage behind the newly rich. You can create software and media that works for you while you sleep." — `2019-04-17-product-media.md`

| Question | Yes | No |
|----------|-----|-----|
| Once built, can you serve the 1,000th customer for effectively $0? | +1 | 0 |
| Is your product digital (software, content, data, media)? | +1 | 0 |
| Can you serve customers while you sleep? | +1 | 0 |
| Does serving more customers NOT require more employees? | +1 | 0 |
| Can you distribute globally without physical infrastructure? | +1 | 0 |

**Zero marginal cost score:** 0-1 = labor-intensive (you're renting time), 2-3 = partially leveraged, 4-5 = fully leveraged.

**The critical transition:** If the user scores 0-1 here, help them find a way to productize. Every service business contains a product waiting to be extracted.

> "An army of robots is already here. It's very cheaply available. The bottleneck is just figuring out intelligent and interesting things to do to them." — `2019-04-19-egalitarian-leverage.md`

Ask: "What part of what you do could be turned into software, a template, a course, or a tool that runs without you?"

#### Tier 3: Network Effects

> "The value of a network is proportional to the square of the number of nodes in the network." — `2019-04-22-business-models.md`

Network effects are the strongest form of competitive advantage. Each new user makes the product more valuable for all existing users. This creates natural monopolies.

> "Network effects create natural monopolies." — `2019-04-22-business-models.md`

| Question | Yes | No |
|----------|-----|-----|
| Does each new user make the product more valuable for existing users? | +1 | 0 |
| Would switching to a competitor mean losing access to other users? | +1 | 0 |
| Do your users create content, data, or connections that other users consume? | +1 | 0 |
| Is there a "tipping point" after which growth becomes self-sustaining? | +1 | 0 |
| Can you articulate the specific mechanism by which users add value to each other? | +1 | 0 |

**Network effect score:** 0-1 = no network effects, 2-3 = emerging, 4-5 = strong network effects.

**The language test:** Naval uses language as the canonical example of network effects. English is valuable because everyone speaks it, and everyone speaks it because it's valuable. Ask:

> "Is your product like a language — where the more people use it, the more everyone has to use it?"

> "You should always be thinking about how your users, your customers, can add value to each other because that is the ultimate form of leverage." — `2019-04-22-business-models.md`

### Step 3: Diagnose and Prescribe

#### The Business Model Matrix

Map the user's scores to Naval's hierarchy:

| Profile | Tier 1 (Scale) | Tier 2 (Zero MC) | Tier 3 (Network) | Diagnosis |
|---------|----------------|-------------------|-------------------|-----------|
| **Service business** | 0-1 | 0-1 | 0 | You're renting time. Productize or stay small. |
| **Product business** | 2-3 | 0-1 | 0 | You have scale but not leverage. Can you digitize? |
| **Software/media** | 2-4 | 4-5 | 0-1 | You have leverage but no moat. Can users add value to each other? |
| **Platform/marketplace** | 3-4 | 4-5 | 4-5 | You're in the strongest position. Protect and grow the network. |

#### The Upgrade Path

For each tier the user is missing, provide specific recommendations:

**To add zero marginal cost (Tier 2):**
1. Identify the repeatable knowledge in your service and package it as software, templates, or content
2. Build once, sell many times — courses, tools, APIs, digital products
3. Use code as your "robot army" to do the repetitive work

**To add network effects (Tier 3):**
1. Find the mechanism by which users can add value to each other (reviews, content, connections, data)
2. Build the smallest viable network — a single use case where 10 users are better than 1
3. Avoid the cold-start trap: seed one side heavily before expecting organic growth

**The zero-to-network pipeline:** Naval observes that zero-marginal-cost businesses can evolve into network-effect businesses. Software that starts as a tool (Tier 2) can become a platform (Tier 3) when users start interacting through it.

#### The Hot Market Warning

> "Anyone in this business who's chasing hot markets gets killed." — `2019-04-22-business-models.md`

If the user is entering a "hot" space because everyone says it's the next big thing, flag this. The best businesses come from genuine specific knowledge applied to a market the founder deeply understands — not from chasing trends.

## Output

### Business Model Assessment: [Product/Company Name]

#### Tier Scores

| Tier | Score | Status |
|------|-------|--------|
| 1. Scale Economies | [0-4] | [None / Moderate / Strong] |
| 2. Zero Marginal Cost | [0-5] | [Labor-intensive / Partially leveraged / Fully leveraged] |
| 3. Network Effects | [0-5] | [None / Emerging / Strong] |

#### Current Model Classification

**You are running a: [Service / Product / Software / Platform] business.**

[2-3 sentences on where they stand and what this means for their ceiling.]

#### Upgrade Recommendations

**Priority 1:** [The most impactful tier to add next, with 2-3 specific actions]

**Priority 2:** [The second tier to pursue, with timeline and prerequisites]

**Long-term vision:** [What this business looks like if it achieves all three tiers]

#### Leverage Assessment

| Leverage Type | Current | Potential |
|--------------|---------|-----------|
| Labor | [How many people required?] | [Can you reduce?] |
| Capital | [How much capital required?] | [Does it compound?] |
| Code | [Any software?] | [What could you build?] |
| Media | [Any content/audience?] | [What could you create?] |

> "Fortunes require leverage. Business leverage comes from capital, people and products with no marginal costs of replication." — `2019-04-15-labor-capital.md`

#### The Compounding Question

Will this business be stronger in 5 years simply because it exists today? If the answer is no — if a new entrant could replicate your position — you don't have a durable model yet.

## Source Transcripts

- `2019-04-22-business-models.md` — The three-tier hierarchy: scale economies, zero marginal cost, network effects
- `2019-04-19-egalitarian-leverage.md` — Permissionless leverage, code and media as the great equalizer
- `2019-04-15-labor-capital.md` — Why labor is the worst leverage and capital requires specific knowledge
- `2019-04-17-product-media.md` — Products and media as leverage that works while you sleep

## Related Skills

- **leverage-stack-evaluator** — Evaluate which form of leverage (labor, capital, code, media) to pursue given your position
- **wealth-creation-audit** — Assess whether your current path creates wealth or just rents time
- **specific-knowledge-identifier** — Find the intersection of talent, curiosity, and market value that powers your business model
- **ai-leverage-evaluator** — Evaluate how AI can accelerate your move up the leverage stack

## Related Frameworks

- `permissionless-vs-permissioned-leverage.md` — Code and media don't require anyone's permission
- `inputs-vs-outputs-disconnection.md` — You want a business where inputs and outputs are highly disconnected
- `renting-time-vs-owning-equity.md` — Service businesses rent time; product businesses create equity
- `the-internet-broadens-career-space.md` — The internet enables niche zero-marginal-cost businesses at global scale
