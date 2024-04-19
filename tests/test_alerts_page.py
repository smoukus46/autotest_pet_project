from pages.alerts_page import AlertsPage
from pytest_testrail.plugin import pytestrail
from pages.locators import *


@pytestrail.case('C10')
def test_check_alerts(browser):
    """Проверка отработки различных типов всплывающих уведомлений"""
    alerts_page = AlertsPage(browser)
    alerts_page.open_main_page()
    alerts_page.click_alerts_page_button()
    alerts_page.alerts_menu_items_is_displayed()
    alerts_page.open_alerts_tab()
    alerts_page.check_alert_is_visible(AlertsPageLocators.ALERT_BTN, 0, 'You clicked a button')
    alerts_page.check_alert_is_visible(AlertsPageLocators.TIMER_ALERT_BTN, 5, 'This alert appeared after 5 seconds')
    alerts_page.check_confirm_alert()
    alerts_page.check_propmt_alert('Artem')
