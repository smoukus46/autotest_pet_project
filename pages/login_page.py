from .main_page import MainPage
import time
from .locators import *

menu_items = [LoginPageLocators.LOGIN_ITEM, LoginPageLocators.BOOK_STORE_ITEM,
              LoginPageLocators.PROFILE_ITEM, LoginPageLocators.BOOK_STORE_API_ITEM]


class LoginPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_book_store_application(self):
        """Открывает раздел Book Store"""
        self.find_element(MainPageLocators.BOOK_STORE_PAGE).click()

    def book_store_application_menu_items_is_displayed(self):
        """Проверяет отображение всех разделов меню Elements"""
        return self.items_is_displayed(menu_items)

    def open_login_tab(self):
        """Открывает вкладку Login"""
        self.find_element(LoginPageLocators.LOGIN_ITEM).click()

    def fill_login_form(self):
        """Заполняет форму логина"""
        self.fill_input(LoginPageLocators.USER_NAME_INPUT, "Artem.Alenin5")
        self.fill_input(LoginPageLocators.PASSWORD_INPUT, "Artem!Alenin46")

    def click_new_user_btn(self):
        """Нажимает кнопку New User"""
        self.find_element(LoginPageLocators.NEW_USER_BTN).click()

    def switch_to_captcha_on_registration_form(self):
        """Переключает на капчу на форме регистрации и проставляет чек-бокс капчи"""
        iframe = self.find_element(RegisterPageLocators.CAPTCHA_FRAME)
        self.browser.switch_to.frame(iframe)
        self.find_element(RegisterPageLocators.CAPTCHA_CHECKBOX).click()

    def fill_registration_form(self):
        """Заполняет форму регистрации и проставляет чек-бокс в капче"""
        self.fill_input(RegisterPageLocators.FIRST_NAME_INPUT, 'Artem')
        self.fill_input(RegisterPageLocators.LAST_NAME_INPUT, 'Alenin')
        self.fill_input(RegisterPageLocators.USER_NAME_INPUT, 'Artem.Alenin5')
        self.fill_input(RegisterPageLocators.PASSWORD_INPUT, 'Artem!Alenin46')
        self.switch_to_captcha_on_registration_form()
        time.sleep(30)
        self.browser.switch_to.default_content()
        self.find_element(RegisterPageLocators.REGISTER_BTN).click()

    def check_alert(self):
        """Проверяет появление уведомления о том, что пользователь зарегистрирован"""
        alert = self.browser.switch_to.alert
        assert alert.text == 'User Register Successfully.'
        alert.accept()
        self.browser.switch_to.default_content()

    def click_back_to_login_btn(self):
        """Нажимает на кнопку Back to login"""
        self.find_element(RegisterPageLocators.BACK_TO_LOGIN_BTN).click()

    def click_to_login_btn(self):
        """Нажимает на кнопку Login"""
        self.find_element(LoginPageLocators.LOGIN_BTN).click()

    def profile_page_elements_is_present(self):
        """Проверяет отображение элементов на странице Profile"""
        self.element_is_visible(ProfilePageLocators.LOG_OUT_BTN)
        user_name = self.find_element(ProfilePageLocators.USER_NAME_LABEL)
        assert user_name.text == "Artem.Alenin5"
