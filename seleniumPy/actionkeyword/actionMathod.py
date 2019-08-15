#!/user/bin/env python    
# -*- coding:utf-8 -*-
'''
关键字驱动的总方法
'''
from  selenium import  webdriver
from  base.findElemen import  FindElement
from  time import sleep

class ActionMethod():
    def __init__(self):
        pass

    #定义打开浏览器的方法
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素[读取配置文件]
    def get_element(self,key):
        # print('key::::%s'%key)
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return  element



    #输入元素[根据定位元素的属性]
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        element = self.get_element(key)
        element.click()
    #等待
    def sleep_time(self):
        sleep(5)
    #关闭浏览器
    def close_drowser(self):
        self.driver.close()
    #获取title
    def get_title(self):
        title = self.driver.title
        return  title


if __name__ == '__main__':
    pass