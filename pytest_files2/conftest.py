# conftest.py
# it is a file whr we keep common fixtures shared across multiple files
# in conftest we keep fixture code that can be used by all the test files
# conftest.py will recognize all th test_files and fixture is applied to all test files
# the filename should must be conftest.py




from selenium.webdriver import Chrome
from time import sleep
import pytest



@pytest.fixture(scope='module')
def sample():
    driver=Chrome()
    driver.maximize_window()
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")
    sleep(3)
    yield driver
    driver.close()





#
#
# (.venv) PS C:\Users\Levono\PycharmProjects\Selenium_A17\pytest_files2> pytest -vs
# =========================================== test session starts ===========================================
# platform win32 -- Python 3.13.9, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\Levono\PycharmProjects\Selenium_A17\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\Levono\PycharmProjects\Selenium_A17\pytest_files2
# plugins: order-1.5.0
# collected 8 items
#
# test_reg.py::Test_Register::test_enter_name PASSED
# test_reg.py::Test_Register::test_enter_email PASSED
# test_reg.py::Test_Register::test_pwd PASSED
# test_reg.py::Test_Register::test_click_reg PASSED
# test_login.py::Test_Login::test_click_log PASSED
# test_login.py::Test_Login::test_enter_lemail PASSED
# test_login.py::Test_Login::test_enter_log_pwd PASSED
# test_login.py::Test_Login::test_click_log_btn PASSED
#
# =========================================== 8 passed in 23.52s ============================================
#
#



