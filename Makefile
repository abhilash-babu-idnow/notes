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
	pandoc $(flags) -o public/pytest.html "BookSummary/Pytest.md" -c $(style)
	pandoc $(flags) -o public/hands_on_ml.html "BookSummary/Hands on Machine Learning.md" -c $(style)
	pandoc $(flags) -o public/bash_idioms.html "BookSummary/Bash Idioms.md" -c $(style)
	pandoc $(flags) -o public/ds_cmd_line.html "BookSummary/Data Science at Command Line.md" -c $(style)
	pandoc $(slide_flags) -o public/practices_of_agile_developer.html "BookSummary/Practices of Agile Developers.md" --slide-level 2
	pandoc $(slide_flags) -o public/domain_storytelling.html "BookSummary/Domain Storytelling.md" --slide-level 2
	pandoc $(slide_flags) -o public/pandas_puzzles.html "BookSummary/Pandas Brain Teasers.md" --slide-level 2
	pandoc $(slide_flags) -o public/python_puzzles.html "BookSummary/Python Brain Teasers.md" --slide-level 2
	pandoc $(slide_flags) -o public/effective_python.html "BookSummary/Effective Python.md" --slide-level 2
