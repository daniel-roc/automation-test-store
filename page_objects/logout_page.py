from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LogoutPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=account/logout"
    __login_or_register_button = (By.ID, "customer_menu_top")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def get_url(self) -> str:
        return self.__url
    
    def get_login_or_register_button_text(self) -> str:
        return super()._get_text(self.__login_or_register_button)