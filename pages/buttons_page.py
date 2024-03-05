from .base_page import BasePage
from .locators import *


class ButtonsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def double_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.DOUBLE_CLICK_MESSAGE)

    def right_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.RIGHT_CLICK_MESSAGE)

    def dynamic_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.DYNAMIC_CLICK_MESSAGE)

    def open_buttons_tab(self):
        self.button_click(ButtonsPageLocators.BUTTONS_ITEM)

    def click_dynamic_button(self):
        self.button_click(ButtonsPageLocators.CLICK_ME_BTN)
