#!/usr/bin/env python3
"""
Rename markdown files to match their H1 document titles.

Usage:
    python scripts/rename_to_titles.py              # Dry-run (default)
    python scripts/rename_to_titles.py --apply      # Actually rename
    python scripts/rename_to_titles.py --analyze    # Just show title length stats
"""

import argparse
import re
from pathlib import Path
from urllib.parse import quote, unquote

# Maximum filename length (without .md extension)
# Windows MAX_PATH is 260, but we want reasonable lengths
MAX_FILENAME_LENGTH = 150  # Captures 95%+ of titles


def sanitize_filename(title: str) -> str:
    """Convert a document title to a safe filename (without extension)."""
    # Replace characters not allowed in Windows filenames
    safe = title
    safe = safe.replace(':', '_')      # Colon -> underscore
    safe = safe.replace('?', '')       # Remove question marks
    safe = safe.replace('*', '')       # Remove asterisks
    safe = safe.replace('<', '')       # Remove angle brackets
    safe = safe.replace('>', '')
    safe = safe.replace('|', '')       # Remove pipes
    safe = safe.replace('"', '')       # Remove quotes
    safe = safe.replace('/', '-')      # Slash -> hyphen
    safe = safe.replace('\\', '-')     # Backslash -> hyphen
    
    # Collapse multiple spaces/hyphens
    safe = re.sub(r'\s+', ' ', safe)
    safe = re.sub(r'-+', '-', safe)
    safe = safe.strip(' -')
    
    # Truncate if needed
    if len(safe) > MAX_FILENAME_LENGTH:
        # Try to truncate at a word boundary
        truncated = safe[:MAX_FILENAME_LENGTH]
        last_space = truncated.rfind(' ')
        if last_space > MAX_FILENAME_LENGTH - 30:
            truncated = truncated[:last_space]
        safe = truncated.rstrip(' -')
    
    return safe


def extract_h1_title(text: str) -> str | None:
    """Extract the H1 title from markdown text."""
    # Match # Title or # **Title** at start of line
    match = re.search(r'^#\s+\*{0,2}(.+?)\*{0,2}\s*$', text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def find_references(data_root: Path, old_path: Path) -> list[tuple[Path, str, str]]:
    """Find all markdown references to a file."""
    references = []
    old_rel = old_path.relative_to(data_root)
    old_name = old_path.name
    old_stem = old_path.stem
    
    # URL-encoded version
    old_name_encoded = quote(old_name)
    
    for md_file in data_root.rglob('*.md'):
        if md_file == old_path:
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception:
            continue
        
        # Look for references: [text](path/to/file.md) or [text](path/to/file.md#anchor)
        # Also handles URL-encoded filenames
        patterns = [
            old_name,
            old_name_encoded,
            str(old_rel).replace('\\', '/'),
            quote(str(old_rel).replace('\\', '/')),
        ]
        
        for pattern in patterns:
            if pattern in content:
                references.append((md_file, old_name, content))
                break
    
    return references


def update_references(data_root: Path, old_path: Path, new_path: Path, apply: bool) -> int:
    """Update all references from old filename to new filename."""
    refs = find_references(data_root, old_path)
    updated = 0
    
    old_name = old_path.name
    new_name = new_path.name
    old_name_encoded = quote(old_name)
    new_name_encoded = quote(new_name)
    
    old_rel = str(old_path.relative_to(data_root)).replace('\\', '/')
    new_rel = str(new_path.relative_to(data_root)).replace('\\', '/')
    
    for ref_file, _, content in refs:
        new_content = content
        
        # Replace full relative paths first (more specific)
        new_content = new_content.replace(quote(old_rel), quote(new_rel))
        new_content = new_content.replace(old_rel, new_rel)
        
        # Then just filenames
        new_content = new_content.replace(old_name_encoded, new_name_encoded)
        new_content = new_content.replace(old_name, new_name)
        
        if new_content != content:
            updated += 1
            if apply:
                ref_file.write_text(new_content, encoding='utf-8')
    
    return updated


def analyze_lengths(data_root: Path):
    """Analyze title lengths to help pick truncation value."""
    lengths = []
    
    for md_file in sorted(data_root.rglob('*.md')):
        if 'reprocess_needed' in str(md_file):
            continue
        
        try:
            text = md_file.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        
        title = extract_h1_title(text)
        if not title:
            continue
        
        safe = sanitize_filename(title)
        lengths.append((len(safe), safe, md_file.name))
    
    lengths.sort(reverse=True)
    
    print(f"Total files with H1 titles: {len(lengths)}")
    print(f"\nLength distribution (sanitized, before truncation):")
    print(f"  > 200 chars: {sum(1 for l,_,_ in lengths if l > 200)}")
    print(f"  150-200:     {sum(1 for l,_,_ in lengths if 150 < l <= 200)}")
    print(f"  120-150:     {sum(1 for l,_,_ in lengths if 120 < l <= 150)}")
    print(f"  100-120:     {sum(1 for l,_,_ in lengths if 100 < l <= 120)}")
    print(f"  80-100:      {sum(1 for l,_,_ in lengths if 80 < l <= 100)}")
    print(f"  <= 80:       {sum(1 for l,_,_ in lengths if l <= 80)}")
    
    print(f"\nLongest titles (top 15):")
    for length, safe_title, orig_name in lengths[:15]:
        print(f"  {length:3d}: {safe_title[:90]}...")
    
    # Calculate optimal truncation
    for limit in [100, 120, 140, 150, 160, 180]:
        would_truncate = sum(1 for l,_,_ in lengths if l > limit)
        pct = (len(lengths) - would_truncate) / len(lengths) * 100
        print(f"\nAt {limit} char limit: {would_truncate} truncated, {pct:.1f}% complete")


def main():
    global MAX_FILENAME_LENGTH
    
    parser = argparse.ArgumentParser(description='Rename markdown files to match H1 titles')
    parser.add_argument('--apply', action='store_true', help='Actually rename files (default: dry-run)')
    parser.add_argument('--analyze', action='store_true', help='Just analyze title lengths')
    parser.add_argument('--max-length', type=int, default=MAX_FILENAME_LENGTH,
                        help=f'Maximum filename length (default: {MAX_FILENAME_LENGTH})')
    args = parser.parse_args()
    
    MAX_FILENAME_LENGTH = args.max_length
    
    data_root = Path(__file__).parent.parent / 'data'
    
    if args.analyze:
        analyze_lengths(data_root)
        return
    
    # Collect all renames needed
    renames = []
    
    for md_file in sorted(data_root.rglob('*.md')):
        if 'reprocess_needed' in str(md_file):
            continue
        
        try:
            text = md_file.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"ERROR reading {md_file}: {e}")
            continue
        
        title = extract_h1_title(text)
        if not title:
            continue
        
        safe_name = sanitize_filename(title) + '.md'
        
        # Skip if already matches
        if md_file.name == safe_name:
            continue
        
        new_path = md_file.parent / safe_name
        
        # Check for collision
        if new_path.exists() and new_path != md_file:
            print(f"COLLISION: {md_file.name} -> {safe_name} (target exists)")
            continue
        
        renames.append((md_file, new_path, title))
    
    if not renames:
        print("No renames needed - all files already match their titles!")
        return
    
    print(f"{'DRY RUN - ' if not args.apply else ''}Found {len(renames)} files to rename:\n")
    
    total_refs = 0
    for old_path, new_path, title in renames:
        old_rel = old_path.relative_to(data_root)
        new_rel = new_path.relative_to(data_root)
        
        # Count references
        refs = find_references(data_root, old_path)
        ref_count = len(refs)
        total_refs += ref_count
        
        truncated = " [TRUNCATED]" if len(sanitize_filename(title)) > MAX_FILENAME_LENGTH else ""
        
        print(f"  {old_rel}")
        print(f"    -> {new_rel.name}{truncated}")
        if ref_count > 0:
            print(f"       ({ref_count} reference(s) to update)")
        print()
    
    print(f"Summary: {len(renames)} files, {total_refs} references to update")
    
    if args.apply:
        print("\nApplying changes...")
        for old_path, new_path, title in renames:
            # Update references first
            updated = update_references(data_root, old_path, new_path, apply=True)
            
            # Then rename the file
            old_path.rename(new_path)
            
            print(f"  Renamed: {old_path.name}")
            if updated > 0:
                print(f"           Updated {updated} reference(s)")
        
        print(f"\nDone! Renamed {len(renames)} files.")
    else:
        print("\nRun with --apply to execute these renames.")


if __name__ == '__main__':
    main()
