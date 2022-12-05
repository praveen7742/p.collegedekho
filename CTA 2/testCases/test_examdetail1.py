import time
import requests
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#sys.path.append("/home/collegedekho/p.collegedekho/CTA 2")
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from pageObjects.Xpaths import Xpath
from utilities.customLogger import LogGen

class Test_ExamDetail2(Cta):

    baseURL1 = ReadConfig.getExamDetailURL()
    logger = LogGen.loggen()  # Logger
   
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ctaexamdetail(self,setup):           
        self.logger.info("******* Starting CTA Exam Detail*********")
        self.driver = setup
        self.driver.get(self.baseURL1)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

#Set Exam Alert

        # Exam_Alert = self.driver.find_element(By.XPATH,"//div[@class = 'setAlert setExamAlert'][1]")
        # time.sleep(2)
        # self.logger.info("CTA : " + Exam_Alert.text)
        # time.sleep(2)
        # Exam_Alert.click()
        
        self.xp = Xpath(self.driver)
        self.xp.ExmDtl_Alert()
        self.cta_detail()
        time.sleep(7)
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

#Download button
        # download = self.driver.find_element(By.XPATH,"//div[@class='ctaBox']//button[@class='button change-alert-text gtm-lead-click alert-button apply_now_det_cd gtm-lead-click django-button-config']")
        # time.sleep(2)
        # self.logger.info("CTA : " + download.text)
        # time.sleep(2)
        
        # download.click()
        # time.sleep(2)
        self.xp = Xpath(self.driver)
        self.xp.ExmDtl_dwnld()
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()
        time.sleep(3)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)
        self.closeform()
        self.database()
        time.sleep(2)

#Subscribe now cta

        # Subscribe_now = self.driver.find_element(By.XPATH,"//div[@class='box']/button")
        # time.sleep(2)
        # self.logger.info("CTA : " + Subscribe_now.text)
        # time.sleep(2)
        # Subscribe_now.click()
        # time.sleep(2)
        self.xp = Xpath(self.driver)
        self.xp.ExmDtl_Subscribe()
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

        self.cta_detail()
        time.sleep(5)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
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

        # footerform = self.driver.find_element(By.XPATH,"//div[@class = 'expertGraphic setExpertBlock']/div")
        # footerform.location_once_scrolled_into_view
        # time.sleep(2)
        # self.logger.info("Scrolled into footer form")
        # time.sleep(4)
        self.xp = Xpath(self.driver)
        self.xp.ExmDtl_footer()
        self.footer_form()
        time.sleep(2)
        time.sleep(3)
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
            self.driver.refresh()
        else:
            self.driver.refresh()
            time.sleep(2)
        
        self.thankyou_message()
        time.sleep(2)
        self.database()
        time.sleep(2)
        self.driver.close()












