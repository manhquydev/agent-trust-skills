---
name: autonomous-runs
description: Run an AI agent unattended with a verifiable end condition, an isolated worktree, a one-line-per-decision log and an explicit stuck exit. Use for overnight runs, long loops and any work that proceeds without check-ins.
license: MIT
metadata:
  author: manhquydev
  version: "1.0.0"
  source: Distilled from Lauren Tan's public talks and the pstack project
---

# Autonomous Runs

## Check the three preconditions

- Start an unattended run only when the end condition is verifiable by the agent itself, in countable terms.

- Isolate the workspace before the run: a fresh worktree or branch that cannot damage shared state while nobody watches.

- Require a decision log for the run, one line per decision with time, decision, reason, evidence and result.

- Hold the run when any precondition fails, and say which one is missing instead of starting hopefully.

## Write the run instruction

- Name the task and define done in the instruction itself, the way a night instruction reads: migrate every caller to the new parser in a fresh worktree, done means zero old callers, all fixtures pass and the old API deleted.

- State the commit policy explicitly, such as do not ask before committing, when the run is meant to proceed without check-ins.

- Give an explicit exit: if truly stuck after a few hours, stop and write up why, with the evidence gathered so far.

- Set the loop to continue until the end condition verifies, not until a time budget feels long enough.

## Review the morning after

- Read the decision log first and the diff second, so judgment calls get reviewed before line-level detail.

- Verify the end condition yourself on the real artifact before accepting the run.

- Convert every surprising decision into a skill update, a new check or a new constraint before the next run.

- Track how often the exit fires, because a run that often ends stuck is a briefing or constraints problem, not an agent problem.

## Related skills

- [Task Briefing for Agents](../task-briefing/SKILL.md)

- [Build Agent Trust](../build-agent-trust/SKILL.md)

- [Bot Team Design](../bot-team-design/SKILL.md)
