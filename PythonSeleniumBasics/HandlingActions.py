import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingActions(BasicSelenium):
    def verifyactions(self):
        inputform=self.browser.find_element(By.XPATH,"//a[@href='simple-form-demo.php']")
        actions=ActionChains(self.browser)
        #actions.context_click(inputform).perform() #for right click
        actions.move_to_element(inputform).perform() #for mouse hovering
        time.sleep(5)
    def draganddrop(self):
        self.browser.get("https://selenium.qabible.in/drag-drop.php")
        dragdrop=self.browser.find_element(By.XPATH,"//span[text()='Draggable n°2']")
        draggable=self.browser.find_element(By.XPATH,"//div[@id='mydropzone']")
        actions=ActionChains(self.browser)
        actions.drag_and_drop(dragdrop,draggable).perform()
        time.sleep(5)

handlingactions=HandlingActions()
handlingactions.accessbrowser()
#handlingactions.verifyactions()
handlingactions.draganddrop()