from selenium.webdriver.chrome.webdriver import WebDriver
from pages.accordian_page import AccordianPage, AccordianPageLocators
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C12')
def test_folding_and_unfolding_details(browser: WebDriver):
    """Проверка разворачивания и сворачивания деталей на странице"""
    test_accordian_page = AccordianPage(browser)
    test_accordian_page.open_main_page()
    test_accordian_page.click_widgets_button()
    test_accordian_page.check_elements_widgets_dropdown()
    test_accordian_page.click_accordian_button()
    test_accordian_page.click_button_section(AccordianPageLocators.FIRST_SECTION_HEADING)
    test_accordian_page.body_is_present(AccordianPageLocators.FIRST_SECTION_BODY)
    test_accordian_page.click_accordian_button(AccordianPageLocators.SECOND_SECTION_HEADING)
    test_accordian_page.body_is_not_present(AccordianPageLocators.FIRST_SECTION_BODY)
    test_accordian_page.body_is_present(AccordianPageLocators.SECOND_SECTION_BODY)
    test_accordian_page.click_button_section(AccordianPageLocators.THIRD_SECTION_HEADING)
    test_accordian_page.body_is_not_present(AccordianPageLocators.SECOND_SECTION_BODY)
    test_accordian_page.body_is_present(AccordianPageLocators.THIRD_SECTION_BODY)
