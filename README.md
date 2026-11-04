# Agent Trust Skills

A professional skill pack for working with AI coding agents: how to earn trust in an agent step by step, verify its work on the real product, turn repeated reminders into hard constraints, and run agents autonomously without losing control.

The methods are distilled from the public talks, posts and open-source tooling of **Lauren Tan** (@poteto), software engineer on the Grok Bot team at SpaceXAI, formerly Cursor, Meta (React Compiler) and Netflix. They are generalized here into reusable agent skills. This repository is an independent study artifact. It is not affiliated with SpaceXAI, Cursor or Lauren Tan, and her reported output figures are her own self-published numbers, not audited benchmarks.

## The core idea

Trust in an agent is not given. It is earned with evidence, one rung at a time:

1. Start local, where you can watch the agent work.
2. Build verification before delegating real work.
3. Package know-how into skills, then unit test the skills with evals.
4. Convert every repeated reminder into a harder constraint.
5. Brief tasks with verifiable done criteria, never with a prescribed method.
6. Widen permissions only as checks pass, and log every decision in one line.
7. Scale to the cloud and a bot team only after the local loop is trusted.
8. Treat tokens as investment capital and measure accepted outcomes, not activity.

The full method is written up in [docs/PLAYBOOK.md](docs/PLAYBOOK.md).

## Skills in this pack

| Skill | What it does |
|---|---|
| [build_agent_trust](skills/build_agent_trust/SKILL.md) | Climb the trust ladder in order, split work by reversibility, review decisions instead of output |
| [verification_first](skills/verification_first/SKILL.md) | Give the agent a way to run and check the real product, with a feature map and evidence-required reporting |
| [skill_evals](skills/skill_evals/SKILL.md) | Unit test skills with scored cases, a cross-model judge and a loop that runs until the score is perfect |
| [hard_constraints](skills/hard_constraints/SKILL.md) | Turn soft guidance into lint rules, CI failures and architecture, so the shortest path is the best path |
| [task_briefing](skills/task_briefing/SKILL.md) | Write five-part task briefs with pass or fail done criteria, and prototype instead of planning in the abstract |
| [autonomous_runs](skills/autonomous_runs/SKILL.md) | Run agents unattended with a verifiable end condition, an isolated worktree and a one-line decision log |
| [bot_team_design](skills/bot_team_design/SKILL.md) | Design an outer loop and an inner loop, one owner per task, few sharp bots with explicit anti-jobs |
| [measure_agent_roi](skills/measure_agent_roi/SKILL.md) | Front-load token spend on verification, skills and refactors, and track the manual-fix rate instead of counting tasks |

## Install

Each folder under `skills/` is one self-contained skill in the standard format: a `SKILL.md` with the method and a `skill.yaml` with its descriptor.

- For Muse: copy the skill folders into `~/workspace/custom-skills/`.
- For Claude Code: copy the skill folders into `.claude/skills/` in your project or `~/.claude/skills/` for all projects. Only `SKILL.md` is read there.
- For any other agent harness: point the harness at the `SKILL.md` files, or paste a skill into your system prompt.

## Sources

- Maven workshop, How Cursor Turned AI Agents Into Better Engineers (12 Aug 2026): https://www.youtube.com/watch?v=I_oMJk6barY
- Solo talk, How I Shipped 2,000 PRs Last Month (21 Sep 2026): https://www.youtube.com/watch?v=NjoZoUm85x0
- Behind the Craft podcast, We Built Grok Bot (27 Sep 2026): https://realalpha.app/v/xZ5TEaleUdg/?t=762
- Grok Bot guide post on X (31 Oct 2026): https://x.com/poteto/status/2116580481236115933
- pstack, Lauren Tan's open-source skill stack: https://github.com/cursor/plugins/tree/main/pstack

## Tiếng Việt

Bộ skill này chắt lọc phương pháp làm việc với AI agent từ các buổi chia sẻ công khai của Lauren Tan (kỹ sư Grok Bot tại SpaceXAI): xây niềm tin theo từng nấc bằng bằng chứng, dựng khả năng tự kiểm chứng trước khi giao việc, kiểm thử skill bằng eval, biến nhắc nhở lặp lại thành ràng buộc cứng trong CI và kiến trúc, giao việc bằng tiêu chí hoàn thành phán được đạt hay không đạt, và đo kết quả được chấp nhận thay vì đếm số tác vụ. Tài liệu phương pháp đầy đủ nằm ở [docs/PLAYBOOK.md](docs/PLAYBOOK.md). Repo này là sản phẩm học tập độc lập, không liên kết với SpaceXAI, Cursor hay Lauren Tan.

## License

MIT. See [LICENSE](LICENSE). Methods are credited to Lauren Tan's public work, linked above.
