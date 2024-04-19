import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from generator.generator import SelectValues, Colors

class SelectMenuPageLocators:

    select = SelectValues()
    select_value = select.select_values
    colors = Colors()
    color = colors.colors

    # Кнопка Select Menu в выпадающем списке Widgets
    SELECT_MENU_ITEM = (By.XPATH, "//li[@id='item-8']/span[text()='Select Menu']")

    # Поле Select Value
    SELECT_VALUE_INPUT = (By.ID, "withOptGroup")

    # Значения выпадающего списка Select Value
    ELEMENT_IN_SELECT_VALUE_INPUT = (By.XPATH, "//div[@class=' css-yt9ioa-option']")

    # Поле Select One
    SELECT_ONE_INPUT = (By.ID, "selectOne")

    # Значения выпадающего списка Select One
    ELEMENT_IN_SELECT_ONE_INPUT = (By.ID, f"react-select-3-option-0-{random.randint(0, 5)}")

    # Поле Old Style Select Menu
    OLD_STYLE_SELECT_MENU_INPUT = (By.ID, "oldSelectMenu")

    # Значения выпадающего списка Old Style Select Menu
    ELEMENT_IN_OLD_STYLE_SELECT_MENU = (By.XPATH, f"//option[text()='{color}']")

    # Поле Multiselect Dropdown Menu
    MULTISELECT_DROPDOWN_INPUT = (By.XPATH, "//*[@id='selectMenuContainer']/div[7]/div/div/div")

    # Выпадающие значения Multiselect Dropdown Menu
    ELEMENT_IN_MULTISELECT_DROPDOWN_INPUT = (By.XPATH, "//div[@class=' css-11unzgr']/div")

    # Кнопка очистки поля Multiselect Dropdown Menu
    CLEAR_MULTISELECT_DROPDOWN_INPUT = (By.CSS_SELECTOR, "#selectMenuContainer > div:nth-child(8) > div > div > div > div.css-1wy0on6 > div:nth-child(1) > svg > path")

    # Поле Standart multi select
    STANDART_MULTI_SELECT_INPUT = (By.ID, "cars")

class SelectMenuPage(MainPage):

    cars_models = ["Volvo", "Saab", "Opel", "Audi"]

    def click_select_menu_button(self):
        """Нажимает кнопку "Select Menu" в выпадающем списке Widgets"""
        return self.find_element(SelectMenuPageLocators.SELECT_MENU_ITEM).click()
    
    def click_and_fill_select_value_input(self):
        """Нажимает на поле Select Value и заполняет его значением"""
        self.find_element(SelectMenuPageLocators.SELECT_VALUE_INPUT).click()
        elements = self.find_elements(SelectMenuPageLocators.ELEMENT_IN_SELECT_VALUE_INPUT)
        elements[random.randint(0, 4)].click()

    def click_and_fill_select_one_input(self):
        """Нажимает на поле Select One и заполняет его значением"""
        self.find_element(SelectMenuPageLocators.SELECT_ONE_INPUT).click()
        self.find_element(SelectMenuPageLocators.ELEMENT_IN_SELECT_ONE_INPUT).click()
    
    def click_and_fill_old_style_select_menu(self):
        """Нажимает на поле Old Style Select Menu и заполняет его значением"""
        self.find_element(SelectMenuPageLocators.OLD_STYLE_SELECT_MENU_INPUT).click()
        self.find_element(SelectMenuPageLocators.ELEMENT_IN_OLD_STYLE_SELECT_MENU).click()

    def click_and_fill_multiselect_dropdown_input(self):
        """Нажимает на поле Multiselect Dropdown Menu и заполняет его значением"""
        self.find_element(SelectMenuPageLocators.MULTISELECT_DROPDOWN_INPUT).click()
        colors = self.find_elements(SelectMenuPageLocators.ELEMENT_IN_MULTISELECT_DROPDOWN_INPUT)
        for _ in colors:
            random.choice(colors).click()
            colors = self.find_elements(SelectMenuPageLocators.ELEMENT_IN_MULTISELECT_DROPDOWN_INPUT)
        self.find_element(SelectMenuPageLocators.CLEAR_MULTISELECT_DROPDOWN_INPUT).click()

    def fill_standart_multi_select_input(self):
        """Выбирает значение в поле Standart multi select"""
        self.select_value_text(SelectMenuPageLocators.STANDART_MULTI_SELECT_INPUT, random.choice(self.cars_models))
