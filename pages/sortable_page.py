import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class SortablePageLocators:

    # Кнопка Select Menu в выпадающем списке Widgets
    SORTABLE_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Sortable']")

    # Кнопка вкладки List
    LIST_TAB_BUTTON = (By.ID, "demo-tab-list")

    # Кнопка Grid
    GRID_TAB_BUTTON = (By.ID, "demo-tab-grid")

    # Элементы вкладки List
    ELEMENTS_TAB_LIST = (By.XPATH, "//div[@id='demo-tabpane-list']/div/div")

    # Элементы вкладки Grid
    ELEMENTS_TAB_GRID = (By.XPATH, "//div[@id='demo-tabpane-grid']/div/div/div")

class SortablePage(MainPage):

    def click_sortable_button(self):
        """Нажимает кнопку "Sortable" в выпадающем списке Widgets"""
        return self.find_element(SortablePageLocators.SORTABLE_ITEM).click()

    def get_sortable_items(self, locator):
        """Возвращает список элементов для сортировка"""
        items_list = self.find_elements(locator)
        return [item.text for item in items_list]

    def drag_and_drop_list(self):
        """Перетаскивает элементы на вкладке List"""
        order_before = self.get_sortable_items(SortablePageLocators.ELEMENTS_TAB_LIST)
        item_list = random.sample(self.find_elements(SortablePageLocators.ELEMENTS_TAB_LIST), k=2)
        self.drag_and_drop_elements(item_list[0], item_list[1])
        order_after = self.get_sortable_items(SortablePageLocators.ELEMENTS_TAB_LIST)
        print(order_before)
        print(order_after)
        return order_before, order_after
    
    def drag_and_drop_grid(self):
        """Перетаскивает элементы на вкладке Grid"""
        self.find_element(SortablePageLocators.GRID_TAB_BUTTON).click()
        order_before = self.get_sortable_items(SortablePageLocators.ELEMENTS_TAB_GRID)
        item_list = random.sample(self.find_elements(SortablePageLocators.ELEMENTS_TAB_GRID), k=2)
        self.drag_and_drop_elements(item_list[0], item_list[1])
        order_after = self.get_sortable_items(SortablePageLocators.ELEMENTS_TAB_GRID)
        print(order_before)
        print(order_after)
        return order_before, order_after
