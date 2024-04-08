import time
from .locators import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        """Открывает страницу по переданному урлу"""
        self.browser.get(url)

    def find_element(self, locator, _time=20):
        """Ищет один элемент, подходящий по условию"""
        element = WebDriverWait(self.browser, _time).until(EC.visibility_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    def find_elements(self, locator, _time=20):
        """Ищет все элементы, подходящие по условию"""
        return WebDriverWait(self.browser, _time).until(EC.visibility_of_all_elements_located(locator))

    def fill_input(self, element_locator, sending_text: str):
        """Заполняет поле"""
        self.find_element(element_locator).send_keys(sending_text)

    def key_enter(self, locator):
        """Нажимает клавишу ENTER"""
        return self.find_element(locator).send_keys(Keys.ENTER)

    def key_delete(self, locator):
        """Нажимает клавишу DELETE"""
        return self.find_element(locator).send_keys(Keys.DELETE)

    def key_backspace(self, locator):
        """Нажимает клавишу DELETE"""
        return self.find_element(locator).send_keys(Keys.BACKSPACE)

    def select_value_text(self, locator, value):
        """Выбирает значение из тега select по видимому тексту"""
        select = Select(self.find_element(locator))
        select.select_by_visible_text(value)

    def get_attribute_element(self, locator, attribute="value"):
        """Берет значение у атрибута элемента"""
        element = self.find_element(locator)
        value = element.get_attribute(attribute)
        return value

    def simple_pause(self, _time):
        """Пауза, необходимо в метод передавать число секунд, которое нужно ожидать"""
        return time.sleep(_time)

    def slider_move(self, locator, x, y):
        """Удерживает элемент ЛКМ и перетягивает его влево или вправо"""
        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(locator, x, y)
        actions.perform()

    def element_not_be_clickable(self, locator, time=3):
        """Проверяет некликабельность элемента"""
        try:
            element = WebDriverWait(self.browser, time).until(lambda driver: driver.find_element(*locator).is_enabled() is False)
            return True
        except TimeoutException:
            return False

    def element_is_visible(self, locator):
        """Метод проверяет отображается ли элемент на экране"""
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def element_is_invisible(self, locator):
        """Метод проверяет отсутствует ли элемент на экране"""
        try:
            self.find_element(locator)
        except TimeoutException:
            return False
        return True

    def hovering_mouse_an_item(self, locator):
        """Перемещает курсор мыши на элемент"""
        actions = ActionChains(self.browser)
        actions.move_to_element(self.find_element(locator))
        actions.perform()

    def items_is_displayed(self, items):
        """Проверяет отображение нескольких элементов на странице"""
        for item in items:
            return self.element_is_visible(item)

    def items_is_not_displayed(self, items):
        """Проверяет отсутствие нескольких элементов на странице"""
        for item in items:
            return self.element_is_invisible(item)

    def fill_selector_by_value(self, locator, value):
        """Осуществляет заполнение селектора выбранным значением"""
        select = Select(self.browser.find_element(locator))
        select.select_by_value(value)

    def switch_to_window(self, window_number: int):
        self.browser.switch_to.window(self.browser.window_handles[window_number])

    def close_window(self):
        self.browser.close()