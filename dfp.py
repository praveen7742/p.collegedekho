from selenium import webdriver 
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--headless") 
#driver = webdriver.Chrome(options=chrome_options)  
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)


class dfp(unittest.TestCase):   
    
    def test_dfpnews(self):
        
        self.driver = driver
        driver.maximize_window()
        driver.get("https:www.collegedekho.com/news?magicflag=1")
        print("----------------------------------------------News Listing---------------------------------")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_College_NEWS_Home_Page_Header_LeaderBoard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()
        

    def test_dfpstream(self):
        self.driver = driver
        driver.maximize_window()
        driver.get("https://www.collegedekho.com/engineering-stream/?magicflag=1")
        print("----------------------------------------------Stream ---------------------------------")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_Stream_Template_Leaderboard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpcourses(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------Course Listing---------------------------------")
        driver.get("https://www.collegedekho.com/courses/?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_Course_Listing_Leaderboard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpcoursesdetail(self):
        self.driver = driver
        driver.maximize_window()
        print("--------------------------------Course Detail------------------------------------------")
        time.sleep(2)
        driver.get("https://www.collegedekho.com/courses/btech/?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_Course_Detail_Leaderboard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpexamlisting(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------Exam Listing---------------------------------")
        driver.get("https://www.collegedekho.com/test-preparation/?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_Home_Exam_Listing_Leaderboard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpQnalisting(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------Qna Listing---------------------------------")
        driver.get("https://www.collegedekho.com/qna/?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_College_QNA_Header_LeaderBoard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpQnadetail(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------Qna Detail---------------------------------")
        driver.get("https://www.collegedekho.com/qna/i-want-to-know-about-the-eligibility-requirements-for-pursuing-btech-at-alliance-university")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_College_QNA_Detail_Header_LeaderBoard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)

    def test_dfpcollegelisting(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------College Lising---------------------------------")
        driver.get("https://www.collegedekho.com/colleges-in-india/?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_College_List_Page_Body1_LeaderBoard_0")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def test_dfpcollegedetail(self):
        self.driver = driver
        driver.maximize_window()
        print("----------------------------------------------College Detail---------------------------------")
        driver.get("https://www.collegedekho.com/colleges/iima?magicflag=1")
        print("current url = " + driver.current_url)
        print("current title = " + driver.title)
        frames = driver.find_elements_by_tag_name("iframe")
        print("There are ", len(frames),"frames on this webpage") 
        for f in frames:
            print("frame ID:", f.get_attribute('id'), "frame Name:", f.get_attribute('name'), "frame width:", f.get_attribute('width'),
            "frame height:", f.get_attribute('height'))
        elm = driver.find_element_by_id("google_ads_iframe_/99910373/CLD_College_Detail_Overview_Page_Header_Leaderboard_0__container__")
        elm.click()
        time.sleep(5)
        childwindow = driver.window_handles[1]
        driver.switch_to_window(childwindow)
        print("current url =" + driver.current_url)
        print("current title = " + driver.title)
        parentwindow = driver.window_handles[0]
        driver.switch_to_window(parentwindow)
        driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
