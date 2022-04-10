from pathlib import Path
import re

summary = Path.cwd() / "BookSummary" / "book summary.md"

lines = []
with open(summary) as f:
    for line in f.readlines():
        line = re.sub(r'\[\[.*\]\]', '', line)
        lines.append(line)

with open(Path.cwd() / "BookSummary" / "index.md", "w") as f:
    for line in lines:
        f.write(line)
