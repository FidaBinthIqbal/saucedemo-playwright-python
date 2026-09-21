import pytest

from config import BASE_URL, STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)

    login_page.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    return page