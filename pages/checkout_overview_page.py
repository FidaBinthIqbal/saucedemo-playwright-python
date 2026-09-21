from playwright.sync_api import Page


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator('[data-test="title"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')

        self.payment_info = page.locator(
            '[data-test="payment-info-value"]'
        )
        self.shipping_info = page.locator(
            '[data-test="shipping-info-value"]'
        )

        self.subtotal = page.locator(
            '[data-test="subtotal-label"]'
        )
        self.tax = page.locator(
            '[data-test="tax-label"]'
        )
        self.total = page.locator(
            '[data-test="total-label"]'
        )

        self.cancel_button = page.locator(
            '[data-test="cancel"]'
        )
        self.finish_button = page.locator(
            '[data-test="finish"]'
        )

    def get_product(self, product_name: str):
        return self.cart_items.filter(
            has=self.page.get_by_role(
                "link",
                name=product_name,
                exact=True
            )
        )

    def finish_order(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()