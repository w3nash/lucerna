# Rust Unit

## Rule
Handle testing with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Testing failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing testing from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```typescript
test('exports', async () => { await exportReport(); });
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```typescript
test('exports through a typed command', async () => {
  const invoke = vi.fn().mockResolvedValue({ path: '/tmp/report.csv' });
  await exportReport({ patientId: 'p_123' }, { invoke });
  expect(invoke).toHaveBeenCalledWith('export_report', {
    request: { patientId: 'p_123' },
  });
});
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/develop/Tests/index.mdx
