# Tauri Skill Evaluation Results

Baseline responses were generated in this implementation session without loading `tauri-skills`; fresh subagent contexts were not used because the user did not authorize subagent delegation. The omissions below are preserved as evaluation evidence for the rule requirements.

## IPC

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted capability exposure, channel backpressure, cancellation ownership, and stable error serialization.
- Mapped rule requirements: ipc-access-control, ipc-channels, ipc-cancellation, ipc-serializable-errors.

### Forward test with `tauri-skills`

Pass: the router points this scenario to ipc-access-control, ipc-channels, ipc-cancellation, ipc-serializable-errors and the cited rules cover the missing criteria.

## Security

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted window/webview-bound capabilities, remote API restrictions, CSP/isolation review, and secret boundaries.
- Mapped rule requirements: sec-capability-boundaries, sec-remote-api, sec-csp, sec-secret-boundaries.

### Forward test with `tauri-skills`

Pass: the router points this scenario to sec-capability-boundaries, sec-remote-api, sec-csp, sec-secret-boundaries and the cited rules cover the missing criteria.

## Plugin

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted mobile bindings, permission schema definitions, generated schema checks, and platform conditional compilation.
- Mapped rule requirements: plugin-custom-mobile, plugin-permissions, config-generated-schemas, arch-platform-runtime.

### Forward test with `tauri-skills`

Pass: the router points this scenario to plugin-custom-mobile, plugin-permissions, config-generated-schemas, arch-platform-runtime and the cited rules cover the missing criteria.

## Mobile

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted unsupported multiwindow assumptions, lifecycle differences, platform manifest/plist split, and device testing.
- Mapped rule requirements: mobile-multiwindow, life-mobile-differences, mobile-manifest-plist, test-packaging-smoke.

### Forward test with `tauri-skills`

Pass: the router points this scenario to mobile-multiwindow, life-mobile-differences, mobile-manifest-plist, test-packaging-smoke and the cited rules cover the missing criteria.

## Release

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted desktop-only updater separation from mobile stores, artifact signature verification, staged rollout, and rollback.
- Mapped rule requirements: update-desktop-scope, update-signatures, update-rollout, bundle-ios.

### Forward test with `tauri-skills`

Pass: the router points this scenario to update-desktop-scope, update-signatures, update-rollout, bundle-ios and the cited rules cover the missing criteria.

## Migration

### Baseline response generated without `tauri-skills`

The response gave a high-level implementation outline and mentioned common Tauri concepts, but it did not consistently force source/schema lookup, least-privilege capability design, platform-specific verification, or release/runtime cleanup.

### Observed baseline omissions

- Omitted allowlist-to-capabilities conversion detail, extracted plugin review, updater changes, and staged regression verification.
- Mapped rule requirements: migrate-allowlist, migrate-plugins, migrate-updater, migrate-regression.

### Forward test with `tauri-skills`

Pass: the router points this scenario to migrate-allowlist, migrate-plugins, migrate-updater, migrate-regression and the cited rules cover the missing criteria.

## Retrieval Gap Tests

- Event versus channel: pass via `ipc-direct-vs-event`, `ipc-channels`, and `event-pressure`.
- Restrict filesystem scope per window: pass via `plugin-file-system`, `sec-capability-boundaries`, and `sec-scopes`.
- Packaged-only sidecar failure: pass via `sidecar-packaging`, `sidecar-process-tree`, and `debug-packaged-only`.
- Mobile-store updates versus desktop updater: pass via `update-desktop-scope`, `bundle-android`, and `bundle-ios`.
