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