from .main_page import MainPage
from .locators import *


class BrowserWindowsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_browser_windows_tab(self):
        """Открывает вкладку Browser Windows"""
        self.find_element(BrowserWindowsPageLocators.BROWSER_WINDOWS_ITEM).click()

    def click_new_tab_button(self):
        """Нажимает кнопку New Tab"""
        self.find_element(BrowserWindowsPageLocators.NEW_TAB_BTN).click()

    def new_window_is_displayed(self, window_number):
        """Проверяет отображение нового окна"""
        self.switch_to_window(window_number)
        new_tab = self.find_element(BrowserWindowsPageLocators.NEW_TAB_WINDOW_TEXT)
        assert new_tab.text == "This is a sample page", "Текст не соответствует ожидаемому"
        self.close_window()
        self.switch_to_window(0)

    def click_new_window_button(self):
        """Нажимает кнопку New Window"""
        self.find_element(BrowserWindowsPageLocators.NEW_WINDOW_BTN).click()

    def click_new_window_message(self):
        """Нажимает кнопку New Window Message"""
        self.find_element(BrowserWindowsPageLocators.NEW_WINDOW_MESSAGE).click()

    def about_blank_window_is_displayed(self):
        """Проверяет отображение окна с адресом about:blank"""
        new_window_handle = [window for window in self.browser.window_handles if window != self.browser.current_window_handle][0]
        self.browser.switch_to.window(new_window_handle)
        self.close_window()
        self.switch_to_window(0)
