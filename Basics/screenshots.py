#syntax:- driver.save_screenshot("filename.png")


from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()
from datetime import datetime




# capturing screenshot in netflix
'''driver.get("https://www.netflix.com/in/")
sleep(4)
driver.save_screenshot("screenshot3.png")
sleep(3)'''




# capturing screenshot in amazon prime
'''driver.get("https://www.primevideo.com/")
sleep(4)
driver.save_screenshot("screenshot2.png")
sleep(3)'''




'''driver.get("https://www.google.com/")
sleep(4)
a=driver.find_element("name","q")
a.screenshot("defect.png")
sleep(4)'''



# driver.find_element("xpath","//div[@class='ytThumbnailViewModelImage']")




# capturing screenshot in particular folder:-

# to copy path of any folder follow the below steps:-
# right click on folder
# copy path/reference
# click on absolute path




'''driver.get("https://www.anthropic.com/")
sleep(3)
driver.save_screenshot("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\screenshots\\defect1.png")
sleep(4)'''












# extracting date and time

'''from datetime import datetime
print(datetime.now())'''


# year-month-date hour-minute-seconds.milliseconds



# to change the format of date and time


'''
from datetime import datetime
print(datetime.now().strftime("%A %d/%m/%Y  %H:%M:%S"))

'''

# %A------>day
# %d ------> date
# %m ------> month
# %Y ----->Year








# implementing time stamp in screenshot
'''driver.get("https://www.netflix.com/in/")
sleep(4)
print(datetime.now().strftime("%A %d/%m/%Y  %H:%M:%S"))
sleep(3)
driver.save_screenshot("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\screenshots\\defect2.png")
sleep(5)'''




# step1:-
# open browser enter url ----->   https://pharmeasy.in/
# welcome should be display


# on the top --> click on medicine option
# medicine page should display



# search for some medicine
# make sure search medicine page should display





'''driver.get("https://pharmeasy.in/")
sleep(6)
first_title="PharmEasy – Online Pharmacy & Medical Store with Healthcare Services in India | 50 Lakhs+ Customers"
assert driver.title==first_title, driver.save_screenshot("C:\\Users\\Levono\\PycharmProjects\\Selenium_A17\\screenshots\\defect3.png")

driver.find_element("xpath","(//a[.='Medicine'])[2]").click()
sleep(3)
med_title="Buy Medicines Online - Up to 24% OFF | Fast Delivery by PharmEasy"
assert driver.title==med_title
sleep(4)

driver.find_element("xpath","//div[@class='LoginDrawer-module_svgBlock__K6xgl']").click()
sleep(7)'''


















driver.quit()