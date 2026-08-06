import json

from sample_service import routes
from sample_service.store import ItemStore


def test_an_unknown_field_is_ignored():
    routes.STORE = ItemStore()

    status, created = routes.create_item({"name": "widget", "colour": "red"})

    assert status == 201
    assert json.dumps(created)
    assert "colour" not in created
