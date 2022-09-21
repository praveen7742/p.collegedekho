import time
import requests
from logs import logs
import unittest
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *

class Login(Cta,logs,Baseclass):
    def test_login(self):           
        time.sleep(2)
        self.test_log()     
        self.driver.maximize_window()
        self.driver.get("https://user:pass@staging-hz.collegedekho.com/btech-colleges-in-india/?magicflag=1")
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        # Apply now

        Course_apply_now = self.driver.find_element(By.XPATH,("//div[@class='col-md-12 first-box']//button[@role='button'][normalize-space()='Apply Now']"))
        # Course_apply_now.location_once_scrolled_into_view
        time.sleep(2)

        # Talk_experts.send_keys(Keys.PAGE_UP)
        self.logger.info("CTA : " + Course_apply_now.text)
        Course_apply_now.click()

        self.cta_detail()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        #Get Free Counselling CTA
        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(4)
        Get__free_counselling_listing = self.driver.find_element(By.CSS_SELECTOR,".apply_now_det_cd.django-button-config.gtm-lead-click[data-insti-id='2820']")
        time.sleep(2)
        self.logger.info("CTA : " + Get__free_counselling_listing.text)
        time.sleep(2)
        Get__free_counselling_listing.click()
        self.logger.info("Clicked on Get free counselling cta")
        time.sleep(2)
        self.cta_detail()
        time.sleep(2)
        self.closeform()

        #Download Brochure CTA

        time.sleep(2)
        Download_Brochure = self.driver.find_element(By.CSS_SELECTOR,".apply_now_det_cd.django-button-config.gtm-lead-click.download-brochure[data-insti-id='2247']")
        time.sleep(2)
        self.logger.info("CTA : " + Download_Brochure.text)
        time.sleep(2)
        Download_Brochure.click()
        self.logger.info("Clicked on Download brochure cta")
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()
        time.sleep(2)
        self.closeform()

        # if os.path.isfile("home/yashdhamija/Downloads/Indian Institute of Technology.pdf"):
        #     self.logger.info("File download is completed")


        #shortlist
        time.sleep(2)
        Shortlist_Listing = self.driver.find_element(By.XPATH,"(//button[@role='button'][normalize-space()='Shortlist'])[1]")
        time.sleep(2)
        self.logger.info("CTA : " + Shortlist_Listing.text)
        time.sleep(2)
        Shortlist_Listing.click()
        self.logger.info("Clicked on Shortlist Listing cta")
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()
        time.sleep(2)
        self.closeform()

        #Talk to our experts
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)")
        Talk_to_experts = self.driver.find_element(By.XPATH,"//button[normalize-space()='Talk to our Experts']")
        time.sleep(2)
        self.logger.info("CTA : " + Talk_to_experts.text)
        time.sleep(2)
        Talk_to_experts.click()
        self.logger.info("Clicked on Talk to Experts")
        time.sleep(2)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(2)

        self.cta_detail()
        time.sleep(2)
        self.closeform()

        #FOOTER FORM

        footerform = self.driver.find_element(By.CSS_SELECTOR,"div[class='expertGraphic setExpertBlock'] div[class='head']")
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

       
        self.footer_form()
        time.sleep(3)
        
        self.thankyou_message()
        time.sleep(2)




if  __name__ == "__main__":
    unittest.main()