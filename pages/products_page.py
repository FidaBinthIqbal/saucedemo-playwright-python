from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator('[data-test="title"]')
        self.products = page.locator('[data-test="inventory-item"]')
        self.cart = page.locator('[data-test="shopping-cart-link"]')

        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator(
            '[data-test="logout-sidebar-link"]'
        )

    def add_product_to_cart(self, product_name: str):
        product = self.products.filter(
            has=self.page.get_by_text(product_name, exact=True)
        )

        product.get_by_role("button",name="Add to cart").click()

    def open_cart(self):
        self.cart.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()