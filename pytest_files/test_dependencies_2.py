import pytest


'''class TestSample:
    @pytest.mark.dependency()
    def test_reg(self):
        print("login executing")


    @pytest.mark.dependency(depends=['test_reg'])
    def test_login(self):
        print("login executing")
'''

# pytest will look for test_reg in global area...as we do not have
# test_reg in global area thts the reason dependent test function will also nit get executed it will be skipped





'''@pytest.mark.dependency()
def test_reg():
    print("login executing")

class TestSample:
    @pytest.mark.dependency(depends=['test_reg'])
    def test_login(self):
        print("login executing")'''



# pytest test_dependencies_2.py -vs

#
# collected 2 items
#
# test_dependencies_2.py::test_reg login executing
# PASSED
# test_dependencies_2.py::TestSample::test_login login executing
# PASSED






'''
class TestSample:
    @pytest.mark.dependency()
    def test_reg(self):
        print("login executing")


    @pytest.mark.dependency(depends=['TestSample::test_reg'])
    def test_login(self):
        print("login executing")'''



#
# collected 2 items
#
# test_dependencies_2.py::TestSample::test_reg login executing
# PASSED
# test_dependencies_2.py::TestSample::test_login login executing
# PASSED






