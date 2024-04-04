import time
from .main_page import MainPage
from .locators import *
from selenium.common.exceptions import NoSuchElementException
from generator.generator import Date

hobbies = [PracticeFormPageLocators.HOBBIES_SPORTS_CHECKBOX, PracticeFormPageLocators.HOBBIES_READING_CHECKBOX,
           PracticeFormPageLocators.HOBBIES_MUSIC_CHECKBOX]


class PracticeFormPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    date_input = Date()
    year_select_date = date_input.year_for_select_date
    year_date_and_time = date_input.year_for_date_and_time
    month_name = date_input.month_name
    number_month = date_input.month_number
    day = date_input.day
    time = date_input.time

    def click_menu_forms_button(self):
        """Нажимает на кнопку Forms"""
        self.find_element(MainPageLocators.FORMS_PAGE).click()

    def forms_menu_item_is_displayed(self):
        """Проверяет отображение вкладок меню Forms"""
        return self.element_is_visible(PracticeFormPageLocators.PRACTICE_FORM_ITEM)

    def open_practice_tab(self):
        """Открывает вкладку practice form"""
        self.find_element(PracticeFormPageLocators.PRACTICE_FORM_ITEM).click()

    def fill_first_name_input(self):
        """"Заполняет поле имя"""
        self.fill_input(PracticeFormPageLocators.FIRST_NAME_INPUT, 'Ken')

    def fill_last_name_input(self):
        """Заполняет поле фамилия"""
        self.fill_input(PracticeFormPageLocators.LAST_NAME_INPUT, 'Smith')

    def fill_email_input(self):
        """Заполняет поле email"""
        self.fill_input(PracticeFormPageLocators.EMAIL_INPUT, 'KenSmith@test.ru')

    def gender_radio_click(self):
        """Нажимает на кнопку выбора пола"""
        self.find_element(PracticeFormPageLocators.GENDER_BTN).click()

    def fill_mobile_input(self):
        """Заполняет поле мобильный телефон"""
        self.fill_input(PracticeFormPageLocators.MOBILE_INPUT, '8800555353')

    def set_date_item_from_list(self, elements, value):
        """Выбирает дату"""
        item_list = self.find_elements(elements)

        for item in item_list:
            if item.text == value:
                item.click()
                break

    def fill_datepicker(self, month_name=month_name, year=year_select_date, day=day):
        """Заполняет поле дата"""
        self.find_element(PracticeFormPageLocators.DATE_OR_BIRTH_INPUT).click()
        try:
            self.select_value_text(PracticeFormPageLocators.DATEPICKER_MONTH, month_name)
            self.select_value_text(PracticeFormPageLocators.DATEPICKER_YEAR, year)
            self.set_date_item_from_list(PracticeFormPageLocators.DATEPICKER_DAY, day)
        except NoSuchElementException:
            print("Такого элемента нет")

    def fill_subjects_input(self):
        """Заполняет поле предметы"""
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Chemistry')
        time.sleep(2)
        self.find_element(PracticeFormPageLocators.SUBJECT_CHEMISTRY_ITEM).click()
        self.fill_input(PracticeFormPageLocators.SUBJECT_INPUT, 'Maths')
        time.sleep(2)
        self.find_element(PracticeFormPageLocators.SUBJECT_MATHS_ITEM).click()

    def hobbies_checkbox_click(self):
        """Заполняет поле хобби"""
        for hobbie in hobbies:
            self.find_element(hobbie).click()

    def upload_picture(self):
        """Загружает файл"""
        self.fill_input(PracticeFormPageLocators.UPLOAD_PICTURE_BTN, 'D:/1.png')

    def fill_current_address_input(self):
        """Заполняет поле адрес проживания"""
        self.fill_input(PracticeFormPageLocators.CURRENT_ADDRESS_INPUT, 'Pushkina st., house of Kolotushkin')

    def fill_state_selector(self):
        """Заполняет поле штат"""
        self.find_element(PracticeFormPageLocators.STATE_INPUT).click()
        self.find_element(PracticeFormPageLocators.STATE_NCR_SELECT).click()

    def fill_city_selector(self):
        """Заполняет поле город"""
        self.find_element(PracticeFormPageLocators.CITY_INPUT).click()
        self.find_element(PracticeFormPageLocators.CITY_GURGAON_SELECT).click()

    def click_submit_button(self):
        """Нажимает на кнопку Submit"""
        self.find_element(PracticeFormPageLocators.SUBMIT_BTN).click()

    def click_close_button(self):
        """Нажимает кнопку Закрыть"""
        self.find_element(PracticeFormPageLocators.CLOSE_BTN).click()
