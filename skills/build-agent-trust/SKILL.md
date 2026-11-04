---
name: build-agent-trust
description: Earn autonomy for an AI coding agent in stages, promoting it only on verified evidence and splitting work by reversibility. Use when setting up a new agent collaboration, widening an agent's permissions, or diagnosing why an agent setup feels untrustworthy or bottlenecked on human review.
license: MIT
metadata:
  author: manhquydev
  version: "1.0.0"
  source: Distilled from Lauren Tan's public talks and the pstack project
---

# Build Agent Trust

## Start as the verifier

- Take the verifier role from day one: design the environment, equip the agent, and judge evidence instead of hovering over every action or rubber-stamping output.

- Expect low output while trust is unbuilt, and treat that phase as construction rather than failure.

- Name the failure mode out loud when it appears: if the human reviews every keystroke, the human is the bottleneck.

## Climb the trust ladder in order

- Start the agent on your own machine, where you can watch full tasks and see which tools it calls, where it stalls and what it misunderstands.

- Grant autonomy one rung at a time: watched runs, then unwatched runs with evidence review, then unattended runs, then self-merging work.

- Require evidence for every promotion: a run history with checks passing and no escaped defects at the current rung.

- Demote a rung after any escaped defect, and write down which missing check allowed it.

- Refuse to scale to many parallel agents before the single-agent loop is trusted, because untrusted scale only burns tokens faster.

## Split work by reversibility

- Let the agent run reversible work autonomously and report afterwards.

- Stop and ask the user before irreversible work, such as pushing to a shared branch, deploying, deleting data or contacting customers.

- Answer questions with an experiment whenever an experiment can answer them, instead of escalating to the user.

- Accept "this should not be done" as a valid agent conclusion, and reward the evidence behind it.

## Review decisions, not output

- Keep a decision log with one line per decision: time, decision, reason, evidence and result.

- Review the decision log at the end of each unattended period instead of re-reading the whole body of work.

- Ask a different model to read the log and flag entries that need attention when volume grows.

- Feed every flagged decision back into a skill, a check or a constraint so the same judgment is not needed twice.

## Related skills

- [Verification First](../verification-first/SKILL.md)

- [Autonomous Runs](../autonomous-runs/SKILL.md)

- [Measure Agent ROI](../measure-agent-roi/SKILL.md)
