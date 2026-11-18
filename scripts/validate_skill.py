#!/usr/bin/env python3
"""Dependency-free structural checks for a Codex skill repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

skill_path = ROOT / "SKILL.md"
agent_path = ROOT / "agents" / "openai.yaml"
readme_path = ROOT / "README.md"

for path in (skill_path, agent_path, readme_path):
    require(path.is_file(), f"Missing required file: {path.relative_to(ROOT)}")

if skill_path.is_file():
    content = skill_path.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    require(frontmatter is not None, "SKILL.md must start with YAML frontmatter")
    if frontmatter:
        metadata = frontmatter.group(1)
        name = re.search(r"^name:\s*([\w-]+)\s*$", metadata, re.M)
        description = re.search(r"^description:\s*(.+)$", metadata, re.M)
        require(bool(name), "SKILL.md frontmatter must contain a valid name")
        if name:
            require(name.group(1) == "bug-hunter", "Skill name must be bug-hunter")
        require(bool(description and description.group(1).strip()),
                "SKILL.md frontmatter must contain a description")
    require("# Bug Hunter" in content, "SKILL.md must contain its main heading")
    require("## Workflow" in content, "SKILL.md must describe its workflow")
    require("## Output format" in content, "SKILL.md must define output format")

if agent_path.is_file():
    content = agent_path.read_text(encoding="utf-8")
    require(re.search(r"^interface:\s*$", content, re.M) is not None,
            "agents/openai.yaml must contain interface mapping")
    for field in ("display_name", "short_description", "default_prompt"):
        require(re.search(rf"^  {field}:\s*\S+", content, re.M) is not None,
                f"agents/openai.yaml missing interface.{field}")

if readme_path.is_file():
    content = readme_path.read_text(encoding="utf-8")
    require("SKILL.md" in content, "README.md should link to SKILL.md")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print("Skill validation passed.")
