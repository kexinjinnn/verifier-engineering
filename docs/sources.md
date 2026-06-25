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

## Self-evolving / meta-harness agents (the application on top) — PRIMARY, VERIFIED

These are the adversarially-verified primary sources from the deep-research pass
(see [`../REPORT.md`](../REPORT.md)). Prefer these over the secondary writeups above.

- **Meta-Harness** (Stanford IRIS Lab; outer-loop harness search, frozen model):
  arXiv:2603.28052 — <https://arxiv.org/abs/2603.28052> ·
  artifact <https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact>
- **Agentic Harness Engineering / AHE** (Fudan/PKU/Qiji Zhifeng; falsifiable-contract
  self-evolution): arXiv:2604.25850 — <https://arxiv.org/html/2604.25850v1> ·
  code <https://github.com/china-qijizhifeng/agentic-harness-engineering>
- **GEPA** (ICLR 2026 Oral; reflective prompt evolution beats RLVR):
  arXiv:2507.19457 — <https://arxiv.org/abs/2507.19457>
- **SICA** (self-improving coding agent, edits own codebase):
  arXiv:2504.15228 — <https://arxiv.org/html/2504.15228v2> ·
  code <https://github.com/MaximeRobeyns/self_improving_coding_agent>
- **EvoSkill** (skills synthesized from failed trajectories):
  arXiv:2603.02766 — <https://arxiv.org/pdf/2603.02766> ·
  code <https://github.com/sentient-agi/EvoSkill>
- "6× harness gap" motivation (SWE-bench Mobile): arXiv:2602.09540 —
  <https://arxiv.org/abs/2602.09540>

## Verification / reward hacking (the open problem) — PRIMARY, VERIFIED

- **LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking** (ICLR 2026):
  arXiv:2604.15149 — <https://arxiv.org/abs/2604.15149> ·
  code <https://github.com/ml-research/llms-gaming-verifiers>
- **Finding Widespread Cheating on Agent Benchmarks** (METR/DebugML; 30%+ of runs):
  <https://debugml.github.io/cheating-agents/>
- **VerIF** (hybrid rule-based + reasoning-LLM-judge verifier; EMNLP 2025):
  arXiv:2506.09942 — <https://arxiv.org/pdf/2506.09942> ·
  code <https://github.com/THU-KEG/VerIF>
- **Agentic reward modeling / RewardAgent**: arXiv:2502.19328 —
  <https://arxiv.org/pdf/2502.19328>

## Benchmarks referenced

- **Terminal-Bench 2.0** — the harness-optimization results above are reported
  against this suite. Margins between top automated and hand-tuned agents are
  often small (~2 pts); confirm exact numbers against the primary PDFs.

## Caveat on sources

The **blog/X items at the top** are secondary writeups of the *naming moment*;
the discourse figures (e.g. "6.5M views") trace to those reports and are not
independently verified. Two claims were **refuted** in verification and excluded
from `REPORT.md`: a mis-stated Terminus-KIRA baseline figure, and the overreach
that VerIF frames verification as "the central role" in RLVR. An earlier
"Trivedy 52.8%→66.5%" figure also failed verification and was dropped in favor of
the primary-source AHE result. The **arXiv items** are recent (Mar–Apr 2026)
preprints, author-reported, without independent reproduction — treat each as one
strong data point, not settled fact.
