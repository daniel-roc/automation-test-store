from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class ForgotPasswordPage(BasePage):
    
    __url = "https://automationteststore.com/index.php?rt=account/forgotten/password"
    __username_input_field = (By.ID, "forgottenFrm_loginname")
    __email_input_field = (By.ID, "forgottenFrm_email")
    __continue_button = (By.XPATH, "//button[@title='Continue']")
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_url(self) -> str:
        return self.__url
    
    def type_user_credentials(self, username: str, email: str):
        super()._type(self.__username_input_field, username)
        super()._type(self.__email_input_field, email)
    
    def click_continue_button(self):
        super()._click(self.__continue_button)