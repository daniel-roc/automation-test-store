import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from faker import Faker
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
    __faker = Faker()

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def type_all_fields(self):
        password = self.__faker.password()
        super()._type(self.__first_name_input_field, self.__faker.first_name())
        super()._type(self.__last_name_input_field, self.__faker.last_name())
        super()._type(self.__email_input_field, self.__faker.email())
        super()._type(self.__telephone_input_field, self.__faker.phone_number())
        super()._type(self.__fax_input_field, self.__faker.phone_number())
        super()._type(self.__company_input_field, self.__faker.company())
        super()._type(self.__addres1_input_field, self.__faker.building_number())
        super()._type(self.__addres2_input_field, self.__faker.street_name())
        super()._type(self.__city_input_field, self.__faker.city())
        super()._select_dropdown_by_name(self.__country_dropdown_list, self.__faker.country())
        time.sleep(2)
        super()._select_dropdown_by_index(self.__region_state_dropdown_list, 1)
        super()._type(self.__zip_code_input_field, self.__faker.postcode())
        super()._type(self.__username_input_field, self.__faker.user_name())
        super()._type(self.__password_input_field, password)
        super()._type(self.__password_confirm_input_field, password)
        super()._click(self.__subscribe_yes_radio_button)
        super()._click(self.__privacy_police_checkbox)
        super()._click(self.__continue_button)
    

    def type_required_fields(self):
        password = self.__faker.password()
        super()._type(self.__first_name_input_field, self.__faker.first_name())
        super()._type(self.__last_name_input_field, self.__faker.last_name())
        super()._type(self.__email_input_field, self.__faker.email())
        super()._type(self.__addres1_input_field, self.__faker.street_address())
        super()._type(self.__city_input_field, self.__faker.city())
        super()._select_dropdown_by_name(self.__country_dropdown_list, self.__faker.country())
        time.sleep(2)
        super()._select_dropdown_by_index(self.__region_state_dropdown_list, 1)
        super()._type(self.__zip_code_input_field, self.__faker.postcode())
        super()._type(self.__username_input_field, self.__faker.user_name())
        super()._type(self.__password_input_field, password)
        super()._type(self.__password_confirm_input_field, password)
        super()._click(self.__privacy_police_checkbox)
        super()._click(self.__continue_button)
        
                









            

    
    