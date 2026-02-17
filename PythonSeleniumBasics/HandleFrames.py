import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandleFrames(BasicSelenium):
    def verifyframes(self):
        self.browser.get("https://demoqa.com/frames")
        frame1 = self.browser.find_element(By.XPATH, "//iframe[@id='frame1']")
        time.sleep(5)
        totalframes=len(self.browser.find_elements(By.TAG_NAME,"iframe"))
        print(totalframes)
        self.browser.switch_to.frame(frame1) #switch() used to switch the focus of driver into a frame or tab
        frame=self.browser.find_element(By.XPATH, "//h1[text()='This is a sample page']")
        print(frame.text)
        self.browser.switch_to.default_content() #to release the focus from the frames

HandleFrames=HandleFrames()
HandleFrames.accessbrowser()
HandleFrames.verifyframes()

