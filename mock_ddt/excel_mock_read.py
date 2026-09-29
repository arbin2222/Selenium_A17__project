




# 7. DDT
# Open the SauceDemo website and try to log in using wrong username and password.
#
# Follow these steps:
#
# 1. Read the username and password from the Excel file.
# 2. Enter the username in the username field.
# 3. Enter the password in the password field.
# 4. Click the Login button.
# 5. An error message will be displayed because the credentials are incorrect.
# 6. Check whether the error message is displayed.
# 7. If the error message is displayed, take a screenshot.
# 8. Save each screenshot with a different name.
# 9. Repeat the same steps for all the username and password values available in the Excel file.
#
#
#
# Consider the below usernames and passwords:-
# Username    Password
# kavita      Kavita@123
# priya       Priya@456
# Sneha       Sneha@789
# Samreen     Samreen@321
# Unknown     unknown@654
#
#
#
#











#

from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep



from xlrd import  *
wb=open_workbook("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\mock_ddt\\excel_mock.xlsx")
sheet=wb.sheet_by_name("Sheet1")

for i in range(1,sheet.nrows):
    rows=sheet.row_values(i,0,2)     #['kavita','kavita@123']
    un=rows[0]
    pwd=rows[1]

    driver.get("https://www.saucedemo.com/")
    sleep(3)
    driver.find_element("id","user-name").send_keys(un)
    driver.find_element("id","password").send_keys(pwd)
    driver.find_element("id","login-button").click()
    sleep(4)

    error_msg=driver.find_element("xpath","//h3[@data-test='error']")
    assert error_msg.is_displayed(),"correct credentials"
    driver.save_screenshot(f'{i}.png')

    sleep(2)
    




driver.close()



























# a='saqib'
# b=10
#
#
# print(f"ur name is {a} and age is {b}")