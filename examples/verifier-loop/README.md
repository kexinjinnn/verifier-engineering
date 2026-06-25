# Example: verifier-driven loop (maker / checker)

The thesis in ~120 lines: **the loop is the commodity; the verifier is the moat.**

```bash
python3 verifier_loop.py
```

## What it shows

A maker proposes a `slugify()` implementation; a verifier *executes* it against a
hidden test oracle and returns a precise reason on failure. The loop feeds that
reason back, and the maker converges in 3 iterations:

```
iter 1: [unit-tests] FAIL — slugify('  Trim  Me ') == '--trim--me-', want 'trim-me'
iter 2: [unit-tests] FAIL — slugify('  Trim  Me ') == 'trim--me', want 'trim-me'
iter 3: [gate] PASS — all gates passed
```

## The parts that matter

- **`Verifier` / `Gate`** — the primitive. A gate is a conjunction of verifiers,
  cheapest-first, failing closed with the *reason*. Everything else is plumbing.
- **`run_loop`** — ~20 lines. Deliberately boring. This is the half that
  commoditized.
- **The feedback channel** — `verdict.feedback` becomes the maker's next input.
  A verifier that only returned `True/False` would waste the loop. **Make the
  "no" informative.**

## The seam for a real LLM

Replace `MockMaker` with anything implementing `propose(task, feedback) -> str`:

```python
class LLMMaker:
    def propose(self, task, feedback):
        msg = task if feedback is None else f"{task}\n\nLast attempt failed: {feedback}"
        return call_your_model(msg)   # Anthropic / OpenAI / local — your choice

run_loop(task, LLMMaker(), gate)      # loop, gate, budget: unchanged
```

The invariance is the lesson: swapping in a frontier model changes the maker and
nothing else. Your engineering effort lives in the gate.

## Extend it

- Add an **adversarial second verifier** (a critic LLM prompted to refute the
  candidate) to the gate — maker/checker with a real checker.
- Make a verifier **non-deterministic** (an LLM-judge) and watch reward-hacking
  appear — the bridge to the open problem in the top-level README.
