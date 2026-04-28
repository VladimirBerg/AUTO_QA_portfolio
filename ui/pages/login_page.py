from playwright.sync_api import Page
from ui.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_flash_message(self) -> str:
        return self.flash_message.inner_text()

    def is_logged_in(self) -> bool:
        return "You logged into a secure area!" in self.get_flash_message()

    def is_logged_out(self) -> bool:
        return "You logged out of the secure area!" in self.get_flash_message()
