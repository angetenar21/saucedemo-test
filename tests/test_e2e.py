import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Checkout functionality")
class TestE2E:

    @allure.title("End to End Checkout Flow")
    def test_e2e_checkout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step("Add an item to the cart"):
            inventory_page.add_item_to_cart("Sauce Labs Fleece Jacket")
            
        with allure.step("Go to cart and click checkout"):
            inventory_page.go_to_cart()
            cart_page.click_checkout()
            
        with allure.step("Enter checkout information"):
            checkout_page.enter_checkout_info("Manish", "Yadav", "12345")
            checkout_page.click_continue()
            
        with allure.step("Verify total and finish"):
            total = checkout_page.get_total()
            assert total != "", "Total is empty"
            checkout_page.click_finish()
            
        with allure.step("Verify checkout completion"):
            assert checkout_page.get_complete_header() == "Thank you for your order!", "Checkout did not complete successfully"
