import time
import requests
import mysql.connector
from common_configration import Cta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.Baseclass import *



class Login(Cta,Baseclass):
    def test_login(self):           
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
        self.whatsapp_enabled()
        time.sleep(2)
       
        self.ctaclose_button()


        time.sleep(3)

        #APPLY NOW CTA
        Apply_now = self.driver.find_element(By.XPATH,("(//button[normalize-space()='Apply Now'])[1]"))
        Apply_now.location_once_scrolled_into_view
        time.sleep(2)


        Apply_now.send_keys(Keys.PAGE_UP)
       
        self.logger.info("CTA : " + Apply_now.text)
        time.sleep(2)
        Apply_now.click()
        self.logger.info("Clicked on Apply now cta")
       
        self.cta_detail()
        self.ctaclose_button()

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


     

        # generate_otpbutton = self.driver.find_element(By.ID,"gtm_loginGenerateOtp")
        # generate_otpbutton.click()
        # time.sleep(5)

        # parser = ConfigParser()
        # parser.read('Login.ini')



        conn = mysql.connector.connect(host='95.217.156.247',database = 'cld22apr22',user = 'ro', password = 'readonly@5456555')
        self.logger.info(conn)
        time.sleep(5)
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



        
       