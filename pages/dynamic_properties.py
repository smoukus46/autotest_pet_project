from .base_page import BasePage
from .locators import *


class DynamicProperties(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_dynamic_properties_tab(self):
        self.button_click(DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM)

    def will_enable_button_is_disabled(self):
        self.find(DynamicPropertiesPageLocators.WILL_ENABLE_BTN).get_attribute('disabled')

    def visible_after_five_seconds_button_is_not_displayed(self):
        self.element_is_not_displayed(DynamicPropertiesPageLocators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)

    def color_changing_button_white(self):
        color = self.find(DynamicPropertiesPageLocators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        assert color == '#fff'

    def color_changing_button_red(self):
        color = self.find(DynamicPropertiesPageLocators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        assert color == 'dc3545'

    def visible_after_five_seconds_button_is_displayed(self):
        self.is_element_displayed(DynamicPropertiesPageLocators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)
