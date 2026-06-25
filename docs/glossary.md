# Glossary

**Verifier** — A function `candidate → (passed, feedback)` that decides whether
an output meets a criterion. The scarce primitive of this repo. Best when cheap,
deterministic, and adversarial. Examples: a unit-test runner, a type checker, a
schema validator, a rubric-scoring LLM-judge.

**Gate** — A composition of verifiers (usually a conjunction) that an output
must clear. Fails closed: any single failure stops the gate and returns that
verifier's reason. Order cheapest-first. See `examples/verifier-loop/`.

**Oracle** — A source of ground-truth "correct" for a task: a hidden test suite,
a reference solution, a formal proof checker. Cheap oracles are what make a
domain *machine-checkable* — the regime where the whole paradigm works.

**Maker / Checker (a.k.a. generator/critic, writer/verifier)** — The split where
one agent proposes and a *separate* agent (different instructions, ideally a
different model) tries to prove it wrong. The checker's job is refutation, not
agreement.

**Loop engineering** — Designing the cycle (generate → check → retry → stop)
that drives an agent toward a goal, instead of hand-prompting each step. Viral
June 2026.

**Harness** — Everything around the model that turns it into an agent: system
prompt, tool definitions, memory, retrieval, permissions, retry policy,
observability. "The harness, not the model, determines production performance."

**Harness engineering** — Hand-designing that environment. Increasingly being
automated (see *meta-harness*).

**Meta-harness / self-evolving agent** — A search process that mutates the
harness (prompts, skills, config) and selects variants by a verifier-defined
reward — improving the scaffold with *frozen model weights*. GEPA, EvoSkill,
Meta-Harness, SICA, DARWIN, AgentFactory. The toy core is in
`examples/meta-harness/`.

**Reward (function)** — The scalar a self-evolving system maximizes, computed by
a verifier over held-out tasks. Authoring this well *is* verifier engineering.

**Reward model** — A learned approximation of human preference used as a
stand-in verifier when no cheap oracle exists. Powerful but gameable.

**Reward hacking / Goodharting** — When an optimizer finds outputs that score
high on the verifier without being actually good — exploiting holes in the
grader. The central risk: an optimizer will find *every* hole you leave. Why
practice #5 is "distrust your own grader."

**LLM-judge** — Using an LLM to score outputs against a rubric. The main hope
for verifying *fuzzy* domains, and the main liability: judges carry position
bias, verbosity bias, and self-preference. Trustworthy, gaming-resistant judges
are the open problem this repo points at.

**Verifiable reward (RLVR-style)** — A reward computed from a checkable signal
(tests pass, proof checks, exact-match) rather than a learned model. The gold
standard where available; the reason code/math/proofs lead the self-evolution
work.

**Eval-as-infrastructure** — Treating verifiers as versioned, first-class CI/CD
gates with regression tracking — not as a notebook you run by hand.

**Machine-checkable vs. fuzzy domains** — Machine-checkable: a cheap oracle
exists (code, math, formal proofs). Fuzzy: correctness is a matter of judgment
(taste, strategy, product fit). The stack works in the former and stalls in the
latter — the fault line the whole forecast turns on.
