from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class MainPageLocators:

    # Кнопка Elements
    BUTTON_ELEMENTS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(1)")

    # Кнопка Forms
    BUTTON_FORMS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(2)")

    # Кнопка Alerts, Frame & Windows
    BUTTON_ALERTS_FRAME_WINDOWS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(3)")

    # Кнопка WIDGETS
    BUTTON_WIDGETS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(4)")

    # Кнопка Interactions
    BUTTON_INTERACTIONS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(5)")

    # Кнопка Book Store Application
    BUTTON_BOOK_STORE_APPLICATION = (By.CSS_SELECTOR, ".category-cards > div:nth-child(6)")

class MainPage(BasePage):

    def open_main_page(self):
        """Открывает в браузере главную страницу demoqa"""
        self.open('https://demoqa.com/')

    def click_button_page(self, args):
        """Нажимает кнопку перехода на нужную страницу в главном меню"""
        return self.find_element(args).click()

    def check_tabs_in_main_dropdown(self, args: list):
        """Проверяет отображение позиций выпадающего списка"""
        elements = args
        try:
            for element in elements:
                return self.find_element(element).is_displayed()
        except NoSuchElementException:
            print("Элемент не найден на странице")

    def click_button_widgets_page(self):
        return self.find_element(MainPageLocators.BUTTON_WIDGETS).click()
