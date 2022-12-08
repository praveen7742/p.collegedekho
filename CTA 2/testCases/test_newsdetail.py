import time
import requests
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageObjects.common_configuration import Cta
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import *
from pageObjects.Xpaths import Xpath



class Test_newsdetail(Cta):
    
    baseURL7 = ReadConfig.getNewsDtlURL()
    logger = LogGen.loggen()  # Logger

  
    def test_newsdetail(self,setup):
        self.logger.info("******* Starting CTA test for NewsDetail**********")
        self.driver = setup
        self.driver.get(self.baseURL7)
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

    
        self.driver.refresh()
        self.xp = Xpath(self.driver)
        self.xp.Allnews()
        new_url = self.driver.current_url
        self.logger.info("Current_Url : " + new_url)
        time.sleep(20)

        # popup_click=self.driver.find_element(By.CSS_SELECTOR,("div[class='commonForm collegesForm commomFormCustom'] div[class='formContent']"))
        # popup_click.click()

        try:
            self.xp.News_detail_popup()
            time.sleep(5)
            self.cta_detail()
            time.sleep(15)
            refreshed_url = self.driver.current_url
            self.logger.info("Current_Url : " + refreshed_url)
        
            if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
                self.driver.back()
                time.sleep(2)
            else:
                self.driver.refresh()
                time.sleep(15)
        
            self.database()
            time.sleep(5)
        
        except:
            pass

        # popup_close = self.driver.find_element(By.CSS_SELECTOR,("div[class='formContent'] div[class='formInputs'] button[class='close']"))
        # popup_close.click()
        try:
            self.xp.News_detail_popupclose()
            time.sleep(5)
        except:
            pass

        # Subscribe_now_news = self.driver.find_element(By.XPATH,("//span[normalize-space()='Subscribe Now']"))
        # Subscribe_now_news.location_once_scrolled_into_view
        # time.sleep(2)

        # self.logger.info("CTA : " + Subscribe_now_news.text)
        # Subscribe_now_news.click()

        
        self.xp.News_detail_subscribe()
    
        time.sleep(5)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(10)
        self.cta_detail()
        time.sleep(20)
    
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
        else:
            self.driver.refresh()
            time.sleep(15)
        
        self.database()
        time.sleep(2)
        
        # popup_close = self.driver.find_element(By.CSS_SELECTOR,("div[class='formContent'] div[class='formInputs'] button[class='close']"))
        # popup_close.click()

        try:
            self.xp.News_detail_popupclose()
            time.sleep(5)
        except:
            pass


        # Subscribe_now_footer = self.driver.find_element(By.XPATH,"//div[@class='ctaBlock footerSticky footerfixed']//button[@id='btn-cta21']")
        # Subscribe_now_footer.click()
        self.driver.execute_script("window.scrollBy(0,150)","")
        time.sleep(15)
        
        self.xp.News_detail_subscribe_sticky()

        time.sleep(5)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        time.sleep(5)
        self.cta_detail()
        time.sleep(20)

        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(2)
        else:
            self.driver.refresh()
            time.sleep(15)
            
        self.database()
        time.sleep(2)

        try:
            self.xp.News_detail_popupclose()
            time.sleep(5)
        except:
            pass

        # self.driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(10)

        self.xp.news_detail_footer()
        self.footer_form()
        time.sleep(3)
        
        self.thankyou_message()
        time.sleep(2)

        self.database()
        time.sleep(2)