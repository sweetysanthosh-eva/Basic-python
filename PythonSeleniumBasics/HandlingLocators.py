from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingLocators(BasicSelenium):
    def verifylocators(self):
        self.browser.get("https://selenium.qabible.in/simple-form-demo.php")
        self.browser.find_element(By.ID,"single-input-field")
        self.browser.find_element(By.CLASS_NAME,"form-control")
        self.browser.find_element(By.TAG_NAME,"div")
        self.browser.find_element(By.LINK_TEXT,"Simple Form Demo")
        self.browser.find_element(By.PARTIAL_LINK_TEXT,"simple")
        self.browser.find_element(By.CSS_SELECTOR,"input[id='single-input-field']")
        self.browser.find_element(By.XPATH,"//input[@id='single-input-field'")




