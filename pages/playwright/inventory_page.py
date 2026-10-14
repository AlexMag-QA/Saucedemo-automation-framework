from playwright.sync_api import Page, Locator


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.title: Locator = page.locator(".title")