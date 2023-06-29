from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    
    __url = "https://automationteststore.com/index.php?rt=account/login"
    __username_input_field = (By.ID, "loginFrm_loginname")
    __password_input_field = (By.ID, "loginFrm_password")
    __login_button = (By.XPATH, "//button[@title='Login']")
    __error_message = (By.XPATH, "//div[@id='maincontainer']//div[@class='col-md-12 col-xs-12 mt20']/div/div[1]")
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def type_user_credentials(self, username: str, password: str):
        super()._type(self.__username_input_field, username)
        super()._type(self.__password_input_field, password)
    
    def click_login_button(self):
        super()._click(self.__login_button)
    
    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message)