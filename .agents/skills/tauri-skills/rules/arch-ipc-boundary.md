# Ipc Boundary

## Rule
Handle architecture with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Architecture failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing architecture from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```typescript
const contents = await fetch('file:///Users/example/secret.txt').then(r => r.text());
await fetch('https://example.com/upload', { method: 'POST', body: contents });
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```typescript
const report = await invoke<Report>('load_report', {
  request: { reportId },
});
// Rust owns filesystem access; the window capability exposes only load_report.
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/concept/architecture.mdx
