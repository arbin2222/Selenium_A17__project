from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from time import sleep

import pytest
from time import sleep


@pytest.fixture(scope='module',params=[1,2,3])
def setup(request):
    a = request.param
    if a==1:
        driver=Chrome()

    elif a==2:
        driver=Edge()

    elif a==3:
        driver=Firefox()

    driver.get("https://demowebshop.tricentis.com/")
    sleep(3)
    yield driver
    driver.close()


####################################################################################

'''
def test_click_reg(setup):
       setup.find_element("xpath","//a[text()='Register']").click()
       sleep(4)'''

# collected 3 items
#
# test_cbt.py::test_click_reg[1] PASSED
# test_cbt.py::test_click_reg[2] PASSED
# test_cbt.py::test_click_reg[3] PASSED
#
# ===================================== 3 passed in 49.46s ====================================




#####################################################################################







class TestReg:
    def test_click_reg(self,setup):
       setup.find_element("xpath","//a[text()='Register']").click()
       sleep(3)


    def test_click_radio(self,setup):
        setup.find_element("id","gender-female").click()


    def test_first_name(self,setup):
        setup.find_element("id","FirstName").send_keys("keerthana")


    def test_last_name(self,setup):
        setup.find_element("id","LastName").send_keys("S")


    def test_email(self,setup):
        setup.find_element("id","Email").send_keys("keethanass@gmail.com")


    def test_pwd(self,setup):
        setup.find_element("id","Password").send_keys(123456)


    def test_confirm_pwd(self,setup):
        setup.find_element("id","ConfirmPassword").send_keys(123456)


    def test_click_reg_btn(self,setup):
        setup.find_element("id","register-button").click()
        sleep(3)











class TestLogin:
    def test_click_login(self,setup):
        setup.find_element("xpath","//a[text()='Log in']").click()
        sleep(3)

    def test_email(self,setup):
        setup.find_element("id","Email").send_keys("keethanass@gmail.com")


    def test_enter_pwd(self,setup):
        setup.find_element("id","Password").send_keys(123456)


    def test_click_log_btn(self,setup):
        setup.find_element("xpath","//input[@value='Log in']").click()
        sleep(3)



