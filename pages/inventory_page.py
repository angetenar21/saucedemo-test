from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    
    def get_title(self):
        return self.get_text(self.TITLE)
        
    def add_item_to_cart(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{formatted_name}")
        self.click(locator)

    def remove_item_from_cart(self, item_name):
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"remove-{formatted_name}")
        self.click(locator)
        
    def get_cart_badge_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_ICON)
