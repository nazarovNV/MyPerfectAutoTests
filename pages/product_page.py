from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        button_add_to_basket.click()

    def is_good_in_basket(self, what):
        good_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDEED_TO_BASKET).text
        assert good_name == what, f"Where is no '{what}' good"

    def is_good_price_equal_basket_price(self):
        good_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text
        assert good_price == basket_price, f"'{good_price}' didn't equal {basket_price}"