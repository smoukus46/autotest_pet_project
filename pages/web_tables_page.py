from .base_page import BasePage
from .locators import *

registration_form_inputs = [WebTablesPageLocators.FIRST_NAME_INPUT, WebTablesPageLocators.LAST_NAME_INPUT,
                            WebTablesPageLocators.EMAIL_INPUT, WebTablesPageLocators.AGE_INPUT,
                            WebTablesPageLocators.SALARY_INPUT, WebTablesPageLocators.DEPARTMENT_INPUT]


class WebTablesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_web_tables_tab(self):
        self.button_click(WebTablesPageLocators.WEB_TABLES_ITEM)

    def click_add_button(self):
        self.button_click(WebTablesPageLocators.ADD_BTN)

    def registration_form_items_is_displayed(self):
        self.items_is_displayed(registration_form_inputs)

    def fill_registration_form(self):
        self.fill_input(WebTablesPageLocators.FIRST_NAME_INPUT, 'Artem')
        self.fill_input(WebTablesPageLocators.LAST_NAME_INPUT, 'Alenin')
        self.fill_input(WebTablesPageLocators.EMAIL_INPUT, 'Artem.Alenin@test.ru')
        self.fill_input(WebTablesPageLocators.AGE_INPUT, '24')
        self.fill_input(WebTablesPageLocators.SALARY_INPUT, '2000')
        self.fill_input(WebTablesPageLocators.DEPARTMENT_INPUT, 'DPR')

    def click_submit_button(self):
        self.button_click(WebTablesPageLocators.SUBMIT_BTN)

    def check_added_result(self):
        adding_info = ['Artem', 'Alenin', 'Artem.Alenin@test.ru', '24', '2000', 'DPR']
        row_info = []
        added_row = self.find(WebTablesPageLocators.USER_ADD_ROW)
        row_elements = added_row.find_elements_by_tag_name('div')

        for element in row_elements:
            row_info.append(element.text)
            print(element.text)
        print(row_info)

        for info in adding_info:
            assert info in row_info
            print(info)
