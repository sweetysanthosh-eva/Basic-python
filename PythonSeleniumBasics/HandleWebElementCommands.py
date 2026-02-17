import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleWebElementCommands(BasicSelenium):
    def verifywebelementcommands(self):
        self.browser.get("https://selenium.qabible.in/simple-form-demo.php")
        message=self.browser.find_element(By.XPATH,"//input[@id='single-input-field']")
        message.send_keys("hello")
        time.sleep(5)
        showmessage=self.browser.find_element(By.XPATH,"//button[@id='button-one']")
        showmessage.click() #command used how to click an element
        yourmessage=self.browser.find_element(By.XPATH,"//div[@id='message-one']")
        print(yourmessage.text)
        print(yourmessage.is_displayed())
        print(yourmessage.is_enabled())
        time.sleep(5)
HandleWebElementCommand=HandleWebElementCommands()
HandleWebElementCommand.accessbrowser()
HandleWebElementCommand.verifywebelementcommands()



