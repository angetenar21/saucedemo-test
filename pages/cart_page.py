from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    
    def is_checkout_button_visible(self):
        return self.is_visible(self.CHECKOUT_BUTTON)
        
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        
    def get_cart_items_names(self):
        elements = self.find_elements(self.INVENTORY_ITEM_NAME)
        return [element.text for element in elements]
