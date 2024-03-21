from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage, MainPageLocators

class DatePickerLocators:

    # Поле выбор даты
    SELECT_DATE_INPUT = (By.ID, "#datePickerMonthYearInput")

    # Выпадающий список месяцев
    DROPDOWN_MONTHS = (By.XPATH, "//select[@class='react-datepicker__month-select']")

    # Выпадающий список лет
    DROPDOWN_YEARS = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    # Выбор дня месяца
    SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")


class DatePickerPage(MainPage):

    