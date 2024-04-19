from .main_page import MainPage
from pages.locators import *


class ModalDialogsPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_modal_dialogs_tab(self):
        """Открывает вкладку Modal Dialogs"""
        self.find_element(ModalDialogsPageLocators.MODAL_DIALOGS_ITEM).click()

    def click_small_modal_button(self):
        """Нажимает на кнопку Small Button"""
        self.find_element(ModalDialogsPageLocators.SMALL_MODAL_BTN).click()

    def check_small_modal_is_visible(self):
        """Проверяет отображение маленького модального окна"""
        small_modal = self.find_element(ModalDialogsPageLocators.SMALL_MODAL)
        small_modal_body = self.find_element(ModalDialogsPageLocators.SMALL_MODAL_BODY)
        width = small_modal.value_of_css_property("width")
        height = small_modal.value_of_css_property("height")
        assert width == '300px'
        assert height == '222px'
        assert small_modal_body.text == "This is a small modal. It has very less content"

    def click_close_small_modal_button(self):
        """Нажимает кнопку закрытия маленького модального окна"""
        self.find_element(ModalDialogsPageLocators.CLOSE_SMALL_MODAL_BTN).click()

    def click_large_modal_button(self):
        """Нажмает кнопку Large Modal"""
        self.find_element(ModalDialogsPageLocators.LARGE_MODAL_BTN).click()

    def check_large_modal_is_visible(self):
        """Проверяет отображение большого модального окна"""
        large_modal = self.find_element(ModalDialogsPageLocators.LARGE_MODAL)
        large_modal_body = self.find_element(ModalDialogsPageLocators.LARGE_MODAL_BODY)
        width = large_modal.value_of_css_property("width")
        height = large_modal.value_of_css_property("height")
        assert width == '800px'
        assert height == '334px'
        assert large_modal_body.text == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    def click_close_large_modal_button(self):
        """Нажимает кнопку закрытия большого модального окна"""
        self.find_element(ModalDialogsPageLocators.CLOSE_LARGE_MODAL_BTN).click()
