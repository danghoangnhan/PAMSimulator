.PHONY: install run lint test build

install:
	uv sync --group test

run:
	uv run python main.py

lint:
	uv run flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

test:
	uv run --group test pytest -q

build:
	uv sync --group build && uv run pyinstaller main.spec
