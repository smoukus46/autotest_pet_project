import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.main_page import MainPage
from generator.generator import Date

class DatePickerLocators:

    # Кнопка Date Picker в выпадающем списке Widgets
    DATE_PICKER_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Date Picker']")

    # Поле Select Date
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")

    # Выпадающий список месяцев в поле Select Date
    SELECT_DATE_DROPDOWN_MONTHS = (By.XPATH, "//select[@class='react-datepicker__month-select']")

    # Выпадающий список лет в поле Select Date
    SELECT_DATE_DROPDOWN_YEARS = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    # Выбор дня месяца в поле Select Date
    SELECT_DATE_SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    # Поле Date And Time
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")

    # Кнопка раскрытия выпадающего списка месяцев в поле Date And Time
    DATE_AND_TIME_MONTHS = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")

    # Выпадающий список месяцев
    DATE_AND_TIME_MONTHS_VALUES = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")

    # Кнопка раскрытия выпадающего списка лет в поле Date And Time
    DATE_AND_TIME_YEARS = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")

    # Выпадающий список лет
    DATE_AND_TIME_YEARS_VALUES = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

    # Выбор дня месяца в поле Date And Time
    DATE_AND_TIME_SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    # Выпадающий список выбора времени в поле Date And Time
    DATE_AND_TIME_SELECT_TIME = (By.CSS_SELECTOR, "li[class^='react-datepicker__time-list-item ']")


class DatePickerPage(MainPage):

    date_input = Date()
    year_select_date = date_input.year_for_select_date
    year_date_and_time = date_input.year_for_date_and_time
    month_name = date_input.month_name
    number_month = date_input.month_number
    day = date_input.day
    time = date_input.time

    def set_date_item_from_list(self, elements, value):
        """Выбирает дату"""
        item_list = self.find_elements(elements)
        
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def click_date_picker_button(self):
        """Нажимает кнопку "Date Picker" в выпадающем списке Widgets"""
        return self.find_element(DatePickerLocators.DATE_PICKER_ITEM).click()

    def open_select_date_dropdown(self):
        """Нажимает в поле ввода Select Date и открывает выпадающий список"""
        return self.find_element(DatePickerLocators.SELECT_DATE_INPUT).click()

    def select_date(self, month_name=month_name, year=year_select_date, day=day):
        """Выбирает месяц, год и день месяца"""
        try:
            self.select_value_text(DatePickerLocators.SELECT_DATE_DROPDOWN_MONTHS, month_name)
            self.select_value_text(DatePickerLocators.SELECT_DATE_DROPDOWN_YEARS, year)
            self.set_date_item_from_list(DatePickerLocators.SELECT_DATE_SELECT_DAY, day)
        except NoSuchElementException:
            print("Такого элемента нет")

    def open_date_and_time_dropdown(self):
        """Нажимает в поле ввода Date And Time и открывает выпадающий список"""
        return self.find_element(DatePickerLocators.DATE_AND_TIME_INPUT).click()
    
    def select_date_and_time(self, month_name=month_name, year=year_date_and_time, day=day, time=time):
        """Выбирает дату и время"""
        try:
            self.find_element(DatePickerLocators.DATE_AND_TIME_MONTHS).click()
            self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_MONTHS_VALUES, month_name)
            self.simple_pause(2)
            self.find_element(DatePickerLocators.DATE_AND_TIME_YEARS).click()
            self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_YEARS_VALUES, year)
            self.simple_pause(2)
            self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_SELECT_DAY, day)
            self.simple_pause(2)
            self.set_date_item_from_list(DatePickerLocators.DATE_AND_TIME_SELECT_TIME, time)
        except NoSuchElementException:
            print("Такого элемента нет")

    def get_attribute_input_before(self):
        """Берет значение поля изначально"""
        value_before = self.get_attribute_element(DatePickerLocators.SELECT_DATE_INPUT, 'value')
        return value_before
    
    def get_attribute_element_input_after(self):
        """Берет значение поля изначально"""
        value_after = self.get_attribute_element(DatePickerLocators.SELECT_DATE_INPUT, 'value')
        return value_after
