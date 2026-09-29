# SELENIUM QUESTIONS TO SOLVE:
#
# 1. https://testautomationpractice.blogspot.com/
# Select sunday checkbox. Before clicking it, check whether it is already selected
#
#
#
#
# 2. https://testing.qaautomationlabs.com/file-upload.php
#    Upload any file
#
#
#
# 3. https://testing.qaautomationlabs.com/dropdown.php
#       print all dropdown options from single select dropdown
#
#
#
#
# 4. Find all links in flipkart and print their text.
#
#
#
# 5. count total number of images present in
#    https://www.zomato.com/bangalore/delivery
#
#
#
#
# 6. Open a website(amazon) and verify that the title is correct.
#
#
#
#
#
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
#
# 8. https://practice.expandtesting.com/dynamic-loading/2
#      wait until hello world text appears
#            print the text(Hello World) after waiting
#
#
#
#
#
# 9. Open the SauceDemo website.
# https://www.saucedemo.com/
#
# Enter the valid username: standard_user
# Enter the valid password: secret_sauce
# Click the Login button.
# After clicking Login, the URL will change to the inventory page.
# Use Explicit Wait to wait until the URL contains inventory.
# After the URL contains inventory, print Login successful.
#
#
#
#
#
#
#
#
# using traversing:-
# 10. search for any product in flipkart
# fetch that product's  ram storage in flipkart
#
#
#
#
#
#
#
#
#
#
# 11.	Open nyka
# https://www.nykaa.com/
# search for dot and key sunscreen
# hover on preview size
# click on preview size
# click on view details
# next tab will get opened in that tab click on add to bag
#
#
#
#
#
#
#
#
#
#
#
#
# 12. https://practice.expandtesting.com/js-dialogs
#
# Question
# Click the button that opens the prompt popup.
# Enter your name into the popup.
# Click OK.
# Print the message displayed on the webpage.
#
#
#
#
#
#
#
#
#
#
#
#
#
# 13. Write all the methods and properties in select class
#
#
# 14. who introduced selenium and when it was introduced
#
#
#
# 15. list out all components of selenium
#
#
# 16. list out all locators in selenium.
# Which locator is having the highest priority
#
#
#
#
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


# 1. https://testautomationpractice.blogspot.com/
# # Select sunday checkbox. Before clicking it, check whether it is already selected
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(5)
a=driver.find_element("id","sunday")

assert a.is_selected(),a.click()
print("Already selected")'''




# 2. https://testing.qaautomationlabs.com/file-upload.php
#    Upload any file

'''path="C:\\Users\\Levono\\OneDrive\\Desktop\\06_Slicing.pdf"
driver.get("https://testing.qaautomationlabs.com/file-upload.php")
sleep(4)
driver.find_element("xpath","//input[@id='fileInput']").send_keys(path)
sleep(4)'''




# 3.https://testing.qaautomationlabs.com/dropdown.php
# #       print all dropdown options from single select dropdown

'''from selenium.webdriver.support.select import Select

driver.get("https://testing.qaautomationlabs.com/dropdown.php")
sleep(7)
a=driver.find_element("id","fruitDropdown")
s=Select(a)
b=s.options
for i in b:
    print(i.text)'''



# 4. Find all links in flipkart and print their text.

'''driver.get("https://www.flipkart.com/")
sleep(4)
a=driver.find_elements("tag name","a")
for i in a:
    print(i.text)'''



# 5. count total number of images present in
#    https://www.zomato.com/bangalore/delivery

'''driver.get("https://www.zomato.com/bangalore/delivery")
sleep(4)
a=driver.find_elements("tag name","img")       #a=['web1','web2',......]
print(len(a))'''


#  6. Open a website(amazon) and verify that the title is correct
'''driver.get("https://www.amazon.in/")
sleep(6)
expected_title='Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
assert driver.title==expected_title,"Wrong page"
print("correct page opened")'''





#
# 8. https://practice.expandtesting.com/dynamic-loading/2
#      wait until hello world text appears
#            print the text(Hello World) after waiting


'''driver.implicitly_wait(100)
driver.get("https://practice.expandtesting.com/dynamic-loading/2")
driver.find_element("xpath","//button[text()='Start']").click()
a=driver.find_element("xpath","//h4[text()='Hello World!']")
print(a.text)'''





# 9. Open the SauceDemo website.
# https://www.saucedemo.com/
#
# Enter the valid username: standard_user
# Enter the valid password: secret_sauce
# Click the Login button.
# After clicking Login, the URL will change to the inventory page.
# Use Explicit Wait to wait until the URL contains inventory.
# After the URL contains inventory, print Login successful.


'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://www.saucedemo.com/")
sleep(4)
driver.find_element("id","user-name").send_keys("standard_user")
driver.find_element("id","password").send_keys("secret_sauce")
driver.find_element("id","login-button").click()
url='https://www.saucedemo.com/inventory.html'
a=WebDriverWait(driver,100)
a.until(EC.url_to_be(url))
sleep(5)'''




# using traversing:-
# 10. search for any product in flipkart
# fetch that product's  ram storage in flipkart
'''
driver.get("https://www.flipkart.com/")
sleep(4)
a=driver.find_element("name","q")
a.send_keys("iphone")
a.submit()
sleep(3)
a=driver.find_element("xpath","//div[text()='Apple iPhone 15 (Black, 128 GB)']/..//li[@class='DTBslk']")
print(a.text)'''







# 11.	Open nyka
# https://www.nykaa.com/
# search for dot and key sunscreen
# hover on preview size
# click on preview size
# click on view details
# next tab will get opened in that tab click on add to bag


'''driver.get("https://www.nykaa.com/")
sleep(4)
a=driver.find_element("xpath","search-suggestions-nykaa")
a.send_keys("dot and key sunscreen")
a.submit()
sleep(3)

from selenium.webdriver.common.action_chains import ActionChains
ac=ActionChains(driver)
b=driver.find_element("xpath","//div[@class='css-i9shm8']")
ac.move_to_element(b).perform()
sleep(2)

driver.find_element("xpath","//button[text()='Preview Size']").click()
sleep(2)
driver.find_element("xpath","//div[text()='View Details']").click()

a=driver.window_handles
driver.switch_to.window(a[1])
sleep(3)
driver.find_element("xpath","//span[text()='Add to Bag']").click()

sleep(5)
'''





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













driver.quit()