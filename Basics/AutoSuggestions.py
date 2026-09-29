#AutoSuggestions:
# Two types:-
# 1. Inspectable AutoSuggestions
# 2. Non inspectable AutoSuggestions


from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome()
from time import sleep
driver.maximize_window()




# inspectable autosuggestions
'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").send_keys("samsung")
sleep(2)
a=driver.find_elements("xpath","//div[@class='s-suggestion-container']")
for i in a:
    print(i.text)'''








# non inspectable autosuggestion
'''driver.get("https://www.flipkart.com/")
sleep(3)
driver.find_element("xpath","//span[text()='✕']").click()
sleep(3)
driver.find_element("name","q").send_keys("samsung")
sleep(2)
a=driver.find_elements("xpath","//div[@class='VDtK0l _1psv1ze2u _1psv1ze53 _1psv1ze9x _1psv1ze7o']")
for i in a:
    print(i.text)'''






# to pause the page follow the below steps
# go to sources tab
# click on pause icon


# myntra
# zepto ------> type kitkat  thn print all autosuggestions which is displayed




'''driver.get("https://www.myntra.com/")
sleep(3)
driver.find_element("xpath","//input[@placeholder='Search for products, brands and more']").send_keys("cord sets")
sleep(2)
a=driver.find_elements("xpath","//li[@class='desktop-suggestion null']")
for i in a:
    print(i.text)
'''




















driver.quit()