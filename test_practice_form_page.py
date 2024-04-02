from .pages.practice_form_page import PracticeFormPage
from pytest_testrail.plugin import pytestrail
from .pages.locators import *


@pytestrail.case('C8')
def test_fill_student_form(browser):
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
    assert "Ken Smith" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_STUDENT_NAME).text
    assert "KenSmith@test.ru" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_EMAIL).text
    assert "Male" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_GENDER).text
    assert "8800555353" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_PHONE).text
    assert "25 October,1997" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_DATE).text
    assert "Chemistry, Maths" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_SUBJECTS).text
    assert "Sports, Reading" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_HOBBIES).text
    assert "1.png" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_PICTURE).text
    assert ("Pushkina st., house of Kolotushkin" ==
            practice_form_page.find_element(PracticeFormPageLocators.RESULT_ADDRESS).text)
    assert "NCR Gurgaon" == practice_form_page.find_element(PracticeFormPageLocators.RESULT_STATE_AND_CITY).text
    practice_form_page.click_close_button()
    practice_form_page.element_is_not_displayed(PracticeFormPageLocators.INFO_ABOUT_STUDENT_FORM)
