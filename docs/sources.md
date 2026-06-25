# Sources

Primary sources behind the thesis, grouped by claim. The deep-research report
(`REPORT.md`) carries the adversarially-verified subset; this is the fuller
working bibliography. Dates and figures should be re-checked against the
originals before external citation.

## The loop-engineering moment (the trigger)

- Peter Steinberger (@steipete), origin post — via Yahoo Tech:
  <https://tech.yahoo.com/ai/claude/articles/forget-prompt-engineering-loop-engineering-090101184.html>
- Boris Cherny, "my job is to write loops" — MindStudio:
  <https://www.mindstudio.ai/blog/what-is-loop-engineering-ai-coding-agents>
- Addy Osmani, "Loop Engineering": <https://addyosmani.com/blog/loop-engineering/>
- LangChain, "The Art of Loop Engineering":
  <https://www.langchain.com/blog/the-art-of-loop-engineering>
- The Register (skeptic's view), "still needs humans in the loop":
  <https://www.theregister.com/ai-and-ml/2026/06/24/loop-engineering-latest-ai-buzzword-still-needs-humans-in-the-loop/>
- The @mosyaseen "something that can say no" reply, reported in Firecrawl's
  writeup: <https://www.firecrawl.dev/blog/loop-engineering>

## Harness engineering (the layer below)

- Faros, "Harness Engineering — the harness, not the model, determines
  performance": <https://www.faros.ai/blog/harness-engineering>
- Addy Osmani, "Agent Harness Engineering":
  <https://addyosmani.com/blog/agent-harness-engineering/>
- `ai-boost/awesome-harness-engineering` (12 design primitives; frontiers list):
  <https://github.com/ai-boost/awesome-harness-engineering>
- Agent Harness Engineering: A Survey:
  <https://picrew.github.io/LLM-Harness/main.pdf>

## Verifier / verification-first design (the floor — this repo)

- "stop perfecting prompts, start writing verifiers" framing — Firecrawl:
  <https://www.firecrawl.dev/blog/loop-engineering>
- `cobusgreyling/loop-engineering` (maker/checker split, verifier sub-agent):
  <https://github.com/cobusgreyling/loop-engineering>
- `serenakeyitan/awesome-agent-loops` (X-sourced /loop commands):
  <https://github.com/serenakeyitan/awesome-agent-loops>

## Self-evolving / meta-harness agents (the application on top)

- Meta-Harness (Lee et al., 2026) & Trivedy (2026) harness-optimization
  benchmark results, collected in the self-evolving-agents survey:
  <https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents>
- "A Survey of Self-Evolving Agents" (what/when/how/where to evolve):
  <https://arxiv.org/pdf/2507.21046>
- GEPA / Hermes self-evolution (ICLR 2026 oral; DSPy + GEPA):
  <https://github.com/NousResearch/hermes-agent-self-evolution>
- EvoSkill (skills synthesized from failed trajectories):
  <https://github.com/sentient-agi/EvoSkill>
- AgentFactory (self-evolving via subagent accumulation):
  <https://arxiv.org/pdf/2603.18000>
- DARWIN (dynamic agentically-rewriting self-improving network):
  <https://arxiv.org/pdf/2602.05848>

## Benchmarks referenced

- Terminal-Bench 2.0 / Terminal-Bench-2 — the harness-optimization results above
  are reported against this suite. Verify exact numbers against the primary
  papers before citing.

## Caveat on sources

Several of the above are secondary writeups (blogs, vendor posts) reporting on
X threads and papers. The numeric claims (6.5M views, 76.4%, 52.8%→66.5%) trace
to those secondary reports and should be confirmed against primary artifacts —
the deep-research pass exists precisely to separate the verified from the
plausible.
