# Tauri Skill Evaluation Scenarios

## IPC
Design a Tauri v2 command accepting a validated request object, streaming progress, supporting cancellation, and returning typed errors to TypeScript.

Success: addresses serde shape matching, command registration, channel/backpressure choice, cancellation ownership, error serialization, frontend typing, and capability exposure.

## Security
Review a Tauri v2 app that grants shell, filesystem, HTTP, and opener permissions globally to every window and loads some remote content.

Success: applies least privilege, window/webview-bound capabilities, scoped permissions, remote API restrictions, CSP/isolation, URL validation, and secret boundaries.

## Plugin
Add a custom Tauri v2 plugin that works on desktop, Android, and iOS and exposes one command to the frontend.

Success: covers plugin builder/setup, mobile plugin registration and bindings, permission definitions, generated schemas, platform conditional compilation, and JavaScript guest bindings.

## Mobile
Add deep-link file associations and secondary-window behavior to Android and iOS.

Success: separates platform support, manifest/plist changes, plugin initialization, mobile lifecycle differences, testing, and unsupported multiwindow assumptions.

## Release
Design signed, auto-updating releases for macOS, Windows, Linux, Android, and iOS through CI.

Success: separates desktop updater from mobile stores, covers bundle formats, signing/notarization, updater signatures and endpoints, secret handling, matrix builds, artifact verification, rollout, and rollback.

## Migration
Migrate a Tauri v1 app using an allowlist, embedded APIs, updater, shell, filesystem, and deep links to Tauri v2.

Success: covers plugin extraction, JavaScript and Rust API changes, config migration, allowlist-to-capabilities conversion, permission scopes, updater changes, mobile considerations, and regression verification.
