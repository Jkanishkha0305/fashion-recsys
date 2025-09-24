install-python:
	uv python install

install:
	uv venv
	. .venv/bin/activate
	uv pip install --all-extras --requirement pyproject.toml