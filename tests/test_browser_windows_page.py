from pages.browser_windows_page import BrowserWindowsPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C9')
def test_open_browser_windows(browser):
    """Проверка открытия окон браузера"""
    browser_windows_page = BrowserWindowsPage(browser)
    browser_windows_page.open_main_page()
    browser_windows_page.click_alerts_page_button()
    browser_windows_page.alerts_menu_items_is_displayed()
    browser_windows_page.open_browser_windows_tab()
    browser_windows_page.click_new_tab_button()
    browser_windows_page.new_window_is_displayed(1)
    browser_windows_page.click_new_window_button()
    browser_windows_page.new_window_is_displayed(-1)
    browser_windows_page.click_new_window_message()
    browser_windows_page.about_blank_window_is_displayed()
