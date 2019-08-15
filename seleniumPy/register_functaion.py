#!/user/bin/env python    
# -*- coding:utf-8 -*-
'''
封装第一次的代码。
'''
from selenium import webdriver
from time import sleep
import  random
from  PIL import Image
from treeRequest.ShowapiRequest import ShowapiRequest
import base64
import os
from base.findElemen import  FindElement
import  time
'''
将定位元素和输入数据元素结合起来
定位了一些 方法（截图、获取当前时间）

'''

class RegisterFunction():

    def __init__(self,url,i):
        self.driver =self.get_driver(url,i)

    #获取driver，并打开url
    def get_driver(self,url):
        if i == 1:
            driver=webdriver.Chrome ()
        elif i == 2:
            driver= webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息(get_user_element方法已经定位到了元素位置，data为输入的元素信息)
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #定位用户信息获取element【 key 为定位元素的 值，可以为id或name。FindElement类里面已经判断了】
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_email=''.join ( random.sample ( 'qweqv312312fsfdsfs' , 8 ) )
        return user_email

    # 获取验证码图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot ( file_name )
        code_element=self.get_user_element('code_image')
        left=code_element.location['x']
        top=code_element.location['y']
        right=code_element.size['width'] + left
        hights=code_element.size['height'] + top
        im=Image.open ( file_name )
        img=im.crop ( (left , top , right , hights) )
        img.save ( file_name )

    # 解析验证码图片，获取验证码
    def code_online(self,file_name):
        print ( file_name )
        self.get_code_image(file_name)
        r=ShowapiRequest ( url="http://route.showapi.com/184-5" , my_appId="101951" ,
                           my_appSecret="eed0dc29616f4c72b545bdd9da6d3412" )
        with open ( file_name , 'rb' ) as fb:
            bData=base64.b64encode ( fb.read () )
        r.addBodyPara ( "img_base64" , bData )
        r.addBodyPara ( "typeId" , "35" )
        r.addBodyPara ( "convert_to_jpg" , "0" )
        r.addBodyPara ( "needMorePrecise" , "0" )
        res=r.post ()
        text=res.json ()["showapi_res_body"]["Result"]
        print ( text )
        return text

    #截图的方法
    def get_screenshot(self,mokuai):
        times = time.strftime('%Y_%m_%d %H%-M%-S')
        dir = '../screenshot/codeErro%s_%s.png'%(mokuai,times)
        self.driver.save_screenshot(dir)
    def run_main(self):
        userName=self.get_range_user ()
        userEmail=userName + '@qq.com'
        file_name=os.path.dirname ( os.path.dirname ( __file__ ) ) + '/selenium3+python3/images/test01.png'
        code_text =self.code_online(file_name)
        self.send_user_info('user_Email',userEmail)
        self.send_user_info('user_Name',userName)
        self.send_user_info('user_Pwd','11111')
        self.send_user_info('code_text',code_text)
        self.send_user_info('register_Btn').click()
        code_erro =  self.get_user_element('code_text_erro')

        #注册是否成功判断
        if code_erro == None:
            print('注册成功')
        else:
            print('注册失败')

            self.driver.save_screenshot('../screenshot/codeErro.png')
        sleep(5)
        self.driver.close()



if __name__ == '__main__':
    for i in range(3):
        r = RegisterFunction('http://www.5itest.cn/register',i)
        r.run_main()