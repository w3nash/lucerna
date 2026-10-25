# Android

## Rule
Handle packaging with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Packaging failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing packaging from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```json
{"bundle":{"active":true,"targets":"all"}}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```json
{"bundle":{"active":true,"targets":["dmg","nsis","appimage"],"icon":["icons/32x32.png","icons/icon.icns","icons/icon.ico"]}}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/distribute/google-play.mdx
