from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    
    __url = "https://automationteststore.com/"
    __home_button = (By.CLASS_NAME, "menu_home")
    __specials_page_button = (By.CLASS_NAME, "menu_specials")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def open_url(self):
        return super().open_url(self.__url)
    
    def hover_menu_button(self):
        self._driver.maximize_window()
        super()._hover_over(self.__home_button)
    
    def click_specials_button(self):
        super()._click(self.__specials_page_button)
    
    
