from .base_page import BasePage
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

class AutoCompletePage(BasePage):
    
    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_widgets_button(self):
        """Метод открывает выпадающий список Widgets"""
        self.click_menu_elements_button(AccordianPageLocators.WIDGETS_PAGE)

    def widgets_menu_items_is_displayed(self):
        """Метод проверяет отображение элементов выпадающего списка Widgets"""
        return self.items_is_displayed(menu_items)

    def open_auto_complete_tab(self):
        """Метод открывает форму Auto complete"""
        self.button_click(AutoCompletePage.AUTO_COMPLETE_ITEM)

    def filling_field(self, args):
        """Метод заполняет поле Type multiple color names"""
        self.fill_input(AutoCompletePageLocators.MULTIPLE_INPUT, *args)

