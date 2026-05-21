import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Login functionality")
class TestLogin:

    @allure.title("Successful login with standard user")
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        with allure.step("Open login page"):
            login_page.load()
            
        with allure.step("Enter valid credentials"):
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Verify inventory page is displayed"):
            assert inventory_page.get_title() == "Products", "Inventory page title did not match"

    @allure.title("Failed login with locked out user")
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        
        with allure.step("Open login page"):
            login_page.load()
            
        with allure.step("Enter locked out credentials"):
            login_page.login("locked_out_user", "secret_sauce")
            
        with allure.step("Verify error message is displayed"):
            error_message = login_page.get_error_message()
            assert "locked out" in error_message, f"Expected locked out message, got: {error_message}"
