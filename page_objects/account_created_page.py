from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class AccountCreatedPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=account/success"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url