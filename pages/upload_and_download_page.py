from .base_page import BasePage
from .locators import *
import os


class UploadAndDownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_upload_and_download_tab(self):
        self.button_click(UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM)

    def upload_picture(self):
        self.button_click(UploadAndDownloadPageLocators.UPLOAD_BTN)
        self.fill_input(UploadAndDownloadPageLocators.UPLOAD_BTN, 'D:/1.png')

    def upload_path_is_displayed(self):
        self.is_element_displayed(UploadAndDownloadPageLocators.UPLOAD_FILE_PATH)

    def download_picture(self):
        self.button_click(UploadAndDownloadPageLocators.DOWNLOAD_BTN)

    def check_download_file(self):
        file_path = 'D:/1.png'
        assert os.path.exists(file_path), "Файл не был скачан"
