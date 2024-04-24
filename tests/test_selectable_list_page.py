from pages.selectable_page import SelectablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C40')
def test_selectable_list(browser):
    """Проверка работы выбора элементов в списочном отображении"""
    test_selectable_list = SelectablePage(browser)
    test_selectable_list.open_main_page()
    test_selectable_list.click_button_page('interactions_page')
    test_selectable_list.click_selectable_button()
    test_selectable_list.select_random_element_list()
    test_selectable_list.simple_pause(2)

@pytestrail.case('C41')
def test_selectable_grid(browser):
    """Проверка работы выбора элементов в плиточном отображении"""
    test_selectable_grid = SelectablePage(browser)
    test_selectable_grid.open_main_page()
    test_selectable_grid.click_button_page('interactions_page')
    test_selectable_grid.click_selectable_button()
    test_selectable_grid.select_random_element_grid()
    test_selectable_grid.simple_pause(2)
