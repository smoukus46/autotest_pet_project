import time
from pages.datepicker_page import DatePickerPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C14')
def test_date_picker(browser):
    """Проверка работы дата пикера"""
    test_date_picker = DatePickerPage(browser)
    test_date_picker.open_main_page()
    test_date_picker.click_button_widgets_page()
    test_date_picker.click_date_picker_button()
    test_date_picker.open_date_picker_dropdown()
    test_date_picker.select_month_and_year()
