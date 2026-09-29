from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
from time import sleep
driver.maximize_window()




from POM_automation_exercise.welcome_page import welcome
from POM_automation_exercise.login_page import login
from POM_automation_exercise.signup_page import signup
from POM_automation_exercise.acc_created_page import acc_created
from POM_automation_exercise.home_page import home
from POM_automation_exercise.view_cart_page import view_cart


wp=welcome(driver)
l=login(driver)
s=signup(driver)
ac=acc_created(driver)
hm=home(driver)
vc=view_cart(driver)




driver.implicitly_wait(100)

driver.get("https://automationexercise.com/")
sleep(4)



wp.click_on_signup()
sleep(3)
l.reg_name()
l.reg_email()
l.click_signup()
sleep(3)

s.click_mrs()
s.enter_pwd()
s.select_day()
s.select_month()
s.select_year()
s.enter_fname()
s.enter_lname()
s.enter_address()
s.select_country()
s.enter_state()
s.enter_city()
s.enter_zipcode()
s.enter_mob_no()
sleep(2)
s.click_create_acc()
sleep(6)



ac.click_continue()
sleep(4)


hm.click_logout()
sleep(4)

l.login_email()
l.login_pwd()
l.click_login()

sleep(4)

hm.click_add_to_cart()
hm.click_view_cart()

sleep(4)

vc.click_checkout()





sleep(6)

driver.quit()



