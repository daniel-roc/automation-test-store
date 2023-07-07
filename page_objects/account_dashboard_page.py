from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AccountDashboardPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=account/account"
    __header_locator = (By.XPATH, "//h1//span[@class='maintext']")
    __logoff_button = (By.XPATH, "//ul[@id='customer_menu_top']/li/ul//a[@href='https://automationteststore.com/index.php?rt=account/logout']")
    __dropdown_account_menu = (By.CLASS_NAME, "menu_text")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def get_url(self) -> str:
        return self.__url
    
    def get_header_text(self) -> str:
        return super()._get_text(self.__header_locator)
    
    def click_logoff_button(self):
        super()._hover_over(self.__dropdown_account_menu)
        super()._click(self.__logoff_button)