import time
from pages.auto_complete_page import AutoCompletePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C13')
def test_auto_complete(browser):
    """Проверка работы автокомплита"""
    test_auto_complete_page = AutoCompletePage(browser)
    test_auto_complete_page.open_main_page()
    test_auto_complete_page.click_button_widgets_page()
    test_auto_complete_page.click_auto_complete_button()
    for _ in range(3):
        test_auto_complete_page.fill_input_multiple()
        test_auto_complete_page.key_enter_multiple()
        time.sleep(2)
    test_auto_complete_page.key_del_multiple()
    time.sleep(2)
    test_auto_complete_page.delete_all_values_in_multiple()
    test_auto_complete_page.fill_input_single()
    test_auto_complete_page.key_enter_multiple()
