#!/usr/bin/env python3

from pathlib import Path
import sys


def extract_checklist_items(path: Path):
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ]") or stripped.startswith("- [x]"):
            items.append(stripped)
    return items


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: checklist-helper.py <markdown-file>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    items = extract_checklist_items(path)
    print(f"Checklist items: {len(items)}")
    for item in items:
        print(item)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
