from .locators import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

menu_items = [TextBoxPageLocators.TEXT_BOX_ITEM, CheckBoxPageLocators.CHECKBOX_ITEM,
              RadioBtnPageLocators.RADIO_BTN_ITEM, WebTablesPageLocators.WEB_TABLES_ITEM,
              ButtonsPageLocators.BUTTONS_ITEM, LinksPageLocators.LINKS_ITEM,
              BrokenLinksPageLocators.BROKEN_LINKS_ITEM, UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM,
              DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM]
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self, url):
        self.browser.get(url)

    def open_main_page(self):
        self.open('https://demoqa.com/')

    def find(self, args):
        return self.browser.find_element(*args)

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

    def fill_input(self, element_locator, sending_text):
        self.find(element_locator).send_keys(sending_text)

    def click_menu_elements_button(self):
        self.button_click(MainPageLocators.ELEMENTS_PAGE)

    def button_double_click(self):
        action.double_click(ButtonsPageLocators.DOUBLE_CLICK_BTN).perform()

    def button_right_click(self):
        action.context_click(ButtonsPageLocators.RIGHT_CLICK_BTN).perform()

    def fill_selector_by_value(self, locator, value):
        select = Select(self.browser.find(locator))
        select.select_by_value(value)
