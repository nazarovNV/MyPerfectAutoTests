from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        index_of_word_login = current_url.find('login')
        assert index_of_word_login != -1, "There is no word 'login' in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "Sign up form is not presented"

    def register_new_user(self, email, password):
        sign_up_email_input = self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL_INPUT)
        sign_up_email_input.send_keys(email)

        sign_up_password_input = self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD_INPUT)
        sign_up_password_input.send_keys(password)

        sign_up_repeat_password_input = self.browser.find_element(*LoginPageLocators.SIGN_UP_REPEAT_PASSWORD_INPUT)
        sign_up_repeat_password_input.send_keys(password)

        sign_up_button = self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON)
        sign_up_button.click()



