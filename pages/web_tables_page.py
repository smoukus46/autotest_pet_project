from .main_page import MainPage
from .locators import *

registration_form_inputs = [WebTablesPageLocators.FIRST_NAME_INPUT, WebTablesPageLocators.LAST_NAME_INPUT,
                            WebTablesPageLocators.EMAIL_INPUT, WebTablesPageLocators.AGE_INPUT,
                            WebTablesPageLocators.SALARY_INPUT, WebTablesPageLocators.DEPARTMENT_INPUT]
adding_info = ['Artem', 'Alenin', 'Artem.Alenin@test.ru', '24', '2000', 'DPR']


class WebTablesPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_web_tables_tab(self):
        self.find_element(WebTablesPageLocators.WEB_TABLES_ITEM).click()

    def click_add_button(self):
        self.find_element(WebTablesPageLocators.ADD_BTN).click()

    def registration_form_items_is_displayed(self):
        self.items_is_displayed(registration_form_inputs)

    def fill_registration_form(self):
        for i in range(len(registration_form_inputs)):
            self.fill_input(registration_form_inputs[i], adding_info[i])

    def click_submit_button(self):
        self.find_element(WebTablesPageLocators.SUBMIT_BTN).click()

    def check_added_result(self):
        added_row = self.find_elements(WebTablesPageLocators.USER_ADD_ROW)

        for element in added_row[:-1]:
            assert element.text in adding_info

    def open_edit_form(self):
        self.find_element(WebTablesPageLocators.EDIT_BTN_ONE).click()

    def fill_salary_input(self):
        self.find_element(WebTablesPageLocators.SALARY_INPUT).clear()
        self.find_element(WebTablesPageLocators.SALARY_INPUT).send_keys('25000')

    def check_editing_row(self):
        row = self.find_elements(WebTablesPageLocators.FIRST_ROW)

        for element in row:
            if element == row[4]:
                assert element.text == '25000'

    def delete_row(self):
        self.find_element(WebTablesPageLocators.DELETE_BTN_ONE).click()

    def fill_row_countering(self):
        fill_row_counter = 0
        rows = self.find_elements(WebTablesPageLocators.ALL_ROWS_LOCATOR)

        for row in rows:
            sub_rows = row.find_elements(By.CLASS_NAME, "rt-td")
            for element in sub_rows[:-1]:
                if element.text != ' ':
                    fill_row_counter += 1
                else:
                    break
        return fill_row_counter

    def check_deleting(self):
        row_before_delete = self.fill_row_countering()
        self.delete_row()
        row_after_delete = self.fill_row_countering()
        assert row_before_delete != row_after_delete

    def searching_in_table(self, text_to_search: str):
        self.find_element(WebTablesPageLocators.SEARCH_INPUT).clear()
        self.fill_input(WebTablesPageLocators.SEARCH_INPUT, text_to_search)

    def check_searching_result(self, string_for_comparison: list):
        search_result = []
        rows = self.find_elements(WebTablesPageLocators.ALL_ROWS_LOCATOR)

        for row in rows:
            sub_rows = row.find_elements(By.CLASS_NAME, "rt-td")
            for element in sub_rows[:3]:
                if element.text != ' ':
                    search_result.append(element.text)
            assert search_result == string_for_comparison, "Выведенные данные не соответствуют поисковому запросу"

