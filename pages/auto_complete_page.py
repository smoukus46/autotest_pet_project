from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from pages.main_page import MainPage
from generator.generator import Colors


class AutoCompleteLocators:

    # Кнопка Auto Complete в выпадающем списке Widgets
    AUTO_COMPLETE_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Auto Complete']")

    # Поле multiple
    MULTIPLE_INPUT = (By.ID, "autoCompleteMultipleInput")

    # Кнопка очистки поля multiple
    MULTIPLE_INPUT_REMOVE_BTN = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")

    # Поле single
    SINGLE_INPUT = (By.ID, "autoCompleteSingleInput")



class AutoCompletePage(MainPage):

    def click_widgets_button(self):
        """Нажимает кнопку "Widgets" в главном меню"""
        return self.click_button_page(MainPageLocators.BUTTON_WIDGETS)

    def click_auto_complete_button(self):
        """Нажимает кнопку "Auto complete" в выпадающем списке Widgets"""
        return self.find_element(AutoCompleteLocators.AUTO_COMPLETE_ITEM).click()

    def fill_input_multiple(self):
        """Заполняет поле multiple рандомным значением"""
        color = Colors()
        return self.fill_input(AutoCompleteLocators.MULTIPLE_INPUT, f"{color.colors}")

    def key_enter_multiple(self):
        """Нажимает клавишу "Enter" для выбора 1 значения из выпадающего списка в поле multiple"""
        return self.key_enter(AutoCompleteLocators.MULTIPLE_INPUT)

    def key_del_multiple(self):
        """Нажимает клавишу "DEL" в поле multiple"""
        return self.key_delete(AutoCompleteLocators.MULTIPLE_INPUT)

    def delete_all_values_in_multiple(self):
        """Очищает поле multiple"""
        return self.find_element(AutoCompleteLocators.MULTIPLE_INPUT_REMOVE_BTN).click()

    def fill_input_single(self):
        """Заполняет поле single рандомным значением"""
        color = Colors()
        return self.fill_input(AutoCompleteLocators.SINGLE_INPUT, f"{color.colors}")

    def key_enter_single(self):
        """Нажимает клавишу "Enter" для выбора 1 значения из выпадающего списка в поле single"""
        return self.key_enter(AutoCompleteLocators.SINGLE_INPUT)
