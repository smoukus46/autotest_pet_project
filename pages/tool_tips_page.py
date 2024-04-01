from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class ToolTipsPageLocators:

    # Кнопка Tool Tips в выпадающем списке Widgets
    TOOL_TIPS_ITEM = (By.XPATH, "//li[@id='item-6']/span[text()='Tool Tips']")

    # Кнопка Hover
    BUTTON_HOVER_ME_TO_SEE = (By.ID, "toolTipButton")

    # Ховер кнопки Hover
    HOVER_BUTTON_ME_TO_SEE = (By.XPATH, "//div[text()='You hovered over the Button']")

    # Поле Hover me to see
    FIELD_HOVER_ME_TO_SEE = (By.ID, "toolTipTextField")

    # Ховер поля Hover me to see
    HOVER_FIELD_ME_TO_SEE = (By.XPATH, "//div[text()='You hovered over the text field']")

    # Надпись Contrary
    INSCRIPTION_FIRST = (By.XPATH, "//a[text()='Contrary']")

    # Ховер надписи Contrary
    FIRST_TEXT_HOVER = (By.XPATH, "//div[text()='You hovered over the Contrary']")

    # Надпись 1.10.32
    INSCRIPTION_SECOND = (By.XPATH, "//a[text()='1.10.32']")

    # Ховер надписи 1.10.32
    SECOND_TEXT_HOVER = (By.XPATH, "//div[text()='You hovered over the 1.10.32']")


class ToolTipsPage(MainPage):

    hovers_elements_dict = {
        'button_hover_me_to_see': {
            'button_hover': ToolTipsPageLocators.BUTTON_HOVER_ME_TO_SEE, 
            'hover_button': ToolTipsPageLocators.HOVER_BUTTON_ME_TO_SEE,
        },
        'field_hover_me_to_see': {
            'field_hover': ToolTipsPageLocators.FIELD_HOVER_ME_TO_SEE,
            'hover_field': ToolTipsPageLocators.HOVER_FIELD_ME_TO_SEE,
        },
        'inscriptions_hovers': {
            'first_inscription': ToolTipsPageLocators.INSCRIPTION_FIRST,
            'hover_first_inscription': ToolTipsPageLocators.FIRST_TEXT_HOVER,
            'second_inscription': ToolTipsPageLocators.INSCRIPTION_SECOND,
            'hover_second_inscription': ToolTipsPageLocators.SECOND_TEXT_HOVER
        }
    }

    def check_is_visible_element(self, locator):
        """Проверяет видимость элемента"""
        if self.element_is_visible(locator):
            print("Элемент отображается")
        else:
            print('Элемент не видим, либо не прошло 10 секунд с момента загрузки страницы.')

    def click_tool_tips_button(self):
        """Нажимает кнопку "Tool Tips" в выпадающем списке Widgets"""
        return self.find_element(ToolTipsPageLocators.TOOL_TIPS_ITEM).click()
    
    def check_element_hover(self, key, value):
        """Нажимает кнопку "Hover me to see" в выпадающем списке Tool Tips"""
        self.hovering_mouse_an_item(self.hovers_elements_dict[key][value])
        self.check_is_visible_element(self.hovers_elements_dict[key][value])
