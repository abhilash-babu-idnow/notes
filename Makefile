SHELL := bash

.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: all

all: index out

index:
	python3 build.py

style = sakura-dark-solarized.css
flags = -s -f markdown
slide_flags = -s -V revealjs-url=revealjs/reveal.js-master/dist -t revealjs -f markdown

out: index
	pandoc $(flags) -o public/index.html "BookSummary/index.md" -c $(style)
	pandoc $(flags) -o public/pytest.html "BookSummary/pytest_notes.md" -c $(style)
	pandoc $(flags) -o public/hands_on_ml.html "BookSummary/hands_on_ml.md" -c $(style)
	pandoc $(flags) -o public/bash_idioms.html "BookSummary/Bash_Idioms.md" -c $(style)
	pandoc $(flags) -o public/ds_cmd_line.html "BookSummary/Data_science_at_command_line.md" -c $(style)
	pandoc $(slide_flags) -o public/practices_of_agile_developer.html BookSummary/practices_of_agile_developer.md --slide-level 2
	pandoc $(slide_flags) -o public/domain_storytelling.html BookSummary/domain_storytelling.md --slide-level 2
	pandoc $(slide_flags) -o public/pandas_puzzles.html BookSummary/Pandas_Brain_Teasers.md --slide-level 2
	pandoc $(slide_flags) -o public/python_puzzles.html BookSummary/Python_Brain_Teasers.md --slide-level 2
	pandoc $(slide_flags) -o public/effective_python.html BookSummary/Effective_python.md --slide-level 2
