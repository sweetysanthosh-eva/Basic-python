import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingDropdown(BasicSelenium):
    def verifydropdown(self):
        self.browser.get("https://selenium.qabible.in/select-input.php")
        selectcolor=self.browser.find_element(By.XPATH,"//select[@id='single-input-field']")
        select=Select(selectcolor) #syntax for dropdown
        select.select_by_index(1)
        select.select_by_value("Yellow")
        time.sleep(5)
        select.select_by_visible_text("Green")
    def verifycheckbox(self):
        self.browser.get("https://selenium.qabible.in/check-box-demo.php")
        checkbox=self.browser.find_element(By.XPATH,"//input[@id='gridCheck']")
        checkbox.click()
        time.sleep(5)
    def verifyradiobutton(self):
        self.browser.get("https://selenium.qabible.in/radio-button-demo.php")
        radiobutton=self.browser.find_element(By.XPATH,"//input[@id='inlineRadio1']")
        radiobutton.click()
        time.sleep(5)

handlingdropdown=HandlingDropdown()
handlingdropdown.accessbrowser()
handlingdropdown.verifydropdown()
handlingdropdown.verifycheckbox()
handlingdropdown.verifyradiobutton()