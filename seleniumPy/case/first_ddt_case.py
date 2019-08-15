#!/user/bin/env python    
#   -*- coding:utf-8 -*-
'''
数据驱动的类，包含：
邮箱、用户名、密码、验证码。错误信息定位元素，错误提示信息
'''
import ddt
import  unittest
from business.register_business import RegisterBusiness
from  selenium import  webdriver
import unittest
import HTMLTestRunner
import logging
from  BSTestRunner import BSTestRunner
import os
import time
from  util.excel_util import  ExcelUtil

ex =ExcelUtil()
data = ex.getValues()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome ()
        self.driver.get ( 'http://www.5itest.cn/register' )
        self.rBusiness=RegisterBusiness ( self.driver )

    def tearDown(self):
        # time.sleep(5)
        self.driver.close ()
    # ["775283670@qq.com","http://www.5itest.cn/register","1qaz2wsx","code","user_name_error","字符长度必须小于等于18，一个中文字算2个字符"],
    # ["770@qq.com","OneDate","1qaz2wsx","code","user_name_error","验证码错误"]

    '''
     
     @ddt.data(
            ["12","123123","666666","code","user_email_error","请输入有效的电子邮件地址"]
    )
    解包，数据长度要一致
    @ddt.unpack
    def test_register_error(self,email,username,password,code,asssertCode,assertText):
        error = self.rBusiness.register_function(email,username,password,code,asssertCode,assertText)
        logging.info ( '用例被运行了' )
        self.assertFalse(error,'测试失败')
     
     '''
    #excle 表 取数据的形式 使用方式
    @ddt.data(*data)
    def test_register_error(self,data):
        email , username , password , code , asssertCode , assertText =data
        error = self.rBusiness.register_function(email,username,password,code,asssertCode,assertText)
        logging.info ( '用例被运行了' )
        self.assertFalse(error,'测试失败')
if __name__ == '__main__':
    # unittest.main()
    filePath = "D:\\untitled\\seleniumPy\\report\\first_case1.html"
    suit = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)

    with open(filePath,'wb') as fb :
        logging.info('报告被运行了吗')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fb,verbosity=1,title=u'测试报告哈',description=u'这是内容selenium3+python3+po+ddt')
        runner.run(suit)