import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def driver():
    manager = ChromeDriverManager()
    my_driver = webdriver.Chrome(service=ChromeService(manager.install()))
    yield my_driver
    my_driver.quit()