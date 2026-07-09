# sample-service

A small HTTP service used as a synthetic fixture. It keeps a set of items in
memory and exposes them over a JSON API.

## Endpoints

| Method | Path      | Purpose                  |
| ------ | --------- | ------------------------ |
| GET    | `/health` | Liveness probe           |
| GET    | `/items`  | List the stored items    |
| POST   | `/items`  | Create an item by name   |
