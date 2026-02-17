import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingAlerts(BasicSelenium):
    def verifysimplealerts(self):
        self.browser.get("https://selenium.qabible.in/javascript-alert.php")
        alertbutton=self.browser.find_element(By.XPATH, "//button[@class='btn btn-success']")
        alertbutton.click()
        alert=self.browser.switch_to.alert
        print(alert.text)
        time.sleep(5)
        alert.accept()
    def verifyconfirmalerts(self):
        self.browser.get("https://selenium.qabible.in/javascript-alert.php")
        confirmalerts=self.browser.find_element(By.XPATH, "//button[@class='btn btn-warning']")
        confirmalerts.click()
        alert=self.browser.switch_to.alert
        #alert.accept() # ok
        alert.dismiss() #to cancel the message alerts
        time.sleep(5)
    def prompt_alert(self):
            # Navigate to URL
        self.browser.get("https://demoqa.com/alerts")

            # Locate the prompt alert button and click it
        prompt_alert = self.browser.find_element(By.ID, "promtButton")
        prompt_alert.click()

            # Switch to alert and send keys, then accept it
        alert = self.browser.switch_to.alert
        alert.send_keys("riya")
        time.sleep(5)
        alert.accept()
        time.sleep(10)


HandlingAlerts=HandlingAlerts()
HandlingAlerts.accessbrowser()
#HandlingAlerts.verifysimplealerts()
#HandlingAlerts.verifyconfirmalerts()
HandlingAlerts.prompt_alert()
