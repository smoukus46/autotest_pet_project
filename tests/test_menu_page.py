from pages.menu_page import MenuPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C19')
def test_tool_tips(browser):
    """Проверка отображения меню"""
    test_tool_tips = MenuPage(browser)
    test_tool_tips.open_main_page()
    test_tool_tips.click_button_widgets_page()
    test_tool_tips.click_menu_button()
    test_tool_tips.check_elements_in_menu()
    test_tool_tips.check_elements_in_sub_menu()
