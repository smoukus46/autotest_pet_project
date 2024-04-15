import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class DroppablePageLocators:

    # Кнопка Droppable в выпадающем списке Interactions
    DROPPABLE_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Droppable']")

    # Кнопка вкладки Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")

    # Элемент Drage me вкладки Simple
    SIMPLE_TAB_DRAG_ME = (By.XPATH, "//div[@class='simple-drop-container']/div[1]")

    # Элемент Drop box вкладки Simple
    SIMPLE_TAB_DROP_BOX = (By.XPATH, "//div[@class='simple-drop-container']/div[2]")
    
    # Текст элемента drop box вкладки Simple
    SIMPLE_TAB_DROP_BOX_TEXT = (By.XPATH, "//div[@class='simple-drop-container']/div[2]/p")

    # Кнопка вкладки Accept
    ACCEPT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-accept']")

    # Элемент Acceptable вкладки Accept
    ACCEPT_TAB_ACCEPTABLE = (By.XPATH, "//div[@class='accept-drop-container']/div[1]/div[1]")

    # Элемент Not Acceptable вкладки Accept
    ACCEPT_TAB_NOT_ACCEPTABLE = (By.XPATH, "//div[@class='accept-drop-container']/div[1]/div[2]")

    # Элемент Drop box вкладки Accept
    ACCEPT_TAB_DROP_BOX = (By.XPATH, "//div[@class='accept-drop-container']/div[2]")

    # Текст элемента drop box вкладки Accept
    ACCEPT_TAB_DROP_BOX_TEXT = (By.XPATH, "//div[@class='accept-drop-container']/div[2]/p")


class DroppablePage(MainPage):

    def click_droppable_button(self):
        """Нажимает кнопку "Droppable" в выпадающем списке Interactions"""
        return self.find_element(DroppablePageLocators.DROPPABLE_ITEM).click()
    
    def simple_tab(self):
        """Перемещает элемент Drag me в элемент Drop box"""
        self.find_element(DroppablePageLocators.SIMPLE_TAB).click()
        text_before = self.find_element(DroppablePageLocators.SIMPLE_TAB_DROP_BOX_TEXT).text
        drag_me = self.find_element(DroppablePageLocators.SIMPLE_TAB_DRAG_ME)
        drop_here = self.find_element(DroppablePageLocators.SIMPLE_TAB_DROP_BOX)
        self.drag_and_drop_elements(drag_me, drop_here)
        text_after = self.find_element(DroppablePageLocators.SIMPLE_TAB_DROP_BOX_TEXT).text
        print(text_before)
        print(text_after)
        return text_before, text_after
    
    def accept_tab(self):
        """Перемещает элементы Acceptable и Not Acceptable на вкладке Accept"""
        self.find_element(DroppablePageLocators.ACCEPT_TAB).click()
        not_acceptable = self.find_element(DroppablePageLocators.ACCEPT_TAB_NOT_ACCEPTABLE)
        acceptable = self.find_element(DroppablePageLocators.ACCEPT_TAB_ACCEPTABLE)
        drop_box = self.find_element(DroppablePageLocators.ACCEPT_TAB_DROP_BOX)
        self.drag_and_drop_elements(not_acceptable, drop_box)
        text_before = self.find_element(DroppablePageLocators.ACCEPT_TAB_DROP_BOX_TEXT).text
        self.drag_and_drop_elements(acceptable, drop_box)
        text_after = self.find_element(DroppablePageLocators.ACCEPT_TAB_DROP_BOX_TEXT).text
        print(text_before)
        print(text_after)
        return text_before, text_after
