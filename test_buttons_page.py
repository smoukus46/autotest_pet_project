from .pages.buttons_page import ButtonsPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C32')
def test_fill_forms_on_text_box_page(browser):
    test_buttons_page = ButtonsPage(browser)
    test_buttons_page.open_main_page()
    test_buttons_page.click_menu_elements_button()
    test_buttons_page.elements_menu_items_is_displayed()
    test_buttons_page.open_buttons_tab()
    test_buttons_page.button_double_click()
    test_buttons_page.button_right_click()
    test_buttons_page.click_dynamic_button()
    test_buttons_page.double_click_message_is_displayed()
    test_buttons_page.right_click_message_is_displayed()
    test_buttons_page.dynamic_click_message_is_displayed()
