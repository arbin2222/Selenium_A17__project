'''from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument('--disable-notifications')
driver=Chrome(o)
driver.maximize_window()
from time import sleep'''




# popup:- a small window appearing on the page
# thr are 6 types of pop ups:-

# 1. JavaScript Alerts
# 2. Notification pop ups
# 3. Authentication popups
# 4. file upload popup
# 5. file download popup
# 6. hidden division pop



# 1. JavaScript Alerts:

# 3 types of JS alerts:-
# 1. Simple alert
# 2. confirmation alert
# 3. prompt alert




# property used in JS Alerts:-
# driver.switch_to.alert


# methods used in JS Alerts:-
# 1. accept() ----> Click on OK button
# 2. dismiss() ---> Click on cancel button




# 1. Simple Alert:-
# Characteristics of simple alert:-
# 1. It is not inspectable
# 2. simple alerts will be having OK button





'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.find_element("id","alertBtn").click()
sleep(4)

# switch the control to alert
a=driver.switch_to.alert

# clicking on Ok button
a.accept()

sleep(6)'''








# 2. Confirmation Alert:-
# Characteristics of simple alert:-
# 1. It is not inspectable
# 2. confirmation alerts will be having OK and CANCEL Button



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.find_element("id","confirmBtn").click()
sleep(4)

# switch the control to alert
a=driver.switch_to.alert

# clicking on OK Button
a.accept()

sleep(4)'''






'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.find_element("id","confirmBtn").click()
sleep(4)

# switch the control to alert
a=driver.switch_to.alert

# clicking on cancel Button
a.dismiss()

sleep(4)'''







# 3. prompt alert:-
# Characteristics of simple alert:-
# 1. It is not inspectable
# 2. prompt alert will accept user input and it will have OK and CANCEL buttons




'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.find_element("id","promptBtn").click()
sleep(4)
# switch the control to alert
a=driver.switch_to.alert
# entering the data in input field
a.send_keys("Steve")
# clicking on OK Button
a.accept()
sleep(8)'''



'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(2)
driver.find_element("id","promptBtn").click()
sleep(4)
# switch the control to alert
a=driver.switch_to.alert
# entering the data in input field
a.send_keys("Steve")
# clicking on dismiss Button
a.dismiss()
sleep(8)'''





# Deleting HP Envy
'''driver.get("https://demoapps.qspiders.com/ui/alert/prompt")
sleep(4)
driver.find_element("xpath","(//input[@type='checkbox'])[4]").click()
sleep(1)
driver.find_element("id","deleteButton").click()
sleep(2)
# switch the control to alert
a=driver.switch_to.alert
# entering data
a.send_keys("Deleted")
sleep(4)
# clicking on Ok Button
a.accept()
sleep(5)'''






# 2. file upload pop up:-

# single file upload
'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
path="C:\\Users\\Levono\\OneDrive\\Desktop\\github commands.docx"
sleep(3)
driver.find_element("id","singleFileInput").send_keys(path)
sleep(4)'''





'''driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
path="C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\screenshots\\defect1.png"
path2="C:\\Users\\Levono\\OneDrive\\Desktop\\06_Slicing.pdf"
a=driver.find_element("id","multipleFilesInput")
a.send_keys(path)
sleep(2)
a.send_keys(path2)
sleep(4)'''






# 2. notification pop ups:
# Characteristics of notification popups:-
# 1. Not inspectable
# 2. allow or block permission




'''driver.get("https://www.deccanherald.com/")
sleep(6)
'''


'''
driver.get("https://www.news18.com/")
sleep(20)'''





# 3. authentication popup:


# characteristics of authentication popup:-
# 1. non inspectable
# 2. asks for username and password for signin

# to handle authentication popup:
# syntax:-
# https://username:password@url



'''driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
sleep(4)'''



'''driver.get("https://admin:admin@razorpay.com/payment-button/")
sleep(4)'''






# hidden division popups:-
# characteristics :-
# 1. Inspectable
# 2. initially this pop up will be hidden



'''driver.get("https://www.redbus.in/")
sleep(4)
driver.find_element("xpath","//button[@type='button']").click()
sleep(3)
driver.find_element("xpath","//button[@aria-label='Log in']").click()
sleep(2)
driver.find_element("xpath","//input[@type='tel']").send_keys("9870256780")
sleep(5)'''











'''driver.get("https://www.zomato.com/bangalore/delivery")
sleep(3)
driver.find_element("xpath","//button[text()='Sign up']").click()
sleep(2)
driver.find_element("xpath","//input[@type='text']").send_keys("arbin taj")
driver.find_element("xpath","(//input[@type='text'])[2]").send_keys("arbin@gmail.com")
sleep(2)
driver.find_element("xpath","//input[@type='checkbox']").click()
sleep(2)
driver.find_element("xpath","//span[.='Create account']").click()
sleep(5)'''




# file download pop up
'''driver.get("https://demoqa.com/upload-download")
sleep(4)
driver.find_element("id","downloadButton").click()
sleep(5)'''







'''
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
sleep(6)
driver.find_element("id","double-prompt").click()

a=driver.switch_to.alert
a.send_keys("Neha")
sleep(3)
a.accept()

sleep(4)
a=driver.switch_to.alert
a.send_keys("Arbin")
sleep(3)
a.accept()

sleep(9)'''





'''driver.get("https://www.file.io/")
sleep(4)
path="C:\\Users\\Levono\\OneDrive\\Desktop\\06_Slicing.pdf"
driver.find_element("id","select-files-input").send_keys(path)
sleep(15)'''


# driver.quit()




