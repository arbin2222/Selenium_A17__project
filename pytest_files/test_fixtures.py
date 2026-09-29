# def login():
#     print("launch browser")
import pytest


# A B C D-----> users
# A -----> upload post in insta
# B -----> scroll reels in insta
# C ----> chat in insta
# D ---->  upload story in insta


#
# def A():
#     print("open insta")             #pre task          #setup operation
#     print("login insta")             #pre task         #setup op
#     print("upload post")               #main task
#     print("logout\n")                 #post task          #teardown operation
#
#
#
# def B():
#     print("open insta")
#     print("login insta")
#     print("scroll reels")              #main task
#     print("logout\n")
#
#
#
#
# def C():
#     print("open insta")
#     print("login insta")
#     print("chat")
#     print("logout\n")
#
#
#
#
# def D():
#     print("open insta")
#     print("login insta")
#     print("upload story")
#     print("logout")



#
# A()
# B()
# C()
# D()






#
# def func():
#     print("open insta")
#     print("login insta")
#     print("Logout insta")
#
#
#
#
# def A():
#     print("upload post")
#
#
# def B():
#     print("scroll reels")
#
#
# def C():
#     print("chatting")
#
#
# def D():
#     print("upload story")







# ##################################################################################
# fixtures:- used to perform setup and teardown operation
# it is a kind of decorator, it will execute before and after each test_func/module/class

# syntax:-

'''@pytest.fixture
def fixture_func():
    setup 
    yield
    teardown 
    


def test_func(fixture_func):
    pass                #maintask

def test_func1(fixture_func):
    pass                  #maintask


def test_func2(fixture_func):
    pass    '''               #maintask







'''
@pytest.fixture()
def insta():
    print("open insta")
    print("login insta")
    yield
    print("logout insta")



def test_A(insta):
    print("upload post")


def test_B(insta):
    print("scroll reels")


def test_C(insta):
    print("chatting")



def test_D(insta):
    print("upload story")

'''




# collected 4 items
#
# test_fixtures.py::test_A open insta
# login insta
# upload post
# PASSEDlogout insta
#
# test_fixtures.py::test_B open insta
# login insta
# scroll reels
# PASSEDlogout insta
#
# test_fixtures.py::test_C open insta
# login insta
# chatting
# PASSEDlogout insta
#
# test_fixtures.py::test_D open insta
# login insta
# upload story
# PASSEDlogout insta






# test functions performs main task
# fixture func performs set(pre task) and teardown(post task)




'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")



def test_sample(greet):
    print("login executing")'''



# collected 1 item
#
# test_fixtures.py::test_sample good morning
# login executing
# PASSEDgood night







'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_login(greet):
    print("login executing")

def test_logout(greet):
    print("logout executing")'''





# collected 2 items
#
# test_fixtures.py::test_login good morning
# login executing
# PASSEDgood night
#
# test_fixtures.py::test_logout good morning
# logout executing
# PASSEDgood night




'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg():
    print("register executing")'''



# note:- in the above example..in test_reg() we are not passing fixture
# so fixture will not be applied to tht test function


# collected 1 item
#
# test_fixtures.py::test_reg register executing
# PASSED






'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg(greet):
    print("register executing")'''



# collected 1 item
#
# test_fixtures.py::test_reg good morning
# register executing
# PASSEDgood night





'''

@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg(greet):
    print("register executing")


def test_sample():
    print("sample executing")



def test_logout(greet):
    print("logout executing")'''



# collected 3 items
#
# test_fixtures.py::test_reg good morning
# register executing
# PASSEDgood night
#
# test_fixtures.py::test_sample sample executing
# PASSED
# test_fixtures.py::test_logout good morning
# logout executing
# PASSEDgood night















'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg():
    print("register executing")


def test_sample():
    print("sample executing")



def test_logout(greet):
    print("logout executing")'''


# collected 3 items
#
# test_fixtures.py::test_reg register executing
# PASSED
# test_fixtures.py::test_sample sample executing
# PASSED
# test_fixtures.py::test_logout good morning
# logout executing
# PASSEDgood night












'''@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg():
    print("register executing")


def test_sample():
    print("sample executing")'''


# collected 2 items
#
# test_fixtures.py::test_reg register executing
# PASSED
# test_fixtures.py::test_sample sample executing
# PASSED


'''
@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


def test_reg(greet):
    print("register executing")'''


#
# collected 1 item
#
# test_fixtures.py::test_reg good morning
# register executing
# PASSEDgood night







'''
@pytest.fixture()
def greet():
    print("good morning")
    yield
    print("good night")


@pytest.fixture()
def sample():
    print("hi")
    yield
    print('bye')


def test_reg(greet):
    print("register executing")


def test_user(sample):
    print("User")'''




# collected 2 items
#
# test_fixtures.py::test_reg good morning
# register executing
# PASSEDgood night
#
# test_fixtures.py::test_user hi
# User
# PASSEDbye





'''
@pytest.fixture()
def greet():
    print("gm")
    yield
    print("gn")


def test_sample(greet):
    print("ga")'''






'''
@pytest.fixture()
def greet():
    print("gm")
    yield
    print("gn")


def test_sample(greet):
    print("ga")


def test_login(greet):
    print("login executing")

def test_logout(greet):
    print("logout executing")'''



# collected 3 items
#
# test_fixtures.py::test_sample gm
# ga
# PASSEDgn
#
# test_fixtures.py::test_login gm
# login executing
# PASSEDgn
#
# test_fixtures.py::test_logout gm
# logout executing
# PASSEDgn





















'''@pytest.fixture()
def greet():
    print("gm")
    yield
    print("gn")


def test_sample(greet):
    print("ga")


def test_login(greet):
    print("login executing")

def test_logout():
    print("logout executing")
    '''


# collected 3 items
#
# test_fixtures.py::test_sample gm
# ga
# PASSEDgn
#
# test_fixtures.py::test_login gm
# login executing
# PASSEDgn
#
# test_fixtures.py::test_logout logout executing
# PASSED






'''@pytest.fixture()
def greet():
    print("gm")



def test_sample(greet):
    print("ga")'''


# collected 1 item
#
# test_fixtures.py::test_sample gm
# ga
# PASSED




'''@pytest.fixture()
def greet():
    print("gm")



def test_sample(greet):
    print("ga")

def test_login(greet):
    print("login exe")


def test_logout(greet):
    print("logout exe")'''


# collected 3 items
#
# test_fixtures.py::test_sample gm
# ga
# PASSED
# test_fixtures.py::test_login gm
# login exe
# PASSED
# test_fixtures.py::test_logout gm
# logout exe
# PASSED












'''@pytest.fixture()
def greet():
    print("gm")


@pytest.fixture()
def main():
    print("hey")
    yield
    print("bye")


def test_sample(greet):
    print("ga")


def test_login(main):
    print("login exe")


def test_logout(greet):
    print("logout exe")'''



# collected 3 items
#
# test_fixtures.py::test_sample gm
# ga
# PASSED
# test_fixtures.py::test_login hey
# login exe
# PASSEDbye
#
# test_fixtures.py::test_logout gm
# logout exe
# PASSED







'''@pytest.fixture()
def greet():
    print("gm")
    print("hi")
    print("hey")
    print("👋🏻👋🏻")


def test_sample(greet):
    print("ga")'''




# collected 1 item
#
# test_fixtures.py::test_sample gm
# hi
# hey
# 👋🏻👋🏻
# ga
# PASSED






'''@pytest.fixture()
def greet():
    yield
    print("gn")


def test_sample(greet):
    print("ga")'''



# collected 1 item
#
# test_fixtures.py::test_sample ga
# PASSEDgn


'''
@pytest.fixture()
def greet():
    yield
    print("gn")


def test_sample(greet):
    print("ga")


def test_signin(greet):
    print("signin exe")'''



# collected 2 items
#
# test_fixtures.py::test_sample ga
# PASSEDgn
#
# test_fixtures.py::test_signin signin exe
# PASSEDgn







# if we want to apply fixtures to test function then we have to pass fixture func name as an argument in test_func
# if we dont provide fixture func as an argument in test_func then fixture will ot be wpplied to that particular test_func
# if we are having multiple test functions then we have to pass fixture func in every test_func
# so to overcome this drawback we have to pass "autouse=True" as an argument in fixture itself
# if we pass "autouse=True" as an argument in fixture then automatically the fixture will be applied to all test_func




'''
@pytest.fixture(autouse=True)
def greet():
    print("gm")
    yield
    print("gn")


def test_sample():
    print("ga")


def test_signin():
    print("signin exe")'''


# collected 2 items
#
# test_fixtures.py::test_sample gm
# ga
# PASSEDgn
#
# test_fixtures.py::test_signin gm
# signin exe
# PASSEDgn




'''

@pytest.fixture(autouse=True)
def greet():
    print("gm")
    yield
    print("gn")


class TestSample:
    def test_login(self):
        print("login executing")

    def test_logout(self):
        print("logout executing")
'''


# collected 2 items
#
# test_fixtures.py::TestSample::test_login gm
# login executing
# PASSEDgn
#
# test_fixtures.py::TestSample::test_logout gm
# logout executing
# PASSEDgn




# scope of fixtures:
# 1. functional scope ----> fixture will be applied to individual test_func
# 2. class scope   ---> fixture will be applied to individual class
# 3. module scope  ---> fixture will be applied to individual module




'''
@pytest.fixture(autouse=True,scope="class")
def greet():
    print("gm")
    yield
    print("gn")


class TestSample:
    def test_login(self):
        print("login executing")

    def test_logout(self):
        print("logout executing")


    def test_signin(self):
        print("signin executing")

    def test_reg(self):
        print("register executing")

'''


# collected 4 items
#
# test_fixtures.py::TestSample::test_login gm
# login executing
# PASSED
# test_fixtures.py::TestSample::test_logout logout executing
# PASSED
# test_fixtures.py::TestSample::test_signin signin executing
# PASSED
# test_fixtures.py::TestSample::test_reg register executing
# PASSEDgn





'''
@pytest.fixture(scope="class")
def greet():
    print("gm")
    yield
    print("gn")


class TestSample:
    def test_login(self):
        print("login executing")

    def test_logout(self,greet):
        print("logout executing")

    def test_signin(self,greet):
        print("signin executing")


class TestSample1:
    def test_login1(self):
        print("log exe")

    def test_logout1(self):
        print("logout exe")

    def test_signin1(self):
        print("signin exe")'''



# collected 6 items
#
# test_fixtures.py::TestSample::test_login gm
# login executing
# PASSED
# test_fixtures.py::TestSample::test_logout logout executing
# PASSED
# test_fixtures.py::TestSample::test_signin signin executing
# PASSEDgn
#
# test_fixtures.py::TestSample1::test_login1 gm
# log exe
# PASSED
# test_fixtures.py::TestSample1::test_logout1 logout exe
# PASSED
# test_fixtures.py::TestSample1::test_signin1 signin exe
# PASSEDgn





'''@pytest.fixture(autouse=True)
def greet():
    print("gm")
    yield
    print("gn")


def test_login1():
    print("log exe")


def test_logout1():
    print("logout exe")


def test_signin1():
    print("signin exe")'''


# collected 3 items
#
# test_fixtures.py::test_login1 gm
# log exe
# PASSEDgn
#
# test_fixtures.py::test_logout1 gm
# logout exe
# PASSEDgn
#
# test_fixtures.py::test_signin1 gm
# signin exe
# PASSEDgn







'''@pytest.fixture(scope="function")
def greet():
    print("gm")
    yield
    print("gn")


def test_login1():
    print("log exe")


def test_logout1():
    print("logout exe")


def test_signin1():
    print("signin exe")'''



# collected 3 items
#
# test_fixtures.py::test_login1 log exe
# PASSED
# test_fixtures.py::test_logout1 logout exe
# PASSED
# test_fixtures.py::test_signin1 signin exe
# PASSED







'''
@pytest.fixture(autouse=True,scope="module")
def greet():
    print("gm")
    yield
    print("gn")


class TestSample:
    def test_login(self):
        print("login executing")

    def test_logout(self):
        print("logout executing")

    def test_signin(self):
        print("signin executing")


class TestSample1:
    def test_login1(self):
        print("log exe")

    def test_logout1(self):
        print("logout exe")

    def test_signin1(self):
        print("signin exe")
'''


# note:- if we are having multiple test functions in a class
# and if we are not not passing autouse=True and scope="class" in  fixture then to apply fixture  for that particualr class it is mandatory that any one  of the test fuc should be having fixture func as argument
