# chore: add a container health check

## Summary

This proposal will let container runtimes detect unhealthy service instances. It is intentionally scoped so the service can
ship the change independently and preserve the existing item API behavior.

## Goals

- Define observable behavior before implementation.
- Keep compatibility with existing clients.
- Make failure modes explicit and testable.

## Non-goals

This change does not introduce authentication, persistence, or a new framework.
