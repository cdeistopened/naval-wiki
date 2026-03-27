---
name: "All Abstractions Are Leaky"
description: "Trigger: someone is relying entirely on AI/no-code tools without understanding what is happening underneath, or someone is debating whether to learn fundamentals vs. just using tools"
type: framework
domain: ai-technology
episodes:
  - 2026-02-ai/POLISHED.md
source: Naval Ravikant
---

## When to Use

Use this when someone is building on top of tools they do not understand. They are vibe-coding entire applications, using no-code platforms for mission-critical systems, or managing AI outputs without being able to evaluate them. They may be producing impressive results right now but are one bug, one edge case, or one abstraction leak away from being stuck.

Also use this when someone asks whether it is still worth learning fundamentals (coding, math, writing, cooking from scratch) when tools can do it for them.

## The Framework

Naval states a principle from software engineering that applies to all domains:

> "All abstractions are leaky."

In software, an abstraction is a layer that hides complexity. A programming language hides machine code. A framework hides the programming language. AI code generation hides the framework. Each layer makes you faster but also more vulnerable — because when the abstraction breaks, you need to understand the layer below to fix it.

Naval applies this directly to the AI coding revolution:

> "Software engineers still have two massive advantages on you. First, they think in code, so they actually know what's going on underneath."

When AI writes code for you, it will make mistakes. It will produce bugs, suboptimal architecture, and edge cases it cannot handle. A vibe coder hits these walls and is stuck. A software engineer recognizes the leak, drops down a level, fixes it, and moves on.

This is why professional engineers using AI are dramatically more productive than non-engineers using AI:

> "If you want to build a well-architected application, if you want to be able to even specify a well-architected application, if you want to be able to make it run at high performance, if you want it to do its best, if you want to catch the bugs early, then you're going to want to have a software engineering background."

The principle extends beyond code. If you use AI to write, understanding writing makes your AI-assisted writing better. If you use AI to analyze data, understanding statistics lets you catch when the AI is wrong. If you use AI to design, understanding design principles lets you fix the leaks.

Knowledge of the layer below always helps. Not because you need to operate at that layer full-time, but because you need to be able to drop down when the abstraction fails — and it always will.

## Example

A marketing manager uses Claude to build an internal dashboard. It works beautifully for three months. Then one day the database query returns incorrect aggregations. The AI cannot fix its own bug because it does not understand the specific data model. A developer looks at it, sees a join condition that is wrong, fixes it in five minutes. The marketing manager was leveraged by the abstraction for three months and stuck when it leaked. The developer was leveraged for three months and briefly inconvenienced when it leaked. Same tool, different outcomes, because one understood the layer below.

## Output

After applying this framework, you should be able to:

1. Identify which abstractions you are currently relying on without understanding the layer below
2. Decide which layers are worth learning (the ones where leaks would be catastrophic or frequent)
3. Use AI tools confidently while maintaining the ability to debug them
4. Prioritize learning fundamentals alongside learning tools, not instead of them

> Source: "On AI" (2026-02-ai/POLISHED.md), Naval Podcast, February 2026
