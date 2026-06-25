"""
verifier_loop.py — a minimal verifier-driven agent loop (maker/checker split).

The thesis of this repo in ~120 lines: the loop is the easy half. The hard,
scarce half is *the thing in the loop that can say "no"* — a verifier. This
file makes that split concrete and runnable with zero dependencies.

    task ──> [maker] ──> candidate ──> [verifier] ──> pass? ──> done
                ^                                       │
                └──────────── feedback ◀───── no ───────┘

Swap `MockMaker` for a real LLM by implementing the `Maker` protocol
(`propose(task, feedback) -> str`). The loop, the verifier, the budget, and the
stop condition do not change — that is the whole point.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable, Protocol


# --------------------------------------------------------------------------- #
# Verifiers: the primitive this repo argues is the real moat.                  #
# A verifier maps a candidate -> (passed, feedback). Cheap, deterministic,     #
# and adversarial where possible. Compose several into a gate.                 #
# --------------------------------------------------------------------------- #
@dataclass
class Verdict:
    passed: bool
    feedback: str
    verifier: str


Verifier = Callable[[str], Verdict]


def make_test_verifier(name: str, fn: Callable[[str], tuple[bool, str]]) -> Verifier:
    def _v(candidate: str) -> Verdict:
        ok, msg = fn(candidate)
        return Verdict(passed=ok, feedback=msg, verifier=name)
    return _v


@dataclass
class Gate:
    """A conjunction of verifiers. Fails closed: any failure stops the gate and
    returns that verifier's feedback. Order cheapest-first."""
    verifiers: list[Verifier]

    def check(self, candidate: str) -> Verdict:
        for v in self.verifiers:
            verdict = v(candidate)
            if not verdict.passed:
                return verdict
        return Verdict(passed=True, feedback="all gates passed", verifier="gate")


# --------------------------------------------------------------------------- #
# Maker: anything that proposes a candidate given a task + last feedback.      #
# --------------------------------------------------------------------------- #
class Maker(Protocol):
    def propose(self, task: str, feedback: str | None) -> str: ...


class MockMaker:
    """Deterministic stand-in for an LLM. It "learns" only from feedback,
    mimicking how a real maker uses the verifier's no to converge. Replace with
    an LLM call; the loop below is unchanged."""

    def __init__(self, attempts: list[str]):
        self._attempts = attempts
        self._i = 0

    def propose(self, task: str, feedback: str | None) -> str:
        candidate = self._attempts[min(self._i, len(self._attempts) - 1)]
        self._i += 1
        return candidate


# --------------------------------------------------------------------------- #
# The loop. ~20 lines. This is the commodity half.                            #
# --------------------------------------------------------------------------- #
@dataclass
class LoopResult:
    success: bool
    candidate: str
    iterations: int
    transcript: list[str] = field(default_factory=list)


def run_loop(task: str, maker: Maker, gate: Gate, max_iters: int = 6) -> LoopResult:
    feedback: str | None = None
    transcript: list[str] = []
    candidate = ""
    for i in range(1, max_iters + 1):
        candidate = maker.propose(task, feedback)
        verdict = gate.check(candidate)
        transcript.append(
            f"iter {i}: [{verdict.verifier}] "
            f"{'PASS' if verdict.passed else 'FAIL'} — {verdict.feedback}"
        )
        if verdict.passed:
            return LoopResult(True, candidate, i, transcript)
        feedback = verdict.feedback  # the 'no' is what makes the next try better
    return LoopResult(False, candidate, max_iters, transcript)


# --------------------------------------------------------------------------- #
# Demo: write a Python function that passes a hidden test suite.               #
# The verifier *executes* the candidate — a machine-checkable oracle, the      #
# regime where this whole paradigm works best.                                 #
# --------------------------------------------------------------------------- #
def _exec_against_tests(candidate: str) -> tuple[bool, str]:
    if not re.search(r"def\s+slugify\s*\(", candidate):
        return False, "no function named `slugify` defined"
    ns: dict = {}
    try:
        exec(candidate, ns)  # noqa: S102 — sandbox in real use; fine for a demo
    except Exception as e:  # noqa: BLE001
        return False, f"candidate raised on import: {e!r}"
    fn = ns.get("slugify")
    cases = [
        ("Hello World", "hello-world"),
        ("  Trim  Me ", "trim-me"),
        ("Café del Mar!!", "cafe-del-mar"),
    ]
    for inp, want in cases:
        try:
            got = fn(inp)
        except Exception as e:  # noqa: BLE001
            return False, f"slugify({inp!r}) raised {e!r}"
        if got != want:
            return False, f"slugify({inp!r}) == {got!r}, want {want!r}"
    return True, "3/3 cases pass"


def _demo() -> None:
    gate = Gate([make_test_verifier("unit-tests", _exec_against_tests)])

    # Three escalating attempts; only the third handles accents + trimming.
    attempts = [
        "def slugify(s):\n    return s.lower().replace(' ', '-')\n",
        "def slugify(s):\n    return s.strip().lower().replace(' ', '-')\n",
        (
            "import re, unicodedata\n"
            "def slugify(s):\n"
            "    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()\n"
            "    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')\n"
            "    return s\n"
        ),
    ]
    result = run_loop("write slugify()", MockMaker(attempts), gate)
    print("\n".join(result.transcript))
    print(f"\nresult: {'SUCCESS' if result.success else 'FAILURE'} "
          f"in {result.iterations} iterations")
    print("final candidate:\n" + result.candidate)


if __name__ == "__main__":
    _demo()
