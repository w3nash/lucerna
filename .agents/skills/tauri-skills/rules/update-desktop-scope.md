# Desktop Scope

## Rule
Handle updater with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Updater failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing updater from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```json
{"bundle":{"createUpdaterArtifacts":true},"plugins":{"updater":{"endpoints":["https://updates.example.com/latest.json"]}}}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```json
{"bundle":{"createUpdaterArtifacts":"v1Compatible"},"plugins":{"updater":{"pubkey":"TAURI_UPDATER_PUBLIC_KEY","endpoints":["https://updates.example.com/{{target}}/{{arch}}/{{current_version}}"]}}}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/plugin/updater.mdx
