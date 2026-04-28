import pytest
import allure
from ui.pages.login_page import LoginPage

@allure.feature("UI Login")
class TestLoginPlaywright:

    @allure.title("Successful login with valid credentials")
    @pytest.mark.ui
    def test_successful_login(self, page, config):
        login_page = LoginPage(page)
        login_page.navigate(f"{config['base_url']}/login")
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert login_page.is_logged_in()

    @allure.title("Failed login with invalid password")
    @pytest.mark.ui
    def test_failed_login(self, page, config):
        login_page = LoginPage(page)
        login_page.navigate(f"{config['base_url']}/login")
        login_page.login("tomsmith", "wrongpassword")
        assert "Your password is invalid!" in login_page.get_flash_message()

    @allure.title("Logout after login")
    @pytest.mark.ui
    def test_logout(self, page, config):
        login_page = LoginPage(page)
        login_page.navigate(f"{config['base_url']}/login")
        login_page.login("tomsmith", "SuperSecretPassword!")
        page.locator("a[href='/logout']").click()
        assert login_page.is_logged_out()
