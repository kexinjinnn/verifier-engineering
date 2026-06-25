"""
meta_harness.py — a tiny self-evolving / meta-harness optimizer.

The next step past verifier-driven loops: stop hand-tuning the harness. Let a
search process mutate the harness (here: a prompt template + config) and select
variants by their *verifier-defined reward* on held-out tasks. This is the toy
core of GEPA / EvoSkill / Meta-Harness: an evolution agent improving the
scaffold, scored by a grader — frozen "model", no weight updates.

    population ──> [mutate] ──> variants ──> [score on held-out via verifier]
         ^                                              │
         └────────────── select top-k ◀────────────────┘

The reward here is computed by the *same kind of verifier* as verifier_loop.py.
That is the link between the two examples: verifier engineering is the floor;
meta-harness optimization is what you build on top of it.

Deterministic (seeded) so it runs identically everywhere — Date/random-free by
design. Swap `apply_harness` for a real LLM call and the search loop is unchanged.
"""
from __future__ import annotations

from dataclasses import dataclass, replace


# --------------------------------------------------------------------------- #
# The "harness" being optimized. In reality: system prompt, tool descriptions, #
# retrieval config, skill set, retry policy. Here: 3 knobs that change how a    #
# fixed, dumb "model" transforms input -> output.                              #
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Harness:
    strip: bool          # trim whitespace before processing?
    lower: bool          # normalize case?
    collapse: bool       # collapse internal whitespace to single '-'?

    def key(self) -> str:
        return f"strip={int(self.strip)} lower={int(self.lower)} collapse={int(self.collapse)}"


def apply_harness(h: Harness, text: str) -> str:
    """The frozen 'model': a fixed transform whose behavior is governed entirely
    by harness config. Improving the *harness* improves the output without
    touching the model — the central finding behind Meta-Harness."""
    s = text
    if h.strip:
        s = s.strip()
    if h.lower:
        s = s.lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif h.collapse:
            if not prev_dash:
                out.append("-")
                prev_dash = True
        else:
            out.append(ch)
    return "".join(out).strip("-")


# --------------------------------------------------------------------------- #
# The verifier-defined reward. Held-out tasks with known-good answers; reward   #
# is fraction passing. This is the grader the whole search optimizes against.   #
# --------------------------------------------------------------------------- #
HELD_OUT = [
    ("Hello World", "hello-world"),
    ("  Lots   of   space  ", "lots-of-space"),
    ("MixedCASE Input", "mixedcase-input"),
    ("trailing!!", "trailing"),
]


def reward(h: Harness) -> float:
    passed = sum(1 for inp, want in HELD_OUT if apply_harness(h, inp) == want)
    return passed / len(HELD_OUT)


# --------------------------------------------------------------------------- #
# The evolution loop: enumerate/mutate harness variants, keep the best by       #
# reward. Tiny config space, so we do exhaustive search; the *shape* is what     #
# matters — mutate, score-by-verifier, select. Scale this and it's GEPA.        #
# --------------------------------------------------------------------------- #
def neighbors(h: Harness) -> list[Harness]:
    return [
        replace(h, strip=not h.strip),
        replace(h, lower=not h.lower),
        replace(h, collapse=not h.collapse),
    ]


def optimize(start: Harness, steps: int = 8) -> tuple[Harness, float, list[str]]:
    best, best_r = start, reward(start)
    log = [f"baseline   {start.key()}  reward={best_r:.2f}"]
    seen = {start.key()}
    for _ in range(steps):
        improved = False
        for cand in neighbors(best):
            if cand.key() in seen:
                continue
            seen.add(cand.key())
            r = reward(cand)
            log.append(f"  try      {cand.key()}  reward={r:.2f}")
            if r > best_r:
                best, best_r, improved = cand, r, True
        if not improved:
            break
        log.append(f"  -> keep  {best.key()}  reward={best_r:.2f}")
    return best, best_r, log


def _demo() -> None:
    # A deliberately bad hand-tuned baseline: no normalization at all.
    baseline = Harness(strip=False, lower=False, collapse=False)
    best, best_r, log = optimize(baseline)
    print("\n".join(log))
    print(f"\nhand-tuned baseline reward: {reward(baseline):.2f}")
    print(f"auto-optimized harness:     {best.key()}  reward={best_r:.2f}")
    print(
        "\ntakeaway: the search beat the fixed baseline by changing the harness "
        "alone —\nno change to the underlying 'model'. That is the Meta-Harness result "
        "in miniature."
    )


if __name__ == "__main__":
    _demo()
