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
    NAME_OUTPUT = (By.ID, "name")
    EMAIL_OUTPUT = (By.ID, "email")
    CURRENT_ADDRESS_OUTPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_OUTPUT = (By.ID, "permanentAddress")


class CheckBoxPageLocators:
    CHECKBOX_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Check Box']")
    EXPAND_ALL_BTN = (By.CLASS_NAME, "rct-option rct-option-expand-all")
    COLLAPSE_ALL_BTN = (By.CLASS_NAME, "rct-option rct-option-collapse-all")
    HOME_EXPAND_CLOSE = (By.CLASS_NAME, "rct-collapse rct-collapse-btn")


class RadioBtnPageLocators:
    RADIO_BTN_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Radio Button']")
    YES_RADIO_BTN = (By.ID, "yesRadio")
    IMPRESSIVE_RADIO_BTN = (By.ID, "impressiveRadio")
    NO_RADIO_BTN = (By.CLASS_NAME, "custom-control-input disabled")
    RESULT_TEXT = (By.CLASS_NAME, "text-success")


class WebTablesPageLocators:
    WEB_TABLES_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Web Tables']")


class ButtonsPageLocators:
    BUTTONS_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Buttons']")
    DOUBLE_CLICK_BTN = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BTN = (By.ID, "rightClickBtn")
    CLICK_ME_BTN = (By.ID, "9ksW1")
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")


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
    UPLOAD_FILE_PATH = (By.ID, "uploadedFilePath")


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
    SUBJECT_CHEMISTRY_ITEM = (By.ID, "react-select-2-option-1")
    SUBJECT_MATHS_ITEM = (By.ID, "react-select-2-option-0")
    HOBBIES_SPORTS_CHECKBOX = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_CHECKBOX = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC_CHECKBOX = (By.ID, "hobbies-checkbox-3")
    UPLOAD_PICTURE_BTN = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    STATE_NCR_SELECT = (By.ID, "react-select-3-option-0")
    CITY_GURGAON_SELECT = (By.ID, "react-select-4-option-1")
    SUBMIT_BTN = (By.ID, "submit")
    CLOSE_BTN = (By.ID, "closeLargeModal")
    INFO_ABOUT_STUDENT_FORM = (By.CLASS_NAME, "modal-content")
    RESULT_STUDENT_NAME = (By.XPATH, "//tbody/tr[1]/td[2]")
    RESULT_EMAIL = (By.XPATH, "//tbody/tr[2]/td[2]")
    RESULT_GENDER = (By.XPATH, "//tbody/tr[3]/td[2]")
    RESULT_PHONE = (By.XPATH, "//tbody/tr[4]/td[2]")
    RESULT_DATE = (By.XPATH, "//tbody/tr[5]/td[2]")
    RESULT_SUBJECTS = (By.XPATH, "//tbody/tr[6]/td[2]")
    RESULT_HOBBIES = (By.XPATH, "//tbody/tr[7]/td[2]")
    RESULT_PICTURE = (By.XPATH, "//tbody/tr[8]/td[2]")
    RESULT_ADDRESS = (By.XPATH, "//tbody/tr[9]/td[2]")
    RESULT_STATE_AND_CITY = (By.XPATH, "//tbody/tr[10]/td[2]")


class BrowserWindowsPageLocators:
    BROWSER_WINDOWS_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Browser Windows']")
    NEW_TAB_BTN = (By.ID, "tabButton")
    NEW_WINDOW_BTN = (By.ID, "windowButton")
    NEW_WINDOW_MESSAGE = (By.ID, "messageWindowButton")


class AlertsPageLocators:
    ALERTS_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Alerts']")
    ALERT_BTN = (By.ID, "alertButton")
    TIMER_ALERT_BTN = (By.ID, "timerAlertButton")
    CONFIRM_BTN = (By.ID, "confirmButton")
    PROMPT_BTN = (By.ID, "promtButton")


class ModalDialogsPageLocators:
    FRAMES_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Frames']")
    NESTED_FRAMES_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Nested Frames']")
    MODAL_DIALOGS_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Modal Dialogs']")
    SMALL_MODAL_BTN = (By.ID, "showSmallModal")
    LARGE_MODAL_BTN = (By.ID, "showLargeModal")
    SMALL_MODAL = (By.CLASS_NAME, "modal-content")
    CLOSE_SMALL_MODAL_BTN = (By.ID, "closeSmallModal")
    LARGE_MODAL = (By.CLASS_NAME, "modal-content")
    CLOSE_LARGE_MODAL_BTN = (By.ID, "closeLargeModal")


class AccordianPageLocators:
    ACCORDIAN_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Accordian']")
    FIRST_SECTION_HEADING = (By.ID, "section1Heading")
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, "#section1Content p")
    SECOND_SECTION_HEADING = (By.ID, "section2Heading")
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, "#section2Content:first-child")
    THIRD_SECTION_HEADING = (By.ID, "section3Heading")
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, "#section3Content p")


class AutoCompletePageLocators:
    AUTO_COMPLETE_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Auto Complete']")
    MULTIPLE_INPUT = (By.ID, "autoCompleteMultipleInput")
    SINGLE_INPUT = (By.ID, "autoCompleteSingleInput")
    RED_COLOR_MULTIPLE_SELECTOR = (By.ID, "react-select-4-option-0")
    GREEN_COLOR_MULTIPLE_SELECTOR = (By.ID, "react-select-4-option-1")
    PURPLE_COLOR_MULTIPLE_SELECTOR = (By.ID, "react-select-4-option-2")
    INDIGO_COLOR_SINGLE_SELECTOR = (By.ID, "react-select-3-option-1")
    MAGENTA_COLOR_SINGLE_SELECTOR = (By.ID, "react-select-3-option-2")
    MULTIPLE_AUTO_COMPLETE_REMOVE_BTN = (By.XPATH, "(//div[@class='css-xb97g8 auto-complete__multi-value__remove'])[1]")
    MULTIPLE_INPUT_REMOVE_BTN = (By.CLASS_NAME,
                                 "auto-complete__indicator auto-complete__clear-indicator css-tlfecz-indicatorContainer")


class DatePickerPageLocators:
    DATE_PICKER_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Date Picker']")
    SELECT_DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    SELECT_DATE_MONTH_INPUT = (By.CLASS_NAME, "react-datepicker__month-select")
    SELECT_DATE_YEAR_INPUT = (By.CLASS_NAME, "react-datepicker__year-select")
    SELECT_DATE_DAY = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--018")
    DATE_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    DATE_TIME_MONTH_INPUT = (By.CLASS_NAME, "react-datepicker__month-read-view--selected-month")
    DATE_TIME_YEAR_INPUT = (By.CLASS_NAME, "react-datepicker__year-read-view--selected-year")
    DATE_TIME_DAY = (By.CLASS_NAME, "react-datepicker__day react-datepicker__day--005")
    DATE_TIME_SELECTOR = (By.XPATH, "//ul[@class='react-datepicker__time-list']/li[text()='17:45']")


class SliderPageLocators:
    SLIDER_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Slider']")
    # SLIDER =
    TOOLTIP = (By.CLASS_NAME, "range-slider__tooltip__label")
    SLIDER_VALUE_INPUT = (By.ID, "sliderValue")


class ProgressBarPageLocators:
    PROGRESS_BAR_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Progress Bar']")
    START_STOP_BTN = (By.ID, "startStopButton")
    RESET_BTN = (By.ID, "resetButton")
    PROGRESS_BAR = (By.CLASS_NAME, "progress-bar bg-info")


class TabsPageLocators:
    TABS_ITEM = (By.XPATH, "//li[@id='item-5']/span[text()='Tabs']")
    TAB_WHAT_BTN = (By.ID, "demo-tab-what")
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-what .mt-3")
    TAB_ORIGIN_BTN = (By.ID, "demo-tab-origin")
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-origin .mt-3")
    TAB_USE_BTN = (By.ID, "demo-tab-use")
    TAB_USE_CONTENT = (By.CSS_SELECTOR, "#demo-tabpane-use .mt-3")
    TAB_MORE_BTN = (By.ID, "demo-tab-more")


class ToolTipsPageLocators:
    TOOL_TIPS_ITEM = (By.XPATH, "//li[@id='item-6']/span[text()='Tool Tips']")
    HOVER_BTN = (By.ID, "toolTipButton")
    BTN_TOOL_TIP = (By.CLASS_NAME, "tooltip-inner")
    HOVER_INPUT = (By.ID, "texFieldToolTopContainer")
    INPUT_TOOL_TIP = (By.CLASS_NAME, "tooltip-inner")
    HOVER_WORD = (By.XPATH, "(//div[@id='texToolTopContainer'])/a[1]")
    WORD_TOOL_TIP = (By.CLASS_NAME, "tooltip-inner")
    HOVER_NUM = (By.XPATH, "(//div[@id='texToolTopContainer'])/a[2]")
    NUM_TOOL_TIP = (By.CLASS_NAME, "tooltip-inner")


class MenuPageLocators:
    MENU_ITEM = (By.XPATH, "//li[@id='item-7']/span[text()='Menu']")
    MAIN_MENU_ITEM_ONE = (By.XPATH, "//li/a[text()='Main Item 1']")
    MAIN_MENU_ITEM_TWO = (By.XPATH, "//li/a[text()='Main Item 2']")
    SUB_ITEM_ONE = (By.XPATH, "(//li/ul/li/a[text()='Sub Item'])[1]")
    SUB_ITEM_TWO = (By.XPATH, "(//li/ul/li/a[text()='Sub Item'])[2]")
    SUB_SUB_LIST = (By.XPATH, "//li/ul/li/a[text()='SUB SUB LIST »']")
    SUB_SUB_ITEM_ONE = (By.XPATH, "//li/ul/li/ul/li/a[text()='Sub Sub Item 1']")
    SUB_SUB_ITEM_TWO = (By.XPATH, "//li/ul/li/ul/li/a[text()='Sub Sub Item 2']")
    MAIN_MENU_ITEM_THREE = (By.XPATH, "//li/a[text()='Main Item 3']")


class SelectMenuPageLocators:
    SELECT_MENU_ITEM = (By.XPATH, "//li[@id='item-8']/span[text()='Select Menu']")
    SELECT_VALUE_MENU = (By.ID, "react-select-5-input")
    VALUE_OF_SELECT_MENU_ONE = (By.ID, "react-select-5-option-3")
    VALUE_OF_SELECT_MENU_TWO = (By.ID, "react-select-5-option-0-0")
    SELECT_ONE_MENU = (By.ID, "react-select-6-input")
    VALUE_OF_SELECT_ONE_MENU = (By.ID, "react-select-6-option-0-1")
    OLD_STYLE_SELECT_MENU = (By.ID, "oldSelectMenu")
    MULTISELECT_DROPDOWN_MENU = (By.ID, "react-select-7-input")
    RED_COLOR_OF_MULTISELECT_DROPDOWN_MENU = (By.ID, "react-select-4-option-3")
    GREEN_COLOR_OF_MULTISELECT_DROPDOWN_MENU = (By.ID, "react-select-4-option-0")
    BLUE_COLOR_OF_MULTISELECT_DROPDOWN_MENU = (By.ID, "react-select-4-option-1")
    INPUT_REMOVE_ITEM = (By.XPATH, "(//div[@class=' css-1wy0on6'])[3]/div[1]")
    VALUE_REMOVE_ITEM = (By.XPATH, "((//div[@class='css-1rhbuit-multiValue'])[1]/div[@class='css-xb97g8']")


class SortablePageLocators:
    SORTABLE_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Sortable']")
    LIST_ITEM_ONE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='One'])[1]")
    LIST_ITEM_TWO = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Two'])[1]")
    LIST_ITEM_THREE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Three'])[1]")
    LIST_ITEM_FOUR = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Four'])[1]")
    LIST_ITEM_FIVE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Five'])[1]")
    LIST_ITEM_SIX = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Six'])[1]")
    GRID_TAB = (By.ID, "demo-tab-grid")
    GRID_ITEM_ONE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='One'])[2]")
    GRID_ITEM_TWO = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Two'])[2]")
    GRID_ITEM_THREE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Three'])[2]")
    GRID_ITEM_FOUR = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Four'])[2]")
    GRID_ITEM_FIVE = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Five'])[2]")
    GRID_ITEM_SIX = (By.XPATH, "(//div[@class='list-group-item list-group-item-action'][text()='Six'])[2]")


class SelectablePageLocators:
    SELECTABLE_ITEM = (By.XPATH, "//li[@id='item-1']/span[text()='Selectable']")
    LIST_FIRST_ITEM = (By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action'][text()='Cras justo odio']")
    LIST_SECOND_ITEM = (By.XPATH,
                     "//li[@class='mt-2 list-group-item list-group-item-action'][text()='Dapibus ac facilisis in']")
    LIST_THIRD_ITEM = (By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action'][text()='Morbi leo risus']")
    LIST_FORTH_ITEM = (By.XPATH,
                      "//li[@class='mt-2 list-group-item list-group-item-action'][text()='Porta ac consectetur ac']")
    LIST_FIRST_ITEM_IS_SELECTED = (By.XPATH,
                                   "//li[@class='mt-2 list-group-item active list-group-item-action'][text()='Cras justo odio']")
    LIST_TWO_ITEM_IS_SELECTED = (By.XPATH,
                     "//li[@class='mt-2 list-group-item active list-group-item-action'][text()='Dapibus ac facilisis in']")
    GRID_TAB = (By.ID, "demo-tab-grid")
    GRID_FIRST_ITEM = (By.XPATH, "//li[@class='list-group-item list-group-item-action'][text()='One']")
    GRID_SECOND_ITEM = (By.XPATH, "//li[@class='list-group-item list-group-item-action'][text()='Two']")
    GRID_THIRD_ITEM = (By.XPATH, "//li[@class='list-group-item list-group-item-action'][text()='Three']")
    GRID_FIRST_ITEM_IS_SELECTED = (By.XPATH,
                                   "//li[@class='list-group-item active list-group-item-action'][text()='One']")
    GRID_THIRD_ITEM_IS_SELECTED = (By.XPATH,
                                   "//li[@class='list-group-item active list-group-item-action'][text()='Three']")


class ResizablePageLocators:
    RESIZABLE_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Resizable']")
    RESIZABLE_BOX = (By.ID, "resizableBoxWithRestriction")
    RESIZABLE_CONTAINER = (By.ID, "resizable")


class DroppablePageLocators:
    DROPPABLE_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Droppable']")
    SIMPLE_DRAGGABLE_ITEM = (By.ID, "draggable")
    SIMPLE_DROPPABLE_ITEM = (By.CSS_SELECTOR, "#simpleDropContainer > #droppable")
    ACCEPT_TAB = (By.ID, "droppableExample-tab-accept")
    ACCEPT_ITEM = (By.ID, "acceptable")
    NOT_ACCEPT_ITEM = (By.ID, "notAcceptable")
    ACCEPT_DROPPABLE_ITEM = (By.CSS_SELECTOR, "#acceptDropContainer > #droppable")
    PREVENT_PROPOGATION_TAB = (By.ID, "droppableExample-tab-preventPropogation")
    DRAG_BOX_ITEM = (By.ID, "dragBox")
    NOT_GREEDY_DROP_BOX = (By.ID, "notGreedyDropBox")
    NOT_GREEDY_INNER_DROP_BOX = (By.ID, "notGreedyInnerDropBox")
    GREEDY_DROP_BOX = (By.ID, "greedyDropBox")
    GREEDY_INNER_DROP_BOX = (By.ID, "greedyDropBoxInner")
    REVERT_DRAGGABLE_TAB = (By.ID, "droppableExample-tab-revertable")
    REVERTABLE_ITEM = (By.ID, "revertable")
    NOT_REVERTABLE_ITEM = (By.ID, "notRevertable")
    REVERTABLE_DROPPABLE_ITEM = (By.CSS_SELECTOR, "#revertableDropContainer > #droppable")


class DraggablePageLocators:
    DRAGGABLE_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Dragabble']")
    SIMPLE_DRAGGABLE_BOX = (By.ID, "dragBox")
    AXIS_RESTRICTED_TAB = (By.ID, "draggableExample-tab-axisRestriction")
    RESTRICTED_ONLY_X_BOX = (By.ID, "restrictedX")
    RESTRICTED_ONLY_Y_BOX = (By.ID, "restrictedY")
    CONTAINER_RESTRICTED_TAB = (By.ID, "draggableExample-tab-containerRestriction")
    WRAP_CONTAINER = (By.ID, "containmentWrapper")
    BOX_IN_CONTAINER = (By.CLASS_NAME, "draggable ui-widget-content ui-draggable ui-draggable-handle")
    WRAP_TEXT = (By.CLASS_NAME, "draggable ui-widget-content m-3")
    TEXT_IN_CONTAINER = (By.CLASS_NAME, "ui-widget-header ui-draggable ui-draggable-handle")
    CURSOR_STYLE_TAB = (By.ID, "draggableExample-tab-cursorStyle")
    CURSOR_IN_CENTER_BOX = (By.ID, "cursorCenter")
    CURSOR_IN_TOP_LEFT_BOX = (By.ID, "cursorTopLeft")
    CURSOR_IN_BOTTOM_BOX = (By.ID, "cursorBottom")


class LoginPageLocators:
    LOGIN_ITEM = (By.XPATH, "//li[@id='item-0']/span[text()='Login']")
    BOOK_STORE_ITEM = (By.XPATH, "//li[@id='item-2']/span[text()='Book Store']")
    PROFILE_ITEM = (By.XPATH, "//li[@id='item-3']/span[text()='Profile']")
    BOOK_STORE_API_ITEM = (By.XPATH, "//li[@id='item-4']/span[text()='Book Store API']")
    USER_NAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login")
    NEW_USER_BTN = (By.ID, "newUser")


class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    USER_NAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    CAPTCHA_CHECKBOX = (By.ID, "recaptcha-anchor")
    REGISTER_BTN = (By.ID, "register")
    LOGOUT_BTN = (By.XPATH, "//button[text()='Log out']")
    