import pytest
from pageObjects.common_configuration import Cta

from testCases.test_deskhomepage import Test_deskhomepage
from testCases.test_examdetail1 import Test_ExamDetail2
from testCases.test_careercta import Test_Career
from testCases.test_examlisting import Test_examlisting
from testCases.test_careercta import Test_Career

class Test_allsuites:
    def __init__(self):

        TC1_HomePage = pytest.TestLoader().loadTestsFromTestCase(Test_deskhomepage)
        TC2_ExamDetail = pytest.TestLoader().loadTestsFromTestCase(Test_ExamDetail2)
        TC3_CareerDetail = pytest.TestLoader().loadTestsFromTestCase(Test_Career)
        TC4_ExamListing = pytest.TestLoader().loadTestsFromTestCase(Test_examlisting)


        #Creating Test Suites acc to Sanity,Masters,Functionality

        AllTestCases = pytest.TestSuite([TC1_HomePage,TC2_ExamDetail,TC3_CareerDetail,TC4_ExamListing])
        pytest.TextTestRunner().run(AllTestCases)
