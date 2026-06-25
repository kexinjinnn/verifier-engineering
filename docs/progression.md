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

*All figures below are the adversarially-verified versions from [`REPORT.md`](../REPORT.md);
each traces to a primary arXiv source in [`sources.md`](sources.md).*

- **Meta-Harness (Stanford IRIS Lab — arXiv:2603.28052):** an outer-loop agent
  (Claude Code + Opus-4.6) searches over *harness code* around a **frozen** base
  model. **76.4% on Terminal-Bench 2.0 (Opus 4.6)**, beating hand-engineered
  Terminus-KIRA (74.7%); **#1 among Haiku 4.5 agents (37.6%)**; beats the SOTA
  context system ACE by **7.7 pts with 4× fewer tokens**. *(Ranks #2 overall on
  Opus 4.6 behind ForgeCode 81.8% — automated ≠ unbeatable.)*
- **Agentic Harness Engineering / AHE (arXiv:2604.25850):** independent
  corroboration — **Terminal-Bench 2 pass@1 69.7% → 77.0%** over 10 self-evolution
  iterations on GPT-5.4, beating human-designed Codex-CLI (71.9%). Each edit is a
  **"falsifiable contract"**; ablation shows *prompt-only* self-evolution actually
  **regresses (−2.3 pp)** while structural harness edits pay (+3–6 pp).
- **GEPA (ICLR 2026 Oral — arXiv:2507.19457):** reflective prompt evolution beats
  RLVR (GRPO) by **6% avg / up to 20% with 35× fewer rollouts**, and the
  prompt-optimizer MIPROv2 by **>10%**.
- **SICA (arXiv:2504.15228):** an agent editing its own full Python codebase —
  SWE-Bench Verified **17% → 53%** (50-task subset).
- **EvoSkill (arXiv:2603.02766):** synthesizes reusable skills from *failed*
  trajectories; model frozen, Pareto-selected on validation.

The pattern across all of them: **the human stops tuning the scaffold and starts
authoring the reward.** That reward is a verifier — and §4 of [`REPORT.md`](../REPORT.md)
shows how often it gets gamed, which is why the reward is the hard part.

> ⚠️ Earlier drafts of this file cited a "Trivedy 52.8%→66.5%" figure from a
> secondary blog; it did **not** survive verification and has been replaced by
> the primary-source AHE result above. Confirm any figure against the arXiv PDFs
> before external citation.
