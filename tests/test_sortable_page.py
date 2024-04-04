from pages.sortable_page import SortablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C21')
def test_sortable(browser):
    """Проверка работы ползунка"""
    test_sortable = SortablePage(browser)
    test_sortable.open_main_page()
    test_sortable.click_button_page('interactions_page')
    test_sortable.click_sortable_button()
    test_sortable.drag_and_drop_list()
    test_sortable.drag_and_drop_grid()
