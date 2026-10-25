import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_skill.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skill", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def valid_rule(self, rule_id="ipc-typed-commands"):
        return f"""# Typed Commands

## Rule
Use typed request and response objects.

## Why
They keep Rust and TypeScript contracts stable.

## Incorrect
Passing ad hoc positional values.

```rust
#[tauri::command]
fn import_file(path: String) -> Result<String, String> {{
    Ok(path)
}}
```

## Correct
Use serde-compatible structs and generated frontend types.

```rust
#[derive(serde::Deserialize)]
struct ImportFileRequest {{
    path: String,
}}

#[tauri::command]
fn import_file(request: ImportFileRequest) -> Result<(), ImportFileError> {{
    Ok(())
}}
```

## Platform and version notes
Applies to Tauri v2 desktop and mobile.

## Exceptions
Tiny internal commands can use primitives when the contract is documented.

## Sources
- src/content/docs/develop/calling-rust.mdx
"""

    def valid_skill(self):
        skill = self.write(
            "skill/SKILL.md",
            """---
name: tauri-skills
description: Use when creating, configuring, implementing, reviewing, debugging, securing, testing, optimizing, packaging, signing, updating, distributing, or migrating a Tauri application, plugin, desktop feature, Android feature, or iOS feature.
---

# Tauri Skills

- [ipc-typed-commands](rules/ipc-typed-commands.md) - typed command contracts.
""",
        )
        self.write("skill/rules/ipc-typed-commands.md", self.valid_rule())
        self.write(
            "skill/references/source-index.md",
            """# Official Tauri Source Index

## Mapped topics

| Official path | Mapped rules | Status |
|---|---|---|
| src/content/docs/develop/calling-rust.mdx | ipc-typed-commands | mapped |

## Exclusions

| Official path | Reason |
|---|---|
| src/content/docs/start/index.mdx | Non-guidance index page. |
""",
        )
        return skill.parent

    def test_parse_frontmatter_rejects_missing_and_wrong_name(self):
        v = load_validator()
        missing = self.write("missing.md", "# No frontmatter\n")
        self.assertEqual(v.parse_frontmatter(missing), {})
        wrong = self.write("wrong.md", "---\nname: other\n---\n")
        errors = v.validate_skill(wrong.parent, None, None, None)
        self.assertTrue(any("name must be tauri-skills" in e for e in errors))

    def test_collect_rule_links_rejects_duplicate_and_broken_links(self):
        v = load_validator()
        skill = self.write(
            "SKILL.md",
            """---
name: tauri-skills
description: x
---
- [ipc-typed-commands](rules/ipc-typed-commands.md)
- [ipc-typed-commands](rules/ipc-typed-commands.md)
- [bad](rules/missing.md)
""",
        )
        links = v.collect_rule_links(skill)
        self.assertEqual(links, {"ipc-typed-commands", "bad"})
        errors = v.validate_skill(skill.parent, None, None, None)
        self.assertTrue(any("duplicate rule link" in e for e in errors))
        self.assertTrue(any("broken rule link" in e for e in errors))

    def test_validate_rule_rejects_malformed_ids_sections_and_prefixes(self):
        v = load_validator()
        bad = self.write("rules/nope.md", "# Bad\n\n## Rule\nOnly one section.\n")
        errors = v.validate_rule(bad, {"ipc"})
        self.assertTrue(any("unknown rule prefix" in e for e in errors))
        self.assertTrue(any("missing required section" in e for e in errors))
        malformed = self.write("rules/ipc_bad.md", self.valid_rule("ipc_bad"))
        errors = v.validate_rule(malformed, {"ipc"})
        self.assertTrue(any("malformed rule id" in e for e in errors))

    def test_validate_rule_requires_code_examples(self):
        v = load_validator()
        missing_examples = self.write(
            "rules/ipc-no-examples.md",
            """# No Examples

## Rule
Use examples.

## Why
They make the rule concrete.

## Incorrect
Only prose.

## Correct
Still only prose.

## Platform and version notes
Applies to Tauri v2.

## Exceptions
None.

## Sources
- src/content/docs/develop/calling-rust.mdx
""",
        )
        errors = v.validate_rule(missing_examples, {"ipc"})
        self.assertTrue(any("Incorrect section must include a fenced code example" in e for e in errors))
        self.assertTrue(any("Correct section must include a fenced code example" in e for e in errors))

    def test_parse_source_index_detects_mapped_and_excluded_topics(self):
        v = load_validator()
        index = self.write(
            "source-index.md",
            """# Official Tauri Source Index

## Mapped topics
| Official path | Mapped rules | Status |
|---|---|---|
| src/content/docs/develop/calling-rust.mdx | ipc-typed-commands | mapped |

## Exclusions
| Official path | Reason |
|---|---|
| src/content/docs/start/index.mdx | Non-guidance index page. |
""",
        )
        mapped, excluded = v.parse_source_index(index)
        self.assertEqual(mapped, {"src/content/docs/develop/calling-rust.mdx"})
        self.assertEqual(excluded, {"src/content/docs/start/index.mdx"})

    def test_collect_official_topics_filters_english_docs(self):
        v = load_validator()
        docs = self.root / "docs"
        self.write("docs/src/content/docs/develop/calling-rust.mdx", "x")
        self.write("docs/src/content/docs/ja/develop/calling-rust.mdx", "x")
        self.write("docs/src/content/docs/blog/tauri-1-0.md", "x")
        topics = v.collect_official_topics(docs, "WORKTREE")
        self.assertEqual(topics, {"src/content/docs/develop/calling-rust.mdx"})

    def test_validate_skill_reports_unmapped_topics_and_unexplained_exclusions(self):
        v = load_validator()
        skill = self.valid_skill()
        docs = self.root / "docs"
        self.write("docs/src/content/docs/develop/calling-rust.mdx", "x")
        self.write("docs/src/content/docs/security/csp.mdx", "x")
        errors = v.validate_skill(skill, docs, "WORKTREE", None)
        self.assertTrue(any("unmapped official topic" in e for e in errors))
        index = skill / "references" / "source-index.md"
        index.write_text(
            index.read_text(encoding="utf-8")
            + "| src/content/docs/security/csp.mdx |  |\n",
            encoding="utf-8",
        )
        errors = v.validate_skill(skill, docs, "WORKTREE", None)
        self.assertTrue(any("unexplained exclusion" in e for e in errors))

    def test_compare_trees_ignores_cache_and_detects_byte_divergence(self):
        v = load_validator()
        a = self.root / "a"
        b = self.root / "b"
        (a / "__pycache__").mkdir(parents=True)
        (b / "__pycache__").mkdir(parents=True)
        (a / "x.md").write_text("one", encoding="utf-8")
        (b / "x.md").write_text("two", encoding="utf-8")
        (a / "__pycache__" / "x.pyc").write_bytes(b"1")
        errors = v.compare_trees(a, b)
        self.assertTrue(any("mirror differs" in e for e in errors))

    def test_complete_valid_fixture_has_no_errors_and_cli_ok(self):
        v = load_validator()
        skill = self.valid_skill()
        mirror = self.root / "mirror"
        mirror.mkdir()
        for path in skill.rglob("*"):
            if path.is_file():
                target = mirror / path.relative_to(skill)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(path.read_bytes())
        docs = self.root / "docs"
        self.write("docs/src/content/docs/develop/calling-rust.mdx", "x")
        errors = v.validate_skill(skill, docs, "WORKTREE", mirror)
        self.assertEqual(errors, [])
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(skill),
                "--tauri-docs",
                str(docs),
                "--revision",
                "WORKTREE",
                "--mirror",
                str(mirror),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK: tauri-skills validation passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
