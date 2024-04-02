from .main_page import MainPage
from .locators import *

hobbies = [PracticeFormPageLocators.HOBBIES_SPORTS_CHECKBOX, PracticeFormPageLocators.HOBBIES_READING_CHECKBOX]


class PracticeFormPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_forms_button(self):
        self.find_element(PracticeFormPageLocators.PRACTICE_FORM_ITEM).click()

    def forms_menu_item_is_displayed(self):
        return self.is_element_displayed(PracticeFormPageLocators.PRACTICE_FORM_ITEM)

    def open_practice_tab(self):
        self.find_element(PracticeFormPageLocators.PRACTICE_FORM_ITEM).click()

    def fill_first_name_input(self):
        self.fill_input(PracticeFormPageLocators.FIRST_NAME_INPUT, 'Ken')

    def fill_last_name_input(self):
        self.fill_input(PracticeFormPageLocators.LAST_NAME_INPUT, 'Smith')

    def fill_email_input(self):
        self.fill_input(PracticeFormPageLocators.EMAIL_INPUT, 'KenSmith@test.ru')

    def gender_radio_click(self):
        self.find_element(PracticeFormPageLocators.GENDER_BTN).click()

    def fill_mobile_input(self):
        self.fill_input(PracticeFormPageLocators.MOBILE_INPUT, '8800555353')

    def fill_datepicker(self):
        self.find_element(PracticeFormPageLocators.DATE_OR_BIRTH_INPUT).click()
        self.fill_selector_by_value(PracticeFormPageLocators.DATEPICKER_MONTH, '9')
        self.fill_selector_by_value(PracticeFormPageLocators.DATEPICKER_YEAR, '1997')
        self.find_element(PracticeFormPageLocators.DATEPICKER_DAY).click()

    def fill_subjects_input(self):
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Chemistry')
        self.find_element(PracticeFormPageLocators.SUBJECT_CHEMISTRY_ITEM).click()
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Maths')
        self.find_element(PracticeFormPageLocators.SUBJECT_MATHS_ITEM).click()

    def hobbies_checkbox_click(self):
        for hobbie in hobbies:
            self.find_element(hobbie).click()

    def upload_picture(self):
        self.find_element(PracticeFormPageLocators.UPLOAD_PICTURE_BTN).click()
        self.fill_input(PracticeFormPageLocators.UPLOAD_PICTURE_BTN, 'D:/1.png')

    def fill_current_address_input(self):
        self.fill_input(PracticeFormPageLocators.CURRENT_ADDRESS_INPUT, 'Pushkina st., house of Kolotushkin')

    def fill_state_selector(self):
        self.find_element(PracticeFormPageLocators.STATE_INPUT).click()
        self.find_element(PracticeFormPageLocators.STATE_NCR_SELECT).click()

    def fill_city_selector(self):
        self.find_element(PracticeFormPageLocators.CITY_INPUT).click()
        self.find_element(PracticeFormPageLocators.CITY_GURGAON_SELECT).click()

    def click_submit_button(self):
        self.find_element(PracticeFormPageLocators.SUBMIT_BTN).click()

    def click_close_button(self):
        self.find_element(PracticeFormPageLocators.CLOSE_BTN).click()
