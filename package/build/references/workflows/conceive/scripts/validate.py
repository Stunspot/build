#!/usr/bin/env python3
"""Check CONCEIVE runtime structure; this does not evaluate model behavior."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROLES = {
    "taylor-reed": "Taylor Reed",
    "morgan-hayes": "Morgan Hayes",
    "alex-jordan": "Alex Jordan",
    "calvin-merrick": "Calvin Merrick",
    "nathan-vantage": "Nathan Vantage",
}
REQUIRED = (
    "SKILL.md", "agents/openai.yaml", "references/deliberation.md",
    "references/native-coordination.md", "references/handoff.md",
    "assets/participant-brief.md", "assets/session-record.md",
    "assets/design-handoff.md", "examples/community-workshop.md",
    "evals/cases.md", "sources/PROVENANCE.md", "sources/source-manifest.json",
    "sources/thunktank-t3-original.txt",
)


def quoted_field(text: str, name: str) -> str | None:
    match = re.search(rf'^\s*{re.escape(name)}:\s*"([^"\r\n]*)"\s*$', text, re.M)
    return match.group(1) if match else None


def validate(root: Path) -> dict:
    errors: list[str] = []
    checked_links = 0
    for relative in (*REQUIRED, *(f"roles/{slug}.md" for slug in ROLES)):
        path = root / relative
        if not path.is_file():
            errors.append(f"Missing required runtime file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty required runtime file: {relative}")
    if errors:
        return {"ok": False, "errors": errors, "scope": "runtime structure only"}

    skill = (root / "SKILL.md").read_text(encoding="utf-8-sig")
    metadata = (root / "agents/openai.yaml").read_text(encoding="utf-8-sig")
    description = quoted_field(skill, "description")
    if not description or description != quoted_field(metadata, "short_description"):
        errors.append("description and short_description must be present and identical")
    if not re.search(r"^name: conceive\s*$", skill, re.M):
        errors.append("Skill identifier must be conceive")
    if quoted_field(skill, "version") != "0.1.0":
        errors.append("Runtime version must be 0.1.0")
    if quoted_field(metadata, "display_name") != "CONCEIVE":
        errors.append("Display name must be CONCEIVE")

    role_files = {path.stem for path in (root / "roles").glob("*.md")}
    if role_files != set(ROLES):
        errors.append(f"Expected exactly five named role files; found {sorted(role_files)}")
    for slug, name in ROLES.items():
        role_text = (root / "roles" / f"{slug}.md").read_text(encoding="utf-8-sig")
        if not role_text.startswith(f"# {name} — "):
            errors.append(f"Role identity mismatch: {slug}")
        if f"roles/{slug}.md" not in skill:
            errors.append(f"Entrypoint does not link role seed: {slug}")

    try:
        manifest = json.loads((root / "sources/source-manifest.json").read_text(encoding="utf-8-sig"))
        source_path = (root / "sources" / manifest["file"]).resolve()
        source_path.relative_to((root / "sources").resolve())
        source_bytes = source_path.read_bytes()
        if hashlib.sha256(source_bytes).hexdigest() != manifest["sha256"]:
            errors.append("Preserved source SHA-256 differs from source manifest")
        if len(source_bytes) != manifest["bytes"]:
            errors.append("Preserved source byte size differs from source manifest")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid source manifest or path: {exc}")

    for path in root.rglob("*.md"):
        try:
            body = path.read_text(encoding="utf-8-sig")
        except UnicodeError as exc:
            errors.append(f"Non-UTF-8 Markdown: {path.relative_to(root)}: {exc}")
            continue
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", body):
            target = target.strip().strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                if not target.startswith(("https://", "http://", "mailto:")):
                    errors.append(f"Unsupported absolute link in {path.relative_to(root)}: {target}")
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            resolved = (path.parent / local).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"Link escapes runtime in {path.relative_to(root)}: {target}")
                continue
            checked_links += 1
            if not resolved.is_file():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")

    return {
        "ok": not errors,
        "version": "0.1.0",
        "role_files": len(role_files),
        "local_links_checked": checked_links,
        "source_identity": "matches recorded original" if not any("source" in e.lower() for e in errors) else "failed",
        "metadata_parity": bool(description and description == quoted_field(metadata, "short_description")),
        "errors": errors,
        "scope": "Source identity, metadata and runtime resource structure; not native launch, separate-context execution, design quality or user value.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
