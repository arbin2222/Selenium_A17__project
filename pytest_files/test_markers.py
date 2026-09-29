# markers:-
# used to mark/group testcases


# two types in markers:-
# 1. custom markers
# 2. inbuilt markers
#    in inbuilt markers we have:
# 1. skip     2.skipif    3.xfail     4.parametrize






# 1. custom markers:- these are the user defined markers
# syntax:- @pytest.mark.markername





# among all the test functions if i want to execute or test only test_login then we will mark it with marker
# and for the execution of tht particular marker type the command given below:-
# pytest test_filename.py -vs -m="markername"

import pytest


'''
def test_username():
    print("username executing")


def test_password():
    print("password executing")


@pytest.mark.sanity
def test_login():
    print("login executing")'''


# pytest test_markers.py -vs -m='sanity'

# collected 3 items / 2 deselected / 1 selected
#
# test_markers.py::test_login login executing
# PASSED







'''
def test_username():
    print("username executing")


@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.sanity
def test_login():
    print("login executing")'''


# pytest test_markers.py -vs -m='sanity'


# collected 3 items / 1 deselected / 2 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login login executing
# PASSED





'''
def test_username():
    print("username executing")


@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.regression
def test_logout():
    print("logout executing")'''


# pytest test_markers.py -vs -m='regression'
# collected 4 items / 3 deselected / 1 selected
#
# test_markers.py::test_logout logout executing
# PASSED



'''
@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")'''



# pytest test_markers.py -vs -m='regression'


# collected 4 items / 2 deselected / 2 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED








'''@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")'''


# pytest test_markers.py -vs -m='sanity'



# collected 4 items / 1 deselected / 3 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login login executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED







'''@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")'''


# pytest test_markers.py -vs -m='regression and sanity'
# note:- if i am using and operator both the markers should be present in one single test function then only it will execute tht particular test function




# collected 4 items / 2 deselected / 2 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED










'''@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")
'''

# pytest test_markers.py -vs -m='regression and smoke'


# collected 4 items / 4 deselected / 0 selected



'''

@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")'''

# pytest test_markers.py -vs -m='sanity and smoke'


# collected 4 items / 3 deselected / 1 selected
#
# test_markers.py::test_login login executing
# PASSED

















'''
@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")'''



# pytest test_markers.py -vs -m='sanity and regression'


# collected 4 items / 2 deselected / 2 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED












'''@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")


@pytest.mark.smoke
@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")
'''





# pytest test_markers.py -vs -m='sanity and sanity'


# collected 4 items / 1 deselected / 3 selected
#
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login login executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED









'''
@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")



@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")
'''


# pytest test_markers.py -vs -m='smoke or regression'


# collected 4 items / 1 deselected / 3 selected
#
# test_markers.py::test_username username executing
# PASSED
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED













'''
@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")



@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")
'''




# pytest test_markers.py -vs -m='smoke or sanity'


# collected 4 items
#
# test_markers.py::test_username username executing
# PASSED
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login login executing
# PASSED
# test_markers.py::test_logout logout executing
# PASSED







'''@pytest.mark.sanity
class TestSample:
    def test_password(self):
        print("password executing")

    def test_login(self):
        print("login executing")




class TestSample1:
    def test_password1(self):
        print("pass executing")

    def test_login1(self):
        print("log executing")'''




# pytest test_markers.py -vs -m='sanity'



# collected 4 items / 2 deselected / 2 selected
#
# test_markers.py::TestSample::test_password password executing
# PASSED
# test_markers.py::TestSample::test_login login executing
# PASSED








'''
@pytest.mark.smoke
def test_username():
    print("username executing")


@pytest.mark.regression
@pytest.mark.sanity
def test_password():
    print("password executing")



@pytest.mark.sanity
def test_login():
    print("login executing")


@pytest.mark.sanity
@pytest.mark.regression
def test_logout():
    print("logout executing")

'''

# pytest test_markers.py -vs -m='not sanity'


# collected 4 items / 3 deselected / 1 selected
#
# test_markers.py::test_username username executing
# PASSED







# 2. inbuilt markers:-


# 1. skip:-
# we use this marker on order to skip the execution of testcase

# syntax:-
# @pytest.mark.skip
# def test_func():
#       pass






'''def test_username():
    print("username executing")



def test_password():
    print("password executing")



@pytest.mark.skip
def test_login():
    print("login executing")



def test_logout():
    print("logout executing")
'''


# pytest test_markers.py -vs

#
# collected 4 items
#
# test_markers.py::test_username username executing
# PASSED
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login SKIPPED (unconditional skip)
# test_markers.py::test_logout logout executing
# PASSED









'''@pytest.mark.skip
def test_username():
    print("username executing")


def test_password():
    print("password executing")


@pytest.mark.skip
def test_login():
    print("login executing")


def test_logout():
    print("logout executing")'''


# pytest test_markers.py -vs

# collected 4 items
#
# test_markers.py::test_username SKIPPED (unconditional skip)
# test_markers.py::test_password password executing
# PASSED
# test_markers.py::test_login SKIPPED (unconditional skip)
# test_markers.py::test_logout logout executing
# PASSED





'''@pytest.mark.skip
class TestSample:
    def test_login(self):
        print("login executing")

    def test_logout(self):
        print("logout executing")'''


# pytest test_markers.py -vs


# collected 2 items
#
# test_markers.py::TestSample::test_login SKIPPED (unconditional skip)
# test_markers.py::TestSample::test_logout SKIPPED (unconditional skip)






'''class TestSample:
    def test_login(self):
        print("login executing")


    @pytest.mark.skip
    def test_logout(self):
        print("logout executing")'''

# pytest test_markers.py -vs


# pytest test_markers.py -rA


# collected 2 items
#
# test_markers.py::TestSample::test_login login executing
# PASSED
# test_markers.py::TestSample::test_logout SKIPPED (unconditional skip)







# 2. skipif:-
# it is also used to skip the execution of test function but the skip will happen based on a condition
# it takes 2 arguments:-
# 1st arg------> condition    (True or False)
#   if the condition is True it will skip the execution of test case
#   if the condition is false it  will execute the test function

# 2nd arg -----> reason for skipping

# condition is not mandatory but reason is mandatory


# syntax:- @pytest.mark.skipif(condition,reason)
#           def test_func():
#               pass




'''@pytest.mark.skipif(True,reason='login already done')
def test_login():
    print("login executing")'''



# collected 1 item
#
# test_markers.py::test_login SKIPPED (login already done)






'''@pytest.mark.skipif(False,reason='login already done')
def test_login():
    print("login executing")'''



# collected 1 item
#
# test_markers.py::test_login login executing
# PASSED






'''@pytest.mark.skipif(reason='login already done')
def test_login():
    print("login executing")'''



# if we dont provide condition then by default it will take the condition as True

#
# collected 1 item
#
# test_markers.py::test_login SKIPPED (login already done)





'''@pytest.mark.skipif(False)
def test_login():
    print("login executing")
'''
# Error


'''@pytest.mark.skipif(True)
def test_login():
    print("login executing")'''
# Error






##########################################################################################


'''
@pytest.mark.skipif(9>2,reason='login already done')
def test_login():
    print("login executing")'''



# collected 1 item
#
# test_markers.py::test_login SKIPPED (login already done)






'''def test_login():
    pt("login executing")'''


# collected 1 item
#
# test_markers.py::test_login FAILED




'''def test_login():
    raise Exception'''

# collected 1 item
#
# test_markers.py::test_login FAILED






'''def test_logout():
    p("logout exe")'''

# collected 1 item
#
# test_markers.py::test_logout FAILED





# 3. xfail:-
# this is an expected failure
#



'''
def test_username():
    print("login executing")


def test_pwd():
    print("password executing")


@pytest.mark.xfail
def test_login():
    raise Exception'''



#
# collected 3 items
#
# test_markers.py::test_username login executing
# PASSED
# test_markers.py::test_pwd password executing
# PASSED
# test_markers.py::test_login XFAIL



'''
@pytest.mark.xfail
def test_username():
    pt("login executing")


def test_pwd():
    print("password executing")



def test_login():
    raise Exception'''



# collected 3 items
#
# test_markers.py::test_username XFAIL
# test_markers.py::test_pwd password executing
# PASSED
# test_markers.py::test_login FAILED



'''
@pytest.mark.xfail
def test_username():
    print("login executing")   #XPASS    #XFAIL


def test_pwd():
    print("password executing")



def test_login():
    raise Exception'''




'''@pytest.mark.xfail
class TestSample:
    def test_username(self):
        print("login executing")

    def test_pwd(self):
        print("password executing")

    def test_login(self):
        raise Exception'''


# collected 3 items
#
# test_markers.py::TestSample::test_username login executing
# XPASS
# test_markers.py::TestSample::test_pwd password executing
# XPASS
# test_markers.py::TestSample::test_login XFAIL






'''
class TestSample:
    def test_username(self):
        print("login executing")

    def test_pwd(self):
        print("password executing")

    @pytest.mark.xfail
    def test_login(self):
        raise Exception'''


# collected 3 items
#
# test_markers.py::TestSample::test_username login executing
# PASSED
# test_markers.py::TestSample::test_pwd password executing
# PASSED
# test_markers.py::TestSample::test_login XFAIL




'''
class TestSample:
    def test_username(self):
        print("login executing")

    @pytest.mark.xfail
    def test_pwd(self):
        prt("password executing")



    @pytest.mark.xfail
    def test_login(self):
        print("login executing")


    def test_logout(self):
        raise Exception
    '''


# collected 4 items
#
# test_markers.py::TestSample::test_username login executing
# PASSED
# test_markers.py::TestSample::test_pwd XFAIL
# test_markers.py::TestSample::test_login login executing
# XPASS
# test_markers.py::TestSample::test_logout FAILED






# 4. parametrize:-
# execute  the test function with different inputs and mulitple times

# syntax:- @pytest.mark.parametrize("var1",[val1,val2,val3])

'''@pytest.mark.parametrize("a",['hi','hello','bye'])
def test_sample(a):
    print(a)'''



# collected 3 items
#
# test_markers.py::test_sample[hi] hi
# PASSED
# test_markers.py::test_sample[hello] hello
# PASSED
# test_markers.py::test_sample[bye] bye
# PASSED





'''@pytest.mark.parametrize("a,b",[(10,20),(30,10),(100,200)])
def test_sample(a,b):
    print(a+b)'''




# def test_add1():
#     a = 10
#     b = 20
#     print(a+b)
#
#
#
# def test_add2():
#     a = 30
#     b = 10
#     print(a+b)
#
#
#
# def test_add3():
#     a = 100
#     b = 200
#     print(a+b)








# collected 3 items
#
# test_markers.py::test_sample[10-20] 30
# PASSED
# test_markers.py::test_sample[30-10] 40
# PASSED
# test_markers.py::test_sample[100-200] 300
# PASSED




'''@pytest.mark.parametrize("a,b,c",[(1,2,10),(30,10,2),(100,200,2),(90,1,2),(1,4,0)])
def test_sample(a,b,c):
    print(a+b+c)'''

#
# collected 5 items
#
# test_markers.py::test_sample[1-2-10] 13
# PASSED
# test_markers.py::test_sample[30-10-2] 42
# PASSED
# test_markers.py::test_sample[100-200-2] 302
# PASSED
# test_markers.py::test_sample[90-1-2] 93
# PASSED
# test_markers.py::test_sample[1-4-0] 5
# PASSED




'''@pytest.mark.parametrize("a,b,c,d",[(1,2,10,3),(30,10,2,1),(100,200,1,2),(90,1,2,2),(1,4,0,2)])
def test_sample(a,b,c,d):
    print(a+b+c+d)'''


# 4th time ---> c?-->2
# 2nd  time ---> d? ----> 1
# last time ----> b? ---> 4
# first time ----> a? ---> 1





'''@pytest.mark.parametrize("a",['archana','neha','saqib','pavitra','bhagyashree','bishakha'])
def test_login(a):
    print(a)'''

#
# collected 6 items
#
# test_markers.py::test_login[archana] archana
# PASSED
# test_markers.py::test_login[neha] neha
# PASSED
# test_markers.py::test_login[saqib] saqib
# PASSED
# test_markers.py::test_login[pavitra] pavitra
# PASSED
# test_markers.py::test_login[bhagyashree] bhagyashree
# PASSED
# test_markers.py::test_login[bishakha] bishakha
# PASSED





'''@pytest.mark.parametrize("a,b",[('biryani',300),('pizza',200),('burger',150),('pancakes',180),('pasta',200)])
def test_login(a,b):
    print(f'the dish is {a} and price is {b}')
    '''



# collected 5 items
#
# test_markers.py::test_login[biryani-300] the dish is biryani and price is 300
# PASSED
# test_markers.py::test_login[pizza-200] the dish is pizza and price is 200
# PASSED
# test_markers.py::test_login[burger-150] the dish is burger and price is 150
# PASSED
# test_markers.py::test_login[pancakes-180] the dish is pancakes and price is 180
# PASSED
# test_markers.py::test_login[pasta-200] the dish is pasta and price is 200
# PASSED







'''from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep


@pytest.mark.parametrize("u,p",[('archana',1234),('bishakha',3456),('pavitra',7891),('saqib',1291),('bhagyashree',8129)])
def test_saucedemo(u,p):
    driver = Chrome(o)
    driver.maximize_window()
    sleep(2)
    driver.get("https://www.saucedemo.com/")
    sleep(4)
    driver.find_element("id","user-name").send_keys(u)
    driver.find_element("id","password").send_keys(p)
    sleep(2)
    driver.find_element("id","login-button").click()
    sleep(5)
    driver.quit()'''




# collected 5 items
#
# test_markers.py::test_saucedemo[archana-1234] PASSED
# test_markers.py::test_saucedemo[bishakha-3456] PASSED
# test_markers.py::test_saucedemo[pavitra-7891] PASSED
# test_markers.py::test_saucedemo[saqib-1291] PASSED
# test_markers.py::test_saucedemo[bhagyashree-8129] PASSED









'''
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep



@pytest.mark.parametrize("u,p",[('archana',123456),('bishakha',345699),('pavitra',789781),('saqib',121091),('bhagyashree',812599)])
def test_insta(u,p):
    driver=Chrome(o)
    driver.maximize_window()
    driver.get("https://www.instagram.com/")
    sleep(3)
    driver.find_element("name","email").send_keys(u)
    driver.find_element("name","pass").send_keys(p)
    sleep(2)
    driver.find_element("xpath","//span[text()='Log in']").click()
    sleep(3)
    driver.close()'''

# pytest test_markers.py -vs


# collected 5 items
#
# test_markers.py::test_insta[archana-123456] PASSED
# test_markers.py::test_insta[bishakha-345699] PASSED
# test_markers.py::test_insta[pavitra-789781] PASSED
# test_markers.py::test_insta[saqib-121091] PASSED
# test_markers.py::test_insta[bhagyashree-812599] PASSED
#
# ========================================= 5 passed in 71.93s (0:01:11) ==========================================








'''
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep




@pytest.mark.parametrize("u,p",[('archana',123456),('bishakha',345699),('pavitra',789781),('saqib',121091),('bhagyashree',812599)])
def test_insta(u,p):
    driver=Chrome(o)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    sleep(3)
    driver.find_element("name","email").send_keys(u)
    driver.find_element("name","pass").send_keys(p)
    sleep(2)
    driver.find_element("xpath","//span[text()='Log in']").click()
    sleep(3)
    driver.close()
    '''



#
# collected 5 items
#
# test_markers.py::test_insta[archana-123456] PASSED
# test_markers.py::test_insta[bishakha-345699] PASSED
# test_markers.py::test_insta[pavitra-789781] PASSED
# test_markers.py::test_insta[saqib-121091] PASSED
# test_markers.py::test_insta[bhagyashree-812599] PASSED
#
# ========================================= 5 passed in 70.48s (0:01:10) ==========================================
















# PARAMETRIZE AND DDT:-


from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep
from xlrd import *

wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
l=[]


def get_data():
    for i in range(1,sheet.nrows):
        rows=sheet.row_values(i,0,2)    #rows=[saqib,90811]
        u=rows[0]
        p=rows[1]
        l.append((u,p))
    return l



@pytest.mark.parametrize("u,p",get_data())
def test_insta(u,p):
    driver=Chrome(o)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    sleep(3)
    driver.find_element("name","email").send_keys(u)
    driver.find_element("name","pass").send_keys(p)
    sleep(2)
    driver.find_element("xpath","//span[text()='Log in']").click()
    sleep(3)
    driver.close()



####################################  WORKING #######################################################################################

# row_values(1,0,2)--->aditya
# row_values(2,0,2) ---> neha
# row_values(3,0,2)---> saqib
# row_values(4,0,2)----> smaila
# row_values(5,0,2)---> keerthana




# #1.
# l=[('aditya', 12345)]
#
# # 2.
# [('aditya', 12345),('neha',56789)]
#
#
# # 3.
# [('aditya', 12345),('neha',56789),('saqib',90811)]



##############################################################################################################################

# OUTPUT:-

#
# collected 9 items
#
# test_markers.py::test_insta[Aditya-1234.0] PASSED
# test_markers.py::test_insta[Neha -4567.0] PASSED
# test_markers.py::test_insta[Saqib-8901.0] PASSED
# test_markers.py::test_insta[Smaila-7892.0] PASSED
# test_markers.py::test_insta[keerthana-5643.0] PASSED
# test_markers.py::test_insta[surabhi-6782.0] PASSED
# test_markers.py::test_insta[pavithra-1799.0] PASSED
# test_markers.py::test_insta[kirti-7812.0] PASSED
# test_markers.py::test_insta[Logesh-1233.0] PASSED
#
# ========================================= 9 passed in 113.31s (0:01:53) ==========================================================









#####################################  PARAMETRIZE + DDT TASK ####################################################################


# Assignment 1---> Instagram

'''Create a separate Excel workbook named instagram.xlsx.(store some 5 or 6 username passwords not less than this)

Write a Pytest Selenium script that reads username and password from instagram.xlsx

Use @pytest.mark.parametrize to pass the username and password.

Open the Instagram website. (https://www.instagram.com/)

Enter the username and password.

Click on the log in button.'''





# Assignment 2---> Saucedemo
'''Create a separate Excel workbook named saucedemo.xlsx.(store some 5 or 6 username passwords not less than this)

Write a Pytest Selenium script that reads username and password from saucedemo.xlsx.

Use @pytest.mark.parametrize to pass the username and password.

Open the Saucedemo website. (https://www.saucedemo.com/)

Enter the username and password.

Click on the log in button.'''





