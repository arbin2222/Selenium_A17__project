from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()






'''driver.get("https://www.flipkart.com/")
sleep(3)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(1)
driver.find_element("name","q").send_keys("iphone")
driver.find_element("xpath","//button[@type='submit']").click()
sleep(2)
driver.find_element("xpath","//div[@class='RG5Slk']").click()
sleep(3)
a=driver.window_handles                    #a=['tab1','tab2']
driver.switch_to.window(a[1])
sleep(2)
driver.find_element("xpath","//div[text()='Buy now']").click()
sleep(5)
driver.find_element("xpath","//input[@type='number']").send_keys("8965035672")
sleep(3)
driver.find_element("xpath","//button[text()='Continue']").click()
sleep(5)'''


# open amazon ----> then search for iphone ----> click on any iphone  ----> now in the next tab you will find option--->
# add to wishlist ---> click on add to wishlist
