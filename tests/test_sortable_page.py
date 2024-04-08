from pages.sortable_page import SortablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C38')
def test_sortable_list(browser):
    """Проверка отображения сортировки элементов в списочном отображении"""
    test_sortable_list = SortablePage(browser)
    test_sortable_list.open_main_page()
    test_sortable_list.click_button_page('interactions_page')
    test_sortable_list.click_sortable_button()
    test_sortable_list.drag_and_drop_list()

@pytestrail.case('C39')
def test_sortable_grid(browser):
    """Проверка отображения сортировки элементов в плиточном отображении"""
    test_sortable_grid = SortablePage(browser)
    test_sortable_grid.open_main_page()
    test_sortable_grid.click_button_page('interactions_page')
    test_sortable_grid.click_sortable_button()
    test_sortable_grid.drag_and_drop_grid()
