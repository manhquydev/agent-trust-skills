# Bot Team Design

## Split the outer loop from the inner loop

- Give the outer loop the signals and the judgment: gather bug reports, complaints and feature ideas from every channel, decide what is worth doing and keep the reason attached to each task.

- Give the inner loop the execution: a repository, a problem, acceptance criteria and required evidence in, a reviewable result out.

- Keep the reason with the task at every handoff, because a worker that knows why a task exists makes better local decisions.

## Assign one owner per task

- Give every task and every pull request exactly one owning bot, and route questions about it to that owner.

- Let a coordinator break work down and delegate rather than execute, once the team passes a handful of bots.

- Run parallel attempts on the same task only as a deliberate pattern: independent slices, or competing attempts whose reports merge with evidence and unresolved gaps listed.

## Protect the verdict

- Verify a merge-ready result with a fresh verifier, including live behavior and regressions.

- Void any pass verdict the moment the underlying code changes, and re-verify from the verdict step.

- Allow auto-merge only when that permission was granted explicitly in advance and the verification gate has passed.

## Keep few, sharp bots

- Prefer a small team of excellent bots over a crowd of vague ones, and use a designer bot to draft new bots against a written pattern.

- Write each bot's job as one job, one voice, plus an explicit anti-job list of things it must never do and tools it must not hold.

- Onboard each bot like an intern: supervised runs first, skills saved from its corrected work, autonomy widened on evidence.

- Turn repeated multi-step bot work into plain scripts where possible, because code is cheaper than a bot reasoning through the same steps every time.

## Respect the shared machine

- Design permissions for where files and credentials actually live, because bots on one account commonly share one cloud computer and one credential vault.

- Never treat a role split between bots as a security boundary, and keep high-risk credentials out of shared scope entirely.

- Give each bot its own email and service accounts where the platform allows, so its actions stay attributable and separable.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
