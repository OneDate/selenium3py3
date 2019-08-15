#!/user/bin/env python    
#-*- coding:utf-8 -*-
'''
业务层
'''
from handle.register_handle import RegisterHandle
class  RegisterBusiness():

    def __init__(self,driver):
        self.rHandle = RegisterHandle(driver)

    def send_data(self , email , username , passwword , code):
        self.rHandle.send_user_email ( email )
        self.rHandle.send_user_name ( username )
        self.rHandle.send_user_password ( passwword )
        self.rHandle.send_user_code ( code )
        self.rHandle.click_regster_button ()
        # self.register_success()

    def register_success(self):
        return self.rHandle.click_regster_button ().text()

    #ddt 数据驱动使用的方法 [使用总方法] 其他的方法都可以不使用
    def register_function(self,email,username,password,code,asssertCode,assertText):
        self.send_data(email,username,password,code)
        if self.rHandle.get_user_text_error(asssertCode,assertText) == None:
            # print('邮箱验证不成功')
            # 等于 none  说明错误的提示没有出现，正确的
            return True
        else:
            return False

    #执行操作
    def register_email_erro(self,email,username,passwword,code):
        self.send_data(email,username,passwword,code)

        if self.rHandle.get_user_text('user_email_error','请输入有效的电子邮件地址') == None:
            print('邮箱验证不成功')
            return True
        else:
            return False
    def register_username_error(self,email,username,passwword,code):
        self.send_data(email,username,passwword,code)

        if self.rHandle.get_user_text ( 'user_neme_error' , '字符长度必须小于等于18，一个中文字算2个字符' ) == None:
            print ( '邮箱验证不成功' )
            return True
        else:
            return False

    def register_password_error(self,email,username,passwword,code):
        self.send_data(email,username,passwword,code)

        if self.rHandle.get_user_text ( 'user_password_error' , '最多只能输入 20 个字符' ) == None:
            print ( '邮箱验证不成功' )
            return True
        else:
            return False

    def register_code_error(self,email,username,passwword,code):
        self.send_data(email,username,passwword,code)

        if self.rHandle.get_user_text ( 'code_text_erro' , '验证码错误' ) == None:
            print ( '邮箱验证不成功' )
            return True
        else:
            return False