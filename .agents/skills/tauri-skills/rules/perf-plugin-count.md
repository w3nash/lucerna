# Plugin Count

## Rule
Handle performance with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Performance failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing performance from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
rows.iter().map(|row| format!("{row:?}")).collect::<Vec<_>>().join("\n")
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
let row_count = rows.len();
tauri::async_runtime::spawn_blocking(move || write_report_file(rows)).await??;
Ok(ReportSummary { row_count })
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/concept/size.mdx
