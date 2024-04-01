from pages.tool_tips_page import ToolTipsPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C18')
def test_tool_tips(browser):
    """Проверка отображения тултипов на странице"""
    test_tool_tips = ToolTipsPage(browser)
    test_tool_tips.open_main_page()
    test_tool_tips.click_button_widgets_page()
    test_tool_tips.click_tool_tips_button()
    test_tool_tips.check_element_hover('button_hover_me_to_see', 'button_hover')
    test_tool_tips.simple_pause(2)
    test_tool_tips.check_element_hover('field_hover_me_to_see', 'field_hover')
    test_tool_tips.simple_pause(2)
    test_tool_tips.check_element_hover('inscriptions_hovers', 'first_inscription')
    test_tool_tips.simple_pause(2)
    test_tool_tips.check_element_hover('inscriptions_hovers', 'second_inscription')
