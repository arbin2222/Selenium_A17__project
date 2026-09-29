#pytest:- it is a unit testing framework
# used to execute the methods automatically
# can group testfunc



################################################################################################################

'''def login():
    print("login executing")


def logout():
    print("logout executing")



login()
logout()'''






'''class Sample:
    def login(self):
        print("login executing")

    def logout(self):
        print("logout executing")

ob=Sample()
ob.login()
ob.logout()'''




#####################################################################################################
# rules of pytest:
# 1. filename should always start with test_  or can end with _test
#      ex:- test_filename.py       or         filename_test.py

# 2. func/method name should always start with test_
#        ex:-    def test_functionname():


# 3. classname should always start with Test
#            ex:-  class TestSample:



# Note:- pytest will automatically recognize the files,func/methods or classes which are following
# pytest rules


# pytest test_basics.py -vs
# to execute pytest files or classes or methods   we have to type the below command in terminal
# pytest test_filename.py -vs
# v ----> verbosity   ----> prints whthr the test fun passed or failed
# s ----> scripting    ---> prints all the print statements


# to execute/run pytest code follow the below steps:
# 1. right click -----> click on open in -----> click on terminal ----> in terminal type command ----> pytest test_filename.py -vs




import pytest



'''def test_login():
    print("login executing")'''



# pytest test_basics.py -vs
# collected 1 item
#
# test_basics.py::test_login login executing
# PASSED





'''def test_login():
    print("login executing")

def logout():
    print("logout executing")'''


# note:- logout() is not following pytest rules so pytest will not recognise logout()...logout() will not be executed


#
# collected 1 item
#
# test_basics.py::test_login login executing
# PASSED







'''
def test_login():
    print("login executing")

def test_logout():
    print("logout executing")'''

# collected 2 items
#
# test_basics.py::test_login login executing
# PASSED
# test_basics.py::test_logout logout executing
# PASSED













'''def test_login():
    print("login executing")

def test_logout():
    print("logout executing")

def signin():
    print("signin executing")'''


# collected 2 items
#
# test_basics.py::test_login login executing
# PASSED
# test_basics.py::test_logout logout executing
# PASSED




'''
def test_login():
    print("login executing")

def test_logout():
    print("logout executing")

def test_signin():
    print("signin executing")

test_login()
test_logout()
test_signin()'''



# if we rae using pytest then we need not to call the methods separately...if we call then test fuctions will be executed for two times

#  login executing
# logout executing
# signin executing
# collected 3 items
#
# test_basics.py::test_login login executing
# PASSED
# test_basics.py::test_logout logout executing
# PASSED
# test_basics.py::test_signin signin executing
# PASSED









'''def test_reg():
    print("register executing")

def test_login():
    print("login executing")
    def test_logout():
        print("logout executing")'''



# incase of nested functions pytest recognizes only outer function...inner function will not be recognized


# collected 2 items
#
# test_basics.py::test_reg register executing
# PASSED
# test_basics.py::test_login login executing
# PASSED









'''class Sample:
    def test_reg(self):
        print("reg executing")

    def test_logout(self):
        print("logout executing")'''


# it will not recognize class because class is not following rules
# collected 0 items




'''class TestSample:
    def test_reg(self):
        print("reg executing")

    def test_logout(self):
        print("logout executing")'''


# collected 2 items
#
# test_basics.py::TestSample::test_reg reg executing
# PASSED
# test_basics.py::TestSample::test_logout logout executing
# PASSED







'''class TestSample:
    def test_reg(self):
        print("reg executing")

    def logout(self):
        print("logout executing")'''

# collected 1 item
#
# test_basics.py::TestSample::test_reg reg executing
# PASSED




'''def test_login():
    print("login executing")


def test_login():
    print("logout executing")'''



# if we are having the funcs with same name it will execute the latest one


# collected 1 item
#
# test_basics.py::test_login logout executing
# PASSED











'''class TestSample:
    def test_login(self):
        print("login executing")

    def test_login(self):
        print("logout executing")




class TestSample:
    def test_reg(self):
        print("reg executing")

    def test_reg(self):
        print("register executing")'''


# collected 1 item
#
# test_basics.py::TestSample::test_reg register executing
# PASSED












































