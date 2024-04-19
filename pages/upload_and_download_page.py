from .main_page import MainPage
from .locators import *
import os


class UploadAndDownloadPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_upload_and_download_tab(self):
        """Открывает вкладку Upload and Download"""
        self.find_element(UploadAndDownloadPageLocators.UPLOAD_AND_DOWNLOAD_ITEM).click()

    def upload_picture(self):
        """Загружает картинку на сайт"""
        self.fill_input(UploadAndDownloadPageLocators.UPLOAD_BTN, 'D:/1.png')

    def upload_path_is_displayed(self):
        """Проверяет отображение пути к загружаемому файлу"""
        self.element_is_visible(UploadAndDownloadPageLocators.UPLOAD_FILE_PATH)

    def download_picture(self):
        """Скачивает картинку"""
        self.find_element(UploadAndDownloadPageLocators.DOWNLOAD_BTN).click()

    def check_download_file(self):
        """Проверяет, что картинка скачалась"""
        file_path = 'C:/Users/Nikita.Yakovlev/Downloads/sampleFile.jpeg'
        assert os.path.exists(file_path), "Файл не был скачан"
