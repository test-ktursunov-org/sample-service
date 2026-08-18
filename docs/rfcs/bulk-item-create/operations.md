# Rollout and operations

The change should ship behind configuration when behavior could affect existing
clients. Operators can compare request counts, latency, and error rates before
and after enabling it. Rollback consists of disabling the option and restarting
the service; no data migration is required.

## Signals

- Request throughput and status-code distribution
- p50 and p95 response latency
- Validation and internal error counts
- Process restarts and health-check failures
