import time
import requests
import pytest
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#sys.path.append("/home/collegedekho/p.collegedekho/CTA 2")
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from pageObjects.Xpaths import Xpath
from utilities.customLogger import LogGen

class Test_ColDetail(Cta):

    baseURL4 = ReadConfig.getCareerDtlURL()
    logger = LogGen.loggen()  # Logger
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ctacoldetail(self,setup): 

        time.sleep(2)
        self.logger.info("******* Starting College CTA*********")
        self.driver = setup
        self.driver.get(self.baseURL4)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        
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
        self.driver.close()

