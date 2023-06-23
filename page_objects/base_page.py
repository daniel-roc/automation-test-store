from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.common import NoSuchElementException

class BasePage():

    def __init__(self, driver: WebDriver):
        self._driver = driver
    
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    def _open_url(self, url: str):
        self._driver.get(url)
    
    def _find(self, locator: tuple):
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str,  time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_clickable(locator, time)
        return self._find(locator).clear()
    
    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_dropdown(self, locator: tuple, selected_text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        dropdow = Select(self._find(locator))
        dropdow.select_by_visible_text(selected_text)

    def _wait_until_element_is_visible(self, locator: tuple,  time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))
    
    def _wait_until_element_is_invisible(self, locator: tuple,  time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.invisibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.element_to_be_clickable(locator))

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False