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


class Test_Career(Cta):

    baseURL3 = ReadConfig.getCareerDtlURL()
    logger = LogGen.loggen()  # Logger
    @pytest.mark.sanity
    @pytest.mark.regression

    def test_career(self,setup):           
        time.sleep(2)
        self.logger.info("******* Starting Career Detail CTA*********")
        self.driver = setup
        self.driver.get(self.baseURL3)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        time.sleep(2)
       

        # Follow career

        # Follow_career = self.driver.find_element(By.XPATH,("//button[normalize-space()='Follow']"))
        # time.sleep(2)
        # self.logger.info("CTA : " + Follow_career.text)
        # Follow_career.click()
        self.xp = Xpath(self.driver)
        self.xp.Carrer_Follow()
        self.cta_detail()
        time.sleep(4)
        if "https://user:pass@staging-hz.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)

        self.database()
        time.sleep(2)

        #Get Expert Help
        self.xp.Career_ExmAlrt()
        # self.driver.execute_script("window.scrollTo(0,2800)")
        # time.sleep(4)
    
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(2)
        self.cta_detail()
        time.sleep(4)
        if "https://user:pass@staging-hz.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)

        self.database()
        time.sleep(2)


        #Get experts help Footer sticky
        time.sleep(2)
        # self.driver.execute_script("window.scrollTo(0,1000)")
        # Get_expert_help_2 = self.driver.find_element(By.XPATH,)
        # time.sleep(2)
        # self.logger.info("CTA : " + Get_expert_help_2.text)
        # time.sleep(2)
        # Get_expert_help_2.click()
        # self.logger.info("Clicked on Talk to Experts 2")
        # time.sleep(2)

        self.xp.Career_sticky()
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(2)

        self.cta_detail()
        time.sleep(4)
        if "https://user:pass@staging-hz.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)

        self.database()
        time.sleep(2)
        self.driver.close()
    
