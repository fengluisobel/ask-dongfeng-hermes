#!/usr/bin/env python3
"""Smoke-check that Ask DongFeng is bundled as a Hermes built-in skill."""

from __future__ import annotations

from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile


REQUIRED_PATHS = [
    "skills/software-development/ask-dongfeng/SKILL.md",
    "skills/software-development/ask-dongfeng/references",
    "skills/software-development/ask-dongfeng/scripts",
    "skills/software-development/ask-dongfeng/agents",
    "skills/software-development/ask-dongfeng/scripts/validate_artifact.py",
    "skills/software-development/ask-dongfeng/scripts/validate_skill.py",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    missing: list[str] = []
    for rel in REQUIRED_PATHS:
        if not (repo_root / rel).exists():
            missing.append(rel)

    skill_md = repo_root / "skills/software-development/ask-dongfeng/SKILL.md"
    content = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    checks = {
        "frontmatter name": "name: ask-dongfeng" in content,
        "DongFeng Packet": "DongFeng Packet" in content,
        "control artifact": "control-artifact" in content,
        "operating modes": "intent-to-spec" in content and "review-gate" in content,
    }

    failed_checks = [name for name, ok in checks.items() if not ok]

    if missing or failed_checks:
        if missing:
            print("Missing required paths:", file=sys.stderr)
            for rel in missing:
                print(f"  - {rel}", file=sys.stderr)
        if failed_checks:
            print("Failed content checks:", file=sys.stderr)
            for name in failed_checks:
                print(f"  - {name}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="ask-dongfeng-hermes-home-") as tmp_home:
        env = os.environ.copy()
        env["HERMES_HOME"] = tmp_home
        env["HERMES_BUNDLED_SKILLS"] = str(repo_root / "skills")

        sync = subprocess.run(
            [
                sys.executable,
                "-c",
                "from tools.skills_sync import sync_skills; "
                "r = sync_skills(quiet=True); "
                "raise SystemExit(0 if 'ask-dongfeng' in r.get('copied', []) or r.get('skipped', 0) >= 0 else 1)",
            ],
            cwd=repo_root,
            env=env,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=60,
        )
        if sync.returncode != 0:
            print("Bundled skill sync failed.", file=sys.stderr)
            print(sync.stdout, file=sys.stderr)
            print(sync.stderr, file=sys.stderr)
            return sync.returncode

        listing = subprocess.run(
            [
                sys.executable,
                "-m",
                "hermes_cli.main",
                "skills",
                "list",
                "--source",
                "builtin",
                "--enabled-only",
            ],
            cwd=repo_root,
            env=env,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=60,
        )
        output = (listing.stdout or "") + (listing.stderr or "")
        if listing.returncode != 0 or "ask-dongfeng" not in output:
            print("Hermes did not list ask-dongfeng as a builtin skill after sync.", file=sys.stderr)
            print(output, file=sys.stderr)
            return listing.returncode or 1

        shutil.rmtree(tmp_home, ignore_errors=True)

    print("PASS: Ask DongFeng built-in skill files are present and recognizable.")
    print("PASS: Hermes lists ask-dongfeng as a builtin skill after bundled sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
