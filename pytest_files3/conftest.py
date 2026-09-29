from selenium.webdriver import Chrome
from time import sleep
import pytest




@pytest.fixture(scope='module')
def demowebshop():
    driver=Chrome()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    sleep(3)
    yield driver
    driver.close()





#
# (.venv) PS C:\Users\Levono\PycharmProjects\Selenium_A17\pytest_files3> pytest -vs
# ================================ test session starts ================================
# platform win32 -- Python 3.13.9, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Levono\PycharmProjects\Selenium_A17\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Levono\PycharmProjects\Selenium_A17\pytest_files3
# plugins: order-1.5.0
# collected 12 items
#
# test_reg.py::TestReg::test_click_reg PASSED
# test_reg.py::TestReg::test_click_radio PASSED
# test_reg.py::TestReg::test_first_name PASSED
# test_reg.py::TestReg::test_last_name PASSED
# test_reg.py::TestReg::test_email PASSED
# test_reg.py::TestReg::test_pwd PASSED
# test_reg.py::TestReg::test_confirm_pwd PASSED
# test_reg.py::TestReg::test_click_reg_btn PASSED
# test_login.py::TestLogin::test_click_login PASSED
# test_login.py::TestLogin::test_email PASSED
# test_login.py::TestLogin::test_enter_pwd PASSED
# test_login.py::TestLogin::test_click_log_btn PASSED
#
# ================================ 12 passed in 35.41s ==============================