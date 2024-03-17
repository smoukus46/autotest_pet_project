from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import *

menu_items = [AccordianPageLocators.ACCORDIAN_ITEM, 
              AutoCompletePageLocators.AUTO_COMPLETE_ITEM, 
              DatePickerPageLocators.DATE_PICKER_ITEM, 
              SliderPageLocators.SLIDER_ITEM, 
              ProgressBarPageLocators.PROGRESS_BAR_ITEM, 
              TabsPageLocators.TABS_ITEM, 
              ToolTipsPageLocators.TOOL_TIPS_ITEM, 
              MenuPageLocators.MENU_ITEM, 
              SelectMenuPageLocators.SELECT_MENU_ITEM]

class AccordianPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_widgets_button(self):
        """Метод раскрывает выпадающий список Widgets"""
        self.click_menu_elements_button(AccordianPageLocators.WIDGETS_PAGE)

    def widgets_menu_items_is_displayed(self):
        """Метод проверяет отображение элементов выпадающего списка Widgets"""
        return self.items_is_displayed(menu_items)

    def open_accordian_tab(self):
        """Метод открывает форму Accordian"""
        self.button_click(AccordianPageLocators.ACCORDIAN_ITEM)

    def disclosure_section(self, args):
        """Метод раскрывает деталь"""
        self.button_click(*args)

    def section_is_displayed(self, args):
        """Метод проверяет отображение раскрытой детали"""
        try:
            return self.is_element_displayed(*args)
        except NoSuchElementException:
            return False

    def section_is_not_displayed(self, args):
        """Метод проверяет скрытие предыдущей детали"""
        try:
            return self.items_is_not_displayed(*args)
        except NoSuchElementException:
            return False

    def section_text(self, args):
        """Метод проверяет текст внутри тела детали"""
        return self.capture_text(*args)
