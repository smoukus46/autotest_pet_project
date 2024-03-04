from .locators import *

menu_items = [TextBoxPageLocators.TEXT_BOX_ITEM, CheckBoxPageLocators.CHECKBOX_ITEM,
                  RadioBtnPageLocators.RADIO_BTN_ITEM, WebTablesPageLocators.WEB_TABLES_ITEM,
                  ButtonsPageLocators.BUTTONS_ITEM, LinksPageLocators.LINKS_ITEM,
                  BrokenLinksPageLocators.BROKEN_LINKS_ITEM, UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM,
                  DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM]


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

    def is_element_displayed(self, selector):
        return self.find(selector).is_displayed()

    def items_is_displayed(self, items):
        for item in items:
            return self.is_element_displayed(item)

    def button_click(self, button):
        self.find(button).click()

    def elements_menu_items_is_displayed(self):
        return self.items_is_displayed(menu_items)

    def fill_input(self, element_locator, sending_text):
        self.find(element_locator).send_keys(sending_text)

    def click_menu_elements_button(self):
        self.button_click(MainPageLocators.ELEMENTS_PAGE)


