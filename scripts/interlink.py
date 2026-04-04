#!/usr/bin/env python3
"""
Interlink Naval Wiki — add [[wiki-links]] for first occurrence of known frameworks.

Scans all markdown files in site/content/. For each file, finds mentions of known
page titles (frameworks) and wraps the FIRST unlinked occurrence
in a [[slug|display text]] wiki link.

Rules:
- Only links the first occurrence per page
- Skips text already inside wiki links [[...]]
- Skips text inside markdown links [text](url)
- Skips text inside headings (# lines)
- Skips text inside frontmatter (--- blocks)
- Skips text inside code blocks (``` blocks)
- Skips self-references (don't link a page to itself)
- Longer titles match first (prevents partial matches)
"""

import os
import re
import yaml
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "site" / "content"

# Directories to scan for linkable pages
LINKABLE_DIRS = ["frameworks"]

# Directories to process (add links into)
PROCESS_DIRS = ["frameworks"]

def extract_titles(content_dir: Path) -> dict[str, tuple[str, str]]:
    """Build map of display_title -> (slug, folder) for all linkable pages."""
    titles = {}

    for dirname in LINKABLE_DIRS:
        dirpath = content_dir / dirname
        if not dirpath.exists():
            continue

        for md_file in dirpath.glob("*.md"):
            slug = md_file.stem

            # Read frontmatter
            text = md_file.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue

            end = text.find("---", 3)
            if end == -1:
                continue

            try:
                fm = yaml.safe_load(text[3:end])
            except yaml.YAMLError:
                continue

            # Naval wiki uses "name" instead of "title"
            if not fm or "name" not in fm:
                continue

            title = fm["name"].strip()

            titles[title] = (slug, dirname)

            # For titles with long names like "The Addiction Framework: Why Modern Addictions..."
            # also register the short version before the colon
            if ":" in title:
                short = title.split(":")[0].strip()
                if len(short) > 3:
                    if short not in titles:
                        titles[short] = (slug, dirname)

    return titles


def is_in_protected_zone(text: str, match_start: int, match_end: int) -> bool:
    """Check if a match position is inside a protected zone (link, code, etc.)."""

    # Check if inside an existing wiki link [[...]]
    # Find the nearest [[ before the match
    before = text[:match_start]
    open_wiki = before.rfind("[[")
    close_wiki = before.rfind("]]")
    if open_wiki > close_wiki:
        # We're inside an unclosed [[
        return True

    # Check if inside a markdown link [text](url)
    # Look for [ before us that hasn't been closed with ](
    bracket_open = before.rfind("[")
    bracket_close = before.rfind("]")
    if bracket_open > bracket_close and bracket_open >= 0:
        return True

    # Check if inside a markdown link URL part ](url)
    paren_pattern = before.rfind("](")
    paren_close = before.rfind(")")
    if paren_pattern > paren_close and paren_pattern >= 0:
        return True

    # Check if inside inline code `...`
    backtick_count = before.count("`")
    if backtick_count % 2 == 1:
        return True

    return False


def is_heading_line(text: str, match_start: int) -> bool:
    """Check if the match is on a heading line."""
    line_start = text.rfind("\n", 0, match_start) + 1
    line = text[line_start:match_start].lstrip()
    return line.startswith("#")


def add_links(filepath: Path, titles: dict[str, tuple[str, str]], dry_run: bool = False) -> int:
    """Add wiki links to a single file. Returns count of links added."""
    text = filepath.read_text(encoding="utf-8")

    # Extract frontmatter
    if not text.startswith("---"):
        return 0

    fm_end = text.find("---", 3)
    if fm_end == -1:
        return 0

    fm_end += 3  # Include the closing ---
    frontmatter = text[:fm_end]
    body = text[fm_end:]

    # Get this file's own slug to avoid self-linking
    own_slug = filepath.stem

    # Split body into code blocks and non-code blocks
    # We only process non-code blocks
    code_block_pattern = re.compile(r'(```[\s\S]*?```)', re.MULTILINE)

    # Track which titles we've already linked in this file
    linked = set()

    # Sort titles by length (longest first) to prevent partial matches
    sorted_titles = sorted(titles.keys(), key=len, reverse=True)

    links_added = 0

    for title in sorted_titles:
        slug, folder = titles[title]

        # Skip self-references
        if slug == own_slug:
            continue

        # Skip if we already linked this slug
        if slug in linked:
            continue

        # Skip if this title is too short (risk of false positives)
        if len(title) < 4:
            continue

        # Build regex pattern — match whole words, case-sensitive
        # Escape regex special chars in title
        escaped = re.escape(title)
        pattern = re.compile(r'(?<!\[)(?<!\w)' + escaped + r'(?!\w)(?!\])', re.MULTILINE)

        # Find all matches in body
        for match in pattern.finditer(body):
            start = match.start()
            end = match.end()

            # Check protections
            if is_in_protected_zone(body, start, end):
                continue

            if is_heading_line(body, start):
                continue

            # Check if inside code block
            in_code = False
            for cb in code_block_pattern.finditer(body):
                if cb.start() <= start < cb.end():
                    in_code = True
                    break
            if in_code:
                continue

            # Check if the text right before is already a wiki link opener
            before_text = body[max(0, start-2):start]
            if "[[" in before_text:
                continue

            # Build the wiki link
            matched_text = match.group()
            # Use shortest-path resolution (Quartz CrawlLinks setting)
            link = f"[[{slug}|{matched_text}]]"

            # Replace only this first occurrence
            body = body[:start] + link + body[end:]
            linked.add(slug)
            links_added += 1
            break  # Only first occurrence

    if links_added > 0 and not dry_run:
        filepath.write_text(frontmatter + body, encoding="utf-8")

    return links_added


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Interlink Naval Wiki pages")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be linked without changing files")
    parser.add_argument("--verbose", action="store_true", help="Show per-file details")
    args = parser.parse_args()

    print("Building title index...")
    titles = extract_titles(CONTENT_DIR)
    print(f"  Found {len(titles)} linkable titles")

    # Show some examples
    frameworks = [(t, s) for t, (s, d) in titles.items() if d == "frameworks"]
    print(f"  Frameworks: {len(frameworks)}")

    total_links = 0
    files_modified = 0

    for dirname in PROCESS_DIRS:
        dirpath = CONTENT_DIR / dirname
        if not dirpath.exists():
            continue

        files = sorted(dirpath.glob("*.md"))
        dir_links = 0

        for filepath in files:
            count = add_links(filepath, titles, dry_run=args.dry_run)
            if count > 0:
                dir_links += count
                files_modified += 1
                if args.verbose:
                    print(f"  {filepath.name}: +{count} links")

        total_links += dir_links
        print(f"\n{dirname}/: {dir_links} links added across {len(files)} files")

    mode = "would add" if args.dry_run else "added"
    print(f"\nTotal: {mode} {total_links} links in {files_modified} files")


if __name__ == "__main__":
    main()
