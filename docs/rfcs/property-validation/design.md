# Design

The change belongs at the HTTP boundary, with domain logic kept independent of
transport details. Configuration is parsed once at startup and passed through
explicit dependencies. The store remains responsible only for item state.

## Components

1. Routes validate incoming values and translate failures.
2. Service helpers implement the property validation behavior.
3. Logging records outcomes without including request bodies.
4. Tests exercise both the contract and internal edge cases.

This split keeps future persistence work separate from the API contract.
