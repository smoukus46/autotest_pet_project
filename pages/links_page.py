from .main_page import MainPage
from .locators import *
import requests

main_page_elements = [MainPageLocators.ELEMENTS_PAGE, MainPageLocators.FORMS_PAGE,
                      MainPageLocators.ALERTS_FRAME_WINDOWS_PAGE, MainPageLocators.WIDGETS_PAGE,
                      MainPageLocators.INTERACTIONS_PAGE, MainPageLocators.BOOK_STORE_PAGE]


class LinksPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def elements_on_main_page_is_displayed(self):
        return self.items_is_displayed(main_page_elements)

    def open_links_tab(self):
        self.find_element(LinksPageLocators.LINKS_ITEM).click()

    def open_home_link(self):
        self.find_element(LinksPageLocators.HOME_LINK).click()

    def open_dynamic_home_link(self):
        self.find_element(LinksPageLocators.HOME_DYNAMIC_LINK).click()

    def open_created_link(self):
        self.find_element(LinksPageLocators.CREATED_LINK).click()

    def open_no_content_link(self):
        self.find_element(LinksPageLocators.NO_CONTENT_LINK).click()

    def open_moved_link(self):
        self.find_element(LinksPageLocators.MOVED_LINK).click()

    def open_bad_request_link(self):
        self.find_element(LinksPageLocators.BAD_REQUEST_LINK).click()

    def open_unauthorized_link(self):
        self.find_element(LinksPageLocators.UNAUTHORIZED_LINK).click()

    def open_forbidden_link(self):
        self.find_element(LinksPageLocators.FORBIDDEN_LINK).click()

    def open_not_found_link(self):
        self.find_element(LinksPageLocators.NOT_FOUND_LINK).click()

    def check_link_status(self, link_locator, link_path: str, link_status_code: int):
        link = 'https://demoqa.com/'
        request = requests.get(f"{link}{link_path}")
        if request.status_code != link_status_code:
            self.find_element(link_locator).click()
        else:
            assert request.status_code == link_status_code, "Статус-код не соответствует ожидаемому"
