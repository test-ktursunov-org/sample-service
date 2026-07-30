# Architecture

The service is three layers with no cycles between them:

- `app.py` — the HTTP shell: it parses the request and writes the response.
- `routes.py` — the request handlers: they translate payloads into store calls
  and pick the status code.
- `store.py` — the state: an in-memory map of items behind a lock.

Anything computable without a socket lives in `routes.py` or below, which is
what the tests exercise directly.
