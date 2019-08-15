#!/user/bin/env python    
#       -*- coding:utf-8 -*-
import base64

from treeRequest import ShowapiRequest
import os
'''
识别 图片中的数字

'''



# text = pytesseract.image_to_string(image)

# print(text)
def get_text(image):
    r = ShowapiRequest ( "http://route.showapi.com/184-5" , "101951" , "eed0dc29616f4c72b545bdd9da6d3412" )
    with open(image,'rb') as fb:
        bData = base64.b64encode(fb.read())
    r.addBodyPara("img_base64", bData)
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res =r.post()

    text = res.json()["showapi_res_body"]["Result"]
    print(text)
    return text
if __name__ == '__main__':

    image = os.path.dirname(os.path.dirname(__file__))+'/selenium3+python3/images/test01.png'
    print(os.path.dirname(os.path.dirname(__file__)))

    i = get_text(image)
