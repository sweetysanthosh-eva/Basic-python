import time

from selenium import webdriver


class BasicSelenium:
    def __init__(self):
        self.browser=webdriver.Chrome()
    def accessbrowser(self):
        browser = webdriver.Chrome()  # initializing the chrome instance
        self.browser.get("https://selenium.qabible.in")  #for getting the url
       # self.browser.maximize_window()
        time.sleep(10)  #get the time duration

    def closebrowser(self):
       # self.browser.quit()
      self.browser.close()

basic=BasicSelenium()
basic.accessbrowser()
basic.closebrowser()


