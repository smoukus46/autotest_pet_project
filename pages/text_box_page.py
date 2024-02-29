from .base_page import BasePage
from .locators import *


class TextBoxPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def is_menu_items_is_displayed(self):
        self.is_element_displayed(TextBoxPageLocators.TEXT_BOX_ITEM)
        self.is_element_displayed(CheckBoxPageLocators.CHECKBOX_ITEM)
        self.is_element_displayed(RadioBtnPageLocators.RADIO_BTN_ITEM)
        self.is_element_displayed(WebTablesPageLocators.WEB_TABLES_ITEM)
        self.is_element_displayed(ButtonsPageLocators.BUTTONS_ITEM)
        self.is_element_displayed(LinksPageLocators.LINKS_ITEM)
        self.is_element_displayed(BrokenLinksPageLocators.BROKEN_LINKS_ITEM)
        self.is_element_displayed(UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM)
        self.is_element_displayed(DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM)

    def is_inputs_is_displayed(self):
        self.is_element_displayed(TextBoxPageLocators.NAME_INPUT)
        self.is_element_displayed(TextBoxPageLocators.EMAIL_INPUT)
        self.is_element_displayed(TextBoxPageLocators.CURRENT_ADDRESS_INPUT)
        self.is_element_displayed(TextBoxPageLocators.PERMANENT_ADDRESS_INPUT)
        self.is_element_displayed(TextBoxPageLocators.SUBMIT_BTN)
