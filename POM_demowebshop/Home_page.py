from selenium.webdriver.common.action_chains import ActionChains


class Home_Page:
    computer="xpath","//a[contains(text(),'Computers')]"
    desktop="xpath","//a[contains(text(),'Desktops')]"

    def __init__(self,driver):
        self.driver=driver

    def hover_computer(self):
        a=self.driver.find_element(*Home_Page.computer)
        ac=ActionChains(self.driver)
        ac.move_to_element(a).perform()


    def click_desktops(self):
        self.driver.find_element(*Home_Page.desktop).click()





