import random
from pages.droppable_page import DroppablePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C43')
def test_droppable(browser):
    """Проверка работы Drop'a"""
    test_droppable = DroppablePage(browser)
    test_droppable.open_main_page()
    test_droppable.click_button_page('interactions_page')
    test_droppable.click_droppable_button()
    simple_text_before, simple_text_after = test_droppable.simple_tab()
    assert simple_text_before != simple_text_after, "Перемещение элемента Drag me в элемент Drop box не прошло"
    accept_text_before, accept_text_after = test_droppable.accept_tab()
    assert accept_text_before == 'Drop here', "Перемещение элементов Not Acceptable не прошло"
    assert accept_text_after == 'Dropped', "Перемещение элементов Acceptable не прошло"
