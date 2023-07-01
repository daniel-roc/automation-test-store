from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AccountDashboardPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=account/account"
    __header_locator = (By.XPATH, "//h1//span[@class='maintext']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def get_url(self) -> str:
        return self.__url
    
    def get_header_text(self) -> str:
        return super()._get_text(self.__header_locator)
