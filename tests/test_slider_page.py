import time
from pages.slider_page import SliderPage
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C14')
def test_slider(browser):
    """Проверка работы ползунка"""
    test_slider = SliderPage(browser)
    test_slider.open_main_page()
    test_slider.click_button_widgets_page()
    test_slider.click_slider_button()
    test_slider.move_slider_left_or_right()
