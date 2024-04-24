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

    # Третий выпадающий список меню
    MAIN_MENU_ITEM_THIRD = (By.XPATH, "//a[text()='Main Item 3']")

    # Первый элемент выпадающего списка Main Item 2
    FIRST_ELEMENT_IN_MAIN_ITEM_SECOND = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li[1]/a")

    # Второй элемент выпадающего списка Main Item 2
    SECOND_ELEMENT_IN_MAIN_ITEM_SECOND = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li[2]/a")

    # Третий элемент выпадающего списка Main Item 2
    THIRD_ELEMENT_IN_MAIN_ITEM_SECOND = (By.XPATH, "//ul[@id='nav']/li[2]/ul/li[3]/a")

    # Первый элемент вложенного выпадающего списка
    FIRST_ELEMENT_IN_SUB_MENU = (By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[1]/a")

    # Второй элемент вложенного выпадающего списка
    SECOND_ELEMENT_IN_SUB_MENU = (By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")


class MenuPage(MainPage):

    main_item_second_elements = [MenuPageLocators.FIRST_ELEMENT_IN_MAIN_ITEM_SECOND, MenuPageLocators.SECOND_ELEMENT_IN_MAIN_ITEM_SECOND, MenuPageLocators.THIRD_ELEMENT_IN_MAIN_ITEM_SECOND]
    sub_menu_elements_in_main_item_second = [MenuPageLocators.FIRST_ELEMENT_IN_SUB_MENU, MenuPageLocators.SECOND_ELEMENT_IN_SUB_MENU]

    def click_menu_button(self):
        """Нажимает кнопку "Menu" в выпадающем списке Widgets"""
        return self.find_element(MenuPageLocators.MENU_ITEM).click()

    def check_first_main_item(self):
        """Проверяет наличие первого меню"""
        element = self.element_is_visible(MenuPageLocators.MAIN_MENU_ITEM_FIRST)
        if element == True:
            print('Элемент первого выпадающего списка виден')
        else:
            print('Элемент первого выпадающего списка не виден')

    def check_second_main_item(self):
        """Проверяет наличие элементов во втором меню"""
        self.hovering_mouse_an_item(MenuPageLocators.MAIN_MENU_ITEM_SECOND)
        for item in self.main_item_second_elements:
            if item != MenuPageLocators.THIRD_ELEMENT_IN_MAIN_ITEM_SECOND:
                self.hovering_mouse_an_item(item)
                element = self.element_is_visible(item)
                if element == True:
                    print('Элемент второго выпадающего списка виден')
                else:
                    print('Элемент второго выпадающего списка не виден')
            else:
                self.hovering_mouse_an_item(item)
                for sub_item in self.sub_menu_elements_in_main_item_second:
                    self.hovering_mouse_an_item(sub_item)
                    element = self.element_is_visible(sub_item)
                    if element == True:
                        print('Элемент третьего вложенного выпадающего списка виден')
                    else:
                        print('Элемент третьего вложенного выпадающего списка не виден')

    def check_third_main_item(self):
        """Проверяет наличие первого меню"""
        element = self.element_is_visible(MenuPageLocators.MAIN_MENU_ITEM_THIRD)
        if element == True:
            print('Элемент третьего выпадающего списка виден')
        else:
            print('Элемент третьего выпадающего списка не виден')
