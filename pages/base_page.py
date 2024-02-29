class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self, url):
        self.browser.get(url)

    def open_main_page(self):
        self.open('https://demoqa.com/')

    def find(self, args):
        return self.browser.find_element(*args)

    def is_element_displayed(self, selector):
        return self.find(selector).is_displayed()
