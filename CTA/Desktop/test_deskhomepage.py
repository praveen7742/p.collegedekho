from lib2to3.pgen2.driver import Driver
import time
from logs import *
import requests
from common_configration import *
from conftest import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Login(logs,Baseclass):
    def test_login(self):
        self.test_log()             #log setup
    
        time.sleep(2)       
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        #Talk to expert 1 cta
        # driver.execute_script("window.scrollTo(0, 2700)") 
        # time.sleep(2)
        #object of Actions class to scroll up and down
        # action = ActionChains(driver)
        # action.sendKeys(Keys.PAGE_DOWN).perform()


        Talk_experts = self.driver.find_element(By.XPATH,("(//button[normalize-space()='Talk to our Experts'])[1]"))
        Talk_experts.location_once_scrolled_into_view
        time.sleep(2)

        Talk_experts.send_keys(Keys.PAGE_UP)
        self.logger.info(Talk_experts.text)
        Talk_experts.click()
        time.sleep(3)
        self.logger.info(Talk_experts.get_attribute("class"))
        time.sleep(2)
        self.cta_detail(self.driver)
        time.sleep(3)

        #Whatsapp Enabled button

        # Whatsapp_enabled = driver.find_element(By.XPATH,("//span[@class="slider round"]")).isEnabled())


        # APPLY NOW

        # Apply_now1 = driver.find_element(By.XPATH,"//button[normalize-space()='Apply Now'])[1]"

        # Footer form

        # Footer_form1 = driver.find_element(By.XPATH,"//div[normalize-space()='Want to learn more about college options and to secure an admission now!'])[1]"





        
       