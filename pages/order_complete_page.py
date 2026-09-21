from playwright.sync_api import Page


class OrderCompletePage:

    def __init__(self, page: Page):
        self.page = page

        self.complete_container = page.locator(
            '[data-test="checkout-complete-container"]'
        )
        self.complete_header = page.locator(
            '[data-test="complete-header"]'
        )
        self.complete_text = page.locator(
            '[data-test="complete-text"]'
        )

        self.back_home_button = page.locator(
            '[data-test="back-to-products"]'
        )
        self.generate_pdf_button = page.locator(
            '[data-test="generate-pdf-order"]'
        )

    def back_home(self):
        self.back_home_button.click()