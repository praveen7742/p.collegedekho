import time
import requests
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#sys.path.append("/home/collegedekho/p.collegedekho/CTA 2")
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import *



class Test_001(Cta):
    
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger


    def test_cta_homepage(self,setup):
        self.logger.info("******* Starting CTA TEST HOMEPAGE**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        if actual_title == "Find Top Colleges & Universities in India | Explore Courses, Exams, Admissions & Latest News":
            assert True
        else:
            assert False
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

        self.cta_detail()
        self.closeform()
        time.sleep(2)

        #APPLY NOW CTA
        Apply_now = self.driver.find_element(By.XPATH,("(//button[normalize-space()='Apply Now'])[1]"))
        Apply_now.location_once_scrolled_into_view
        time.sleep(2)


        Apply_now.send_keys(Keys.PAGE_UP)
       
        self.logger.info("CTA : " + Apply_now.text)
        time.sleep(2)
        Apply_now.click()
        self.logger.info("Clicked on Apply now cta")
        time.sleep(2)

        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()

       
        self.cta_detail()
        time.sleep(2)
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




        
        # otp_query_1 = ("""select * from users_otp where phone_no = {} order by id desc""".format(parser.get('otplogin', 'Number_range_5')))
        # cursor = conn.cursor()
        # cursor.execute(otp_query_1)
        # row = cursor.fetchone()
        # result_dict = list(row)
        # self.logger.info(result_dict[2])
        # otp_value = [int(x) for x in str(result_dict[2])]
        # try:
        #     for index, value in enumerate(otp_value):
                    
        #         otp_1 = self.driver.find_element(By.XPATH,"(//input[@placeholder='-'])//input[{}]".format(int(index)+1))
        #         otp_1.send_keys(value)
        #         time.sleep(5)
                    
        # except Exception as e:

        #     self.logger.info(e)
        #     for index, value in enumerate(result_dict):
        #         otp_1_new = self.driver.find_element(By.XPATH,"//input[@name='first'])[{}]".format(int(index)+1))
        #         otp_1_new.send_keys(value)
        #         time.sleep(5)
            
        #     verify_button = self.driver.find_element(By.ID,"gtm_loginVerify")
        #     verify_button.click()
        #     time.sleep()

if  __name__ == "__main__":
    unittest.main()

    
    