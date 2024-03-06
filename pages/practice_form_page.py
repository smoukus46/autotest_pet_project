from .base_page import BasePage
from .locators import *

hobbies = [PracticeFormPageLocators.HOBBIES_SPORTS_CHECKBOX, PracticeFormPageLocators.HOBBIES_READING_CHECKBOX]


class PracticeFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_forms_button(self):
        self.button_click(PracticeFormPageLocators.PRACTICE_FORM_ITEM)

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
        self.fill_input(PracticeFormPageLocators.MOBILE_INPUT, '8800555353')

    def fill_datepicker(self):
        self.button_click(PracticeFormPageLocators.DATE_OR_BIRTH_INPUT)
        self.fill_selector_by_value(PracticeFormPageLocators.DATEPICKER_MONTH, '9')
        self.fill_selector_by_value(PracticeFormPageLocators.DATEPICKER_YEAR, '1997')
        self.find(PracticeFormPageLocators.DATEPICKER_DAY).click()

    def fill_subjects_input(self):
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Chemistry')
        self.find(PracticeFormPageLocators.SUBJECT_CHEMISTRY_ITEM).click()
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Maths')
        self.find(PracticeFormPageLocators.SUBJECT_MATHS_ITEM).click()

    def hobbies_checkbox_click(self):
        for hobbie in hobbies:
            self.button_click(hobbie)

    def upload_picture(self):
        self.button_click(PracticeFormPageLocators.UPLOAD_PICTURE_BTN)
        self.fill_input(PracticeFormPageLocators.UPLOAD_PICTURE_BTN, 'D:/1.png')

    def fill_current_address_input(self):
        self.fill_input(PracticeFormPageLocators.CURRENT_ADDRESS_INPUT, 'Pushkina st., house of Kolotushkin')

    def fill_state_selector(self):
        self.find(PracticeFormPageLocators.STATE_INPUT).click()
        self.find(PracticeFormPageLocators.STATE_NCR_SELECT).click()

    def fill_city_selector(self):
        self.find(PracticeFormPageLocators.CITY_INPUT).click()
        self.find(PracticeFormPageLocators.CITY_GURGAON_SELECT).click()

    def click_submit_button(self):
        self.button_click(PracticeFormPageLocators.SUBMIT_BTN)

    def click_close_button(self):
        self.button_click(PracticeFormPageLocators.CLOSE_BTN)
