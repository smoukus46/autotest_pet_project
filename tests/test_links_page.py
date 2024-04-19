from pages.links_page import LinksPage
from pages.locators import *
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C33')
def test_links_page(browser):
    """Проверка работы ссылок на странице 'Links'"""
    links_page = LinksPage(browser)
    links_page.open_main_page()
    links_page.click_menu_elements_button()
    links_page.elements_menu_items_is_displayed()
    links_page.open_links_tab()
    links_page.open_home_link()
    links_page.switch_to_window(1)
    links_page.elements_on_main_page_is_displayed()
    links_page.close_window()
    links_page.switch_to_window(0)
    links_page.open_dynamic_home_link()
    links_page.switch_to_window(1)
    links_page.elements_on_main_page_is_displayed()
    links_page.close_window()
    links_page.switch_to_window(0)
    links_page.check_link_status(LinksPageLocators.CREATED_LINK, "created", 201)
    links_page.check_link_status(LinksPageLocators.NO_CONTENT_LINK, "no-content", 204)
    links_page.check_link_status(LinksPageLocators.MOVED_LINK, "moved", 301)
    links_page.check_link_status(LinksPageLocators.BAD_REQUEST_LINK, "bad-request", 400)
    links_page.check_link_status(LinksPageLocators.UNAUTHORIZED_LINK, "unauthorized", 401)
    links_page.check_link_status(LinksPageLocators.FORBIDDEN_LINK, "forbidden", 403)
    links_page.check_link_status(LinksPageLocators.NOT_FOUND_LINK, "invalid-url", 404)
