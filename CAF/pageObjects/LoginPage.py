class CAF_HC:
    # Identify all the common locators

    search = "//input[@id='institute_search'])[1]"

    # capture the driver from the test case
    def __init__(self, driver):
        self.driver = driver  # initiating the local driver

    def search_click(self):
        self.driver.find_element_by_xpath(self.search).click()
