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
    assert accept_text_after == 'Dropped!', "Перемещение элементов Acceptable не прошло"
    outer_not_greedy_text_before, inner_not_greedy_text_before, outer_not_greedy_text_after, inner_not_greedy_text_after, inner_greedy_text_before, inner_greedy_text_after, outer_greedy_text_before, outer_greedy_text_after = test_droppable.prevent_propogation_tab()
    assert outer_not_greedy_text_before != outer_not_greedy_text_after, "Перемещение элемента Drag me в элемент Drop box не прошло"
    assert inner_not_greedy_text_before != inner_not_greedy_text_after, "Перемещение элемента Drag me в элемент Drop box не прошло"
    assert inner_greedy_text_before != inner_greedy_text_after, "Перемещение элемента Drag me в элемент Drop box не прошло"
    assert outer_greedy_text_before != outer_greedy_text_after, "Перемещение элемента Drag me в элемент Drop box не прошло"
    text_before, text_after, not_revert_position_before, not_revert_position_after, will_revert_position_before, will_revert_position_after = test_droppable.revert_draggable_tab()
    assert text_before != text_after, "Перемещение элемента Not Revert в элемент Drop box не прошло"
    assert not_revert_position_before != not_revert_position_after, "Элемент Not Revert не вернулся в Drop Box"
    assert will_revert_position_before != will_revert_position_after, "Элемент Will Revert не вернулся в исходное положение"
