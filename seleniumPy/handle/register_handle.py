#!/user/bin/env python    
#-*- coding:utf-8 -*-
'''
输入数据元素
'''
from page.registerPage import  ResgiterPage
class RegisterHandle():

    def __init__(self,driver):
        self.rPage = ResgiterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.rPage.get_email_element().send_keys(email)
    #输入用户名
    def send_user_name(self,username):
        self.rPage.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self,password):
        self.rPage.get_password_element().send_keys(password)

    # 输入验证码图片
    def send_user_code_image(self):
        self.rPage.get_code_image_element()

    # 输入验证码
    def send_user_code(self,code ):
        self.rPage.get_code_element ().send_keys(code)



    # 获取提示语的文字信息：
    def get_user_text_error(self,info,strToast):
        textinfo = None
        if info =='user_email_error':
            textinfo = self.rPage.get_email_error_element().text
        elif info == 'user_neme_error':
            textinfo = self.rPage.get_username_error_element().text
        elif info == 'user_password_error':
            textinfo =self.rPage.get_password_error_element().text
        elif info == 'code_text_erro':
            textinfo = self.rPage.get_code_error_element ().text

        return  textinfo

    #点击注册按钮
    def click_regster_button(self):
        self.rPage.get_button_element().click()