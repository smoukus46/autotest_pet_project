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
        }
        }

    def click_slider_button(self):
        """Нажимает кнопку "Tabs" в выпадающем списке Widgets"""
        return self.find_element(TabsPageLocators.TABS_ITEM).click()
    
    def click_and_check_tab(self, button, content):
        """Жмет кнопку вкладки и проверяет содержимое"""
        self.find_element(button).click()
        tab_contents = self.find_element(content).text
        return len(tab_contents)
    