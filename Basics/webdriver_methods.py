# webdriver methods----->used to control browser

from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep

# 1. get():- used to navigate to an application

'''driver.get("https://www.instagram.com/")'''




'''driver.get("https://www.facebook.com/")'''




'''driver.get("ht.facbook.com/")'''
# Whn the url is not valid we will be getting Invalid Argument Exception



'''driver.get("https://www.selenium.dev/")'''




'''
driver.get("https://www.instagram.com/")
driver.get("https://www.nykaa.com/")'''





'''driver.get("https://www.instagram.com/")
sleep(3)
driver.get("https://www.nykaa.com/")
sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
driver.get("https://aqualogica.in/")
'''




# 2. back():-used to navigate to previous page
'''driver.get("https://www.instagram.com/")
sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
driver.back()'''




'''driver.get("https://www.instagram.com/")
sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
driver.back()
driver.get("https://www.zomato.com/bangalore/delivery")'''



'''driver.get("https://www.instagram.com/")
sleep(3)
driver.get("https://www.amazon.in/")
sleep(3)
driver.back()
driver.get("https://www.zomato.com/bangalore/delivery")
driver.back()'''






'''driver.get("https://aqualogica.in/")
sleep(3)
driver.back()'''



'''driver.back()'''




# 3. forward():-
'''driver.get("https://www.instagram.com/")
sleep(3)
driver.get("https://www.flipkart.com/")
sleep(3)
driver.back()
sleep(2)
driver.forward()'''




'''driver.get("https://www.nykaa.com/")
sleep(3)
driver.forward()'''





'''driver.forward()'''




# 4. refresh():-
'''driver.get("https://www.plixlife.com/")
sleep(10)
driver.refresh()'''




'''
driver.get("https://www.plixlife.com/")
sleep(4)
driver.get("https://www.crocs.in/")
sleep(4)
driver.refresh()'''





'''sleep(4)
driver.refresh()'''





# 5. maximize_window():-
'''
driver.get("https://www.anthropic.com/")
driver.maximize_window()'''



# 6. minimize_window():-

'''sleep(4)
driver.minimize_window()'''







'''sleep(4)
driver.minimize_window()
sleep(3)
driver.get("https://www.anthropic.com/")'''




# 7. fullscreen_window()
'''driver.get("https://www.youtube.com/")
sleep(4)
driver.fullscreen_window()
'''



'''driver.get("https://open.spotify.com/")
sleep(4)
driver.fullscreen_window()'''




'''driver.fullscreen_window()
sleep(3)
driver.maximize_window()'''





'''driver.fullscreen_window()
sleep(3)
driver.get("https://www.flipkart.com/")
sleep(4)'''









# 8. set_window_size():-
'''driver.set_window_size(1100,800)'''



'''driver.set_window_size(-1100,-800)'''
# the above code will throw the below exception
# InvalidArgumentException





# 9. set_window_position():-
'''driver.set_window_position(0,400)'''
'''left to right----> +ve X
right to left------> -ve X
up to down------> +ve y
down to up -----> -ve y'''



# task
# try with negative values




# 10.get_window_size():-
'''a=driver.get_window_size()
print(a['height'])'''



'''a=driver.get_window_size()
print(a['width'])'''



'''a=driver.get_window_size()
print(a)
'''


# 11. get_window_position():-
'''
a=driver.get_window_position()
print(a)'''




'''a=driver.get_window_position()
print(a['x'])
print(a['y'])'''




# 12. get_window_rect():-
'''a=driver.get_window_rect()
print(a)'''


'''a=driver.get_window_rect()
print(a['width'])'''




# properties:-
# 13. current_url:-
'''driver.get("https://www.flipkart.com/")
print(driver.current_url)'''





'''driver.get("https://thedermaco.com/")
sleep(3)
driver.get("https://sites.google.com/psu.edu/cearl/")
sleep(3)
print(driver.current_url)'''




'''driver.get("https://gemini.google.com/")
sleep(3)
print(driver.current_url)
driver.get("https://www.spacex.com/")
sleep(3)
driver.get("https://copilot.microsoft.com/")
sleep(3)
driver.get("https://www.poorvika.com/")
sleep(3)
print(driver.current_url)'''






'''sleep(2)
print(driver.current_url)
driver.get("https://www.pizzahut.co.in/account/otp")
sleep(3)
driver.get("https://claude.ai/login")
sleep(3)
driver.get("https://www.nike.in/")
sleep(3)
print(driver.current_url)'''





# 14. title:-
'''driver.get("https://www.flipkart.com/")
print(driver.title)'''




'''
driver.get("https://thedermaco.com/")
sleep(3)
driver.get("https://sites.google.com/psu.edu/cearl/")
sleep(3)
print(driver.title)
'''




'''driver.get("https://gemini.google.com/")
sleep(3)
print(driver.title)
driver.get("https://www.spacex.com/")
sleep(3)
driver.get("https://copilot.microsoft.com/")
sleep(3)
driver.get("https://www.poorvika.com/")
sleep(3)
print(driver.title)'''






'''sleep(2)
print(driver.title)
driver.get("https://www.pizzahut.co.in/account/otp")
sleep(3)
driver.get("https://claude.ai/login")
sleep(3)
driver.get("https://www.nike.in/")
sleep(3)
print(driver.title)
'''




# 15.page_source:-
'''driver.get("https://www.flipkart.com/")
print(driver.page_source)'''




# 16. window_handles:-
# used to fetch the id of a tab
'''
sleep(8)                                           #manually open two tabs
print(driver.window_handles)'''




'''

sleep(20)                                           #manually open 5 tabs
print(driver.window_handles)
'''




'''sleep(10)                                             #mnaully open 1 tab and close first
print(driver.window_handles)
'''




'''sleep(20)
a=driver.window_handles                    #a=['tab1','tab2','tab3']
print(len(a))'''



# 5 tabs
'''a=driver.window_handles
print(a)'''

# number of tabs opened = number of tab ids
# 5=5




'''
sleep(20)                                             #open a new tab
driver.get("https://www.croma.com/")
sleep(4)
driver.get("https://www.moneycontrol.com/")

'''

# 17. current_window_handle:
# used to fetch the tab id where control is present
'''
sleep(20)                                           #open two tabs
print(driver.window_handles)
print(driver.current_window_handle)
'''




# 18. switch_to.window():-
# used to switch control


'''driver.get("https://www.facebook.com/")
sleep(20)                                                      #open a new tab
a=driver.window_handles                                 #a=['tab1','tab2']
driver.switch_to.window(a[1])
driver.get("https://www.instagram.com/")
sleep(4)
'''



# i want to open two diff applications in two diff tabs
'''driver.get("https://www.mcaffeine.com/")
sleep(20)                                                #open a new tab
a=driver.window_handles
driver.switch_to.window(a[1])
driver.get("https://trends.google.com/trends/")'''





# open blinkit in one tab
# in another tab open youtube





# 19. switch_to.new_window():
# to open new tab or new window
# accepts one arg------------->'tab'  or 'window'


'''driver.switch_to.new_window('tab')'''




'''driver.get("https://www.instagram.com/")
sleep(2)
driver.switch_to.new_window('tab')
driver.get("https://www.hotstar.com/in/home")
sleep(3)
driver.switch_to.new_window('tab')
driver.get("https://www.jio.com/")
sleep(4)'''



'''sleep(4)
driver.switch_to.new_window('window')

driver.get("https://www.primevideo.com/")'''




# 20.close()

'''sleep(3)
driver.switch_to.new_window('tab')
sleep(2)
driver.close()'''






# 21. quit()

'''sleep(3)
driver.switch_to.new_window('tab')
sleep(2)
driver.quit()'''




























































































































































































































































































































# task:
# wht is class?
# wht is object
# how to create class?
# hpw t create object?
# how to fetch method present inside class
# diffrence between func and method












# driver.get("https://www.instagram.com/")
# sleep(5)
# if driver.title=='Instagram':
#     print("navigated to correct page")
# else:
#     print("navigated to wrong page")






