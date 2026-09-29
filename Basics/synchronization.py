from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep


'''
driver.get("https://www.shoppersstack.com/")
driver.find_element("id","loginBtn").click()
driver.find_element("id","Email").send_keys("arbin@gmail.com")
driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("Password")'''

# The above code will throw NoSuchElementException





'''driver.get("https://www.shoppersstack.com/")
sleep(7)
driver.find_element("id","loginBtn").click()
sleep(4)
driver.find_element("id","Email").send_keys("arbin@gmail.com")
driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("Password")


sleep(6)'''





'''
driver.implicitly_wait(2000)
driver.get("https://www.shoppersstack.com/")
driver.find_element("id","loginBtn").click()
driver.find_element("id","Email").send_keys("arbin@gmail.com")
driver.find_element("xpath","(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]").send_keys("Password")
'''









# driver.get("https://www.google.com/")
# sleep(4)
# driver.find_element("css selector","textarea[jsname='yZiJbe']").send_keys("python selenium")
# sleep(5)



'''
driver.implicitly_wait(10000)
driver.get("https://www.shoppersstack.com/products_page/5408")
driver.find_element("id","Check Delivery").send_keys("123456")
driver.find_element("name","Check").click()'''
#   The above code will throw  ElementClickInterceptedException



'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(100)
driver.get("https://www.shoppersstack.com/products_page/5408")
driver.find_element("id","Check Delivery").send_keys("123456")
a=driver.find_element("name","Check")
ob=WebDriverWait(driver,100)
ob.until(EC.element_to_be_clickable(a))
a.click()'''






'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://www.amazon.in/")
a='Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
ob=WebDriverWait(driver,50)
ob.until(EC.title_is(a))'''




'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://www.amazon.in/")
a='Online Shopping site in India'
ob=WebDriverWait(driver,50)
ob.until(EC.title_contains(a))'''




'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://www.amazon.in/")
ob=WebDriverWait(driver,50)
ob.until(EC.url_to_be("https://www.amazon.in/"))'''





'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(100)

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element("id","name").send_keys("abc")
a=driver.find_element("xpath","//input[@value='sunday']")
a.click()
ob=WebDriverWait(driver,70)
ob.until(EC.element_to_be_selected(a))'''







# if we are able to modify polling frequency time thn it is fluent wait
'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(100)
driver.get("https://www.shoppersstack.com/products_page/5408")
driver.find_element("id","Check Delivery").send_keys("123456")
a=driver.find_element("name","Check")

ob=WebDriverWait(driver,100,0.2)
ob.until(EC.element_to_be_clickable(a))
a.click()'''






























driver.quit()









'''class A:
    def disp(self):
        pass
    

ob=A()
ob.disp()'''






'''class WebDriverWait:
    def until(self):
        pass
    
ob=WebDriverWait()
ob.until()'''











