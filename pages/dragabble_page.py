import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class DragabblePageLocators:

    # Кнопка Dragabble в выпадающем списке Interactions
    DRAGGABLE_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Dragabble']")

    # Кнопка вкладки Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='draggableExample-tab-simple']")

    # Элемент Drag me вкладки Simple
    SIMPLE_TAB_DRAG_ME = (By.XPATH, "//div[@id='draggableExample-tabpane-simple']/div")

    # Кнопка вкладки Axis Restricted
    AXIS_RESTRICTED_TAB = (By.XPATH, "//a[@id='draggableExample-tab-axisRestriction']")

    # Элемент Only X вкладки Axis Restricted
    ONLY_X_AXIS_RESTRICTED = (By.XPATH, "//div[@class='axis-restriction-container mt-4']/div[1]")

    # Элемент Only X вкладки Axis Restricted
    ONLY_Y_AXIS_RESTRICTED = (By.XPATH, "//div[@class='axis-restriction-container mt-4']/div[2]")

    # Кнопка вкладки Container Restricted
    CONTAINER_RESTRICTED_TAB = (By.XPATH, "//a[@id='draggableExample-tab-containerRestriction']")

    # Элемент I'm contained within the box вкладки Container Restricted
    FIRST_DRAG_ME = (By.XPATH, "//div[@id='containmentWrapper']/div")

    # Элемент I'm contained within my parent вкладки Container Restricted
    SECOND_DRAG_ME = (By.XPATH, "//div[@class='draggable ui-widget-content m-3']/span")


class DragabblePage(MainPage):

    def click_dragabble_button(self):
        """Нажимает кнопку "Droppable" в выпадающем списке Interactions"""
        return self.find_element(DragabblePageLocators.DRAGGABLE_ITEM).click()
    
    def simple_tab(self):
        """Перемещает элемент Drag me на вкладке Simple в рандомное положение"""
        self.find_element(DragabblePageLocators.SIMPLE_TAB).click()
        drag_me = self.find_element(DragabblePageLocators.SIMPLE_TAB_DRAG_ME)
        text_before = self.find_element(DragabblePageLocators.SIMPLE_TAB_DRAG_ME).get_attribute('style')
        self.element_stretching(drag_me, random.randint(50, 150), random.randint(50, 150))
        text_after = self.find_element(DragabblePageLocators.SIMPLE_TAB_DRAG_ME).get_attribute('style')
        print(text_before, text_after)
        return text_before, text_after

    def axis_restricted_tab(self):
        """Перемещает элемент Only X и Only Y на вкладке Axis Restricted в рандомное положение"""
        self.find_element(DragabblePageLocators.AXIS_RESTRICTED_TAB).click()
        only_x = self.find_element(DragabblePageLocators.ONLY_X_AXIS_RESTRICTED)
        only_y = self.find_element(DragabblePageLocators.ONLY_Y_AXIS_RESTRICTED)
        only_x_text_before = self.find_element(DragabblePageLocators.ONLY_X_AXIS_RESTRICTED).get_attribute('style')
        only_y_text_before = self.find_element(DragabblePageLocators.ONLY_Y_AXIS_RESTRICTED).get_attribute('style')
        self.element_stretching(only_x, random.randint(50, 150), 0)
        self.element_stretching(only_y, 0, random.randint(50, 150))
        only_x_text_after = self.find_element(DragabblePageLocators.ONLY_X_AXIS_RESTRICTED).get_attribute('style')
        only_y_text_after = self.find_element(DragabblePageLocators.ONLY_Y_AXIS_RESTRICTED).get_attribute('style')
        print(only_x_text_before, only_y_text_before)
        print(only_x_text_after, only_y_text_after)
        return only_x_text_before, only_y_text_before, only_x_text_after, only_y_text_after
    
    def container_restricted_tab(self):
        """Перемещает элементы I'm contained within the box и I'm contained within my parent на вкладке Container Restricted в рандомное положение внутри контейнеров"""
        self.find_element(DragabblePageLocators.CONTAINER_RESTRICTED_TAB).click()
        first_drag_me = self.find_element(DragabblePageLocators.FIRST_DRAG_ME)
        second_drag_me = self.find_element(DragabblePageLocators.SECOND_DRAG_ME)
        self.element_stretching(first_drag_me, 500, 200)
        self.element_stretching(second_drag_me, 20, 100)
