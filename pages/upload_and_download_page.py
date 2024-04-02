from .main_page import MainPage
from .locators import *
import os


class UploadAndDownloadPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_upload_and_download_tab(self):
        self.find_element(UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM).click()

    def upload_picture(self):
        self.find_element(UploadAndDownloadPageLocators.UPLOAD_BTN).click()
        self.fill_input(UploadAndDownloadPageLocators.UPLOAD_BTN, 'D:/1.png')

    def upload_path_is_displayed(self):
        self.is_element_displayed(UploadAndDownloadPageLocators.UPLOAD_FILE_PATH)

    def download_picture(self):
        self.find_element(UploadAndDownloadPageLocators.DOWNLOAD_BTN).click()

    def check_download_file(self):
        file_path = 'D:/1.png'
        assert os.path.exists(file_path), "Файл не был скачан"
