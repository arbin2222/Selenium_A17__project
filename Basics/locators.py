from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep





# ID Locator
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("id","name").send_keys("arbin taj")
driver.find_element("id","email").send_keys("arbin@gmail.com")
driver.find_element("id","phone").send_keys("1234567890")
driver.find_element("id","alertBtn").click()
sleep(4)'''


# https://www.pizzahut.co.in/account/otp


# https://demowebshop.tricentis.com/register
'''
driver.get("https://demowebshop.tricentis.com/register")
sleep(3)
driver.find_element("id","gender-female").click()
sleep(1)
driver.find_element("id","FirstName").send_keys("arbin")
sleep(1)
driver.find_element("id","LastName").send_keys("taj")
sleep(1)
driver.find_element("id","Email").send_keys("arbin@gmail.com")
sleep(1)
driver.find_element("id","Password").send_keys("123456")
sleep(1)
driver.find_element("id","ConfirmPassword").send_keys("123456")
sleep(1)
driver.find_element("id","register-button").click()
sleep(6)'''



# https://demoqa.com/automation-practice-form
# enter first name,last name,email,gender,mobile number



# name locator
'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
driver.find_element("name","name").send_keys("arbin taj")
driver.find_element("name","email").send_keys("arbin@gmail.com")
driver.find_element("name","password").send_keys("1234567")
sleep(5)'''




# https://www.saucedemo.com/
# enter name password




# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# enter name password






# class name:
# class attribute value
# whrever space is thr replace space with .

'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("class name","nav-input.nav-progressive-attribute").send_keys("iphone 17 pro")
sleep(4)'''





'''driver.get("https://www.flipkart.com/")
sleep(8)
driver.find_element("class name","b3wTlE").click()
sleep(4)'''


'''driver.get("https://www.flipkart.com/")
sleep(9)
driver.find_element("class name","nw1UBF.v1zwn25").send_keys("samsung s26 ultra")
sleep(4)'''



# https://www.myntra.com/
# enter some product

'''driver.get("https://www.myntra.com/")
sleep(4)
driver.find_element("class name","desktop-searchBar").send_keys("lakme lipstick")
sleep(4)
'''





# saucedemo
# https://www.saucedemo.com/
# enter username and password
'''driver.get("https://www.saucedemo.com/")
sleep(3)
driver.find_element("class name","input_error.form_input").send_keys("arbin")
sleep(2)
driver.find_element("class name","input_error.form_input").send_keys("734563")
sleep(4)'''





# tag name:-
# --->using thier html tags
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("tag name","input").send_keys("arbin")
sleep(1)
driver.find_element("tag name","input").send_keys(" LSIFBUIR")
sleep(4)'''



'''driver.get("https://www.saucedemo.com/")
sleep(4)
driver.find_element("tag name","input").send_keys("arbin")
sleep(2)
driver.find_element("tag name","input").send_keys("598678946")
sleep(2)
driver.find_element("tag name","input").click()
sleep(5)
'''



'''
driver.get("https://www.myntra.com/")
sleep(3)
driver.find_element("tag name","input").send_keys("Lehenga")
sleep(5)'''





'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
driver.find_element("tag name","input").send_keys("arbin")
driver.find_element("tag name","input").send_keys("arbin@gmail.com")
driver.find_element("tag name","input").send_keys("123456")
driver.find_element("tag name","button").click()
sleep(10)'''


'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
a=driver.find_element("tag name","input")
print(a)
'''


# find_element():-
# matching with 0 elements
'''driver.get("https://example.com/")
sleep(3)
a=driver.find_element("tag name","input")
print(a)'''
# if we are using find_element() and if non one of the element is getting matched with the value
# I have written it will throw    NoSuchElementException





# find_elements():-
# matching with 0 elements
'''driver.get("https://example.com/")
sleep(3)
a=driver.find_elements("tag name","input")
print(a)'''
# if we are using find_elements() and if non one of the element is getting matched with the value
# I have written it will return []





# find_element():-
# matching with 1 element
'''driver.get("https://example.com/")
sleep(3)
a=driver.find_element("tag name","a")
print(a)'''
# if we are using find_element() and if exactly one element is getting matched with the value
# I have written it will return that web element






# find_elements():-
# matching with 1 element
'''driver.get("https://example.com/")
sleep(3)
a=driver.find_elements("tag name","a")
print(a)'''
# if we are using find_elements() and if exactly one element is getting matched with the value
# I have written it will return  that web element inside list






# find_element():-
# matching with more than 1 element
'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
a=driver.find_element("tag name","input")
print(a)'''
# if we are using find_element() and if more than one element is getting matched with the value
# I have written it will return the address of only first matched element





# find_elements():-
# matching with more than 1 element
'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
a=driver.find_elements("tag name","input")
print(a)'''
# if we are using find_element() and if more than one element is getting matched with the value
# I have written it will return the address of all matching elements




# 5. link text:
'''driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("link text","Messenger").click()
sleep(4)'''


'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("link text","merrymoonmary").click()
sleep(4)'''



# click on blogger
# click on START button

'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("link text","Blogger").click()
sleep(4)'''


'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("link text","Udemy Courses").click()
sleep(4)'''



# 6. partial link text:
# using partial visible text

'''driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("partial link text","Messeng").click()
sleep(4)
'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("partial link text","merrymoon").click()
sleep(4)'''



'''driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("partial link text","Meta A").click()
sleep(4)'''






# css selector
# 1. tagname with attribute
# syntax:- tagname[attribute_name='attribute_value']

'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("css selector","input[class='form-control']").send_keys("abc")
sleep(2)
driver.find_element("css selector","input[id='email']").send_keys("abc@gmail.com")
sleep(2)
driver.find_element("css selector","input[placeholder='Enter Phone']").send_keys("12345678900")
sleep(2)
driver.find_element("css selector","textarea[class='form-control']").send_keys("Bangalore")
sleep(2)
driver.find_element("css selector","input[value='female']").click()
sleep(2)
driver.find_element("css selector","input[value='sunday']").click()
sleep(4)'''


# syntax:- tagname[attribute_name='attribute_value']
'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
driver.find_element("css selector","input[id='name']").send_keys("arbin")
sleep(2)
driver.find_element("css selector","input[name='email']").send_keys("arbin@gmail.com")
sleep(2)
driver.find_element("css selector","input[type='password']").send_keys("4375676")
sleep(2)
driver.find_element("css selector","button[type='submit']").click()
sleep(5)'''




# 2. ID selector
#      #idvalue

'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(6)
driver.find_element("css selector","#name").send_keys("arbin")
sleep(2)
driver.find_element("css selector","#email").send_keys("arbin@gmail.com")
sleep(2)
driver.find_element("css selector","#password").send_keys("67547356")
sleep(5)'''



'''driver.get("https://demowebshop.tricentis.com/login")
sleep(4)
driver.find_element("css selector","#Email").send_keys("arbin@gmail.com")
sleep(2)
driver.find_element("css selector","#Password").send_keys("06978587")
sleep(2)
driver.find_element("css selector","#RememberMe").click()
sleep(5)'''




# 3. Class selector
#      .classvalue

'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("css selector",".nav-input.nav-progressive-attribute").send_keys("iphone 17 pro max")
sleep(4)'''



'''driver.get("https://www.flipkart.com/")
sleep(6)
driver.find_element("css selector",".nw1UBF.v1zwn25").send_keys("samsung s26")
sleep(6)'''



'''driver.get("https://www.myntra.com/")
sleep(4)
driver.find_element("css selector",".desktop-searchBar").send_keys("Lehenga")
sleep(5)'''




'''driver.get("https://www.saucedemo.com/")
sleep(4)
driver.find_element("css selector",".input_error.form_input").send_keys("arbin")
sleep(2)
driver.find_element("css selector",".input_error.form_input").send_keys("90687968")
sleep(5)'''




# 4. tagname Selector
#   tagname
'''driver.get("https://www.myntra.com/")
sleep(4)
driver.find_element("css selector","input").send_keys("mars lipstick")
sleep(5)'''


'''driver.get("https://www.saucedemo.com/")
sleep(4)
driver.find_element("css selector","input").send_keys("arbin")
sleep(2)
driver.find_element("css selector","input").send_keys("90687968")
sleep(5)'''



'''driver.get("https://blinkit.com/s/")
sleep(3)
driver.find_element("css selector","input").send_keys("Bangalore")
sleep(8)
driver.find_element("css selector","input").send_keys("Curd")
sleep(5)'''



# 5. tagname with id
#      tagname#idvalue

'''driver.get("https://www.saucedemo.com/")
sleep(3)
driver.find_element("css selector","input#user-name").send_keys("standard_user")
sleep(2)
driver.find_element("css selector","input#password").send_keys("secret_sauce")
sleep(2)
driver.find_element("css selector","input#login-button").click()
sleep(4)'''



#6. tagname with class
#      tagname.classvalue


'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("css selector","input.nav-input.nav-progressive-attribute").send_keys("iphone 17 pro max")
sleep(6)
'''





# xpath
# 1. Absolute xpath

'''driver.get("https://www.saucedemo.com/")
sleep(3)
driver.find_element("xpath","/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("arbin")
sleep(2)
driver.find_element("xpath","/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("9856758")
sleep(2)
driver.find_element("xpath","/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
sleep(6)
'''


'''driver.get("https://www.myntra.com/")
sleep(4)
driver.find_element("xpath","/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("Deos")
sleep(5)'''



# register in demowebshop




# relative xpath
# basic xpath
# 1. xpath by attribute:-
# syntax:- //tagname[@attribute_name='attribute_value']

# before writing the value directly in the script first we have to verify that value
# to verify the value we have to write the value in search box
# we will get the search box when ctrl+f is pressed
# write the value in that search box then if it is showing 1 of 1 match then only you should take that value
# if it is showing more than one match change the attribute

'''driver.get("https://demowebshop.tricentis.com/register")
sleep(4)
driver.find_element("xpath","//input[@value='F']").click()
sleep(2)
driver.find_element("xpath","//input[@id='FirstName']").send_keys("arbin")
sleep(2)
driver.find_element("xpath","//input[@name='LastName']").send_keys("taj")
sleep(2)
driver.find_element("xpath","//input[@id='Email']").send_keys("arbin@gmail.com")
sleep(2)
driver.find_element("xpath","//input[@id='Password']").send_keys("1234567")
sleep(2)
driver.find_element("xpath","//input[@name='ConfirmPassword']").send_keys("1234567")
sleep(2)
driver.find_element("xpath","//input[@value='Register']").click()
sleep(6)'''



'''driver.get("https://www.saucedemo.com/")
sleep(3)
driver.find_element("xpath","//input[@placeholder='Username']").send_keys("standard_user")
sleep(2)
driver.find_element("xpath","//input[@placeholder='Password']").send_keys("secret_sauce")
sleep(2)
driver.find_element("xpath","//input[@value='Login']").click()
sleep(5)'''



# 2. xpath by text():- using visible text
# //tagname[text()='Visible text']              or     //tagname[.='Visible text']

'''driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("xpath","//span[text()='Create new account']").click()
sleep(5)'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","//a[text()='Udemy Courses']").click()
sleep(4)'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","//button[text()='START']").click()
sleep(4)'''




'''driver.get("https://www.facebook.com/")
sleep(5)
a=driver.find_elements("tag name","input")
sleep(5)

print(a[0].get_attribute("class"))
sleep(2)
print(a[1].get_attribute("class"))
sleep(5)
'''


# open website
# click on blog
# click on simple alert
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","//a[text()='Blog']").click()
sleep(2)
driver.back()
sleep(2)
driver.find_element("xpath","//button[text()='Simple Alert']").click()
sleep(3)'''



# 3. xpath by indexing
# syntax:- (xpath)[index]
'''driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element("xpath","(//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft'])[2]").click()
sleep(4)'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(4)
driver.find_element("xpath","(//input[@class='form-control'])[2]").send_keys("abc@gmail.com")
sleep(4)'''



'''driver.get("https://demoqa.com/automation-practice-form")
sleep(3)
driver.find_element("xpath","(//input[@type='text'])[2]").send_keys("taj")
sleep(4)'''




'''driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(3)
driver.find_element("xpath","(//input[@type='text'])[1]").send_keys("arbin")
sleep(3)
'''










# usage of contains():
# 1. if text/attribute value is lengthier
# 2. to handle partially dynamic elements
# 3. if text/attribute value is containing spaces in beginning or ending



# 3. contains() with attribute:-
# syntax:- //tagname[contains(@attribute_name,'attribute_value')]


'''driver.get("https://www.facebook.com/")
sleep(4)
driver.find_element("xpath","//input[contains(@class,'x1i10hfl')]").send_keys("abc@gmail.com")
sleep(2)
driver.find_element("xpath","(//input[contains(@class,'x1i10hfl')])[2]").send_keys("83756847")
sleep(5)
'''



# instagram

'''driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element("xpath","//input[contains(@class,'x1i10hfl')]").send_keys("abc@gmail.com")
sleep(2)
driver.find_element("xpath","(//input[contains(@class,'x1i10hfl')])[2]").send_keys("83756847")
sleep(5)'''





# dynamic


'''driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element("xpath","//input[contains(@id,'_')]").send_keys("arbin")
sleep(5)'''








# 4. contains() with text():-
# syntax:- //tagname[contains(text(),'Visible text')]

'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","//a[contains(text(),'merrymoon')]").click()
sleep(4)'''





'''driver.get("https://demowebshop.tricentis.com/")
sleep(4)
driver.find_element("xpath","(//a[contains(text(),'Books')])[3]").click()
sleep(5)'''




# Advance xpath
# Traversing
# forward (/ or //) and backward (/..) traversing

'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone 16e 128 GB: Built for Apple Intelligence, A18 Chip, Supersized Battery Life, 48MP Fusion. Camera, 15.40 cm (6.1″) Super Retina XDR Display; Black']/../../../..//span[@class='a-price-whole']")
print(a.text)'''




'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 256 GB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Space Black']/../../../..//span[@class='a-size-small a-color-base']")
print(a.text)'''


'''driver.get("https://www.flipkart.com/")
sleep(5)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(3)
driver.find_element("name","q").send_keys("samsung s26")
driver.find_element("xpath","//button[@title='Search for Products, Brands and More']").click()
sleep(3)
a=driver.find_element("xpath","//div[text()='Samsung Galaxy S26+ 5G (Cobalt Violet, 512 GB)']/../..//div[@class='hZ3P6w DeU9vF']")
sleep(2)
print(a.text)'''







'''driver.get("https://www.flipkart.com/")
sleep(5)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(3)
driver.find_element("name","q").send_keys("samsung s26")
driver.find_element("xpath","//button[@title='Search for Products, Brands and More']").click()
sleep(3)
a=driver.find_element("xpath","//div[text()='Samsung Galaxy S26+ 5G (Cobalt Violet, 512 GB)']/..//div[@class='MKiFS6']")
sleep(2)
print(a.text)'''


# xpath by axes:-
# parent and child

'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Cloud White']/parent::h2/parent::a/parent::div/parent::div//child::span[@class='a-price-whole']")
print(a.text)'''




'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Cloud White']/parent::h2/parent::a/parent::div/parent::div//child::span[@class='a-size-small a-color-base']")
print(a.text)'''




# ancestor-descendant
# fetching price
'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Cloud White']/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']/descendant::span[@class='a-price-whole']")
print(a.text)'''




# fetching ratings
'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Cloud White']/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']/descendant::span[@class='a-size-small a-color-base']")
print(a.text)'''



# fetch delivery date
'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(2)
driver.find_element("id","nav-search-submit-button").click()
sleep(4)
a=driver.find_element("xpath","//span[text()='iPhone Air 1 TB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Space Black']/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']/descendant::span[@id='WVCRIAFWG']")
print(a.text)'''






# assignment
# fetch ratings and price in flipkart using parent and child axes
# fetch ratings and price in flipkart using ancestor and descendant axes



# blinkit
'''driver.get("https://blinkit.com/")
sleep(6)
driver.find_element("name","select-locality").send_keys("Rt nagar Bangalore")
sleep(2)
driver.find_element("xpath","//div[@class='LocationSearchList__LocationListContainer-sc-93rfr7-0 lcVvPT']").click()
sleep(5)
driver.find_element("xpath","//div[@class='SearchBar__AnimationWrapper-sc-16lps2d-1 iJnYYS']").click()
sleep(2)
driver.find_element("xpath","//input[@placeholder='Search for atta dal and more']").send_keys("Amul cheese slices")
sleep(2)
driver.find_element("xpath","//div[@class='SearchBarContainer__IconContainer-sc-hl8pft-2 gaVCA-d']").click()
sleep(3)
driver.find_element("xpath","(//div[text()='Amul Cheese Slices']/../../..//div[@role='button'])[2]").click()
sleep(30)'''




# following-sibling(younger)
# preceding-sibling(elder)


# following-sibling
'''driver.get("https://www.w3schools.com/html/html_tables.asp")
sleep(3)
a=driver.find_element("xpath","//td[text()='Island Trading']/following-sibling::td")
print(a.text)'''


# preceding-sibling
'''driver.get("https://www.w3schools.com/html/html_tables.asp")
sleep(3)
a=driver.find_element("xpath","//td[text()='UK']/preceding-sibling::td[1]")
print(a.text)'''





# preceding-sibling
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","//label[text()='Sunday']/preceding-sibling::input").click()
sleep(4)'''


driver.quit()




