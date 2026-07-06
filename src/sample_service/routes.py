from dataclasses import asdict

from sample_service.store import ItemStore

STORE = ItemStore()


def health() -> tuple[int, dict]:
    return 200, {"status": "ok"}


def list_items() -> tuple[int, dict]:
    return 200, {"items": [asdict(item) for item in STORE.list()]}


def create_item(payload: dict) -> tuple[int, dict]:
    item = STORE.add(payload["name"])
    return 201, asdict(item)
