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
