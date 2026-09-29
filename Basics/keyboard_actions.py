#to perform keyboard actions we have to import keys class
# keys class provide keys
# if we want to perform any keyboard action we have to use keys class inside send_keys
# with the help of keys class we cannot deal with alphabets

# syntax:- send_keys(Keys.keyname)

# send_keys(Keys.SHIFT)
# send_keys(Keys.BACKSPACE)
# send_keys(Keys.TAB)


#from selenium.webdriver.common.keys import Keys



from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()
from selenium.webdriver.common.keys import Keys



# entering the characters in capital
'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_element("id","twotabsearchtextbox")
a.send_keys(Keys.SHIFT+'i')
a.send_keys("phone")
sleep(5)'''




#open amazon
#enter some value
# remove entire value

'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_element("id","twotabsearchtextbox")
a.send_keys("Samsung")
a.send_keys(Keys.CONTROL+'A')
sleep(3)
a.send_keys(Keys.BACKSPACE)
sleep(5)'''





# open facebook
# enter ur name in username field
# copy the name from username field
# paste it in password field
# then click on login button






# performing scrolling using keys
'''driver.get("https://www.facebook.com/")
sleep(3)
a=driver.find_element("xpath","//a[text()='Careers']")
a.send_keys(Keys.PAGE_DOWN)
sleep(5)'''





# search selenium in google then get thn result page
'''driver.get("https://www.google.com/")
sleep(3)
a=driver.find_element("name","q")
a.send_keys("python selenium")
sleep(2)
a.send_keys(Keys.ENTER)
sleep(5)'''







# open google
# type python selenium
# hit enter
driver.get("https://www.google.com/")
sleep(3)
a=driver.find_element("name","q")
a.send_keys("python selenium")
sleep(2)
a.send_keys(Keys.ENTER)
sleep(5)






















driver.quit()