#!/user/bin/env python    
#   -*- coding:utf-8 -*-
import configparser
class ReadIni(object):

    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name="D:/untitled/seleniumPy/config/localConfig.ini"

        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    #加载ini文件
    def load_ini(self,file_name):
        cf=configparser.ConfigParser ()
        cf.read(file_name)
        return  cf

    #获取 value值
    def get_value(self,key):
        value = self.cf.get ( self.node , key)
        # print(value)
        return  value


if __name__ == '__main__':
    r = ReadIni()
    r.get_value('user_Name' )

