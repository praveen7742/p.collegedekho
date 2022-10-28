import time
import requests
from logs import logs
import unittest
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *


class Career(Cta,logs,Baseclass):
    def test_career(self):           
        time.sleep(2)
        self.test_log()     
        self.driver.maximize_window()
        self.driver.get("https://user:pass@staging-hz.collegedekho.com/careers/police-officer?magicflag=1")
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        # Follow career

        Follow_career = self.driver.find_element(By.XPATH,("//button[normalize-space()='Follow']"))
        time.sleep(2)
        self.logger.info("CTA : " + Follow_career.text)
        Follow_career.click()

        self.cta_detail()
        time.sleep(2)
        self.closeform()
        time.sleep(2)

        #Get Expert Help
        self.driver.execute_script("window.scrollTo(0,2800)")
        time.sleep(4)
        Get_expert_help_cta = self.driver.find_element(By.XPATH,"//div[@class='block latestUpdates']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']")
        time.sleep(2)
        self.logger.info("CTA : " + Get_expert_help_cta.text)
        time.sleep(2)
        Get_expert_help_cta.click()
        self.logger.info("Clicked on Get expert help cta")
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(2)
        self.cta_detail()
        time.sleep(2)
        self.closeform()

        #Get experts help 2
        time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0,1000)")
        Get_expert_help_2 = self.driver.find_element(By.XPATH,"//div[@class='ctaBlock footerSticky footerfixed']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']")
        time.sleep(2)
        self.logger.info("CTA : " + Get_expert_help_2.text)
        time.sleep(2)
        Get_expert_help_2.click()
        self.logger.info("Clicked on Talk to Experts 2")
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(2)

        self.cta_detail()
        time.sleep(2)
        self.closeform()
    


if  __name__ == "__main__":
    unittest.main()
