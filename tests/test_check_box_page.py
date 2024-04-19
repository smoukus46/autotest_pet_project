from pages.check_box_page import CheckBoxPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C23')
def test_checkboxes(browser):
    """Проверка корректной работы чек-боксов в деталях"""
    checkbox_page = CheckBoxPage(browser)
    checkbox_page.open_main_page()
    checkbox_page.click_menu_elements_button()
    checkbox_page.elements_menu_items_is_displayed()
    checkbox_page.open_checkbox_tab()
    checkbox_page.open_all_list()
    checkbox_page.check_all_items_is_displayed()
    checkbox_page.close_all_list()
    checkbox_page.check_all_items_is_not_displayed()
    checkbox_page.open_home_expand_button()
    checkbox_page.check_home_items_is_displayed()
    checkbox_page.open_desktop_expand_button()
    checkbox_page.check_desktop_items_is_displayed()
    checkbox_page.click_notes_checkbox()
    checkbox_page.check_result_box('notes')
    checkbox_page.click_notes_checkbox()
    checkbox_page.result_box_is_not_displayed()
    checkbox_page.click_home_checkbox()
    checkbox_page.check_result_box('wordFile')
