from .main_page import MainPage
from selenium.webdriver import ActionChains
from .locators import *


class ButtonsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def double_click_message_is_displayed(self):
        """Проверяет отображение сообщения о нажатии на кнопку двойного клика"""
        return self.element_is_visible(ButtonsPageLocators.DOUBLE_CLICK_MESSAGE)

    def right_click_message_is_displayed(self):
        """Проверяет отображение сообщения о нажатии на кнопку правого клика"""
        return self.element_is_visible(ButtonsPageLocators.RIGHT_CLICK_MESSAGE)

    def dynamic_click_message_is_displayed(self):
        """Проверяет отображение сообщения о нажатии на кнопку динамического клика"""
        return self.element_is_visible(ButtonsPageLocators.DYNAMIC_CLICK_MESSAGE)

    def open_buttons_tab(self):
        """Нажимает на пункт меню Buttons"""
        self.find_element(ButtonsPageLocators.BUTTONS_ITEM).click()

    def click_dynamic_button(self):
        """Нажимает динамическую кнопку"""
        self.find_element(ButtonsPageLocators.CLICK_ME_BTN).click()

    def button_double_click(self):
        """Нажимает кнопку двойного клика"""
        action = ActionChains(self.browser)
        action.double_click(self.find_element(ButtonsPageLocators.DOUBLE_CLICK_BTN)).perform()

    def button_right_click(self):
        """Нажимает кнопку правого клика"""
        action = ActionChains(self.browser)
        action.context_click(self.find_element(ButtonsPageLocators.RIGHT_CLICK_BTN)).perform()
