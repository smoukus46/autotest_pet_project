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
        """Открывает вкладку 'Web Tables'"""
        self.find_element(WebTablesPageLocators.WEB_TABLES_ITEM).click()

    def click_add_button(self):
        """Нажимает кнопку 'Добавить'"""
        self.find_element(WebTablesPageLocators.ADD_BTN).click()

    def registration_form_items_is_displayed(self):
        """Проверяет отображение полей с формы регистрации"""
        self.items_is_displayed(registration_form_inputs)

    def fill_registration_form(self):
        """Заполняет форму регистрации"""
        for i in range(len(registration_form_inputs)):
            self.fill_input(registration_form_inputs[i], adding_info[i])

    def click_submit_button(self):
        """Нажимает кнопку 'Submit'"""
        self.find_element(WebTablesPageLocators.SUBMIT_BTN).click()

    def check_added_result(self):
        """Проверяет добавленную информацию"""
        added_row = self.find_elements(WebTablesPageLocators.USER_ADD_ROW)

        for element in added_row[:-1]:
            assert element.text in adding_info, "Текст столбца не совпадает с проверяемым"

    def open_edit_form(self):
        """Открывает форму редактирования"""
        self.find_element(WebTablesPageLocators.EDIT_BTN_ONE).click()

    def fill_salary_input(self):
        """Заполнение поля 'Зарплата'"""
        self.find_element(WebTablesPageLocators.SALARY_INPUT).clear()
        self.find_element(WebTablesPageLocators.SALARY_INPUT).send_keys('25000')

    def check_editing_row(self):
        """Проверяет строку после редактирования"""
        row = self.find_elements(WebTablesPageLocators.FIRST_ROW)

        for element in row:
            if element == row[4]:
                assert element.text == '25000', "Зарплата не равна 25 000"

    def delete_row(self):
        """Удаляет строку"""
        self.find_element(WebTablesPageLocators.DELETE_BTN_ONE).click()

    def fill_row_countering(self):
        """Считает количество непустых строк в таблице"""
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
        """Проверяет отсутствие удаляемой строки"""
        row_before_delete = self.fill_row_countering()
        self.delete_row()
        row_after_delete = self.fill_row_countering()
        assert row_before_delete != row_after_delete, "Количество не пустых строк совпадает"

    def searching_in_table(self, text_to_search: str):
        """Осуществляет поиск данных в таблице"""
        self.find_element(WebTablesPageLocators.SEARCH_INPUT).clear()
        self.fill_input(WebTablesPageLocators.SEARCH_INPUT, text_to_search)

    def check_searching_result(self, string_for_comparison: list):
        """Проверяет результаты поиска"""
        search_result = []
        rows = self.find_elements(WebTablesPageLocators.ALL_ROWS_LOCATOR)

        for row in rows:
            sub_rows = row.find_elements(By.CLASS_NAME, "rt-td")
            for element in sub_rows[:3]:
                if element.text != ' ':
                    search_result.append(element.text)
            assert search_result == string_for_comparison, "Выведенные данные не соответствуют поисковому запросу"

    def create_ten_records(self):
        """Создает 10 записей в таблице"""
        for _ in range(11):
            self.click_add_button()
            self.fill_registration_form()
            self.click_submit_button()

    def fill_page_input(self, page: str):
        """Заполняет поле с номером страницы"""
        self.key_backspace(WebTablesPageLocators.PAGE_INPUT)
        self.fill_input(WebTablesPageLocators.PAGE_INPUT, page)
        self.key_enter(WebTablesPageLocators.PAGE_INPUT)

    def check_first_row_on_first_page(self):
        """Проверяет первую строку, отображаемую на первой странице"""
        added_row = self.find_elements(WebTablesPageLocators.FIRST_ROW)

        for element in added_row[:-1]:
            assert element.text not in adding_info, "Текст столбца не совпадает с проверяемым"

    def check_first_row_on_second_page(self):
        """Проверяет первую строку, отображаемую на второй странице"""
        added_row = self.find_elements(WebTablesPageLocators.FIRST_ROW)

        for element in added_row[:-1]:
            assert element.text in adding_info, "Текст столбца не совпадает с проверяемым"

    def click_next_btn(self):
        """Нажимает кнопку 'Next'"""
        self.find_element(WebTablesPageLocators.NEXT_BTN).click()

    def click_prev_btn(self):
        """Нажимает кнопку 'Previous'"""
        self.find_element(WebTablesPageLocators.PREVIOUS_BTN).click()
