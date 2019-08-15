#!/user/bin/env python    
#  -*- coding:utf-8 -*-
from  selenium import webdriver
from  util.read_ini import ReadIni
import time
'''

代码封装了获取ini文件的值的类
将数据取出为一字符串：id>register_email
使用spit('>')方法进行分割为list
list[0]:为id，就是用id定位的方法，将list[1]传入

第二次封装了关键在驱动的方法：

'''

class FindElement():

    def __init__(self,driver):
        self.driver = driver

    #封装element
    def get_element(self,key):
        read_ini =ReadIni()
        data = read_ini.get_value(key)
        by =data.split('>')[0]
        value = data.split('>')[1]
        try:

            if by == 'id':
                return  self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name ( value )
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_elements_by_xpath (value)
        except:
            times=time.strftime ( '%Y_%m_%d %H%-M%-S' )
            dir = '../screenshot/codeErro%s_%s.png'%(times)
            self.driver.save_screenshot(dir)
            return  None

# if __name__ == '__main__':
#     d = FindElement()
