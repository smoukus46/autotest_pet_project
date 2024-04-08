import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class SelectablePageLocators:

    # Кнопка Selectable в выпадающем списке Widgets
    SELECTABLE_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Selectable']")

    # Кнопка вкладки List
    LIST_TAB_BUTTON = (By.XPATH, "//a[@id='demo-tab-list']")

    # Кнопка Grid
    GRID_TAB_BUTTON = (By.XPATH, "//a[@id='demo-tab-grid']")

    # Элементы вкладки List
    ELEMENTS_TAB_LIST = (By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action']")

    # Элементы вкладки Grid
    ELEMENTS_TAB_GRID = (By.XPATH, "//li[@class='list-group-item list-group-item-action']")

class SelectablePage(MainPage):

    def click_selectable_button(self):
        """Нажимает кнопку "Selectable" в выпадающем списке Widgets"""
        return self.find_element(SelectablePageLocators.SELECTABLE_ITEM).click()

    def get_selectable_items(self, locator):
        """Возвращает список элементов для выбора"""
        items_list = self.find_elements(locator)
        return [item.text for item in items_list]

    def select_random_element(self):
        """Выбирает элементы на вкладке List"""
        item_list = random.sample(self.find_elements(SelectablePageLocators.ELEMENTS_TAB_LIST), k=random.randint(4, 7))
        for item in item_list:
            self.find_element(item).click()
