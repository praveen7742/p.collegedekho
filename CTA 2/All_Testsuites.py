import unittest

from testCases.test_deskhomepage import Test_deskhomepage
from testCases.test_examdetail1 import Test_ExamDetail2
#from testCases.test_examlisting import Test_examlisting


#Get All Tests from Signup,Login,LOgin OTP 
TC1_HomePage = unittest.TestLoader().loadTestsFromTestCase(Test_deskhomepage)
TC2_ExamDetail = unittest.TestLoader().loadTestsFromTestCase(Test_ExamDetail2)

#Creating Test Suites acc to Sanity,Masters,Functionality

AllTestCases = unittest.TestSuite([TC1_HomePage,TC2_ExamDetail])
unittest.TextTestRunner().run(AllTestCases)