import pytest

from sample_service import routes
from sample_service.store import ItemStore


@pytest.fixture()
def stocked_store():
    routes.STORE = ItemStore()
    for index in range(5):
        routes.STORE.add(f"item-{index}")
    return routes.STORE


@pytest.mark.parametrize(
    ("offset", "limit", "expected"),
    [
        (0, 2, ["item-0", "item-1"]),
        (2, 2, ["item-2", "item-3"]),
        (4, 2, ["item-4"]),
        (5, 2, []),
    ],
)
def test_a_window_returns_only_its_slice(stocked_store, offset, limit, expected):
    _, body = routes.list_items(offset=offset, limit=limit)

    names = [item["name"] for item in body["items"]]
    assert names == expected, f"should page: offset={offset} limit={limit}"
