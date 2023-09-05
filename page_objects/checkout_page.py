from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=checkout/confirm"
    __confirm_order_button = (By.ID, "checkout_btn")
    __title = (By.CLASS_NAME, "maintext")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_url(self) -> str:
        return self.__url
    
    def is_item_in_the_cart(self, item_name: str) -> bool:
        item = (By.XPATH, "//a[@class='checkout_heading'][text()='%s']" % item_name)
        return super()._is_displayed(item)
    
    def confirm_order(self):
        super()._click(self.__confirm_order_button)

    def has_order_been_processed(self) -> bool:
        actual_title = super()._get_text(self.__title)
        expected_title = "CHECKOUT CONFIRMATION"
        if actual_title == expected_title:
            return True
        else:
            return False
