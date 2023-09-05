import pytest
import webdriver_manager
from page_objects.checkout_page import CheckoutPage

from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.special_offers_page import SpecialOffersPage


class TestPositiveScenarios:

    @pytest.mark.positive
    @pytest.mark.order
    def test_complete_order(self, driver: webdriver_manager):
        home_page = HomePage(driver)
        specials_page = SpecialOffersPage(driver)
        product_page = ProductPage(driver)
        shopping_cart = ShoppingCartPage(driver)
        login_page = LoginPage(driver)
        checkout_page = CheckoutPage(driver)
        product_title = "Absolue Eye Precious Cells"

        home_page.open_url()
        home_page.hover_menu_button()
        home_page.click_specials_button()
        assert home_page.current_url == specials_page.get_url(), "The actual URL is not the expected."
        specials_page.click_on_product(product_title)
        assert product_page.get_title() == product_title, "Product title is not the expected"
        product_page.add_to_cart()
        assert product_page.current_url == shopping_cart.get_url(), "The actual URL is not the expected."
        shopping_cart.checkout_order()
        login_page.type_user_credentials("johndoe1234", "Password123")
        login_page.click_login_button()
        assert login_page.current_url == checkout_page.get_url(), "The actual URL is not the expected."
        assert checkout_page.is_item_in_the_cart(product_title) == True, "Item isn't in the cart."
        checkout_page.confirm_order()
        assert checkout_page.has_order_been_processed() == True, "The order has not been processed!"