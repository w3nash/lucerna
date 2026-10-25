# Blocking Async

## Rule
Handle anti with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Anti failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing anti from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```rust
#[tauri::command]
fn run_tool(input: String) {
    Command::new("sh").arg("-c").arg(input).spawn().unwrap();
}
```

## Correct
Apply [ipc-blocking-work](./ipc-blocking-work.md) and document the positive rule that replaces the anti-pattern.

```rust
#[tauri::command]
fn run_tool(request: ToolRequest) -> Result<(), ToolError> {
    let argument = ValidatedArgument::try_from(request.argument)?;
    Command::new("approved-tool").arg(argument.as_ref()).spawn()?;
    Ok(())
}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/security/capabilities.mdx
