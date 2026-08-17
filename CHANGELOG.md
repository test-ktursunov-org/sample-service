# Changelog

## Unreleased

- Items carry tags; blank entries are dropped at creation and the field is
  serialised as a JSON array on every read path.

## 0.1.0

- Readiness endpoint reporting the store size.
- Structured request logging.
- Pagination on the listing endpoint, clamped to a maximum page size.
- Single-item read and delete.
