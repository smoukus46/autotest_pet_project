from pages.select_menu_page import SelectMenuPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C20')
def test_select_menu(browser):
    """Проверка работы select menu"""
    test_select_menu = SelectMenuPage(browser)
    test_select_menu.open_main_page()
    test_select_menu.click_button_page('widgets_page')
    test_select_menu.click_select_menu_button()
    test_select_menu.click_and_fill_select_value_input()
    test_select_menu.click_and_fill_select_one_input()
    test_select_menu.click_and_fill_old_style_select_menu()
    test_select_menu.fill_standart_multi_select_input()
    test_select_menu.click_and_fill_multiselect_dropdown_input()
