import pytest

from page_objects.home_page import HomePage
from page_objects.specials_products_page import SpecialsPage


class TestPositiveScenarios:

    @pytest.mark.positive
    @pytest.mark.order
    @pytest.mark.debug
    def test_complete_order(self, driver):
        home_page = HomePage(driver)
        home_page.open_url()
        home_page.hover_menu_button()
        home_page.click_specials_button()
        specials_page = SpecialsPage(driver)
        assert home_page.current_url == specials_page.get_url(), "The actual URL is not the expected."
        product_title = "Brunette expressions Conditioner"
        specials_page.click_on_product(product_title)
        assert specials_page.get_title() == product_title, "Product title is not the expected"
        
        