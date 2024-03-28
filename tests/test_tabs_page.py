from pages.tabs_page import TabsPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C14')
def test_tabs(browser):
    """Проверка работы ползунка"""
    test_tabs = TabsPage(browser)
    test_tabs.open_main_page()
    test_tabs.click_button_widgets_page()
    test_tabs.click_tab_button()
    test_tabs.click_and_check_tab('tab_what', 'what_button')
    text_in_tab_what = test_tabs.check_content_tab('tab_what', 'what_content')
    assert len(text_in_tab_what) == 574, "Содержимое пустое"
    test_tabs.simple_pause(2)
    test_tabs.click_and_check_tab('tab_origin', 'origin_button')
    test_tabs.simple_pause(2)
    test_tabs.click_and_check_tab('tab_use', 'use_button')
    text_in_tab_use = test_tabs.check_content_tab('tab_use', 'use_content')
    assert len(text_in_tab_use) == 613, "Содержимое пустое"
    test_tabs.simple_pause(2)
    assert test_tabs.check_not_clickable_tab('more_button') == False, "Кнопка кликабельна"
