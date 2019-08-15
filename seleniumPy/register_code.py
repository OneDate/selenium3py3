#!/user/bin/env python    
#   -*- coding:utf-8 -*-
'''
注册的类。比较low的 代码
包含了，浏览器的初始化，定位element，获取随机数，截取验证码图片，
获取验证码文字，填入信息开始运行
'''
from selenium import webdriver
from time import sleep
import  random
from  PIL import Image
from treeRequest.ShowapiRequest import ShowapiRequest
import base64
import os

driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get('http://www.5itest.cn/register')
    driver.maximize_window()
    sleep(5)

#获取element信息
def get_element_id(id):
    element = driver.find_element_by_id(id)

    return element
#获取随机数
def get_range_user():
    user_email =''.join(random.sample('qweqv312312fsfdsfs',8))
    return user_email
#获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot (file_name)
    code_element=driver.find_element_by_id ( 'getcode_num' )
    left=code_element.location['x']
    top=code_element.location['y']
    right=code_element.size['width'] + left
    hights=code_element.size['height'] + top
    im=Image.open (file_name )
    img=im.crop ( (left , top , right , hights) )
    img.save (file_name )
#解析验证码图片，获取验证码
def code_online(file_name):
    print(file_name)
    r = ShowapiRequest ( url="http://route.showapi.com/184-5" , my_appId="101951" , my_appSecret="eed0dc29616f4c72b545bdd9da6d3412" )
    with open ( file_name , 'rb' ) as fb:
        bData=base64.b64encode ( fb.read () )
    r.addBodyPara("img_base64" , bData )
    r.addBodyPara("typeId" , "35" )
    r.addBodyPara("convert_to_jpg" , "0" )
    r.addBodyPara("needMorePrecise" , "0" )
    res=r.post ()
    text=res.json ()["showapi_res_body"]["Result"]
    print(text)
    return text

def run_main():
    userName = get_range_user()
    userEmail = userName +'@qq.com'
    file_name = os.path.dirname(os.path.dirname(__file__))+'/selenium3+python3/images/test01.png'
    driver_init()
    get_element_id('register_email').send_keys(userEmail)
    get_element_id('register_nickname').send_keys(userName)
    get_element_id('register_password').send_keys('111111')
    get_code_image(file_name)
    text = code_online(file_name)

    get_element_id ( 'captcha_code' ).send_keys ( text )

    sleep(5)
    driver.close()
if __name__ == '__main__':
    run_main()