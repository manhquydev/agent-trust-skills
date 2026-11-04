# Skill Evals

## Treat every skill as code under test

- Write an evaluation for each skill you rely on, because an untested skill is a promise rather than an asset.

- Build each case from a real past task: the input, the constraints and the result a good run must produce.

- Store cases with neutral names and neutral folder labels, so the agent cannot tell it is being tested and perform for the test.

## Score with an independent judge

- Set a written rubric per case before running anything: what counts as pass, what counts as partial and what evidence the run must show.

- Run each case in an isolated context, so one case cannot borrow answers from another.

- Have a judge from a different model family score the runs against the rubric, and read the disagreements yourself.

- Loop on the skill, not on the case: edit the skill, rerun the full set and keep looping until the score is perfect across the set.

## Maintain skills from real failures

- Watch real runs the way you would pair with a colleague: which tools get called, where the agent stalls and where it quietly guesses.

- Convert every real failure into a new eval case before fixing the skill, so the failure stays covered after the fix.

- Re-run the eval set on a schedule and after any model change, because a skill that passed last month can rot silently.

- Retire or rewrite a skill whose eval score drops twice in a row instead of patching it a third time.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
