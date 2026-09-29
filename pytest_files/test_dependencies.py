# we can create dependencies between test cases
# one test case can be dependent on other test case

# install-----> pytest-dependency

# syntax:-
# @pytest.mark.dependency()                 #independent
# def test_func1():
#     pass
#
# @pytest.mark.dependency(depends=['test_func1'])
# def test_func2():                                     #dependent
#     pass




# points to remember:
# 1. if the independent test case executes without any error, then dependent should also work without any error
# 2. if the independent test case is not working fine, thn dependent test case will be skipped




import pytest


'''@pytest.mark.dependency()
def test_reg():
    print("register executing")



@pytest.mark.dependency(depends=['test_reg'])
def test_login():
    print("login executing")'''




# pytest test_dependencies.py -vs

#
# collected 2 items
#
# test_dependencies.py::test_reg register executing
# PASSED
# test_dependencies.py::test_login login executing
# PASSED
#
# =========================================== 2 passed in 0.04s ===========================================
#





'''@pytest.mark.dependency()
def test_reg():
    prt("register executing")



@pytest.mark.dependency(depends=['test_reg'])
def test_login():
    print("login executing")'''



#
# collected 2 items
#
# test_dependencies.py::test_reg FAILED
# test_dependencies.py::test_login SKIPPED (test_login depends on test_reg)
#
# =============================================== FAILURES ================================================
# _______________________________________________ test_reg ________________________________________________
#
#     @pytest.mark.dependency()
#     def test_reg():
# >       prt("register executing")
#         ^^^
# E       NameError: name 'prt' is not defined
#
# test_dependencies.py:60: NameError
# ======================================== short test summary info ========================================
# FAILED test_dependencies.py::test_reg - NameError: name 'prt' is not defined
# ===================================== 1 failed, 1 skipped in 0.24s ======================================






