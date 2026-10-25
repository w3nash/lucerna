#!/usr/bin/env python3
"""Add fenced incorrect/correct examples to every Tauri rule and refresh the mirror."""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Dict, Tuple


Example = Tuple[str, str, str]

EXAMPLES: Dict[str, Example] = {
    "arch": (
        "typescript",
        "const contents = await fetch('file:///Users/example/secret.txt').then(r => r.text());\n"
        "await fetch('https://example.com/upload', { method: 'POST', body: contents });",
        "const report = await invoke<Report>('load_report', {\n"
        "  request: { reportId },\n"
        "});\n"
        "// Rust owns filesystem access; the window capability exposes only load_report.",
    ),
    "setup": (
        "bash",
        "npm install @tauri-apps/api@latest\ncargo add tauri",
        "npm install @tauri-apps/api@2 @tauri-apps/cli@2\n"
        "cargo add tauri@2\n"
        "npx tauri info",
    ),
    "front": (
        "typescript",
        "export default defineConfig({ server: { port: 0 }, build: { ssr: true } });",
        "export default defineConfig({\n"
        "  server: { strictPort: true, port: 1420 },\n"
        "  envPrefix: ['VITE_', 'TAURI_'],\n"
        "  build: { target: 'es2021' },\n"
        "});",
    ),
    "config": (
        "json",
        '{"tauri":{"allowlist":{"all":true}},"build":{"devPath":"http://localhost:3000"}}',
        '{"$schema":"https://schema.tauri.app/config/2",'
        '"identifier":"com.example.app",'
        '"build":{"devUrl":"http://localhost:1420","frontendDist":"../dist"}}',
    ),
    "life": (
        "rust",
        "tauri::Builder::default().setup(|_app| {\n"
        "    std::thread::spawn(run_background_loop);\n"
        "    Ok(())\n"
        "});",
        "tauri::Builder::default().setup(|app| {\n"
        "    let token = CancellationToken::new();\n"
        "    app.manage(AppTasks { shutdown: token.clone() });\n"
        "    tauri::async_runtime::spawn(run_background_loop(token));\n"
        "    Ok(())\n"
        "});",
    ),
    "ipc": (
        "rust",
        "#[tauri::command]\n"
        "async fn import_file(path: String) -> Result<String, String> {\n"
        '    Ok(format!("imported {path}"))\n'
        "}",
        "#[derive(serde::Deserialize)]\n"
        '#[serde(rename_all = "camelCase")]\n'
        "struct ImportFileRequest { path: String }\n\n"
        "#[derive(serde::Serialize)]\n"
        '#[serde(rename_all = "camelCase")]\n'
        "struct ImportFileResponse { imported_id: String }\n\n"
        "#[tauri::command]\n"
        "async fn import_file(\n"
        "    request: ImportFileRequest,\n"
        ") -> Result<ImportFileResponse, ImportFileError> {\n"
        "    validate_path(&request.path)?;\n"
        '    Ok(ImportFileResponse { imported_id: "file_123".into() })\n'
        "}",
    ),
    "event": (
        "typescript",
        "listen('status', event => console.log(event.payload));",
        "const unlisten = await listen<{ jobId: string; state: string }>(\n"
        "  'job://status/v1',\n"
        "  event => renderStatus(event.payload),\n"
        ");\n"
        "unlisten();",
    ),
    "state": (
        "rust",
        "let mut state = state.lock().unwrap();\n"
        "upload_to_server(&state.buffer).await;",
        "let buffer = {\n"
        "    let state = state.lock().await;\n"
        "    state.buffer.clone()\n"
        "};\n"
        "upload_to_server(&buffer).await;",
    ),
    "window": (
        "rust",
        'WebviewWindowBuilder::new(app, "main", WebviewUrl::External(url.parse()?))\n'
        "    .build()?;",
        'WebviewWindowBuilder::new(app, "settings", WebviewUrl::App("/settings".into()))\n'
        '    .title("Settings")\n'
        "    .build()?;",
    ),
    "resource": (
        "rust",
        'let template = std::fs::read_to_string("../assets/template.html")?;',
        "let template = app\n"
        "    .path()\n"
        '    .resolve("templates/template.html", BaseDirectory::Resource)\n'
        "    .and_then(std::fs::read_to_string)?;",
    ),
    "sidecar": (
        "rust",
        'Command::new("sh")\n'
        '    .arg("-c")\n'
        '    .arg(format!("converter {input}"))\n'
        "    .spawn()?;",
        "let sidecar = app\n"
        "    .shell()\n"
        '    .sidecar("converter")?\n'
        "    .arg(validated_input);\n"
        "let (mut events, child) = sidecar.spawn()?;",
    ),
    "plugin": (
        "rust",
        "tauri::Builder::default()\n"
        "    .run(tauri::generate_context!())?;\n"
        "// Frontend calls a plugin that was never initialized.",
        "tauri::Builder::default()\n"
        "    .plugin(tauri_plugin_opener::init())\n"
        "    .run(tauri::generate_context!())?;\n"
        "// Grant only the required opener permission to the intended capability.",
    ),
    "mobile": (
        "rust",
        "#[tauri::command]\n"
        "fn open_secondary_window(app: tauri::AppHandle) -> tauri::Result<()> {\n"
        "    create_desktop_window(&app)\n"
        "}",
        "#[cfg(desktop)]\n"
        "fn open_secondary_window(app: tauri::AppHandle) -> tauri::Result<()> {\n"
        "    create_desktop_window(&app)\n"
        "}\n\n"
        "#[cfg(mobile)]\n"
        "fn open_secondary_window(_app: tauri::AppHandle) -> tauri::Result<()> {\n"
        '    Err(tauri::Error::AssetNotFound("mobile multiwindow unsupported".into()))\n'
        "}",
    ),
    "sec": (
        "json",
        '{"identifier":"all-access","windows":["*"],'
        '"permissions":["shell:default","fs:default","http:default","opener:default"]}',
        '{"identifier":"main-report-export","windows":["main"],'
        '"permissions":["core:default",'
        '{"identifier":"fs:allow-write-text-file",'
        '"allow":[{"path":"$DOCUMENT/reports/*.csv"}]}]}',
    ),
    "err": (
        "rust",
        'database_load(id).map_err(|error| format!("{error:?}"))',
        "#[derive(serde::Serialize)]\n"
        '#[serde(tag = "code", rename_all = "snake_case")]\n'
        "enum ProfileError { NotFound, PermissionDenied }\n\n"
        "database_load(id).map_err(map_profile_error)",
    ),
    "test": (
        "typescript",
        "test('exports', async () => { await exportReport(); });",
        "test('exports through a typed command', async () => {\n"
        "  const invoke = vi.fn().mockResolvedValue({ path: '/tmp/report.csv' });\n"
        "  await exportReport({ patientId: 'p_123' }, { invoke });\n"
        "  expect(invoke).toHaveBeenCalledWith('export_report', {\n"
        "    request: { patientId: 'p_123' },\n"
        "  });\n"
        "});",
    ),
    "debug": (
        "bash",
        "npm run tauri build\n# Rebuild repeatedly without logs or packaged-path evidence.",
        "RUST_LOG=tauri=trace,my_app=debug npm run tauri dev\n"
        "RUST_BACKTRACE=1 ./src-tauri/target/release/my-app\n"
        "npm run tauri info",
    ),
    "perf": (
        "rust",
        'rows.iter().map(|row| format!("{row:?}")).collect::<Vec<_>>().join("\\n")',
        "let row_count = rows.len();\n"
        "tauri::async_runtime::spawn_blocking(move || write_report_file(rows)).await??;\n"
        "Ok(ReportSummary { row_count })",
    ),
    "bundle": (
        "json",
        '{"bundle":{"active":true,"targets":"all"}}',
        '{"bundle":{"active":true,"targets":["dmg","nsis","appimage"],'
        '"icon":["icons/32x32.png","icons/icon.icns","icons/icon.ico"]}}',
    ),
    "sign": (
        "yaml",
        "- run: npm run tauri build\n"
        "  env:\n"
        "    APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}",
        "- run: npm run tauri build -- --no-bundle\n"
        "- run: ./scripts/sign-and-verify.sh\n"
        "  if: github.ref_type == 'tag'",
    ),
    "update": (
        "json",
        '{"bundle":{"createUpdaterArtifacts":true},'
        '"plugins":{"updater":{"endpoints":["https://updates.example.com/latest.json"]}}}',
        '{"bundle":{"createUpdaterArtifacts":"v1Compatible"},'
        '"plugins":{"updater":{"pubkey":"TAURI_UPDATER_PUBLIC_KEY",'
        '"endpoints":["https://updates.example.com/{{target}}/{{arch}}/{{current_version}}"]}}}',
    ),
    "ci": (
        "yaml",
        "runs-on: ubuntu-latest\n"
        "steps:\n"
        "  - run: npm run tauri build -- --target universal-apple-darwin",
        "strategy:\n"
        "  matrix:\n"
        "    os: [macos-latest, windows-latest, ubuntu-latest]\n"
        "runs-on: ${{ matrix.os }}\n"
        "steps:\n"
        "  - run: npm ci\n"
        "  - run: npm run tauri build",
    ),
    "migrate": (
        "json",
        '{"tauri":{"allowlist":{"all":true}}}',
        '{"identifier":"main-files","windows":["main"],'
        '"permissions":["core:default",'
        '{"identifier":"fs:allow-read-text-file",'
        '"allow":[{"path":"$DOCUMENT/*.txt"}]}]}',
    ),
    "anti": (
        "rust",
        "#[tauri::command]\n"
        "fn run_tool(input: String) {\n"
        '    Command::new("sh").arg("-c").arg(input).spawn().unwrap();\n'
        "}",
        "#[tauri::command]\n"
        "fn run_tool(request: ToolRequest) -> Result<(), ToolError> {\n"
        "    let argument = ValidatedArgument::try_from(request.argument)?;\n"
        '    Command::new("approved-tool").arg(argument.as_ref()).spawn()?;\n'
        "    Ok(())\n"
        "}",
    ),
}

SECTION_RE = re.compile(
    r"(^## (Incorrect|Correct)\n)(.*?)(?=^## |\Z)",
    flags=re.MULTILINE | re.DOTALL,
)


def add_examples(path: Path) -> bool:
    prefix = path.stem.split("-", 1)[0]
    language, incorrect, correct = EXAMPLES.get(prefix, EXAMPLES["arch"])
    text = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        heading, section, body = match.groups()
        prose = body.strip().split("```", 1)[0].strip()
        code = incorrect if section == "Incorrect" else correct
        return f"{heading}{prose}\n\n```{language}\n{code}\n```\n\n"

    updated = SECTION_RE.sub(replace, text)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def copy_mirror(canonical: Path, mirror: Path) -> None:
    if mirror.exists():
        shutil.rmtree(mirror)

    def ignore(_directory: str, names: list[str]) -> set[str]:
        return {
            name
            for name in names
            if name == "__pycache__" or name == ".DS_Store" or name.endswith(".pyc")
        }

    shutil.copytree(canonical, mirror, ignore=ignore)


def main() -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    repository = skill_dir.parents[2]
    rule_files = sorted((skill_dir / "rules").glob("*.md"))
    changed = sum(add_examples(path) for path in rule_files)
    copy_mirror(skill_dir, repository / ".claude" / "skills" / "tauri-skills")
    print(f"updated {changed} rules; refreshed mirror")


if __name__ == "__main__":
    main()
