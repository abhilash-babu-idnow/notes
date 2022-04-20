#!/bin/python3

from pathlib import Path
import re
from shutil import copyfile
import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO)

summary = Path.cwd() / "BookSummary" / "Summary.md"
logging.info(summary)

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

subprocess.run(f"pandoc -s -f -o public/index.html public/index.md", shell=True)
for md_file in book_summary_path.rglob("*.md"):
    if md_file.stem.lower() == 'summary':
        continue
    old_fname = md_file.name
    new_fname = old_fname.replace(" ", "_")
    new_fname = new_fname.lower()
    dest_path = Path.cwd() / "public" / new_fname
    logging.info(f"Copying {md_file} to {dest_path}")
    copyfile(str(md_file), str(dest_path))
    if not dest_path.exists():
        logging.error(f"File {dest_path} doesn't exist")
    else:
        logging.info(f"{dest_path} exists.")
        command = f"pandoc -s -f markdown -o {dest_path.with_suffix('.html')} {dest_path}"
        logging.info(command)
        subprocess.run(command, shell=True)
