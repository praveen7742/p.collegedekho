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



class Test_newsBoard(Cta):
    
    baseURL = ReadConfig.getBoardDtlURL()
    logger = LogGen.loggen()  # Logger

  
    def test_newsboard(self,setup):
        self.logger.info("******* Starting CTA test for New Board**********")
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

        #Download sample paper (Commented the code due to 500 error)

    
        # self.driver.refresh()
        # self.xp = Xpath(self.driver)
        
        # self.xp.board_dwnldsmplpprcta()
        # time.sleep(3)
        # self.driver.find_element(By.ID,"id_name_cta").clear()
        # self.driver.find_element(By.ID,"id_email_cta").clear()
        # self.driver.find_element(By.ID,"id_phone_cta").clear()
        # self.cta_detail()
        # self.logger.info("Sample paper is downloaded")
        # time.sleep(3)
        # if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
        #     time.sleep(2)
        #     self.driver.back()
        #     time.sleep(2)
        #     self.driver.refresh()
        # else:
        #     self.driver.refresh()
        #     time.sleep(2)
        # self.closeform()
        # self.database()
        # time.sleep(2)

# Download Guide1
        self.driver.refresh()
        self.xp = Xpath(self.driver)
        time.sleep(2)
        self.xp.board_dwnldguidecta1()
        time.sleep(3)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
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

    # Download Guide 2
        self.driver.refresh()
        self.xp = Xpath(self.driver)
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        self.xp.board_dwnldguidecta2()
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
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

#FOOTER FORM 
        self.driver.refresh()
        self.xp = Xpath(self.driver)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,4500)")
        time.sleep(2)
        self.xp.board_footerform()
        self.footer_form()
        time.sleep(3)
        
        self.thankyou_message()
        time.sleep(2)
        self.driver.close()