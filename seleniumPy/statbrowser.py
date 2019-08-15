#!/user/bin/env python    
#   -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import  logging
from selenium.webdriver.support.wait import  WebDriverWait
from  selenium.webdriver.common.by import By
import  random
from  PIL import Image
from treeRequest.ShowapiRequest import ShowapiRequest
import  base64
from  time import  sleep

'''
启动不同浏览器
'''
driver = webdriver.Firefox()
# fdriver = webdriver.Firefox()
logging.info(u'启动谷歌浏览器驱动')
driver.get('http://www.5itest.cn/register')
#隐私等待5秒钟
driver.implicitly_wait(5)
#判断界面正常打开。标题是否包含
regiset = EC.title_contains('注册')

# emile = driver.find_element_by_id('register_email')
emiles = (By.ID,'register_email')
#判断元素在界面上是否展示(显示等待10秒钟 )
WebDriverWait(driver,10).until(EC.visibility_of_element_located(emiles))

email_element = driver.find_element_by_id('register_email')
#get_attribute()方法 ，获取 元素的属性，直接跟 属性的字段名
print(email_element.get_attribute('placeholder'))
email_element.send_keys('775283670@qq.com')
print(email_element.get_attribute('value'))
# uaser = driver.find_elements_by_class_name('controls')[1]
# uaser .find_element_by_class_name('form-control').send_keys('username')
# driver.find_element_by_name('password').send_keys('1213123')


#随机生成
for i in range(5):
    user_email =''.join(random.sample('qweqv312312fsfdsfs',5))+'@qq.com'
'''
关于获取验证码的操作：
1、先将网页保存为图片
2、定位验证码元素
3、打印验证码元素的坐标 location 方法
4、获取验证码图片的 整体坐标（根据元素的宽度和高度）
5、使用crop函数，进行剪裁，将上一步获取的坐标写入
6、在将剪裁的图片进行保存

'''
#验证码的操作【】
driver.save_screenshot('E:/imco.png')
code_element= driver.find_element_by_id('getcode_num')
#打印 验证码的坐标      location()打印坐标的方法
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] +left
hights = code_element.size['height'] +top
im=Image.open('E:/imco.png')
img=im.crop((left,top,right,hights))
img.save('E:/imco1.png')
'''
解析验证码图片
(使用的第三方的接口。需导入文件ShowapiRequest)
'''
r = ShowapiRequest("http://route.showapi.com/184-5","101951","eed0dc29616f4c72b545bdd9da6d3412" )
#因接口传入图片为base64 位的，需要在线转换下
with open('E:/imco1.png','rb') as fb:
    bData = base64.b64encode(fb.read())
r.addBodyPara("img_base64", bData)
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res =r.post()

text = res.json()["showapi_res_body"]["Result"]
driver.find_element_by_id('captcha_code').send_keys(text)
print('图片验证码：%s'%(text))

sleep(5)
driver.close()