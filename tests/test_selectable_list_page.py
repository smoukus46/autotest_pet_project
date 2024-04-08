from pages.selectable_page import SelectablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C40')
def test_selectable(browser):
    """Проверка отображения сортировки элементов в плиточном отображении"""
    test_selectable = SelectablePage(browser)
    test_selectable.open_main_page()
    test_selectable.click_button_page('interactions_page')
    test_selectable.click_selectable_button()
    test_selectable.select_random_element()
