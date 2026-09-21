from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator('[data-test="title"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')

        self.continue_shopping = page.locator(
            '[data-test="continue-shopping"]'
        )
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

    def get_product(self, product_name: str):
        return self.cart_items.filter(
            has=self.page.get_by_text(product_name, exact=True)
        )

    def remove_product(self, product_name: str):
        product = self.get_product(product_name)
        product.get_by_role("button", name="Remove").click()

    def continue_shopping_to_products(self):
        self.continue_shopping.click()

    def checkout(self):
        self.checkout_button.click()