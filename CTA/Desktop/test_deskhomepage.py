import time
from logs import *
from common_configration import *
from conftest import *
from utilities.Baseclass import *



class Login(logs,Baseclass):
    def test_login(self):
        self.test_log()             #log steup
        window_size = self.driver.get_window_size() #Get Home screen window size
        self.logger.info(window_size)
        time.sleep(20)
        