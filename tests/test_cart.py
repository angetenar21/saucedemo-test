import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Cart functionality")
class TestCart:

    @allure.title("Add item to cart and verify")
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        
        item_to_add = "Sauce Labs Backpack"
        
        with allure.step("Login as standard user"):
            login_page.load()
            login_page.login("standard_user", "secret_sauce")
            
        with allure.step(f"Add '{item_to_add}' to cart"):
            inventory_page.add_item_to_cart(item_to_add)
            
        with allure.step("Verify cart badge count is 1"):
            assert inventory_page.get_cart_badge_count() == 1, "Cart badge count is not 1"
            
        with allure.step("Go to cart and verify item is present"):
            inventory_page.go_to_cart()
            cart_items = cart_page.get_cart_items_names()
            assert item_to_add in cart_items, f"Item '{item_to_add}' not found in cart"
