from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class ToolTipsPage:

    # Кнопка Tool Tips в выпадающем списке Widgets
    TOOL_TIPS_ITEM = (By.XPATH, "//li[@id='item-6']/span[text()='Tool Tips']")

    # Кнопка Hover
    HOVER_BUTTON = (By.ID, "toolTipButton")

    # Поле Hover me to see
    FIELD_HOVER_ME_TO_SEE = (By.ID, "toolTipTextField")

    # Надпись Contrary
    INSCRIPTION_FIRST = (By.XPATH, "//a[text()='Contrary']")

    # Ховер надписи Contrary
    FIRST_TEXT_HOVER = (By.XPATH, "//div[text()='You hovered over the Contrary']")

    # Надпись 1.10.32
    INSCRIPTION_SECOND = (By.XPATH, "//a[text()='1.10.32']")

    # Ховер надписи 1.10.32
    SECOND_TEXT_HOVER = (By.XPATH, "//div[text()='You hovered over the 1.10.32']")


class ToolTipsPage(MainPage):
    