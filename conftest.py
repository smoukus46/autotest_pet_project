import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
