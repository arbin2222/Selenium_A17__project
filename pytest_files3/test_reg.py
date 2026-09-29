import pytest
from time import sleep


@pytest.mark.order(1)
class TestReg:
    def test_click_reg(self,demowebshop):
        demowebshop.find_element("xpath","//a[text()='Register']").click()
        sleep(3)

    def test_click_radio(self,demowebshop):
        demowebshop.find_element("id","gender-female").click()

    def test_first_name(self,demowebshop):
        demowebshop.find_element("id","FirstName").send_keys("keerthana")


    def test_last_name(self,demowebshop):
        demowebshop.find_element("id","LastName").send_keys("S")


    def test_email(self,demowebshop):
        demowebshop.find_element("id","Email").send_keys("keethanass@gmail.com")


    def test_pwd(self,demowebshop):
        demowebshop.find_element("id","Password").send_keys(123456)


    def test_confirm_pwd(self,demowebshop):
        demowebshop.find_element("id","ConfirmPassword").send_keys(123456)


    def test_click_reg_btn(self,demowebshop):
        demowebshop.find_element("id","register-button").click()
        sleep(3)