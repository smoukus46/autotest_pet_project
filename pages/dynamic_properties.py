from .main_page import MainPage
from .locators import *


class DynamicPropertiesPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_dynamic_properties_tab(self):
        """Открывает вкладку динамических настроек"""
        self.find_element(DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM).click()

    def will_enable_button_is_disabled(self):
        """Проверяет кнопку на заблокированность"""
        self.find_element(DynamicPropertiesPageLocators.WILL_ENABLE_BTN).get_attribute('disabled')

    def visible_after_five_seconds_button_is_not_displayed(self):
        """Проверяет отсуствие кнопки на странице до истечения пяти секунд"""
        self.element_is_invisible(DynamicPropertiesPageLocators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)

    def color_changing_button_white(self):
        """Проверяет кнопку с изменяющимся цветом текста на белый цвет"""
        color = self.find_element(DynamicPropertiesPageLocators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        print(color)
        assert color == 'rgba(255, 255, 255, 1)', 'Цвет не соответствует ожидаемому'

    def color_changing_button_red(self):
        """Проверяет кнопку с изменяющимся цветом текста на смену цвет на красный"""
        color = self.find_element(DynamicPropertiesPageLocators.COLOR_CHANGE_BUTTON).value_of_css_property('color')
        assert color == 'rgba(220, 53, 69, 1)', 'Цвет не соответствует ожидаемому'

    def visible_after_five_seconds_button_is_displayed(self):
        """Проверяет отображение кнопки на странице после истечения пяти секунд"""
        self.element_is_visible(DynamicPropertiesPageLocators.VISIBLE_AFTER_FIVE_SECONDS_BUTTON)
