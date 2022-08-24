import mysql.connector
import time
# # from tabulate import tabulate

class Database():
    def test_database(self):
        # conn = mysql.connector.connect(host='172.31.35.54',database = 'collegedekho',user = 'cld_ro', password = 'cld9^%67&G')
        # self.logger.info(conn)

        
        conn = mysql.connector.connect(host='95.217.156.247',database = 'collegedekho_17may22',user = 'ro', password = 'readonly@5456555')
        self.logger.info(conn)
            
        otp_query_1 = ("""select * from users_otp where phone_no = 8619007372""")
        cursor = conn.cursor()
        cursor.execute(otp_query_1)
        row = cursor.fetchall()
        result_dict = list(row)
        self.logger.info(result_dict)
        # try:
        #     for index, value in enumerate(result_dict):
                #new
        #         otp_1 = driver.find_element(By.XPATH,"//li[@class='CollegedekhoNavBar_otpFields__Xb_KM']//input[{}]".format(int(index)+1))
        #         otp_1.send_keys(value)
        #         time.sleep(5)
        # except:
        #     for index, value in enumerate(result_dict):
                    #new
        #         otp_1_new = driver.find_element(By.XPATH,"//input[@name='first'])[{}]".format(int(index)+1))
        #         otp_1_new.send_keys(value)
        #         time.sleep(5)
        

        
        # profile_query_2 = ("""select * from users_userprofile where phone = {}""".format(random_number))
        # cursor = conn.cursor()
        # cursor.execute(profile_query_2)
        # row_1 = cursor.fetchone()
        # result_dict_1 = list(row_1)
        # self.logger.info(result_dict_1)
            

