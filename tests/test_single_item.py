from sample_service import routes
from sample_service.store import ItemStore


def test_a_missing_item_is_reported_as_not_found():
    routes.STORE = ItemStore()

    assert routes.get_item(404)[0] == 404
    assert routes.delete_item(404)[0] == 404


def test_a_deleted_item_can_no_longer_be_read():
    routes.STORE = ItemStore()
    _, created = routes.create_item({"name": "widget"})

    assert routes.delete_item(created["id"])[0] == 204
    assert routes.get_item(created["id"])[0] == 404
