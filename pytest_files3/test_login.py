import pytest
from time import sleep

@pytest.mark.order(2)
class TestLogin:
    def test_click_login(self,demowebshop):
        demowebshop.find_element("xpath","//a[text()='Log in']").click()
        sleep(3)

    def test_email(self,demowebshop):
        demowebshop.find_element("id","Email").send_keys("keethanass@gmail.com")


    def test_enter_pwd(self,demowebshop):
        demowebshop.find_element("id","Password").send_keys(123456)


    def test_click_log_btn(self,demowebshop):
        demowebshop.find_element("xpath","//input[@value='Log in']").click()
        sleep(3)


