import random
from pages.dragabble_page import DragabblePage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C44')
def test_dragabble(browser):
    """Проверка работы Drag'а"""
    test_dragabble = DragabblePage(browser)
    test_dragabble.open_main_page()
    test_dragabble.click_button_page('interactions_page')
    test_dragabble.click_dragabble_button()
    text_before, text_after = test_dragabble.simple_tab()
    assert text_before != text_after, "Элемент Drag me не был перемещен"
    only_x_text_before, only_y_text_before, only_x_text_after, only_y_text_after = test_dragabble.axis_restricted_tab()
    assert only_x_text_before != only_x_text_after, "Элемент Only X не был перемещен"
    assert only_y_text_before != only_y_text_after, "Элемент Only Y не был перемещен"
    test_dragabble.container_restricted_tab()
