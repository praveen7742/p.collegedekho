import time
import requests
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_examlisting(Cta):
    baseURL = ReadConfig.getHomepageURL()
    logger = LogGen.loggen()  # Logger

    def test_ctaexamlist(self):           
        time.sleep(2)
        self.test_log()  
        self.driver.maximize_window()   
        time.sleep(3)
        Url = self.driver.get("https://user:pass@staging-hz.collegedekho.com/engineering-entrance-exams/?magicflag=1")
        self.logger.info(Url)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

#Set Exam Alert

        exam_Alert = self.driver.find_element(By.XPATH,"(//span[@class='button gtm-lead-click apply_now_det_cd ex_list change-alert-text'][normalize-space()='Set Exam Alert'])[1]")
        time.sleep(2)
        self.logger.info("CTA : " + exam_Alert.text)
        time.sleep(2)
        exam_Alert.click()
        
        self.cta_detail()

        self.driver.back()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
        self.logger.info("Page refreshed successfully")
        time.sleep(5)

        exam_Alert2 = self.driver.find_element(By.XPATH,"//span[@data-exam_id= 1015]")
        exam_Alert2.location_once_scrolled_into_view
        time.sleep(3)
        exam_Alert2.click()
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        self.cta_detail()

        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
        self.logger.info("Page refreshed successfully")
        time.sleep(5)
