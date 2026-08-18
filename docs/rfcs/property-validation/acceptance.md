# Acceptance scenarios

## Happy path

- A valid request produces the documented success response.
- Repeating a read-only request produces an equivalent result.
- Logs include the operation name and final status.

## Boundaries

- Missing optional values use documented defaults.
- Malformed input produces a 4xx response with a stable error code.
- Unexpected internal failures produce a generic 5xx response.
- Existing item endpoints continue to pass their regression suite.
