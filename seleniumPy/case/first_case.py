#!/user/bin/env python    
#   -*- coding:utf-8 -*-
from business.register_business import RegisterBusiness
from  selenium import  webdriver
import unittest
from logsss.register_log import UserLog
import HTMLTestRunner
import os

class FirstCase(unittest.TestCase):

    #装饰器 ：@classmethod :所有case执行之前都会执行.只会被执行一次
    @classmethod
    def setUpClass(cls):
        cls.log=UserLog ()
        cls.logger=cls.log.get_log ()

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Wancheng')
        cls.log.close_handle ()

    def setUp(self):
        self.driver =webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')

        self.logger.debug ( "asdasdasd a" )


        self.rBusiness = RegisterBusiness(self.driver)


    def tearDown(self):

        self.driver.close()

    def test_login_emil_erro(self):
        emali_error = self.rBusiness.register_email_erro('email','username','password','code')
        self.assertFalse(emali_error)
    #     # if emali_error ==True:
    #     #     print('注册失败')
    # def test_login_username_erro(self):
    #     username_error=self.rBusiness.register_username_error ( 'email' , 'username1' , 'password' , 'code' )
    #     self.assertFalse ( username_error )
    #     # if username_error == True:
    #     #     print ( '注册失败,用户名错误' )
    # def test_login_password_erro(self):
    #     password_error=self.rBusiness.register_password_error ( 'email' , 'username2' , 'password' , 'code' )
    #     self.assertFalse ( password_error )
    #     # if password_error == True:
    #     #     print ( '注册失败,密码错误' )
    # @unittest.skip('不执行这一条')
    # def test_login_succes(self):
    #     if self.rBusiness.register_success() == None:
    #         print('注册成功')
    # def run_main(self):
    #     self.test_login_emil_erro()
    #     self.test_login_password_erro()
    #     self.test_login_username_erro()
    #     self.test_login_succes()
if __name__ == '__main__':
    # r =FirstCase()
    # r.run_main()
    # suit = unittest.TestSuite()
    # suit.addTest(FirstCase('test_login_emil_erro'))
    # file = '../report/fasrt01.html'
    # with open(file,'wb') as fb :
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fb,title='测试报告',description='内容')
    # runner.run(suit)
    unittest.main()