# Verifier Engineering

> **The floor under self-evolving agents.** Prompt → context → loop → harness engineering each got absorbed by the system once it was named. The skill that *doesn't* get absorbed — and that every layer above depends on — is defining "correct" precisely and cheaply enough that a machine can optimize against it. That is verifier engineering.

This repo is a thesis, a map, and a runnable starter kit for what comes **after loop engineering**.

---

## The one-paragraph argument

In June 2026, "loop engineering" went viral: *stop prompting agents, design loops that prompt them.* True, but the loop is the easy half. The most-upvoted reply to the thread that started it said the quiet part out loud — *"designing the loop is half of it. the other half is putting something in the loop that can say no."* That "something" is a **verifier**. Once everyone has loops, the loop commoditizes and the differentiator becomes the quality of the grader. And the moment you can grade cheaply, you can *search* — which is why the frontier work (GEPA, EvoSkill, Meta-Harness) is **agents that optimize their own harness against a verifier**, beating hand-tuned scaffolds with frozen model weights. Verifier engineering is the bottleneck that gates all of it.

## The layer cake

```
              ┌─────────────────────────────────────────────┐
   the app    │  SELF-EVOLVING / META-HARNESS                │   agents that rewrite
              │  agent mutates its own prompt/skills/config  │   their own scaffold
              ├─────────────────────────────────────────────┤
              │  LOOP ENGINEERING                            │   design the cycle that
   commodity  │  task → generate → check → retry            │   prompts the agent
              ├─────────────────────────────────────────────┤
              │  HARNESS ENGINEERING                         │   the environment the
              │  tools, memory, permissions, observability   │   agent runs inside
              ╞═════════════════════════════════════════════╡
  THE FLOOR   │  VERIFIER ENGINEERING                        │ ◀ the scarce primitive:
  (this repo) │  define "correct" so a machine can optimize  │   everything above
              │  it — tests, evals, judges, reward models    │   depends on this
              └─────────────────────────────────────────────┘
```

> **A note on naming, from the research.** The buzzword most likely to *stick* is
> "harness engineering" / "meta-harness optimization" — that's the layer where
> automation just beat expert humans on benchmarks ([`REPORT.md` §2](REPORT.md)).
> "Verifier engineering" is not the front-running *label*; it's the durable
> *lever* underneath every one of those systems. This repo is named for the lever
> on purpose: labels churn, the skill of authoring trustworthy graders doesn't.

Read it bottom-up: **self-evolution is downstream of verification.** A self-improving agent can only climb a gradient you can measure. Where verification is cheap and trustworthy (code, math, proofs) the whole stack works. Where it's fuzzy (taste, product judgment, "is this what the user meant") the stack stalls and humans snap back into the loop. **That's the real frontier-after-the-frontier.**

## What's in here

| Path | What it is |
| --- | --- |
| [`REPORT.md`](REPORT.md) | **Deep-research report** (25 sources, 23 adversarially-verified claims): trend-name candidates, the benchmark evidence, primary papers, and a late-2026→2027 forecast. |
| [`docs/progression.md`](docs/progression.md) | The prompt → context → loop → harness → verifier arc, with who coined what and when. |
| [`docs/glossary.md`](docs/glossary.md) | Verifier, gate, reward model, maker/checker, meta-harness, reward hacking, LLM-judge — defined. |
| [`docs/sources.md`](docs/sources.md) | Primary sources: the viral threads, the repos, the benchmark papers. |
| [`examples/verifier-loop/`](examples/verifier-loop/) | **Runnable.** A maker/checker loop. The verifier *executes* candidates against a test oracle. The loop is ~20 lines; the verifier is the point. |
| [`examples/meta-harness/`](examples/meta-harness/) | **Runnable.** A tiny self-evolving optimizer: mutate the harness, score by verifier-defined reward, keep the best. Beats a fixed baseline with no "model" change. |

## Run it (zero dependencies, Python 3.10+)

```bash
python3 examples/verifier-loop/verifier_loop.py   # loop converges once a gate says "no"
python3 examples/meta-harness/meta_harness.py     # harness search: reward 0.00 → 1.00
```

Both examples are deterministic and dependency-free so they run identically anywhere. Each has a single seam — `Maker.propose()` / `apply_harness()` — where you drop in a real LLM. **The loop, the gate, the budget, and the search do not change when you do.** That invariance is the thesis in code.

## The five practices of verifier engineering

1. **Write the verifier before the prompt.** Pin "done" up front: a test, a type check, a schema, a rubric. If you can't state the check, you don't yet have a task — you have a vibe.
2. **Split maker from checker.** Different instructions, ideally a different model. The checker's job is to *prove the maker wrong*, not to agree.
3. **Make the "no" informative.** A verifier that only returns `False` wastes the loop. Return the *reason* — that feedback is what makes the next attempt better (see `verifier_loop.py`).
4. **Treat evals as infrastructure, not a notebook.** Verifiers belong in CI as first-class gates, versioned and regression-tracked — not run by hand.
5. **Distrust your own grader.** Reward models get gamed; LLM-judges have biases. Adversarially probe the verifier itself. An optimizer will find every hole you leave.

## Where this goes (the open problem)

Everything above is solved for **machine-checkable** domains. The wave *after* this one belongs to whoever makes verification cheap and **gaming-resistant for fuzzy domains** — trustworthy LLM-judges, reward models that don't collapse under optimization pressure. That's the research bet `REPORT.md` argues for.

---

*Scaffolded from a live research pass on the post-loop-engineering trend. See [`docs/sources.md`](docs/sources.md) for citations and [`CONTRIBUTING.md`](CONTRIBUTING.md) to add patterns.*
