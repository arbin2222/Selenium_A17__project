class Desktop_Page:
    add_to_cart="xpath","//a[text()='Simple Computer']/../..//input"
    shopping_cart="xpath","//span[text()='Shopping cart']"

    def __init__(self,driver):
        self.driver=driver

    def click_add_to_cart(self):
        self.driver.find_element(*Desktop_Page.add_to_cart).click()

    def click_shopping_cart(self):
        self.driver.find_element(*Desktop_Page.shopping_cart).click()



        