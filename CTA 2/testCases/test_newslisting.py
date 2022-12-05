import time
import requests
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import *
from pageObjects.Xpaths import Xpath




class Test_newslisting(Cta):
    
    baseURL = ReadConfig.getNewslistingUrl()
    logger = LogGen.loggen()  # Logger

  
    def test_newslisting(self,setup):
        self.logger.info("******* Starting CTA test for Newslisting**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        if actual_title == "Education News : Latest News on Courses, Colleges and Exams - CollegeDekho":
            assert True
        else:
            assert False
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(2)
        
        # Subscribe_now = self.driver.find_element(By.XPATH,("//span[contains(@class,'gtm-lead-click')]"))
        # Subscribe_now.click()
        # time.sleep(2)

        self.xp = Xpath(self.driver)
        self.xp.Newslisting_subscribenow()

        self.cta_detail()
        time.sleep(2)
        new_url=self.driver.current_url

        # if new_url == "https://staging-hz.collegedekho.com/news/?magicflag=1":
        #     self.driver.refresh()
        # else:
        #     self.driver.back()
        #     time.sleep(2)
        #     self.driver.refresh()
        #     time.sleep(4)

        if new_url == "https://www.collegedekho.com/my-dashboard/colleges":
            self.driver.back()
            time.sleep(5)
        else:
            self.driver.refresh()
            time.sleep(5)

        self.database()
        time.sleep(2)

        self.driver.close()

if  __name__ == "__main__":
    unittest.main()

    
    