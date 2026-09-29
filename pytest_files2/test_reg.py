import pytest

@pytest.mark.order(1)
class Test_Register:
    def test_enter_name(self,sample):
        sample.find_element("id","name").send_keys("arbin taj")


    def test_enter_email(self,sample):
        sample.find_element("id","email").send_keys("arbin@gmail.com")

    def test_pwd(self,sample):
        sample.find_element("id","password").send_keys("123456")



    def test_click_reg(self,sample):
        sample.find_element("xpath","//button[text()='Register']").click()

