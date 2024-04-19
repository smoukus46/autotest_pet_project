from .main_page import MainPage
from pages.locators import *
import time


class AlertsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_alerts_tab(self):
        """Открывает вкладку Alerts"""
        self.find_element(AlertsPageLocators.ALERTS_ITEM).click()

    def check_alert_is_visible(self, locator, sleeping_time: int, assertion_text: str):
        """Проверяет, что всплывающие окна отображаются"""
        self.find_element(locator).click()
        time.sleep(sleeping_time)
        alert = self.browser.switch_to.alert
        assert alert.text == assertion_text
        alert.accept()
        self.browser.switch_to.default_content()

    def check_confirm_alert(self):
        """Проверяет, что всплывающее окно с подтверждением отображается"""
        self.find_element(AlertsPageLocators.CONFIRM_BTN).click()
        alert = self.browser.switch_to.alert
        alert.dismiss()
        self.browser.switch_to.default_content()
        confirm_result = self.find_element(AlertsPageLocators.CONFIRM_RESULT)
        assert confirm_result.text == 'You selected Cancel'

    def check_propmt_alert(self, your_name: str):
        """Проверяет, что всплывающее окно с полем ввода отображается"""
        self.find_element(AlertsPageLocators.PROMPT_BTN).click()
        alert = self.browser.switch_to.alert
        alert.send_keys(your_name)
        alert.accept()
        self.browser.switch_to.default_content()
        propmt_result = self.find_element(AlertsPageLocators.PROMPT_RESULT)
        assert propmt_result.text == f'You entered {your_name}'
