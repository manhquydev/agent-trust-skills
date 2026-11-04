---
name: measure-agent-roi
description: Measure whether an AI agent setup pays off by treating tokens as investment, front-loading spend on verification, skills and refactors, and tracking the manual-fix rate and accepted outcomes instead of task counts. Use when budgeting agent spend or reporting on agent productivity.
license: MIT
metadata:
  author: manhquydev
  version: "1.0.0"
  source: Distilled from Lauren Tan's public talks and the pstack project
---

# Measure Agent ROI

## Treat tokens as investment capital

- Spend tokens up front on the assets that compound: verification tooling, skills with evals, and refactors that make the codebase easy for agents.

- Compare token spend against the human cost of the same work, including coordination cost, rather than against zero.

- Expect the setup phase to look expensive, and judge it on the months after rather than the first week.

## Track the manual-fix rate

- Count how often a human has to correct, redo or rescue agent work, per week, as the headline health metric.

- Invest the next token budget wherever the manual-fix rate concentrates.

- Stop and find the missing layer when the rate stays flat after an investment, instead of spending more on the same setup.

- Remember that a flat rate usually means a missing verification path, a missing eval or a soft rule that should have been a hard constraint.

## Measure accepted outcomes, not activity

- Count accepted fixes, review time, rework volume, escaped defects and cost per accepted change.

- Refuse pull request counts and task counts as success metrics, because they measure motion rather than results and can overlap or inflate.

- Treat any headline output number, including your own, as self-reported until an independent count at the repository level confirms it.

## Right-size the effort

- Skip the fleet and the biggest model when a constrained codebase lets a smaller model do the work well, because good constraints buy more than raw capability.

- Start a new adopter on one agent, local, watched, before any discussion of scale or spend.

- Write your cost and outcome numbers down weekly, so the investment case rests on your ledger rather than on anyone's public claims.

## Related skills

- [Build Agent Trust](../build-agent-trust/SKILL.md)

- [Skill Evals](../skill-evals/SKILL.md)
