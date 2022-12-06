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

class Test_coursedetail(Cta):
    
    baseURL = ReadConfig.getCoursedetailURL()
    logger = LogGen.loggen()  # Logger

  
    def test_coursedetaill(self,setup):
        self.logger.info("******* Starting CTA test for CourseDetail**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        if actual_title == "B Tech Course - Fees, Syllabus, Courses List, Subjects, Salary & Scope":
            assert True
        else:
            assert False
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        self.xp = Xpath(self.driver)
        self.xp.CourseDtl_Chk_Eligibility()
        time.sleep(5)
        self.cta_detail()
        time.sleep(15)

        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
        else:
            self.driver.refresh()
            time.sleep(15)

        self.database()
        time.sleep(5)

        self.driver.close()

if  __name__ == "__main__":
    unittest.main()