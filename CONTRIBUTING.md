# Contributing

This repo is a thesis + map + starter kit for verifier engineering. Contributions
that sharpen any of the three are welcome.

## Good additions

- **New runnable examples** under `examples/` — keep them dependency-free,
  deterministic, and `python3 file.py`-runnable. Each example earns its place by
  making *one* idea legible, not by being realistic.
- **Sources** — add primary sources to `docs/sources.md`. Prefer the original
  artifact (paper, thread, repo) over a secondary writeup. Flag numeric claims
  that you couldn't trace to a primary.
- **Glossary terms** — one crisp paragraph, defined against how it's actually
  used in the field.
- **Real-LLM adapters** — a thin `Maker` / harness adapter for a specific SDK,
  kept optional so the core stays dependency-free.

## House rules

1. **Verifier first.** Any example that demonstrates a loop must show the
   verifier doing real work — an executed check, not a rubber stamp.
2. **Keep the seam.** Examples must have a single, labeled place where a real
   model plugs in, and the surrounding loop/gate/search must not change when it
   does. That invariance is the point.
3. **Distrust graders in writing.** If an example uses an LLM-judge or learned
   reward, note the reward-hacking failure mode in its README.
4. **Cite or caveat.** New factual claims in docs get a `sources.md` entry or an
   explicit "unverified" tag.

## Running everything

```bash
python3 examples/verifier-loop/verifier_loop.py
python3 examples/meta-harness/meta_harness.py
```

Both should exit 0 and print a converging transcript.
