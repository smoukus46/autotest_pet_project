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

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def element_is_not_displayed(self, locator):
        return self.find(locator).is_not_displayed()

    def items_is_displayed(self, items):
        for item in items:
            return self.is_element_displayed(item)

    def items_is_not_displayed(self, items):
        for item in items:
            return self.element_is_not_displayed(item)

    def button_click(self, button):
        self.find(button).click()

    def elements_menu_items_is_displayed(self):
        return self.items_is_displayed(menu_items)

    def click_menu_elements_button(self, args):
        self.button_click(*args)

    def button_double_click(self):
        action = ActionChains(self.browser)
        action.double_click(ButtonsPageLocators.DOUBLE_CLICK_BTN).perform()

    def button_right_click(self):
        action = ActionChains(self.browser)
        action.context_click(ButtonsPageLocators.RIGHT_CLICK_BTN).perform()

    def fill_selector_by_value(self, locator, value):
        select = Select(self.find(locator))
        select.select_by_value(value)

    def capture_text(self, args):
        return self.find(*args).text
