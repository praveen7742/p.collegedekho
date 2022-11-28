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
    
    baseURL = ReadConfig.getNewslistingUrl()
    logger = LogGen.loggen()  # Logger

  
    def test_newsdetail(self,setup):
        self.logger.info("******* Starting CTA test for Newslisting**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("-------------------------")
        actual_title = self.driver.title
        self.logger.info(actual_title)
        time.sleep(2)
        current_url = self.driver.current_url
        self.logger.info("Current_Url : " + current_url)
        response = requests.get(current_url)
        self.logger.info("Response : " + str(response.status_code))
        
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0,1150)","")
        time.sleep(2)

        # All_news = self.driver.find_element(By.CSS_SELECTOR,("body > div.body > div:nth-child(5) > div.allNewsBlock.block > div.rightCol > ul > li:nth-child(1) > div > a"))
        # All_news.click()
        self.xp = Xpath(self.driver)
        self.xp.Allnews()
        # new_url = self.driver.current_url
        self.logger.info("Current_Url : " + new_url)
        time.sleep(15)

        # popup_click=self.driver.find_element(By.CSS_SELECTOR,("div[class='commonForm collegesForm commomFormCustom'] div[class='formContent']"))
        # popup_click.click()
        self.xp.News_detail_popup()
        time.sleep(5)
        self.cta_detail()
        time.sleep(15)
        # refreshed_url = self.driver.current_url
        
        # if refreshed_url == new_url:
        #     self.driver.refresh()
        #     time.sleep(15)
        # else:
        #     self.driver.back()
        #     time.sleep(2)
        #     self.driver.refresh()
        #     time.sleep(15)

        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(15)
        else:
            self.driver.refresh()
            time.sleep(15)
        
        self.database()
        time.sleep(2)

        # popup_close = self.driver.find_element(By.CSS_SELECTOR,("div[class='formContent'] div[class='formInputs'] button[class='close']"))
        # popup_close.click()

        self.xp.News_detail_popup_close()

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
        self.cta_detail()
        time.sleep(20)

        # refreshed_url_1 = self.driver.current_url
        
        # if refreshed_url_1 == new_url:
        #     self.driver.refresh()
        #     time.sleep(15)
        # else:
        #     self.driver.back()
        #     time.sleep(2)
        #     self.driver.refresh()
        #     time.sleep(15)
    
        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(15)
        else:
            self.driver.refresh()
            time.sleep(15)
        
        self.database()
        time.sleep(2)

        # popup_close = self.driver.find_element(By.CSS_SELECTOR,("div[class='formContent'] div[class='formInputs'] button[class='close']"))
        # popup_close.click()

        self.xp.News_detail_popup_close()



        # Subscribe_now_footer = self.driver.find_element(By.XPATH,"//button[contains(text(),'Subscribe Now')]")
        # Subscribe_now_footer.click()
        self.xp.News_detail_subscribe_footer()

        time.sleep(5)
        self.driver.find_element(By.ID,"id_name_cta").clear()
        self.driver.find_element(By.ID,"id_email_cta").clear()
        self.driver.find_element(By.ID,"id_phone_cta").clear()
        self.cta_detail()
        time.sleep(15)

        # refreshed_url_2 = self.driver.current_url
        
        # if refreshed_url_2 == new_url:
        #     self.driver.refresh()
        #     time.sleep(15)
        # else:
        #     self.driver.back()
        #     time.sleep(2)
        #     self.driver.refresh()
        #     time.sleep(15)

        if "https://www.collegedekho.com/my-dashboard/colleges" in self.driver.current_url:
            self.driver.back()
            time.sleep(15)
        else:
            self.driver.refresh()
            time.sleep(15)
        
        self.database()
        time.sleep(2)

        # footerform = self.driver.find_element(By.XPATH,"//div[@class = 'expertGraphic setExpertBlock']/div")
        # footerform.location_once_scrolled_into_view
        # time.sleep(2)
        # self.logger.info("Scrolled into footer form")
        # time.sleep(4)

        self.xp.Hp_foot_frm()
        self.footer_form()
        time.sleep(3)
        
        self.thankyou_message()
        time.sleep(2)

        self.database()
        time.sleep(2)

        

        self.driver.close()

if  __name__ == "__main__":
    unittest.main()
