class acc_created:
    continuee="xpath","//a[text()='Continue']"

    def __init__(self,driver):
        self.driver=driver


    def click_continue(self):
        self.driver.find_element(*acc_created.continuee).click()