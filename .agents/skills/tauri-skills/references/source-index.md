# Official Tauri Source Index

- Research date (UTC): 2026-06-20
- Documentation repository: https://github.com/tauri-apps/tauri-docs
- Documentation branch: v2
- Documentation revision: 92d327ec5cbb5199f48d57ec1a6bc31b7b83aacd
- Version policy: inspect the target project's installed Tauri versions and generated schemas before applying version-sensitive guidance.
- Supporting local schema inspection: apps/desktop/node_modules/@tauri-apps/cli/config.schema.json and apps/desktop/src-tauri/gen/schemas/desktop-schema.json were inspected when present.

## Retained English topic roots

- src/content/docs/concept/
- src/content/docs/develop/
- src/content/docs/distribute/
- src/content/docs/learn/
- src/content/docs/plugin/
- src/content/docs/reference/
- src/content/docs/security/
- src/content/docs/start/

## Mapped topics

| Official path | Mapped rules | Status |
|---|---|---|
| src/content/docs/concept/Inter-Process Communication/brownfield.md | arch-ipc-boundary | mapped |
| src/content/docs/concept/Inter-Process Communication/index.mdx | arch-ipc-boundary | mapped |
| src/content/docs/concept/Inter-Process Communication/isolation.md | arch-isolation-choice | mapped |
| src/content/docs/concept/architecture.mdx | arch-platform-runtime | mapped |
| src/content/docs/concept/index.mdx | arch-platform-runtime | mapped |
| src/content/docs/concept/process-model.md | arch-process-model | mapped |
| src/content/docs/concept/size.mdx | arch-binary-size | mapped |
| src/content/docs/develop/Debug/crabnebula-devtools.mdx | debug-frontend-devtools | mapped |
| src/content/docs/develop/Debug/index.mdx | debug-frontend-devtools | mapped |
| src/content/docs/develop/Debug/linux-graphics.md | debug-linux-graphics | mapped |
| src/content/docs/develop/Debug/neovim.mdx | debug-neovim | mapped |
| src/content/docs/develop/Debug/rustrover.mdx | debug-rustrover | mapped |
| src/content/docs/develop/Debug/vscode.mdx | debug-vscode | mapped |
| src/content/docs/develop/Plugins/develop-mobile.mdx | plugin-custom-mobile | mapped |
| src/content/docs/develop/Plugins/index.mdx | plugin-architecture | mapped |
| src/content/docs/develop/Tests/WebDriver/Example/selenium.mdx | test-selenium | mapped |
| src/content/docs/develop/Tests/WebDriver/Example/webdriverio.mdx | test-webdriverio | mapped |
| src/content/docs/develop/Tests/WebDriver/ci.md | test-ci-display | mapped |
| src/content/docs/develop/Tests/WebDriver/index.mdx | test-webdriver | mapped |
| src/content/docs/develop/Tests/index.mdx | test-rust-unit | mapped |
| src/content/docs/develop/Tests/mocking.mdx | test-frontend-mocks | mapped |
| src/content/docs/develop/_sections/frontend-listen.mdx | arch-platform-runtime | mapped |
| src/content/docs/develop/calling-frontend.mdx | ipc-direct-vs-event, event-targeting | mapped |
| src/content/docs/develop/calling-rust.mdx | ipc-command-macro, ipc-typed-objects | mapped |
| src/content/docs/develop/configuration-files.mdx | config-tauri-conf | mapped |
| src/content/docs/develop/icons.mdx | resource-icons | mapped |
| src/content/docs/develop/index.mdx | arch-platform-runtime | mapped |
| src/content/docs/develop/resources.mdx | resource-directories | mapped |
| src/content/docs/develop/sidecar.mdx | sidecar-binaries | mapped |
| src/content/docs/develop/state-management.mdx | state-manage | mapped |
| src/content/docs/develop/updating-dependencies.mdx | setup-version-alignment | mapped |
| src/content/docs/distribute/Pipelines/crabnebula-cloud.mdx | ci-provenance | mapped |
| src/content/docs/distribute/Pipelines/github.mdx | ci-matrix | mapped |
| src/content/docs/distribute/Sign/android.mdx | sign-android | mapped |
| src/content/docs/distribute/Sign/ios.mdx | sign-ios | mapped |
| src/content/docs/distribute/Sign/linux.mdx | sign-linux | mapped |
| src/content/docs/distribute/Sign/macos.mdx | sign-macos | mapped |
| src/content/docs/distribute/Sign/windows.mdx | sign-windows | mapped |
| src/content/docs/distribute/app-store.mdx | bundle-ios | mapped |
| src/content/docs/distribute/appimage.mdx | bundle-linux-appimage | mapped |
| src/content/docs/distribute/aur.mdx | bundle-aur | mapped |
| src/content/docs/distribute/crabnebula-cloud.mdx | bundle-macos | mapped |
| src/content/docs/distribute/debian.mdx | bundle-linux-deb | mapped |
| src/content/docs/distribute/dmg.mdx | bundle-dmg | mapped |
| src/content/docs/distribute/flatpak.mdx | bundle-flatpak | mapped |
| src/content/docs/distribute/google-play.mdx | bundle-android | mapped |
| src/content/docs/distribute/index.mdx | bundle-macos | mapped |
| src/content/docs/distribute/macos-application-bundle.mdx | bundle-macos | mapped |
| src/content/docs/distribute/microsoft-store.mdx | bundle-macos | mapped |
| src/content/docs/distribute/rpm.mdx | bundle-linux-rpm | mapped |
| src/content/docs/distribute/snapcraft.mdx | bundle-snapcraft | mapped |
| src/content/docs/distribute/windows-installer.mdx | bundle-windows | mapped |
| src/content/docs/learn/Security/capabilities-for-windows-and-platforms.mdx | sec-capability-boundaries | mapped |
| src/content/docs/learn/Security/using-plugin-permissions.mdx | plugin-permissions | mapped |
| src/content/docs/learn/Security/writing-plugin-permissions.mdx | sec-custom-permissions | mapped |
| src/content/docs/learn/index.mdx | arch-platform-runtime | mapped |
| src/content/docs/learn/mobile-file-associations.mdx | mobile-manifest-plist | mapped |
| src/content/docs/learn/mobile-multiwindow.mdx | mobile-multiwindow | mapped |
| src/content/docs/learn/sidecar-nodejs.mdx | sidecar-packaging | mapped |
| src/content/docs/learn/splashscreen.mdx | window-splash | mapped |
| src/content/docs/learn/system-tray.mdx | window-tray | mapped |
| src/content/docs/learn/window-customization.mdx | window-title-bars | mapped |
| src/content/docs/learn/window-menu.mdx | window-menus | mapped |
| src/content/docs/plugin/autostart.mdx | plugin-autostart | mapped |
| src/content/docs/plugin/barcode-scanner.mdx | plugin-barcode-scanner | mapped |
| src/content/docs/plugin/biometric.mdx | plugin-biometric | mapped |
| src/content/docs/plugin/cli.mdx | plugin-cli | mapped |
| src/content/docs/plugin/clipboard.mdx | plugin-clipboard | mapped |
| src/content/docs/plugin/deep-linking.mdx | plugin-deep-linking | mapped |
| src/content/docs/plugin/dialog.mdx | plugin-dialog | mapped |
| src/content/docs/plugin/file-system.mdx | plugin-file-system | mapped |
| src/content/docs/plugin/geolocation.mdx | plugin-geolocation | mapped |
| src/content/docs/plugin/global-shortcut.mdx | plugin-global-shortcut | mapped |
| src/content/docs/plugin/haptics.mdx | plugin-haptics | mapped |
| src/content/docs/plugin/http-client.mdx | plugin-http-client | mapped |
| src/content/docs/plugin/index.mdx | plugin-architecture | mapped |
| src/content/docs/plugin/localhost.mdx | plugin-localhost | mapped |
| src/content/docs/plugin/logging.mdx | plugin-logging | mapped |
| src/content/docs/plugin/nfc.mdx | plugin-nfc | mapped |
| src/content/docs/plugin/notification.mdx | plugin-notification | mapped |
| src/content/docs/plugin/opener.mdx | plugin-opener | mapped |
| src/content/docs/plugin/os-info.mdx | plugin-os-info | mapped |
| src/content/docs/plugin/persisted-scope.mdx | plugin-persisted-scope | mapped |
| src/content/docs/plugin/positioner.mdx | plugin-positioner | mapped |
| src/content/docs/plugin/process.mdx | plugin-process | mapped |
| src/content/docs/plugin/shell.mdx | plugin-shell | mapped |
| src/content/docs/plugin/single-instance.mdx | plugin-single-instance | mapped |
| src/content/docs/plugin/sql.mdx | plugin-sql | mapped |
| src/content/docs/plugin/store.mdx | plugin-store | mapped |
| src/content/docs/plugin/stronghold.mdx | plugin-stronghold | mapped |
| src/content/docs/plugin/updater.mdx | plugin-updater | mapped |
| src/content/docs/plugin/upload.mdx | plugin-upload | mapped |
| src/content/docs/plugin/websocket.mdx | plugin-websocket | mapped |
| src/content/docs/plugin/window-state.mdx | plugin-window-state | mapped |
| src/content/docs/reference/_cli.mdx | config-generated-schemas | mapped |
| src/content/docs/reference/_cli_ios.mdx | config-generated-schemas | mapped |
| src/content/docs/reference/acl/core-permissions.mdx | sec-command-sets | mapped |
| src/content/docs/reference/environment-variables.mdx | config-env | mapped |
| src/content/docs/reference/webview-versions.md | arch-webview-variability | mapped |
| src/content/docs/security/asset-protocol.mdx | sec-asset-protocol | mapped |
| src/content/docs/security/capabilities.mdx | sec-least-privilege | mapped |
| src/content/docs/security/csp.mdx | sec-csp | mapped |
| src/content/docs/security/ecosystem.mdx | sec-least-privilege | mapped |
| src/content/docs/security/future.mdx | sec-least-privilege | mapped |
| src/content/docs/security/http-headers.mdx | sec-http-headers | mapped |
| src/content/docs/security/index.mdx | sec-least-privilege | mapped |
| src/content/docs/security/lifecycle.mdx | sec-least-privilege | mapped |
| src/content/docs/security/permissions.mdx | sec-least-privilege | mapped |
| src/content/docs/security/runtime-authority.mdx | sec-runtime-authority | mapped |
| src/content/docs/security/scope.mdx | sec-least-privilege | mapped |
| src/content/docs/start/create-project.mdx | setup-create-tauri-app | mapped |
| src/content/docs/start/frontend/index.mdx | front-framework-selection | mapped |
| src/content/docs/start/frontend/leptos.mdx | front-leptos | mapped |
| src/content/docs/start/frontend/nextjs.mdx | front-nextjs | mapped |
| src/content/docs/start/frontend/nuxt.mdx | front-nuxt | mapped |
| src/content/docs/start/frontend/qwik.mdx | front-qwik | mapped |
| src/content/docs/start/frontend/sveltekit.mdx | front-sveltekit | mapped |
| src/content/docs/start/frontend/trunk.mdx | front-trunk | mapped |
| src/content/docs/start/frontend/vite.mdx | front-vite | mapped |
| src/content/docs/start/index.mdx | arch-platform-runtime | mapped |
| src/content/docs/start/migrate/from-tauri-1.mdx | migrate-dependencies | mapped |
| src/content/docs/start/migrate/from-tauri-2-beta.mdx | migrate-dependencies | mapped |
| src/content/docs/start/migrate/index.mdx | migrate-config | mapped |
| src/content/docs/start/prerequisites.mdx | setup-prerequisites | mapped |
| src/content/docs/start/project-structure.mdx | setup-project-structure | mapped |

## Exclusions

| Official path | Reason |
|---|---|
| src/content/docs/index.mdx | Top-level index page outside retained implementation roots. |
| src/content/docs/start/index.mdx | Non-guidance section index page. |
| src/content/docs/concept/index.mdx | Non-guidance section index page. |
| src/content/docs/develop/index.mdx | Non-guidance section index page. |
| src/content/docs/distribute/index.mdx | Non-guidance section index page; distribution topics are mapped individually. |
| src/content/docs/learn/index.mdx | Non-guidance section index page. |
| src/content/docs/security/index.mdx | Non-guidance section index page. |
