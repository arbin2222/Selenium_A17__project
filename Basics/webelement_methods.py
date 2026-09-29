#Webelement method:- to perform actions on web elements

#1.send_keys():- used to enter data in input fields
# syntax:- webelement.send_keys("value")


# 2.click():- used to perform click action
# syntax:- webelement.click()


from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome()
from time import sleep
driver.maximize_window()



# 3. submit():- used to submit the data which is entered
# syntax: webelement.submit()


'''driver.get("https://www.google.com/")
sleep(3)
a=driver.find_element("name","q")
a.send_keys("python selenium")
a.submit()
sleep(30)'''


'''driver.get("https://www.flipkart.com/")
sleep(3)
a=driver.find_element("name","q")
a.send_keys("iphone")
a.submit()
sleep(5)'''

# note: submit() will work only is <form> is present(whichver the element we are locating tht particular element should
# be of form tag)




# 4. clear():-
# to clear preexisiting text we use clear()
# syntax:- webelement.clear()


'''driver.get("https://demo.vtiger.com/vtigercrm/index.php")
sleep(15)
a=driver.find_element("id","username")
a.clear()
sleep(2)
a.send_keys("arbin")
b=driver.find_element("id","password")
b.clear()
sleep(2)
b.send_keys("384758")
sleep(4)'''



# 5. is_displayed():-
# used to check whthr the ele is present on the page or not
# it returns Boolean values(True or False)
# True------> if the ele is displayed
# false or error----> if the element is hidden
# syntax:- webelement.is_displayed()



'''driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
sleep(3)
a=driver.find_element("id","myDIV")
sleep(1)
print(a.is_displayed())'''


'''driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
sleep(2)
driver.find_element("xpath","//button[.='Toggle Hide and Show']").click()
sleep(2)
a=driver.find_element("id","myDIV")
sleep(1)
print(a.is_displayed())'''



'''driver.get("https://www.facebook.com/")
sleep(5)
a=driver.find_element("xpath","//a[text()='Find your account and log in.']")
sleep(3)
print(a.is_displayed())'''



'''
driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("xpath","//span[text()='Log in']").click()
sleep(3)
a=driver.find_element("xpath","//a[text()='Find your account and log in.']")
sleep(3)
print(a.is_displayed())'''




# 6. is_enabled():-
# used to check whthr the element is enabled or not
# returns boolean values:-
# True ------> element is enabled
# False----> element is disabled

# syntax:- webelement.is_enabled()



'''driver.get("https://the-internet.herokuapp.com/dynamic_controls")
sleep(3)
z=driver.find_element("xpath","//input[@type='text']")
sleep(6)
print(z.is_enabled())'''




'''driver.get("https://the-internet.herokuapp.com/dynamic_controls")
sleep(3)
driver.find_element("xpath","//button[text()='Enable']").click()
sleep(3)
z=driver.find_element("xpath","//input[@type='text']")
sleep(6)
print(z.is_enabled())'''




# 7. is_selected():-
# method checks whthr the selectable element(checkboxes,radio buttons,dropdowns) is selected or not
# returns boolean values:-
# True ------> element is selected
# False----> element is not selected

# syntax:- webelement.is_selected()


'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
a=driver.find_element("id","saturday")
print(a.is_selected())'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
a=driver.find_element("id","female")
a.click()
sleep(2)
print(a.is_selected())'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(5)
a=driver.find_element("xpath","//option[@value='india']")
sleep(2)
print(a.is_selected())'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(5) 
# manually selected india

a=driver.find_element("xpath","//option[@value='india']")
sleep(2)
print(a.is_selected())
'''





#8. text:
# it is a property used to get the visible text of an element
# syntax:- webelement.text
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
a=driver.find_element("id","alertBtn")
print(a.text)'''





'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
a=driver.find_element("xpath","//button[@name='start']")
print(a.text)'''



# 9. get_attribute():-
# used to get the value of attribute
# accepts one argument ------------> "attribute_name"
# syntax:- webelement.get_attribute("attribute_name")


'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
a=driver.find_element("xpath","//input[@placeholder='Enter Name']")
sleep(2)
print(a.get_attribute("id"))'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
a=driver.find_element("id","monday")
sleep(2)
print(a.get_attribute("value"))
sleep(2)'''



#10. size:
# used to fetch the size of an element
# it will return height and width in dictionary format
# syntax:- webelement.size


'''driver.get("https://www.instagram.com/")
sleep(3)
a=driver.find_element("name","email")
sleep(2)
print(a.size)'''



#10. location:
# used to fetch the position of an element
# it will returns value in x and y axis in dictionary format
# syntax:- webelement.location

'''driver.get("https://www.instagram.com/")
sleep(3)
a=driver.find_element("name","email")
sleep(2)
print(a.location)'''




#11. rect:
# used to fetch the position of an element
# it will returns height,width,x and y axis in dictionary format
# syntax:- webelement.rect

'''driver.get("https://www.instagram.com/")
sleep(3)
a=driver.find_element("name","email")
sleep(2)
print(a.rect)'''




























driver.quit()



























































driver.quit()