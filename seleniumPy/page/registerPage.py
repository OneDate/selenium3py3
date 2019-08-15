#!/user/bin/env python    
#-*- coding:utf-8 -*-
'''
定位元素
'''
from base.findElemen import FindElement
class ResgiterPage():
    def __init__(self,driver):
        self.fd = FindElement(driver)

    #定位邮箱元素
    def get_email_element(self):
        return self.fd.get_element('user_Email')

    #定位用户名元素
    def get_username_element(self):
        return self.fd.get_element('user_Name')
    #定位密码元素
    def get_password_element(self):
        return self.fd.get_element('user_Pwd')

    #定位验证码图片
    def get_code_image_element(self):
        return self.fd.get_element('code_image')
    #定位验证码输入框元素
    def get_code_element(self):
        return self.fd.get_element('code_text')
    #点位注册确定按钮
    def get_button_element(self):
        return  self.fd.get_element('register_Btn')

    #邮箱错误
    def get_email_error_element(self):
        return self.fd.get_element('user_email_error')
    #用户名错误
    def get_username_error_element(self):
        return self.fd.get_element('user_neme_error')
    #密码错误
    def get_password_error_element(self):
        return self.fd.get_element('register_password')
    #定位验证码错误
    def get_code_error_element(self):
        return self.fd.get_element('code_text_erro')