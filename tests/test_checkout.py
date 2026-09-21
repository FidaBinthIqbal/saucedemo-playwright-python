from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.order_complete_page import OrderCompletePage


def test_complete_checkout_with_valid_information(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.fill_customer_information(
        "Fida",
        "Tester",
        "689121"
    )

    checkout_page.continue_to_overview()

    checkout_overview_page = CheckoutOverviewPage(logged_in_page)

    expect(checkout_overview_page.title).to_have_text(
        "Checkout: Overview"
    )

    checkout_overview_page.finish_order()

    order_complete_page = OrderCompletePage(logged_in_page)

    expect(order_complete_page.complete_header).to_have_text(
        "Thank you for your order!"
    )

def test_checkout_with_missing_required_information(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    # Leave all fields empty
    checkout_page.continue_to_overview()

    expect(checkout_page.error_message).to_be_visible()
    expect(checkout_page.error_message).to_contain_text(
        "First Name is required"
    )

def test_checkout_with_blank_spaces(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.fill_customer_information(
        " ",
        " ",
        " "
    )

    checkout_page.continue_to_overview()

    expect(checkout_page.error_message).to_be_visible()

def test_cancel_checkout(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.cancel()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )