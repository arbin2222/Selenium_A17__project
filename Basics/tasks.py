
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()



# xpath
# In flipkart search for iphone. # get the all the phone names and prices
'''
driver.get("https://www.flipkart.com/")
sleep(3)
a=driver.find_element("name","q")
a.send_keys("iphone")
a.submit()
sleep(4)
phones=driver.find_elements("xpath","//div[@class='RG5Slk']")

# phones=['apple','apple 16 pro','apple iphone 17'............]
prices=driver.find_elements("xpath","//div[@class='hZ3P6w DeU9vF']")

for i in range(len(phones)):
    print("Mobile: " ,phones[i].text)
    print("price: " ,prices[i].text)


driver.quit()'''


'''for i in range(0,3):
    print("apple")'''
# prints apple for three times


'''for i in range(3):
    print("apple")'''
# prints apple for three times


'''a='selenium'
for i in range(len(a)):
    print("apple")'''
# 0 1 2 3 4 5 6 7


# for i in phones:
#     print(phones[i].text)

