class home:
    logout="xpath","//a[@href='/logout']"
    add_to_cart="xpath","//a[@class='btn btn-default add-to-cart']"
    view_cart="xpath","//u[text()='View Cart']"

    def __init__(self,driver):
        self.driver=driver

    def click_logout(self):
        self.driver.find_element(*home.logout).click()


    def click_add_to_cart(self):
        self.driver.find_element(*home.add_to_cart).click()


    def click_view_cart(self):
        self.driver.find_element(*home.view_cart).click()


        
