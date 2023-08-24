from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SpecialsPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=product/special"
    __title = (By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_url(self) -> str:
        return self.__url

    def click_on_product(self, product= str):
        super()._click((By.XPATH, "//a[@title='%s']" % (product,)))

    def get_title(self) -> str:
        return super()._get_text(self.__title)