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

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
