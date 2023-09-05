from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    __title = (By.TAG_NAME, "h1")
    __add_to_cart_button = (By.CLASS_NAME, "productpagecart")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_title(self) -> str:
        return super()._get_text(self.__title)
    
    def add_to_cart(self):
        super()._click(self.__add_to_cart_button)
    
    
    