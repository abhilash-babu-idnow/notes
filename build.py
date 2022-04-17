from pathlib import Path
import re
from shutil import copyfile
import os

summary = Path.cwd() / "BookSummary" / "Summary.md"

lines = []
with open(summary) as f:
    for line in f.readlines():
        match = re.search(r'\[\[(.*)\]\]', line)
        if match:
            desc = match.groups()[0]
            html_name = desc.replace(' ', '_')
            html_name = html_name.lower()
            lines.append(f"- [{desc}](https://blog.abhilashbabuj.com/notes/{html_name}.html)\n")
        else:
            lines.append(line)

with open(Path.cwd() / "public" / "index.md", "w") as f:
    for line in lines:
        f.write(line)

book_summary_path = Path.cwd() / "BookSummary"

for md_file in book_summary_path.rglob("*.md"):
    old_fname = md_file.name
    new_fname = old_fname.replace(" ", "_")
    new_fname = new_fname.lower()
    dest_path = Path.cwd() / "public" / new_fname
    copyfile(str(md_file), str(dest_path))
    os.system(f"pandoc -o {dest_path.with_suffix('.html')} {dest_path} -c style1.css")
