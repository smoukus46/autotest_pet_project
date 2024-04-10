from pages.resizable_page import ResizablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C42')
def test_resizable(browser):
    """Проверка возможности изменения размера поля посредством растягивания поля"""
    test_resizable = ResizablePage(browser)
    test_resizable.open_main_page()
    test_resizable.click_button_page('interactions_page')
    test_resizable.click_resizable_button()
    test_resizable.field_slide_max()
    test_resizable.simple_pause(3)