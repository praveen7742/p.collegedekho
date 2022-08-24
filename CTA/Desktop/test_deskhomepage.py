import time
from logs import *
from common_configration import *
from conftest import *
from database import *
from utilities.Baseclass import *



class Login(Baseclass,Database,logs):
    def test_login(self):
        self.test_log()             #log steup
        window_size = self.driver.get_window_size() #Get Home screen window size
        self.logger.info(window_size)
        time.sleep(2)
        self.test_database()
        time.sleep(2)
        
