import pytest
from pageObjects.common_configuration import Cta

from testCases.test_deskhomepage import Test_deskhomepage
from testCases.test_examdetail1 import Test_ExamDetail2

class Test_allsuites:
    def __init__(self):



#Get All Tests from Signup,Login,LOgin OTP 
        TC1_HomePage = pytest.TestLoader().loadTestsFromTestCase(Test_deskhomepage)
        TC2_ExamDetail = pytest.TestLoader().loadTestsFromTestCase(Test_ExamDetail2)
        # TC3_LoginOtp = pytest.TestLoader().loadTestsFromTestCase(checkloginotp)

        #Creating Test Suites acc to Sanity,Masters,Functionality

        AllTestCases = pytest.TestSuite([TC1_HomePage,TC2_ExamDetail])
        pytest.TextTestRunner().run(AllTestCases)
