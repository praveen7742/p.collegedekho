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



class Test_newsdetail(Cta):
    
    baseURL = ReadConfig.getNewsDtlURL()
    logger = LogGen.loggen()  # Logger

  
    def test_newsdetail(self,setup):
        self.logger.info("******* Starting CTA test for NewsDetail**********")
        self.driver = setup
        self.driver.get(self.baseURL)
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

    
        self.driver.refresh()
        self.xp = Xpath(self.driver)
        self.xp.Newsdtl_setexamalert11()
        time.sleep(3)
        self.cta_detail()
        time.sleep(3)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)
        self.closeform()
        self.database()
        time.sleep(2)

# GET SAMPLE PAPERS

        self.xp = Xpath(self.driver)
        self.xp.Newsdtl_getsmplppr()
        time.sleep(3)
        self.cta_detail()
        time.sleep(3)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)
        self.closeform()
        self.database()
        time.sleep(2)