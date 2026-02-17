import time

from selenium.webdriver.common.by import By

from basics.PythonSeleniumBasics.BasicSelenium import BasicSelenium


class HandlingTables(BasicSelenium):
    def verifytables(self):
        self.browser.get("https://selenium.qabible.in/table-pagination.php")
        selecttable=self.browser.find_element(By.XPATH,"//table[@id='dtBasicExample']/tbody/tr[1]")
        print(selecttable.text)
        column=self.browser.find_element(By.XPATH,"//table[@id='dtBasicExample']/tbody/tr[1]/td[3]")
        print(column.text)
        time.sleep(5)

handlingtables=HandlingTables()
handlingtables.accessbrowser()
handlingtables.verifytables()

