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
    ExmLstng_ExmAlrt_btn = "(//span[@class='button gtm-lead-click apply_now_det_cd ex_list change-alert-text'][normalize-space()='Set Exam Alert'])[1]"
    CareerDtl_follow_Btn= "(//button[normalize-space()='Follow'])[1]"
    CareerDtl_ExmAlrt_Btn = "//div[@class='block latestUpdates']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']"
    CareerDtl_Footersticky = "//div[@class='ctaBlock footerSticky footerfixed']//button[@class='btn button django-form-submit gtm-lead-click apply_now_det_cd'][normalize-space()='Get Expert Help']"
    CollegeDtl_Dwnl_btn =   "//div[@class='CollegedekhoShareBtn_btnDownload__yOJ5w']//button[1]"
    CollegeDtl_dwnld_brchre_Btn = "//div[@class='CollegedekhoShareBtn_btnDownload__yOJ5w']//button[1]"
    CollegeDtl_apply_now_Btn = "//div[@class='ctaBox']/button"
    CollegeDtl_SubscribeNow_Btn = "//div[@class='box']/button"
    CollegeDtl_footer_sticky= "//div[@class = 'expertGraphic setExpertBlock']/div"






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

    def Collegedtl_foterform(self):

        footerform = self.driver.find_element(By.XPATH,self.CollegeDtl_footer_sticky)
        footerform.location_once_scrolled_into_view
        time.sleep(2)
        self.logger.info("Scrolled into footer form")
        time.sleep(4)

