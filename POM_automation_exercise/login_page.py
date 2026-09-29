class login:
    r_name="xpath","//input[@data-qa='signup-name']"
    r_email="xpath","//input[@data-qa='signup-email']"
    r_signup="xpath","//button[@data-qa='signup-button']"
    l_email="xpath","//input[@data-qa='login-email']"
    l_pwd="xpath","//input[@data-qa='login-password']"
    login='xpath',"//button[@data-qa='login-button']"

    def __init__(self,driver):
        self.driver=driver

    def reg_name(self):
        self.driver.find_element(*login.r_name).send_keys("tamillllarasan")


    def reg_email(self):
        self.driver.find_element(*login.r_email).send_keys("tamillllarasan@gmail.com")



    def click_signup(self):
        self.driver.find_element(*login.r_signup).click()



    def login_email(self):
        self.driver.find_element(*login.l_email).send_keys("tamillllarasan@gmail.com")


    def login_pwd(self):
        self.driver.find_element(*login.l_pwd).send_keys("123456")


    def click_login(self):
        self.driver.find_element(*login.login).click()

