from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.main_page import MainPage, MainPageLocators

texts_in_body_sections = ["""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",
                          """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.""",
                          """It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."""]

class AccordianPageLocators:

    # Кнопка Widgets в главном меню
    WIDGETS_PAGE = (By.CSS_SELECTOR, ".category-cards > div:nth-child(4)")

    # Кнопка Accordian в выпадающем списке Widgets
    ACCORDIAN_ITEM = (By.XPATH, "//span[text()='Accordian']")

    # Кнопка раскрытия первой детали
    FIRST_SECTION_HEADING = (By.ID, "section1Heading")

    # Тело первой детали
    FIRST_SECTION_BODY = (By.XPATH, "//div[@id='section1Content']")

    # Содержимое тела первой детали
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "//div[@id='section1Content']/p")

    # Кнопка раскрытия второй детали
    SECOND_SECTION_HEADING = (By.ID, "section2Heading")

    # Тело второй детали
    SECOND_SECTION_BODY = (By.XPATH, "//div[@id='section2Content']")

    # Содержимое тела второй детали
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "//div[@id='section3Content']/p")

    # Кнопка раскрытия третьей детали
    THIRD_SECTION_HEADING = (By.ID, "section3Heading")

    # Тело третьей детали
    THIRD_SECTION_BODY = (By.XPATH, "//div[@id='section3Content']")

    # Содержимое тела третьей детали
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "//div[@id='section3Content']/p")


class AccordianPage(MainPage):

    def click_widgets_button(self):
        """Нажимает кнопку "Widgets" в главном меню"""
        return self.click_button_page(MainPageLocators.BUTTON_WIDGETS)

    def click_accordian_button(self):
        """Нажимает кнопку "Accordian" в выпадающем списке Widgets-"""
        return self.find_element(AccordianPageLocators.ACCORDIAN_ITEM).click()

    def click_button_first_section(self):
        """Нажимает на первую деталь (раскрывает её)"""
        return self.find_element(AccordianPageLocators.FIRST_SECTION_HEADING).click()

    def click_button_second_section(self):
        """Нажимает на вторую деталь (раскрывает её)"""
        return self.find_element(AccordianPageLocators.SECOND_SECTION_HEADING).click()

    def click_button_third_section(self):
        """Нажимает на третью деталь (раскрывает её)"""
        return self.find_element(AccordianPageLocators.THIRD_SECTION_HEADING).click()

    def first_body_is_present(self, time=10):
        """Проверяет отображение тела первой детали и наличие в DOM"""
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(AccordianPageLocators.FIRST_SECTION_BODY))

    def second_body_is_present(self, time=10):
        """Проверяет отображение тела второй детали и наличие в DOM"""
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(AccordianPageLocators.SECOND_SECTION_BODY))

    def third_body_is_present(self, time=10):
        """Проверяет отображение тела третьей детали и наличие в DOM"""
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(AccordianPageLocators.THIRD_SECTION_BODY))

    def first_body_is_not_present(self, time=10):
        """Проверяет то, что тело первой детали не отображается"""
        return WebDriverWait(self.browser, time).until(EC.invisibility_of_element(AccordianPageLocators.FIRST_SECTION_BODY))

    def second_body_is_not_present(self, time=10):
        """Проверяет то, что тело второй детали не отображается"""
        return WebDriverWait(self.browser, time).until(EC.invisibility_of_element(AccordianPageLocators.SECOND_SECTION_BODY))

    def check_text_in_body_first_section(self):
        text_in_body = self.find_element(AccordianPageLocators.FIRST_SECTION_CONTENT).text
        assert text_in_body == texts_in_body_sections[0], "The text doesn't match"

    def check_text_in_body_second_section(self):
        text_in_body_1 = self.find_element(By.XPATH, "//div[@id='section2Content']/p[1]").text
        text_in_body_2 = self.find_element(By.XPATH, "//div[@id='section2Content']/p[2]").text
        assert text_in_body_1 + text_in_body_2 == texts_in_body_sections[1], "The text doesn't match"

    def check_text_in_body_third_section(self):
        text_in_body = self.find_element(AccordianPageLocators.THIRD_SECTION_CONTENT).text
        assert text_in_body == texts_in_body_sections[2], "The text doesn't match"
