# coding=utf-8
'''
Created on 2018-1-29
@author: zhangxu
Project:登录测试用例
'''


import unittest
import requests
import json



class Mytest(unittest.TestCase):   #封装测试环境的初始化和还原的类
    def setUp(self):                   #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass


class TestLogin(Mytest):

    def test_login_success(self):   #验证成功登录
        self.url = "http://192.168.8.197:8000/user/login"
        self.data = {
            "username": "apple",  # 用户名
            "password": "apple",  # 密码
        }
        r = requests.post(url = self.url,json = self.data)
        print(r.text)
        print(r.status_code)
        self.assertIn("SUCCESS", r.text)  # 断言判断接口返回是否符合要求，可以写多个断言！

    def test_login_wrongpassword(self):  #密码错误
        self.url = "http://192.168.8.197:8000/user/login"
        self.data = {
            "username": "apple",  # 用户名
            "password": "apple1",  # 密码
        }
        r = requests.post(url=self.url, json=self.data)
        print(r.text)
        print(r.status_code)
        self.assertIn("2001", r.text)  # 断言判断接口返回是否符合要求，可以写多个断言！

    def test_login_usernotexist(self):  #用户不存在
        self.url = "http://192.168.8.197:8000/user/login"
        self.data = {
            "username": "apple11",  # 用户名
            "password": "apple1",  # 密码
        }
        r = requests.post(url=self.url, json=self.data)
        print(r.text)
        print(r.status_code)
        self.assertIn("2000", r.text)  # 断言判断接口返回是否符合要求，可以写多个断言！



if __name__=="__main__":
    unittest.main()