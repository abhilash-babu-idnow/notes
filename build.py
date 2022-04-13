from pathlib import Path
import re

summary = Path.cwd() / "BookSummary" / "book summary.md"

lines = []
with open(summary) as f:
    for line in f.readlines():
        match = re.search(r'\[\[(.*)\]\]', line)
        if match:
            desc = match.groups()[0]
            html_name = desc.replace(' ', '_')
            html_name = html_name.lower()
            lines.append(f"- [{desc}](https://blog.abhilashbabuj.com/Notes/{html_name}.html)\n")
        else:
            lines.append(line)

with open(Path.cwd() / "BookSummary" / "index.md", "w") as f:
    for line in lines:
        f.write(line)
