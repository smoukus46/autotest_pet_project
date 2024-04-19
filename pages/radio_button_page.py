from .main_page import MainPage
from .locators import *


class RadioButtonPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_yes_radio_button(self):
        """Кликает в радиобаттон yes"""
        self.find_element(RadioBtnPageLocators.YES_RADIO_BTN1).click()

    def click_impressive_radio_button(self):
        """Кликает в радиобаттон Impressive"""
        self.find_element(RadioBtnPageLocators.IMPRESSIVE_RADIO_BTN1).click()

    def no_button_is_disabled(self):
        """Проверяет кнопку No на заблокированность"""
        return self.find_element(RadioBtnPageLocators.NO_RADIO_BTN1).get_attribute("disabled")

    def open_radio_button_tab(self):
        """Открывает вкладку radio button"""
        self.find_element(RadioBtnPageLocators.RADIO_BTN_ITEM).click()
