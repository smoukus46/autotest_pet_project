from .pages.radio_button_page import RadioButtonPage
from pytest_testrail.plugin import pytestrail
from .pages.locators import *


@pytestrail.case('C24')
def test_check_selecting_radio_button(browser):
    radio_button_page = RadioButtonPage(browser)
    radio_button_page.open_main_page()
    radio_button_page.click_menu_elements_button()
    radio_button_page.elements_menu_items_is_displayed()
    radio_button_page.click_yes_radio_button()
    assert "Yes" == radio_button_page.find(RadioBtnPageLocators.RESULT_TEXT).text
    radio_button_page.click_impressive_radio_button()
    assert "Impressive" == radio_button_page.find(RadioBtnPageLocators.RESULT_TEXT).text
    radio_button_page.no_button_is_displayed()
