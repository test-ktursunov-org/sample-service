# sample-service

A small HTTP service used as a synthetic fixture. It keeps a set of items in
memory and exposes them over a JSON API.

## Endpoints

| Method | Path      | Purpose                  |
| ------ | --------- | ------------------------ |
| GET    | `/health` | Liveness probe           |
| GET    | `/items`  | List the stored items    |
| POST   | `/items`  | Create an item by name   |
| GET    | `/ready`  | Readiness plus item count |
| GET    | `/items/{id}` | Read a single item   |
| DELETE | `/items/{id}` | Delete a single item |

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) to run it locally and
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the layering.
