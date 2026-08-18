# Contract

The public contract for **docker healthcheck** follows the service's JSON conventions.
Clients receive deterministic status codes, content types, and response fields.
Existing requests remain valid without opting into the new behavior.

## Compatibility

- Unknown fields remain ignored where they are ignored today.
- Error responses never expose internal exception details.
- Empty collections are represented as arrays, not null values.

## Example

A client sends a normal request and may opt into the new behavior using the
documented field or header. The server returns the result with stable metadata.
