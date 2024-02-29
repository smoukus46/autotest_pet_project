class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(5)

    def open(self, url):
        return self.browser.get(url)

    def find(self, args):
        return self.browser.find_element(*args)

