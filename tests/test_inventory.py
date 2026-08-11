import pytest

from data.products import Products


@pytest.mark.smoke 
@pytest.mark.parametrize(
    "product",
    [
        Products.BACKPACK,
        Products.BIKE_LIGHT,
    ],
    ids=[
        "Backpack",
        "Bike Light",
    ]
)
def test_add_product_to_cart(authorized_inventory_page, product):
    authorized_inventory_page.add_to_cart(product)

    assert authorized_inventory_page.get_cart_items_count() == "1"

@pytest.mark.regression
def test_remove_backpack_from_cart(authorized_inventory_page):
    authorized_inventory_page.add_to_cart(Products.BACKPACK)

    assert authorized_inventory_page.get_cart_items_count() == "1"

    authorized_inventory_page.remove_from_cart(Products.BACKPACK)

    assert not authorized_inventory_page.has_cart_badge()

@pytest.mark.regression
def test_cart_badge_is_hidden_when_cart_is_empty(
        authorized_inventory_page
):
    assert not authorized_inventory_page.has_cart_badge()
