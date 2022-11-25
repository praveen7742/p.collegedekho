import time
import requests
import unittest
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.Xpaths import Xpath

class Test_examlisting(Cta):
    baseURL2 = ReadConfig.getEXamListingURL()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_ctaexamlist(self,setup):           
        time.sleep(2)
        self.logger.info("******* Starting Exam Listing CTA*********")
        self.driver = setup
        self.driver.get(self.baseURL2)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        time.sleep(2)

#Set Exam Alert

        # exam_Alert = self.driver.find_element(By.XPATH,)
        # time.sleep(2)
        # self.logger.info("CTA : " + exam_Alert.text)
        # time.sleep(2)
        # exam_Alert.click()
        self.xp = Xpath(self.driver)
        self.xp.ExmListing_EXmAlrt()
        
        self.cta_detail()

        time.sleep(3)
        if "https://user:pass@staging-hz.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)
        
        self.database()
        time.sleep(2)
        self.driver.close()
       

       

