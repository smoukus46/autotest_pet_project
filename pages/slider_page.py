import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class SliderPageLocators:

    # Кнопка Slider в выпадающем списке Widgets
    SLIDER_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Slider']")

    # Ползунок
    SLIDER_ITEM_INPUT = (By.XPATH, "//input[@class='range-slider range-slider--primary']")

    # Значение ползунка
    SLIDER_ITEM_INPUT_VALUE = (By.ID, "#sliderValue")


class SliderPage(MainPage):

    def click_slider_button(self):
        """Нажимает кнопку "Slider" в выпадающем списке Widgets"""
        return self.find_element(SliderPageLocators.SLIDER_ITEM).click()

    def move_slider_left_or_right(self):
        """Перемещает ползунок влево или вправо"""
        value_before = self.find_element(SliderPageLocators.SLIDER_ITEM_INPUT_VALUE)
        print(value_before.get_attribute("value"))
        element = self.find_element(SliderPageLocators.SLIDER_ITEM_INPUT)
        self.slider_move(element, random.randint(1, 100), 0)
        value_after = self.find_element(SliderPageLocators.SLIDER_ITEM_INPUT_VALUE)
        print(value_after.get_attribute("value"))
