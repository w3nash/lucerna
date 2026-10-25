# Initialization

## Rule
Handle state with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
State failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing state from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
let mut state = state.lock().unwrap();
upload_to_server(&state.buffer).await;
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
let buffer = {
    let state = state.lock().await;
    state.buffer.clone()
};
upload_to_server(&buffer).await;
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/state-management.mdx
