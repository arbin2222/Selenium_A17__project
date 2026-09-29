from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep

driver.get("https://www.saucedemo.com/")
sleep(4)


class Loginpage:

    un="id","user-name"
    pas="id","password"
    log="id","login-button"

    def __init__(self,driver):
        self.driver=driver

    def username(self):
        self.driver.find_element(*Loginpage.un).send_keys("standard_user")
        sleep(2)



    def pwd(self):
        self.driver.find_element(*Loginpage.pas).send_keys("secret_sauce")
        sleep(2)


    def log_btn(self):
        self.driver.find_element(*Loginpage.log).click()
        sleep(5)








ob=Loginpage(driver)
ob.username()
ob.pwd()
ob.log_btn()




driver.quit()









#
# (val1,val2,...........,valn)
#
# (val1,)
#
#
# val1,val2,val3,..................,valn



# a=1,2
# print(type(a))



# a=1,9,8,7


# a=('hi',)
# print(type(a))

