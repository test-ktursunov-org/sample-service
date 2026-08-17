from sample_service import routes
from sample_service.store import ItemStore


def test_created_item_appears_in_the_listing():
    routes.STORE = ItemStore()

    status, created = routes.create_item({"name": "widget"})
    assert status == 201

    status, listing = routes.list_items()
    assert status == 200
    assert listing["items"] == [created]


def test_a_blank_name_is_rejected():
    routes.STORE = ItemStore()

    for name in ("", "   "):
        status, body = routes.create_item({"name": name})
        assert status == 400, f"should reject: {name!r}"
        assert body["error"]


def test_an_overlong_name_is_rejected():
    routes.STORE = ItemStore()

    status, body = routes.create_item({"name": "x" * (routes.MAX_NAME_LENGTH + 1)})

    assert status == 400
    assert body["error"]


def test_blank_tags_are_dropped():
    routes.STORE = ItemStore()

    _, created = routes.create_item({"name": "widget", "tags": ["a", " ", "b"]})

    assert created["tags"] == ["a", "b"]
