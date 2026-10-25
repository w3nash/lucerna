#!/usr/bin/env python3
"""Validate the tauri-skills package structure and source coverage."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


ALLOWED_PREFIXES = {
    "arch",
    "setup",
    "front",
    "config",
    "life",
    "ipc",
    "event",
    "state",
    "window",
    "resource",
    "sidecar",
    "plugin",
    "mobile",
    "sec",
    "err",
    "test",
    "debug",
    "perf",
    "bundle",
    "sign",
    "update",
    "ci",
    "migrate",
    "anti",
}

REQUIRED_RULE_SECTIONS = [
    "Rule",
    "Why",
    "Incorrect",
    "Correct",
    "Platform and version notes",
    "Exceptions",
    "Sources",
]

DOC_ROOTS = (
    "src/content/docs/concept/",
    "src/content/docs/develop/",
    "src/content/docs/distribute/",
    "src/content/docs/learn/",
    "src/content/docs/plugin/",
    "src/content/docs/reference/",
    "src/content/docs/security/",
    "src/content/docs/start/",
)

IGNORED_NAMES = {".DS_Store", "__pycache__"}


def section_body(text: str, section: str) -> str:
    match = re.search(
        rf"^## {re.escape(section)}\n(?P<body>.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else ""


def posix(path: Path) -> str:
    return path.as_posix()


def parse_frontmatter(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: Dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def _rule_link_matches(skill_md: Path) -> List[re.Match[str]]:
    text = skill_md.read_text(encoding="utf-8")
    return list(re.finditer(r"\[([a-z0-9-]+)\]\(rules/([a-z0-9-]+)\.md\)", text))


def collect_rule_links(skill_md: Path) -> Set[str]:
    links: Set[str] = set()
    for match in _rule_link_matches(skill_md):
        label, _target = match.groups()
        links.add(label)
    return links


def _duplicate_rule_links(skill_md: Path) -> List[str]:
    seen: Set[str] = set()
    duplicates: List[str] = []
    for match in _rule_link_matches(skill_md):
        label, target = match.groups()
        rule_id = label if label == target else target
        if rule_id in seen:
            duplicates.append(rule_id)
        seen.add(rule_id)
    return duplicates


def validate_rule(path: Path, allowed_prefixes: Set[str]) -> List[str]:
    errors: List[str] = []
    rule_id = path.stem
    if not re.fullmatch(r"[a-z]+-[a-z0-9-]+", rule_id):
        errors.append(f"{posix(path)}: malformed rule id {rule_id}")
    prefix = rule_id.split("-", 1)[0]
    if prefix not in allowed_prefixes:
        errors.append(f"{posix(path)}: unknown rule prefix {prefix}")

    text = path.read_text(encoding="utf-8")
    if not re.search(r"^# .+", text, flags=re.MULTILINE):
        errors.append(f"{posix(path)}: missing H1 title")
    sections = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    for section in REQUIRED_RULE_SECTIONS:
        if section not in sections:
            errors.append(f"{posix(path)}: missing required section {section}")
    if sections[: len(REQUIRED_RULE_SECTIONS)] != REQUIRED_RULE_SECTIONS:
        errors.append(f"{posix(path)}: required sections are out of order")
    for example_section in ("Incorrect", "Correct"):
        if "```" not in section_body(text, example_section):
            errors.append(
                f"{posix(path)}: {example_section} section must include a fenced code example"
            )
    return errors


def _parse_table_rows(path: Path) -> Iterable[List[str]]:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or set(stripped.replace("|", "").strip()) <= {"-"}:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0] in {"Official path", "---"}:
            continue
        yield cells


def parse_source_index(path: Path) -> Tuple[Set[str], Set[str]]:
    mapped: Set[str] = set()
    excluded: Set[str] = set()
    in_exclusions = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_exclusions = line.lower().startswith("## exclusions")
        stripped = line.strip()
        if not stripped.startswith("|") or set(stripped.replace("|", "").strip()) <= {"-"}:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] == "Official path":
            continue
        if in_exclusions:
            excluded.add(cells[0])
        elif len(cells) >= 3 and cells[2] == "mapped":
            mapped.add(cells[0])
    return mapped, excluded


def _exclusion_reasons(path: Path) -> Dict[str, str]:
    reasons: Dict[str, str] = {}
    in_exclusions = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_exclusions = line.lower().startswith("## exclusions")
        if not in_exclusions:
            continue
        stripped = line.strip()
        if not stripped.startswith("|") or set(stripped.replace("|", "").strip()) <= {"-"}:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0] != "Official path":
            reasons[cells[0]] = cells[1] if len(cells) > 1 else ""
    return reasons


def _is_retained_topic(path: str) -> bool:
    if not path.endswith((".md", ".mdx")):
        return False
    return path.startswith(DOC_ROOTS)


def collect_official_topics(repo: Path, revision: str) -> Set[str]:
    if revision == "WORKTREE":
        base = repo / "src" / "content" / "docs"
        if not base.exists():
            return set()
        paths = [posix(path.relative_to(repo)) for path in base.rglob("*") if path.is_file()]
    else:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "ls-tree",
                "-r",
                "--name-only",
                revision,
                "src/content/docs",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            return set()
        paths = result.stdout.splitlines()
    return {path for path in paths if _is_retained_topic(path)}


def _walk_files(root: Path) -> Dict[str, Path]:
    files: Dict[str, Path] = {}
    if not root.exists():
        return files
    for path in root.rglob("*"):
        if any(part in IGNORED_NAMES for part in path.parts) or path.suffix == ".pyc":
            continue
        if path.is_file():
            files[posix(path.relative_to(root))] = path
    return files


def compare_trees(canonical: Path, mirror: Path) -> List[str]:
    errors: List[str] = []
    left = _walk_files(canonical)
    right = _walk_files(mirror)
    for rel in sorted(set(left) - set(right)):
        errors.append(f"mirror missing {rel}")
    for rel in sorted(set(right) - set(left)):
        errors.append(f"mirror has extra {rel}")
    for rel in sorted(set(left) & set(right)):
        if left[rel].read_bytes() != right[rel].read_bytes():
            errors.append(f"mirror differs for {rel}")
    return errors


def validate_skill(
    skill_dir: Path,
    docs_repo: Optional[Path],
    revision: Optional[str],
    mirror: Optional[Path],
) -> List[str]:
    errors: List[str] = []
    if skill_dir.is_file():
        skill_md = skill_dir
        skill_dir = skill_md.parent
    else:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            for markdown_file in skill_dir.glob("*.md"):
                if parse_frontmatter(markdown_file):
                    skill_md = markdown_file
                    break
    if not skill_md.exists():
        return [f"{posix(skill_md)}: missing SKILL.md"]

    frontmatter = parse_frontmatter(skill_md)
    if frontmatter.get("name") != "tauri-skills":
        errors.append(f"{posix(skill_md)}: name must be tauri-skills")
    if not frontmatter.get("description"):
        errors.append(f"{posix(skill_md)}: missing description")

    for duplicate in _duplicate_rule_links(skill_md):
        errors.append(f"{posix(skill_md)}: duplicate rule link {duplicate}")

    linked_rules = collect_rule_links(skill_md)
    for rule_id in sorted(linked_rules):
        rule_path = skill_dir / "rules" / f"{rule_id}.md"
        if not rule_path.exists():
            errors.append(f"{posix(skill_md)}: broken rule link {rule_id}")

    rules_dir = skill_dir / "rules"
    if rules_dir.exists():
        for rule_path in sorted(rules_dir.glob("*.md")):
            errors.extend(validate_rule(rule_path, ALLOWED_PREFIXES))
            if rule_path.stem not in linked_rules:
                errors.append(f"{posix(rule_path)}: rule is not linked from SKILL.md")

    source_index = skill_dir / "references" / "source-index.md"
    if source_index.exists():
        mapped, excluded = parse_source_index(source_index)
        reasons = _exclusion_reasons(source_index)
        for topic in sorted(excluded):
            if not reasons.get(topic):
                errors.append(f"{posix(source_index)}: unexplained exclusion {topic}")
        if docs_repo is not None and revision is not None:
            official = collect_official_topics(docs_repo, revision)
            for topic in sorted(official - mapped - excluded):
                errors.append(f"{posix(source_index)}: unmapped official topic {topic}")
            for topic in sorted(mapped - official):
                errors.append(f"{posix(source_index)}: source-index topic not in official docs {topic}")
    elif docs_repo is not None:
        errors.append(f"{posix(source_index)}: missing source-index.md")

    if mirror is not None:
        errors.extend(compare_trees(skill_dir, mirror))

    return errors


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("--tauri-docs", type=Path)
    parser.add_argument("--revision")
    parser.add_argument("--mirror", type=Path)
    args = parser.parse_args(argv)

    errors = validate_skill(args.skill_dir, args.tauri_docs, args.revision, args.mirror)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: tauri-skills validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
