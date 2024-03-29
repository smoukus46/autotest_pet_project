from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

class ToolTipsPage:

    # Кнопка Tool Tips в выпадающем списке Widgets
    TOOL_TIPS_ITEM = (By.XPATH, "//li[@id='item-6']/span[text()='Tool Tips']")

    # Кнопка Hover
    HOVER_BUTTON = (By.ID, "toolTipButton")

    