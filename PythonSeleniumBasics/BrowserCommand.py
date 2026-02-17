from BasicSelenium import BasicSelenium



class BrowserCommand(BasicSelenium):
    def verifycommand(self):
        print(self.browser.title)
        print(self.browser.current_url )
        print(self.browser.current_window_handle)
        print(self.browser.page_source)
basic=BrowserCommand()
basic.accessbrowser()
basic.verifycommand()



