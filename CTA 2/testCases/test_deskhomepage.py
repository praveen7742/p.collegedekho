import time
import requests
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#sys.path.append("/home/collegedekho/p.collegedekho/CTA 2")
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import *



class Test_deskhomepage(unittest.TestCase,Cta):
    
    baseURL = ReadConfig.getHomepageURL()
    logger = LogGen.loggen()  # Logger

    
    def test_cta_homepage(self,setup):
        self.logger.info("******* Starting CTA TEST HOMEPAGE**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        if actual_title == "Find Top Colleges & Universities in India | Explore Courses, Exams, Admissions & Latest News":
            assert True
        else:
            assert False
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

  
        Talk_experts = self.driver.find_element(By.XPATH,("(//button[normalize-space()='Talk to our Experts'])[1]"))
        Talk_experts.location_once_scrolled_into_view
        time.sleep(2)

        Talk_experts.send_keys(Keys.PAGE_UP)
        self.logger.info("CTA : " + Talk_experts.text)
        Talk_experts.click()

        self.cta_detail()
        time.sleep(5)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
        else:
            self.driver.refresh()
            time.sleep(2)
        
        self.database()
        time.sleep(2)

        #FOOTER FORM

        footerform = self.driver.find_element(By.XPATH,"//div[@class = 'expertGraphic setExpertBlock']/div")
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

       
        self.footer_form()
        time.sleep(3)
        
        self.thankyou_message()
        time.sleep(2)

        self.database()
        time.sleep(2)
        
        

if  __name__ == "__main__":
    unittest.main()

    
    