import mysql.connector
import pytest
from selenium.webdriver.common.by import By
from logs import *
from Desktop.test_deskhomepage import Login
import time
# # from tabulate import tabulate

class Database(Login):
    def test_database(self):
        # conn = mysql.connector.connect(host='172.31.35.54',database = 'collegedekho',user = 'cld_ro', password = 'cld9^%67&G')
        # self.logger.info(conn)

        
        # conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho_17may22',user = 'ro', password = 'readonly@5456555')
        # self.logger.info(conn)
        conn = mysql.connector.connect(host='95.217.156.247',database = 'cld22apr22',user = 'ro', password = 'readonly@5456555')
        self.logger.info(conn)

        query = ("""SELECT uup.added_on,
        uup.id as "user_id",
        uup.name,
        uup.phone_no,
        uup.email,
        uup.state_id,
        uup.board,
        uup.user_city_id,
        iis.institute_id,
        iis.college_action,
        ua.button_id,
        uupp.preferred_stream_id,
        uupp.preferred_level
        FROM users_userprofile AS uup
        LEFT JOIN users_userpreferences AS uupp ON uupp.user_id = uup.id
        LEFT JOIN users_activity AS ua ON ua.user_id = uup.id
        left join institute_instituteshortlist as iis on iis.user_id = uup.id
        order by uup.id limit 5 """).format(self.random_phonenumber)
        
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        result_dict = list(row)
        self.logger.info(result_dict)
            
        otp_query_1 = ("""select * from users_otp where phone_no = {}""").format(self.random_phonenumber)
        cursor = conn.cursor()
        cursor.execute(otp_query_1)
        row = cursor.fetchall()
        result_dict = list(row)
        self.logger.info(result_dict)
        try:
            for index, value in enumerate(result_dict):
                otp_1_new = self.driver.find_element(By.XPATH,"//li[@class='CollegedekhoNavBar_otpFields__Xb_KM']//input[{}]".format(int(index)+1))
                otp_1_new.send_keys(value)
                time.sleep(5)
        except:
            for index, value in enumerate(result_dict):
                otp_1_new = self.driver.find_element(By.XPATH,"//input[@name='first'])[{}]".format(int(index)+1))
                otp_1_new.send_keys(value)
                time.sleep(5)
        

        
        # profile_query_2 = ("""select * from users_userprofile where phone = {}""".format(random_number))
        # cursor = conn.cursor()
        # cursor.execute(profile_query_2)
        # row_1 = cursor.fetchone()
        # result_dict_1 = list(row_1)
        # self.logger.info(result_dict_1)

    #STAGING DATABASE CONNECTION

    def staging_database(self): 
        conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho_17may22',user = 'ro', password = 'readonly@5456555')
        self.logger.info(conn)
        time.sleep(2)
        query = ("""select code,phone_no from users_otp where phone_no = {} order by id desc""").format(random_number)
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        result_dict = list(row)
        self.logger.info(result_dict)
        
        #OTP Functionality


        try:
            for index, value in enumerate(result_dict):
                otp_1_new = self.driver.find_element(By.CSS_SELECTOR,"//li[@class='otp_fields otp_fields_register']//input[{}]".format(int(index)+1))
                otp_1_new.send_keys(value)
                time.sleep(5)

        except:
            for index, value in enumerate(result_dict):
                time.sleep(2)
                otp_1_new = self.driver.find_element(By.XPATH,"(//input[@placeholder='-'])[1]".format(int(index)+1))
                otp_1_new.send_keys(value)
                time.sleep(3)
    
        
        self.logger.info("Otp added successfully")
        time.sleep(2)

        #Clicking on verify button

        verify_button = self.driver.find_element(By.XPATH,"//input[@id='gtm_loginVerify']")
        verify_button.click()
        time.sleep(5)

            
