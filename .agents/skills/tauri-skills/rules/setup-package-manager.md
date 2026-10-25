# Package Manager

## Rule
Handle setup with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Setup failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing setup from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```bash
npm install @tauri-apps/api@latest
cargo add tauri
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```bash
npm install @tauri-apps/api@2 @tauri-apps/cli@2
cargo add tauri@2
npx tauri info
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/start/create-project.mdx
