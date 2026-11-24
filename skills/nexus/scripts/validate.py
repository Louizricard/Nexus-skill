#!/usr/bin/env python3
"""Offline structural checks for the Nexus package (Python 3, stdlib only)."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

entry = root / 'SKILL.md'
if not entry.is_file():
    sys.exit('FAIL: SKILL.md missing')
content = entry.read_text(encoding='utf-8')
front = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
check(front is not None, 'Missing YAML frontmatter')
if front:
    header = front.group(1)
    name = re.search(r'^name: ([a-z0-9-]+)$', header, re.M)
    check(bool(name and name[1] == root.name and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name[1]) and len(name[1]) <= 64), 'Invalid skill name')
    desc = re.search(r'^description: >-\n((?:  [^\n]+\n?)+)', header, re.M)
    check(bool(desc and 0 < len(' '.join(desc[1].split())) <= 1024), 'Invalid description')
check(len(content.splitlines()) < 500, 'SKILL.md should remain under 500 lines')
links = re.findall(r'\]\((references/[^)]+)\)', content)
check(len(set(links)) == 8, 'Expected 8 unique reference links')
for link in links:
    check((root / link).is_file(), f'Missing reference: {link}')
chapters = []
for path in sorted((root / 'references').glob('0[1-7]-*.md')):
    chapters.extend(int(n) for n in re.findall(r'^## (\d+)\. ', path.read_text(encoding='utf-8'), re.M))
check(chapters == list(range(17)), f'Expected source chapters 0–16 exactly once, got {chapters}')
if errors:
    print('\n'.join('FAIL: ' + e for e in errors))
    sys.exit(1)
print('PASS: Nexus entrypoint, metadata, reference links and all 17 original chapters.')
print('Scope: package structure only; no agent or website runtime tests performed.')
