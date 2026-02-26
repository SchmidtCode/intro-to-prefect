# Intro to Prefect

This project is meant as an introduction to data engineering through Prefect.
This `main` branch is the starting point. For the completed version, see
the `complete` branch.

## Requirements

- Python 3.12+
- `uv` (<https://docs.astral.sh/uv/>)
- Docker with Compose support

## Setup (uv sync + Python 3.12)

From the project root:

```bash
# Create virtual environment using Python 3.12
uv venv .venv --python 3.12

# Sync dependencies from uv.lock (includes dev extras)
uv sync --extra dev

# Install pre-commit hooks
uv run pre-commit install

# Start required services
docker compose up -d

# Configure Prefect to use local API
uv run prefect config set \
  PREFECT_API_URL="http://127.0.0.1:4200/api"

# Start Prefect server
uv run prefect server start
````

You do not need to activate the virtual environment.
`uv run` ensures commands execute inside `.venv`.

If you prefer activation:

```bash
source .venv/bin/activate
pip install -e '.[dev]'
pre-commit install
docker-compose up -d
prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
prefect server start
```

## Teardown

```shell
docker-compose down
```
