import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Xpath :
     #HomePage Xpaths
    Talk_to_experts = "//button[normalize-space()='Talk to our Experts'])[1]"
    Footer_Form = "//div[@class = 'expertGraphic setExpertBlock']/div"

    # def __init__(self, driver):
    #     self.driver = driver

    # def test_cta_homepage(self):
    #         Talk_experts = self.driver.find_element(By.XPATH,(self.Talk_to_experts))
    #         Talk_experts.location_once_scrolled_into_view
    #         time.sleep(2)

    #         Talk_experts.send_keys(Keys.PAGE_UP)
    #         self.logger.info("CTA : " + Talk_experts.text)
    #         Talk_experts.click()

    #         self.cta_detail()
    #         self.driver.back()
    #         self.driver.refresh()
    #         time.sleep(2)
