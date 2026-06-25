# The progression: prompt → context → loop → harness → verifier

Each wave is a name for whatever the current models were still bad at. As the
model or the surrounding system absorbs that weakness, the named discipline
fades and a new one forms around the next bottleneck. Tracking the arc tells you
where the leverage is *now*.

| Wave | Year(ish) | The scarce skill | What absorbed it |
| --- | --- | --- | --- |
| **Prompt engineering** | 2022–2023 | Wording the single call | Better instruction-tuned models; the "magic words" stopped mattering |
| **Context engineering** | 2024–2025 | Curating what's in the window | Longer contexts + retrieval/compaction baked into harnesses |
| **Loop engineering** | June 2026 | Designing the cycle that prompts the agent | Coding agents (Claude Code, Codex, Devin) ship the loop as a default |
| **Harness engineering** | early–mid 2026 | The environment the agent runs inside | Automated harness optimization (see below) is already beating hand-tuning |
| **Verifier engineering** | the live frontier | Defining "correct" so a machine can optimize it | *Not yet absorbed — this is where the leverage is* |
| **Self-evolving / meta-harness** | the application on top | Letting an agent improve its own scaffold | Gated entirely by the verifier beneath it |

## The origin of the loop-engineering moment

- **June 8, 2026** — Peter Steinberger (@steipete) posts: *"you shouldn't be
  prompting coding agents anymore. You should be designing loops that prompt
  your agents."* ~6.5M views; a week of timeline argument.
- **Boris Cherny** (Claude Code) reframes it: *"I don't prompt Claude anymore.
  I have loops that are running… My job is to write loops."*
- **Addy Osmani** popularizes the term and the five building blocks
  (automations, worktrees, skills, connectors, maker/checker sub-agents).
- **The pivotal reply** (@mosyaseen): *"designing the loop is half of it. the
  other half is putting something in the loop that can say no: a test, a type
  check, a real error."* ← this is the seed of verifier engineering.

## Why verifier engineering is the next floor, not just the next fad

Two structural reasons, not vibes:

1. **It's the bottleneck for the layer above.** Self-evolving agents (the buzzy
   application) optimize against a reward. No trustworthy reward → no
   self-evolution. Verification *gates* the whole upper stack.
2. **It's the most durable abstraction in the list.** Every prior wave named a
   *technique* that a better model swallowed. "Define correct precisely" is not
   a technique the model can swallow — it's the spec the model is optimized
   *against*. It moves up with capability instead of being consumed by it.

## The evidence that harness/loop tuning is already being automated

- **Meta-Harness (Lee et al., 2026):** ~76.4% on Terminal-Bench-2 via *automated*
  harness optimization — surpassing every hand-engineered harness, **frozen model
  weights.**
- **Trivedy (2026):** a fixed GPT-5.2-Codex agent went **52.8% → 66.5%** on
  Terminal-Bench 2.0 through harness changes alone (prompt restructuring,
  context middleware, self-verification hooks).
- **GEPA (ICLR 2026 oral):** reads execution traces, proposes targeted scaffold
  improvements.
- **EvoSkill / SICA / ReVeal:** synthesize reusable skills from *failed*
  trajectories; agents that edit their own codebase; evolution through reliable
  self-verification.

The pattern across all of them: **the human stops tuning the scaffold and starts
authoring the reward.** That reward is a verifier.

> Verify every figure in this file against [`sources.md`](sources.md) before
> citing it externally — these are populated from a research pass and the
> deep-research report (`REPORT.md`) carries the adversarially-checked versions.
