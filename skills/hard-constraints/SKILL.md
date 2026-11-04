---
name: hard-constraints
description: Convert repeated agent mistakes and reminders into hard enforcement, ranked from style guides through lint and CI to architecture, so the shortest path is the best path. Use when the same error recurs, when guidance keeps being ignored, or when designing a codebase for agents.
license: MIT
metadata:
  author: manhquydev
  version: "1.0.0"
  source: Distilled from Lauren Tan's public talks and the pstack project
---

# Hard Constraints

## Know the five layers

- Rank every rule by the layer that enforces it, from softest to hardest: style guide, skills, machine-readable rules, lint and CI, and architecture.

- Expect soft layers to be forgotten under pressure, and never let an important rule live only in prose.

- Ask of every repeated error: how do I turn this into a lint rule, and how do I turn this into a CI failure.

## Make the shortest path the best path

- Design the codebase assuming the agent always takes the shortest path, then make that path the correct one.

- Give each durable value a single owner that writes it, and forbid writes from anywhere else.

- Add new behavior as new isolated files instead of branches inside shared files, so the easy edit is also the clean edit.

- Fail automatically on banned dependencies and banned patterns, with an error message that names the allowed alternative.

## Ban what agents are bad at

- Ban constructs with a known failure record in your stack, at CI level, the way useEffect is banned outright in the Dune codebase for being a recurring footgun.

- Consider banning code comments when agents use them to narrate history or shift blame, and require the reasoning to live in the decision log instead.

- Keep every ban small, explicit and reviewed, and record the incident that earned each one.

## Handle exceptions without weakening the wall

- Route a genuine exception through a small, visible, reviewed escape hatch rather than a quiet workaround.

- Expire exceptions by default, and re-justify them on renewal.

- Count how often each constraint fires, and investigate the constraint rather than the agent when one fires constantly.

## Related skills

- [Verification First](../verification-first/SKILL.md)

- [Skill Evals](../skill-evals/SKILL.md)

- [Bot Team Design](../bot-team-design/SKILL.md)
