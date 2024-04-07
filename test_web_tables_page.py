from .pages.web_tables_page import WebTablesPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C25')
def test_adding_info_in_web_table(browser):
    """Проверка возможности добавления записи на форме 'Web Tables'"""
    web_tables_page = WebTablesPage(browser)
    web_tables_page.open_main_page()
    web_tables_page.click_menu_elements_button()
    web_tables_page.elements_menu_items_is_displayed()
    web_tables_page.open_web_tables_tab()
    web_tables_page.click_add_button()
    web_tables_page.registration_form_items_is_displayed()
    web_tables_page.fill_registration_form()
    web_tables_page.click_submit_button()
    web_tables_page.check_added_result()


@pytestrail.case('C26')
def test_editing_note_in_web_table(browser):
    """Проверка возможности редактирования записи на форме 'Web Tables'"""
    web_tables_page = WebTablesPage(browser)
    web_tables_page.open_main_page()
    web_tables_page.click_menu_elements_button()
    web_tables_page.elements_menu_items_is_displayed()
    web_tables_page.open_web_tables_tab()
    web_tables_page.open_edit_form()
    web_tables_page.fill_salary_input()
    web_tables_page.click_submit_button()
    web_tables_page.check_editing_row()


@pytestrail.case('C27')
def test_deleting_note_in_web_table(browser):
    """Проверка возможности удаления записи на форме 'Web Tables'"""
    web_tables_page = WebTablesPage(browser)
    web_tables_page.open_main_page()
    web_tables_page.click_menu_elements_button()
    web_tables_page.elements_menu_items_is_displayed()
    web_tables_page.open_web_tables_tab()
    web_tables_page.check_deleting()


@pytestrail.case('C28')
def test_check_searching_in_web_table(browser):
    """Проверка возможности поиска на форме 'Web Tables'"""
    web_tables_page = WebTablesPage(browser)
    web_tables_page.open_main_page()
    web_tables_page.click_menu_elements_button()
    web_tables_page.elements_menu_items_is_displayed()
    web_tables_page.open_web_tables_tab()
    web_tables_page.searching_in_table("Cierra")
    web_tables_page.check_searching_result(["Cierra", "Vega", "39"])
    web_tables_page.searching_in_table("Legal")
    web_tables_page.check_searching_result(["Kierra", "Gentry", "29"])
