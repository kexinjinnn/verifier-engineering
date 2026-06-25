# Example: meta-harness optimizer (self-evolving, in miniature)

The layer above the verifier loop: **stop hand-tuning the harness — search it.**

```bash
python3 meta_harness.py
```

## What it shows

A fixed, dumb "model" transforms text into a slug. Its behavior is governed
entirely by a 3-knob **harness** (`strip`, `lower`, `collapse`). Starting from a
deliberately bad hand-tuned baseline, an evolution loop mutates the harness and
keeps whatever scores higher on a **verifier-defined reward** over held-out
tasks:

```
baseline   strip=0 lower=0 collapse=0  reward=0.00
  ...
auto-optimized harness:     strip=0 lower=1 collapse=1  reward=1.00
```

**Reward 0.00 → 1.00 by changing the harness alone — no change to the "model."**
That is the Meta-Harness / GEPA result reduced to something you can read in one
sitting.

## Why this is the same idea as the big papers

| This demo | The real systems |
| --- | --- |
| 3 boolean knobs | system prompt, tool descriptions, skills, retrieval, retry policy |
| exhaustive neighbor search | GEPA trace-guided proposals; EvoSkill skill mutation; evolutionary search |
| `reward()` over 4 held-out cases | a verifier suite / benchmark (e.g. Terminal-Bench-2) |
| frozen `apply_harness` | frozen model weights |

Scale the config space and the search, keep the shape — **mutate, score-by-verifier,
select** — and you have a self-evolving agent.

## The dependency that names this repo

`reward()` is just a verifier over held-out tasks. **The optimizer is only as
good as that reward.** Make it a sloppy LLM-judge and the search will happily
find harnesses that score well and behave badly — reward hacking. That is why
verifier engineering is the *floor*: self-evolution can't rise above the quality
of the grader beneath it.

## The seam for a real system

Swap `apply_harness(h, text)` for "run the agent under config `h` on the task,"
and `reward(h)` for "score the agent's trajectories with your verifier suite."
The `optimize()` loop is unchanged.
