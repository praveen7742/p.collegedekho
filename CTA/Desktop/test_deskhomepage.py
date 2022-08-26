import time
from logs import *
import requests
from setting import *
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *



class Login(Cta,logs,Baseclass):
    def test_login(self):
        self.test_log()            
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
        time.sleep(3)
        self.logger.info("CTA Class: " + Talk_experts.get_attribute("class"))
        time.sleep(2)
        self.cta_detail()
        time.sleep(2)

        

        

        #Whatsapp Enabled button

        # Whatsapp_enabled = driver.find_element(By.XPATH,("//span[@class="slider round"]")).isEnabled())


        # APPLY NOW

        # Apply_now1 = driver.find_element(By.XPATH,"//button[normalize-space()='Apply Now'])[1]"

        # Footer form

        # Footer_form1 = driver.find_element(By.XPATH,"//div[normalize-space()='Want to learn more about college options and to secure an admission now!'])[1]"





        
       