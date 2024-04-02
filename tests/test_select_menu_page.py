from pages.menu_page import MenuPage
from pytest_testrail.plugin import pytestrail

@pytestrail.case('C19')
def test_menu(browser):
    """Проверка отображения меню"""