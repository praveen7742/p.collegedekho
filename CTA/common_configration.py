import time
import json
from conftest import *
from utilities.Baseclass import *
from selenium.webdriver.support.ui import Select

class CTA():
    def cta_detail(self):
        time.sleep(2)
        self.driver.find_element_by_id("id_name_cta").send_keys("praveen")
        self.driver.find_element_by_id("id_email_cta").send_keys("praven@cld.com")
        time.sleep(1)
        self.driver.find_element_by_id("id_phone_cta").send_keys(9384747343)
        time.sleep(2)
        try:
            stream = Select(self.driver.find_element_by_id("id_stream_cta"))
            stream.select_by_index(1)
        except :
            pass 
        time.sleep(2)
        try:
           level =  Select(self.driver.find_element_by_id("id_pref_level_cta"))
           level.select_by_index(1) 
        except:
            pass
        time.sleep(1)
        try:
           state = Select(self.driver.find_element_by_id("id_state_cta"))
           state.select_by_index(1)
        except:
            pass
        time.sleep(1)
        try:
           board =  Select(self.driver.find_element_by_id("id_board_cta"))
           board.select_by_index(1)
        except:
            pass
        time.sleep(1)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(5)

        return CTA()
    
    
    def footer_form(self):
        time.sleep(2)
        self.driver.find_element_by_id("id_name").send_keys("praveen")
        self.driver.find_element_by_id("id_phone").send_keys(8764876467)
        time.sleep(1)
        self.driver.find_element_by_id("id_email").send_keys("praveen4322@cld.com")
        time.sleep(2)
        self.driver.find_element_by_id("id_stream").send_keys("Law") 
        time.sleep(2)
        self.driver.find_element_by_id("id_pref_level").send_keys("UG") 
        time.sleep(1)
        self.driver.find_element_by_id("id_pref_state").send_keys("Delhi")
        time.sleep(1)
        self.driver.find_element_by_id("id_board").send_keys("State Board")
        time.sleep(1)
        self.driver.find_element_by_css_selector('input[id="86"]').click()
        time.sleep(5)


    def thankyou_message(self):
        time.sleep(2)
        thankyou = self.driver.find_element_by_id("common_moda_success_message")
        self.logger.info(thankyou.text)
        time.sleep(2)
        closebutton = self.driver.find_element_by_xpath("//button[@type='button']")
        closebutton.click()
        time.sleep(2)
    
    
