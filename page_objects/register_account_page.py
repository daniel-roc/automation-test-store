import time
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class RegisterAccountPage(BasePage):

    __url = "https://automationteststore.com/index.php?rt=account/create"
    __first_name_input_field = (By.ID, "AccountFrm_firstname")
    __last_name_input_field = (By.ID, "AccountFrm_lastname")
    __email_input_field = (By.ID, "AccountFrm_email")
    __telephone_input_field = (By.ID, "AccountFrm_telephone")
    __fax_input_field = (By.ID, "AccountFrm_fax")
    __company_input_field = (By.ID, "AccountFrm_company")
    __addres1_input_field = (By.ID, "AccountFrm_address_1")
    __addres2_input_field = (By.ID, "AccountFrm_address_2")
    __city_input_field = (By.ID, "AccountFrm_city")
    __region_state_dropdown_list = (By.ID, "AccountFrm_zone_id")
    __zip_code_input_field = (By.ID, "AccountFrm_postcode")
    __country_dropdown_list = (By.ID, "AccountFrm_country_id")
    __username_input_field = (By.ID, "AccountFrm_loginname")
    __password_input_field = (By.ID, "AccountFrm_password")
    __password_confirm_input_field = (By.ID, "AccountFrm_confirm")
    __subscribe_yes_radio_button = (By.ID, "AccountFrm_newsletter1")
    __subscribe_no_radio_button = (By.ID, "AccountFrm_newsletter0")
    __privacy_police_checkbox = (By.ID, "AccountFrm_agree")
    __continue_button = (By.XPATH, "//button[@title='Continue']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def type_form(self, first_name: str, last_name: str, email: str, telephone: str, fax: str, company: str, addres1: str, addres2: str, city: str, region_state: str, zip_code: str, country: str, username: str, password: str, password_confirm: str, subscribe: str, privacy_policy: str):
        super()._type(self.__first_name_input_field, first_name)
        super()._type(self.__last_name_input_field, last_name)
        super()._type(self.__email_input_field, email)
        super()._type(self.__telephone_input_field, telephone)
        super()._type(self.__fax_input_field, fax)
        super()._type(self.__company_input_field, company)
        super()._type(self.__addres1_input_field, addres1)
        super()._type(self.__addres2_input_field, addres2)
        super()._type(self.__city_input_field, city)
        super()._select_dropdown(self.__country_dropdown_list, country)
        time.sleep(2)
        super()._select_dropdown(self.__region_state_dropdown_list, region_state)
        super()._type(self.__zip_code_input_field, zip_code)
        super()._type(self.__username_input_field, username)
        super()._type(self.__password_input_field, password)
        super()._type(self.__password_confirm_input_field, password_confirm)
        if subscribe == 'Yes' or subscribe == 'yes':
            super()._click(self.__subscribe_yes_radio_button)
        elif subscribe == 'No' or subscribe == 'no':
            super()._click(self.__subscribe_no_radio_button)
        if privacy_policy == 'Yes' or privacy_policy == 'yes':
            super()._click(self.__privacy_police_checkbox)
        super()._click(self.__continue_button)
        
        
                









            

    
    