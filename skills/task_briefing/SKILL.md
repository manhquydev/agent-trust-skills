# Task Briefing for Agents

## Write the five-part brief

- State the goal in one or two sentences, in terms of the outcome rather than the activity.

- Define done as criteria that can be judged pass or fail, in countable terms wherever possible: zero old callers remain, all fixtures pass, the export shows every row.

- Name the evidence the agent must present: the measurement before and after, the screenshot, the failing job id, the log excerpt.

- Include the clues already known, such as when the problem started and which deploy it followed.

- List the constraints that bound the work, such as files not to touch and behaviors that must not change.

## Leave the method open

- Omit your step-by-step method, because prescribing it imports your blind spots into the agent's run.

- Omit your guess at the cause, because a stated diagnosis anchors the investigation and hides the real one.

- Model the pattern on this shape: "the export drops its last row since yesterday's deploy, failing job id is 4812, reproduce first then fix, done means the 60k-row fixture exports every row, show me the row counts before and after."

## Check understanding before work starts

- Have the agent restate the task in its own words, and correct the restatement rather than the work when it drifts.

- Prefer a voice brain dump for rich context, then the same restatement check, when typing the brief would lose detail.

- Write the brief down as a document before code when the task is large, so the agent can re-read it mid-run.

## Prototype instead of planning in the abstract

- Settle design questions with two or three small prototypes behind a toggle, then choose by measured results.

- Refuse abstract plan review loops, because an agent asked to critique a plan invents theoretical risks instead of evidence.

- Remember the rule behind this: the best spec is code.

## Fix the workflow per task type

- Run bug work as reproduce first, then narrow, then fix.

- Run feature work as data structure first, then behavior.

- Run refactors as record current output, then change, then prove the output is unchanged.

- Run performance work as baseline measurement first, and report only in before and after numbers.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
