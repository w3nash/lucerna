# Frontend Devtools

## Rule
Handle debugging with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Debugging failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing debugging from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```bash
npm run tauri build
# Rebuild repeatedly without logs or packaged-path evidence.
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```bash
RUST_LOG=tauri=trace,my_app=debug npm run tauri dev
RUST_BACKTRACE=1 ./src-tauri/target/release/my-app
npm run tauri info
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/Debug/index.mdx
