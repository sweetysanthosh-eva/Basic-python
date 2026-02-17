import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class Executor(BasicSelenium):
    def verify_javascript_executor(self):
        self.browser.get("https://selenium.qabible.in/simple-form-demo.php")
        # Locate the button with XPath
        show_message_button = self.browser.find_element(By.XPATH, "//button[@id='button-one']")

        # JavaScript Executor for clicking the button
        self.browser.execute_script("arguments[0].click();", show_message_button)

        # Scroll down by 200px
        self.browser.execute_script("window.scrollBy(0, 200);")
        # Scroll up by 350px
        self.browser.execute_script("window.scrollBy(0, -350);")

        # 4. Scroll to the end using `scrollTo()`
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

Executor= Executor()
Executor.accessbrowser()
Executor.verify_javascript_executor()

