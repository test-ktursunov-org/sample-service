from sample_service import routes
from sample_service.store import ItemStore


def test_created_item_appears_in_the_listing():
    routes.STORE = ItemStore()

    status, created = routes.create_item({"name": "widget"})
    assert status == 201

    status, listing = routes.list_items()
    assert status == 200
    assert listing["items"] == [created]
