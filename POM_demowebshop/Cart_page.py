class Cart_Page:
    terms="id","termsofservice"
    checkout="id","checkout"

    def __init__(self,driver):
        self.driver=driver

    def click_terms_conditions(self):
        self.driver.find_element(*Cart_Page.terms).click()


    def click_checkout(self):
        self.driver.find_element(*Cart_Page.checkout).click()



