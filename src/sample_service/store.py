from dataclasses import dataclass
from itertools import count


@dataclass(frozen=True)
class Item:
    id: int
    name: str


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(1)

    def add(self, name: str) -> Item:
        item = Item(id=next(self._ids), name=name)
        self._items[item.id] = item
        return item

    def list(self) -> list[Item]:
        return list(self._items.values())
