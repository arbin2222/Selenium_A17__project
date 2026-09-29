from time import sleep
import pytest


@pytest.mark.order(2)
class Test_Login:
    def test_click_log(self,sample):
        sample.find_element("xpath","//a[@class='poppins text-[12px] font-sans font-bold text-slate-500 relative top-3 hover:text-slate-700 cursor-pointer underline']").click()
        sleep(3)


    def test_enter_lemail(self,sample):
        sample.find_element("id","email").send_keys("arbin@gmail.com")
        sleep(2)

    def test_enter_log_pwd(self,sample):
        sample.find_element("id","password").send_keys("1234567")
        sleep(2)


    def test_click_log_btn(self,sample):
        sample.find_element("xpath","//button[text()='Login']").click()
        sleep(2)







# launch browser
# test reg
# test login
# close browser




