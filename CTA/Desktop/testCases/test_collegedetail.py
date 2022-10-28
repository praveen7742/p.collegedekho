import time
import requests
from logs import logs
import unittest
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *

class ColDetail(Cta,logs,Baseclass):
    def test_ctacoldetail(self):           
        time.sleep(2)
        self.test_log()  
        self.driver.maximize_window()   
        time.sleep(3)
        Url = self.driver.get("https://user:pass@cd-staging-rhz.collegedekho.com/colleges/lpu")
        self.logger.info(Url)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

#Download brochure

        download_brochure = self.driver.find_element(By.XPATH,"//div[@class='CollegedekhoShareBtn_btnDownload__yOJ5w']//button[1]")
        time.sleep(2)
        self.logger.info("CTA : " + download_brochure.text)
        time.sleep(2)
        download_brochure.click()
        
        self.cta_detail()
        time.sleep(5)
        lets_begin = self.driver.find_element(By.XPATH,"//div[@class = 'collegeDekhoFollowUp_rewoardBox__sWZMH']//button")
        time.sleep(2)
        lets_begin.click()
        time.sleep(2)
        self.closeform()
        time.sleep(3)

#Apply Now
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

        self.driver.refresh()
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

