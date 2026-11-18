# Codex Bug Hunter

A reusable [OpenAI Codex](https://developers.openai.com/codex/skills) skill for systematic bug hunting, root-cause analysis, security-minded code review, and regression testing.

## What it does

- **Finds and prioritizes bugs** in frontend, backend, API, database, and async code.
- **Separates confirmed bugs from possible risks**, with reproduction evidence whenever possible.
- **Investigates root causes** and reports file paths and line references.
- **Fixes bugs on request** using minimal changes and targeted regression tests.
- **Validates findings** without inventing test results.
- **Defaults to read-only mode** unless you ask for changes.

## Install

Install globally for your local Codex environment:

```bash
git clone https://github.com/ananthajeethd4-ux/codex-bug-hunter.git
mkdir -p ~/.agents/skills
cp -R codex-bug-hunter ~/.agents/skills/bug-hunter
```

Or place the repository files in `.agents/skills/bug-hunter/` inside a project to make it project-scoped.

## Usage

In a Codex session:

```text
$bug-hunter Hunt for bugs in this repository. Report confirmed issues with evidence.
```

To authorize fixes:

```text
$bug-hunter Find and fix confirmed bugs, add regression tests, and validate changes.
```

To focus on a subsystem:

```text
$bug-hunter Audit authentication and authorization paths. Do not modify files.
```

## Modes

| Mode | Behavior |
| --- | --- |
| Hunt (default) | Read-only inspection, verification, and prioritized report |
| Fix | Minimal patches, regression tests, and validation |
| Regression | Reproduce and prevent a specific failure |
| Focused audit | Investigate a specified component or flow |

Findings use **P0–P3** severity and include location, trigger, impact, evidence, root cause, and validation status.

## Files

- [SKILL.md](SKILL.md) — skill instructions and investigation workflow
- [agents/openai.yaml](agents/openai.yaml) — Codex UI metadata

## Safety and reliability

The skill avoids destructive checks, respects uncommitted work and secrets, and does not claim bugs are fixed without verification. It is a debugging assistant, **not a guarantee that all defects or vulnerabilities will be found**.

## License

No license has been selected yet. The repository is public, but reuse rights remain with the copyright holder unless a license is added.
