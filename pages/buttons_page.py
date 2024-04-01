from .main_page import MainPage
from selenium.webdriver import ActionChains
from .locators import *


class ButtonsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def double_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.DOUBLE_CLICK_MESSAGE)

    def right_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.RIGHT_CLICK_MESSAGE)

    def dynamic_click_message_is_displayed(self):
        return self.is_element_displayed(ButtonsPageLocators.DYNAMIC_CLICK_MESSAGE)

    def open_buttons_tab(self):
        self.find_element(ButtonsPageLocators.BUTTONS_ITEM).click()

    def click_dynamic_button(self):
        self.find_element(ButtonsPageLocators.CLICK_ME_BTN).click()

    def button_double_click(self):
        action = ActionChains(self.browser)
        action.double_click(self.find_element(ButtonsPageLocators.DOUBLE_CLICK_BTN)).perform()

    def button_right_click(self):
        action = ActionChains(self.browser)
        action.context_click(self.find_element(ButtonsPageLocators.RIGHT_CLICK_BTN)).perform()
