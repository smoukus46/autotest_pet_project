from .base_page import BasePage
from .locators import *


class RadioButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_yes_radio_button(self):
        self.button_click(RadioBtnPageLocators.YES_RADIO_BTN)

    def click_impressive_radio_button(self):
        self.button_click(RadioBtnPageLocators.IMPRESSIVE_RADIO_BTN)

    def no_button_is_displayed(self):
        return self.is_element_displayed(RadioBtnPageLocators.NO_RADIO_BTN)
