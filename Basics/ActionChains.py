# ActionsChains is a class
# mouse actions and keyboard actions

# syntax for importing actionchains class

'''from selenium.webdriver.common.action_chains import ActionChains
ac=ActionChains(driver)'''




from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome()
driver.maximize_window()
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
ac=ActionChains(driver)



# note:- whenever we are using Actionchain class methods thn we have to include one more method that is perform()


# 1. click():
# used to perform click action
# accept one argument
# syntax:- ob.click(webelement)



'''driver.get("https://www.google.com/")
sleep(3)
a=driver.find_element("xpath","//a[text()='Gmail']")
ac.click(a).perform()
sleep(4)'''




'''driver.get("https://www.google.com/")
sleep(3)
a=driver.find_element("xpath","//a[text()='Images']")
ac.click(a).perform()
sleep(4)'''






# 2. double_click():-
# used to perform double click action
# syntax:- ob.double_click(webelement)



'''driver.get("https://demoqa.com/buttons")
sleep(3)
a=driver.find_element("id","doubleClickBtn")
ac.double_click(a).perform()
sleep(4)'''




# from selenium.webdriver.common.action_chains import ActionChains
# ac=ActionChains(driver)



# 3. context_click():-
# used to perform right click action
# syntax:-  ob.context_click(webelement)



'''driver.get("https://demoqa.com/buttons")
sleep(3)
a=driver.find_element("id","rightClickBtn")
ac.context_click(a).perform()
sleep(4)
'''





# 4. move_to_element():-
# used to perform hover action
# syntax:- ob.move_to_element(webelement)



'''driver.get("https://www.amazon.in/")
sleep(3)
a=driver.find_element("xpath","//span[contains(text(),'Account & Lists')]")
ac.move_to_element(a).perform()
sleep(4)'''



# 5. click_and_hold():-
# used to perform click and hold action
# syntax:- ob.click_and_hold(webelement)


'''driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
sleep(2)
driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
sleep(2)
driver.find_element("id","password").send_keys("1234567")
sleep(2)
a=driver.find_element("xpath","//img[@class='ng-star-inserted']")
ac.click_and_hold(a).perform()
sleep(6)'''







# 6. release():-
# releases the mouse button after clicking and holding it
# syntax:- ob.release()

'''driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
sleep(2)
driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
sleep(2)
driver.find_element("id","password").send_keys("1234567")
sleep(2)
a=driver.find_element("xpath","//img[@class='ng-star-inserted']")
ac.click_and_hold(a).perform()
ac.release().perform()
sleep(6)'''




# 7. pause():-
# used to pause execution for the specified number of seconds
# syntax:- ob.pause(seconds)


'''driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
sleep(2)
driver.find_element("xpath","//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
sleep(2)
driver.find_element("id","password").send_keys("1234567")
sleep(2)
a=driver.find_element("xpath","//img[@class='ng-star-inserted']")
ac.click_and_hold(a).perform()
ac.pause(4).perform()
ac.release().perform()
sleep(6)'''




# 8. drag_and_drop():
# used to perform drag and drop action
# accepts 2 arguments:-
# 1st arg-------> draggable element
# 2nd arg ------> droppable element
# syntax:- ob.drag_and_drop(source,dest)




'''driver.get("https://demoqa.com/droppable")
sleep(3)
a=driver.find_element("id","draggable")
b=driver.find_element("id","droppable")
ac.drag_and_drop(a,b).perform()
sleep(4)'''






# 9. send_keys():-
# used to enter the data in input field which is focused
# syntax:- ob.send_keys("value")

'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id","twotabsearchtextbox").click()
ac.send_keys("iphone").perform()
sleep(5)
'''



# flipkart




# 10. send_keys_to_element():-
# used to enter the data
# two arguments:-
# 1st arg-------->webelement wherein you want to enter data
# 2nd arg-------->value
# syntax:- ob.send_keys_to_element(webelement,"value")




'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_element("id","twotabsearchtextbox")
ac.send_keys_to_element(a,"Samsung").perform()
sleep(5)'''






# 11. scroll_to_element():-
# used to perform scrolling
# ob.scroll_to_element(webelement)

'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_element("xpath","//a[text()='See more from Amazon Live']")
ac.scroll_to_element(a).perform()
sleep(8)'''




# 12. scroll_by_amount():-
#used to perform scrolling action
# ot will scroll the webpage till the specified distance
# accepts 2 args:-
# 1st arg:- value for x axis(horizontal scroll)
# 2nd arg:- value for y axis(vertical scroll)
# syntax:- ob.scroll_by_amount(x,y)




'''driver.get("https://www.amazon.in/")
sleep(4)
ac.scroll_by_amount(0,3000).perform()
sleep(5)'''



'''driver.get("https://demoapps.qspiders.com/ui/scroll/newTabHorizontal")
sleep(7)
ac.scroll_by_amount(2000,0).perform()
sleep(4)'''






















# actions_chains.py

# class ActionChains:
#           def double_click():
#                   pass


#           def drag_and_drop():
#                   pass



# a=ActionChains()
# a.double_click()







'''driver.get("https://www.kirupa.com/html5/press_and_hold.htm")
sleep(4)
a=driver.find_element("id","item")
ac.click_and_hold(a).perform()
sleep(5)'''





'''
driver.get("https://www.kirupa.com/html5/press_and_hold.htm")
sleep(4)
a=driver.find_element("id","item")
ac.click_and_hold(a).perform()
ac.pause(5).perform()
ac.release(a).perform()
sleep(5)'''





# https://www.selenium.dev/selenium/web/mouse_interaction.html

# /the above is for drag and drop







driver.quit()