#!/user/bin/env python    
#-*- coding:utf-8 -*-
import unittest

class TestRegister(unittest.TestCase):
    def setUp(self):
        print('注册用例开始执行')
    def tearDown(self):
        print('注册用例执行结束')
    def testR01(self):
        print('第一条注册用例')
    def testR02(self):
        print('第二条注册用例')
    def testR03(self):
        print('第三条注册用例')
if __name__ == '__main__':
    unittest.main()