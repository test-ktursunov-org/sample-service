from dataclasses import asdict

from sample_service.store import ItemStore

STORE = ItemStore()


def health() -> tuple[int, dict]:
    return 200, {"status": "ok"}


DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100


def list_items(offset: int = 0, limit: int = DEFAULT_PAGE_SIZE) -> tuple[int, dict]:
    items = STORE.list(offset=offset, limit=limit)
    return 200, {"items": [asdict(item) for item in items], "offset": offset}


def create_item(payload: dict) -> tuple[int, dict]:
    name = str(payload.get("name", "")).strip()
    if not name:
        return 400, {"error": "name must not be blank"}

    item = STORE.add(name)
    return 201, asdict(item)
