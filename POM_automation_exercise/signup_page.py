from selenium.webdriver.support.select import Select

class signup:
    mrs="id","uniform-id_gender2"
    pwd="id","password"
    day="id","days"
    month="id", "months"
    year="id", "years"
    fname='xpath',"//input[@data-qa='first_name']"
    lname="xpath","//input[@data-qa='last_name']"
    address="xpath","//input[@data-qa='address']"
    country="id", "country"
    state="id","state"
    city="id","city"
    zipcode="xpath","//input[@data-qa='zipcode']"
    mob_no="xpath","//input[@data-qa='mobile_number']"
    create_acc="xpath","//button[@data-qa='create-account']"



    def __init__(self,driver):
        self.driver=driver


    def click_mrs(self):
        self.driver.find_element(*signup.mrs).click()


    def enter_pwd(self):
        self.driver.find_element(*signup.pwd).send_keys("123456")


    def select_day(self):
        a = self.driver.find_element(*signup.day)
        s = Select(a)
        s.select_by_visible_text("1")


    def select_month(self):
        a = self.driver.find_element(*signup.month)
        s = Select(a)
        s.select_by_visible_text("November")


    def select_year(self):
        a = self.driver.find_element(*signup.year)
        s = Select(a)
        s.select_by_visible_text("2000")



    def enter_fname(self):
        self.driver.find_element(*signup.fname).send_keys("tamil")


    def enter_lname(self):
        self.driver.find_element(*signup.lname).send_keys("arasan")


    def enter_address(self):
        self.driver.find_element(*signup.address).send_keys("chennai")



    def select_country(self):
        a = self.driver.find_element(*signup.country)
        s = Select(a)
        s.select_by_visible_text("India")


    def enter_state(self):
        self.driver.find_element(*signup.state).send_keys("tamil nadu")


    def enter_city(self):
        self.driver.find_element(*signup.city).send_keys("Chennai")



    def enter_zipcode(self):
        self.driver.find_element(*signup.zipcode).send_keys("560032")


    def enter_mob_no(self):
        self.driver.find_element(*signup.mob_no).send_keys('6789023416')



    def click_create_acc(self):
        self.driver.find_element(*signup.create_acc).click()
