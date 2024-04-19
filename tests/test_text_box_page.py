from pages.text_box_page import TextBoxPage
from pytest_testrail.plugin import pytestrail
from pages.locators import *


@pytestrail.case('C7')
def test_fill_forms_on_text_box_page(browser):
    """Проверка возможности заполнения формы "Text box"""
    text_box_page = TextBoxPage(browser)
    text_box_page.open_main_page()
    text_box_page.click_menu_elements_button()
    text_box_page.elements_menu_items_is_displayed()
    text_box_page.open_text_box_tab()
    text_box_page.inputs_is_displayed()
    text_box_page.fill_name_input()
    text_box_page.fill_email_input()
    text_box_page.fill_current_address()
    text_box_page.fill_permanent_address()
    text_box_page.click_submit_button()
    assert ('Name:Artem.Alenin' ==
            text_box_page.find_element(TextBoxPageLocators.NAME_OUTPUT).text), 'Текст не соотвествует передаваемому'
    assert ('Email:Artem.Alenin@test.ru' ==
            text_box_page.find_element(TextBoxPageLocators.EMAIL_OUTPUT).text), 'Текст не соотвествует передаваемому'
    assert ('Current Address :City of Kursk' == text_box_page.find_element(TextBoxPageLocators.CURRENT_ADDRESS_OUTPUT).text), 'Текст не соотвествует передаваемому'
    assert ('Permananet Address :Kosinovo village' == text_box_page.find_element(TextBoxPageLocators.PERMANENT_ADDRESS_OUTPUT).text), 'Текст не соотвествует передаваемому'
