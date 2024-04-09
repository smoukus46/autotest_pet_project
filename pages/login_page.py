from .main_page import MainPage
import time
import requests
from .locators import *

menu_items = [LoginPageLocators.LOGIN_ITEM, LoginPageLocators.BOOK_STORE_ITEM,
              LoginPageLocators.PROFILE_ITEM, LoginPageLocators.BOOK_STORE_API_ITEM]


class LoginPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_book_store_application(self):
        self.find_element(MainPageLocators.BOOK_STORE_PAGE).click()

    def book_store_application_menu_items_is_displayed(self):
        """Проверяет отображение всех разделов меню Elements"""
        return self.items_is_displayed(menu_items)

    def open_login_tab(self):
        self.find_element(LoginPageLocators.LOGIN_ITEM).click()

    def click_new_user_btn(self):
        self.find_element(LoginPageLocators.NEW_USER_BTN).click()

    def fill_registration_form(self):
        self.fill_input(RegisterPageLocators.FIRST_NAME_INPUT, 'Artem')
        self.fill_input(RegisterPageLocators.LAST_NAME_INPUT, 'Alenin')
        self.fill_input(RegisterPageLocators.USER_NAME_INPUT, 'Artem.Alenin3')
        self.fill_input(RegisterPageLocators.PASSWORD_INPUT, 'Artem!Alenin46')
        iframe = self.find_element(RegisterPageLocators.CAPTCHA_FRAME)
        self.browser.switch_to.frame(iframe)
        self.find_element(RegisterPageLocators.CAPTCHA_CHECKBOX).click()
        time.sleep(10)
        self.browser.switch_to.default_content()
        self.find_element(RegisterPageLocators.REGISTER_BTN).click()

    def check_alert(self):
        alert = self.browser.switch_to.alert()
        assert alert.text == 'User Register Successfully.'
        alert.accept()

    def click_back_to_login_btn(self):
        self.find_element(RegisterPageLocators.BACK_TO_LOGIN_BTN).click()
