import pytest
from selenium import webdriver
from faker import Faker

@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    yield my_driver
    my_driver.quit()

@pytest.fixture()
def faker():
    faker = Faker()
    return faker