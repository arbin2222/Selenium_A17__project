class Login_Page:
    log="xpath","//a[text()='Log in']"
    email="id","Email"
    pwd="id","Password"
    log_btn="xpath","//input[@value='Log in']"

    def __init__(self,driver):
        self.driver=driver

    def click_login(self):
        self.driver.find_element(*Login_Page.log).click()



    def enter_email(self):
        self.driver.find_element(*Login_Page.email).send_keys("arbintaj125@gmail.com")


    def enter_pwd(self):
        self.driver.find_element(*Login_Page.pwd).send_keys("Arbin@2005")


    def click_log_btn(self):
        self.driver.find_element(*Login_Page.log_btn).click()





















# ob=LoginPage()
# ob.click_login()
# ob1=LoginPage()
# ob1.click_login()
# ob2=LoginPage()
# ob2.click_login()
# ob3=LoginPage()
# ob3.click_login()


