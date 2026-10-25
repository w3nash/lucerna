# Command Macro

## Rule
Handle IPC with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Ipc failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing IPC from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
#[tauri::command]
async fn import_file(path: String) -> Result<String, String> {
    Ok(format!("imported {path}"))
}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```rust
#[derive(serde::Deserialize)]
#[serde(rename_all = "camelCase")]
struct ImportFileRequest { path: String }

#[derive(serde::Serialize)]
#[serde(rename_all = "camelCase")]
struct ImportFileResponse { imported_id: String }

#[tauri::command]
async fn import_file(
    request: ImportFileRequest,
) -> Result<ImportFileResponse, ImportFileError> {
    validate_path(&request.path)?;
    Ok(ImportFileResponse { imported_id: "file_123".into() })
}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/calling-rust.mdx
