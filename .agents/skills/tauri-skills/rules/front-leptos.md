# Leptos

## Rule
Handle frontend with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Frontend failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing frontend from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```typescript
export default defineConfig({ server: { port: 0 }, build: { ssr: true } });
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```typescript
export default defineConfig({
  server: { strictPort: true, port: 1420 },
  envPrefix: ['VITE_', 'TAURI_'],
  build: { target: 'es2021' },
});
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/start/frontend/leptos.mdx
