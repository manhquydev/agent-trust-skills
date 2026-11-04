# Verification First

## Build the verification path before delegating

- Give the agent a way to run the real product before giving it real work: launch the app, click, type, navigate and observe the result.

- Capture performance evidence the agent can read, such as timings, traces, screenshots and logs, and teach it where each kind lives.

- Prefer driving the real artifact over checking proxies, because compiling cleanly and self-reported success prove nothing about behavior.

## Write the feature map

- Keep a short map file of the product surface: screens, navigation paths and how to locate each element the agent must touch.

- Update the map in the same change that adds or moves a feature, and treat a stale map as a bug.

- Keep the map factual and short, so the agent reads it every run instead of skipping it.

## Require evidence with every claim

- Accept a completion claim only with its evidence attached: a screenshot, a measurement before and after, or a log excerpt.

- Separate the worker from the verifier: the agent that wrote the change never signs off its own work.

- Use a fresh agent, ideally from a different model family, to verify a merge-ready result, including live behavior and regressions.

- Void the verdict and re-verify whenever the code changes after a pass, however small the change looks.

## Prove every check can fail

- Break the build or the behavior on purpose once for each new check, and watch the check go red before trusting it.

- Record which check guards which failure, so a green run can be read as coverage rather than luck.

- Turn every escaped defect into a new check first and a postmortem second.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
