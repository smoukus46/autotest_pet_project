from pages.accordian_page import AccordianPage, AccordianPageLocators
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C12')
def test_folding_and_unfolding_details(browser):
    """Проверка разворачивания и сворачивания деталей на странице"""
    test_accordian_page = AccordianPage(browser)
    test_accordian_page.open_main_page()
    test_accordian_page.click_widgets_button()
    test_accordian_page.click_accordian_button()
    test_accordian_page.click_button_first_section()
    test_accordian_page.first_body_is_present()
    test_accordian_page.click_button_second_section()
    test_accordian_page.second_body_is_present()
    test_accordian_page.first_body_is_not_present()
    test_accordian_page.click_button_third_section()
    test_accordian_page.third_body_is_present()
    test_accordian_page.second_body_is_not_present()
