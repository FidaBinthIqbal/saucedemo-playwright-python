from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD, LOCKED_USERNAME, INVALID_PASSWORD


def test_valid_login(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    expect(products_page.title).to_have_text("Products")

def test_login_with_invalid_password(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login(STANDARD_USERNAME, INVALID_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )

def test_login_with_locked_out_user(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login(LOCKED_USERNAME, STANDARD_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out."
    )

def test_logout_successfully(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)

    expect(products_page.title).to_have_text("Products")

    products_page.logout()

    expect(login_page.username).to_be_visible()
    expect(login_page.password).to_be_visible()
    expect(login_page.login_button).to_be_visible()

def test_login_with_empty_credentials(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login("", "")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

def test_login_with_empty_password(page: Page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login(STANDARD_USERNAME, "")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            STANDARD_USERNAME,
            INVALID_PASSWORD,
            "Username and password do not match",
        ),
        (
            LOCKED_USERNAME,
            STANDARD_PASSWORD,
            "Sorry, this user has been locked out.",
        ),
        (
            "",
            "",
            "Username is required",
        ),
        (
            STANDARD_USERNAME,
            "",
            "Password is required",
        ),
    ],
)
def test_login_validation(
    page: Page,
    username,
    password,
    expected_error,
):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        expected_error
    )