# Verify

## Rule
Handle signing with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Signing failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing signing from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```yaml
- run: npm run tauri build
  env:
    APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```yaml
- run: npm run tauri build -- --no-bundle
- run: ./scripts/sign-and-verify.sh
  if: github.ref_type == 'tag'
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/distribute/index.mdx
