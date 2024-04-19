from pages.practice_form_page import PracticeFormPage
from pytest_testrail.plugin import pytestrail
from pages.locators import *


@pytestrail.case('C8')
def test_fill_student_form(browser):
    """Заполнение формы регистрации студента"""
    practice_form_page = PracticeFormPage(browser)
    practice_form_page.open_main_page()
    practice_form_page.click_menu_forms_button()
    practice_form_page.forms_menu_item_is_displayed()
    practice_form_page.open_practice_tab()
    practice_form_page.fill_first_name_input()
    practice_form_page.fill_last_name_input()
    practice_form_page.fill_email_input()
    practice_form_page.gender_radio_click()
    practice_form_page.fill_mobile_input()
    practice_form_page.fill_datepicker()
    practice_form_page.fill_subjects_input()
    practice_form_page.hobbies_checkbox_click()
    practice_form_page.upload_picture()
    practice_form_page.fill_current_address_input()
    practice_form_page.fill_state_selector()
    practice_form_page.fill_city_selector()
    practice_form_page.click_submit_button()
    assert "Ken Smith" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_STUDENT_NAME).text, 'Имя не соответствует заполняемому'
    assert "KenSmith@test.ru" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_EMAIL).text, 'Фамилия не соответствует заполняемому'
    assert "Male" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_GENDER).text, 'Пол не соответствует заполняемому'
    assert "8800555353" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_PHONE).text, 'Телефон не соответствует заполняемому'
    assert None is not practice_form_page.find_element(PracticeFormPageLocators.RESULT_DATE).text, 'Дата рождения не соответствует выбранной'
    assert "Chemistry, Maths" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_SUBJECTS).text, 'Предметы не соответствуют выбранным'
    assert "Sports, Reading, Music" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_HOBBIES).text, 'Хобби не соответствуют выбранным'
    assert "1.png" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_PICTURE).text, 'Имя файла не соответствует заполняемому'
    assert "Pushkina st., house of Kolotushkin" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_ADDRESS).text, 'Адрес не соответствует заполняемому'
    assert "NCR Gurgaon" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_STATE_AND_CITY).text, 'Город не соответствует заполняемому'
    practice_form_page.click_close_button()
    practice_form_page.element_is_invisible(PracticeFormPageLocators.INFO_ABOUT_STUDENT_FORM)
