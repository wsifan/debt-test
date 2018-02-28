import unittest
import json
import requests
#from HTMLTestRunner import HTMLTestRunner
import time


#加载测试文件
from test_case import test_userlogin






#构造测试集
suite = unittest.TestSuite()


#TestSuite类的addTest()方法把不同测试类中的测试方法组装到测试套件中。
#增加测试用例==》接口文件名.接口类(方法也就是这个接口的其他用例),要把每一个测试用例都增加进来！！！
suite.addTest(test_userlogin.TestLogin('test_login_success'))
suite.addTest(test_userlogin.TestLogin('test_login_wrongpassword'))
suite.addTest(test_userlogin.TestLogin('test_login_usernotexist'))





if __name__ == "__main__":
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

