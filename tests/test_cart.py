from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_single_product_to_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    expect(products_page.cart).to_have_text("1")

def test_add_multiple_products_to_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")
    products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")

    expect(products_page.cart).to_have_text("3")

def test_remove_product_from_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    expect(products_page.cart).to_have_text("2")

    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    expect(cart_page.get_product("Sauce Labs Backpack")).to_be_visible()

    cart_page.remove_product("Sauce Labs Backpack")

    expect(cart_page.get_product("Sauce Labs Backpack")).to_have_count(0)

def test_verify_cart_product_details(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    product = cart_page.get_product("Sauce Labs Backpack")

    expect(product).to_be_visible()

    expect(
        product.locator('[data-test="inventory-item-price"]')
    ).to_have_text("$29.99")

    expect(
        product.locator('[data-test="item-quantity"]')
    ).to_have_text("1")


def test_remove_all_products_from_cart(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")

    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    cart_page.remove_product("Sauce Labs Backpack")
    cart_page.remove_product("Sauce Labs Bike Light")

    expect(cart_page.cart_items).to_have_count(0)