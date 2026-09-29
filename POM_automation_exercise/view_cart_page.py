class view_cart:
    checkout='xpath',"//a[.='Proceed To Checkout']"

    def __init__(self,driver):
        self.driver=driver

    def click_checkout(self):
        self.driver.find_element(*view_cart.checkout).click()