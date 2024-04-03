import time

from pages.upload_and_download_page import UploadAndDownloadPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C36')
def test_upload_and_download_file(browser):
    """Проверка работы скачивания и загрузки файла """
    upload_and_download_page = UploadAndDownloadPage(browser)
    upload_and_download_page.open_main_page()
    upload_and_download_page.click_menu_elements_button()
    upload_and_download_page.elements_menu_items_is_displayed()
    upload_and_download_page.open_upload_and_download_tab()
    upload_and_download_page.download_picture()
    time.sleep(5)
    upload_and_download_page.check_download_file()
    upload_and_download_page.upload_picture()
    upload_and_download_page.upload_path_is_displayed()
