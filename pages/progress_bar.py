import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class ProgressBarLocators:

    # Кнопка Progress Bar в выпадающем списке Widgets
    PROGRESS_BAR_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Progress Bar']")

    # Кнопка Start, Stop, Reset
    START_STOP_RESET_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")

    # Прогресс бар
    PROGRESS_BAR_INFO = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

class ProgressBarPage(MainPage):

    def click_progress_bar_button(self):
        """Нажимает кнопку "Progress Bar" в выпадающем списке Widgets"""
        return self.find_element(ProgressBarLocators.PROGRESS_BAR_ITEM).click()

    def click_start_stop_reset_button(self):
        """Нажимает кнопку start/stop/reset"""
        self.find_element(ProgressBarLocators.START_STOP_RESET_BUTTON).click()
        self.simple_pause(random.randint(2, 7))
        self.find_element(ProgressBarLocators.START_STOP_RESET_BUTTON).click()
