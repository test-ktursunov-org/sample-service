# fix: standardize API error envelopes

## Summary

This proposal will return a stable machine-readable shape for every API failure. It is intentionally scoped so the service can
ship the change independently and preserve the existing item API behavior.

## Goals

- Define observable behavior before implementation.
- Keep compatibility with existing clients.
- Make failure modes explicit and testable.

## Non-goals

This change does not introduce authentication, persistence, or a new framework.
