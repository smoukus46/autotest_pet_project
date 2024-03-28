import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class TabsPageLocators:

    # Кнопка Tabs в выпадающем списке Widgets
    TABS_ITEM = (By.XPATH, "//li[@id='item-5']/span[text()='Tabs']")

    # Кнопка вкладки What
    TAB_WHAT_BUTTON = (By.CSS_SELECTOR, "a[id='demo-tab-what']")

    # Содержимое вкладки What
    TAB_WHAT_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-what']/p")

    # Кнопка вкладки Origin
    ORIGIN_TAB_BUTTON = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")

    # Содержимое вкладки Origin #1
    TAB_ORIGIN_CONTENT_FIRST = (By.XPATH, "//div[@id='demo-tabpane-origin']/p[1]")

    # Содержимое вкладки Origin #2
    TAB_ORIGIN_CONTENT_SECOND = (By.XPATH, "//div[@id='demo-tabpane-origin']/p[2]")

    # Кнопка вкладки Use
    TAB_USE_BUTTON = (By.CSS_SELECTOR, "a[id='demo-tab-use']")

    # Содержимое вкладки Use
    TAB_USE_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-use']/p")

    # Кнопка вкладки More
    TAB_MORE_BUTTON = (By.CSS_SELECTOR, "a[id='demo-tab-more']")


class TabsPage(MainPage):

    tabs_dict = {
        "tab_what": {
            "what_button": TabsPageLocators.TAB_WHAT_BUTTON,
            "what_content":  TabsPageLocators.TAB_WHAT_CONTENT,
        },
        "tab_origin": {
            "origin_button": TabsPageLocators.ORIGIN_TAB_BUTTON,
            "origin_content_1": TabsPageLocators.TAB_ORIGIN_CONTENT_FIRST,
            "origin_content_2": TabsPageLocators.TAB_ORIGIN_CONTENT_SECOND,
        },
        "tab_use": {
            "use_button": TabsPageLocators.TAB_USE_BUTTON,
            "use_content": TabsPageLocators.TAB_USE_CONTENT
        },
        "tab_more": {
            "more_button": TabsPageLocators.TAB_MORE_BUTTON
            }
        }


    def click_tab_button(self):
        """Нажимает кнопку "Tabs" в выпадающем списке Widgets"""
        return self.find_element(TabsPageLocators.TABS_ITEM).click()
    
    def click_and_check_tab(self, button, tab):
        """Жмет кнопку вкладки и проверяет содержимое"""
        return self.find_element(self.tabs_dict[button][tab]).click()

    def check_content_tab(self, button, content):
        """Проверяет, что содержимое вкладки не пустое"""
        text = self.find_element(self.tabs_dict[button][content]).text
        print(len(text))
        return text

    def check_not_clickable_tab(self, locator):
        """Проверяет, что нельзя открыть вкладку more"""
        return self.element_not_be_clickable(self.tabs_dict['tab_more'][locator])
