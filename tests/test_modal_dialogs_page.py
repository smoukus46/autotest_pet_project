from pages.modal_dialogs_page import ModalDialogsPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C11')
def test_check_alerts(browser):
    """Проверка размера модальных окон"""
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.open_main_page()
    modal_dialogs_page.click_alerts_page_button()
    modal_dialogs_page.alerts_menu_items_is_displayed()
    modal_dialogs_page.open_modal_dialogs_tab()
    modal_dialogs_page.click_small_modal_button()
    modal_dialogs_page.check_small_modal_is_visible()
    modal_dialogs_page.click_close_small_modal_button()
    modal_dialogs_page.click_large_modal_button()
    modal_dialogs_page.check_large_modal_is_visible()
    modal_dialogs_page.click_close_large_modal_button()
