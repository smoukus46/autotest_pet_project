from .locators import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find_element(self, locator, time=10):
        """Ищет один элемент, подходящий по условию"""
        element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def fill_input(self, element_locator, sending_text: str):
        """Заполняет поле"""
        self.find_element(element_locator).send_keys(sending_text)

    def key_enter(self, locator):
        """Нажимает клавишу ENTER"""
        return self.find_element(locator).send_keys(Keys.ENTER)

    def key_delete(self, locator):
        """Нажимает клавишу DELETE"""
        return self.find_element(locator).send_keys(Keys.DELETE)

    def select_value_text(self, locator, value):
        """Выбирает значение из тега select по видимому тексту"""
        select = Select(self.find(locator))
        select.select_by_visible_text(value)
