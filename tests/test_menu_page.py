from pages.menu_page import MenuPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C19')
def test_menu(browser):
    """Проверка отображения меню"""
    test_menu = MenuPage(browser)
    test_menu.open_main_page()
    test_menu.click_button_page('widgets_page')
    test_menu.click_menu_button()
    test_menu.check_first_main_item()
    test_menu.check_second_main_item()
    test_menu.check_third_main_item()
