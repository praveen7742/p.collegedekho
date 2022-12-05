import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen

class Xpath():

     #HomePage Xpaths
    logger = LogGen.loggen()  # Logger
    Hmpg_Talk_to_experts = "(//button[normalize-space()='Talk to our Experts'])[1]"
    Hmpg_Footer_Form = "//div[@class = 'expertGraphic setExpertBlock']/div"
    # Exam Detail Xpaths
    ExmDtl_Exm_Alrt = "//div[@class = 'setAlert setExamAlert'][1]"
    ExmDtl_Dwnld_Btn = "//div[@class='ctaBox']//button[@class='button change-alert-text gtm-lead-click alert-button apply_now_det_cd gtm-lead-click django-button-config']"
    ExmDtl_Subscribe_Btn = "//div[@class='box']/button"
    ExmDtl_footer_cta = "//div[@class = 'expertGraphic setExpertBlock']/div"
    Newslisting_subscribenow_btn= "//span[contains(@class,'gtm-lead-click')]"
    Allnews_btn= "body > div.body > div:nth-child(5) > div.allNewsBlock.block > div.rightCol > ul > li:nth-child(1) > div > a"
    popup_click_btn= "div[class='commonForm collegesForm commomFormCustom'] div[class='formContent']"
    popup_close_btn= "div[class='formContent'] div[class='formInputs'] button[class='close']"
    Subscribe_now_news_btn = "//span[normalize-space()='Subscribe Now']"
    News_detail_subscribe_sticky_btn="#btn-cta3"
    News_detail_footer_btn = "//div[@class = 'expertGraphic setExpertBlock']/div"

    def __init__(self, driver):
        self.driver = driver
     
     #Homepage Talk to experts
    def Hp_tlk_exprt(self):
        Talk_experts = self.driver.find_element(By.XPATH, self.Hmpg_Talk_to_experts)
        Talk_experts.location_once_scrolled_into_view
        time.sleep(2)

        Talk_experts.send_keys(Keys.PAGE_UP)
        self.logger.info("CTA : " + Talk_experts.text)
        Talk_experts.click()
        time.sleep(3)

        # Homepage Footer Form
    def Hp_foot_frm(self):
        footerform = self.driver.find_element(By.XPATH,self.Hmpg_Footer_Form)
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

    #Exam Details Xpaths
    def ExmDtl_Alert(self):
        Exam_Alert = self.driver.find_element(By.XPATH,self.ExmDtl_Exm_Alrt)
        time.sleep(2)
        self.logger.info("CTA : " + Exam_Alert.text)
        time.sleep(2)
        Exam_Alert.click()
        time.sleep(2)

    def ExmDtl_dwnld(self):
        download = self.driver.find_element(By.XPATH,self.ExmDtl_Dwnld_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + download.text)
        time.sleep(2)
        download.click()
        time.sleep(2)

    def ExmDtl_Subscribe(self):

        Subscribe_now = self.driver.find_element(By.XPATH,self.ExmDtl_Subscribe_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + Subscribe_now.text)
        time.sleep(2)
        Subscribe_now.click()
        time.sleep(2)

    def ExmDtl_footer(self):

        footerform = self.driver.find_element(By.XPATH,self.ExmDtl_footer_cta)
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

    def Newslisting_subscribenow(self):

        Subscribe_now = self.driver.find_element(By.XPATH,self.Newslisting_subscribenow_btn)
        Subscribe_now.click()
        time.sleep(2)
    
    def Allnews(self):

        All_news = self.driver.find_element(By.CSS_SELECTOR,self.Allnews_btn)
        All_news.click()
        time.sleep(2)
    
    def News_detail_popup(self):

        popup_click=self.driver.find_element(By.CSS_SELECTOR,self.popup_click_btn)
        popup_click.click()
        time.sleep(2)

    def News_detail_popupclose(self):

        popup_close = self.driver.find_element(By.CSS_SELECTOR,self.popup_close_btn)
        popup_close.click()
        time.sleep(2)

    def News_detail_subscribe(self):

        Subscribe_now_news = self.driver.find_element(By.XPATH,self.Subscribe_now_news_btn)
        Subscribe_now_news.location_once_scrolled_into_view
        time.sleep(2)

        self.logger.info("CTA : " + Subscribe_now_news.text)
        Subscribe_now_news.click()

    def News_detail_subscribe_sticky(self):    
        Subscribe_now_footer = self.driver.find_element(By.CSS_SELECTOR,self.News_detail_subscribe_sticky_btn)
        Subscribe_now_footer.click()
    
    def news_detail_footer(self):
        newsfooterform = self.driver.find_element(By.XPATH,self.News_detail_footer_btn)
        newsfooterform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)