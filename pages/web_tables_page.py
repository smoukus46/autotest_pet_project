from .base_page import BasePage
from .locators import *

registration_form_inputs = [WebTablesPageLocators.FIRST_NAME_INPUT, WebTablesPageLocators.LAST_NAME_INPUT,
                            WebTablesPageLocators.EMAIL_INPUT, WebTablesPageLocators.AGE_INPUT,
                            WebTablesPageLocators.SALARY_INPUT, WebTablesPageLocators.DEPARTMENT_INPUT]
adding_info = ['Artem', 'Alenin', 'Artem.Alenin@test.ru', '24', '2000', 'DPR']


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
        for i in range(len(registration_form_inputs)):
            self.fill_input(registration_form_inputs[i], adding_info[i])

    def click_submit_button(self):
        self.button_click(WebTablesPageLocators.SUBMIT_BTN)

    def check_added_result(self):
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

    def open_edit_form(self):
        self.button_click(WebTablesPageLocators.EDIT_BTN_ONE)

    def fill_salary_input(self):
        self.find(WebTablesPageLocators.SALARY_INPUT).clear()
        self.find(WebTablesPageLocators.SALARY_INPUT).send_keys('25000')

    def check_editing_row(self):
        row_info = []
        row = self.find(WebTablesPageLocators.FIRST_ROW)
        row_elements = row.find_elements_by_tag_name('div')

        for element in row_elements:
            row_info.append(element.text)

        assert row_info[4] == ['25000']
