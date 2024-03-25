from pages.progress_bar import ProgressBarPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C16')
def test_progress_bar(browser):
    """Проверка работы прогресс бара """
    test_progress_bar = ProgressBarPage(browser)
    test_progress_bar.open_main_page()
    test_progress_bar.click_button_widgets_page()
    test_progress_bar.click_progress_bar_button()
    test_progress_bar.click_start_stop_reset_button()
