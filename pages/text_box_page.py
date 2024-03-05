from .base_page import BasePage
from .locators import *

input_items = [TextBoxPageLocators.NAME_INPUT, TextBoxPageLocators.EMAIL_INPUT,
               TextBoxPageLocators.CURRENT_ADDRESS_INPUT, TextBoxPageLocators.PERMANENT_ADDRESS_INPUT,
               TextBoxPageLocators.SUBMIT_BTN]


class TextBoxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def inputs_is_displayed(self):
        return self.items_is_displayed(input_items)

    def open_text_box_tab(self):
        self.button_click(TextBoxPageLocators.TEXT_BOX_ITEM)

    def fill_name_input(self):
        self.fill_input(TextBoxPageLocators.NAME_INPUT, 'Artem.Alenin')

    def fill_email_input(self):
        self.fill_input(TextBoxPageLocators.EMAIL_INPUT, 'Artem.Alenin@test.ru')

    def fill_current_address(self):
        self.fill_input(TextBoxPageLocators.CURRENT_ADDRESS_INPUT, 'City of Kursk')

    def fill_permanent_address(self):
        self.fill_input(TextBoxPageLocators.PERMANENT_ADDRESS_INPUT, 'Kosinovo village')

    def click_submit_button(self):
        self.button_click(TextBoxPageLocators.SUBMIT_BTN)
