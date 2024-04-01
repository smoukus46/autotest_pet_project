from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class MenuPageLocators:

    # Кнопка Menu в выпадающем списке Widgets
    MENU_ITEM = (By.XPATH, "//li[@id='item-7']/span[text()='Menu']")

    # Первый выпадающий список меню
    MAIN_MENU_ITEM_FIRST = (By.XPATH, "//a[text()='Main Item 1']")

    # Второй выпадающий список меню
    MAIN_MENU_ITEM_SECOND = (By.XPATH, "//a[text()='Main Item 2']")

    # Выпадающий подсписок
    SUB_SUB_MENU = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li[3]")

    # Элементы второго выпадающего списка
    SUB_ITEMS_IN_MAIN_MENU_SECOND = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li")

    # Элементы третьего выпадающего подсписка
    SUB_ITEMS_IN_SUB_MENU = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li[3]/ul/li")

    # Третий выпадающий список меню
    MAIN_MENU_ITEM_THIRD = (By.XPATH, "//a[text()='Main Item 3']")


class MenuPage(MainPage):

    def click_menu_button(self):
        """Нажимает кнопку "Menu" в выпадающем списке Widgets"""
        return self.find_element(MenuPageLocators.MENU_ITEM).click()
    
    def check_sub_item_in_menu(self, locator):
        """Проверяет отображение элемент в выпадающем списке"""
        item_list = self.find_elements(locator)
        
        for item in item_list:
            self.hovering_mouse_an_item(item)
            if self.element_is_visible(item):
                print(f'Элемент: {item} отображается')
            else:
                print(f'Элемент: {item} не отображается')
    
    def check_elements_in_menu(self):
        """Проверяет отображение элементов в выпадающем списке"""
        self.hovering_mouse_an_item(MenuPageLocators.MAIN_MENU_ITEM_SECOND)
        self.check_sub_item_in_menu(MenuPageLocators.SUB_ITEMS_IN_MAIN_MENU_SECOND)
    
    def check_elements_in_sub_menu(self):
        """Проверяет отображение элементов в выпадающем подсписке"""
        self.hovering_mouse_an_item(MenuPageLocators.MAIN_MENU_ITEM_SECOND)
        self.hovering_mouse_an_item(MenuPageLocators.SUB_SUB_MENU)
        self.check_sub_item_in_menu(MenuPageLocators.SUB_ITEMS_IN_SUB_MENU)
