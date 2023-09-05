from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ShoppingCartPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=checkout/cart"
    __checkout_button = (By.ID, "cart_checkout1")
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def get_url(self) -> str:
        return self.__url
    
    def checkout_order(self):
        super()._click(self.__checkout_button)
    
    