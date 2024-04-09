import time
from pages.login_page import LoginPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C21')
def test_register_user_in_book_store(browser):
    """Регистрация пользователя"""
    login_page = LoginPage(browser)
    login_page.open_main_page()
    login_page.open_book_store_application()
    login_page.book_store_application_menu_items_is_displayed()
    login_page.open_login_tab()
    login_page.click_new_user_btn()
    login_page.fill_registration_form()
    time.sleep(5)
    login_page.check_alert()
    login_page.click_back_to_login_btn()
