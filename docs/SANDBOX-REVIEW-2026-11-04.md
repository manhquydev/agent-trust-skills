# Sandbox Review, 2026-11-04

The pack was installed into a throwaway project and exercised end to end before this review was written. This document records what was tested, the evidence, the problems found and the limits of the test.

## Test subject

A small Python project with an intentional defect: a CSV exporter that silently drops its last data row. A 6,000-row fixture and a row-count check script (`check_export.py`, exit 0 on pass, exit 1 on fail) served as the verification artifact.

## What was tested

**Discovery layer.** The official Agent Skills reference library (`skills-ref` 0.1.1) read all 8 skills: `read-properties` returned a name and full description for each, and `to-prompt` produced the standard `<available_skills>` XML with correct locations. Separately, the Muse skill search surfaced the locally installed copies on relevant queries.

**task-briefing.** A brief was written from the skill's five-part pattern: outcome goal, countable pass or fail criteria, required evidence, known clues, constraints, with no prescribed method and no asserted diagnosis. The brief was complete enough to run the whole exercise from.

**verification-first.** The row-count check was run against the unfixed code first and failed as required: 6,000 rows in, 5,999 out, exit 1. The check therefore demonstrably can fail, and the baseline numbers became the before evidence.

**autonomous-runs.** The fix ran in an isolated git worktree on its own branch, with a decision log of one line per decision. The fix itself was one line. After the fix the check passed: 6,000 in, 6,000 out, exit 0. The main checkout still failed the check afterwards, proving the isolation held.

**hard-constraints.** A guard script banning the offending slice pattern, with a fix hint in its failure message, was run against both versions: exit 1 with the red message on the original code, exit 0 on the fixed code.

**skill-evals.** A two-case mini eval for task-briefing was built with neutral case names and a six-point rubric. The skill-written brief scored 6/6. A deliberately bad brief (asserted diagnosis, prescribed method, no evidence requirement) scored 1/6, so the rubric discriminates.

**Routing inspection.** Sample intents (granting overnight auto-merge, designing a review bot team, judging token spend) were matched against the eight frontmatter descriptions by reading. Each intent maps to a distinct skill, with build-agent-trust and autonomous-runs naturally adjacent on the autonomy intent and cross-linked for that reason.

## Problems found

1. The README skill table still showed snake_case names as link text after the folder rename. Fixed in the same commit as this review.
2. The quick keyword scorer used in the mini eval passed one criterion for the bad brief spuriously, because the anti-pattern text itself contains the word "rows". Keyword scoring is weak evidence. The skill-evals method already prescribes a rubric plus an independent judge for this reason, and this sandbox run confirms why.
3. The restate step in task-briefing degenerates when the operator and the agent are the same party, as in this self-run. The step is designed for a human delegating to an agent and could not be exercised meaningfully here.

## Limits of this test

No independent agent executed the skills. The Codex CLI is installed on the test machine but not logged in, so a cross-model live run, including a different-model judge for the eval, remains untested. The procedures were executed by the pack author's own agent, strictly following the written steps, which tests followability and completeness but not independent interpretation. The governance skills (build-agent-trust, bot-team-design, measure-agent-roi) were exercised at the discovery and routing level only, because they govern weeks of work rather than a single sandbox task.
