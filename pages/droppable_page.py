import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class DroppablePageLocators:

    # Кнопка Droppable в выпадающем списке Interactions
    DROPPABLE_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Droppable']")

    # Кнопка вкладки Simple
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")

    # Элемент Drag me вкладки Simple
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

    # Кнопка вкладки Prevent Propogation
    PREVENT_PROPOGATION_TAB = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")

    # Элемент Drag me вкладки Prevent Propogation
    PREVENT_PROPOGATION_DRAG_ME = (By.XPATH, "//div[@class='drag-box mt-4 ui-draggable ui-draggable-handle' and @id='dragBox']")

    # Элемент Not greedy inner вкладки Prevent Propogation
    NOT_GREEDY_INNER_DROP_BOX = (By.XPATH, "//div[@id='notGreedyDropBox']/div/p")

    # Элемент Not greedy outer вкладки Prevent Propogation
    NOT_GREEDY_OUTER_DROP_BOX = (By.XPATH, "//div[@id='notGreedyDropBox']/p")

    # Элемент Greedy inner вкладки Prevent Propogation
    GREEDY_INNER_DROP_BOX = (By.XPATH, "//div[@id='greedyDropBoxInner']/p")

    # Элемент Greedy outer вкладки Prevent Propogation
    GREEDY_OUTER_DROP_BOX = (By.XPATH, "//div[@id='greedyDropBox']/p")

    # Кнопка вкладки Revert Draggable
    REVERT_DRAGGABLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-revertable']")

    # Элемент Will Revert вкладки Revert Draggable
    REVERT_DRAGGABLE_WILL_REVERT = (By.XPATH, "//div[@id='revertable']")

    # Элемент Not Revert вкладки Revert Draggable
    REVERT_DRAGGABLE_NOT_REVERT = (By.XPATH, "//div[@id='notRevertable']")

    # Элемент Drop box вкладки Revert Draggable
    REVERT_DRAGGABLE_DROP_BOX = (By.XPATH, "//div[@class='revertable-drop-container']/div[2]")

    # Текст элемент Drop box вкладки Revert Draggable
    REVERT_DRAGGABLE_DROP_BOX_TEXT = (By.XPATH, "//div[@class='revertable-drop-container']/div[2]/p")

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

    def prevent_propogation_tab(self):
        """Перемещает элемент Drag me в inner и outer боксы"""
        self.find_element(DroppablePageLocators.PREVENT_PROPOGATION_TAB).click()
        drag_me = self.find_element(DroppablePageLocators.PREVENT_PROPOGATION_DRAG_ME)
        inner_not_greedy_drop_box = self.find_element(DroppablePageLocators.NOT_GREEDY_INNER_DROP_BOX)
        inner_greedy_drop_box = self.find_element(DroppablePageLocators.GREEDY_INNER_DROP_BOX)
        outer_greedy_drop_box = self.find_element(DroppablePageLocators.GREEDY_OUTER_DROP_BOX)
        outer_not_greedy_text_before = self.find_element(DroppablePageLocators.NOT_GREEDY_OUTER_DROP_BOX).text
        inner_not_greedy_text_before = self.find_element(DroppablePageLocators.NOT_GREEDY_INNER_DROP_BOX).text
        self.drag_and_drop_elements(drag_me, inner_not_greedy_drop_box)
        outer_not_greedy_text_after = self.find_element(DroppablePageLocators.NOT_GREEDY_OUTER_DROP_BOX).text
        inner_not_greedy_text_after = self.find_element(DroppablePageLocators.NOT_GREEDY_INNER_DROP_BOX).text
        inner_greedy_text_before = self.find_element(DroppablePageLocators.GREEDY_INNER_DROP_BOX).text
        self.drag_and_drop_elements(drag_me, inner_greedy_drop_box)
        inner_greedy_text_after = self.find_element(DroppablePageLocators.GREEDY_INNER_DROP_BOX).text
        outer_greedy_text_before = self.find_element(DroppablePageLocators.GREEDY_OUTER_DROP_BOX).text
        self.drag_and_drop_elements(drag_me, outer_greedy_drop_box)
        outer_greedy_text_after = self.find_element(DroppablePageLocators.GREEDY_OUTER_DROP_BOX).text
        print(outer_not_greedy_text_before, inner_not_greedy_text_before)
        print(outer_not_greedy_text_after, inner_not_greedy_text_after)
        print(inner_greedy_text_before, inner_greedy_text_after)
        print(outer_greedy_text_before, outer_greedy_text_after)
        return outer_not_greedy_text_before, inner_not_greedy_text_before, outer_not_greedy_text_after, inner_not_greedy_text_after, inner_greedy_text_before, inner_greedy_text_after, outer_greedy_text_before, outer_greedy_text_after

    def revert_draggable_tab(self):
        """Перемещает элементы Will Revert и Not Revert в drop box"""
        self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_TAB).click()
        will_revert = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_WILL_REVERT)
        not_revert = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_NOT_REVERT)
        drop_box = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_DROP_BOX)
        text_before = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_DROP_BOX_TEXT).text
        self.drag_and_drop_elements(not_revert, drop_box)
        text_after = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_DROP_BOX_TEXT).text
        not_revert_position_before = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_NOT_REVERT).get_attribute('style')
        self.drag_and_drop_elements(not_revert, will_revert)
        not_revert_position_after = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_NOT_REVERT).get_attribute('style')
        will_revert_position_before = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_WILL_REVERT).get_attribute('style')
        self.drag_and_drop_elements(will_revert, drop_box)
        will_revert_position_after = self.find_element(DroppablePageLocators.REVERT_DRAGGABLE_WILL_REVERT).get_attribute('style')
        print(text_before, text_after)
        print(not_revert_position_before, not_revert_position_after)
        print(will_revert_position_before, will_revert_position_after)
        return text_before, text_after, not_revert_position_before, not_revert_position_after, will_revert_position_before, will_revert_position_after
