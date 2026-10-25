---
name: tauri-skills
description: Use when creating, configuring, implementing, reviewing, debugging, securing, testing, optimizing, packaging, signing, updating, distributing, or migrating a Tauri application, plugin, desktop feature, Android feature, or iOS feature.
---

# Tauri Skills

Use this skill before designing, writing, reviewing, debugging, securing, testing, packaging, signing, distributing, updating, or migrating Tauri v2 applications and plugins. Use Tauri v1 material only for migration work.

## Required Workflow

1. Inspect installed Tauri crate and package versions, frontend package versions, Cargo features, package manager, `src-tauri/tauri.conf.*`, generated config schemas, generated ACL/capability schemas, existing capabilities, plugin initialization, and target platforms before editing.
2. For version-sensitive APIs, check the target project's installed schemas and the official source index in [references/source-index.md](references/source-index.md). Do not rely on memory when generated schemas disagree.
3. Choose the smallest applicable rules below, read those rule files, and apply their checklist-level guidance. For security-sensitive work, also read the linked `sec-*` rule.
4. Verify with the narrowest meaningful tests plus capability review, target-platform checks, and packaged smoke tests for release changes.

## Non-Negotiable Invariants

- Least privilege: bind permissions to the narrowest command, plugin, scope, window, webview, platform, and URL set that works.
- Typed IPC: use serde-compatible request/response objects and stable serializable errors for nontrivial commands.
- Platform-explicit behavior: state desktop, Android, and iOS support separately; never imply unsupported mobile or updater behavior.
- Lifecycle cleanup: own listeners, channels, windows, sidecars, background work, and state cleanup.
- Release verification: signed, packaged, updater, and store changes require artifact-level verification and rollback thinking.

## Rule Router

### arch
- [arch-process-model](rules/arch-process-model.md) - Process Model.
- [arch-ipc-boundary](rules/arch-ipc-boundary.md) - Ipc Boundary.
- [arch-webview-variability](rules/arch-webview-variability.md) - Webview Variability.
- [arch-isolation-choice](rules/arch-isolation-choice.md) - Isolation Choice.
- [arch-binary-size](rules/arch-binary-size.md) - Binary Size.
- [arch-platform-runtime](rules/arch-platform-runtime.md) - Platform Runtime.

### setup
- [setup-prerequisites](rules/setup-prerequisites.md) - Prerequisites.
- [setup-create-tauri-app](rules/setup-create-tauri-app.md) - Create Tauri App.
- [setup-manual-init](rules/setup-manual-init.md) - Manual Init.
- [setup-project-structure](rules/setup-project-structure.md) - Project Structure.
- [setup-version-alignment](rules/setup-version-alignment.md) - Version Alignment.
- [setup-package-manager](rules/setup-package-manager.md) - Package Manager.
- [setup-rust-targets](rules/setup-rust-targets.md) - Rust Targets.
- [setup-mobile-init](rules/setup-mobile-init.md) - Mobile Init.

### front
- [front-framework-selection](rules/front-framework-selection.md) - Select Frontend Frameworks by Runtime Fit.
- [front-vite](rules/front-vite.md) - Vite.
- [front-nextjs](rules/front-nextjs.md) - Nextjs.
- [front-nuxt](rules/front-nuxt.md) - Nuxt.
- [front-sveltekit](rules/front-sveltekit.md) - Sveltekit.
- [front-qwik](rules/front-qwik.md) - Qwik.
- [front-trunk](rules/front-trunk.md) - Trunk.
- [front-leptos](rules/front-leptos.md) - Leptos.

### config
- [config-schema-edits](rules/config-schema-edits.md) - Schema Edits.
- [config-tauri-conf](rules/config-tauri-conf.md) - Tauri Conf.
- [config-platform-merge](rules/config-platform-merge.md) - Platform Merge.
- [config-identifiers](rules/config-identifiers.md) - Identifiers.
- [config-versions](rules/config-versions.md) - Versions.
- [config-products](rules/config-products.md) - Products.
- [config-build-commands](rules/config-build-commands.md) - Build Commands.
- [config-dev-build-urls](rules/config-dev-build-urls.md) - Dev Build Urls.
- [config-bundle](rules/config-bundle.md) - Bundle.
- [config-features](rules/config-features.md) - Features.
- [config-env](rules/config-env.md) - Env.
- [config-generated-schemas](rules/config-generated-schemas.md) - Generated Schemas.

### life
- [life-builder-order](rules/life-builder-order.md) - Builder Order.
- [life-setup-timing](rules/life-setup-timing.md) - Setup Timing.
- [life-activation-focus](rules/life-activation-focus.md) - Activation Focus.
- [life-close-requests](rules/life-close-requests.md) - Close Requests.
- [life-graceful-shutdown](rules/life-graceful-shutdown.md) - Graceful Shutdown.
- [life-restart](rules/life-restart.md) - Restart.
- [life-cleanup](rules/life-cleanup.md) - Cleanup.
- [life-single-instance](rules/life-single-instance.md) - Single Instance.
- [life-mobile-differences](rules/life-mobile-differences.md) - Mobile Differences.
- [life-background-work](rules/life-background-work.md) - Background Work.

### ipc
- [ipc-command-macro](rules/ipc-command-macro.md) - Command Macro.
- [ipc-handler-registration](rules/ipc-handler-registration.md) - Handler Registration.
- [ipc-serde-shapes](rules/ipc-serde-shapes.md) - Serde Shapes.
- [ipc-typed-objects](rules/ipc-typed-objects.md) - Typed Objects.
- [ipc-serializable-errors](rules/ipc-serializable-errors.md) - Serializable Errors.
- [ipc-async-safety](rules/ipc-async-safety.md) - Async Safety.
- [ipc-blocking-work](rules/ipc-blocking-work.md) - Blocking Work.
- [ipc-access-control](rules/ipc-access-control.md) - Access Control.
- [ipc-channels](rules/ipc-channels.md) - Channels.
- [ipc-progress](rules/ipc-progress.md) - Progress.
- [ipc-cancellation](rules/ipc-cancellation.md) - Cancellation.
- [ipc-large-payloads](rules/ipc-large-payloads.md) - Large Payloads.
- [ipc-binary-payloads](rules/ipc-binary-payloads.md) - Binary Payloads.
- [ipc-direct-vs-event](rules/ipc-direct-vs-event.md) - Direct Vs Event.

### event
- [event-targeting](rules/event-targeting.md) - Targeting.
- [event-naming](rules/event-naming.md) - Naming.
- [event-payloads](rules/event-payloads.md) - Payloads.
- [event-registration](rules/event-registration.md) - Registration.
- [event-cleanup](rules/event-cleanup.md) - Cleanup.
- [event-duplicates](rules/event-duplicates.md) - Duplicates.
- [event-ordering](rules/event-ordering.md) - Ordering.
- [event-delivery](rules/event-delivery.md) - Delivery.
- [event-pressure](rules/event-pressure.md) - Pressure.

### state
- [state-manage](rules/state-manage.md) - Manage.
- [state-state-extractor](rules/state-state-extractor.md) - State Extractor.
- [state-interior-mutability](rules/state-interior-mutability.md) - Interior Mutability.
- [state-lock-granularity](rules/state-lock-granularity.md) - Lock Granularity.
- [state-no-lock-await](rules/state-no-lock-await.md) - No Lock Await.
- [state-initialization](rules/state-initialization.md) - Initialization.
- [state-per-window](rules/state-per-window.md) - Per Window.
- [state-background-cleanup](rules/state-background-cleanup.md) - Background Cleanup.

### window
- [window-labels](rules/window-labels.md) - Labels.
- [window-creation](rules/window-creation.md) - Creation.
- [window-webview-urls](rules/window-webview-urls.md) - Webview Urls.
- [window-navigation](rules/window-navigation.md) - Navigation.
- [window-multiwindow-state](rules/window-multiwindow-state.md) - Multiwindow State.
- [window-monitor-scaling](rules/window-monitor-scaling.md) - Monitor Scaling.
- [window-menus](rules/window-menus.md) - Menus.
- [window-context-menus](rules/window-context-menus.md) - Context Menus.
- [window-tray](rules/window-tray.md) - Tray.
- [window-splash](rules/window-splash.md) - Splash.
- [window-title-bars](rules/window-title-bars.md) - Title Bars.
- [window-drag-regions](rules/window-drag-regions.md) - Drag Regions.
- [window-close-hide](rules/window-close-hide.md) - Close Hide.

### resource
- [resource-directories](rules/resource-directories.md) - Directories.
- [resource-bundled](rules/resource-bundled.md) - Bundled.
- [resource-path-resolution](rules/resource-path-resolution.md) - Path Resolution.
- [resource-icons](rules/resource-icons.md) - Icons.
- [resource-asset-protocol](rules/resource-asset-protocol.md) - Asset Protocol.
- [resource-custom-protocols](rules/resource-custom-protocols.md) - Custom Protocols.
- [resource-immutable-assets](rules/resource-immutable-assets.md) - Immutable Assets.
- [resource-dev-vs-bundle](rules/resource-dev-vs-bundle.md) - Dev Vs Bundle.

### sidecar
- [sidecar-binaries](rules/sidecar-binaries.md) - Binaries.
- [sidecar-target-triples](rules/sidecar-target-triples.md) - Target Triples.
- [sidecar-arguments](rules/sidecar-arguments.md) - Arguments.
- [sidecar-no-shell](rules/sidecar-no-shell.md) - No Shell.
- [sidecar-permissions](rules/sidecar-permissions.md) - Permissions.
- [sidecar-io-drain](rules/sidecar-io-drain.md) - Io Drain.
- [sidecar-cancellation](rules/sidecar-cancellation.md) - Cancellation.
- [sidecar-process-tree](rules/sidecar-process-tree.md) - Process Tree.
- [sidecar-packaging](rules/sidecar-packaging.md) - Packaging.
- [sidecar-untrusted-input](rules/sidecar-untrusted-input.md) - Untrusted Input.

### plugin
- [plugin-architecture](rules/plugin-architecture.md) - Architecture.
- [plugin-permissions](rules/plugin-permissions.md) - Permissions.
- [plugin-custom-desktop](rules/plugin-custom-desktop.md) - Custom Desktop.
- [plugin-custom-mobile](rules/plugin-custom-mobile.md) - Custom Mobile.
- [plugin-autostart](rules/plugin-autostart.md) - Use Autostart Plugin Safely.
- [plugin-barcode-scanner](rules/plugin-barcode-scanner.md) - Use Barcode Scanner Plugin Safely.
- [plugin-biometric](rules/plugin-biometric.md) - Use Biometric Plugin Safely.
- [plugin-cli](rules/plugin-cli.md) - Use Cli Plugin Safely.
- [plugin-clipboard](rules/plugin-clipboard.md) - Use Clipboard Plugin Safely.
- [plugin-deep-linking](rules/plugin-deep-linking.md) - Use Deep Linking Plugin Safely.
- [plugin-dialog](rules/plugin-dialog.md) - Use Dialog Plugin Safely.
- [plugin-file-system](rules/plugin-file-system.md) - Use File System Plugin Safely.
- [plugin-geolocation](rules/plugin-geolocation.md) - Use Geolocation Plugin Safely.
- [plugin-global-shortcut](rules/plugin-global-shortcut.md) - Use Global Shortcut Plugin Safely.
- [plugin-haptics](rules/plugin-haptics.md) - Use Haptics Plugin Safely.
- [plugin-http-client](rules/plugin-http-client.md) - Use Http Client Plugin Safely.
- [plugin-localhost](rules/plugin-localhost.md) - Use Localhost Plugin Safely.
- [plugin-logging](rules/plugin-logging.md) - Use Logging Plugin Safely.
- [plugin-nfc](rules/plugin-nfc.md) - Use Nfc Plugin Safely.
- [plugin-notification](rules/plugin-notification.md) - Use Notification Plugin Safely.
- [plugin-opener](rules/plugin-opener.md) - Use Opener Plugin Safely.
- [plugin-os-info](rules/plugin-os-info.md) - Use Os Info Plugin Safely.
- [plugin-persisted-scope](rules/plugin-persisted-scope.md) - Use Persisted Scope Plugin Safely.
- [plugin-positioner](rules/plugin-positioner.md) - Use Positioner Plugin Safely.
- [plugin-process](rules/plugin-process.md) - Use Process Plugin Safely.
- [plugin-shell](rules/plugin-shell.md) - Use Shell Plugin Safely.
- [plugin-single-instance](rules/plugin-single-instance.md) - Use Single Instance Plugin Safely.
- [plugin-sql](rules/plugin-sql.md) - Use Sql Plugin Safely.
- [plugin-store](rules/plugin-store.md) - Use Store Plugin Safely.
- [plugin-stronghold](rules/plugin-stronghold.md) - Use Stronghold Plugin Safely.
- [plugin-updater](rules/plugin-updater.md) - Use Updater Plugin Safely.
- [plugin-upload](rules/plugin-upload.md) - Use Upload Plugin Safely.
- [plugin-websocket](rules/plugin-websocket.md) - Use Websocket Plugin Safely.
- [plugin-window-state](rules/plugin-window-state.md) - Use Window State Plugin Safely.

### mobile
- [mobile-android-init](rules/mobile-android-init.md) - Android Init.
- [mobile-ios-init](rules/mobile-ios-init.md) - Ios Init.
- [mobile-dev-commands](rules/mobile-dev-commands.md) - Dev Commands.
- [mobile-device-selection](rules/mobile-device-selection.md) - Device Selection.
- [mobile-gradle-xcode](rules/mobile-gradle-xcode.md) - Gradle Xcode.
- [mobile-manifest-plist](rules/mobile-manifest-plist.md) - Manifest Plist.
- [mobile-permissions](rules/mobile-permissions.md) - Permissions.
- [mobile-plugin-bindings](rules/mobile-plugin-bindings.md) - Plugin Bindings.
- [mobile-multiwindow](rules/mobile-multiwindow.md) - Multiwindow.
- [mobile-store-constraints](rules/mobile-store-constraints.md) - Store Constraints.

### sec
- [sec-runtime-authority](rules/sec-runtime-authority.md) - Runtime Authority.
- [sec-least-privilege](rules/sec-least-privilege.md) - Least Privilege.
- [sec-capability-boundaries](rules/sec-capability-boundaries.md) - Capability Boundaries.
- [sec-permission-identifiers](rules/sec-permission-identifiers.md) - Permission Identifiers.
- [sec-command-sets](rules/sec-command-sets.md) - Command Sets.
- [sec-scopes](rules/sec-scopes.md) - Scopes.
- [sec-plugin-permissions](rules/sec-plugin-permissions.md) - Plugin Permissions.
- [sec-custom-permissions](rules/sec-custom-permissions.md) - Custom Permissions.
- [sec-remote-api](rules/sec-remote-api.md) - Remote Api.
- [sec-csp](rules/sec-csp.md) - Csp.
- [sec-http-headers](rules/sec-http-headers.md) - Http Headers.
- [sec-asset-protocol](rules/sec-asset-protocol.md) - Asset Protocol.
- [sec-secret-boundaries](rules/sec-secret-boundaries.md) - Secret Boundaries.
- [sec-supply-chain](rules/sec-supply-chain.md) - Supply Chain.

### err
- [err-domain-errors](rules/err-domain-errors.md) - Domain Errors.
- [err-internal-chains](rules/err-internal-chains.md) - Internal Chains.
- [err-frontend-messages](rules/err-frontend-messages.md) - Frontend Messages.
- [err-panic-boundaries](rules/err-panic-boundaries.md) - Panic Boundaries.
- [err-logging](rules/err-logging.md) - Logging.
- [err-structured-fields](rules/err-structured-fields.md) - Structured Fields.
- [err-redaction](rules/err-redaction.md) - Redaction.
- [err-correlation](rules/err-correlation.md) - Correlation.

### test
- [test-rust-unit](rules/test-rust-unit.md) - Rust Unit.
- [test-command-extraction](rules/test-command-extraction.md) - Command Extraction.
- [test-app-handle](rules/test-app-handle.md) - App Handle.
- [test-frontend-mocks](rules/test-frontend-mocks.md) - Frontend Mocks.
- [test-events](rules/test-events.md) - Events.
- [test-webdriver](rules/test-webdriver.md) - Webdriver.
- [test-selenium](rules/test-selenium.md) - Selenium.
- [test-webdriverio](rules/test-webdriverio.md) - Webdriverio.
- [test-ci-display](rules/test-ci-display.md) - Ci Display.
- [test-packaging-smoke](rules/test-packaging-smoke.md) - Packaging Smoke.
- [test-security-regression](rules/test-security-regression.md) - Security Regression.

### debug
- [debug-frontend-devtools](rules/debug-frontend-devtools.md) - Frontend Devtools.
- [debug-rust-backtraces](rules/debug-rust-backtraces.md) - Rust Backtraces.
- [debug-rust-log](rules/debug-rust-log.md) - Rust Log.
- [debug-vscode](rules/debug-vscode.md) - Vscode.
- [debug-rustrover](rules/debug-rustrover.md) - Rustrover.
- [debug-neovim](rules/debug-neovim.md) - Neovim.
- [debug-webview-inspection](rules/debug-webview-inspection.md) - Webview Inspection.
- [debug-linux-graphics](rules/debug-linux-graphics.md) - Linux Graphics.
- [debug-packaged-only](rules/debug-packaged-only.md) - Packaged Only.

### perf
- [perf-startup](rules/perf-startup.md) - Startup.
- [perf-plugin-count](rules/perf-plugin-count.md) - Plugin Count.
- [perf-release-profile](rules/perf-release-profile.md) - Release Profile.
- [perf-binary-size](rules/perf-binary-size.md) - Binary Size.
- [perf-cargo-features](rules/perf-cargo-features.md) - Cargo Features.
- [perf-webview-count](rules/perf-webview-count.md) - Webview Count.
- [perf-ipc-size](rules/perf-ipc-size.md) - Ipc Size.
- [perf-channel-backpressure](rules/perf-channel-backpressure.md) - Channel Backpressure.
- [perf-listener-fanout](rules/perf-listener-fanout.md) - Listener Fanout.
- [perf-lock-contention](rules/perf-lock-contention.md) - Lock Contention.
- [perf-blocking-work](rules/perf-blocking-work.md) - Blocking Work.
- [perf-resource-loading](rules/perf-resource-loading.md) - Resource Loading.

### bundle
- [bundle-macos](rules/bundle-macos.md) - Macos.
- [bundle-dmg](rules/bundle-dmg.md) - Dmg.
- [bundle-windows](rules/bundle-windows.md) - Windows.
- [bundle-linux-appimage](rules/bundle-linux-appimage.md) - Linux Appimage.
- [bundle-linux-deb](rules/bundle-linux-deb.md) - Linux Deb.
- [bundle-linux-rpm](rules/bundle-linux-rpm.md) - Linux Rpm.
- [bundle-flatpak](rules/bundle-flatpak.md) - Flatpak.
- [bundle-snapcraft](rules/bundle-snapcraft.md) - Snapcraft.
- [bundle-aur](rules/bundle-aur.md) - Aur.
- [bundle-android](rules/bundle-android.md) - Android.
- [bundle-ios](rules/bundle-ios.md) - Ios.

### sign
- [sign-macos](rules/sign-macos.md) - Macos.
- [sign-windows](rules/sign-windows.md) - Windows.
- [sign-android](rules/sign-android.md) - Android.
- [sign-ios](rules/sign-ios.md) - Ios.
- [sign-linux](rules/sign-linux.md) - Linux.
- [sign-ci-secrets](rules/sign-ci-secrets.md) - Ci Secrets.
- [sign-verify](rules/sign-verify.md) - Verify.

### update
- [update-desktop-scope](rules/update-desktop-scope.md) - Desktop Scope.
- [update-signatures](rules/update-signatures.md) - Signatures.
- [update-keys](rules/update-keys.md) - Keys.
- [update-endpoints](rules/update-endpoints.md) - Endpoints.
- [update-feeds](rules/update-feeds.md) - Feeds.
- [update-channels](rules/update-channels.md) - Channels.
- [update-rollout](rules/update-rollout.md) - Rollout.
- [update-ux](rules/update-ux.md) - Ux.

### ci
- [ci-matrix](rules/ci-matrix.md) - Matrix.
- [ci-toolchains](rules/ci-toolchains.md) - Toolchains.
- [ci-lockfiles](rules/ci-lockfiles.md) - Lockfiles.
- [ci-caches](rules/ci-caches.md) - Caches.
- [ci-native-deps](rules/ci-native-deps.md) - Native Deps.
- [ci-signing-isolation](rules/ci-signing-isolation.md) - Signing Isolation.
- [ci-artifacts](rules/ci-artifacts.md) - Artifacts.
- [ci-provenance](rules/ci-provenance.md) - Provenance.
- [ci-gates](rules/ci-gates.md) - Gates.

### migrate
- [migrate-dependencies](rules/migrate-dependencies.md) - Dependencies.
- [migrate-cli](rules/migrate-cli.md) - Cli.
- [migrate-config](rules/migrate-config.md) - Config.
- [migrate-allowlist](rules/migrate-allowlist.md) - Allowlist.
- [migrate-permissions](rules/migrate-permissions.md) - Permissions.
- [migrate-core-api](rules/migrate-core-api.md) - Core Api.
- [migrate-plugins](rules/migrate-plugins.md) - Plugins.
- [migrate-js-imports](rules/migrate-js-imports.md) - Js Imports.
- [migrate-rust-api](rules/migrate-rust-api.md) - Rust Api.
- [migrate-updater](rules/migrate-updater.md) - Updater.
- [migrate-shell-fs-deeplink](rules/migrate-shell-fs-deeplink.md) - Shell Fs Deeplink.
- [migrate-regression](rules/migrate-regression.md) - Regression.

### anti
- [anti-global-capabilities](rules/anti-global-capabilities.md) - Global Capabilities.
- [anti-blanket-plugin-permissions](rules/anti-blanket-plugin-permissions.md) - Blanket Plugin Permissions.
- [anti-remote-content-trust](rules/anti-remote-content-trust.md) - Remote Content Trust.
- [anti-stringly-ipc](rules/anti-stringly-ipc.md) - Stringly Ipc.
- [anti-string-errors](rules/anti-string-errors.md) - String Errors.
- [anti-blocking-async](rules/anti-blocking-async.md) - Blocking Async.
- [anti-lock-across-await](rules/anti-lock-across-await.md) - Lock Across Await.
- [anti-unbounded-events](rules/anti-unbounded-events.md) - Unbounded Events.
- [anti-leaked-listeners](rules/anti-leaked-listeners.md) - Leaked Listeners.
- [anti-shell-interpolation](rules/anti-shell-interpolation.md) - Shell Interpolation.
- [anti-unvalidated-urls](rules/anti-unvalidated-urls.md) - Unvalidated Urls.
- [anti-orphan-sidecars](rules/anti-orphan-sidecars.md) - Orphan Sidecars.
- [anti-frontend-secrets](rules/anti-frontend-secrets.md) - Frontend Secrets.
- [anti-dev-path-assumptions](rules/anti-dev-path-assumptions.md) - Dev Path Assumptions.
- [anti-platform-assumptions](rules/anti-platform-assumptions.md) - Platform Assumptions.
- [anti-unsigned-updates](rules/anti-unsigned-updates.md) - Unsigned Updates.
- [anti-release-only-testing](rules/anti-release-only-testing.md) - Release Only Testing.

## Completion Checklist

- Confirm applicable formatting, linting, unit, integration, frontend, WebDriver, or packaging smoke checks were run for the changed surface.
- Review capabilities and permissions for least privilege, including plugin scopes and remote URL exposure.
- Check every claimed target platform against docs, installed packages, generated schemas, and actual project configuration.
- For release, signing, updater, or CI changes, verify artifacts, signatures, endpoints, checksums, secrets, and rollback path.
- Cite source/version confirmation and avoid unsupported Tauri v1 or mobile claims.
