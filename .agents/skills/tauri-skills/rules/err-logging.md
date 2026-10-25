# Logging

## Rule
Handle errors with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Errors failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing errors from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
database_load(id).map_err(|error| format!("{error:?}"))
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
#[derive(serde::Serialize)]
#[serde(tag = "code", rename_all = "snake_case")]
enum ProfileError { NotFound, PermissionDenied }

database_load(id).map_err(map_profile_error)
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/plugin/logging.mdx
