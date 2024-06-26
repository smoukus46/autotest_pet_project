from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import *
from pages.base_page import BasePage


class MainPageLocators:

    # Кнопка Elements
    BUTTON_ELEMENTS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(1)")

    # Кнопка Forms
    BUTTON_FORMS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(2)")

    # Кнопка Alerts, Frame & Windows
    BUTTON_ALERTS_FRAME_WINDOWS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(3)")

    # Кнопка WIDGETS
    BUTTON_WIDGETS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(4)")

    # Кнопка Interactions
    BUTTON_INTERACTIONS = (By.CSS_SELECTOR, ".category-cards > div:nth-child(5)")

    # Кнопка Book Store Application
    BUTTON_BOOK_STORE_APPLICATION = (By.CSS_SELECTOR, ".category-cards > div:nth-child(6)")


menu_items = [TextBoxPageLocators.TEXT_BOX_ITEM, CheckBoxPageLocators.CHECKBOX_ITEM,
              RadioBtnPageLocators.RADIO_BTN_ITEM, WebTablesPageLocators.WEB_TABLES_ITEM,
              ButtonsPageLocators.BUTTONS_ITEM, LinksPageLocators.LINKS_ITEM,
              BrokenLinksPageLocators.BROKEN_LINKS_ITEM, UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM,
              DynamicPropertiesPageLocators.DYNAMIC_PROPERTIES_ITEM]
alerts_items = [BrowserWindowsPageLocators.BROWSER_WINDOWS_ITEM, AlertsPageLocators.ALERTS_ITEM,
                ModalDialogsPageLocators.MODAL_DIALOGS_ITEM]


class MainPage(BasePage):

    pages_dict = {
        'pages': {
            'elements_page': MainPageLocators.BUTTON_ELEMENTS,
            'forms_page': MainPageLocators.BUTTON_FORMS,
            'alerts_page': MainPageLocators.BUTTON_ALERTS_FRAME_WINDOWS,
            'widgets_page': MainPageLocators.BUTTON_WIDGETS,
            'interactions_page': MainPageLocators.BUTTON_INTERACTIONS,
            'book_store_page': MainPageLocators.BUTTON_BOOK_STORE_APPLICATION
        }
    }

    def open_main_page(self):
        """Открывает в браузере главную страницу demoqa"""
        self.open('https://demoqa.com/')

    def check_tabs_in_main_dropdown(self, args: list):
        """Проверяет отображение позиций выпадающего списка"""
        elements = args
        try:
            for element in elements:
                return self.find_element(element).is_displayed()
        except NoSuchElementException:
            print("Элемент не найден на странице")


    def click_button_widgets_page(self):
        """Кликает на кнопку страницы Widgets"""
        return self.find_element(MainPageLocators.BUTTON_WIDGETS).click()
    
    def click_alerts_page_button(self):
        """Кликает на кнопку страницы Alerts, Frame & Windows"""
        self.find_element(MainPageLocators.BUTTON_ALERTS_FRAME_WINDOWS).click()

    def click_menu_elements_button(self):
        """Кликает на кнопку страницы Elements"""
        return self.find_element(MainPageLocators.BUTTON_ELEMENTS).click()

    def elements_menu_items_is_displayed(self):
        """Проверяет отображение всех разделов меню Elements"""
        return self.items_is_displayed(menu_items)
    
    def alerts_menu_items_is_displayed(self):
        """Проверяет отображение всех разделов меню Alerts, Frame & Windows"""
        return self.items_is_displayed(alerts_items)

    def click_button_page(self, page):
        """Нажимает кнопку перехода на нужную страницу в главном меню"""
        return self.find_element(self.pages_dict['pages'][page]).click()
