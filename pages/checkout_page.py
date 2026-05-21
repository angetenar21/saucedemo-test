from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def enter_checkout_info(self, first_name, last_name, postal_code):
        if first_name:
            self.type_text(self.FIRST_NAME_INPUT, first_name)
        if last_name:
            self.type_text(self.LAST_NAME_INPUT, last_name)
        if postal_code:
            self.type_text(self.POSTAL_CODE_INPUT, postal_code)
            
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
        
    def get_total(self):
        return self.get_text(self.TOTAL_LABEL)
        
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
        
    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)
