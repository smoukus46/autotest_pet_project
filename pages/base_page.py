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
        self.browser.get(url)

    def find_element(self, locator, time=20):
        """Ищет один элемент, подходящий по условию"""
        element = WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    def find_elements(self, locator, time=20):
        """Ищет все элементы, подходящие по условию"""
        return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator))

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

    def hovering_mouse_an_item(self, locator):
        """Перемещает курсор мыши на элемент"""
        actions = ActionChains(self.browser)
        actions.move_to_element(self.find_element(locator))
        actions.perform()

    def drag_and_drop_elements(self, what, where):
        """Перетаскивает элемент"""
        actions = ActionChains(self.browser)
        actions.drag_and_drop(what, where)
        actions.perform()

    def element_stretching(self, locator, x=0, y=0):
        """Удерживает левую кнопку мыши и растягивается по оси x и y"""
        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(locator, x, y)
        actions.perform()
