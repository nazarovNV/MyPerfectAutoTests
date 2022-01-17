from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "form#login_form > p > a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name=login_submit]")

    SIGN_UP_FORM = (By.CSS_SELECTOR, "form#register_form")
    SIGN_UP_EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    SIGN_UP_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    SIGN_UP_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "form.add-to-basket")
    PRODUCT_ADDEED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner:nth-child(2)>p>strong")
    PRODUCT_TO_ADD = (By.CSS_SELECTOR, "div.product_main>h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    GOODS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title")



