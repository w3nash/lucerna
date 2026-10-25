# Use Dialog Plugin Safely

## Rule
Handle official plugins with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Official Plugins failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing official plugins from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
tauri::Builder::default()
    .run(tauri::generate_context!())?;
// Frontend calls a plugin that was never initialized.
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
tauri::Builder::default()
    .plugin(tauri_plugin_opener::init())
    .run(tauri::generate_context!())?;
// Grant only the required opener permission to the intended capability.
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/plugin/dialog.mdx
