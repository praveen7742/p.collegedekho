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
    ExmLstng_ExmAlrt_btn = "(//span[@class='button gtm-lead-click apply_now_det_cd ex_list change-alert-text'][normalize-space()='Set Exam Alert'])[1]"
    CareerDtl_follow_Btn= "(//button[normalize-space()='Follow'])[1]"
    CareerDtl_ExmAlrt_Btn = "//div[@class='block latestUpdates']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']"
    CareerDtl_Footersticky = "//div[@class='ctaBlock footerSticky footerfixed']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']"
    CollegeDtl_Dwnl_btn =   "//div[@class='CollegedekhoShareBtn_btnDownload__yOJ5w']//button[1]"
    CollegeDtl_dwnld_brchre_Btn = "//div[@class='CollegedekhoShareBtn_btnDownload__yOJ5w']//button[1]"
    CollegeDtl_apply_now_Btn = "//div[@class='ctaBox']/button"
    CollegeDtl_SubscribeNow_Btn = "//div[@class='box']/button"
    CollegeDtl_footer_sticky = "//div[@class = 'expertGraphic setExpertBlock']/div"
    NewsDtl_exam_alrt = "//button[@id='gtm-board-set-exam-alert']"
    NewsDtl_Getsampleppr = "(//button[contains(text(),'Get Sample Papers')])[1]"
    NewsDtl_subscribenow = "(//button[@id='btn-cta21'])[1]"
    NewsDtl_registernow = "(//button[@id='btn-cta3'])[1]"
    Board_smplppr = "(//button[@id='gtm-board-download-sample-paper'])[1]"
    Board_Dwnldguide = "(//button[@id='gtm-board-download-guide'])[1]"
    Board_Dwnldguide2 = "(//button[@id='gtm-board-download-guide'])[2]"
    Board_Footerformcta = "(//div[normalize-space()='Want to learn more about college options and to secure an admission now!'])[1]"





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
        
    def ExmListing_EXmAlrt(self):
        time.sleep(2)
        exam_Alert = self.driver.find_element(By.XPATH,self.ExmLstng_ExmAlrt_btn)
        time.sleep(2)
        self.logger.info("CTA : " + exam_Alert.text)
        time.sleep(2)
        exam_Alert.click()

    def Carrer_Follow(self):

        time.sleep(2)
        Follow_career = self.driver.find_element(By.XPATH,self.CareerDtl_follow_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + Follow_career.text)
        Follow_career.click()

    def Career_ExmAlrt(self):

        self.driver.execute_script("window.scrollTo(0,2800)")
        time.sleep(4)
        Get_expert_help_cta = self.driver.find_element(By.XPATH,self.CareerDtl_ExmAlrt_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + Get_expert_help_cta.text)
        time.sleep(2)
        Get_expert_help_cta.click()
        self.logger.info("Clicked on Get expert help cta")
        time.sleep(2)

    def Career_sticky(self):

        self.driver.execute_script("window.scrollTo(0,1000)")
        Get_expert_help_2 = self.driver.find_element(By.XPATH,self.CareerDtl_Footersticky)
        time.sleep(2)
        self.logger.info("CTA : " + Get_expert_help_2.text)
        time.sleep(2)
        Get_expert_help_2.click()
        self.logger.info("Clicked on Talk to Experts Footer sticky")
        time.sleep(2)

    def Collegedtl_DwnldBchre(self):
        download_brochure = self.driver.find_element(By.XPATH,self.CollegeDtl_dwnld_brchre_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + download_brochure.text)
        time.sleep(2)
        download_brochure.click()

    def Collegedtl_applynow(self):
        download = self.driver.find_element(By.XPATH,self.CollegeDtl_apply_now_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + download.text)
        time.sleep(2)
        
        download.click()
        time.sleep(2)

    def Collegedtl_subscribenow(self):
        Subscribe_now = self.driver.find_element(By.XPATH,self.CollegeDtl_SubscribeNow_Btn)
        time.sleep(2)
        self.logger.info("CTA : " + Subscribe_now.text)
        time.sleep(2)
        Subscribe_now.click()
        time.sleep(2)

    def Collegedtl_footerform(self):

        footerform = self.driver.find_element(By.XPATH,self.CollegeDtl_footer_sticky)
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

    def Newsdtl_setexamalert11(self):
        Exam_Alert = self.driver.find_element(By.XPATH,self.NewsDtl_exam_alrt)
        time.sleep(2)
        self.logger.info("CTA : " + Exam_Alert.text)
        time.sleep(2)
        Exam_Alert.click()

    def Newsdtl_getsmplppr(self):
        Sample_ppr = self.driver.find_element(By.XPATH,self.NewsDtl_Getsampleppr)
        time.sleep(2)
        self.logger.info("CTA : " + Sample_ppr.text)
        time.sleep(2)
        Sample_ppr.click()

    def board_dwnldsmplpprcta(self):
        Sample_ppr = self.driver.find_element(By.XPATH,self.Board_smplppr)
        time.sleep(2)
        self.logger.info("CTA : " + Sample_ppr.text)
        time.sleep(2)
        Sample_ppr.click()

    def board_dwnldguidecta1(self):
        Dwnld_guide= self.driver.find_element(By.XPATH,self.Board_Dwnldguide)
        time.sleep(2)
        self.logger.info("CTA : " + Dwnld_guide.text)
        time.sleep(2)
        Dwnld_guide.click()

    def board_dwnldguidecta2(self):
        Dwnld_guide2 = self.driver.find_element(By.XPATH,self.Board_Dwnldguide2)
        time.sleep(2)
        self.logger.info("CTA : " + Dwnld_guide2.text)
        time.sleep(2)
        Dwnld_guide2.click()

    def board_footerform(self):
        self.driver.execute_script("window.scrollBy(0,4500)")
        time.sleep(2)
        Board_Footer = self.driver.find_element(By.XPATH,self.Board_Footerformcta)
        time.sleep(2)
        self.logger.info("CTA : " + Board_Footer.text)
        time.sleep(2)
        Board_Footer.click()
        
    def CourseDtl_Chk_Eligibility(self):

        course_eligib = self.driver.find_element(By.XPATH,self.CourseDtl_Chk_Eligibility_btn)
        course_eligib.click()
        time.sleep(2)
    
    
