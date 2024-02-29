from selenium.webdriver.common.by import By


class MainPageLocators:
    ELEMENTS_PAGE = (By.XPATH, "//*[text()='Elements']")
    FORMS_PAGE = (By.XPATH, "//*[text()='Forms']")
    ALERTS_FRAME_WINDOWS_PAGE = (By.XPATH, "//*[text()='Alerts, Frame & Windows']")
    WIDGETS_PAGE = (By.XPATH, "//*[text()='Widgets']")
    INTERACTIONS_PAGE = (By.XPATH, "//*[text()='Interactions']")
    BOOK_STORE_PAGE = (By.XPATH, "//*[text()='Book Store Application']")


class TextBoxPageLocators:
    TEXT_BOX_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Text Box']")
    