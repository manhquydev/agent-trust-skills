# The Agent Trust Playbook

How to set up trust in an AI coding agent from zero, and how to keep optimizing the collaboration. Distilled from Lauren Tan's public talks and her open-source pstack, generalized for any codebase and any agent harness.

## The mindset

The operator's job is not to write every line and not to rubber-stamp output. It is the head chef's job: design the kitchen, equip the stations, train the cooks, taste before serving. The operator is the verifier. The most common failure at the start is the opposite setup, hovering over every agent action until the human becomes the bottleneck. Tan's own first month produced almost nothing for exactly that reason.

## The ladder

### Rung 1. Start local, where you can observe

Run the agent on your own machine first and watch several full tasks the way you would pair with a new colleague. Note which tools it calls, where it stalls and what it misunderstands. Resist opening fleets of cloud agents at this stage. Untrusted scale only burns tokens faster.

### Rung 2. Build verification before real delegation

Give the agent a way to run the real product and see the result: open the app, click, type, take screenshots, measure performance, read logs. Add a feature map, a short file describing screens, navigation and how to locate elements. Require evidence with every completion claim. A check that has never been seen failing on a deliberately broken build proves nothing, so break the build once on purpose for every new check.

### Rung 3. Package know-how into skills, then eval the skills

Every time the agent repeats a mistake, write the correct procedure down as a skill instead of fixing the instance by hand. Then treat the skill like code: build evaluation cases with expected results, run them in isolation, have a different model judge the outcomes, and loop on the skill until the score is perfect. Keep case names neutral so the agent does not perform for the test. Maintain skills continuously by watching real failures.

### Rung 4. Convert repeated reminders into hard constraints

When the same error appears a second time, do not remind a third time. Move it down a layer, from soft to hard: style guide, then skills, then machine-readable rules, then lint, compiler and CI, then architecture that makes the wrong way impossible to express. Agents take the shortest path, so design the codebase until the shortest path is the best path. One red error line with a fix hint is worth ten lines of guidance, because guidance can be forgotten and CI cannot.

### Rung 5. Brief tasks like a verifier

A good brief has five parts: the goal, done criteria that can be judged pass or fail, the evidence required, the clues already known, and the constraints. Leave out the method, and leave out your own guess at the cause, because both narrow the agent's investigation. Have the agent restate the task in its own words before it starts, so misunderstandings surface immediately. Settle design questions with two or three prototypes behind a toggle and pick by measurement. The best spec is code.

### Rung 6. Widen permissions by evidence, log decisions in one line

Split work by reversibility. Reversible work runs autonomously and is reported afterwards. Irreversible work, such as pushing to a shared branch, deploying, deleting data or contacting customers, stops and asks. Any question an experiment can answer should be answered by an experiment, not by a human. Log each decision in a single line: time, decision, reason, evidence, result. Review the decisions, not the raw work. That is how one operator supervises a large volume.

Unattended runs unlock only when three conditions hold: the end condition is verifiable, the workspace is isolated, and the decision log is complete. A well-formed overnight instruction names the task, defines done in countable terms, forbids asking before committing, and gives an explicit exit: if truly stuck after a few hours, stop and write up why.

### Rung 7. Scale to cloud and a bot team

Split the system into an outer loop that gathers signals, decides what is worth doing and keeps the reason for each task, and an inner loop that executes inside the repository and returns reviewable results with evidence. Give every task exactly one owner. Any change after a pass verdict voids the verdict and triggers a re-check. Auto-merge only when that permission was granted explicitly in advance and the verification gate has passed. Keep few bots, each with one job and an explicit list of anti-jobs, the things it must not do.

One security warning from the platform documentation: bots on the same account commonly share one cloud computer and one credential vault. Splitting roles between bots does not create a security boundary. Design permissions for where files and credentials actually live, not for the org chart.

### Rung 8. Treat tokens as investment, measure accepted outcomes

Spend tokens up front on the assets that compound: verification tooling, skills with evals, and refactors that make the codebase easy for agents. Track the manual-fix rate, the number of times a human has to correct the agent. If that rate does not fall after an investment, a layer is missing. Stop and find it instead of spending more. Measure accepted fixes, review time, rework, escaped defects and cost per accepted change. Never measure pull request counts or task counts. Those are activity, not outcomes.

Set expectations honestly. Reaching the point where agents merge while the operator sleeps took Tan roughly five months of building trust and constraints. This is a construction project measured in months, not an afternoon of installation.
