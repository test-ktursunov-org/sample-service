import threading
from dataclasses import dataclass
from itertools import count


@dataclass(frozen=True)
class Item:
    id: int
    name: str
    tags: tuple[str, ...] = ()


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(1)
        self._lock = threading.Lock()

    def add(self, name: str, tags: tuple[str, ...] = ()) -> Item:
        with self._lock:
            item = Item(id=next(self._ids), name=name, tags=tags)
            self._items[item.id] = item
        return item

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None

    def list(self, offset: int = 0, limit: int | None = None) -> list[Item]:
        items = list(self._items.values())
        if limit is None:
            return items[offset:]
        return items[offset : offset + limit]
