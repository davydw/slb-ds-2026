default: pylint pytest mypy

format:
	autopep8 --in-place school/*.py

pytest:
	pytest

pylint:
	pylint --output-format colorized school; true

mypy:
	python -m mypy school; true
