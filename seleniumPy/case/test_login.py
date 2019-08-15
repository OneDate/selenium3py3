#!/user/bin/env python    
#-*- coding:utf-8 -*-
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        print ( '登录用例开始执行' )

    def tearDown(self):
        print ( '登录用例执行结束' )

    def testL01(self):
        print ( '第一条登录用例' )

    def testL02(self):
        print ( '第二条登录用例' )

    def testL03(self):
        print ( '第三条登录用例' )
if __name__ == '__main__':
    unittest.main()