#!/usr/bin/env python3
"""Checks README.md entries for consistent formatting.

Runs automatically on every pull request. Run it yourself with:
    python3 scripts/check_format.py
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

STATUSES = {"Live", "Early Access", "Beta", "Alpha", "Playtest", "In Development"}
PLATFORMS = {"PC", "Mac", "Linux", "Browser", "Mobile", "Console", "Telnet"}

GAME_SECTIONS = {
    "Indie MMORPGs",
    "Free-to-Play MMORPGs",
    "In Development",
    "Open-Source MMORPGs",
    "Browser and Text MMOs",
}
TOOL_SECTIONS = {"Engines, Frameworks and Server Kits"}
RESOURCE_SECTIONS = {"Dev Resources and Communities"}

HYPE_WORDS = re.compile(
    r"\b(best|greatest|amazing|awesome|revolutionary|incredible|ultimate|#1|number one)\b",
    re.IGNORECASE,
)

ENTRY = re.compile(
    r"^- \[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\) - "
    r"(?P<desc>[A-Z0-9\"'].*?[.!?])(?P<tags>(?: `[^`]+`)*)$"
)


def sort_key(name: str) -> str:
    return name.casefold()


def main() -> int:
    errors = []
    section = None
    names_in_block = []
    seen_urls = {}

    def check_order(block, sec):
        for (prev_line, prev), (line_no, cur) in zip(block, block[1:]):
            if sort_key(cur) < sort_key(prev):
                errors.append(
                    f"line {line_no}: '{cur}' should come before '{prev}' "
                    f"(entries in '{sec}' must be alphabetical)"
                )

    lines = README.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, start=1):
        if line.startswith("## ") or line.startswith("### "):
            check_order(names_in_block, section)
            names_in_block = []
            if line.startswith("## "):
                section = line[3:].strip()
            continue

        if not line.startswith("- [") or section not in (
            GAME_SECTIONS | TOOL_SECTIONS | RESOURCE_SECTIONS
        ):
            continue

        m = ENTRY.match(line)
        if not m:
            errors.append(
                f"line {i}: doesn't match the format "
                "'- [Name](https://link) - Sentence ending with a period. `Tag`'"
            )
            continue

        name, url, desc = m["name"], m["url"], m["desc"]
        tags = re.findall(r"`([^`]+)`", m["tags"])
        names_in_block.append((i, name))

        if url in seen_urls:
            errors.append(f"line {i}: duplicate link (also on line {seen_urls[url]})")
        seen_urls[url] = i

        if len(desc.split()) > 30:
            errors.append(f"line {i}: description is long; please keep it to one short sentence")
        if HYPE_WORDS.search(desc):
            errors.append(f"line {i}: please avoid hype words like 'best' or 'amazing' in descriptions")

        if section in GAME_SECTIONS:
            statuses = [t for t in tags if t in STATUSES]
            unknown = [t for t in tags if t not in STATUSES | PLATFORMS]
            if len(statuses) != 1:
                errors.append(
                    f"line {i}: needs exactly one status tag, one of: "
                    + ", ".join(sorted(STATUSES))
                )
            elif tags and tags[0] not in STATUSES:
                errors.append(f"line {i}: the status tag should come first")
            if not any(t in PLATFORMS for t in tags):
                errors.append(f"line {i}: add at least one platform tag: " + ", ".join(sorted(PLATFORMS)))
            if unknown:
                errors.append(f"line {i}: unknown tag(s): {', '.join(unknown)}")
        elif section in TOOL_SECTIONS:
            if len(tags) != 2:
                errors.append(f"line {i}: tools need two tags: `License` `Language`")
        elif section in RESOURCE_SECTIONS:
            if tags:
                errors.append(f"line {i}: resources don't need tags")

    check_order(names_in_block, section)

    if errors:
        print("Formatting problems found in README.md:\n")
        for e in errors:
            print("  - " + e)
        print("\nSee CONTRIBUTING.md for the format. Thanks for contributing!")
        return 1

    print(f"README.md looks good ({len(seen_urls)} entries checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
