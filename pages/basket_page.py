from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_text_empty(self):
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert basket_text == "Your basket is empty. Continue shopping", \
            "Where is no 'Your basket is empty. Continue shopping' text"

    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), \
            "Where is goods in basket and they should't be here"


