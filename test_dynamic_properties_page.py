import time
from .pages.dynamic_properties import DynamicProperties
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C37')
def check_dynamic_properties(browser):
    dynamic_properties_page = DynamicProperties(browser)
    dynamic_properties_page.open_main_page()
    dynamic_properties_page.click_menu_elements_button()
    dynamic_properties_page.elements_menu_items_is_displayed()
    dynamic_properties_page.open_dynamic_properties_tab()
    dynamic_properties_page.will_enable_button_is_disabled()
    dynamic_properties_page.visible_after_five_seconds_button_is_not_displayed()
    dynamic_properties_page.color_changing_button_white()
    time.sleep(6)
    assert 'None' == dynamic_properties_page.will_enable_button_is_disabled()
    dynamic_properties_page.color_changing_button_red()
    dynamic_properties_page.visible_after_five_seconds_button_is_displayed()
