from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        button_add_to_basket.click()

    def is_good_in_basket(self, what):
        good_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert what == good_name_in_basket, f"Where is no '{what}' in basket. Checked at site {self.url}"

    def is_good_price_equal_basket_price(self, price):
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text
        assert price == basket_price, f"'{price}' didn't equal {basket_price}. Checked at site {self.url}"

    def get_good_name(self):
        good_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TO_ADD).text
        return good_name

    def get_good_price(self):
        good_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return good_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
