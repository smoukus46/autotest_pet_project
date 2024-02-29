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
    NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BTN = (By.ID, "submit")


class CheckBoxPageLocators:
    CHECKBOX_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Check Box']")


class RadioBtnPageLocators:
    RADIO_BTN_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Radio Button']")


class WebTablesPageLocators:
    WEB_TABLES_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Web Tables']")


class ButtonsPageLocators:
    BUTTONS_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Buttons']")
    DOUBLE_CLICK_BTN = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BTN = (By.ID, "rightClickBtn")
    CLICK_ME_BTN = (By.ID, "9ksW1")


class LinksPageLocators:
    LINKS_ITEM = (By.XPATH, "//li[@id='item-5']/span[text()='Links']")
    HOME_LINK = (By.ID, "simpleLink")
    HOME_DYNAMIC_LINK = (By.ID, "dynamicLink")
    CREATED_LINK = (By.ID, "created")
    NO_CONTENT_LINK = (By.ID, "no-content")
    MOVED_LINK = (By.ID, "moved")
    BAD_REQUEST_LINK = (By.ID, "bad-request")
    UNAUTHORIZED_LINK = (By.ID, "unauthorized")
    FORBIDDEN_LINK = (By.ID, "forbidden")
    NOT_FOUND_LINK = (By.ID, "invalid-url")


class BrokenLinksPageLocators:
    BROKEN_LINKS_ITEM = (By.XPATH, "//li[@id='item-6']/span[text()='Broken Links - Images']")


class UploadAndDownloadPageLocators:
    UPLOAD_AND_DOWNLOAD_ITEM = (By.XPATH, "//li[@id='item-7']/span[text()='Upload and Download']")
    DOWNLOAD_BTN = (By.ID, "downloadButton")
    UPLOAD_BTN = (By.ID, "uploadFile")


class DynamicPropertiesPageLocators:
    DYNAMIC_PROPERTIES_ITEM = (By.XPATH, "//li[@id='item-8']/span[text()='Dynamic Properties']")
    WILL_ENABLE_BTN = (By.ID, "enableAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_FIVE_SECONDS_BUTTON = (By.ID, "visibleAfter")


class PracticeFormPageLocators:
    PRACTICE_FORM_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Practice Form']")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_BTN = (By.ID, "gender-radio-1")
    MOBILE_INPUT = (By.ID, "userNumber")
    DATE_OR_BIRTH_INPUT = (By.ID, "dateOfBirthInput")
    DATEPICKER_MONTH = (By.CLASS_NAME, "react-datepicker__month-select")
    DATEPICKER_YEAR = (By.CLASS_NAME, "react-datepicker__year-select")
    DATEPICKER_DAY = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--025")
    SUBJECT_INPUT = (By.CLASS_NAME,
                     "subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3")
    HOBBIES_SPORTS_CHECKBOX = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_CHECKBOX = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC_CHECKBOX = (By.ID, "hobbies-checkbox-3")
    UPLOAD_PICTURE_BTN = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    # STATE_SELECT = (By.ID, "")
    # CITY_SELECT = (By.CSS_SELECTOR, "")
    SUBMIT_BTN = (By.ID, "submit")
