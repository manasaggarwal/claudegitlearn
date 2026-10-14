# Todo Demo

A tiny command-line to-do app for practicing Git and GitHub.

## Run it

Requires Python 3 (no extra packages).

```bash
python3 -m todo add "Learn Git"
python3 -m todo add "Open my first PR"
python3 -m todo list
python3 -m todo done 1
python3 -m todo remove 2
```

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

## Project layout

```
todo/core.py     task logic
todo/cli.py      command line interface
tests/           unit tests
.github/         PR template + automatic test workflow
EXERCISES.md     your Git practice tasks
```Created by YOUR NAME while learning GitHub.