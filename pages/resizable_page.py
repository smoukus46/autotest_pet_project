import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class ResizablePageLocators:

    # Кнопка Resizable в выпадающем списке Interactions
    RESIZABLE_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Resizable']")

    # Контейнер первого растягиваемого поля
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")

    # Ползунок растягивания первого поля
    FIRST_SLIDER = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span")

    # Контейнер второго растягиваемого поля
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")

    # Ползунок растягивания второго поля
    SECOND_SLIDER = (By.CSS_SELECTOR, "div[id='resizable'] span")

class ResizablePage(MainPage):

    fields = {
        'first': [ResizablePageLocators.RESIZABLE_BOX, ResizablePageLocators.FIRST_SLIDER],
        'second': [ResizablePageLocators.RESIZABLE, ResizablePageLocators.SECOND_SLIDER]
    }

    def click_resizable_button(self):
        """Нажимает кнопку "Resizable" в выпадающем списке Interactions"""
        return self.find_element(ResizablePageLocators.RESIZABLE_ITEM).click()
    
    def field_slide(self, number, x: int, y: int):
        """Растягивает поле"""
        size_before = self.find_element(self.fields[number][0]).get_attribute('style')
        self.element_stretching((self.find_element(self.fields[number][1])), x, y)
        size_after = self.find_element(self.fields[number][0]).get_attribute('style')
        print(f'Размер поля до: {size_before}')
        print(f'Размер поля после: {size_after}')
        return size_before, size_after
