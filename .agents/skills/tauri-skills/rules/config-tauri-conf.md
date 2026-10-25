# Tauri Conf

## Rule
Handle configuration with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Configuration failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing configuration from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```json
{"tauri":{"allowlist":{"all":true}},"build":{"devPath":"http://localhost:3000"}}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```json
{"$schema":"https://schema.tauri.app/config/2","identifier":"com.example.app","build":{"devUrl":"http://localhost:1420","frontendDist":"../dist"}}
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/configuration-files.mdx
