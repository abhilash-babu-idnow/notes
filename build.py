#!/bin/python3

from pathlib import Path
import re
from shutil import copyfile
import subprocess
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

summary = Path.cwd() / "BookSummary" / "Summary.md"
logger.info(summary)

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
    if md_file.stem.lower() == 'summary':
        continue
    old_fname = md_file.name
    new_fname = old_fname.replace(" ", "_")
    new_fname = new_fname.lower()
    dest_path = Path.cwd() / "public" / new_fname
    logger.info(f"Copying {md_file} to {dest_path}")
    copyfile(str(md_file), str(dest_path))
    if not dest_path.exists():
        logger.error(f"File {dest_path} doesn't exist")
    command = f"pandoc -s -f markdown -o {dest_path.with_suffix('.html')} {dest_path} -c sakura-dark-solarized.css"
    logger.info(command)
    subprocess.run(command, capture_output=True)
subprocess.run(f"pandoc -s -f -o public/index.html public/index.md -c sakura-dark-solarized.css", shell=True)
