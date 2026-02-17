import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingMultipletabs(BasicSelenium):
    def verifymultipletabs(self):
        self.browser.get("https://demoqa.com/browser-windows")
        firstwindow=self.browser.current_window_handle
        time.sleep(5)
        newtab=self.browser.find_element(By.XPATH, "//button[@id='tabButton']")
        newtab.click()
        handleid=self.browser.window_handles #syntax for retriving and handle multiple tab ids
        for handle in handleid:
            if handle != firstwindow:
                self.browser.switch_to.window(handle)
                print(self.browser.current_url)
                self.browser.switch_to.window(firstwindow)

HandlingMultipletabs=HandlingMultipletabs()
HandlingMultipletabs.accessbrowser()
HandlingMultipletabs.verifymultipletabs()