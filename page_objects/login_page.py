from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    
    __url = "https://automationteststore.com/index.php?rt=account/login"
    __username_input_field = (By.ID, "loginFrm_loginname")
    __password_input_field = (By.ID, "loginFrm_password")
    __login_button = (By.XPATH, "//button[@title='Login']")
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def type_user_credentials(self, username: str, password: str):
        super()._type(self.__username_input_field, username)
        super()._type(self.__password_input_field, password)
    
    def click_login_button(self):
        super()._click(self.__login_button)