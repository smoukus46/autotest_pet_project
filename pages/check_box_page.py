from .main_page import MainPage
from .locators import *

items = [CheckBoxPageLocators.DESKTOP_TITLE, CheckBoxPageLocators.DOCUMENTS_TITLE,
         CheckBoxPageLocators.DOWNLOADS_TITLE, CheckBoxPageLocators.NOTES_TITLE,
         CheckBoxPageLocators.COMMANDS_TITLE, CheckBoxPageLocators.VEU_TITLE,
         CheckBoxPageLocators.GENERAL_TITLE, CheckBoxPageLocators.EXCEL_FILE_TITLE]
home_items = [CheckBoxPageLocators.DESKTOP_TITLE, CheckBoxPageLocators.DOCUMENTS_TITLE,
              CheckBoxPageLocators.DOWNLOADS_TITLE]
desktop_items = [CheckBoxPageLocators.NOTES_TITLE, CheckBoxPageLocators.COMMANDS_TITLE]


class CheckBoxPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_checkbox_tab(self):
        self.find_element(CheckBoxPageLocators.CHECKBOX_ITEM).click()

    def open_all_list(self):
        self.find_element(CheckBoxPageLocators.EXPAND_ALL_BTN).click()

    def check_all_items_is_displayed(self):
        self.items_is_displayed(items)

    def close_all_list(self):
        self.find_element(CheckBoxPageLocators.COLLAPSE_ALL_BTN).click()

    def check_all_items_is_not_displayed(self):
        self.items_is_not_displayed(items)

    def open_home_expand_button(self):
        self.find_element(CheckBoxPageLocators.EXPAND_HOME_BTN).click()

    def check_home_items_is_displayed(self):
        self.items_is_displayed(home_items)

    def open_desktop_expand_button(self):
        self.find_element(CheckBoxPageLocators.EXPAND_DESKTOP_BTN).click()

    def check_desktop_items_is_displayed(self):
        self.items_is_displayed(desktop_items)

    def click_notes_checkbox(self):
        self.find_element(CheckBoxPageLocators.NOTES_CHECKBOX).click()

    def click_home_checkbox(self):
        self.find_element(CheckBoxPageLocators.HOME_CHECKBOX).click()

    def check_result_box(self, assertion_text):
        span_text = []
        result_box_element = self.find_element(CheckBoxPageLocators.RESULT_BOX)
        span_elements = result_box_element.find_elements_by_tag_name("span")

        for span_element in span_elements:
            span_text.append(span_element)
            print(span_element.text)
        print(span_text)
        assert assertion_text in span_text

    def result_box_is_not_displayed(self):
        self.element_is_not_displayed(CheckBoxPageLocators.RESULT_BOX)