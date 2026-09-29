'''from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep
import pytest


@pytest.fixture(autouse=True,scope="class")
def sample():
    driver=Chrome(o)
    driver.get("https://demowebshop.tricentis.com/register")
    sleep(4)
    yield driver
    driver.close()






class Test_Register:
    def test_click_on_female(self,sample):
        sample.find_element("id","gender-female").click()


    def test_first_name(self,sample):
        sample.find_element("id","FirstName").send_keys("keerthana")

    def test_last_name(self,sample):
        sample.find_element("id","LastName").send_keys("S")

    def test_enter_email(self,sample):
        sample.find_element("id","Email").send_keys("keerthana@gmail.com")


    def test_pwd(self,sample):
        sample.find_element("id","Password").send_keys("1234567")

    def test_cpwd(self,sample):
        sample.find_element("id","ConfirmPassword").send_keys("1234567")


    def test_click_reg(self,sample):
        sample.find_element("id","register-button").click()



class Test_Login:
    def test_click_log(self,sample):
        sample.find_element("xpath","//a[text()='Log in']").click()

    def test_enter_lemail(self,sample):
        sample.find_element("id","Email").send_keys("keerthana@gmail.com")

    def test_enter_log_pwd(self,sample):
        sample.find_element("id","Password").send_keys("1234567")


    def test_click_log_btn(self,sample):
        sample.find_element("xpath","//input[@value='Log in']").click()







'''

# collected 11 items
#
# test_fixtures_example.py::Test_Register::test_click_on_female PASSED
# test_fixtures_example.py::Test_Register::test_first_name PASSED
# test_fixtures_example.py::Test_Register::test_last_name PASSED
# test_fixtures_example.py::Test_Register::test_enter_email PASSED
# test_fixtures_example.py::Test_Register::test_pwd PASSED
# test_fixtures_example.py::Test_Register::test_cpwd PASSED
# test_fixtures_example.py::Test_Register::test_click_reg PASSED
# test_fixtures_example.py::Test_Login::test_click_log PASSED
# test_fixtures_example.py::Test_Login::test_enter_lemail PASSED
# test_fixtures_example.py::Test_Login::test_enter_log_pwd PASSED
# test_fixtures_example.py::Test_Login::test_click_log_btn PASSED
#
# ========================================== 11 passed in 32.14s ===========================================














# class sample:
#     def disp(self,a,b):
#         print(a+b)
#
#     def disp2(self,c,d):
#         print(c-d)
#
#
# ob=sample()
# ob.disp(10,20)
# ob.disp2(30,20)











'''
class sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b


ob=sample(10,20)'''












# def disp():
#     s=10
#     return s



# disp() -----> 10

# print(disp())











# launch browser
# application
# register
# close
#
#
#
# launch browser
# application
# login
# close





####################################################################################################################
# example2:-


from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep
import pytest


@pytest.fixture(autouse=True,scope="class")
def sample():
    driver=Chrome(o)
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")
    sleep(4)
    yield driver
    driver.close()






class Test_Register:
    def test_enter_name(self,sample):
        sample.find_element("id","name").send_keys("arbin taj")


    def test_enter_email(self,sample):
        sample.find_element("id","email").send_keys("arbin@gmail.com")

    def test_pwd(self,sample):
        sample.find_element("id","password").send_keys("123456")



    def test_click_reg(self,sample):
        sample.find_element("xpath","//button[text()='Register']").click()



class Test_Login:
    def test_click_log(self,sample):
        sample.find_element("xpath","//a[@class='poppins text-[12px] font-sans font-bold text-slate-500 relative top-3 hover:text-slate-700 cursor-pointer underline']").click()
        sleep(4)

    def test_enter_lemail(self,sample):
        sample.find_element("id","email").send_keys("arbin@gmail.com")

    def test_enter_log_pwd(self,sample):
        sample.find_element("id","password").send_keys("1234567")


    def test_click_log_btn(self,sample):
        sample.find_element("xpath","//button[text()='Login']").click()


