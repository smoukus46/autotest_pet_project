from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.main_page import MainPage
from generator.generator import Date

class DatePickerLocators:

    # Кнопка Date Picker в выпадающем списке Widgets
    DATE_PICKER_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Date Picker']")

    # Поле выбор даты
    SELECT_DATE_INPUT = (By.ID, "#datePickerMonthYearInput")

    # Выпадающий список месяцев
    DROPDOWN_MONTHS = (By.XPATH, "//select[@class='react-datepicker__month-select']")

    # Выпадающий список лет
    DROPDOWN_YEARS = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    # Выбор дня месяца
    SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")


class DatePickerPage(MainPage):


    date_input = Date()
    year = date_input.year
    month_name = date_input.month_name
    number_month = date_input.month_number
    day = date_input.day
    time = date_input.time[:-3]

    def click_date_picker_button(self):
        """Нажимает кнопку "Date Picker" в выпадающем списке Widgets"""
        return self.find_element(DatePickerLocators.DATE_PICKER_ITEM).click()

    def open_date_picker_dropdown(self):
        """Нажимает в поле ввода даты и открывает выпадающий список"""
        return self.find_element(DatePickerLocators.SELECT_DATE_INPUT).click()

    def select_month_and_year(self, month_name=month_name, year=year, day=day):
        """Выбирает месяц, год и день месяца"""
        try:
            self.select_value_text(DatePickerLocators.DROPDOWN_MONTHS, month_name)
            self.select_value_text(DatePickerLocators.DROPDOWN_YEARS, year)
            self.set_date_item_from_list(DatePickerLocators.SELECT_DAY, day)
        except NoSuchElementException:
            print("Такого элемента нет")

    def set_date_item_from_list(self, elements, value):
        item_list = self.find_element(elements)
        
        for item in item_list:
            if item == value:
                item.click()
                break