import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):

    options = Options()
    options.page_load_strategy = 'none'
    options.page_load_strategy = 'eager'

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    browser.maximize_window()

    yield browser
    browser.quit()
