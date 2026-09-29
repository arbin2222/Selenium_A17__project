from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(o)
driver.maximize_window()
from time import sleep

from POM_demowebshop.Login_page import Login_Page
from POM_demowebshop.Home_page import Home_Page
from POM_demowebshop.Desktop_page import Desktop_Page
from POM_demowebshop.Cart_page import Cart_Page
# from foldername.filename import classname


driver.get("https://demowebshop.tricentis.com/")
sleep(4)


log=Login_Page(driver)
log.click_login()
sleep(3)
log.enter_email()
log.enter_pwd()
log.click_log_btn()
sleep(3)




home=Home_Page(driver)
home.hover_computer()
sleep(1)
home.click_desktops()
sleep(3)



desk=Desktop_Page(driver)
desk.click_add_to_cart()
sleep(2)
desk.click_shopping_cart()
sleep(3)





cart=Cart_Page(driver)
cart.click_terms_conditions()
sleep(2)
cart.click_checkout()
sleep(6)




