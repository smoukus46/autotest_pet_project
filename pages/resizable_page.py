import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class ResizablePageLocators:

    # Кнопка Resizable в выпадающем списке Widgets
    RESIZABLE_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Resizable']")

    # Ползунок растягивания первого поля
    FIRST_SLIDER = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span")

    # Ползунок растягивания второго поля
    SECOND_SLIDER = (By.CSS_SELECTOR, "div[id='resizable'] span")

class ResizablePage(MainPage):

    def click_resizable_button(self):
        """Нажимает кнопку "Selectable" в выпадающем списке Widgets"""
        return self.find_element(ResizablePageLocators.RESIZABLE_ITEM).click()
    
    def field_slide_max(self):
        """Растягивает поле на максимум"""
        self.element_stretching(ResizablePageLocators.FIRST_SLIDER, 300, 500)
