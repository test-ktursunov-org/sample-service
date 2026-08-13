from dataclasses import asdict

from sample_service.store import ItemStore

STORE = ItemStore()


def health() -> tuple[int, dict]:
    return 200, {"status": "ok"}


def ready() -> tuple[int, dict]:
    return 200, {"status": "ready", "items": len(STORE.list(limit=None))}


DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
MAX_NAME_LENGTH = 200


def list_items(offset: int = 0, limit: int = DEFAULT_PAGE_SIZE) -> tuple[int, dict]:
    offset = max(offset, 0)
    limit = min(max(limit, 1), MAX_PAGE_SIZE)

    items = STORE.list(offset=offset, limit=limit)
    return 200, {"items": [asdict(item) for item in items], "offset": offset}


def create_item(payload: dict) -> tuple[int, dict]:
    name = str(payload.get("name", "")).strip()
    if not name:
        return 400, {"error": "name must not be blank"}
    if len(name) > MAX_NAME_LENGTH:
        return 400, {"error": f"name must be at most {MAX_NAME_LENGTH} characters"}

    item = STORE.add(name)
    return 201, asdict(item)


def get_item(item_id: int) -> tuple[int, dict]:
    item = STORE.get(item_id)
    if item is None:
        return 404, {"error": "item not found"}
    return 200, asdict(item)


def delete_item(item_id: int) -> tuple[int, dict]:
    if not STORE.delete(item_id):
        return 404, {"error": "item not found"}
    return 204, {}
