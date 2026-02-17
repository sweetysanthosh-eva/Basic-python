import time

from BasicSelenium import BasicSelenium


class NavigationCommands(BasicSelenium):
    def navigateoptions(self):
        self.browser.get("https://www.amazon.in/")
        time.sleep(10)
        self.browser.back()
        time.sleep(10)
        self.browser.forward()
        self.browser.refresh()
Navigation=NavigationCommands()
Navigation.accessbrowser()
Navigation.navigateoptions()

