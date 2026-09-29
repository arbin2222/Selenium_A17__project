# from selenium.webdriver import Chrome,ChromeOptions
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(o)
# from time import sleep
# driver.maximize_window()




# instagram's login page

# with valid username + valid pass
'''driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element("name","email").send_keys("8790657777")
sleep(2)
driver.find_element("name","pass").send_keys("1335623")
sleep(2)
driver.find_element("xpath","//span[text()='Log in']").click()
sleep(5)'''




# with invalid username and valid password
'''driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element("name","email").send_keys("             ")
sleep(2)
driver.find_element("name","pass").send_keys("1335623")
sleep(2)
driver.find_element("xpath","//span[text()='Log in']").click()
sleep(5)'''




#
'''driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element("name","email").send_keys()
sleep(2)
driver.find_element("name","pass").send_keys()
sleep(2)
driver.find_element("xpath","//span[text()='Log in']").click()
sleep(5)'''





# 500 scenarios




# reading the data from external files such as excel file and testing the
# application with multiple sets of inputs



# open_workbook(path):- to open excel file
# sheet_by_name():- to open sheets
# row_values():-
#           1st argument -----> row number( provide index of particular row)

# ex:- row_values(0)   ---> this fetches first row


#            2nd argument  ---> starting column from the specified row


#            3rd argument :-   ending column (excluded)


# 4. nrow:- gives the count of total number of rows present in sheet
# 5. ncols:- gives the count of total number of columns present in sheet




# steps:
# 1. open excel file
# 2. specify sheet name
# 3. specify row or column



from xlrd import *



'''# opening excel file
wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
# specify sheet name
sheet=wb.sheet_by_name("Sheet1")
# specify row or column
# fetching first row
a=sheet.row_values(0)
print(a)'''




# fetching last row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(9)
print(row)'''



# fetch 2nd row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(1)
print(row)'''

# fetch 5th row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(4)
print(row)'''

# fetch 8th row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(7)
print(row)'''

# fetch 4th row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(3)
print(row)'''

# fetch 9th row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(8)
print(row)'''





# fetch smaila's place,mob and pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(4,2)
print(row)'''



# fetch aditya's password, place,mob and pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(1,1)
print(row)'''




# fetch keerthana's mob and pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(5,3)
print(row)'''




# fetch neha's pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(2,4)
print(row)
'''



# fetch  saqib's place, mob no, pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(3,2)
print(row)'''




#fetch logesh's mob and pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(9,3)
print(row)'''



# fetch kirti's only pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(8,4)
print(row)'''


# fetch pavitra's place,mob no, pincode
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(7,2)
print(row)'''


# surabhi's pass,place,mob,pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(6,1)
print(row)'''

# neha's mob and pin
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(2,3)
print(row)'''




# surabhi's place and mob
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(6,2,4)
print(row)'''



# fetching password of saqib
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(3,1,2)
print(row)'''




# fetching mob and oin of logesh
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(9,3,5)
print(row)'''



# fetching mobile number of aditya
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
row=sheet.row_values(1,3,4)
print(row)'''



# counting number of rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
print(sheet.nrows)'''



# counting number of columns
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
print(sheet.ncols)'''




# fetching all rows and columns
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
print(sheet.row_values(0))
print(sheet.row_values(1))
print(sheet.row_values(2))
print(sheet.row_values(3))
print(sheet.row_values(4))
print(sheet.row_values(5))
print(sheet.row_values(6))
print(sheet.row_values(7))
print(sheet.row_values(8))
print(sheet.row_values(9))'''



'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(0,10):
    print(sheet.row_values(i))'''



# for 0 in range(0,10):
#     print(sheet.row_values(0))



# for 1 in range(0,10):
#     print(sheet.row_values(1))



# 0   ---> 1st row
# 1   ---> 2nd
# 2   ---> 3rd
# 3   ---> 4th row
# 4  ---> 5th row
# 5   ---> 6th row
# 6   --> 7th row
# 7  ---> 8th row
# 8   ---> 9th row
# 9   ---> 10th row
# 10  ---> extra index we have to provide






# fetching all usernames and passwords
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
print(sheet.row_values(0,0,2))
print(sheet.row_values(1,0,2))
print(sheet.row_values(2,0,2))
print(sheet.row_values(3,0,2))
print(sheet.row_values(4,0,2))
print(sheet.row_values(5,0,2))
print(sheet.row_values(6,0,2))
print(sheet.row_values(7,0,2))
print(sheet.row_values(8,0,2))
print(sheet.row_values(9,0,2))'''




'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(0,10):
    print(sheet.row_values(i,0,2))'''





# fetching everyone's place and mobile number
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(0,10):
    print(sheet.row_values(i,2,4))'''







# fetching pincode of everyone
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(10):
    print(sheet.row_values(i,4))'''




# fetching everyone's pincode
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(sheet.nrows):
    print(sheet.row_values(i,4))'''





# fetching everyone's username
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(sheet.nrows):
    print(sheet.row_values(i,0,1))  '''




# starting 5 rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(2):
    print(sheet.row_values(i))'''



# starting 5 rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(5):
    print(sheet.row_values(i))'''




# starting 8 rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(8):
    print(sheet.row_values(i))'''





# fetching 2nd and 3rd row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(1,3):
    print(sheet.row_values(i))'''




# fetching 3rd and 4th row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(2,4):
    print(sheet.row_values(i))'''





# fetching last two rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(8,10):
    print(sheet.row_values(i))'''





# fetch last 5 rows
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(5,10):
    print(sheet.row_values(i))'''




# fetch from smaila's row to kirti's row
'''wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(4,9):
    print(sheet.row_values(i))'''


'''
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
from time import sleep



wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\Data_Driven_Testing\\excel.xlsx")
sheet=wb.sheet_by_name("Sheet1")
for i in range(1,sheet.nrows):
    rows=sheet.row_values(i,0,2)        #rows=['aditya',1234]
    username=rows[0]
    password=rows[1]

    driver = Chrome(o)
    driver.maximize_window()

    driver.get("https://www.facebook.com/")
    sleep(4)
    driver.find_element("name","email").send_keys(username)
    sleep(1)
    driver.find_element("name","pass").send_keys(password)
    sleep(1)
    driver.find_element("xpath","//span[text()='Log in']").click()
    sleep(2)
    driver.close()

'''
# instagram

































