from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
# o.add_argument("--incognito")
driver=Chrome(o)
driver.maximize_window()
from time import sleep






# to switch control from parent to child frame we have to use-------->switch_to.frame()
# switch_to.frame() accepts either index or name/id attribute or webelement as an argument





'''driver.get("https://vinothqaacademy.com/iframe/")
sleep(3)'''



# switching the control to frame using indexing
'''driver.switch_to.frame(0)
sleep(1)
driver.find_element("id","nameInput").send_keys("arbin taj")
sleep(2)
driver.find_element("xpath","//input[@type='checkbox']").click()
sleep(2)
driver.find_element("id","roleInput").send_keys("Automation test engineer")
sleep(4)'''



# switching the control to frame using name attribute or id attribute of the frame
'''driver.switch_to.frame("employeetable")
sleep(1)
driver.find_element("id","nameInput").send_keys("arbin taj")
sleep(2)
driver.find_element("xpath","//input[@type='checkbox']").click()
sleep(2)
driver.find_element("id","roleInput").send_keys("Automation test engineer")
sleep(4)'''





# webelement:-
'''a=driver.find_element("xpath","//iframe[@title='Web Table']")
driver.switch_to.frame(a)
sleep(1)
driver.find_element("id","nameInput").send_keys("arbin taj")
sleep(2)
driver.find_element("xpath","//input[@type='checkbox']").click()
sleep(2)
driver.find_element("id","roleInput").send_keys("Automation test engineer")
sleep(4)'''





driver.get("https://in.linkedin.com/")
sleep(4)
a=driver.find_element("xpath","//iframe[@title='Sign in with Google Button']")

driver.switch_to.frame(a)
sleep(3)
driver.find_element("xpath","//span[text()='Continue with Google']").click()
sleep(4)






'''
a=driver.find_element("xpath","//iframe[@title='Registration Form']")
driver.switch_to.frame(a)
sleep(3)
driver.find_element("id","vfb-5").send_keys("arbin")
sleep(4)'''









# switch_to.parent_frame():- switches the control to parent



'''driver.switch_to.frame(2)
sleep(3)
driver.find_element("id","vfb-5").send_keys("arbin")
sleep(4)

driver.switch_to.parent_frame()

driver.switch_to.frame(0)
sleep(3)
driver.find_element("id","roleInput").send_keys("Automation Test Engineer")
sleep(4)'''




# open website
# enter name and role in first frame
# click on male or female in 3rd frame
# click on alert box in 2nd frame

















driver.quit()
