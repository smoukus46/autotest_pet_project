from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class AutoCompleteLocators:

    AUTO_COMPLETE_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Auto Complete']")
    MULTIPLE_INPUT = (By.ID, "autoCompleteMultipleInput")
    MULTIPLE_MENU = (By.XPATH, "//div[@class='auto-complete__menu-list auto-complete__menu-list--is-multi css-11unzgr']")
    SINGLE_INPUT = (By.ID, "autoCompleteSingleInput")
    FIRST_ELEMENT_MENU = (By.XPATH, "//div[@class='auto-complete__menu-list auto-complete__menu-list--is-multi css-11unzgr']/div[1]")
    SECOND_ELEMENT_MENU = (By.XPATH, "//div[@class='auto-complete__menu-list auto-complete__menu-list--is-multi css-11unzgr']/div[2]")
    THIRD_ELEMENT_MENU = (By.XPATH, "//div[@class='auto-complete__menu-list auto-complete__menu-list--is-multi css-11unzgr']/div[3]")
    SELECTED_FIRST_ITEM = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value'][1]")
    SELECTED_SECOND_ITEM = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value'][2]")
    SELECTED_THIRD_ITEM = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value'][3]")
    MULTIPLE_AUTO_COMPLETE_REMOVE_BTN = (By.XPATH, "(//div[@class='css-xb97g8 auto-complete__multi-value__remove'])[1]")
    MULTIPLE_INPUT_REMOVE_BTN = (By.CLASS_NAME,
                                 "auto-complete__indicator auto-complete__clear-indicator css-tlfecz-indicatorContainer")


class AutoCompletePage(BasePage):
