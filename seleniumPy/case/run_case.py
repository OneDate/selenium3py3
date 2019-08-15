#!/user/bin/env python    
#-*- coding:utf-8 -*-
import unittest
import os

class RunClass(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.dirname(os.path.dirname(__file__))
        # case_path = os.path.join(os.getcwd(),'case')
        suit = unittest.defaultTestLoader.discover(case_path,'test*.py')
        unittest.TextTestRunner().run(suit)
if __name__ == '__main__':
    unittest.main()