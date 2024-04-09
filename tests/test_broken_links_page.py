from pages.broken_links_page import BrokenLinksPage
from pages.locators import *
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C34')
def test_check_links_on_broken_links_page(browser):
    """Проверка работы ссылок на странице 'Broken Links'"""
    broken_links_page = BrokenLinksPage(browser)
    broken_links_page.open_main_page()
    broken_links_page.click_menu_elements_button()
    broken_links_page.elements_menu_items_is_displayed()
    broken_links_page.open_broken_links_tab()
    broken_links_page.check_link_status(BrokenLinksPageLocators.VALID_LINK, 200)
    broken_links_page.check_link_status(BrokenLinksPageLocators.BROKEN_LINK, 200)


@pytestrail.case('C35')
def test_check_image_on_broken_links_page(browser):
    """Проверка отображения изображений на странице 'Broken Links'"""
    broken_links_page = BrokenLinksPage(browser)
    broken_links_page.open_main_page()
    broken_links_page.click_menu_elements_button()
    broken_links_page.elements_menu_items_is_displayed()
    broken_links_page.open_broken_links_tab()
    broken_links_page.check_image_path(BrokenLinksPageLocators.IMG_LINK)
    broken_links_page.check_image_path(BrokenLinksPageLocators.BROKEN_IMG_LINK)
