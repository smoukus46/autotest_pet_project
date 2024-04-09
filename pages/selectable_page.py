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
    ELEMENTS_TAB_LIST = (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class^='mt-2 list-group-item list-group-item-action']")

    # Выбранные элементы вкладки List
    ELEMENTS_TAB_LIST_ACTIVE = (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class^='mt-2 list-group-item active list-group-item-action']")

    # Элементы вкладки Grid
    ELEMENTS_TAB_GRID = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class^='list-group-item list-group-item-action']")

    # Выбранные элементы вкладки Grid
    ELEMENTS_TAB_GRID_ACTIVE = (By.CSS_SELECTOR, "div[id='gridContainer'] li[class^='list-group-item active list-group-item-action']")

class SelectablePage(MainPage):

    def click_selectable_button(self):
        """Нажимает кнопку "Selectable" в выпадающем списке Widgets"""
        return self.find_element(SelectablePageLocators.SELECTABLE_ITEM).click()

    def get_selectable_items(self, locator):
        """Возвращает список элементов для выбора"""
        items_list = self.find_elements(locator)
        return [item.text for item in items_list]

    def select_random_element_list(self):
        """Выбирает элементы на вкладке List"""
        no_active_elements = self.get_selectable_items(SelectablePageLocators.ELEMENTS_TAB_LIST)
        item_list = random.sample(self.find_elements(SelectablePageLocators.ELEMENTS_TAB_LIST), k=random.randint(1, 4))
        for item in item_list:
            item.click()
        active_elements = self.get_selectable_items(SelectablePageLocators.ELEMENTS_TAB_LIST_ACTIVE)
        print(no_active_elements)
        print(active_elements)
        return no_active_elements, active_elements

    def select_random_element_grid(self):
        """Выбирает элементы на вкладке List"""
        self.find_element(SelectablePageLocators.GRID_TAB_BUTTON).click()
        no_active_elements = self.get_selectable_items(SelectablePageLocators.ELEMENTS_TAB_GRID)
        item_list = random.sample(self.find_elements(SelectablePageLocators.ELEMENTS_TAB_GRID), k=random.randint(1, 9))
        for item in item_list:
            item.click()
        active_elements = self.get_selectable_items(SelectablePageLocators.ELEMENTS_TAB_GRID_ACTIVE)
        print(no_active_elements)
        print(active_elements)
        return no_active_elements, active_elements
