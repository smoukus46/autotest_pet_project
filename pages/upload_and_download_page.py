from .base_page import BasePage
from .locators import *


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
