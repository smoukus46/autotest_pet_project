from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class AccordianPageLocators:
    
    # Кнопка Widgets в главном меню
    WIDGETS_PAGE = (By.XPATH, "//*[text()='Widgets']")

    # Кнопка Accordian в выпадающем списке Widgets
    ACCORDIAN_ITEM = (By.XPATH, "//span[text()='Accordian']")

    # Кнопка раскрытия первой детали
    FIRST_SECTION_HEADING = (By.ID, "section1Heading")

    # Тело первой детали
    FIRST_SECTION_BODY = (By.XPATH, "//div[@id='section1Content']")

    # Содержимое тела первой детали
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "#section1Content p")

    # Кнопка раскрытия второй детали
    SECOND_SECTION_HEADING = (By.ID, "section2Heading")

    # Тело второй детали
    SECOND_SECTION_BODY = (By.XPATH, "//div[@id='section2Content']")

    # Содержимое тела второй детали
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "#section2Content:first-child")

    # Кнопка раскрытия третьей детали
    THIRD_SECTION_HEADING = (By.ID, "section3Heading")

    # Тело третьей детали
    THIRD_SECTION_BODY = (By.XPATH, "//div[@id='section3Content']")

    # Содержимое тела третьей детали
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "#section3Content p")


class AccordianPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def click_widgets_button(self):
        """Нажимает кнопку "Widgets" в главном меню"""
        return self.browser.find_element(*AccordianPageLocators.WIDGETS_PAGE).click()

    def check_elements_widgets_dropdown(self):
        """Проверяет отображение элементов выпадающего списка Widgets"""
        widgets_dropdown_locators = [(By.XPATH, "//span[text()='Auto Complete']"),
                                     (By.XPATH, "//span[text()='Date Picker']"),
                                     (By.XPATH, "//span[text()='Slider']"),
                                     (By.XPATH, "//span[text()='Progress Bar']"),
                                     (By.XPATH, "//span[text()='Tabs']"),
                                     (By.XPATH, "//span[text()='Tool Tips']"),
                                     (By.XPATH, "//span[text()='Menu']"),
                                     (By.XPATH, "//span[text()='Select Menu']")]
        try:
            for locator in widgets_dropdown_locators:
                WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(*locator))
            return True
        except Exception as e:
            print("An error occurred:", e)
            return False

    def click_accordian_button(self):
        """Нажимает кнопку "Accordian" в выпадающем списке Widgets-"""
        return self.browser.find_element(*AccordianPageLocators.ACCORDIAN_ITEM).click()

    def click_button_section(self, args):
        """Нажимает на деталь (раскрывает её)"""
        return self.browser.find_element(*args).click()

    def body_is_present(self, args):
        """Проверяет отображение детали"""
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(*args))
            return True
        except TimeoutException:
            return False

    def body_is_not_present(self, args):
        """Проверяет, что элемент скрыт на странице"""
        try:
            WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(*args))
            return True
        except TimeoutException:
            return False
