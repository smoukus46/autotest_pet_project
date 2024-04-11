import random
from pages.resizable_page import ResizablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C42')
def test_resizable(browser):
    """Проверка возможности изменения размера поля посредством растягивания поля"""
    test_resizable = ResizablePage(browser)
    test_resizable.open_main_page()
    test_resizable.click_button_page('interactions_page')
    test_resizable.click_resizable_button()
    test_resizable.field_slide('first', 0, 1, random.randint(150, 500), random.randint(150, 300))
    test_resizable.simple_pause(1)
    test_resizable.field_slide('second', 0, 1, random.randint(20, 300), random.randint(20, 300))
    test_resizable.simple_pause(1)
