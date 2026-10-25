# Single Instance

## Rule
Handle lifecycle with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Lifecycle failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing lifecycle from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
tauri::Builder::default().setup(|_app| {
    std::thread::spawn(run_background_loop);
    Ok(())
});
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
tauri::Builder::default().setup(|app| {
    let token = CancellationToken::new();
    app.manage(AppTasks { shutdown: token.clone() });
    tauri::async_runtime::spawn(run_background_loop(token));
    Ok(())
});
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/index.mdx
