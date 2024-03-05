from .base_page import BasePage
from .locators import *

hobbies = [PracticeFormPageLocators.HOBBIES_SPORTS_CHECKBOX, PracticeFormPageLocators.HOBBIES_READING_CHECKBOX]


class PracticeFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def forms_menu_item_is_displayed(self):
        return self.is_element_displayed(PracticeFormPageLocators.PRACTICE_FORM_ITEM)

    def open_practice_tab(self):
        self.button_click(PracticeFormPageLocators.PRACTICE_FORM_ITEM)

    def fill_first_name_input(self):
        self.fill_input(PracticeFormPageLocators.FIRST_NAME_INPUT, 'Ken')

    def fill_last_name_input(self):
        self.fill_input(PracticeFormPageLocators.LAST_NAME_INPUT, 'Smith')

    def fill_email_input(self):
        self.fill_input(PracticeFormPageLocators.EMAIL_INPUT, 'KenSmith@test.ru')

    def gender_radio_click(self):
        self.button_click(PracticeFormPageLocators.GENDER_BTN)

    def fill_mobile_input(self):
        self.fill_input(PracticeFormPageLocators.MOBILE_INPUT, '88005553535')

    def fill_subjects_input(self):
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Chemistry, Math')

    def hobbies_checkbox_click(self):
        for hobbie in hobbies:
            self.button_click(hobbie)

    def fill_current_address_input(self):
        self.fill_input(PracticeFormPageLocators.CURRENT_ADDRESS_INPUT, 'Pushkina st., house of Kolotushkin')

    def fill_state_selector(self):
        self.find(PracticeFormPageLocators.STATE_INPUT).click()
        self.find(PracticeFormPageLocators.STATE_SELECT).click()

    def fill_city_selector(self):
        self.find(PracticeFormPageLocators.CITY_INPUT).click()
        self.find(PracticeFormPageLocators.CITY_SELECT).click()

    def click_submit_button(self):
        self.button_click(PracticeFormPageLocators.SUBMIT_BTN)
