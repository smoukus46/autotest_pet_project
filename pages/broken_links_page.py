from .main_page import MainPage
from .locators import *
import requests


class BrokenLinksPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_broken_links_tab(self):
        """Открывает вкладку 'Broken Links'"""
        self.find_element(BrokenLinksPageLocators.BROKEN_LINKS_ITEM).click()

    def check_link_status(self, link_locator, link_status_code: int):
        """Проверяет совпадение получаемого статус-кода с ожидаемым"""
        link = self.find_element(link_locator).get_attribute("href")
        request = requests.get(link)
        assert request.status_code == link_status_code, "Статус-код не соответствует ожидаемому"

    def check_image_path(self, image_path):
        path = "https://demoqa.com/images/Toolsqa.jpg"
        path_to_image = self.find_element(image_path).get_attribute("src")
        assert path == path_to_image, "Неверный путь к изображению"
