# if condition:
#     TSB
# else:
#     FSB



'''a='Tamilarasan'

if a=='Tamilarasan':
    print("Yes name is equal")
else:
    print("name is not equal")'''




# assertion:-


'''assert condition,FSB
TSB'''




# if condition is true it will TSB
# if condition is False it will print FSB and it will throw Assertion Error


'''a='Tamilarasan'
assert a=='Tamilarasan',"No😔 Not equal"
print("Yes it is equal")'''



'''a='Tamilarasan'
assert a=='tamilarasan',"No😔 Not equal"
print("Yes it is equal")'''

# AssertionError: No😔 Not equal







'''a=11
assert a%2==0,"Odd number"
print("Even number")'''

# AssertionError: Odd number




'''age=20
assert age>=18,"Not eligible to vote"
print("Eligible to vote")'''
# Eligible to vote




'''pizza=1
assert pizza>=2,"Not enough Pizzas"
print("Party starts")'''

# AssertionError: Not enough Pizzas




'''a='mom'
assert a==a[::-1],"not palindrome"
print("palindrome")'''

# palindrome



'''a=123
assert a==1234,"not equal"
print("Equal")'''

# AssertionError: not equal






# assertion in selenium is used for verification purpose



from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()



driver.get("https://www.google.com/")
sleep(15)
assert driver.title=='Google',driver.save_screenshot("google_not_opened.png")
print("Correct page Openend")



'''driver.get("https://www.youtube.com/")
sleep(4)
assert driver.title=='YouTube',"Wrong page"
print("Yes youtube opened")'''
# Yes youtube opened








































driver.quit()








