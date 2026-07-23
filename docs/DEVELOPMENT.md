# Development

Create an environment and install the package in editable mode:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -e . pytest
```

Run the suite:

```sh
pytest -q
```

Run the service against a non-default port:

```sh
SERVICE_PORT=9000 python -c "from sample_service.app import serve; serve()"
```
