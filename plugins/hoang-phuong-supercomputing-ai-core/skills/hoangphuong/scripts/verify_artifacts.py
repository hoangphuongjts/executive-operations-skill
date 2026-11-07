"""Verify artifact presence and SHA-256; never execute inspected files."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys


def verify_manifest(data: object) -> dict[str, object]:
    if not isinstance(data, dict) or set(data) != {"root", "artifacts"}:
        raise ValueError("Expected root and artifacts")
    if not isinstance(data["root"], str) or not Path(data["root"]).is_absolute():
        raise ValueError("root must be an absolute directory")
    root = Path(data["root"]).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("root must be a directory")
    entries = data["artifacts"]
    if not isinstance(entries, list) or not entries:
        raise ValueError("artifacts must be a nonempty list")
    seen: set[str] = set()
    results: list[dict[str, str]] = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"path", "sha256"}:
            raise ValueError("Each artifact needs path and sha256")
        name, expected = entry["path"], entry["sha256"]
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise ValueError("Artifact paths must be unique nonempty strings")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
            raise ValueError("sha256 must contain 64 hexadecimal characters")
        seen.add(name)
        relative = Path(name)
        # Reject Windows drive-relative paths and alternate data streams as well.
        if relative.is_absolute() or relative.drive or ":" in name or ".." in relative.parts:
            results.append({"path": name, "status": "outside_root"})
            continue
        try:
            target = (root / relative).resolve(strict=True)
            if not target.is_relative_to(root):
                status = "outside_root"
            elif not target.is_file():
                status = "not_file"
            else:
                digest = hashlib.sha256()
                with target.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                status = "verified" if digest.hexdigest() == expected.lower() else "hash_mismatch"
        except FileNotFoundError:
            status = "missing"
        except (OSError, RuntimeError):
            status = "unreadable"
        results.append({"path": name, "status": status})
    return {"ok": all(item["status"] == "verified" for item in results), "artifacts": results}


def main() -> int:
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: verify_artifacts.py manifest.json")
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
        result = verify_manifest(data)
    except (ValueError, OSError, RuntimeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=True))
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
