import time
import json
from database import *
from selenium.webdriver.common.by import By
from logs import *
import random
import string
from conftest import *
from selenium.webdriver.support.ui import Select


class Cta(logs):
    def cta_detail(self):
        time.sleep(2)
        random_name = self.random_name()
        self.driver.find_element(By.ID,"id_name_cta").send_keys(random_name)
        self.logger.info("Name : " +random_name)
        if not random_name:
            error_error = driver.find_element(By.ID,"username_error")
            print(error_error.text)
            self.logger.info(error_error.text)
        time.sleep(2)

        random_email = self.random_email()
        self.driver.find_element(By.ID,"id_email_cta").send_keys(random_email)
        time.sleep(1)
        self.logger.info("Email : " +random_email)

        random_number = self.random_phonenumber()
        self.driver.find_element(By.ID,"id_phone_cta").send_keys(random_number)
        time.sleep(2)
        self.logger.info("Phone No : " +random_number)

        try:
            stream = Select(self.driver.find_element(By.ID,"id_stream_cta"))
            stream.select_by_index(1)
            Stream = stream.first_selected_option
            self.logger.info("Pref Stream : " + Stream.text)
            time.sleep(2)
        except :
            self.logger.info("Preferred Stream field not present")
            time.sleep(2)
            pass 
        time.sleep(2)
        try:
           Preflevel =  Select(self.driver.find_element(By.ID,"id_pref_level_cta"))
           Preflevel.select_by_index(1)
           pref_Level = Preflevel.first_selected_option
           self.logger.info("Pref Level : " + pref_Level.text)
           time.sleep(2)
        except:
            self.logger.info("Preferred level field not present")
            time.sleep(2)
            pass
        time.sleep(1)
        try:
           state = Select(self.driver.find_element(By.ID,"id_state_cta"))
           state.select_by_index(1)
           State = state.first_selected_option
           self.logger.info("State : " + State.text)
           time.sleep(2)
        except:
            self.logger.info("State field not present")
            time.sleep(2)
            pass
        time.sleep(1)
        try:
           board =  Select(self.driver.find_element(By.ID,"id_board_cta"))
           board.select_by_index(1)
           Board = board.first_selected_option
           self.logger.info("Board : " + Board.text)
           time.sleep(2)
        except:
            self.logger.info("Board field not present")
            time.sleep(2)
            pass
        time.sleep(2)
       

        #OTP Functionality

        

      

        # self.driver.find_element_by_css_selector("button[type='submit']").click()
        # time.sleep(5)
        # Otp = self.driver.find_element(By.CSS_SELECTOR,"//li[@class='otp_fields otp_fields_register']//input[{}].format(int(index)+1))")
        # Otp.send_keys(otp_query_1)
       
        # return Cta()

        
        # cursor = conn.cursor()
        # cursor.execute(query)
        # row = cursor.fetchone()
        # result_dict = list(row)
        # self.logger.info(result_dict)

    def whatsapp_enabled(self):
         #Whatsapp Enabled

        Whatsapp_enabled = self.driver.find_element(By.XPATH,"(//span[@class='slider round'])[1]")
        if Whatsapp_enabled.is_enabled():
            Whatsapp_enabled.click()
            time.sleep(2)
        else:
            pass
        time.sleep(2)

    def ctaclose_button(self):
        
        #Close button
        close_button = self.driver.find_element(By.XPATH,"//div[@class = 'formInputs']/button") 
        close_button.click()
        time.sleep(2)

    def otpclose_button(self):
        
        #Close button
        closeotp_button = self.driver.find_element(By.XPATH,"//div[@class = 'column rightCol'][1]") 
        closeotp_button.click()
        self.logger.info("Otp screen closed")
        time.sleep(2)



    

       
      
    
    def footer_form(self):
        time.sleep(2)
        random_name = self.random_name()
        self.driver.find_element_by_id("id_name").send_keys(random_name)
        random_Phone = self.random_phonenumber()
        self.driver.find_element_by_id("id_phone").send_keys(random_Phone)
        time.sleep(1)
        random_Email = self.random_email()
        self.driver.find_element_by_id("id_email").send_keys(random_Email)
        time.sleep(2)
        
        try:
           state = Select(self.driver.find_element(By.ID,"id_pref_state"))
           state.select_by_index(1)
           State = state.first_selected_option
           self.logger.info("Pref State : " + State.text)
           time.sleep(2)
        except:
            self.logger.info("State field not present")
            time.sleep(2)
            pass
        time.sleep(1)
        try:
           Preflevel =  Select(self.driver.find_element(By.ID,"id_pref_level"))
           Preflevel.select_by_index(1)
           pref_Level = Preflevel.first_selected_option
           self.logger.info("Pref Level : " + pref_Level.text)
           time.sleep(2)
        except:
            self.logger.info("Preferred level field not present")
            time.sleep(2)
            pass
        time.sleep(1)

        try:
            stream = Select(self.driver.find_element(By.ID,"id_stream"))
            stream.select_by_index(1)
            Stream = stream.first_selected_option
            self.logger.info("Pref Stream : " + Stream.text)
            time.sleep(2)
        except :
            self.logger.info("Preferred Stream field not present")
            time.sleep(2)
            pass 
        time.sleep(2)

        try:
           board =  Select(self.driver.find_element(By.ID,"id_board"))
           board.select_by_index(1)
           Board = board.first_selected_option
           self.logger.info("Pref Board : " + Board.text)
           time.sleep(2)
        except:
            self.logger.info("Pref Board field not present")
            time.sleep(2)
            pass
        time.sleep(2)

        submit_button = self.driverfind_element(By.XPATH,("//input[@id='86'])[1]"))
        submit_button.click()
        self.logger.info("Footer Lead form submitted")



    def thankyou_message(self):
        time.sleep(2)
        thankyou = self.driver.find_element_by_id("common_moda_success_message")
        self.logger.info(thankyou.text)
        time.sleep(2)
        closebutton = self.driver.find_element_by_xpath("//button[@type='button']")
        closebutton.click()
        time.sleep(2)

    def random_phonenumber(self):
        
        ph_no = []

        ph_no.append(random.randint(6, 9))
        
        for i in range(1, 10):
            ph_no.append(random.randint(0, 9))
        
        number = ""
        for i in ph_no:
            print(i, end="")
            number += str(i)
        print(number)

        return number

    def random_name(self):
        return "".join(random.choices(string.ascii_lowercase, k=6))

    def random_email(self):
        random_str =  "".join(random.choice(string.ascii_letters) for _ in range(7))
        return random_str+"@gmail.com"

    
    
