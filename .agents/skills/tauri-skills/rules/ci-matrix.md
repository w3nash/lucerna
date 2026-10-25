# Matrix

## Rule
Handle CI with explicit Tauri v2 ownership, least privilege, platform awareness, lifecycle cleanup, and source/schema verification before editing.

## Why
Ci failures usually come from hidden authority, version drift, or assuming development behavior matches packaged behavior.

## Incorrect
Implementing CI from memory, with global access, broad permissions, no cleanup, or no target-platform verification.

```yaml
runs-on: ubuntu-latest
steps:
  - run: npm run tauri build -- --target universal-apple-darwin
```

## Correct
Read the official source and local generated schemas, apply least privilege, document target-platform behavior, and verify the changed surface.

```yaml
strategy:
  matrix:
    os: [macos-latest, windows-latest, ubuntu-latest]
runs-on: ${{ matrix.os }}
steps:
  - run: npm ci
  - run: npm run tauri build
```

## Platform and version notes
Applies to Tauri v2. Inspect installed crates, packages, generated config schemas, capability schemas, Cargo features, and target platforms for version-sensitive APIs.

## Exceptions
Temporary prototypes may narrow verification, but must not ship unsupported permissions, platform claims, release artifacts, or security-sensitive shortcuts.

## Sources
- src/content/docs/distribute/Pipelines/github.mdx
