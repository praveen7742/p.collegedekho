import time
import requests
from logs import logs
import unittest
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *



class Exam(Cta,logs,Baseclass):
    def test_ctaexam(self):           
        time.sleep(2)
        self.test_log()  
        self.driver.maximize_window()   
        self.driver.get("https://user:pass@staging-hz.collegedekho.com/exam/jee-main/registration-eligibility?magicflag=1")
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        Exam_Alert = self.driver.find_element(By.XPATH,"//div[@class = 'setAlert setExamAlert'][1]")
        time.sleep(2)
        self.logger.info("CTA : " + Exam_Alert.text)
        time.sleep(2)
        Exam_Alert.click()
        
        self.cta_detail()

        self.closeform()
        time.sleep(3)

#Download button
        download = self.driver.find_element(By.XPATH,"//div[@class='ctaBox']/button")
        time.sleep(2)
        self.logger.info("CTA : " + download.text)
        time.sleep(2)
        download.click()
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()
        self.closeform()
        time.sleep(2)

#Subscribe now cta

        Subscribe_now = self.driver.find_element(By.XPATH,"//div[@class='box']/button")
        time.sleep(2)
        self.logger.info("CTA : " + Subscribe_now.text)
        time.sleep(2)
        Subscribe_now.click()
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()

        self.closeform()
        time.sleep(2)





       


