# Asset Protocol

## Rule
Handle resources with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Resources failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing resources from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
let template = std::fs::read_to_string("../assets/template.html")?;
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
let template = app
    .path()
    .resolve("templates/template.html", BaseDirectory::Resource)
    .and_then(std::fs::read_to_string)?;
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/resources.mdx
