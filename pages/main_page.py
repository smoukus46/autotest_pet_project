from selenium.webdriver.common.by import By
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

    def click_button_page(self, args):
        """Нажимает кнопку перехода на нужную страницу в главном меню"""
        return self.find_element(args).click()
