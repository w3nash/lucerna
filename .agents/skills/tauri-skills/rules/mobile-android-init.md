# Android Init

## Rule
Handle mobile with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Mobile failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing mobile from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
#[tauri::command]
fn open_secondary_window(app: tauri::AppHandle) -> tauri::Result<()> {
    create_desktop_window(&app)
}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
#[cfg(desktop)]
fn open_secondary_window(app: tauri::AppHandle) -> tauri::Result<()> {
    create_desktop_window(&app)
}

#[cfg(mobile)]
fn open_secondary_window(_app: tauri::AppHandle) -> tauri::Result<()> {
    Err(tauri::Error::AssetNotFound("mobile multiwindow unsupported".into()))
}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/learn/mobile-file-associations.mdx
