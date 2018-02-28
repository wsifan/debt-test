import unittest
import json
import requests
from HTMLTestRunner import HTMLTestRunner
import time


#加载测试文件
from test_case import test_userlogin






#构造测试集
suit = unittest.TestSuite()


#TestSuite类的addTest()方法把不同测试类中的测试方法组装到测试套件中。
#增加测试用例==》接口文件名.接口类(方法也就是这个接口的其他用例),要把每一个测试用例都增加进来！！！
suit.addTest()





if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(suite)

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    filename = './' + now + 'test_result.html'
    fp = open(filename, "wb")

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="xxx接口测试报告",
                            description="测试用例执行情况：")

    # 运行测试
    runner.run(testunit)
    fp.close()  # 关闭文件对象把数据写进磁盘